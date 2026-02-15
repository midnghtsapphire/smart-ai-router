#!/usr/bin/env python3
"""
Workflow Executor Example
Demonstrates multi-step workflows with different models
"""

import os
from smart_router import SmartRouter


class WorkflowExecutor:
    """Execute multi-step workflows with different models"""
    
    def __init__(self):
        self.routers = {}
        
    def get_router(self, preset):
        """Get or create a router for a preset"""
        if preset not in self.routers:
            self.routers[preset] = SmartRouter(preset=preset)
        return self.routers[preset]
    
    def execute_framework_dev(self, spec: str):
        """Build core framework with premium models"""
        
        print("🏗️  Phase 1: Framework Architecture")
        framework_router = self.get_router("framework-builder")
        architecture = framework_router.chat.completions.create(
            messages=[{
                "role": "user",
                "content": f"""Design complete architecture for: {spec}
                
Include:
- CLI structure
- Core modules
- API design
- Error handling
- Testing strategy"""
            }]
        )
        
        print("🔍 Phase 2: Code Review")
        review_router = self.get_router("code-review")
        review = review_router.chat.completions.create(
            messages=[{
                "role": "user",
                "content": f"Review this architecture for issues:\n\n{architecture.choices[0].message.content}"
            }]
        )
        
        print("✅ Phase 3: Validation")
        test_router = self.get_router("production-testing")
        validation = test_router.chat.completions.create(
            messages=[{
                "role": "user",
                "content": f"Validate this framework architecture and identify any gaps:\n\n{architecture.choices[0].message.content}"
            }]
        )
        
        return {
            "architecture": architecture.choices[0].message.content,
            "review": review.choices[0].message.content,
            "validation": validation.choices[0].message.content
        }
    
    def execute_app_creation(self, idea: str):
        """Create derivative app using free models"""
        
        print("💡 Phase 1: Creative Ideation (FREE)")
        creative_router = self.get_router("creative-ideation")
        ideation = creative_router.chat.completions.create(
            messages=[{
                "role": "user",
                "content": f"Generate blue ocean strategy and implementation plan for: {idea}"
            }]
        )
        
        print("🔍 Phase 2: Code Review")
        review_router = self.get_router("code-review")
        final_check = review_router.chat.completions.create(
            messages=[{
                "role": "user",
                "content": f"Review this implementation plan:\n\n{ideation.choices[0].message.content}"
            }]
        )
        
        return {
            "ideation": ideation.choices[0].message.content,
            "final_check": final_check.choices[0].message.content
        }
    
    def print_cost_summary(self):
        """Print cost summary for all routers"""
        print("\n" + "="*60)
        print("TOTAL COST SUMMARY")
        print("="*60)
        
        total_cost = 0.0
        total_requests = 0
        
        for preset, router in self.routers.items():
            summary = router.get_cost_summary()
            total_cost += summary['total_cost']
            total_requests += summary['total_requests']
            
            print(f"\n{preset}:")
            print(f"  Cost: ${summary['total_cost']:.4f}")
            print(f"  Requests: {summary['total_requests']}")
        
        print(f"\nGrand Total: ${total_cost:.4f}")
        print(f"Total Requests: {total_requests}")


def main():
    # Make sure API key is set
    if not os.getenv("OPENROUTER_API_KEY"):
        print("Error: OPENROUTER_API_KEY environment variable not set")
        return
    
    executor = WorkflowExecutor()
    
    # Example 1: Build core framework (premium investment)
    print("="*60)
    print("BUILDING CORE FRAMEWORK")
    print("="*60)
    
    framework_result = executor.execute_framework_dev(
        "CLI tool for AI model routing with automatic failover"
    )
    
    print("\n📋 Architecture:")
    print(framework_result["architecture"][:500] + "...")
    
    # Example 2: Create derivative app (free tier)
    print("\n" + "="*60)
    print("CREATING DERIVATIVE APP")
    print("="*60)
    
    app_result = executor.execute_app_creation(
        "Mobile app for tracking AI API costs across multiple providers"
    )
    
    print("\n💡 Ideation:")
    print(app_result["ideation"][:500] + "...")
    
    # Print total costs
    executor.print_cost_summary()


if __name__ == "__main__":
    main()
