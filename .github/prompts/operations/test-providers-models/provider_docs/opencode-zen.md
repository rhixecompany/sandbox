---
name: auth-inventory-opencode-zen
description: Rendered per-provider auth inventory captured by test-providers-models on 2026-09-07 15:07 UTC.
---

# Auth inventory — opencode-zen

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on 2026-09-07 15:07 UTC.
> Classified using `scripts/render_auth_inventory.py` (status mapping table).

## Summary

- **Provider:** `opencode-zen`
- **Key env:** `OPENCODE_ZEN_API_KEY`
- **Status:** **auth-failed-401/403**
- **Rate / auth notes:** auth failed ModelError (401) (re-auth may be required) ← | auth failed ModelError (401) (re-auth may be required) | auth failed ModelError (401) (re-auth may be required)
- **Docs:** https://opencode.ai/docs/zen/
- **Auth file verified:** `~/AppData/Local/hermes/auth.json (provider=opencode-zen)`
- **Auth mechanism:** api_key
- **Inference endpoint:** `https://opencode.ai/zen/v1`

## Credentials

| # | Key name | Type | Source | Note |
|---|----------|------|--------|------|
| #1 | `OPENCODE_ZEN_API_KEY` | api_key | `env:OPENCODE_ZEN_API_KEY` | _(no note)_ |
| #2 | `api-key-3` | api_key | `manual` | auth failed ModelError (401) (re-auth may be required) ← |
| #3 | `api-key-4` | api_key | `manual` | auth failed ModelError (401) (re-auth may be required) |
| #4 | `api-key-1` | api_key | `manual` | auth failed ModelError (401) (re-auth may be required) |

## Configuration cross-check

- `~/AppData/Local/hermes/config.yaml` should reference this provider's model
  format (`opencode-zen:<model-id>`) for the primary model and any fallbacks.
- If status is `valid`, the provider is probe-eligible.
- If status is `rate-limited-429` or `exhausted-402`, probes will likely fail;
  the provider should be skipped in Phase 3.
- If status is `auth-failed-401/403`, the key in the active credential slot
  is rejected; rotate or remove the bad key before probing.
