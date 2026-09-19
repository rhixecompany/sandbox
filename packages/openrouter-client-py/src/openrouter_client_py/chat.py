"""send_chat - Convenience function for one-shot OpenRouter chat completions."""

from typing import Any

from .memory import SupermemoryMemory
from .types import (
    ChatCompletion,
    Message,
    OpenRouterClientConfig,
)


async def send_chat(
    api_key: str,
    model: str,
    messages: list[Message],
    http_referer: str | None = None,
    app_title: str | None = None,
    stream: bool = False,
    max_tokens: int | None = None,
    temperature: float | None = None,
    memory: dict[str, Any] | None = None,
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
        memory: Optional Supermemory integration dict, e.g.
            {"containerTag": "user_123", "inject": True, "store": True,
             "limit": 5, "searchMode": "hybrid"}.
            - inject: search prior context (POST /v4/search) and prepend it to
              the system message before the model answers.
            - store: persist each user/assistant exchange (POST
              /v3/documents, taskType "memory").
            Requires SUPERMEMORY_API_KEY in the environment; any failure
            degrades to current behavior (no memory, no error).

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

    # Search-then-answer: retrieve prior context and inject into the system turn.
    chat_messages = list(messages)
    if memory and memory.get("inject") and memory.get("containerTag"):
        try:
            mem = SupermemoryMemory(str(memory["containerTag"]))
            last_user = next((m.content for m in reversed(messages) if m.role == "user"), "")
            query = str(memory.get("searchQuery") or last_user)
            if query:
                results = await mem.asearch_context(
                    query,
                    limit=int(memory.get("limit") or 5),
                    search_mode=str(memory.get("searchMode") or "hybrid"),
                )
                block = SupermemoryMemory.build_system_context(results)
                if block:
                    sys_idx = next(
                        (i for i, m in enumerate(chat_messages) if m.role == "system"),
                        None,
                    )
                    if sys_idx is None:
                        chat_messages.insert(0, Message(role="system", content=block))
                    else:
                        old = chat_messages[sys_idx]
                        chat_messages[sys_idx] = Message(
                            role="system",
                            content=f"{old.content}\n\n{block}",
                            name=old.name,
                        )
        except Exception:
            pass

    completion = await client.chat_send(
        model=model,
        messages=chat_messages,
        stream=stream,
        max_tokens=max_tokens,
        temperature=temperature,
    )

    # Store the exchange for future sessions (best effort).
    if memory and memory.get("store") and memory.get("containerTag"):
        try:
            mem = SupermemoryMemory(str(memory["containerTag"]))
            for m in messages:
                if m.role in ("user", "assistant"):
                    await mem.astore_exchange(m.role, m.content)
        except Exception:
            pass

    return completion
