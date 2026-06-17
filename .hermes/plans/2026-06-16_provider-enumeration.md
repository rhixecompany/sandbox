# Phase 5: Provider Enumeration
**Date:** 2026-06-16

## Active Model/Provider

| Field | Value |
|-------|-------|
| **Active Model** | `gpt-5.4-mini` |
| **Active Provider** | `openai-codex` |
| **Base URL** | `https://chatgpt.com/backend-api/codex` |
| **Config Version** | 29 |
| **Personality** | `concise` |

## Fallback Chain (from `fallback_providers`)

| Priority | Provider | Model | Base URL |
|----------|----------|-------|----------|
| 1 | openrouter | poolside/laguna-m.1:free | https://openrouter.ai/api/v1 |
| 2 | openrouter | openrouter/owl-alpha | https://openrouter.ai/api/v1 |
| 3 | nous | nvidia/nemotron-3-ultra:free | https://inference-api.nousresearch.com/v1 |
| 4 | nous | stepfun/step-3.7-flash:free | https://inference-api.nousresearch.com/v1 |

## Assembly Table: Provider | Where Defined | Env Key | Key Present | Role

| Provider | Where Defined | Env Key | Key Present | Role |
|----------|---------------|---------|-------------|------|
| openai-codex | config.yaml `model:` | OPENAI_API_KEY | ✅ | Primary (active) |
| openrouter | config.yaml `fallback_providers` | OPENROUTER_API_KEY | ✅ | Fallback #1, #2 |
| nous | config.yaml `fallback_providers` | NOUS_BASE_URL | ❌ (not set) | Fallback #3, #4 |
| openrouter (plugin) | plugins.enabled | OPENROUTER_API_KEY | ✅ | Model provider plugin |

## Defined Provider Blocks in config.yaml

| Block | Status | Notes |
|-------|--------|-------|
| `model:` | Active | openai-codex / gpt-5.4-mini |
| `fallback_providers:` | Active | 4 entries (openrouter×2, nous×2) |
| `providers:` | Empty `{}` | No inline provider definitions |
| `openrouter:` | Configured | min_coding_score: 0.65, response_cache: true |
| `bedrock:` | Configured | discovery enabled, no region set |
| `credential_pool_strategies:` | Configured | copilot: fill_first |

## Environment Keys Found in .env

| Key | Status |
|-----|--------|
| OPENROUTER_API_KEY | ✅ Present |
| OPENAI_API_KEY | ✅ Present |
| TAVILY_API_KEY | ✅ Present |
| HF_TOKEN | ✅ Present |
| OLLAMA_API_KEY | ✅ Present |
| MINDSTUDIO_API_KEY | ✅ Present |
| BROWSER_INACTIVITY_TIMEOUT | ✅ Present |
| BROWSER_SESSION_TIMEOUT | ✅ Present |
| BROWSERBASE_ADVANCED_STEALTH | ✅ Present |
| BROWSERBASE_PROXIES | ✅ Present |
| IMAGE_TOOLS_DEBUG | ✅ Present |
| MOA_TOOLS_DEBUG | ✅ Present |
| TERMINAL_ENV | ✅ Present |
| TERMINAL_LIFETIME_SECONDS | ✅ Present |
| TERMINAL_MODAL_IMAGE | ✅ Present |
| TERMINAL_TIMEOUT | ✅ Present |
| VISION_TOOLS_DEBUG | ✅ Present |
| WEB_TOOLS_DEBUG | ✅ Present |

## Key Observations

1. **Primary provider is openai-codex** — errors.log shows repeated 401 "token_invalidated" errors for this provider (as of 2026-06-16 23:38-23:51). The OpenAI Codex token appears to be invalidated.
2. **OpenRouter rate limiting** — errors.log shows 429 "free-models-per-day" exceeded for poolside/laguna-m.1:free fallback.
3. **NOUS_BASE_URL not set** — the nous fallback providers reference `https://inference-api.nousresearch.com/v1` directly in base_url, but the NOUS_BASE_URL env var is not configured.
4. **Active model in .hermes.md says nvidia/nemotron-3-ultra:free** — this contradicts config.yaml which has `model.default: gpt-5.4-mini` / `model.provider: openai-codex`. The .hermes.md is stale.
