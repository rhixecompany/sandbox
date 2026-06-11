# Provider Auth Matrix

Quick reference for provider health checks and common issues.

| Provider | Env Key | Config Key | Common Issues | Status |
|----------|---------|------------|---------------|--------|
| GitHub Copilot | `GITHUB_TOKEN` | `copilot` | Rate limit (weekly ~50 calls/min), PAT must have `gist` scope | ✓ Recommended |
| OpenAI | `OPENAI_API_KEY` | `openai` | 429 quota exceeded, free trial exhausted (3 months), payment method lapsed | ⚠️ Often out |
| OpenRouter | `OPENROUTER_API_KEY` | `openrouter` | Insufficient credits, payment method expired, model deprecated | ⚠️ Often out |
| Google Gemini | `GOOGLE_API_KEY` | `google` | Free tier quota 250k tokens/day, resets daily at UTC midnight | ⚠️ Limited free |
| xAI Grok | `XAI_API_KEY` | `xai` | Rarely configured, free tier limited | ❌ Not active |
| OpenCode | N/A | `opencode` | Payment method missing, no fallback credentials | ❌ Disabled |

## Health Check Pattern

When all providers fail with 429/402/401:
1. Check which provider is primary: `grep "^model:" config.yaml`
2. If primary is over limit, fallback chain kicks in automatically
3. Check `errors.log` for "unhealthy 600s" markers — providers in cooldown
4. If all unhealthy: wait 10min (cooldown expires) or switch primary
5. Last resort: use copilot (GitHub Copilot) — usually has budget

## Error Code Meanings

| Code | Meaning | Recovery |
|------|---------|----------|
| 429 | Rate limit (quota or RPS exceeded) | Wait or upgrade plan |
| 402 | Payment required (insufficient credits/balance) | Add payment method or credits |
| 401 | Unauthorized (wrong key, expired token) | Re-authenticate via `hermes auth` |
| 403 | Forbidden (model deprecated, region restricted) | Update model name in config |
| 500 | Server error (provider issue) | Wait and retry; rarely your problem |

## Session-Specific Notes

**2026-05-27 (current session):**
- Copilot (primary): Healthy, claude-haiku-4.5 active ✓
- gpt-5-mini (fallback): Available as secondary ✓
- OpenRouter: Out of credits (402) — disabled
- Gemini: Free tier exhausted (429) — disabled
- OpenCode: All models missing payment method — disabled
- Root cause of failover chain: System disk 99% full was blocking provider retries early

**Recommendation:** Keep copilot as primary; maintain gpt-5-mini as fallback. Do not re-enable others until user funds them.
