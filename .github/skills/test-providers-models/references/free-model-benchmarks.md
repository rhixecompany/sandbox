# Free Model Benchmark Data (2026-06-28)

## opencode-zen (via `https://opencode.ai/zen/v1`)

| Model | Status | Reasoning | Content Quality | Notes |
|-------|--------|-----------|----------------|-------|
| `deepseek-v4-flash-free` | ✅ Best | ✅ Full | ✅ Correct | Current global model; reasoning before content |
| `mimo-v2.5-free` | ✅ OK | ❌ None | ✅ Correct | Simple, fast, no reasoning |
| `nemotron-3-ultra-free` | ✅ OK | ❌ None | ✅ Verbose | Routed via OpenRouter; wordy |
| `north-mini-code-free` | ❌ Empty | ❌ None | ❌ Empty | Returns empty content in `content` field |
| `qwen3.6-plus-free` | ❌ Ended | — | — | Free promotion expired |
| `minimax-m3-free` | ❌ Ended | — | — | Free promotion expired |

## OpenRouter Free Models (26 available)

Key selections tested or identified:

| Model | Purpose | Notes |
|-------|---------|-------|
| `qwen/qwen3-coder:free` | Coding | Strong coder; first OpenRouter fallback |
| `nvidia/nemotron-3-ultra-550b-a55b:free` | General | 550B param model |
| `google/gemma-4-31b-it:free` | General | 31B efficient model |
| `openrouter/owl-alpha` | General | General free-tier default |
| `meta-llama/llama-3.3-70b-instruct:free` | General | 70B Llama |
| `poolside/laguna-m.1:free` | Coding | Code-focused model |
| `qwen/qwq-plus:free` | Reasoning | Reasoning model |

## Config Structure for Fallbacks

```yaml
fallback_providers:
  - provider: opencode-zen
    model: deepseek-v4-flash-free
    base_url: https://opencode.ai/zen/v1
    api_mode: chat_completions
  - provider: nous
    model: stepfun/step-3.7-flash:free
  - provider: openrouter
    model: qwen/qwen3-coder:free
    base_url: https://openrouter.ai/api/v1
    api_mode: chat_completions
```

## Bench Command (Direct API Test)

```bash
KEY=$(grep OPENCODE_ZEN_API_KEY ~/AppData/Local/hermes/.env | cut -d= -f2)
for model in "deepseek-v4-flash-free" "mimo-v2.5-free"; do
  curl -s https://opencode.ai/zen/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $KEY" \
    -d "{\"model\":\"$model\",\"messages\":[{\"role\":\"user\",\"content\":\"What is 2+2? Reply with ONLY the number.\"}],\"max_tokens\":50}" | \
  python3 -c "import sys,json; d=json.load(sys.stdin); c=d['choices'][0]['message'].get('content','') or '(empty)'; r=d['choices'][0]['message'].get('reasoning_content','') or '(none)'; print(f'content: {c}\\nreasoning: {r[:80]}')"
done
```

## Known Limitations

- `hermes config set` stores JSON values as YAML strings, not proper lists — fix manually after setting
- OpenRouter API key is in Hermes credential store, NOT available as env var in subprocesses
- `reasoning_content` field: deepseek-v4-flash-free puts thinking in this field, content is the final answer
