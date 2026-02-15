"""Core SmartRouter class for intelligent multi-model routing."""

import os
import json
from typing import Optional, Dict, List, Any
from pathlib import Path
import openai
from openai import OpenAI

from .cost_tracker import CostTracker
from .failover import FailoverHandler
from .exceptions import SmartRouterException


class SmartRouter:
    """
    Intelligent AI router with automatic failover and cost tracking.
    
    This class wraps the OpenAI client and provides intelligent routing
    across multiple models with automatic failover, rate limit handling,
    and cost tracking.
    """
    
    def __init__(
        self,
        api_key: Optional[str] = None,
        preset: Optional[str] = None,
        config: Optional[Dict] = None,
        base_url: str = "https://openrouter.ai/api/v1",
        retry_delay: float = 1.0,
        track_costs: bool = True
    ):
        """
        Initialize the SmartRouter.
        
        Args:
            api_key: OpenRouter API key (defaults to OPENROUTER_API_KEY env var)
            preset: Name of a preset configuration to load
            config: Custom configuration dictionary
            base_url: Base URL for the API
            retry_delay: Delay in seconds between failover retries
            track_costs: Whether to track costs
        """
        # Get API key
        self.api_key = api_key or os.environ.get("OPENROUTER_API_KEY")
        if not self.api_key:
            raise SmartRouterException(
                "API key must be provided or set in OPENROUTER_API_KEY environment variable"
            )
        
        # Initialize OpenAI client
        self.client = OpenAI(
            base_url=base_url,
            api_key=self.api_key
        )
        
        # Load configuration
        if preset:
            self.config = self._load_preset(preset)
        elif config:
            self.config = config
        else:
            raise SmartRouterException(
                "Either 'preset' or 'config' must be provided"
            )
        
        # Extract models from config
        self.primary_model = self.config.get("model")
        self.fallback_models = self.config.get("models", [])
        
        # Create full model list (primary + fallbacks)
        self.models = [self.primary_model] + self.fallback_models
        
        # Initialize failover handler
        self.failover_handler = FailoverHandler(
            models=self.models,
            retry_delay=retry_delay
        )
        
        # Initialize cost tracker
        self.track_costs = track_costs
        if track_costs:
            self.cost_tracker = CostTracker()
        
        # Store other config options
        self.temperature = self.config.get("temperature", 0.7)
        self.provider_config = self.config.get("provider", {})
        
    def _load_preset(self, preset_name: str) -> Dict:
        """
        Load a preset configuration from the presets directory.
        
        Args:
            preset_name: Name of the preset (without .json extension)
            
        Returns:
            Configuration dictionary
        """
        # Try multiple possible locations
        possible_paths = [
            Path(__file__).parent.parent / "presets" / f"{preset_name}.json",
            Path.cwd() / "presets" / f"{preset_name}.json",
            Path.home() / ".smart-ai-router" / "presets" / f"{preset_name}.json"
        ]
        
        for preset_path in possible_paths:
            if preset_path.exists():
                with open(preset_path, "r") as f:
                    return json.load(f)
        
        raise SmartRouterException(
            f"Preset '{preset_name}' not found in any of: {[str(p) for p in possible_paths]}"
        )
    
    @property
    def chat(self):
        """Access to chat completions with failover."""
        return ChatCompletions(self)
    
    def get_cost_summary(self) -> Dict:
        """
        Get a summary of costs.
        
        Returns:
            Dictionary containing cost summary
        """
        if not self.track_costs:
            return {"message": "Cost tracking is disabled"}
        
        return self.cost_tracker.get_summary()
    
    def reset_costs(self):
        """Reset the cost tracker."""
        if self.track_costs:
            self.cost_tracker.reset()


class ChatCompletions:
    """Chat completions with automatic failover."""
    
    def __init__(self, router: SmartRouter):
        """
        Initialize chat completions.
        
        Args:
            router: The parent SmartRouter instance
        """
        self.router = router
        
    def create(
        self,
        messages: List[Dict[str, str]],
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        **kwargs
    ):
        """
        Create a chat completion with automatic failover.
        
        Args:
            messages: List of message dictionaries
            temperature: Sampling temperature (overrides config)
            max_tokens: Maximum tokens to generate
            **kwargs: Additional arguments to pass to the API
            
        Returns:
            Chat completion response
        """
        # Use temperature from config if not specified
        if temperature is None:
            temperature = self.router.temperature
        
        # Define the API call function
        def api_call(model: str):
            return self.router.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
                **kwargs
            )
        
        # Execute with failover
        response = self.router.failover_handler.execute_with_failover(api_call)
        
        # Track costs if enabled
        if self.router.track_costs and hasattr(response, "usage"):
            self.router.cost_tracker.track_request(
                model_name=response.model,
                input_tokens=response.usage.prompt_tokens,
                output_tokens=response.usage.completion_tokens
            )
        
        return response
