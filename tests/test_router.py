"""Tests for the SmartRouter class"""

import pytest
import os
from unittest.mock import Mock, patch, MagicMock
from smart_router import SmartRouter
from smart_router.exceptions import SmartRouterException


class TestSmartRouter:
    """Test cases for SmartRouter"""
    
    def test_init_without_api_key(self):
        """Test initialization without API key raises exception"""
        with patch.dict(os.environ, {}, clear=True):
            with pytest.raises(SmartRouterException):
                SmartRouter(preset="creative-ideation")
    
    def test_init_with_api_key(self):
        """Test successful initialization with API key"""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            router = SmartRouter(preset="creative-ideation")
            assert router.api_key == "test-key"
            assert router.primary_model == "arcee-ai/trinity-large-preview:free"
    
    def test_init_with_custom_config(self):
        """Test initialization with custom config"""
        config = {
            "model": "test/model",
            "models": ["test/fallback1", "test/fallback2"],
            "temperature": 0.5
        }
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            router = SmartRouter(config=config)
            assert router.primary_model == "test/model"
            assert router.temperature == 0.5
    
    def test_preset_loading(self):
        """Test that presets load correctly"""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            router = SmartRouter(preset="framework-builder")
            assert router.primary_model == "anthropic/claude-opus-4.6"
            assert "anthropic/claude-sonnet-4.5" in router.fallback_models
    
    def test_cost_tracking_enabled(self):
        """Test that cost tracking is enabled by default"""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            router = SmartRouter(preset="creative-ideation")
            assert router.track_costs is True
            assert router.cost_tracker is not None
    
    def test_cost_tracking_disabled(self):
        """Test that cost tracking can be disabled"""
        config = {
            "model": "test/model",
            "models": []
        }
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            router = SmartRouter(config=config, track_costs=False)
            assert router.track_costs is False
    
    @patch('smart_router.router.OpenAI')
    def test_chat_completion(self, mock_openai):
        """Test chat completion with mocked OpenAI client"""
        # Setup mock
        mock_response = Mock()
        mock_response.choices = [Mock(message=Mock(content="Test response"))]
        mock_response.model = "test/model"
        mock_response.usage = Mock(
            prompt_tokens=10,
            completion_tokens=20,
            total_tokens=30
        )
        
        mock_client = Mock()
        mock_client.chat.completions.create.return_value = mock_response
        mock_openai.return_value = mock_client
        
        # Test
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            router = SmartRouter(preset="creative-ideation")
            response = router.chat.completions.create(
                messages=[{"role": "user", "content": "Test"}]
            )
            
            assert response.choices[0].message.content == "Test response"
            mock_client.chat.completions.create.assert_called_once()
    
    def test_get_cost_summary(self):
        """Test getting cost summary"""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            router = SmartRouter(preset="creative-ideation")
            summary = router.get_cost_summary()
            
            assert "total_cost" in summary
            assert "total_requests" in summary
            assert summary["total_cost"] == 0.0
            assert summary["total_requests"] == 0
    
    def test_reset_costs(self):
        """Test resetting cost tracker"""
        with patch.dict(os.environ, {"OPENROUTER_API_KEY": "test-key"}):
            router = SmartRouter(preset="creative-ideation")
            router.reset_costs()
            
            summary = router.get_cost_summary()
            assert summary["total_cost"] == 0.0
            assert summary["total_requests"] == 0
