---
author: Hermes Agent
description: 'Complete Hermes Agent setup: install, configure providers, MCP servers,
  tools, profiles — from fresh install to verification. Fast path for existing setups.
  Diagnostics and health checks.'
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: hermes-setup
tags:
- imported
title: Hermes Setup & Configuration
version: 2.0.0

---
# Hermes Setup & Configuration

Single authoritative skill for all Hermes Agent setup, configuration, and verification. Consolidates: `hermes-complete-setup`, `hermes-configuration-verification`, `hermes-quickstart`, `hermes-agent-diagnostics-configuration`, `hermes-agent`.

---

## Quick Start

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Interactive setup wizard
hermes setup

# Pick model/provider
hermes model

# Health check
hermes doctor
```

---

## Phase 1: Install & Verify

```bash
# Install
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

# Verify
hermes --version
hermes doctor
```

---

## Phase 2: Provider Configuration

### Adding a Provider

```bash
# Interactive wizard (handles OAuth + API keys)
hermes login --provider <name>  # nous, openai-codex, qwen-oauth
# Or for API key providers:
export OPENROUTER_API_KEY=***
hermes config set providers.openrouter.api_key $OPENROUTER_API_KEY
```

### Provider Reference

| Provider | Auth | Key Env Var | Notes |
|----------|------|-------------|-------|
| OpenRouter | API key | `OPENROUTER_API_KEY` | 200+ models |
| Anthropic | API key | `ANTHROPIC_API_KEY` | Direct |
| Nous Portal | OAuth | `hermes auth` | Free tier |
| OpenAI Codex | OAuth | `hermes auth` | Requires subscription |
| GitHub Copilot | Token | `COPILOT_GITHUB_TOKEN` | Fine-grained PAT |
| Google Gemini | API key | `GOOGLE_API_KEY` / `GEMINI_API_KEY` | |
| DeepSeek | API key | `DEEPSEEK_API_KEY` | |
| xAI / Grok | API key | `XAI_API_KEY` | |
| Hugging Face | Token | `HF_TOKEN` | |
| OpenCode Zen | API key | `OPENCODE_ZEN_API_KEY` | Must include `/chat/completions` in base_url |
| Qwen OAuth | OAuth | `hermes login --provider qwen-oauth` | Requires Qwen CLI |

### Fallback Chain

```yaml
# In ~/.hermes/config.yaml
model:
  default: big-pickle
  provider: opencode-zen
fallback_providers:
  - openrouter
  - google-gemini
  - github-copilot
```

---

## Phase 3: MCP Servers

### Add Server (Recommended)

```bash
hermes mcp add <name> --command "command args"
hermes mcp add <name> --url "https://endpoint/mcp"
```

### Common MCP Servers

```yaml
# ~/.hermes/config.yaml
mcp_servers:
  filesystem:
    command: mcp-server-filesystem
    args: ["--root", "/allowed/path"]
    type: stdio
  sequential-thinking:
    command: mcp-server-sequential-thinking
    type: stdio
  context7:
    url: https://mcp.context7.com/mcp
    headers:
      CONTEXT7_API_KEY: <key>
    type: http
  playwright:
    command: npx
    args: ["@playwright/mcp@latest"]
    type: stdio
  docker:
    command: docker
    args: ["mcp", "gateway", "run", "--profile", "default"]
    type: stdio
```

### Verify

```bash
hermes mcp list
hermes mcp test <name>
hermes mcp test <name>  # enable if pass
```

---

## Phase 4: Toolsets

```bash
# Interactive
hermes tools

# CLI
hermes tools list
hermes tools enable <name>
hermes tools disable <name>

# Per-session (chat flags)
hermes chat --toolsets "web,terminal,file,skills,memory,delegation"
```

### Toolset Reference

| Toolset | Provides |
|---------|----------|
| `web` | Search + extract |
| `search` | Search only |
| `browser` | Browser automation |
| `terminal` | Shell commands |
| `file` | Read/write/search/patch |
| `code_execution` | Sandboxed Python |
| `vision` | Image analysis |
| `image_gen` | AI images |
| `skills` | Skill management |
| `memory` | Cross-session memory |
| `session_search` | Search past conversations |
| `delegation` | Subagent tasks |
| `cronjob` | Scheduled jobs |
| `clarify` | Ask user questions |
| `messaging` | Cross-platform send |
| `todo` | Task tracking |
| `kanban` | Multi-agent queue (workers) |
| `debugging` | Introspection tools |
| `safe` | Minimal low-risk bundle |

---

## Phase 5: Profiles

```bash
# List
hermes profile list

# Create (clones from existing)
hermes profile create code-architect --clone default --clone-all

