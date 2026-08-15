# OpenRouter Client (TypeScript) — Usage Guide

## Install

```bash
cd packages/openrouter-client
bun install
```

## Quick Start

```typescript
import { sendChat } from "openrouter-client";

const response = await sendChat(
  "your-api-key",
  "openai/gpt-4o",
  [{ role: "user", content: "Hello, world!" }],
  {
    httpReferer: "https://your-site.com",
    appTitle: "My Application",
    temperature: 0.7,
  }
);

console.log(response.choices[0].message.content);
```

## Using the Client Class

```typescript
import { OpenRouterClient } from "openrouter-client";

const client = new OpenRouterClient({
  apiKey: "your-api-key",
  httpReferer: "https://your-site.com",
  appTitle: "My Application",
});

const response = await client.chatSend({
  model: "google/gemma-2-9b-it",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "What is 2+2?" },
  ],
  temperature: 0.3,
});

console.log(response.choices[0].message.content);
```

## Streaming

```typescript
import { sendChat } from "openrouter-client";

const stream = await sendChat(
  "your-api-key",
  "openai/gpt-4o",
  [{ role: "user", content: "Write a poem" }],
  { stream: true }
);

// Note: streaming returns the full ChatCompletion; the SDK handles
// streaming internally. For token-by-token streaming, use the SDK directly.
```

## Types

| Type | Description |
|------|-------------|
| `OpenRouterClientConfig` | Client configuration (apiKey, httpReferer, appTitle) |
| `Message` | Chat message with role, content, optional tool calls |
| `ToolCall` | Function tool call with id, type, and function details |
| `ModelChoice` | A single completion choice with message and finish reason |
| `Usage` | Token usage statistics (prompt, completion, total) |
| `ChatCompletion` | Full API response with id, model, choices, and usage |

## Available Models

See [OpenRouter's model list](https://openrouter.ai/models) for all available models. Common examples:

- `openai/gpt-4o` — GPT-4o
- `google/gemma-2-9b-it` — Gemma 2 9B instruction-tuned
- `anthropic/claude-3-opus` — Claude 3 Opus
- `nvidia/nemotron-4-340b` — Nemotron 4 340B

## Error Handling

The SDK throws on API errors (4xx, 5xx). Handle appropriately:

```typescript
try {
  const response = await sendChat(/* ... */);
} catch (error) {
  console.error("OpenRouter API error:", error);
}
```

## License

MIT
