# Test Providers & Models — Phase 4 Report

> Generated: 2026-06-28 | Part of `/execute-all-prompts` pipeline

## Provider Inventory (7 providers)

| # | Provider | Auth | Status | Chain Priority |
|---|----------|------|--------|----------------|
| 1 | opencode-zen | API key (opencode.ai/zen) | ✅ Active | Primary |
| 2 | nous | device_code OAuth | ✅ Active | Fallback 1 |
| 3 | openrouter | OPENROUTER_API_KEY (env) | ✅ Active | Fallback 2 |
| 4 | huggingface | HF_TOKEN (env) | ✅ Active | — |
| 5 | ollama-cloud | OLLAMA_API_KEY (env) | ✅ Active | — |
| 6 | openai-api | manual key + OPENAI_API_KEY (env) | ✅ Keys present | — |
| 7 | copilot | gh auth token + GITHUB_TOKEN | ⚠️ Rate-limited (429) | — |

## Model Discovery

| Provider | Total Models | Free Models | Discovery Method |
|----------|-------------|-------------|------------------|
| OpenRouter | 339 | **26** | Live API (`openrouter.ai/api/v1/models`) |
| Nous (Catalyst) | 24 | 24 curated | Hermes model-catalog.json |
| opencode-zen | 1 | 1 (deepseek-v4-flash-free) | Config |
| HuggingFace | Varies | Varies | HF_INFERENCE_API |
| Ollama Cloud | TBD | TBD | Needs direct query |
| OpenAI API | N/A | N/A | Key not in subprocess env |
| Copilot | TBD | TBD | Rate-limited, can't query |

## OpenRouter Free Models (26)

Top free models from live API:
- meta-llama/llama-3.3-70b-instruct:free
- google/gemma-4-31b-it:free
- deepseek/deepseek-r1-distill-llama-70b:free
- microsoft/phi-3.5-mini-128k-instruct:free
- liquid/lfm-2.5-1.2b-instruct:free
- cohere/north-mini-code:free
- cognitivecomputations/dolphin-mistral-24b-venice-edition:free
(*Full list: 26 models total*)

## Verification

- [x] Phase 0: Auth & Provider Inventory — 7 providers inventoried
- [x] Phase 1: Model Catalog Discovery — OpenRouter (339/26), Nous (24), others noted
- [x] Phase 2: Free Model Extraction — 26 OpenRouter free models identified
- [ ] Phase 3-6: Recommended/Optional — Pending (requires dedicated execution)
