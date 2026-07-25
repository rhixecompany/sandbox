---
author: Hermes Agent + Teknium
description: Configure, extend, or contribute to Hermes Agent.
license: MIT
metadata:
  hermes:
    category: devops
name: hermes-agent
tags:
- imported
title: Hermes Agent
version: 2.1.0

---
# Hermes Agent

Complete reference for configuring, extending, and contributing to Hermes Agent.

## When to Use

- Setting up Hermes Agent for the first time
- Adding providers, MCP servers, or tools
- Configuring profiles, hooks, or plugins
- Troubleshooting Hermes Agent issues
- Contributing to Hermes Agent development

## Quick Commands

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Setup wizard
hermes setup

# Health check
hermes doctor

# Version
hermes --version
```

## Configuration Files

| File | Path | Purpose |
|------|------|---------|
| `config.yaml` | `~/AppData/Local/hermes/config.yaml` | Main configuration |
| `.env` | `~/AppData/Local/hermes/.env` | Environment variables (API keys) |
| `SOUL.md` | `~/AppData/Local/hermes/SOUL.md` | Global personality & standards |
| `USER.md` | `~/AppData/Local/hermes/profiles/*/USER.md` | Per-profile identity |
| `MEMORY.md` | `~/AppData/Local/hermes/profiles/*/MEMORY.md` | Per-profile memory |

## Provider Configuration

```yaml
# ~/AppData/Local/hermes/config.yaml
model:
  default: big-pickle
  provider: opencode-zen

providers:
  openrouter:
    api_key_env: OPENROUTER_API_KEY
  anthropic:
    api_key_env: ANTHROPIC_API_KEY
```

## MCP Servers

```bash
# Add MCP server
hermes mcp add <name> --command "cmd args"
hermes mcp add <name> --url "https://endpoint/mcp"

# List servers
hermes mcp list

# Test server
hermes mcp test <name>
```

## Profiles

```bash
# Create profile
hermes profile create <name> --clone default --clone-all

# Switch profile
hermes profile use <name>

# List profiles
hermes profile list
```

## Hooks

```bash
# Hook directory: $LOCALAPPDATA/hermes/hooks/
# Config: $LOCALAPPDATA/hermes/config.yaml → hooks: section

# Test hook
echo '{}' | bash $LOCALAPPDATA/hermes/hooks/session-logger/log-session-start.sh
```

## Plugins

```bash
# Plugin directory: $LOCALAPPDATA/hermes/plugins/
# Config: $LOCALAPPDATA/hermes/config.yaml → plugins: section
```

## Skills

```bash
# Skills directory: $LOCALAPPDATA/hermes/skills/
# Managed via skill_manage tool
```

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `hermes doctor` fails | Check .env keys, network |
| MCP server offline | `hermes mcp test <name>` |
| Provider errors | Check API keys in .env |
| Config syntax error | `hermes config check` |
| UTF-8 BOM in config | `hermes config edit` |

## Configuration Troubleshooting

> Absorbed from the former `hermes-config-troubleshooting` skill during umbrella consolidation.

Diagnose config path resolution, hook discovery failures, and Windows-specific `HERMES_HOME`/profile overrides.

**Symptoms → likely cause**

| Symptom | Likely cause |
|---------|--------------|
| `hermes hooks list`: "No shell hooks configured" | Config path mismatch or missing allowlist entries |
| `hermes doctor` clean but hooks don't fire | `HERMES_HOME` overridden by profile/env |
| Config edits in workspace `.hermes/` not taking effect | Runtime uses profile data dir, not workspace |
| `shell-hooks-allowlist.json` missing | First-run consent not recorded; non-TTY skips registration |

**Diagnostic steps**
1. Confirm the active `HERMES_HOME`:
   ```bash
   python -c "from hermes_constants import get_hermes_home; print(get_hermes_home())"
   python -c "from hermes_cli.config import get_config_path; print(get_config_path())"
   ```
2. Check both config paths — only one is authoritative at runtime:
   - `~/AppData/Local/hermes/config.yaml` (classic/default profile)
   - `C:\Users\<user>\AppData\Local\hermes\config.yaml` (active profile/runtime)
3. Verify `hooks:` is top-level YAML with `enabled`, `events`, `script`; `script:` must be an absolute Windows path.
4. Inspect allowlist: `~/AppData/Local/hermes/shell-hooks-allowlist.json` must contain `approvals:` entries. Non-TTY sessions skip prompts — use `HERMES_ACCEPT_HOOKS=1`.
5. Profile override check: `hermes profile list`. Named profiles set `HERMES_HOME` to `~/AppData/Local/hermes/profiles/<name>`.

**Windows-specific pitfalls**
- `~/AppData/Local/hermes` may not exist until created; runtime may default to the AppData profile dir.
- Git Bash `$HOME` = `/c/Users/Alexa`, but Windows tools may read `%USERPROFILE%`.
- Drive-letter paths in `script:` need double backslashes or forward slashes.
- Copying a config into `~/AppData/Local/hermes/` does not change an already-running session.

**Verification:** `hermes config check` → version OK; `hermes hooks list` → expected hooks; `hermes hooks doctor` → passes; `hermes hooks test <event>` → synthetic payload succeeds.

## Related Skills

- `hermes-setup` — Complete setup guide
- `hermes-hooks` — Hook lifecycle management
- `hermes-mcp` — MCP server lifecycle
- `hermes-profiles` — Profile management
- `hermes-skill-library-maintenance` — Skill library maintenance


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

