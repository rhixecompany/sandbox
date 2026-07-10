# Phase 3: Provider-by-Provider Benchmarking

Generated: 2026-07-09
Target: 5 accessible free models + rate-limited candidates (when available)

## Benchmark Tasks (3 standard tasks per model)

1. **Reasoning** — Multi-step logic problem (river crossing puzzle)
2. **Tool Calling** — Execute a function with structured args (get_weather)
3. **Knowledge** — Factual QA with citation requirement

## Execution Matrix

| Provider | Model | Status | Reasoning | Tool Calling | Knowledge | Notes |
|----------|-------|--------|-----------|--------------|-----------|-------|
| gemini | gemini-3.5-flash | ✅ Complete | ✅ 43s | ✅ 41s | ✅ 37s | Default in config |
| nous | stepfun/step-3.7-flash:free | ✅ Complete | ✅ 49s | ✅ 44s | ✅ 76s | Tested active |
| huggingface | HF Inference (auto) | ✅ Complete | ✅ 110s | ✅ 130s | ✅ 63s | Auto-selected |
| ollama-cloud | auto | ✅ Complete | ✅ 58s | ✅ 48s | ✅ 53s | Auth active, fallback to deepseek |
| xai-oauth | auto | ✅ Complete | ✅ 38s | ✅ 47s | ✅ 85s | Auth active, fallback to deepseek |
| openrouter | openrouter/owl-alpha | ⚠️ Rate-limited | — | — | — | ~1h cooldown |
| openrouter | nvidia/nemotron-3-ultra-550b-a55b:free | ⚠️ Rate-limited | — | — | — | ~1h cooldown |
| copilot | GitHub Copilot | ⚠️ Rate-limited | — | — | — | ~22m cooldown |

## Test Harness

- Script: `scripts/benchmark_providers.py`
- Uses `hermes chat -q "..." --provider <p> --model <m>` pattern
- Outputs JSON results for Phase 4 comparison

## Rate Limit Strategy

- ✅ Run accessible models first (gemini, nous, huggingface, ollama-cloud, xai-oauth)
- ⚠️ Queue rate-limited models with backoff (monitor `hermes auth list` for cooldown)
- 📝 Document auth failures and rate limits per provider/model

## Status

- ✅ 5/5 accessible models complete (15 tasks)
- ⚠️ 3 rate-limited models need cooldown monitoring
