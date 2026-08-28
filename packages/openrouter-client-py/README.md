# OpenRouter Client (Python) — Usage Guide

## Install

```bash
cd packages/openrouter-client-py
pip install -e ".[test]"   # install with pytest
# or: pip install openrouter-client-py
```

## Quick Start

```python
import asyncio
from openrouter_client_py import send_chat, Message

async def main():
    response = await send_chat(
        api_key="your-api-key",
        model="openai/gpt-4o",
        messages=[Message(role="user", content="Hello, world!")],
        http_referer="https://your-site.com",
        app_title="My Application",
        temperature=0.7,
    )
    print(response.choices[0].message.content)

asyncio.run(main())
```

## Using the Client Class

```python
import asyncio
from openrouter_client_py import OpenRouterClient, OpenRouterClientConfig, Message

async def main():
    config = OpenRouterClientConfig(
        api_key="your-api-key",
        http_referer="https://your-site.com",
        app_title="My Application",
    )
    client = OpenRouterClient(config)

    response = await client.chat_send(
        model="google/gemma-2-9b-it",
        messages=[
            Message(role="system", content="You are a helpful assistant."),
            Message(role="user", content="What is 2+2?"),
        ],
        temperature=0.3,
    )
    print(response.choices[0].message.content)

asyncio.run(main())
```

## Streaming

```python
# Note: streaming returns the full ChatCompletion object.
# For token-by-token streaming, use the SDK directly.
response = await client.chat_send(
    model="openai/gpt-4o",
    messages=[Message(role="user", content="Write a poem")],
    stream=True,
)
```

## Types

| Type                     | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| `OpenRouterClientConfig` | Client configuration (api_key, http_referer, app_title)   |
| `Message`                | Chat message with role, content, optional tool calls      |
| `ToolCall`               | Function tool call with id, type, and function details    |
| `ModelChoice`            | A single completion choice with message and finish reason |
| `Usage`                  | Token usage statistics (prompt, completion, total)        |
| `ChatCompletion`         | Full API response with id, model, choices, and usage      |

## Available Models

See [OpenRouter's model list](https://openrouter.ai/models) for all available models. Common examples:

- `openai/gpt-4o` — GPT-4o
- `google/gemma-2-9b-it` — Gemma 2 9B instruction-tuned
- `anthropic/claude-3-opus` — Claude 3 Opus
- `nvidia/nemotron-4-340b` — Nemotron 4 340B

## Error Handling

The SDK raises exceptions on API errors (4xx, 5xx). Handle appropriately:

```python
try:
    response = await send_chat(...)
except Exception as e:
    print(f"OpenRouter API error: {e}")
```

## Running Tests

```bash
cd packages/openrouter-client-py
pip install -e ".[test]"
pytest tests/test_client.py -v
```

## License

MIT
