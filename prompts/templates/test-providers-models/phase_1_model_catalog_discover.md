# Phase 1: Model Catalog Discovery

Generated: 2026-07-09
Source: `hermes config show`, model catalog fetch (live)

## Summary
- OpenRouter: 27 models (from catalog fetch)
- Nous: 21 models (from catalog fetch)
- Other providers: discovered via auth + config
- Total accessible: 48+ models cataloged

## Model Catalogs Per Provider

### OpenRouter (from https://hermes-agent.nousresearch.com/docs/api/model-catalog.json)
**Models: 27 total**
- Free models: 9 (openrouter/elephant-alpha, openrouter/owl-alpha, poolside/laguna-m.1:free, tencent/hy3-preview:free, nvidia/nemotron-3-super-120b-a12b:free, nvidia/nemotron-3-ultra-550b-a55b:free, inclusionai/ring-2.6-1t:free, openrouter/pareto-code, moonshotai/kimi-k2.6)
- Premium: 18 (Claude 4.8/5, GPT 5.4/5.5, Gemini 3/3.5, Grok 4.3, DeepSeek v4, Qwen 3.6/3.7, etc.)

### Nous Portal (from same catalog)
**Models: 21 total**
- All premium models (no free tier indicated in catalog)
- Same model IDs as OpenRouter but no `:free` variants
- Free-tier gating determined live via Portal pricing (partition_nous_models_by_tier)

### Other Providers (from `hermes auth list` + config)
| Provider | Auth Status | Model Access Method |
|----------|-------------|---------------------|
| copilot | Rate-limited | GitHub Copilot CLI / VS Code |
| gemini | Active | `gemini-3.5-flash` (default in config) |
| huggingface | Active | HF Inference API (model TBD at runtime) |
| ollama-cloud | Active | ollama-cloud hosted models |
| openai-api | Keys present | Manual model selection |
| openai-codex | Rate-limited | Codex CLI models |
| xai-oauth | Active | Grok models via xAI |

## Status
- ✅ Complete: OpenRouter & Nous catalogs fetched from live source
- ✅ Other providers cataloged via auth + config
- ⚠️ Rate-limited providers (copilot, openai-codex, openrouter) need re-auth for full catalog
