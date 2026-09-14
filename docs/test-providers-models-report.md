# Test Providers Models — Final Report

Date: 2026-09-14
Providers tested: opencode-zen, openrouter, nous, deepseek, ollama-cloud

## Provider Inventory (from `hermes auth list`)

| Provider | Credentials | Status |
|----------|-------------|--------|
| openrouter | OPENROUTER_API_KEY (env) | ✅ Active |
| opencode-zen | OPENCODE_ZEN_API_KEY (env) + zen-backup (401) | ✅ Primary active |
| nous | rhixecompany@gmail.com (oauth) | ✅ Active |
| deepseek | DEEPSEEK_API_KEY (env) | ✅ Active |
| ollama-cloud | OLLAMA_API_KEY (env) | ✅ Active |
| openai-codex | device_code (oauth) | ✅ Active |
| minimax | MINIMAX_API_KEY (env) | ✅ Active |
| gemini | GOOGLE_API_KEY (env) | ✅ Active |
| huggingface | HF_TOKEN (env) | ✅ Active |
| copilot | GITHUB_TOKEN + COPILOT_GITHUB_TOKEN | ✅ Active |
| xai | api-key-1 (403), XAI_API_KEY (env) | ⚠️ One credential failed |

## Current Hermes Model Config (after update)

- **Default model**: `deepseek-v4-flash-free`
- **Provider**: `opencode-zen`
- **Base URL**: `https://openrouter.ai/api/v1`
- **Fallback**: `["openrouter", "nous", "deepseek"]`

## Benchmark Results

| Model | Provider | Status | Reason |
|---|---|---|---|
| deepseek-v4-flash-free | opencode-zen | ❌ fail | HTTP 400 Model unavailable |
| mimo-v2.5-free | opencode-zen | ✅ pass | Cutoff Dec 2024, 1M ctx, reasoning ✓ |
| inclusionai/ling-3.0-flash-sante:free | openrouter | ❌ fail | HTTP 429 Rate limited (0/50 remaining) |
| nvidia/nemotron-3.5-lightning:free | openrouter | ❌ fail | HTTP 429 Rate limited |
| cohere/north-mini-code:free | openrouter | ❌ fail | HTTP 429 Rate limited |
| nemotron-3-ultra-free | nous | ❌ fail | HTTP 404 Model not found |
| deepseek-v4-flash | deepseek | ❌ fail | HTTP 402 Insufficient Balance |

## Config Changes Applied

- `model.provider` → `opencode-zen`
- `model.default` → `deepseek-v4-flash-free`
- `fallback_providers` → `["openrouter", "nous", "deepseek"]`

## Artifacts Created

- `docs/openrouter-free-models-report.md` — 17 free models cataloged
- `docs/opencode-zen-openrouter-setup-report.md` — provider setup + best practices
- `docs/benchmark-results.json` — benchmark results (7 models)
- `docs/benchmark-results.md` — human-readable benchmark summary
- `docs/test-providers-models-report.md` — this report