# Hermes Agent Official Reference 2026

**Last Updated:** May 25, 2026  
**Version:** v0.10.0  
**Source:** Official Hermes Agent Documentation & Nous Research

---

## Table of Contents

1. [Quick Overview](#quick-overview)
2. [Installation & Setup](#installation--setup)
3. [CLI Commands Reference](#cli-commands-reference)
4. [Skills System](#skills-system)
5. [MCP Integration](#mcp-integration)
6. [Configuration](#configuration)
7. [Troubleshooting](#troubleshooting)

---

## Quick Overview

**Hermes Agent** is the open-source self-learning AI agent from Nous Research. It's a model-agnostic, autonomous conversational agent that:

- Runs locally as CLI/TUI, on servers via messaging gateway (Telegram/Discord/Slack), or as scheduled cron jobs
- Has a **closed learning loop**: writes reusable "skill" documents and curates persistent memory
- Maintains 660+ ready-made skills across code, ops, data, writing, and research
- Integrates with external tools via Model Context Protocol (MCP)
- Works with 30+ LLM providers (OpenAI, Claude, DeepSeek, Ollama, etc.)

### Key Differentiators

- **Self-improving**: Creates and refines skills from experience
- **Persistent memory**: Learns from every session
- **Platform-agnostic**: Same agent code runs in CLI, messaging, cron
- **Tool ecosystem**: 250+ built-in tools + dynamic MCP server tools
- **Skill registry**: 4 official registries with 660+ ready skills

---

## Installation & Setup

### One-Line Install (macOS/Linux)

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

The installer handles:
- Python 3.11 environment
- Node.js v22
- ripgrep & ffmpeg dependencies
- Repository clone with submodules
- Global `hermes` command in PATH

### Windows (WSL2 + Ubuntu)

1. Install WSL2 and Ubuntu
2. Run the one-line install above in Ubuntu terminal
3. Use `hermes` from within WSL2

### Prerequisites

- Git (only manual requirement)
- Network access to GitHub and package registries
- Shell with permission to install

### First Run

```bash
hermes setup          # Configure LLM provider & API key
hermes doctor         # Validate installation (12 checks)
hermes chat          # Launch interactive agent
```

---

## CLI Commands Reference

### Global Options

| Option | Purpose |
|--------|---------|
| `--profile <name>, -p` | Select profile (overrides default) |
| `--version, -V` | Show version |
| `--resume <session>, -r` | Resume session by ID/title |
| `--continue, -c` | Resume most recent session |
| `--worktree, -w` | Start in isolated git worktree |
| `--yolo` | Bypass dangerous-command prompts |
| `--tui` | Launch TUI (graphical interface) |
| `--dev` | Use TypeScript sources directly (contributors) |

### Core Commands Quick Reference

#### Interaction

| Command | Purpose |
|---------|---------|
| `hermes chat` | Interactive chat |
| `hermes chat -q "..."` | One-shot query |
| `hermes -z "..."` | Pure one-shot (final answer only) |
| `hermes model` | Provider/model selection |

#### Configuration & Setup

| Command | Purpose |
|---------|---------|
| `hermes setup` | First-time/reconfigure wizard |
| `hermes config` | View/edit configuration |
| `hermes config get <key>` | Get specific config value |
| `hermes config set <key> <value>` | Set config value |
| `hermes doctor` | Diagnose 12 common issues |
| `hermes auth` | Manage credentials & OAuth |

#### Skills & Productivity

| Command | Purpose |
|---------|---------|
| `hermes skills list` | List installed skills |
| `hermes skills add <name>` | Install skill from registry |
| `hermes skills reset` | Reset to bundled skills |
| `hermes bundles` | Group skills under slash command |
| `hermes curator` | Background skill maintenance |

#### MCP & Integration

| Command | Purpose |
|---------|---------|
| `hermes mcp list` | List MCP servers |
| `hermes mcp add <name>` | Add MCP server |
| `hermes mcp add <name> --preset <preset>` | Add with preset config |
| `hermes mcp remove <name>` | Remove MCP server |

#### Scheduling & Data

| Command | Purpose |
|---------|---------|
| `hermes cron list` | List scheduled jobs |
| `hermes cron add` | Create scheduled job |
| `hermes sessions list` | List past sessions |
| `hermes backup` | Create config/skills backup |
| `hermes import` | Restore from backup |

#### Messaging & Gateway

| Command | Purpose |
|---------|---------|
| `hermes gateway start` | Run messaging service |
| `hermes slack` | Generate Slack app manifest |
| `hermes whatsapp` | Configure WhatsApp pairing |
| `hermes pairing` | Approve/revoke pairing codes |

#### Debugging

| Command | Purpose |
|---------|---------|
| `hermes logs` | View/tail log files |
| `hermes status` | Agent/auth/platform status |
| `hermes dump` | Copy-pasteable setup summary |
| `hermes debug` | Upload logs for support |

---

## Skills System

### What is a Skill?

A **Skill** is a SKILL.md file—a structured document that tells Hermes what a capability does, what parameters it accepts, and how to use it.

### Skill Structure

```yaml
---
name: code-review
description: Review pull requests and provide feedback
version: 1.0.0
author: Alexa
triggers:
  - "review the PR"
  - "code review"
---

# Code Review Skill

## Overview
This skill reviews code for quality, security, and best practices.

## Usage
Ask: "review this PR for security issues"

## Implementation
[Steps and procedures...]
```

### 4 Official Registries

| Registry | Command | Coverage |
|----------|---------|----------|
| `nous/core` | `hermes skills add nous/core/<name>` | Core capabilities |
| `nous/dev` | `hermes skills add nous/dev/<name>` | Dev tools (660+ total) |
| `community/skills` | `hermes skills add community/<name>` | Community contributions |
| `partner/skills` | `hermes skills add partner/<name>` | Partner integrations |

### Install Skills

```bash
# From registry
hermes skills add code-review

# From GitHub path
hermes skills add nous/dev/code-review

# From direct URL
hermes skills install https://example.com/SKILL.md

# With alias
hermes skills install https://example.com/SKILL.md --name my-skill
```

### Skill Locations

- Per-user: `~/AppData/Local/hermes/skills/`
- Per-project: `./skills/`

---

## MCP Integration

### What is MCP?

**Model Context Protocol** is a standardized protocol that connects Hermes to external tools and data sources (GitHub, databases, file systems, APIs, etc.).

### Two Types of MCP Servers

#### 1. Stdio Servers (Local)

Run as local subprocesses, communicate via stdin/stdout.

```yaml
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user/projects"]
```

**Use when:**
- Server installed locally
- Low-latency access needed
- Following MCP docs with `command`/`args`/`env`

#### 2. HTTP Servers (Remote)

Remote endpoints Hermes connects to directly.

```yaml
mcp_servers:
  remote_api:
    url: "https://mcp.example.com/mcp"
    headers:
      Authorization: "Bearer ***"
```

**Use when:**
- Server hosted externally
- Org exposes internal endpoints
- Avoid local subprocesses

### Configuration Reference

| Key | Type | Purpose |
|-----|------|---------|
| `command` | string | Executable for stdio server |
| `args` | list | Arguments for stdio server |
| `env` | mapping | Environment variables |
| `url` | string | HTTP MCP endpoint |
| `headers` | mapping | HTTP request headers |
| `timeout` | number | Tool call timeout (seconds) |
| `connect_timeout` | number | Initial connection timeout |
| `enabled` | bool | Enable/disable server |
| `supports_parallel_tool_calls` | bool | Allow concurrent execution |
| `tools` | mapping | Per-server filtering |

### Quick Start

```bash
# List servers
hermes mcp list

# Add server with preset
hermes mcp add codex --preset codex

# Add custom server
# Edit ~/AppData/Local/hermes/config.yaml and add to mcp_servers section
```

### Built-in Presets

| Preset | Wires Up |
|--------|----------|
| `codex` | Codex CLI's MCP server (stdio) |

### Tool Naming Convention

Hermes prefixes MCP tools to prevent collisions:

```
mcp_<server_name>_<tool_name>
```

Examples:
- `filesystem.read_file` → `mcp_filesystem_read_file`
- `github.create-issue` → `mcp_github_create_issue`

### Per-Server Filtering

#### Whitelist Tools

```yaml
mcp_servers:
  github:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-github"]
    env:
      GITHUB_PERSONAL_ACCESS_TOKEN: "***"
    tools:
      include: [create_issue, list_issues]
```

Only specified tools are registered.

#### Blacklist Tools

```yaml
mcp_servers:
  stripe:
    url: "https://mcp.stripe.com"
    tools:
      exclude: [delete_customer]
```

All tools except excluded ones are registered.

#### Disable Server

```yaml
mcp_servers:
  legacy:
    url: "https://mcp.legacy.internal"
    enabled: false
```

### Tool Registration & Discovery

- **Automatic discovery**: Hermes discovers MCP server tools at startup
- **Runtime notifications**: When server sends `notifications/tools/list_changed`, Hermes re-fetches tool list automatically
- **Utility tools**: Auto-registers `list_resources`, `read_resource`, `list_prompts`, `get_prompt` if supported
- **Naming**: Same prefix pattern: `mcp_<server>_<utility>`

---

## Configuration

### Config Location

- **Primary**: `~/AppData/Local/hermes/config.yaml`
- **Secrets**: `~/AppData/Local/hermes/.env`
- **Override**: Set `HERMES_CONFIG_PATH` environment variable

### Essential Config Keys

```yaml
# LLM Provider
default_model: "claude-3-5-sonnet-20241022"
providers:
  anthropic:
    api_key: "${ANTHROPIC_API_KEY}"

# MCP Servers
mcp_servers:
  filesystem:
    command: "npx"
    args: ["-y", "@modelcontextprotocol/server-filesystem", "/home/user"]

# Skills
bundled_skills:
  - name: "code-review"
    enabled: true

# Memory
memory:
  provider: "local"
  path: "~/AppData/Local/hermes/memory.md"

# Gateway
gateway:
  host: "0.0.0.0"
  port: 8000
  enable_messaging: true
```

### Environment Variables

Store secrets in `~/AppData/Local/hermes/.env`:

```bash
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...
GITHUB_TOKEN=ghp_...
HERMES_CONFIG_PATH=/custom/path/config.yaml
```

### Config Commands

```bash
# View current config
hermes config show

# Get specific value
hermes config get default_model

# Set value
hermes config set default_model "gpt-4o"

# Edit directly
hermes config edit
```

---

## Troubleshooting

### Common Issues

#### hermes: command not found

**Cause**: PATH not updated after install

**Fix**:
```bash
source ~/.bashrc
# Or open new terminal
```

Also verify `~/AppData/Local/hermes/bin` is in PATH:
```bash
echo $PATH | grep hermes
```

#### API Key Authentication Failed

**Cause**: Invalid/mismatched API key

**Fix**:
```bash
hermes setup
# Paste key without whitespace
# Confirm provider matches key (e.g., Zhipu key only works with provider=glm)
```

#### Skills Install Fails with Checksum Mismatch

**Cause**: Stale registry cache

**Fix**:
```bash
hermes skills cache clean
hermes skills add <name>
```

#### WSL2: Install Hangs at Dependency Resolution

**Cause**: Broken WSL2 DNS (common on enterprise networks)

**Fix**:
```bash
sudo bash -c "echo 'nameserver 8.8.8.8' > /etc/resolv.conf"
# Re-run install
```

#### MCP Server Not Connecting

**Check**:
1. Server is running: `ps aux | grep mcp`
2. Config syntax is valid: `hermes config show`
3. Command path exists: `which npx`
4. Environment variables set: `echo $GITHUB_TOKEN`

**Debug**:
```bash
hermes mcp list              # List servers
hermes logs                  # Check error logs
hermes doctor                # Run diagnostics
```

#### Models Not Available

**Fix**:
```bash
hermes model              # Re-run model wizard
hermes config set default_model "gpt-4o"
hermes doctor            # Validate setup
```

### Diagnostic Commands

```bash
# Comprehensive health check
hermes doctor

# View logs
hermes logs

# Get setup summary (for support)
hermes dump

# Upload diagnostics
hermes debug
```

---

## Additional Resources

- **Official Docs**: https://hermes-agent.nousresearch.com/docs
- **GitHub Repo**: https://github.com/NousResearch/hermes-agent
- **MCP Docs**: https://modelcontextprotocol.io
- **Skill Registry**: https://skills.hermes-agent.io
- **Community**: https://reddit.com/r/hermesagent

---

**Document Version**: 1.0  
**Last Verified**: May 25, 2026  
**Status**: Production Ready ✓
