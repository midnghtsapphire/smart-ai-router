"""Cost tracking functionality for the Smart AI Router."""

from typing import Dict, List
from datetime import datetime
from .models import get_model_cost


class CostTracker:
    """Tracks costs across multiple model requests."""
    
    def __init__(self):
        """Initialize the cost tracker."""
        self.requests: List[Dict] = []
        self.total_cost = 0.0
        
    def track_request(
        self,
        model_name: str,
        input_tokens: int,
        output_tokens: int,
        timestamp: datetime = None
    ):
        """
        Track a single request.
        
        Args:
            model_name: The name of the model used
            input_tokens: Number of input tokens
            output_tokens: Number of output tokens
            timestamp: Timestamp of the request (defaults to now)
        """
        if timestamp is None:
            timestamp = datetime.now()
            
        cost = get_model_cost(model_name, input_tokens, output_tokens)
        
        request_data = {
            "model": model_name,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "cost": cost,
            "timestamp": timestamp
        }
        
        self.requests.append(request_data)
        self.total_cost += cost
        
    def get_total_cost(self) -> float:
        """
        Get the total cost of all tracked requests.
        
        Returns:
            Total cost in dollars
        """
        return self.total_cost
    
    def get_cost_by_model(self) -> Dict[str, float]:
        """
        Get costs broken down by model.
        
        Returns:
            Dictionary mapping model names to total costs
        """
        costs_by_model = {}
        
        for request in self.requests:
            model = request["model"]
            cost = request["cost"]
            
            if model not in costs_by_model:
                costs_by_model[model] = 0.0
            
            costs_by_model[model] += cost
            
        return costs_by_model
    
    def get_request_count(self) -> int:
        """
        Get the total number of tracked requests.
        
        Returns:
            Number of requests
        """
        return len(self.requests)
    
    def get_request_count_by_model(self) -> Dict[str, int]:
        """
        Get request counts broken down by model.
        
        Returns:
            Dictionary mapping model names to request counts
        """
        counts_by_model = {}
        
        for request in self.requests:
            model = request["model"]
            
            if model not in counts_by_model:
                counts_by_model[model] = 0
            
            counts_by_model[model] += 1
            
        return counts_by_model
    
    def get_summary(self) -> Dict:
        """
        Get a summary of all tracked costs and requests.
        
        Returns:
            Dictionary containing summary statistics
        """
        return {
            "total_cost": self.total_cost,
            "total_requests": len(self.requests),
            "cost_by_model": self.get_cost_by_model(),
            "requests_by_model": self.get_request_count_by_model()
        }
    
    def reset(self):
        """Reset the cost tracker."""
        self.requests = []
        self.total_cost = 0.0
