---
name: openrouter-sdk-integration
title: OpenRouter SDK Integration — Specification
description: Specification for TypeScript + Python packages wrapping OpenRouter's chat completions API via official Client SDKs
date: 2026-08-15
status: draft
---

# OpenRouter SDK Integration — Specification

## 1. Overview

Build two standalone packages that wrap OpenRouter's chat completions API using the official Client SDKs, providing a typed, ergonomic convenience layer on top of the SDKs' protocol handling.

| Dimension | Detail |
|-----------|--------|
| **TypeScript package** | `packages/openrouter-client/` — Bun, TypeScript strict |
| **Python package** | `packages/openrouter-client-py/` — uv, Python 3.11+ |
| **Approach** | Official Client SDKs (`@openrouter/sdk` TS, `openrouter` Python) + typed convenience layer |
| **Decision rationale** | Option D from exploration: SDK handles protocol correctly (docs-recommended), our layer provides ergonomic types and simplified public API |
| **API key** | Not available — all tests mocked |

## 2. TypeScript Package Specification

### 2.1 Package metadata

| Field | Value |
|-------|-------|
| Name | `openrouter-client` |
| Location | `packages/openrouter-client/` |
| Runtime | Bun |
| Language | TypeScript strict |
| Dependency | `@openrouter/sdk` (official) |

### 2.2 Public API surface (`src/index.ts`)

Exports:

```typescript
export { OpenRouterClient } from './client';
export { sendChat } from './chat';
export type { ChatCompletion, Message, ModelChoice, OpenRouterClientConfig } from './types';
```

### 2.3 Types (`src/types.ts`)

```typescript
export interface OpenRouterClientConfig {
  apiKey: string;
  httpReferer?: string;
  appTitle?: string;
}

export interface Message {
  role: 'system' | 'user' | 'assistant' | 'tool';
  content: string;
  name?: string;
  tool_calls?: ToolCall[];
  tool_call_id?: string;
}

export interface ToolCall {
  id: string;
  type: 'function';
  function: { name: string; arguments: string; }
}

export interface ModelChoice {
  index: number;
  message: Message;
  logprobs?: number[];
  finish_reason: 'stop' | 'length' | 'tool_calls' | 'content_filter' | 'null';
}

export interface ChatCompletion {
  id: string;
  object: 'chat.completion';
  created: number;
  model: string;
  choices: ModelChoice[];
  usage: { prompt_tokens: number; completion_tokens: number; total_tokens: number; };
}
```

### 2.4 Client wrapper (`src/client.ts`)

```typescript
export class OpenRouterClient {
  constructor(config: OpenRouterClientConfig);

  /** Send a chat completion request. Returns raw ChatCompletion. */
  chatSend(params: { model: string; messages: Message[]; stream?: boolean; max_tokens?: number; temperature?: number; }): Promise<ChatCompletion>;
}
```

Delegates to `@openrouter/sdk` internally. The wrapper:
- Sets `Authorization: Bearer <apiKey>` header
- Optionally sets `HTTP-Referer` and `X-Title` headers from config
- Passes through model, messages, and optional params
- Maps SDK response to our `ChatCompletion` type

### 2.5 Chat convenience wrapper (`src/chat.ts`)

```typescript
export async function sendChat(
  apiKey: string,
  model: string,
  messages: Message[],
  options?: { httpReferer?: string; appTitle?: string; stream?: boolean; max_tokens?: number; temperature?: number; }
): Promise<ChatCompletion>;
```

A one-shot convenience function that constructs an `OpenRouterClient` internally, calls `chatSend`, and returns the result. Designed for simple use cases where a full client instance isn't needed.

### 2.6 Test (`test/chat.test.ts`)

- Mock the `@openrouter/sdk` response
- Test `sendChat` with a single user message returns a `ChatCompletion`
- Test `OpenRouterClient` instantiation with config
- Test that `httpReferer` and `appTitle` are passed as headers when provided
- All tests pass with `bun test`

### 2.7 README

- Install: `bun add @openrouter/sdk` + package install
- Quick start: `sendChat` example
- Client class example with config
- Types documentation
- Link to OpenRouter docs

## 3. Python Package Specification

### 3.1 Package metadata

| Field | Value |
|-------|-------|
| Name | `openrouter-client-py` |
| Location | `packages/openrouter-client-py/` |
| Runtime | Python 3.11+ (uv) |
| Dependency | `openrouter` (pip, official) |

### 3.2 Public API surface (`src/openrouter_client_py/__init__.py`)

```python
from .client import OpenRouterClient
from .chat import send_chat
from .types import ChatCompletion, Message, ModelChoice, OpenRouterClientConfig
```

### 3.3 Types (`src/openrouter_client_py/types.py`)

```python
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
```

