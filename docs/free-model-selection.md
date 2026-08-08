# Free Model Selection — 2026-08-07

Verified live (HTTP probes run 2026-08-07). Working = ready for fallback chain.

## Working Free Models by Provider

| Provider     | Model                                              | Ctx  | Reasoning | Status  |
| ------------ | -------------------------------------------------- | ---- | --------- | ------- |
| opencode-zen | deepseek-v4-flash-free (PRIMARY)                   | 128K | ✓         | working |
| opencode-zen | nemotron-3-ultra-free                              | 1M   | ✓         | working |
| openrouter   | nvidia/nemotron-3-ultra-550b-a55b:free             | 1M   | ✓         | working |
| openrouter   | nvidia/nemotron-3-super-120b-a12b:free             | 1M   | ✓         | working |
| openrouter   | nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free | 256K | ✓         | working |
| openrouter   | google/gemma-4-31b-it:free                         | 262K | no        | working |
| openrouter   | google/gemma-4-26b-a4b-it:free                     | 262K | no        | working |
| openrouter   | openai/gpt-oss-20b:free                            | 131K | no        | working |
| gemini       | gemini-2.5-flash                                   | 1M   | yes       | working |
| ollama-cloud | nemotron-3-ultra                                   | 1M   | ✓         | working |

## Not usable right now (per probe)

- **deepseek** direct API: 402 Payment Required (no credit). Its model `deepseek-v4-flash` is still usable via opencode-zen (primary).
- **huggingface**: token valid + endpoint reachable, but zero inference providers enabled -> all model calls 400.
- **nous**: 403 Cloudflare block on /models.
- **xai-oauth**: personal-team spending limit (402).
- **openai-codex**: oauth rate-limited (429).

## Configured fallback chain (provider level, ordered by rule)

Rule: **vision → reasoning → context size** (no working free model has vision,
so effective order is reasoning → context). Configured 2026-08-08 via
`/test-providers-models`.

- model.provider = opencode-zen
- model.default = deepseek-v4-flash-free (PRIMARY, proven working)
- fallback_providers (ordered):
  1. opencode-zen → deepseek-v4-flash-free (128K, reasoning✓)
  2. openrouter → nvidia/nemotron-3-ultra-550b-a55b:free (1M, ✓)
  3. gemini → gemini-2.5-flash (1M, ✓)
  4. ollama-cloud → nemotron-3-ultra (1M, ✓)

Full working-model ranking (per-provider default_model above):

1. nemotron-3-ultra-free (opencode-zen, 1M, ✓)
2. nvidia/nemotron-3-ultra-550b-a55b:free (openrouter, 1M, ✓)
3. nvidia/nemotron-3-super-120b-a12b:free (openrouter, 1M, ✓)
4. gemini-2.5-flash (gemini, 1M, ✓)
5. nemotron-3-ultra (ollama-cloud, 1M, ✓)
6. nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free (openrouter, 256K, ✓)
7. deepseek-v4-flash-free (opencode-zen, 128K, ✓) — PRIMARY
8. google/gemma-4-31b-it:free (openrouter, 262K, ✗)
9. google/gemma-4-26b-a4b-it:free (openrouter, 262K, ✗)
10. openai/gpt-oss-20b:free (openrouter, 131K, ✗)
