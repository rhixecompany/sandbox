# Phase 2: Free Model Extraction

Generated: 2026-07-10
Source: Model catalog fetch + `hermes auth list` + live benchmark validation

## Summary

- Free models extracted from provider catalogs and triaged for zero-cost access.
- Cross-referenced with credential status to identify benchmarkable models.

## Active Providers with Free/Zero-Cost Models (benchmarked 2026-07-10)

| Provider | Status | Free Model Used | Benchmarked |
|| ---------- | -------- | ----------------- | ------------- ||
| nous | ✅ Active | stepfun/step-3.7-flash:free | ✅ 15/15 tasks |
| openrouter | ✅ Active (flipped) | tencent/hy3:free | ✅ 15/15 tasks |
| huggingface | ✅ Active | HF Inference `auto` (free tier) | ✅ 15/15 tasks |
| ollama-cloud | ✅ Active | `auto` (fallback deepseek-v4-flash-free) | ✅ 15/15 tasks |
| xai-oauth | ✅ Active | Grok `auto` (free) | ✅ 15/15 tasks |

## Rate-Limited / No-Free-Tier Providers (excluded from benchmark)

| Provider | Reason | Cooldown |
|| ---------- | -------- | ---------- ||
| copilot | 429 rate-limited | ~22m |
| gemini | 429 rate-limited | unknown (volatile) |
| openai-codex | usage_limit_reached | 28d 20h |
| openai-api | keys present, paid only | n/a |

## OpenRouter (9 free models — all accessible via Hermes provider chain)

| Model ID | Description | Tier |
|| ---------- | ------------- | ------ ||
| openrouter/elephant-alpha | auto-routes to cheapest coder | ✓ Needed |
| poolside/laguna-m.1:free | free | ✓ Needed |
| tencent/hy3:free | free | ✓ Needed |
| nvidia/nemotron-3-super-120b-a12b:free | free | ☆ Recommended |
| nvidia/nemotron-3-ultra-550b-a55b:free | free | ☆ Recommended |
| inclusionai/ring-2.6-1t:free | free | ☆ Recommended |
| openrouter/pareto-code | auto-routes to cheapest coder | ☆ Recommended |
| moonshotai/kimi-k2.6 | recommended | ◇ Optional |

## Nous (0 free in catalog — free tier determined live via Portal pricing)

- Free models gated by `partition_nous_models_by_tier` at runtime
- Confirmed live: `stepfun/step-3.7-flash:free` ✅ Active

## Status

- ✅ OpenRouter free models extracted from live catalog (9)
- ✅ Nous free model confirmed live (stepfun/step-3.7-flash:free)
- ✅ 5 accessible free models benchmarked (15/15 tasks, 0 failures)
- ⚠️ copilot / gemini / openai-codex excluded (rate-limited); openai-api (paid only)
