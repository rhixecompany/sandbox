---
name: auth-inventory-gemini
description: Rendered per-provider auth inventory captured by test-providers-models on 2026-09-07 15:07 UTC.
---

# Auth inventory — gemini

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on 2026-09-07 15:07 UTC.
> Classified using `scripts/render_auth_inventory.py` (status mapping table).

## Summary

- **Provider:** `gemini`
- **Key env:** `GOOGLE_API_KEY`
- **Status:** **valid**
- **Rate / auth notes:** ←
- **Docs:** https://ai.google.dev/gemini-api/docs
- **Auth file verified:** `~/AppData/Local/hermes/auth.json (provider=gemini)`
- **Auth mechanism:** api_key
- **Inference endpoint:** `https://generativelanguage.googleapis.com/v1beta`

## Credentials

| # | Key name | Type | Source | Note |
|---|----------|------|--------|------|
| #1 | `GOOGLE_API_KEY` | api_key | `env:GOOGLE_API_KEY` | ← |

## Configuration cross-check

- `~/AppData/Local/hermes/config.yaml` should reference this provider's model
  format (`gemini:<model-id>`) for the primary model and any fallbacks.
- If status is `valid`, the provider is probe-eligible.
- If status is `rate-limited-429` or `exhausted-402`, probes will likely fail;
  the provider should be skipped in Phase 3.
- If status is `auth-failed-401/403`, the key in the active credential slot
  is rejected; rotate or remove the bad key before probing.
