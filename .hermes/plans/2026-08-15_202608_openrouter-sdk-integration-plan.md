---
name: openrouter-sdk-integration-plan
title: OpenRouter SDK Integration — Implementation Plan
description: Phased task breakdown for building TypeScript + Python OpenRouter client packages
date: 2026-08-15
status: draft
---

# OpenRouter SDK Integration — Implementation Plan

**Spec:** [2026-08-15_202608_openrouter-sdk-integration-spec.md](2026-08-15_202608_openrouter-sdk-integration-spec.md)
**Goal:** Build two packages wrapping OpenRouter's chat completions API via official Client SDKs with a typed convenience layer.

---

## Phase 0: Discovery (SDK Surface Verification)

_Critical path dependency for all subsequent phases. Must read actual SDK exports before designing types._

### Task 0.1 — Read `@openrouter/sdk` exports (TypeScript)

- **Action:** Install `@openrouter/sdk` in a temp dir, inspect its exported types and methods
- **Goal:** Confirm `chat.send()` shape, response type, header-passing mechanism
- **Output:** Notes on SDK surface (methods, types, how to pass custom headers)
- **Estimate:** 15 min
- **Depends on:** nothing

### Task 0.2 — Read `openrouter` Python package exports

- **Action:** Install `openrouter` in a temp venv, inspect its exported classes and methods
- **Goal:** Confirm chat API shape, response type, header-passing mechanism
- **Output:** Notes on SDK surface (methods, types, how to pass custom headers)
- **Estimate:** 15 min
- **Depends on:** nothing

### Task 0.3 — Adjust spec types if needed

- **Action:** If SDK surface differs from spec assumptions, update the spec document
- **Goal:** Types in spec match what SDK actually provides
- **Estimate:** 10 min
- **Depends on:** 0.1, 0.2

---

## Phase 1: TypeScript Package

### Task 1.1 — Scaffold `packages/openrouter-client/`

- **Action:** Create directory, `package.json`, `tsconfig.json`
- **Details:**
  - `package.json`: name `openrouter-client`, scripts (`test`, `typecheck`), dependency `@openrouter/sdk`
  - `tsconfig.json`: strict mode, targeting ES2022, outDir `dist`
- **Estimate:** 5 min
- **Depends on:** 0.3

### Task 1.2 — Implement `src/types.ts`

- **Action:** Write `ChatCompletion`, `Message`, `ModelChoice`, `OpenRouterClientConfig` types
- **Details:** Match spec section 2.3; adjust if SDK surface from 0.1 differs
- **Estimate:** 10 min
- **Depends on:** 1.1, 0.1

### Task 1.3 — Implement `src/client.ts`

- **Action:** Write `OpenRouterClient` class wrapping `@openrouter/sdk`
- **Details:**
  - Constructor stores config (apiKey, httpReferer, appTitle)
  - `chatSend()` delegates to SDK, maps response to `ChatCompletion`
  - Sets auth + optional headers
- **Estimate:** 20 min
- **Depends on:** 1.2, 0.1

### Task 1.4 — Implement `src/chat.ts`

- **Action:** Write `sendChat` convenience function
- **Details:** Constructs client internally, calls `chatSend`, returns result
- **Estimate:** 10 min
- **Depends on:** 1.3

### Task 1.5 — Implement `src/index.ts`

- **Action:** Re-export all public symbols
- **Estimate:** 5 min
- **Depends on:** 1.2, 1.3, 1.4

### Task 1.6 — Write `test/chat.test.ts`

- **Action:** Mock SDK, write 2+ smoke tests
- **Details:**
  - Test `sendChat` with single user message
  - Test `OpenRouterClient` with config
  - Test header passing (httpReferer, appTitle)
- **Estimate:** 20 min
- **Depends on:** 1.3, 1.4

### Task 1.7 — Write `README.md`

- **Action:** Document install, quick start, client usage, types, examples
- **Estimate:** 15 min
- **Depends on:** 1.5

### Task 1.8 — Verify TypeScript package

- **Action:** `bun install`, `bun test`, `bun run typecheck`
- **Gate:** All pass, zero TypeScript errors
- **Estimate:** 10 min
- **Depends on:** 1.6, 1.1

---

## Phase 2: Python Package

### Task 2.1 — Scaffold `packages/openrouter-client-py/`

- **Action:** Create directory, `pyproject.toml`, `.python-version`
- **Details:**
  - `pyproject.toml`: name `openrouter-client-py`, dependency `openrouter`, test runner pytest
  - `.python-version`: `3.11`
