"""openrouter_client_py - Python client wrapper for OpenRouter chat completions API."""

from .chat import send_chat
from .client import OpenRouterClient
from .memory import SupermemoryMemory, is_available
from .types import (
    ChatCompletion,
    Message,
    ModelChoice,
    OpenRouterClientConfig,
    ToolCall,
    Usage,
)

__all__ = [
    "ChatCompletion",
    "Message",
    "ModelChoice",
    "OpenRouterClient",
    "OpenRouterClientConfig",
    "SupermemoryMemory",
    "ToolCall",
    "Usage",
    "is_available",
    "send_chat",
]
