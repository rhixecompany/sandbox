# Phase 1: Model Catalog Discovery

Generated: 2026-07-10
Source: `hermes config show`, model catalog fetch (live)

## Summary

- OpenRouter: 40 models (from catalog fetch)
- Nous: 30 models (from catalog fetch)
- Free/zero-cost models identified per accessible provider
- Other providers resolve models at runtime via `auto` / Portal fallback

## Model Catalogs Per Provider

### OpenRouter (from <https://hermes-agent.nousresearch.com/docs/api/model-catalog.json>)

**Models: 40 total**

- Free models (9): `openrouter/elephant-alpha`, `poolside/laguna-m.1:free`,
  `tencent/hy3:free`, `nvidia/nemotron-3-super-120b-a12b:free`,
  `nvidia/nemotron-3-ultra-550b-a55b:free`, `inclusionai/ring-2.6-1t:free`,
  `openrouter/pareto-code` (auto-routes), `moonshotai/kimi-k2.6` (recommended),
  `tencent/hy3` (non-free).
- Premium: Claude 4.8/5, GPT 5.4/5.5/5.6, Gemini 3/3.1/3.5, Grok 4.5, DeepSeek v4,
  Qwen 3.6/3.7, etc.

### Nous Portal (from same catalog)

**Models: 30 total**

- No free flag in catalog; free tier gated live via Portal pricing
  (`partition_nous_models_by_tier`).
- Confirmed live free model: `stepfun/step-3.7-flash:free` ✅ Active.

### Other Providers (from `hermes auth list` + config)

| Provider | Auth Status | Model Access Method |
| ---------- | ------------- | --------------------- |
| copilot | Rate-limited (429) | GitHub Copilot CLI / VS Code |
| gemini | Rate-limited (429) | `gemini-3.5-flash` (default in config) |
| huggingface | Active | HF Inference API (`auto`, free tier) |
| ollama-cloud | Active | ollama-cloud hosted (`auto`, fallback deepseek-v4-flash-free) |
| openai-api | Keys present | Manual model selection (paid only) |
| openai-codex | Rate-limited (usage) | Codex CLI models |
| xai-oauth | Active | Grok models via xAI (`auto`) |

## Status

- ✅ Complete: OpenRouter & Nous catalogs fetched from live source
- ✅ Other providers cataloged via auth + config
- ⚠️ Rate-limited providers (copilot, gemini, openai-codex) excluded from benchmark pool
