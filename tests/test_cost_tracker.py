"""Tests for the CostTracker class"""

import pytest
from datetime import datetime
from smart_router.cost_tracker import CostTracker


class TestCostTracker:
    """Test cases for CostTracker"""
    
    def test_init(self):
        """Test CostTracker initialization"""
        tracker = CostTracker()
        assert tracker.total_cost == 0.0
        assert len(tracker.requests) == 0
    
    def test_track_request(self):
        """Test tracking a single request"""
        tracker = CostTracker()
        tracker.track_request(
            model_name="anthropic/claude-opus-4.6",
            input_tokens=1000,
            output_tokens=500
        )
        
        assert tracker.total_cost > 0
        assert len(tracker.requests) == 1
        assert tracker.requests[0]["model"] == "anthropic/claude-opus-4.6"
    
    def test_track_free_model(self):
        """Test tracking a free model request"""
        tracker = CostTracker()
        tracker.track_request(
            model_name="trinity-large-preview:free",
            input_tokens=1000,
            output_tokens=500
        )
        
        assert tracker.total_cost == 0.0
        assert len(tracker.requests) == 1
    
    def test_get_total_cost(self):
        """Test getting total cost"""
        tracker = CostTracker()
        tracker.track_request("anthropic/claude-opus-4.6", 1000, 500)
        tracker.track_request("deepseek/deepseek-v3.2", 1000, 500)
        
        total = tracker.get_total_cost()
        assert total > 0
        assert total == tracker.total_cost
    
    def test_get_cost_by_model(self):
        """Test getting costs broken down by model"""
        tracker = CostTracker()
        tracker.track_request("anthropic/claude-opus-4.6", 1000, 500)
        tracker.track_request("anthropic/claude-opus-4.6", 1000, 500)
        tracker.track_request("deepseek/deepseek-v3.2", 1000, 500)
        
        costs = tracker.get_cost_by_model()
        assert "anthropic/claude-opus-4.6" in costs
        assert "deepseek/deepseek-v3.2" in costs
        assert costs["anthropic/claude-opus-4.6"] > costs["deepseek/deepseek-v3.2"]
    
    def test_get_request_count(self):
        """Test getting total request count"""
        tracker = CostTracker()
        tracker.track_request("anthropic/claude-opus-4.6", 1000, 500)
        tracker.track_request("deepseek/deepseek-v3.2", 1000, 500)
        
        count = tracker.get_request_count()
        assert count == 2
    
    def test_get_request_count_by_model(self):
        """Test getting request counts by model"""
        tracker = CostTracker()
        tracker.track_request("anthropic/claude-opus-4.6", 1000, 500)
        tracker.track_request("anthropic/claude-opus-4.6", 1000, 500)
        tracker.track_request("deepseek/deepseek-v3.2", 1000, 500)
        
        counts = tracker.get_request_count_by_model()
        assert counts["anthropic/claude-opus-4.6"] == 2
        assert counts["deepseek/deepseek-v3.2"] == 1
    
    def test_get_summary(self):
        """Test getting summary statistics"""
        tracker = CostTracker()
        tracker.track_request("anthropic/claude-opus-4.6", 1000, 500)
        tracker.track_request("deepseek/deepseek-v3.2", 1000, 500)
        
        summary = tracker.get_summary()
        assert "total_cost" in summary
        assert "total_requests" in summary
        assert "cost_by_model" in summary
        assert "requests_by_model" in summary
        assert summary["total_requests"] == 2
    
    def test_reset(self):
        """Test resetting the tracker"""
        tracker = CostTracker()
        tracker.track_request("anthropic/claude-opus-4.6", 1000, 500)
        tracker.reset()
        
        assert tracker.total_cost == 0.0
        assert len(tracker.requests) == 0
