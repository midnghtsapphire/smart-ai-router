"""Model definitions and metadata for the Smart AI Router."""

# Model pricing information (per million tokens)
MODEL_PRICING = {
    # Premium Models
    "anthropic/claude-opus-4.6": {"input": 15.0, "output": 75.0},
    "anthropic/claude-sonnet-4.5": {"input": 3.0, "output": 15.0},
    "anthropic/claude-haiku-4.5": {"input": 0.8, "output": 4.0},
    "openai/gpt-5.2-codex": {"input": 10.0, "output": 30.0},
    
    # Cost-Effective Models
    "deepseek/deepseek-v3.2": {"input": 0.25, "output": 0.38},
    "deepseek/deepseek-chat-v3-0324": {"input": 0.25, "output": 0.38},
    
    # Grok Models (X.AI)
    "x-ai/grok-code-fast-1": {"input": 0.20, "output": 0.20},
    "x-ai/grok-4.1-fast": {"input": 0.50, "output": 1.00},
    "x-ai/grok-3-mini": {"input": 0.001, "output": 0.001},
    
    # Google Models
    "google/gemini-2.5-pro-preview": {"input": 1.25, "output": 5.0},
    
    # Qwen Models
    "qwen/qwen3-235b-a22b": {"input": 0.80, "output": 0.80},
    
    # Moonshot Models
    "moonshot/kimi-k2": {"input": 0.30, "output": 0.30},
    
    # Free Models
    "deepseek/deepseek-v3.2:free": {"input": 0.0, "output": 0.0},
    "arcee-ai/trinity-large-preview:free": {"input": 0.0, "output": 0.0},
    "arcee-ai/mimo-v2-flash:free": {"input": 0.0, "output": 0.0},
    "cognitivecomputations/dolphin-mistral-24b-venice-edition:free": {"input": 0.0, "output": 0.0},
    "qwen/qwen-3-coder:free": {"input": 0.0, "output": 0.0},
    "qwen/qwen-3-coder-480b-a35b-instruct:free": {"input": 0.0, "output": 0.0},
    "step/step-3.5-flash:free": {"input": 0.0, "output": 0.0},
    "nothingiisreal/nemo-12b": {"input": 0.0, "output": 0.0},
    "meta-llama/llama-3.3-70b-instruct:free": {"input": 0.0, "output": 0.0},
    "nousresearch/hermes-3-llama-3.1-405b:free": {"input": 0.0, "output": 0.0},
    "openai/gpt-oss-120b:free": {"input": 0.0, "output": 0.0},
}

