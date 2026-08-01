# Providers & Models Full Report — 2026-07-24

## Provider Overview

| Provider                   | Auth           | Rate Limit     | Models (local)             | Free Tier                    |
| -------------------------- | -------------- | -------------- | -------------------------- | ---------------------------- |
| **opencode-zen** (primary) | API key        | ✅ OK          | 1 (deepseek-v4-flash-free) | ✅ Primary model             |
| **openrouter** (fallback)  | API key        | ⚠️ 429 (~5h)   | 39 catalogged              | ✅ 17+ free                  |
| **copilot**                | 3 creds        | ✅ OK          | Varies by plan             | ✅ Included in sub           |
| **huggingface**            | HF_TOKEN       | ✅ OK          | 1000s (hub)                | ✅ 300 req/h free            |
| **nous**                   | OAuth          | ✅ OK          | 31 catalogged              | ❌ (Ling-3.0-flash free 1wk) |
| **openai-api**             | 2 creds        | ✅ OK          | GPT series                 | ❌ paid                      |
| **openai-codex**           | OAuth          | ⚠️ 429 (14d)   | Codex CLI                  | ❌ paid                      |
| **gemini**                 | GOOGLE_API_KEY | ⚠️ 429 (ready) | Gemini series              | ✅ free tier on AI Studio    |
| **ollama-cloud**           | OLLAMA_API_KEY | ✅ OK          | Unknown                    | ❌ paid                      |
| **xai-oauth**              | OAuth          | ✅ OK          | Grok series                | ❌ paid                      |

## Free Models Available (16 distinct)

### OpenRouter Free (17+ models — from web research)

poolside/laguna-m.1:free · poolside/laguna-xs-2.1:free · qwen/qwen3-next-80b-a3b-instruct:free · tencent/hy3:free · cohere/north-mini-code:free · nvidia/nemotron-3-nano-30b-a3b:free · nvidia/nemotron-3-super-120b-a12b:free · nvidia/nemotron-nano-9b-v2:free · google/gemma-4-26b-a4b-it:free · openai/gpt-oss-20b:free · openai/gpt-oss-120b:free · nvidia/nemotron-3-ultra:free · nvidia/nemotron-3-super:free · google/gemma-4-31b-it:free · inclusionai/ring-2.6-1t:free · deepseek/deepseek-chat-v3-0324:free (rotated out?)

### HuggingFace Free Tier

- 300 requests/hour (registered), 1000/h (Pro $9/mo)
- Thousands of models via Serverless Inference API

### Nous Portal

- 0 permanent free models; Ling-3.0-flash free for promotional week

## Fallback Chain (10 deep, all openrouter)

Primary → nemotron-3-ultra → hy3 → laguna-m.1 → laguna-xs-2.1 → nemotron-3-super → north-mini-code → gemma-4-26b → gpt-oss-20b → nemotron-3-nano → nemotron-nano-9b

**Vulnerability:** Entire fallback chain routes through openrouter. If openrouter is rate-limited (currently is), all 10 fallbacks fail. Recommended: add copilot or huggingface as a non-openrouter fallback.

## Recommendations

1. **Add copilot fallback** — copilot has 3 creds, OK rate limit, works without openrouter
2. **Add huggingface fallback** — 300 req/h free, diverse model catalog
3. **Update test script** to include web research phase for provider info refresh
4. **Re-check openrouter rate limit** before benchmarking — currently 429 with ~5h remaining