### 3.4 Client wrapper (`src/openrouter_client_py/client.py`)

```python
class OpenRouterClient:
    def __init__(self, config: OpenRouterClientConfig):
        ...

    def chat_send(self, model: str, messages: List[Message], stream: bool = False,
                  max_tokens: Optional[int] = None, temperature: Optional[float] = None) -> ChatCompletion:
        ...
```

Delegates to the `openrouter` Python package internally. The wrapper:
- Sets auth headers from `api_key`
- Optionally sets `HTTP-Referer` and `X-Title` headers
- Passes through parameters
- Maps SDK response to our `ChatCompletion` type

### 3.5 Chat convenience wrapper (`src/openrouter_client_py/chat.py`)

```python
def send_chat(
    api_key: str,
    model: str,
    messages: List[Message],
    http_referer: Optional[str] = None,
    app_title: Optional[str] = None,
    stream: bool = False,
    max_tokens: Optional[int] = None,
    temperature: Optional[float] = None,
) -> ChatCompletion:
    ...
```

### 3.6 Test (`tests/test_client.py`)

- Mock the `openrouter` SDK response
- Test `send_chat` with a single user message returns a `ChatCompletion`
- Test `OpenRouterClient` instantiation with config
- Test that `http_referer` and `app_title` are passed as headers when provided
- All tests pass with `uv run pytest`

### 3.7 README

- Install: `pip install openrouter` + package install
- Quick start: `send_chat` example
- Client class example with config
- Types documentation
- Link to OpenRouter docs

## 4. Cross-Cutting Concerns

### 4.1 SDK surface verification

Before implementing types, read the actual exports of `@openrouter/sdk` (TS) and `openrouter` (Python) to confirm:
- SDK response shape matches our `ChatCompletion` type design
- Header-setting mechanism (how to pass `httpReferer`, `appTitle`)
- Whether the SDK has a `chat.send()` method or equivalent
- What the SDK's own types look like (to decide how much to re-type vs re-export)

### 4.2 Mocking strategy

Both packages use mocked SDK responses for tests since no API key is available. The mock should return a minimal valid `ChatCompletion` response.

### 4.3 Idempotent README examples

README code examples should be syntactically valid but not execute (no real API key). Use placeholder strings like `'your-api-key'`.

## 5. Files to Create

### TypeScript

| File | Purpose |
|------|---------|
| `packages/openrouter-client/package.json` | Package metadata, scripts, dependency on `@openrouter/sdk` |
| `packages/openrouter-client/tsconfig.json` | TypeScript strict config |
| `packages/openrouter-client/src/types.ts` | Shared types |
| `packages/openrouter-client/src/client.ts` | Client class wrapping SDK |
| `packages/openrouter-client/src/chat.ts` | Convenience `sendChat` function |
| `packages/openrouter-client/src/index.ts` | Public API surface |
| `packages/openrouter-client/test/chat.test.ts` | Mocked smoke tests |
| `packages/openrouter-client/README.md` | Usage, install, examples |

### Python

| File | Purpose |
|------|---------|
| `packages/openrouter-client-py/pyproject.toml` | Package metadata, dependency on `openrouter` |
| `packages/openrouter-client-py/src/openrouter_client_py/__init__.py` | Public API surface |
| `packages/openrouter-client-py/src/openrouter_client_py/types.py` | Shared types |
| `packages/openrouter-client-py/src/openrouter_client_py/client.py` | Client class wrapping SDK |
| `packages/openrouter-client-py/src/openrouter_client_py/chat.py` | Convenience `send_chat` function |
| `packages/openrouter-client-py/tests/test_client.py` | Mocked smoke tests |
| `packages/openrouter-client-py/README.md` | Usage, install, examples |
| `packages/openrouter-client-py/.python-version` | Python version pin (3.11) |

## 6. Verification Criteria

### TypeScript
- `bun install` in `packages/openrouter-client/` succeeds
- `bun test packages/openrouter-client/test/chat.test.ts` passes (2+ tests)
- `bun run typecheck` (tsc --noEmit) passes with zero errors
- README examples are syntactically valid TypeScript

### Python
- `uv sync` in `packages/openrouter-client-py/` succeeds
- `uv run pytest packages/openrouter-client-py/tests/test_client.py` passes (2+ tests)
- README examples are syntactically valid Python

### Both
- SDK surface was verified before type design (documented in implementation notes)
- No real API calls made (mocked tests only)
- Public API surface matches spec exactly

## 7. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| SDK export surface differs from docs | Medium | Medium | Read actual package exports before designing types; adjust types if needed |
| SDK API changes between now and implementation | Low | Low | Pin dependency versions in package.json/pyproject.toml |
| Mock response shape diverges from real API | Low | Low | Mirror the documented OpenRouter response format from docs |