- **Estimate:** 5 min
- **Depends on:** 0.3

### Task 2.2 — Implement `src/openrouter_client_py/types.py`

- **Action:** Write dataclass types matching spec section 3.3
- **Estimate:** 10 min
- **Depends on:** 2.1, 0.2

### Task 2.3 — Implement `src/openrouter_client_py/client.py`

- **Action:** Write `OpenRouterClient` class wrapping `openrouter` SDK
- **Details:**
  - Constructor stores config
  - `chat_send()` delegates to SDK, maps response to `ChatCompletion`
  - Sets auth + optional headers
- **Estimate:** 20 min
- **Depends on:** 2.2, 0.2

### Task 2.4 — Implement `src/openrouter_client_py/chat.py`

- **Action:** Write `send_chat` convenience function
- **Estimate:** 10 min
- **Depends on:** 2.3

### Task 2.5 — Implement `src/openrouter_client_py/__init__.py`

- **Action:** Re-export all public symbols
- **Estimate:** 5 min
- **Depends on:** 2.2, 2.3, 2.4

### Task 2.6 — Write `tests/test_client.py`

- **Action:** Mock SDK, write 2+ smoke tests
- **Details:**
  - Test `send_chat` with single user message
  - Test `OpenRouterClient` with config
  - Test header passing
- **Estimate:** 20 min
- **Depends on:** 2.3, 2.4

### Task 2.7 — Write `README.md`

- **Action:** Document install, quick start, client usage, types, examples
- **Estimate:** 15 min
- **Depends on:** 2.5

### Task 2.8 — Verify Python package

- **Action:** `uv sync`, `uv run pytest`
- **Gate:** All tests pass
- **Estimate:** 10 min
- **Depends on:** 2.6, 2.1

---

## Phase 3: Cross-Cut Verification

### Task 3.1 — Final verification pass

- **Action:** Re-verify both packages end-to-end
- **Details:**
  - TS: `bun install && bun test && bun run typecheck`
  - Python: `uv sync && uv run pytest`
  - Both: README examples are syntactically valid
- **Estimate:** 10 min
- **Depends on:** 1.8, 2.8

### Task 3.2 — Document implementation notes

- **Action:** Record SDK surface findings, any type adjustments made, lessons
- **Estimate:** 10 min
- **Depends on:** 3.1

---

## Task Dependency Graph

```
0.1 ──→ 0.3 ──→ 1.1 ──→ 1.2 ──→ 1.3 ──→ 1.4 ──→ 1.5 ──→ 1.7
 │                │                │                │                │
 └──→ 1.3 ◄─────┘                └──→ 1.6 ────────┘                │
 │                                                                  │
 └──→ 1.8 ←─────────────────────────────────────────────────────────┘
 │
0.2 ──→ 0.3 ──→ 2.1 ──→ 2.2 ──→ 2.3 ──→ 2.4 ──→ 2.5 ──→ 2.7
 │                │                │                │                │
 └──→ 2.3 ◄─────┘                └──→ 2.6 ────────┘                │
 │                                                                  │
 └──→ 2.8 ←─────────────────────────────────────────────────────────┘

1.8 ──→ 3.1 ←── 2.8
              │
              └──→ 3.2
```

## Parallelizable Work

The two packages are **independent** once SDK surface is known:

| Stream     | Tasks                                         | Notes                    |
| ---------- | --------------------------------------------- | ------------------------ |
| **TS**     | 1.1 → 1.2 → 1.3 → 1.4 → 1.5 → 1.6 → 1.7 → 1.8 | Sequential within TS     |
| **Python** | 2.1 → 2.2 → 2.3 → 2.4 → 2.5 → 2.6 → 2.7 → 2.8 | Sequential within Python |
| **Both**   | 1.x and 2.x can run in parallel after 0.3     |                          |

## Total Estimates

| Phase           | Tasks         | Estimated time           |
| --------------- | ------------- | ------------------------ |
| 0: Discovery    | 0.1, 0.2, 0.3 | 40 min                   |
| 1: TypeScript   | 1.1–1.8       | 95 min                   |
| 2: Python       | 2.1–2.8       | 95 min                   |
| 3: Verification | 3.1, 3.2      | 20 min                   |
| **Total**       |               | **~250 min (4.2 hours)** |

## Risks

- SDK surface may require type adjustments mid-implementation (mitigated by Phase 0)
- Mock design needs to match actual SDK response shape (mitigated by reading SDK first)
- Header-passing mechanism may differ between TS and Python SDKs (mitigated by reading both first)
