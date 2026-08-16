---
name: hermes-script-vault-key-validate
title: Vault Key Validation
description: "Validate vault keys vs providers; write verified .env."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [hermes, scripts, devops, secrets, validation, async]
metadata:
  hermes:
    tags: [hermes, scripts, devops, secrets, validation]
    related_skills: [env-credential-hydration, hermes-diagnostic-repair]
    script_path: "C:\\Users\\Alexa\\AppData\\Local\\hermes\\scripts\\vault_key_validate.py"
---

# Vault Key Validation Skill

## Overview

Validates all API keys stored in the GitHub credential vault (`~/Desktop/Github/*.txt`) against live provider endpoints. Produces a verified `.env` file for Hermes.

## When to Use

- Before starting a session that needs external API access
- After adding new credential files to the vault
- Periodic health check of all provider keys
- Debugging "auth failed" errors from MCP servers or provider tools

## Script Interface

**Path:** `$LOCALAPPDATA/hermes/scripts/vault_key_validate.py`

```bash
# Dry-run (default) — show results only
MSYS_NO_PATHCONV=1 python3 vault_key_validate.py

# Write verified keys to hermes .env
MSYS_NO_PATHCONV=1 python3 vault_key_validate.py --apply

# Test specific keys only
MSYS_NO_PATHCONV=1 python3 vault_key_validate.py --only GITHUB_TOKEN,OPENROUTER_API_KEY
```

## Tested Providers (26)

| Key Name | Vault File | Endpoint |
|---|---|---|
| GITHUB_TOKEN | github-pat.txt | api.github.com/user |
| OPENAI_API_KEY_* | openai-api-key.txt | api.openai.com/v1/models |
| OPENROUTER_API_KEY | openrouter_api_key.txt | openrouter.ai/api/v1/auth/key |
| NEON_API_KEY | neon-api-key.txt | mcp.neon.tech/mcp (MCP initialize) |
| HONCHO_API_KEY | huncho-api-key.txt | mcp.honcho.dev/ (MCP initialize) |
| CONTEXT7_API_KEY | context7_api_token.txt | mcp.context7.com/mcp (MCP initialize) |
| TAILSCALE_API_KEY | tailgate-api-key.txt | api.tailscale.com/api/v2/tailnet/-/devices |
| SENTRY_AUTH_TOKEN | sentry_token.txt | sentry.io/api/0/ |
| TACTICAL_API_KEY | tavily-api-key.txt | api.tavily.com/search |
| ...and 16 more | | |

## Skills Required

| Skill | Purpose |
|---|---|
| `env-credential-hydration` | Build .env from credential vault |
| `hermes-diagnostic-repair` | Diagnose provider chain failures |

## Workflow

### Phase 1: Discover
1. Read all `.txt` files from `~/Desktop/Github/`
2. Extract tokens using provider-specific regex patterns
3. Map each key name to its vault file and selector

### Phase 2: Validate
1. For each key, select the appropriate token (auto/prefix/index)
2. Hit the provider's auth endpoint with the token
3. Record HTTP status, response info, and token preview

### Phase 3: Report
1. Print summary: X/Y keys valid
2. List each key with status, HTTP code, info, token preview
3. Exit code 0 if all valid, 1 otherwise

### Phase 4: Apply (optional)
1. If `--apply`, write `KEY=token` lines to `$LOCALAPPDATA/hermes/.env`
2. Only write keys that returned HTTP 200

## Verification Checklist

- [ ] All 26 providers tested without timeout
- [ ] HTTP 200 = valid, any other = invalid
- [ ] Token preview shows first 12 chars only (security)
- [ ] `--apply` writes only verified keys
- [ ] Dry-run is default (safe)

## Pitfalls

- **Windows paths**: Use `MSYS_NO_PATHCONV=1` prefix when calling from git-bash
- **Network timeouts**: 15s per request; some providers (smithery, alibaba) are slower
- **Missing vault files**: Script reports "vault file missing" — not an error, just skipped
- **Alibaba needs both access key + secret**: Only access key in vault; secret handled separately
- **SSE MCP responses**: Some MCP servers (neon, honcho) return 200 with SSE body — parser handles both JSON and event-stream formats