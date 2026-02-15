"""Failover logic for the Smart AI Router."""

import time
from typing import List, Callable, Any, Optional
from .exceptions import RateLimitException, ModelNotAvailableException, AllModelsFailedException


class FailoverHandler:
    """Handles automatic failover between models."""
    
    def __init__(self, models: List[str], retry_delay: float = 1.0):
        """
        Initialize the failover handler.
        
        Args:
            models: List of model names to try in order
            retry_delay: Delay in seconds between retries
        """
        self.models = models
        self.retry_delay = retry_delay
        self.last_error = None
        
    def execute_with_failover(
        self,
        func: Callable,
        *args,
        **kwargs
    ) -> Any:
        """
        Execute a function with automatic failover.
        
        Args:
            func: The function to execute
            *args: Positional arguments for the function
            **kwargs: Keyword arguments for the function
            
        Returns:
            The result of the function call
            
        Raises:
            AllModelsFailedException: If all models fail
        """
        errors = []
        
        for i, model in enumerate(self.models):
            try:
                # Update the model in kwargs
                kwargs["model"] = model
                
                # Try to execute the function
                result = func(*args, **kwargs)
                
                # If successful, return the result
                return result
                
            except Exception as e:
                error_msg = str(e)
                errors.append({
                    "model": model,
                    "error": error_msg
                })
                
                # Check if this is a rate limit error
                if self._is_rate_limit_error(error_msg):
                    self.last_error = RateLimitException(
                        f"Rate limit hit for model {model}: {error_msg}"
                    )
                else:
                    self.last_error = ModelNotAvailableException(
                        f"Model {model} failed: {error_msg}"
                    )
                
                # If this is not the last model, wait before trying the next one
                if i < len(self.models) - 1:
                    time.sleep(self.retry_delay)
                    
        # All models failed
        raise AllModelsFailedException(
            f"All {len(self.models)} models failed. Errors: {errors}"
        )
    
    def _is_rate_limit_error(self, error_msg: str) -> bool:
        """
        Check if an error message indicates a rate limit.
        
        Args:
            error_msg: The error message to check
            
        Returns:
            True if the error is a rate limit error
        """
        rate_limit_indicators = [
            "rate limit",
            "rate_limit",
            "too many requests",
            "429",
            "quota exceeded",
            "requests per minute"
        ]
        
        error_lower = error_msg.lower()
        return any(indicator in error_lower for indicator in rate_limit_indicators)
