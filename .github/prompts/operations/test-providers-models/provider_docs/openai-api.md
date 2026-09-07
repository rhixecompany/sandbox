---
name: auth-inventory-openai-api
description: Rendered per-provider auth inventory captured by test-providers-models on 2026-09-07 15:07 UTC.
---

# Auth inventory — openai-api

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on 2026-09-07 15:07 UTC.
> Classified using `scripts/render_auth_inventory.py` (status mapping table).

## Summary

- **Provider:** `openai-api`
- **Key env:** `OPENAI_API_KEY`
- **Status:** **exhausted-402**
- **Rate / auth notes:** exhausted (402) (ready to retry) | exhausted (402) (ready to retry) ← | exhausted (402) (ready to retry)
- **Docs:** https://platform.openai.com/docs
- **Auth file verified:** `~/AppData/Local/hermes/auth.json (provider=openai-api)`
- **Auth mechanism:** api_key
- **Inference endpoint:** `https://api.openai.com/v1`

## Credentials

| # | Key name | Type | Source | Note |
|---|----------|------|--------|------|
| #1 | `OPENAI_API_KEY` | api_key | `env:OPENAI_API_KEY` | exhausted (402) (ready to retry) |
| #2 | `api-key-1` | api_key | `manual` | exhausted (402) (ready to retry) ← |
| #3 | `api-key-3` | api_key | `manual` | exhausted (402) (ready to retry) |
| #4 | `api-key-4` | api_key | `manual` | _(no note)_ |
| #5 | `api-key-2` | api_key | `manual` | _(no note)_ |

## Configuration cross-check

- `~/AppData/Local/hermes/config.yaml` should reference this provider's model
  format (`openai-api:<model-id>`) for the primary model and any fallbacks.
- If status is `valid`, the provider is probe-eligible.
- If status is `rate-limited-429` or `exhausted-402`, probes will likely fail;
  the provider should be skipped in Phase 3.
- If status is `auth-failed-401/403`, the key in the active credential slot
  is rejected; rotate or remove the bad key before probing.
