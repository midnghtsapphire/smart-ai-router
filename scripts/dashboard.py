#!/usr/bin/env python3
"""Cost and usage dashboard for Smart AI Router"""

import json
import os
from datetime import datetime, timedelta
from pathlib import Path


def display_dashboard():
    """Display cost and usage dashboard"""
    # Try multiple possible locations for cost log
    possible_paths = [
        Path.home() / ".smart-ai-router" / "costs.json",
        Path.cwd() / "costs.json",
        Path.home() / ".clawdbot" / "costs.json"
    ]
    
    log_file = None
    for path in possible_paths:
        if path.exists():
            log_file = path
            break
    
    if not log_file:
        print("No cost data yet. Run some requests first!")
        print(f"Checked locations: {[str(p) for p in possible_paths]}")
        return
    
    try:
        with open(log_file, 'r') as f:
            logs = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading cost data: {e}")
        return
    
    # Today's stats
    today = datetime.now().strftime("%Y-%m-%d")
    today_data = logs.get(today, {"total": 0.0, "requests": []})
    
    print("=" * 60)
    print("📊 SMART AI ROUTER USAGE DASHBOARD")
    print("=" * 60)
    
    print(f"\n📅 Today ({today})")
    print(f"   Total Cost: ${today_data['total']:.4f}")
    print(f"   Requests: {len(today_data['requests'])}")
    
    # Model breakdown
    if today_data['requests']:
        model_costs = {}
        for req in today_data['requests']:
            model = req['model']
            if model not in model_costs:
                model_costs[model] = {"cost": 0.0, "count": 0}
            model_costs[model]["cost"] += req["cost"]
            model_costs[model]["count"] += 1
        
        print("\n   By Model:")
        for model, data in sorted(model_costs.items(), key=lambda x: x[1]["cost"], reverse=True):
            model_short = model.split("/")[-1][:30]
            print(f"      • {model_short}: ${data['cost']:.4f} ({data['count']} req)")
    
    # Weekly stats
    week_total = 0.0
    week_requests = 0
    for i in range(7):
        date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
        if date in logs:
            week_total += logs[date]["total"]
            week_requests += len(logs[date]["requests"])
    
    print(f"\n📅 Last 7 Days")
    print(f"   Total Cost: ${week_total:.2f}")
    print(f"   Requests: {week_requests}")
    print(f"   Avg/Day: ${week_total/7:.2f}")
    
    # Budget status
    daily_budget = float(os.getenv("OPENROUTER_DAILY_BUDGET", "10.00"))
    budget_pct = (today_data['total'] / daily_budget) * 100 if daily_budget > 0 else 0
    
    print(f"\n💰 Budget Status")
    print(f"   Daily Budget: ${daily_budget:.2f}")
    print(f"   Used Today: ${today_data['total']:.2f} ({budget_pct:.1f}%)")
    print(f"   Remaining: ${daily_budget - today_data['total']:.2f}")
    
    if budget_pct > 80:
        print("   ⚠️  Warning: >80% of daily budget used")
    
    print("\n" + "=" * 60)


if __name__ == "__main__":
    display_dashboard()
