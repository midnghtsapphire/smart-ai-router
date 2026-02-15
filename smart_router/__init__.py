"""Smart AI Router - Intelligent multi-model routing with automatic failover."""

from .router import SmartRouter
from .exceptions import (
    SmartRouterException,
    ModelNotAvailableException,
    RateLimitException,
    AllModelsFailedException
)

__version__ = "1.0.0"
__all__ = [
    "SmartRouter",
    "SmartRouterException",
    "ModelNotAvailableException",
    "RateLimitException",
    "AllModelsFailedException"
]
