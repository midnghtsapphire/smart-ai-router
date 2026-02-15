#!/usr/bin/env python3
"""Creative workflow example using Smart AI Router"""

import os
from smart_router import SmartRouter


def main():
    # Make sure API key is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Error: OPENROUTER_API_KEY environment variable not set")
        return
    
    print("="*60)
    print("CREATIVE IDEATION WORKFLOW")
    print("="*60)
    
    # Initialize router with creative preset
    router = SmartRouter(preset="creative-ideation")
    
    # Generate blue ocean strategy ideas
    print("\n💡 Generating blue ocean strategy ideas...")
    response = router.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": """Generate 5 blue ocean strategy ideas for a personalized 
                nutrition company. Focus on underserved markets and innovative approaches."""
            }
        ]
    )
    
    print("\n" + response.choices[0].message.content)
    
    # Generate creative product names
    print("\n" + "="*60)
    print("\n🎨 Generating creative product names...")
    response = router.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": """Generate 10 creative and memorable product names for a 
                line of AI-powered wellness devices. Make them fun and brandable."""
            }
        ]
    )
    
    print("\n" + response.choices[0].message.content)
    
    # Display cost summary
    print("\n" + "="*60)
    print("COST SUMMARY")
    print("="*60)
    summary = router.get_cost_summary()
    print(f"Total Cost: ${summary['total_cost']:.4f}")
    print(f"Total Requests: {summary['total_requests']}")
    print("\nBy Model:")
    for model, cost in summary['cost_by_model'].items():
        model_short = model.split('/')[-1]
        print(f"  {model_short}: ${cost:.4f}")


if __name__ == "__main__":
    main()
