#!/usr/bin/env python3
"""Basic usage example for Smart AI Router"""

import os
from smart_router import SmartRouter


def main():
    # Make sure API key is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Error: OPENROUTER_API_KEY environment variable not set")
        print("Get your key from: https://openrouter.ai/keys")
        return
    
    # Initialize router with a preset
    print("Initializing Smart AI Router with 'creative-ideation' preset...")
    router = SmartRouter(preset="creative-ideation")
    
    # Create a simple chat completion
    print("\nGenerating creative ideas...")
    response = router.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Generate 3 innovative product ideas for a smart home device."
            }
        ]
    )
    
    # Print the response
    print("\nResponse:")
    print(response.choices[0].message.content)
    
    # Check cost summary
    print("\n" + "="*60)
    print("Cost Summary:")
    print("="*60)
    summary = router.get_cost_summary()
    print(f"Total Cost: ${summary['total_cost']:.4f}")
    print(f"Total Requests: {summary['total_requests']}")
    print("\nCost by Model:")
    for model, cost in summary['cost_by_model'].items():
        print(f"  {model}: ${cost:.4f}")


if __name__ == "__main__":
    main()
