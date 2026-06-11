# OpenCode Zen Free Tier — Model Probing Reference

**Last probed:** 2026-05-27  
**Method:** Direct HTTP POST + `hermes chat -q -m MODEL --provider opencode-zen -Q`

## Provider Config

```yaml
model:
  default: big-pickle
  provider: opencode-zen
  base_url: https://opencode.ai/zen/v1
  api_mode: chat_completions
```

The `api_mode: chat_completions` tells Hermes to append `/chat/completions` internally. Do NOT set base_url to the full path — it will break Hermes' internal routing.

## Available Models (from `/v1/models`)

45 models listed across families: Claude 4.x, GPT-5.x, Gemini 2.5/3, Qwen 3.5/3.6, DeepSeek, Grok, GLM, MiniMax, Kimi, Mimo, Nemotron.

## Free Tier (no API key required)

| Model ID | Cutoff | Actual Backend | Status |
|---|---|---|---|
| `big-pickle` | 2025-01 | deepseek-v4-flash | ✅ Active (aliased) |
| `deepseek-v4-flash-free` | 2025-04 | deepseek-v4-flash | ✅ Active |
| `nemotron-3-super-free` | 2024-06 | nvidia/nemotron-3-super | ✅ Active |
| `minimax-m2.5-free` | — | — | ❌ "Free promotion ended" |
| `qwen3.6-plus-free` | — | — | ❌ Deprecated May 2026 |
| `mimo-v2.5-free` | — | — | ❌ No response |

## Paid Tiers (require OPENCODE_ZEN_API_KEY or OAuth)

All Claude, GPT, Gemini, Qwen-plus, Grok, GLM, MiniMax, Kimi models return:
- **Without auth:** `Missing API key`
- **With expired auth:** `HTTP 403 error code 1010` (Cloudflare WAF) or `Invalid API key`

The OPENCODE_ZEN_API_KEY in `.env` returns `Invalid API key` for paid models — likely expired or the account's free tier ended.

## Cloudflare WAF Behavior

**Error code 1010** = "The owner of this website has banned your access based on your browser's signature." This is Cloudflare's bot/rate-limit protection.

**Trigger conditions observed:**
- More than ~5 rapid POST requests within 60 seconds from the same IP
- The first 1-2 requests succeed, then 1010 starts
- Block lasts 30-60 seconds after last request

**Workaround:**
- Insert 3-second delays between requests
- Better: use `hermes chat -q` which routes through Hermes' auth proxy (handles retries) rather than direct curl
- If 403d, wait 60 seconds before retrying

## Testing Command

```bash
# Via Hermes CLI (handles auth + retries)
hermes chat -q "Reply with ONLY 'CUTOFF: YYYY-MM'" -m deepseek-v4-flash-free --provider opencode-zen -Q

# Via direct curl (no auth needed for free models)
curl -s -X POST https://opencode.ai/zen/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{"model":"deepseek-v4-flash-free","messages":[{"role":"user","content":"Your cutoff?"}],"max_tokens":80}'
```
