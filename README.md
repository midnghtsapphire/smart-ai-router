# Smart AI Router

An intelligent, multi-model AI routing architecture designed to optimize for cost, performance, and reliability. This library provides a `SmartRouter` class that automatically handles model selection, failover, and cost tracking, allowing developers to build robust and cost-effective AI-powered applications.

## Core Features

*   **Dynamic Model Routing:** Intelligently selects the best AI model for a given task based on preset configurations and real-time availability.
*   **Automatic Failover:** Seamlessly switches to fallback models in the event of API errors, rate limits, or other failures, ensuring high availability.
*   **Cost Optimization:** Prioritizes free and low-cost models to significantly reduce operational expenses while maintaining high-quality outputs.
*   **Preset Configurations:** Comes with pre-defined presets for common workflows such as creative ideation, code review, and framework development.
*   **Rate Limit Handling:** Automatically detects rate limits and switches to alternative models, preventing service disruptions.
*   **OpenClaw Integration:** Includes a configuration for easy integration with the OpenClaw workflow automation tool.

## Architecture Overview

The Smart AI Router is built upon a phased development strategy that maximizes ROI by strategically allocating resources.

### Phased Development Strategy

This architecture advocates for a two-phase development approach:

1.  **Phase 1: Framework Development (Premium Investment):** This initial phase focuses on building the core application framework using state-of-the-art, premium AI models (e.g., Claude 4.6 Opus). While this involves a higher upfront cost, it ensures a robust and powerful foundation for all subsequent development.

2.  **Phase 2: Derivative Applications (Cost-Effective):** Once the core framework is in place, derivative applications and features are built using a combination of high-performing free and low-cost models (e.g., DeepSeek V3.2, Trinity-Large-Preview). This approach dramatically reduces the cost of ongoing development and deployment.

### Failover Cascade

The `SmartRouter` implements a failover cascade to ensure the resilience of your application. When a request to the primary model fails, the router automatically retries the request with a series of predefined fallback models. This process is transparent to the application and guarantees that a response is returned whenever possible.

## Getting Started

### Installation

Clone the repository and install the required dependencies:

```bash
git clone https://github.com/MIDNGHTSAPPHIRE/smart-ai-router.git
cd smart-ai-router
pip install -r requirements.txt
```

### Configuration

Set your OpenRouter API key as an environment variable:

```bash
export OPENROUTER_API_KEY=\"your_openrouter_api_key\"
```

## Usage

The `SmartRouter` class is the central component of the library. It can be initialized with a preset or a custom configuration.

### Basic Usage

```python
from smart_router.router import SmartRouter

# Initialize the router with a preset
router = SmartRouter(preset=\"creative-ideation\")

# Create a chat completion
response = router.chat.completions.create(
    messages=[
        {
            \"role\": \"user\",
            \"content\": \"Generate a short story about a robot who discovers music.\"
        }
    ]
)

print(response.choices[0].message.content)
```

### Workflows Examples

#### Creative Ideation

```python
from smart_router.router import SmartRouter

# Use the creative-ideation preset for brainstorming
router = SmartRouter(preset=\"creative-ideation\")

response = router.chat.completions.create(
    messages=[
        {
            \"role\": \"user\",
            \"content\": \"Generate 5 blue ocean strategy ideas for a personalized nutrition company.\"
        }
    ]
)

print(response.choices[0].message.content)
```

#### Code Review

```python
from smart_router.router import SmartRouter

# Use the code-review preset for analyzing code
router = SmartRouter(preset=\"code-review\")

code_to_review = \"\"
# Your code here
\"\"

response = router.chat.completions.create(
    messages=[
        {
            \"role\": \"user\",
            \"content\": f\"Review this code for bugs and improvements:\n\n{code_to_review}\"
        }
    ]
)

print(response.choices[0].message.content)
```

## Presets

The Smart AI Router includes several preset configurations for different use cases. These presets are defined in the `presets/` directory.

| Preset                | Primary Model                     | Fallback Models                                                              |
| --------------------- | --------------------------------- | ---------------------------------------------------------------------------- |
| `framework-builder`   | `anthropic/claude-opus-4.6`       | `anthropic/claude-sonnet-4.5`, `openai/gpt-5.2-codex`                        |
| `creative-ideation`   | `trinity-large-preview:free`      | `venice/uncensored:free`, `deepseek/deepseek-v3.2`                           |
| `code-review`         | `deepseek/deepseek-v3.2:free`     | `qwen/qwen-3-coder:free`, `anthropic/claude-sonnet-4.5`                      |

## Cost Optimization

This routing architecture is designed to dramatically reduce costs by prioritizing the use of free and low-cost models. By using premium models only for the initial framework development, and relying on more economical models for ongoing tasks, you can achieve cost savings of up to 100x compared to a purely premium-model-based approach.

For a significant boost in rate limits for free models on OpenRouter, consider purchasing credits. A small one-time investment can increase your daily free request limit from 50 to 1000, providing a 20x capacity increase.

## OpenClaw Integration

To integrate the Smart AI Router with OpenClaw, configure your `~/.clawdbot/clawdbot.json` file with the desired model aliases and failover chains. An example configuration is provided in the `clawdbot.json` file in this repository.

## Production Testing

For testing in a production environment, we recommend a monitoring stack that includes:

*   **Shadow Deployments:** Use a feature flagging platform like LaunchDarkly to run new model configurations in the background without affecting users.
*   **Performance Monitoring:** Track key metrics such as accuracy, precision, recall, and latency. Implement data drift detection to monitor for changes in model performance.
*   **AI Configuration Management:** Use a tool like LaunchDarkly’s AI Configs to manage model configurations at runtime without requiring code deployments.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
