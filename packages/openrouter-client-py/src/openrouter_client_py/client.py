"""openrouter_client_py - Python client wrapper for OpenRouter chat completions API."""

from dataclasses import dataclass
from typing import List, Optional

from .types import (
    OpenRouterClientConfig,
    Message,
    ToolCall,
    ModelChoice,
    Usage,
    ChatCompletion,
)


class OpenRouterClient:
    """OpenRouter API client wrapping the openrouter SDK."""

    def __init__(self, config: OpenRouterClientConfig):
        self._config = config

    async def chat_send(
        self,
        model: str,
        messages: List[Message],
        stream: bool = False,
        max_tokens: Optional[int] = None,
        temperature: Optional[float] = None,
    ) -> ChatCompletion:
        """Send a chat completion request to OpenRouter."""
        import openrouter

        client = openrouter.OpenRouterClient(api_key=self._config.api_key)

        headers = {}
        if self._config.http_referer:
            headers["HTTP-Referer"] = self._config.http_referer
        if self._config.app_title:
            headers["X-Title"] = self._config.app_title

        response = await client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": m.role,
                    "content": m.content,
                    "name": m.name,
                    "tool_calls": [
                        {
                            "id": tc.id,
                            "type": tc.type,
                            "function": {
                                "name": tc.function_name,
                                "arguments": tc.function_arguments,
                            },
                        }
                        for tc in (m.tool_calls or [])
                    ],
                    "tool_call_id": m.tool_call_id,
                }
                for m in messages
            ],
            stream=stream,
            max_tokens=max_tokens,
            temperature=temperature,
            headers=headers,
        )

        choices = [
            ModelChoice(
                index=c.index,
                message=Message(
                    role=c.message.role,
                    content=c.message.content,
                    name=c.message.name,
                    tool_calls=[
                        ToolCall(
                            id=tc.id,
                            type=tc.type,
                            function_name=tc.function.name,
                            function_arguments=tc.function.arguments,
                        )
                        for tc in (c.message.tool_calls or [])
                    ],
                    tool_call_id=c.message.tool_call_id,
                ),
                finish_reason=str(c.finish_reason),
            )
            for c in response.choices
        ]

        usage = Usage(
            prompt_tokens=response.usage.prompt_tokens,
            completion_tokens=response.usage.completion_tokens,
            total_tokens=response.usage.total_tokens,
        )

        return ChatCompletion(
            id=response.id,
            object=response.object,
            created=response.created,
            model=response.model,
            choices=choices,
            usage=usage,
        )
