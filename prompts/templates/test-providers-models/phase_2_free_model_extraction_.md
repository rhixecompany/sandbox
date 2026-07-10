# Phase 2: Free Model Extraction

Generated: 2026-07-09
Source: Model catalog fetch + `hermes auth list` + live validation

## Summary
- Free models extracted from provider catalogs and triaged for zero-cost access.
- Cross-referenced with credential status to identify benchmarkable models.

## Free Models by Provider

### OpenRouter (from catalog - 9 free models)
| Model ID | Description | Benchmarkable |
|----------|-------------|---------------|
| openrouter/elephant-alpha | Free | ⚠️ Provider rate-limited (429) |
| openrouter/owl-alpha | Free | ⚠️ Provider rate-limited (429) |
| poolside/laguna-m.1:free | Free | ⚠️ Provider rate-limited (429) |
| tencent/hy3-preview:free | Free | ⚠️ Provider rate-limited (429) |
| nvidia/nemotron-3-super-120b-a12b:free | Free | ⚠️ Provider rate-limited (429) |
| nvidia/nemotron-3-ultra-550b-a55b:free | Free | ⚠️ Provider rate-limited (429) |
| inclusionai/ring-2.6-1t:free | Free | ⚠️ Provider rate-limited (429) |
| openrouter/pareto-code | Auto-routes to cheapest coder | ⚠️ Provider rate-limited (429) |
| moonshotai/kimi-k2.6 | Recommended (free tier) | ⚠️ Provider rate-limited (429) |

### Nous Portal (21 models - no free tier in catalog)
Free-tier gating determined live via Portal pricing (`partition_nous_models_by_tier`). Tested: `stepfun/step-3.7-flash:free` ✅ Active.

### Active Providers with Free/Zero-Cost Models
| Provider | Status | Known Free Model(s) | Tested |
|----------|--------|---------------------|--------|
| gemini | ✅ Active | gemini-3.5-flash (default) | ✅ Tested |
| huggingface | ✅ Active | HF Inference API free tier | ⏳ Pending |
| nous | ✅ Active | stepfun/step-3.7-flash:free | ✅ Tested |
| ollama-cloud | ✅ Active | ollama-cloud hosted models | ⏳ Pending |
| openai-api | ✅ Keys present | Manual model selection | ⏳ Pending |
| xai-oauth | ✅ Active | Grok models via xAI | ⏳ Pending |

### Rate-Limited Providers (need re-auth)
| Provider | Free Models | Cooldown |
|----------|-------------|----------|
| copilot | GitHub Copilot models | ~22m |
| openai-codex | Codex CLI models | 29d |
| openrouter | 9 free models (see above) | ~1h 51m |

## Benchmark Candidates (Accessible Free Models)
1. **gemini-3.5-flash** (gemini) — ✅ Active, tested
2. **stepfun/step-3.7-flash:free** (nous) — ✅ Active, tested
3. **HF Inference free tier** (huggingface) — ⏳ To test
4. **ollama-cloud models** (ollama-cloud) — ⏳ To test
5. **xAI Grok** (xai-oauth) — ⏳ To test

## Status
- ✅ OpenRouter catalog parsed (9 free models, provider rate-limited)
- ✅ Nous catalog parsed (21 models, free tier live-gated)
- ✅ Active providers identified (6/9 with free access)
- ⏳ Phase 3: Benchmark the 5 accessible candidates

### OpenRouter (9 free models — all accessible via Hermes provider chain)
| Model ID | Description | Tier |
|----------|-------------|------|
| openrouter/elephant-alpha | auto-routes to cheapest coder meeting openrouter.min_coding_score | ✓ Needed |
| openrouter/owl-alpha | free | ✓ Needed |
| poolside/laguna-m.1:free | free | ✓ Needed |
| tencent/hy3-preview:free | free | ✓ Needed |
| nvidia/nemotron-3-super-120b-a12b:free | free | ☆ Recommended |
| nvidia/nemotron-3-ultra-550b-a55b:free | free | ☆ Recommended |
| inclusionai/ring-2.6-1t:free | free | ☆ Recommended |
| openrouter/pareto-code | auto-routes to cheapest coder | ☆ Recommended |
| moonshotai/kimi-k2.6 | recommended | ◇ Optional |

### Nous (0 free in catalog — free tier determined live via Portal pricing)
- Free models gated by `partition_nous_models_by_tier` at runtime
- Must test via `hermes chat --provider nous` to discover actual free models

### Ollama-Cloud (models TBD at runtime)
- Active auth, model list fetched via API at benchmark time

### OpenAI-API (keys present, no free tier)
- Manual key — paid models only

### xAI-OAuth (models TBD at runtime)
- Active auth, Grok models available via xAI portal

## Status
- ✅ OpenRouter free models extracted from live catalog
- ✅ Nous free model discovery requires live testing
- ⏳ Ollama-Cloud, xAI-OAuth require benchmark execution
- ⚠️ OpenAI-API has no free models