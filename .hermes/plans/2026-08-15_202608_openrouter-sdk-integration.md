---
name: openrouter-sdk-integration
title: OpenRouter SDK Integration
description: Build TypeScript + Python packages wrapping OpenRouter's chat completions API via the official Client SDKs
date: 2026-08-15
status: in_progress
---

# OpenRouter SDK Integration Plan

## Goal
Implement a reusable TypeScript + Python package that wraps OpenRouter's chat completions API following the official Quickstart patterns.

## Context
- Docs index fetched: https://openrouter.ai/docs/llms.txt (42K chars, full doc tree)
- Quickstart content loaded: API, Client SDKs, Agent SDK, OpenAI SDK drop-in
- Existing local research: `docs/openrouter-models.json` (8 free models), `docs/research/openrouter-free-models.md`, `docs/research/openrouter-models.md`
- Stack: TypeScript strict + Bun, Python (uv)
- Approach: Client SDKs (`@openrouter/sdk` for TS, `openrouter` for Python) — docs' primary recommendation

## Scope

### TypeScript package (`packages/openrouter-client/`)
- [ ] Install `@openrouter/sdk`
- [ ] `src/client.ts` — OpenRouter client wrapper with configurable apiKey, httpReferer, appTitle
- [ ] `src/chat.ts` — chat.send() wrapper, model + messages params
- [ ] `src/types.ts` — shared types (ChatCompletion, Message, ModelChoice)
- [ ] `src/index.ts` — public API surface
- [ ] `test/chat.test.ts` — basic smoke test (mocked)
- [ ] `README.md` — usage, install, examples

### Python package (`packages/openrouter-client-py/`)
- [ ] Install `openrouter` (pip)
- [ ] `src/openrouter_client_py/client.py` — OpenRouter client wrapper
- [ ] `src/openrouter_client_py/chat.py` — chat.send() wrapper
- [ ] `src/openrouter_client_py/__init__.py` — public API surface
- [ ] `tests/test_client.py` — basic smoke test (mocked)
- [ ] `README.md` — usage, install, examples

## Files to create
| File | Package |
|------|---------|
| `packages/openrouter-client/package.json` | TS |
| `packages/openrouter-client/src/client.ts` | TS |
| `packages/openrouter-client/src/chat.ts` | TS |
| `packages/openrouter-client/src/types.ts` | TS |
| `packages/openrouter-client/src/index.ts` | TS |
| `packages/openrouter-client/test/chat.test.ts` | TS |
| `packages/openrouter-client/README.md` | TS |
| `packages/openrouter-client-py/pyproject.toml` | Python |
| `packages/openrouter-client-py/src/openrouter_client_py/__init__.py` | Python |
| `packages/openrouter-client-py/src/openrouter_client_py/client.py` | Python |
| `packages/openrouter-client-py/src/openrouter_client_py/chat.py` | Python |
| `packages/openrouter-client-py/tests/test_client.py` | Python |
| `packages/openrouter-client-py/README.md` | Python |

## Verification
- TS: `bun test packages/openrouter-client/test/chat.test.ts` passes
- Python: `uv run pytest packages/openrouter-client-py/tests/test_client.py` passes
- Both: README examples are syntactically valid

## Risks
- API key not available for live test — use mocked tests only
- `@openrouter/sdk` / `openrouter` package surface may differ from docs — read actual package exports first

## References
- https://openrouter.ai/docs/quickstart.md
- https://openrouter.ai/docs/llms.txt
- `docs/openrouter-models.json`
- `docs/research/openrouter-free-models.md`
