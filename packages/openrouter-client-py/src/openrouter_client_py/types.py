"""openrouter_client_py - Python client wrapper for OpenRouter chat completions API."""

from dataclasses import dataclass
from typing import Optional, List


@dataclass
class OpenRouterClientConfig:
    api_key: str
    http_referer: Optional[str] = None
    app_title: Optional[str] = None


@dataclass
class ToolCall:
    id: str
    type: str  # 'function'
    function_name: str
    function_arguments: str


@dataclass
class Message:
    role: str  # 'system' | 'user' | 'assistant' | 'tool'
    content: str
    name: Optional[str] = None
    tool_calls: Optional[List[ToolCall]] = None
    tool_call_id: Optional[str] = None


@dataclass
class ModelChoice:
    index: int
    message: Message
    finish_reason: str


@dataclass
class Usage:
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


@dataclass
class ChatCompletion:
    id: str
    object: str  # 'chat.completion'
    created: int
    model: str
    choices: List[ModelChoice]
    usage: Usage