# Model capabilities and use cases
MODEL_CAPABILITIES = {
    "anthropic/claude-opus-4.6": {
        "use_cases": ["framework-development", "complex-reasoning", "code-generation", "agentic-tasks"],
        "strengths": ["sustained reasoning", "multi-step workflows", "complex ideation"],
    },
    "anthropic/claude-sonnet-4.5": {
        "use_cases": ["code-review", "coding-workflows", "tool-orchestration"],
        "strengths": ["SWE-bench performance", "code security", "fast response"],
    },
    "anthropic/claude-haiku-4.5": {
        "use_cases": ["quick-tasks", "simple-queries"],
        "strengths": ["speed", "cost-efficiency"],
    },
    "openai/gpt-5.2-codex": {
        "use_cases": ["code-generation", "debugging"],
        "strengths": ["code understanding", "multi-language support"],
    },
    "deepseek/deepseek-v3.2": {
        "use_cases": ["code-review", "coding-tasks", "cost-effective-development"],
        "strengths": ["90% GPT-5.1 performance", "1/50th cost", "coding excellence"],
    },
    "deepseek/deepseek-v3.2:free": {
        "use_cases": ["code-review", "coding-tasks", "derivative-apps"],
        "strengths": ["free tier", "excellent coding", "cost optimization"],
    },
    "deepseek/deepseek-chat-v3-0324": {
        "use_cases": ["code-review", "coding-tasks", "brainstorming"],
        "strengths": ["similar to v3.2", "coding + reasoning", "cost-effective"],
    },
    "x-ai/grok-code-fast-1": {
        "use_cases": ["fast-iteration", "rapid-prototyping", "code-generation"],
        "strengths": ["190 tok/sec", "ultra-fast", "low latency"],
    },
    "x-ai/grok-4.1-fast": {
        "use_cases": ["agentic-tasks", "autonomous-agents", "production-testing"],
        "strengths": ["agentic specialization", "tool use", "fast reasoning"],
    },
    "x-ai/grok-3-mini": {
        "use_cases": ["cost-effective-tasks", "brainstorming", "code-review"],
        "strengths": ["extremely low cost", "fast", "good quality"],
    },
    "google/gemini-2.5-pro-preview": {
        "use_cases": ["detailed-analysis", "verbose-output", "multilingual", "agentic-tasks"],
        "strengths": ["most verbose", "detailed planning", "strong multilingual"],
    },
    "qwen/qwen3-235b-a22b": {
        "use_cases": ["brainstorming", "multilingual", "reasoning", "agentic-tasks"],
        "strengths": ["strong reasoning", "excellent Chinese/multilingual", "large context"],
    },
    "moonshot/kimi-k2": {
        "use_cases": ["multilingual", "Chinese-language", "brainstorming"],
        "strengths": ["Chinese language model", "strong performance", "multilingual"],
    },
    "arcee-ai/trinity-large-preview:free": {
        "use_cases": ["creative-writing", "storytelling", "role-play"],
        "strengths": ["400B parameters", "creative excellence", "agentic workflows"],
    },
    "arcee-ai/mimo-v2-flash:free": {
        "use_cases": ["creative-ideation", "free-first-stack", "uncensored"],
        "strengths": ["free tier", "fast", "creative"],
    },
    "cognitivecomputations/dolphin-mistral-24b-venice-edition:free": {
        "use_cases": ["creative-ideation", "unrestricted-use-cases", "uncensored"],
        "strengths": ["uncensored", "strong steerability", "free tier"],
    },
    "qwen/qwen-3-coder:free": {
        "use_cases": ["code-generation", "function-calling"],
        "strengths": ["MoE architecture", "long-context reasoning", "free tier"],
    },
    "qwen/qwen-3-coder-480b-a35b-instruct:free": {
        "use_cases": ["code-generation", "function-calling", "repository-reasoning"],
        "strengths": ["MoE architecture", "long-context", "free tier"],
    },
    "step/step-3.5-flash:free": {
        "use_cases": ["general-tasks", "long-context"],
        "strengths": ["MoE architecture", "speed-efficient", "free tier"],
    },
    "nothingiisreal/nemo-12b": {
        "use_cases": ["creative-writing", "uncensored"],
        "strengths": ["Reddit Writing Prompts training", "active narration"],
    },
    "meta-llama/llama-3.3-70b-instruct:free": {
        "use_cases": ["fast-iteration", "brainstorming", "code-review", "creative-ideation"],
        "strengths": ["fastest free model", "31.8s response", "excellent quality"],
    },
    "nousresearch/hermes-3-llama-3.1-405b:free": {
        "use_cases": ["creative-ideation", "brainstorming", "uncensored"],
        "strengths": ["405B parameters", "largest free model", "uncensored"],
    },
    "openai/gpt-oss-120b:free": {
        "use_cases": ["general-tasks", "free-tier"],
        "strengths": ["free tier", "OpenAI quality", "cost optimization"],
    },
}


def get_model_cost(model_name: str, input_tokens: int, output_tokens: int) -> float:
    """
    Calculate the cost for a given model and token usage.
    
    Args:
        model_name: The name of the model
        input_tokens: Number of input tokens
        output_tokens: Number of output tokens
        
    Returns:
        The total cost in dollars
    """
    if model_name not in MODEL_PRICING:
        return 0.0
    
    pricing = MODEL_PRICING[model_name]
    input_cost = (input_tokens / 1_000_000) * pricing["input"]
    output_cost = (output_tokens / 1_000_000) * pricing["output"]
    
    return input_cost + output_cost


def is_free_model(model_name: str) -> bool:
    """
    Check if a model is free.
    
    Args:
        model_name: The name of the model
        
    Returns:
        True if the model is free, False otherwise
    """
    if model_name not in MODEL_PRICING:
        return False
    
    pricing = MODEL_PRICING[model_name]
    return pricing["input"] == 0.0 and pricing["output"] == 0.0


def get_models_by_use_case(use_case: str) -> list[str]:
    """
    Get all models that support a specific use case.
    
    Args:
        use_case: The use case to filter by
        
    Returns:
        List of model names that support the use case
    """
    return [
        model_name
        for model_name, capabilities in MODEL_CAPABILITIES.items()
        if use_case in capabilities.get("use_cases", [])
    ]


def get_free_models() -> list[str]:
    """
    Get all free models.
    
    Returns:
        List of free model names
    """
    return [
        model_name
        for model_name in MODEL_PRICING.keys()
        if is_free_model(model_name)
    ]


def get_model_info(model_name: str) -> dict:
    """
    Get complete information about a model.
    
    Args:
        model_name: The name of the model
        
    Returns:
        Dictionary containing pricing and capabilities
    """
    return {
        "pricing": MODEL_PRICING.get(model_name, {"input": 0.0, "output": 0.0}),
        "capabilities": MODEL_CAPABILITIES.get(model_name, {}),
        "is_free": is_free_model(model_name),
    }
