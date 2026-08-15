"""send_chat - Convenience function for one-shot OpenRouter chat completions."""

from typing import List, Optional

from .types import (
    OpenRouterClientConfig,
    Message,
    ChatCompletion,
)


async def send_chat(
    api_key: str,
    model: str,
    messages: List[Message],
    http_referer: Optional[str] = None,
    app_title: Optional[str] = None,
    stream: bool = False,
    max_tokens: Optional[int] = None,
    temperature: Optional[float] = None,
) -> ChatCompletion:
    """Send a chat completion request with a one-shot convenience API.

    Args:
        api_key: Your OpenRouter API key.
        model: Model identifier (e.g., "openai/gpt-4o").
        messages: Array of chat messages.
        http_referer: Optional HTTP-Referer header for billing attribution.
        app_title: Optional X-Title header for billing attribution.
        stream: Whether to stream the response (default False).
        max_tokens: Maximum tokens to generate.
        temperature: Sampling temperature (0.0-2.0).

    Returns:
        ChatCompletion response object.
    """
    from .client import OpenRouterClient

    config = OpenRouterClientConfig(
        api_key=api_key,
        http_referer=http_referer,
        app_title=app_title,
    )
    client = OpenRouterClient(config)
    return await client.chat_send(
        model=model,
        messages=messages,
        stream=stream,
        max_tokens=max_tokens,
        temperature=temperature,
    )
