---
name: auth-inventory-xai
description: Rendered per-provider auth inventory captured by test-providers-models on 2026-09-07 15:07 UTC.
---

# Auth inventory — xai

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on 2026-09-07 15:07 UTC.
> Classified using `scripts/render_auth_inventory.py` (status mapping table).

## Summary

- **Provider:** `xai`
- **Key env:** `XAI_API_KEY`
- **Status:** **auth-failed-401/403**
- **Rate / auth notes:** auth failed (403) (re-auth may be required) ←
- **Docs:** https://docs.x.ai/docs
- **Auth file verified:** `~/AppData/Local/hermes/auth.json (provider=xai)`
- **Auth mechanism:** api_key
- **Inference endpoint:** `https://api.x.ai/v1`

## Credentials

| # | Key name | Type | Source | Note |
|---|----------|------|--------|------|
| #1 | `api-key-1` | api_key | `manual` | auth failed (403) (re-auth may be required) ← |
| #2 | `XAI_API_KEY` | api_key | `env:XAI_API_KEY` | _(no note)_ |

## Configuration cross-check

- `~/AppData/Local/hermes/config.yaml` should reference this provider's model
  format (`xai:<model-id>`) for the primary model and any fallbacks.
- If status is `valid`, the provider is probe-eligible.
- If status is `rate-limited-429` or `exhausted-402`, probes will likely fail;
  the provider should be skipped in Phase 3.
- If status is `auth-failed-401/403`, the key in the active credential slot
  is rejected; rotate or remove the bad key before probing.
