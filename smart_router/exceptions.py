"""Custom exceptions for the Smart AI Router."""


class SmartRouterException(Exception):
    """Base exception for Smart Router errors."""
    pass


class ModelNotAvailableException(SmartRouterException):
    """Raised when a requested model is not available."""
    pass


class RateLimitException(SmartRouterException):
    """Raised when a rate limit is encountered."""
    pass


class AllModelsFailedException(SmartRouterException):
    """Raised when all models in the failover cascade have failed."""
    pass
