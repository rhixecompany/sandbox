---
name: auth-inventory-xai-oauth
description: Rendered per-provider auth inventory captured by test-providers-models on 2026-09-07 15:07 UTC.
---

# Auth inventory — xai-oauth

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on 2026-09-07 15:07 UTC.
> Classified using `scripts/render_auth_inventory.py` (status mapping table).

## Summary

- **Provider:** `xai-oauth`
- **Key env:** `oauth (device_code)`
- **Status:** **valid**
- **Rate / auth notes:** ←
- **Docs:** https://docs.x.ai/
- **Auth file verified:** `~/AppData/Local/hermes/auth.json (provider=xai-oauth)`
- **Auth mechanism:** device_code_oauth
- **Inference endpoint:** `https://api.x.ai/v1`

## Credentials

| # | Key name | Type | Source | Note |
|---|----------|------|--------|------|
| #1 | `xai-oauth-oauth-1` | oauth | `device_code` | ← |

## Configuration cross-check

- `~/AppData/Local/hermes/config.yaml` should reference this provider's model
  format (`xai-oauth:<model-id>`) for the primary model and any fallbacks.
- If status is `valid`, the provider is probe-eligible.
- If status is `rate-limited-429` or `exhausted-402`, probes will likely fail;
  the provider should be skipped in Phase 3.
- If status is `auth-failed-401/403`, the key in the active credential slot
  is rejected; rotate or remove the bad key before probing.
