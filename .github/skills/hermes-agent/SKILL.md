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
| `config.yaml` | `~/.hermes/config.yaml` | Main configuration |
| `.env` | `~/.hermes/.env` | Environment variables (API keys) |
| `SOUL.md` | `~/.hermes/SOUL.md` | Global personality & standards |
| `USER.md` | `~/.hermes/profiles/*/USER.md` | Per-profile identity |
| `MEMORY.md` | `~/.hermes/profiles/*/MEMORY.md` | Per-profile memory |

## Provider Configuration

```yaml
# ~/.hermes/config.yaml
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
# Hook directory: ~/.hermes/hooks/
# Config: ~/.hermes/config.yaml → hooks: section

# Test hook
echo '{}' | bash ~/.hermes/hooks/session-logger/log-session-start.sh
```

## Plugins

```bash
# Plugin directory: ~/.hermes/plugins/
# Config: ~/.hermes/config.yaml → plugins: section
```

## Skills

```bash
# Skills directory: ~/.hermes/skills/
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

