# Phase 0: Auth & Provider Inventory

Generated: 2026-07-09
Source: `hermes auth list` (live)

## Summary

- Providers inventoried: 8
- Credential status documented per provider.

## Provider Inventory (from `hermes auth list` 2026-07-09)

| # | Provider | Credentials | Status | Notes |
|---|----------|-------------|--------|-------|
| 1 | copilot | gh auth token, GITHUB_TOKEN | ⚠️ Rate-limited (429) | Both creds in cooldown (~22m remaining) |
| 2 | gemini | GOOGLE_API_KEY | ✅ Active | — |
| 3 | huggingface | HF_TOKEN | ✅ Active | — |
| 4 | nous | device_code OAuth | ✅ Active | — |
| 5 | ollama-cloud | OLLAMA_API_KEY | ✅ Active | — |
| 6 | openai-api | manual key + OPENAI_API_KEY (env) | ✅ Keys present | Not exported to subprocess env |
| 7 | openai-codex | device_code OAuth (2) | ⚠️ Rate-limited (429) | Usage limit reached (29d left) |
| 8 | openrouter | OPENROUTER_API_KEY | ⚠️ Rate-limited (429) | ~1h 51m remaining; key in Hermes credential store, NOT in subprocess env |
| 9 | xai-oauth | device_code OAuth | ✅ Active | — |

## Critical Notes

- **OpenRouter key security boundary**: The API key is managed by Hermes' secure credential store and is NOT available as an environment variable in subprocesses (curl, Python). API calls must go through the Hermes provider chain (`hermes chat -q --provider openrouter`).
- **OpenAI API key**: Present but not exported to subprocess environment — same security boundary applies.

## Status

- ✅ Complete: All 8 providers captured from `hermes auth list`
- ✅ Credential status documented per provider
- ⚠️ Action needed: Re-auth copilot, openai-codex, openrouter when cooldowns expire
