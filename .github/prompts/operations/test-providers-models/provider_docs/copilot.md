---
name: auth-inventory-copilot
description: Rendered per-provider auth inventory captured by test-providers-models on 2026-09-07 15:07 UTC.
---

# Auth inventory — copilot

> Captured from `hermes auth list` via `scripts/test-providers-probe.py` on 2026-09-07 15:07 UTC.
> Classified using `scripts/render_auth_inventory.py` (status mapping table).

## Summary

- **Provider:** `copilot`
- **Key env:** `GITHUB_TOKEN / COPILOT_GITHUB_TOKEN`
- **Status:** **valid**
- **Rate / auth notes:** ←
- **Docs:** https://github.com/features/copilot
- **Auth file verified:** `~/AppData/Local/hermes/auth.json (provider=copilot)`
- **Auth mechanism:** api_key
- **Inference endpoint:** `https://api.githubcopilot.com`

## Credentials

| # | Key name | Type | Source | Note |
|---|----------|------|--------|------|
| #1 | `GITHUB_TOKEN` | api_key | `env:GITHUB_TOKEN` | _(no note)_ |
| #2 | `COPILOT_GITHUB_TOKEN` | api_key | `env:COPILOT_GITHUB_TOKEN` | ← |
| #3 | `api-key-3` | api_key | `manual` | _(no note)_ |

## Configuration cross-check

- `~/AppData/Local/hermes/config.yaml` should reference this provider's model
  format (`copilot:<model-id>`) for the primary model and any fallbacks.
- If status is `valid`, the provider is probe-eligible.
- If status is `rate-limited-429` or `exhausted-402`, probes will likely fail;
  the provider should be skipped in Phase 3.
- If status is `auth-failed-401/403`, the key in the active credential slot
  is rejected; rotate or remove the bad key before probing.
