# Free Model Selection — Verified Fallback Chain

Generated: 2026-08-08

## Ordered Fallback Chain (vision → reasoning → context size)

| Rank | Provider     | Model                                              | Context | Reasoning | Vision | Status               |
| ---- | ------------ | -------------------------------------------------- | ------- | --------- | ------ | -------------------- |
| 1    | opencode-zen | deepseek-v4-flash-free                             | 128K    | ✅        | ❌     | ✅ WORKING (Primary) |
| 2    | opencode-zen | nemotron-3-ultra-free                              | 1M      | ❌        | ❌     | ✅ WORKING           |
| 3    | openrouter   | nvidia/nemotron-3-ultra-550b-a55b:free             | 1M      | ❌        | ❌     | ✅ WORKING           |
| 4    | gemini       | gemini-2.5-flash                                   | 1M      | ✅        | ❌     | ✅ WORKING           |
| 5    | ollama-cloud | nemotron-3-ultra                                   | 1M      | ❌        | ❌     | ✅ WORKING           |
| 6    | openrouter   | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | 256K    | ✅        | ❌     | ✅ WORKING           |
| 7    | openrouter   | google/gemma-4-31b-it:free                         | 262K    | ❌        | ❌     | ✅ WORKING           |
| 8    | openrouter   | google/gemma-4-26b-a4b-it:free                     | 262K    | ❌        | ❌     | ✅ WORKING           |
| 9    | openrouter   | openai/gpt-oss-20b:free                            | 131K    | ❌        | ❌     | ✅ WORKING           |

## Configuration Applied

```yaml
model:
  provider: opencode-zen
  default: deepseek-v4-flash-free

fallback_providers:
  - opencode-zen
  - openrouter
  - gemini
  - ollama-cloud

providers:
  opencode-zen:
    default_model: deepseek-v4-flash-free
  openrouter:
    default_model: nvidia/nemotron-3-ultra-550b-a55b:free
  gemini:
    default_model: gemini-2.5-flash
  ollama-cloud:
    default_model: nemotron-3-ultra
```

## Excluded Providers (non-working free tier)

| Provider     | Reason                     |
| ------------ | -------------------------- |
| deepseek     | 402 Payment Required       |
| huggingface  | 400 Bad Request            |
| nous         | 403 Forbidden              |
| xai-oauth    | 402 Payment Required       |
| openai-codex | 429 Rate Limited           |
| copilot      | Not usable as LLM provider |

## Verification

```bash
hermes config check  # ✅ passes
# fallback_providers is a real YAML list (not string)
# Each provider resolves to a working free default_model
```
