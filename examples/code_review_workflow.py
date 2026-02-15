#!/usr/bin/env python3
"""Code review workflow example using Smart AI Router"""

import os
from smart_router import SmartRouter


def main():
    # Make sure API key is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Error: OPENROUTER_API_KEY environment variable not set")
        return
    
    print("="*60)
    print("CODE REVIEW WORKFLOW")
    print("="*60)
    
    # Initialize router with code review preset
    router = SmartRouter(preset="code-review")
    
    # Sample code to review
    code_to_review = """
def calculate_total(items):
    total = 0
    for item in items:
        total = total + item['price'] * item['quantity']
    return total

def apply_discount(total, discount_percent):
    discount = total * discount_percent / 100
    return total - discount
"""
    
    print("\n🔍 Reviewing code for bugs and improvements...")
    print("\nCode to review:")
    print(code_to_review)
    
    response = router.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"""Review this Python code for:
1. Bugs and potential errors
2. Performance improvements
3. Best practices
4. Security issues

Code:
{code_to_review}

Provide specific, actionable feedback."""
            }
        ]
    )
    
    print("\n" + "="*60)
    print("REVIEW RESULTS")
    print("="*60)
    print("\n" + response.choices[0].message.content)
    
    # Display cost summary
    print("\n" + "="*60)
    print("COST SUMMARY")
    print("="*60)
    summary = router.get_cost_summary()
    print(f"Total Cost: ${summary['total_cost']:.4f}")
    print(f"Total Requests: {summary['total_requests']}")
    
    # Show which model was used
    if summary['requests_by_model']:
        print("\nModels Used:")
        for model, count in summary['requests_by_model'].items():
            model_short = model.split('/')[-1]
            print(f"  {model_short}: {count} request(s)")


if __name__ == "__main__":
    main()
