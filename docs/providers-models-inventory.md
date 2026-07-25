# Provider & Model Inventory

> Generated: 2026-07-16 | Orchestrator Phase 5

## Summary

| Provider | Status | Models | Free Models |
| ---------- | -------- | -------- | ------------- |
| OpenCode Zen | Active | ~50+ | 10+ |
| OpenRouter | Active | 342 | 23 free |
| Nous Research | Active | ~30+ | 10+ |
| NVIDIA NIM | Available | ~50+ | 15+ |
| Gemini | Rate-limited (429) | — | — |
| Ollama Cloud | Configured | — | — |
| OpenAI Codex | Rate-limited | — | — |

## Current Config

| Setting | Value |
| --------- | ------- |
| **Primary Model** | `stepfun/step-3.7-flash:free` (Nous) |
| **Fallback** | OpenRouter → Qwen Qwen3 Coder (free) |
| **Provider** | opencode-zen → nous → openrouter |
| **Base URL** | `https://inference-api.nousresearch.com/v1` |

## OpenRouter Free Models (23)

| Model | Provider |
| ------- | ---------- |
| tencent/hy3:free | Tencent |
| poolside/laguna-xs-2.1:free | Poolside |
| nvidia/nemotron-3-ultra-550b-a55b:free | NVIDIA |
| nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | NVIDIA |
| nvidia/nemotron-3-super-120b-a12b:free | NVIDIA |
| nvidia/nemotron-nano-12b-v2-vl:free | NVIDIA |
| nvidia/nemotron-nano-9b-v2:free | NVIDIA |
| nvidia/nemotron-3.5-content-safety:free | NVIDIA |
| poolside/laguna-m.1:free | Poolside |
| google/gemma-4-26b-a4b-it:free | Google |
| google/gemma-4-31b-it:free | Google |
| google/lyria-3-pro-preview | Google |
| google/lyria-3-clip-preview | Google |
| qwen/qwen3-next-80b-a3b-instruct:free | Qwen |
| qwen/qwen3-coder:free | Qwen |
| openai/gpt-oss-20b:free | OpenAI |
| openrouter/free | Wildcard |
| cohere/north-mini-code:free | Cohere |
| cognitivecomputations/dolphin-mistral-24b-venice-edition | Community |

## Credentials Summary

| Provider | Auth Type | Status |
| ---------- | ----------- | -------- |
| Copilot | GitHub Token | Active |
| Gemini | API Key | Rate-limited (429) |
| HuggingFace | HF_TOKEN | Active |
| Nous | OAuth (device) | Active |
| Ollama Cloud | API Key | Active |
| OpenAI API | API Key | Active |
| OpenAI Codex | OAuth | Rate-limited (23d left) |
| OpenRouter | API Key | Active |
| xAI | OAuth | Exhausted |

## Recommendations

- **Current setup optimal** for free-tier usage (Nous → OpenRouter fallback)
- OpenRouter's 23 free models provide good redundancy
- NVIDIA NIM could be added as an additional fallback via custom provider config
- Gemini rate limit recovers automatically; no action needed
