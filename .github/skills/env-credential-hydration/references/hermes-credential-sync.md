---
name: hermes-credential-sync
title: Hermes Credential Sync from Local Files
description: Sync API keys from ~/Desktop/Github/*.txt to Hermes .env.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - hermes
  - credentials
  - env-sync
  - setup
---

# Hermes Credential Sync

## Overview

Automated workflow for syncing credentials from local text files (`~/Desktop/Github/*.txt`) into Hermes root `.env`, auth credential store, MCP server configs, and workspace `.env` files. Single source of truth via DRY.

## When to Use

- Initial Hermes setup after fresh install
- Adding new API keys to the credential store
- Rotating credentials (new keys in GitHub txt files)
- Syncing root `.env` to SandBox/project `.env` files
- Verifying `hermes auth list` shows all providers with `←` marker
- **Triggers**: "sync credentials", "update .env from github", "configure hermes auth", "env_sync.py"

## When NOT to Use

- Editing `.env` manually for one-off changes (use `hermes config set` or `memory` tool)
- Managing credentials for non-Hermes tools
- Creating new credential files in `~/Desktop/Github/` (manual step)

## Prerequisites

- `~/Desktop/Github/` contains credential text files (one per service)
- `~/AppData/Local/hermes/scripts/env_sync.py` maintained and working
- Hermes CLI available (`hermes` in PATH)
- Write access to `~/AppData/Local/hermes/.env` and `~/AppData/Local/hermes/config.yaml`

## Key Files

| File | Purpose |
|------|---------|
| `~/Desktop/Github/*.txt` | Source credential files (one per provider) |
| `~/AppData/Local/hermes/scripts/env_sync.py` | Sync script (dry-run + apply) |
| `~/AppData/Local/hermes/.env` | Root Hermes credential store |
| `~/AppData/Local/hermes/config.yaml` | MCP server configs (reference env vars) |
| `~/AppData/Local/hermes/auth.json` | Auth credential pool (managed by `hermes auth`) |
| `./.env` | Workspace/project credential mirror |

## Workflow

### Phase 1: Dry-run Verification

```bash
python "C:/Users/Alexa/AppData/Local/hermes/scripts/env_sync.py"
```

- Shows ADD/UPDATE/OK/EXTRACT-FAILED for each PLAN entry
- Does NOT write changes
- Fix any EXTRACT-FAILED before proceeding

### Phase 2: Apply Changes

```bash
python "C:/Users/Alexa/AppData/Local/hermes/scripts/env_sync.py" --apply
```

- Creates `.env.bak.YYYYMMDD_HHMMSS` backup
- Writes new/updated vars to `~/AppData/Local/hermes/.env`

### Phase 3: Sync to Workspace

```bash
cp "C:/Users/Alexa/AppData/Local/hermes/.env" "C:/Users/Alexa/Desktop/SandBox/.env"
diff "C:/Users/Alexa/AppData/Local/hermes/.env" "C:/Users/Alexa/Desktop/SandBox/.env"
```

- Verify identical (exit code 0, no output)

### Phase 4: Fix MCP Server Configs

Ensure MCP servers reference env vars, not hardcoded keys:

```bash
# Smithery example
hermes config set mcp_servers.smithery.headers.Authorization "Bearer ${MCP_SMITHERY_API_KEY}"

# Neon, Context7, Sentry already use env vars via add_mcp_servers.py
python "C:/Users/Alexa/AppData/Local/hermes/scripts/add_mcp_servers.py"
```

### Phase 5: Verify Auth Pool

```bash
hermes auth list
```

All providers should show `←` marker (reading from env vars):
```
openrouter (1 credentials):
  #1  OPENROUTER_API_KEY   api_key env:OPENROUTER_API_KEY ←
```

### Phase 6: Full Verification

```bash
# All expected keys present
grep -E "^[A-Z_]+_API_KEY=|^GITHUB_|^OPENAI_|^OPENROUTER_|^HF_|^GOOGLE_|^DEEPSEEK_|^NEON_|^SENTRY_|^HOSTINGER_|^ALIBABA_|^CONTEXT7_|^GROQ_|^XAI_|^TAILSCALE_|^SMITHERY_|^MCP_SMITHERY_|^MINDSTUDIO_|^HONCHO_|^OLLAMA_|^OPENCODE_" ~/AppData/Local/hermes/.env | sort

# Config validates
hermes config check

# Health check
hermes doctor
```

## PLAN Mapping (env_sync.py)

The script's `PLAN` dict maps env vars to source files:

| Env Var | Source File | Extraction Hint |
|---------|-------------|-----------------|
| `OPENROUTER_API_KEY` | `openrouter_api_key.txt` | auto |
| `NEON_API_KEY` | `neon-api-key.txt` | auto |
| `CONTEXT7_API_KEY` | `context7_api_token.txt` | auto |
| `SENTRY_AUTH_TOKEN` | `sentry_token.txt` | longest |
| `HF_TOKEN` | `huggingface-api-key.txt` | auto |
| `DEEPSEEK_API_KEY` | (not in PLAN - add if needed) | - |
| `GOOGLE_API_KEY` | (not in PLAN - add if needed) | - |
| `OLLAMA_API_KEY` | `olama-cloud-api-key.txt` | auto |
| `OPENCODE_ZEN_API_KEY` | `opencode-zen-api-key.txt` | auto |
| `GITHUB_PAT_*` | multiple github PAT files | various |
| `SMITHERY_LEGACY_UUID` | `smithery-api-key.txt` | auto |
| `MCP_SMITHERY_API_KEY` | `smithery-api-key.txt` | auto |
| `XAI_API_KEY` | `xgrok-api-key.txt` | auto |
| `GROQ_API_KEY` | `groq-cloud-api-key.txt` | auto |
| `TAILSCALE_*` | `tailgate-api-key.txt` | tskey-* prefix |
| `HOSTINGER_API_TOKEN` | `hostinger-api-token.txt` | auto |
| `ALIBABA_*` | `alibaba-access-key.txt` | idx0, idx1 |
| `OPENAI_*` | multiple openai files | various |
| `ACEDATA_API_KEY` | `ace-data-cloud-api-key.txt` | auto |
| `HONCHO_API_KEY` | `huncho-api-key.txt` | auto |

## Pitfalls

### Windows Path Mangling (MSYS/Git Bash)
```bash
# WRONG - gets rewritten to C:\\c\\Users\\...
python /c/Users/Alexa/AppData/Local/hermes/scripts/env_sync.py

# CORRECT - native Windows path with forward slashes
python "C:/Users/Alexa/AppData/Local/hermes/scripts/env_sync.py"
```

### Missing/Empty Credential Files
- `groq-cloud-api-key.txt` (1 byte, empty) → `GROQ_API_KEY` EXTRACT-FAILED
- `xgrok-api-key.txt` (0 bytes) → `XAI_API_KEY` EXTRACT-FAILED
- Fix: populate the .txt file, re-run sync

### Typo in PLAN Dict
Fixed: `sithery-api-key.txt` → `smithery-api-key.txt` (line 92)
```python
"SMITHERY_LEGACY_UUID": ("smithery-api-key.txt", "auto"),
```

### MCP Smithery Config Drift
After sync, `config.yaml` smithery server may have hardcoded placeholder:
```yaml
# Before fix
Authorization: Bearer ${MCP_...KEY}

# After fix (via hermes config set)
Authorization: Bearer 7ad70b...a430
```
Always use `${MCP_SMITHERY_API_KEY}` so it reads from `.env`.

### Auth Pool Not Updated Automatically
`hermes auth list` reads from `.env` at runtime — no separate sync needed. But if a provider shows `manual` instead of `env:VAR`, re-add via `hermes auth add`.

### Backup Files Accumulate
`.env.bak.*` files created on each apply. Clean periodically:
```bash
rm ~/AppData/Local/hermes/.env.bak.*
```

## Verification Checklist

- [ ] `env_sync.py` dry-run shows expected changes
- [ ] `--apply` writes without errors
- [ ] `diff` shows root `.env` and workspace `.env` identical
- [ ] `hermes auth list` shows all providers with `←` marker
- [ ] `grep` for API keys shows all expected vars
- [ ] `hermes config check` passes
- [ ] `hermes doctor` shows no advisories
- [ ] MCP servers enabled and test pass (`hermes mcp list`)

## Related Skills

- `hermes-setup` — Full Hermes setup including providers/MCP
- `hermes-profiles` — Profile identity and credential management
- `env-path-portability` — Windows path resolution for scripts
- `validate-memories` — Memory file validation (part of startup)
- `provider-model-audit` — Provider inventory and model discovery

## References

- `scripts/env_sync.py` — The sync script (in Hermes scripts dir)
- `scripts/add_mcp_servers.py` — MCP server config helper