# Switch sticky default
hermes profile use code-architect

# Show details
hermes profile show code-architect

# Export/import
hermes profile export code-architect > backup.tar.gz
hermes profile import backup.tar.gz
```

### Profile Structure

```
~/.hermes/profiles/<name>/
├── config.yaml
├── .env
├── skills/
├── plugins/
├── cron/
└── memories/
```

---

## Quick Commands Reference

### Config

```bash
hermes config show                    # View full config
hermes config edit                    # Open $EDITOR
hermes config set KEY VALUE           # Set value
hermes config path                    # Print config.yaml path
hermes config check                   # Validate
hermes config migrate                 # Update to latest schema
```

### Auth

```bash
hermes auth add                       # Interactive credential wizard
hermes auth list                      # Show pools
hermes auth remove <provider> <index> # Remove credential
hermes auth reset <provider>          # Clear exhaustion status
```

### Sessions

```bash
hermes sessions list                  # Recent sessions
hermes sessions browse                # Interactive picker
hermes sessions export output.jsonl   # Export
hermes sessions prune --older-than 30 # Cleanup
hermes sessions stats                 # Statistics
```

### Cron

```bash
hermes cron list                      # All jobs
hermes cron create "30m"              # Schedules: 30m, every 2h, 0 9 * * *
hermes cron edit <id>
hermes cron pause|resume <id>
hermes cron run <id>
hermes cron remove <id>
```

### Webhooks

```bash
hermes webhook subscribe <name>       # Route at /webhooks/<name>
hermes webhook list
hermes webhook test <name>
hermes webhook remove <name>
```

### Gateway

```bash
hermes gateway run                    # Foreground
hermes gateway install                # System service
hermes gateway start|stop|restart|status
hermes gateway setup                  # Configure platforms
```

### Update/Uninstall

```bash
hermes update
hermes uninstall
```

---

## Fast Path Verification (Existing Setup)

When config exists, skip full setup — run this in 2-3 min:

```bash
# 1. Health check
hermes doctor

# 2. MCP status
hermes mcp list

# 3. Providers
hermes auth list

# 4. Toolsets
hermes tools list

# 5. Test chat
hermes chat -q "What tools are available?"
```

### Expected Healthy Output

| Check | Pass Criteria |
|-------|---------------|
| `hermes doctor` | All sections pass, 0 advisories |
| `hermes mcp list` | 7-8 servers, 6+ enabled, 200+ tools |
| `hermes auth list` | Primary + 2+ fallbacks with creds |
| `hermes tools list` | 19+ toolsets enabled |
| Chat test | Tool discovery <1s, response OK |

---

## Verification Report Template

```
HERMES SETUP VERIFICATION
Date: YYYY-MM-DD
Status: ✅ READY

PROVIDER CHAIN:
  Primary: opencode-zen (big-pickle)
  Fallbacks: openrouter, google-gemini, github-copilot

MCP SERVERS:
  filesystem ✅ 12 tools
  sequential-thinking ✅ 4 tools
  context7 ✅ 8 tools
  playwright ✅ 15 tools
  docker ✅ 20 tools
  Total: 7/8 enabled, 250+ tools

TOOLSETS:
  Core: 9/9 enabled
  Advanced: delegation, cronjob, moa enabled
  Optional: video, spotify disabled

SYSTEM:
  hermes doctor: ALL PASSING
  API: 27/27 checks
  Security: 0 advisories
```

---

## Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| `hermes doctor` fails API checks | Verify .env keys, check network |
| MCP server offline | `hermes mcp test <name>` → check service running |
| UTF-8 BOM in config.yaml | `hermes config edit` (writes clean) |
| 400 "No models" | Fix base_url: must include `/chat/completions` |
| Copilot rate limited | Fallback to OpenRouter or OpenCode Zen |
| Docker MCP on Windows | Disabled by design (WSL2 limit) |
| Context window overflow | `hermes config set compression.threshold 75` |
| Secret redaction off | `hermes config set security.redact_secrets true` |

---

## Windows Notes

- Use POSIX paths in terminal: `/c/Users/...` not `C:\...`
- Ctrl+Enter = newline (Alt+Enter toggles fullscreen)
- `execute_code` sandbox needs `SYSTEMROOT` env (auto-allowed)
- Docker MCP gateway disabled on Windows (use standard docker-mcp)
- Test with `python -m pytest` from system Python, not venv

---

## When to Use

- Fresh Hermes install
- Adding provider/MCP/tool profile
- Full setup verification
- Fast path health check
- Troubleshooting config issues
- **Triggers**: "setup hermes", "configure hermes", "hermes doctor", "add provider", "add mcp", "verify hermes"

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

