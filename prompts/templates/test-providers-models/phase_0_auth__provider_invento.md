# Phase 0: Auth & Provider Inventory

Generated: 2026-07-10
Source: `hermes auth list` (live)

## Summary

- Providers inventoried: 9 (prompt hardcodes 6 — run uses live reality)
- Credential status documented per provider.

## Provider Inventory (from `hermes auth list` 2026-07-10)

| # | Provider | Credentials | Status | Notes |
| --- | ---------- | ------------- | -------- | ------- |
| 1 | copilot | gh auth token, GITHUB_TOKEN | ⚠️ Rate-limited (429) | Both creds in cooldown (ready to retry) |
| 2 | gemini | GOOGLE_API_KEY | ⚠️ Rate-limited (429) | In cooldown (was "active" 2026-07-09) |
| 3 | huggingface | HF_TOKEN | ✅ Active | — |
| 4 | nous | device_code OAuth | ✅ Active | — |
| 5 | ollama-cloud | OLLAMA_API_KEY | ✅ Active | — |
| 6 | openai-api | manual key + OPENAI_API_KEY | ✅ Keys present | Not exported to subprocess; no free tier |
| 7 | openai-codex | device_code OAuth (×2) | ⚠️ usage_limit_reached (429) | 28d 20h cooldown |
| 8 | openrouter | OPENROUTER_API_KEY | ✅ Active | Flipped from rate-limited (was ~1h51m 2026-07-09); key in credential store, NOT subprocess env |
| 9 | xai-oauth | device_code OAuth | ✅ Active | — |

## Critical Notes

- **OpenRouter / OpenAI-API key security boundary**: keys managed by Hermes' secure
  credential store; NOT available as env vars in subprocesses. API calls must go through
  the Hermes provider chain (`hermes chat -q --provider <p>`), not raw curl/Python.
- **Rate-limit states are volatile**: gemini and openrouter flipped between 2026-07-09 and
  2026-07-10. Re-check `hermes auth list` before trusting any cached cooldown.

## Status

- ✅ Complete: 9 providers captured from `hermes auth list`
- ✅ Credential status documented per provider
- ⚠️ Action needed: Re-auth copilot, gemini (cooldown), openai-codex (28d) when windows open
