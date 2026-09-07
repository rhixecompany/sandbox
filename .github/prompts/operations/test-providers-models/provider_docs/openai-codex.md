---
name: auth-inventory-openai-codex
description: Rendered per-provider auth inventory captured by test-providers-models on 2026-09-07 15:07 UTC.
---

# Auth inventory — openai-codex

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on 2026-09-07 15:07 UTC.
> Classified using `scripts/render_auth_inventory.py` (status mapping table).

## Summary

- **Provider:** `openai-codex`
- **Key env:** `oauth (device_code)`
- **Status:** **rate-limited-429**
- **Rate / auth notes:** rate-limited usage_limit_reached (429) (27d 6h left) | rate-limited usage_limit_reached (429) (27d 9h left) | rate-limited usage_limit_reached (429) (27d 17h left)
- **Docs:** https://github.com/features/copilot
- **Auth file verified:** `~/AppData/Local/hermes/auth.json (provider=openai-codex)`
- **Auth mechanism:** device_code_oauth
- **Inference endpoint:** `https://api.openai.com/v1`

## Credentials

| # | Key name | Type | Source | Note |
|---|----------|------|--------|------|
| #1 | `device_code` | oauth | `device_code` | rate-limited usage_limit_reached (429) (27d 6h left) |
| #2 | `openai-codex-oauth-2` | oauth | `device_code` | rate-limited usage_limit_reached (429) (27d 9h left) |
| #3 | `alexanderrhixe30@gmail.com` | oauth | `device_code` | rate-limited usage_limit_reached (429) (27d 17h left) |

## Configuration cross-check

- `~/AppData/Local/hermes/config.yaml` should reference this provider's model
  format (`openai-codex:<model-id>`) for the primary model and any fallbacks.
- If status is `valid`, the provider is probe-eligible.
- If status is `rate-limited-429` or `exhausted-402`, probes will likely fail;
  the provider should be skipped in Phase 3.
- If status is `auth-failed-401/403`, the key in the active credential slot
  is rejected; rotate or remove the bad key before probing.
