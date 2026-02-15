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
    "deepseek/deepseek-v3.2:free": {"input": 0.0, "output": 0.0},
    
    # Free Models
    "trinity-large-preview:free": {"input": 0.0, "output": 0.0},
    "venice/uncensored:free": {"input": 0.0, "output": 0.0},
    "qwen/qwen-3-coder:free": {"input": 0.0, "output": 0.0},
    "qwen/qwen-3-coder-480b-a35b-instruct:free": {"input": 0.0, "output": 0.0},
    "step/step-3.5-flash:free": {"input": 0.0, "output": 0.0},
    "nothingiisreal/nemo-12b": {"input": 0.0, "output": 0.0},
}

# Model capabilities and use cases
MODEL_CAPABILITIES = {
    "anthropic/claude-opus-4.6": {
        "use_cases": ["framework-development", "complex-reasoning", "code-generation"],
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
    "trinity-large-preview:free": {
        "use_cases": ["creative-writing", "storytelling", "role-play"],
        "strengths": ["400B parameters", "creative excellence", "agentic workflows"],
    },
    "venice/uncensored:free": {
        "use_cases": ["creative-ideation", "unrestricted-use-cases"],
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
        "use_cases": ["creative-writing"],
        "strengths": ["Reddit Writing Prompts training", "active narration"],
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
