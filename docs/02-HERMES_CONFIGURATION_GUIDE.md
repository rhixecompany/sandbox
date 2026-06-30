# Hermes Agent Complete Configuration Guide

**Document Type:** Comprehensive Setup & Reference  
**Version:** 1.0  
**Hermes Version:** v0.14.0+  
**Created:** May 25, 2026  
**Environment:** Windows 11 / Linux / macOS

---

## Table of Contents

1. [Overview](#overview)
2. [Installation & Prerequisites](#installation--prerequisites)
3. [Environment Configuration](#environment-configuration)
4. [Global Configuration (config.yaml)](#global-configuration-configyaml)
5. [Project Configuration (.hermes.md)](#project-configuration-hermesmd)
6. [API Key Setup](#api-key-setup)
7. [MCP Server Configuration](#mcp-server-configuration)
8. [Terminal Backend Setup](#terminal-backend-setup)
9. [Verification & Testing](#verification--testing)
10. [Troubleshooting](#troubleshooting)

---

## Overview

**Hermes Agent** is an open-source CLI AI assistant built by Nous Research. It:

- Lives in your terminal (or cloud)
- Accessible via Telegram, Discord, WhatsApp, Signal, Email
- Remembers context across conversations
- Has access to 40+ tools for coding, research, file management
- Supports multiple LLM providers
- Runs on any $5 VPS
- Fully configurable globally and per-project

### System Requirements

| Requirement  | Details                         |
| ------------ | ------------------------------- |
| **OS**       | Linux, macOS, or WSL2 (Windows) |
| **Shell**    | Bash or Zsh                     |
| **Python**   | 3.11+ (auto-installed)          |
| **Node.js**  | 20+ (for messaging)             |
| **Internet** | Required for API calls          |

---

## Installation & Prerequisites

### Step 1: Run the Installer

```bash
curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash
```

**What this does:**

- Installs Python 3.11 (if needed)
- Installs Node.js 20 (for messaging platforms)
- Sets up virtual environment
- Creates the `hermes` command
- Creates config directory: `~/AppData/Local/hermes/`

### Step 2: Reload Shell

```bash
# For Bash
source ~/.bashrc

# For Zsh
source ~/.zshrc
```

### Step 3: Verify Installation

```bash
hermes --version
```

Expected output:

```
Hermes Agent v0.14.0 (2026.5.16)
Python 3.11.14
```

### Step 4: Get an API Key

Hermes requires an LLM API key. Choose one provider:

| Provider        | Best For              | Sign Up                                                     |
| --------------- | --------------------- | ----------------------------------------------------------- |
| **OpenRouter**  | 200+ models, flexible | [openrouter.ai](https://openrouter.ai/)                     |
| **MiniMax**     | Fast, affordable      | [minimax.io](https://www.minimax.io/)                       |
| **Nous Portal** | Nous Research models  | [portal.nousresearch.com](https://portal.nousresearch.com/) |
| **OpenAI**      | GPT-4, GPT-4o         | [platform.openai.com](https://platform.openai.com/)         |
| **Anthropic**   | Claude models         | [console.anthropic.com](https://console.anthropic.com/)     |
| **Google**      | Gemini models         | [aistudio.google.com](https://aistudio.google.com/)         |

**Recommendation:** Start with OpenRouter (free credits, flexible).

---

## Environment Configuration

### Location

```
~/AppData/Local/hermes/.env
```

### Copy Template

```bash
hermes setup
```

Or manually:

```bash
cp ~/AppData/Local/hermes/.env.example ~/AppData/Local/hermes/.env
```

### Essential Variables

#### LLM Provider (Choose One)

```bash
# OpenRouter (Recommended)
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxxxxxx

# Or: Google Gemini
GOOGLE_API_KEY=AIzaSyxxxxxxxxxxxxxxxxxxxx

# Or: OpenAI
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxx

# Or: Anthropic Claude
ANTHROPIC_API_KEY=sk-ant-xxxxxxxxxxxxxxxxxxxx
```

#### Terminal Backend

```bash
# Local execution (default)
TERMINAL_ENV=local

# Or: Docker containers
TERMINAL_ENV=docker
TERMINAL_DOCKER_IMAGE=nikolaik/python-nodejs:python3.11-nodejs20

# Or: Remote SSH
TERMINAL_ENV=ssh
TERMINAL_SSH_HOST=192.168.1.100
TERMINAL_SSH_USER=agent
TERMINAL_SSH_KEY=~/.ssh/id_rsa
```

#### Optional Tool APIs

```bash
# Web search
EXA_API_KEY=
PARALLEL_API_KEY=
FIRECRAWL_API_KEY=

# Image generation
FAL_KEY=

# Audio/Music
SUNO_AUTH_TOKEN=
```

### Set Variables via CLI

```bash
hermes config set OPENROUTER_API_KEY sk-or-v1-xxxxx
hermes config set model openrouter/gpt-4o
hermes config set terminal.backend docker
```

### View Current Configuration

```bash
hermes config show
```

---

## Global Configuration (config.yaml)

### Location

```
~/AppData/Local/hermes/config.yaml
```

### Structure

```yaml
# Agent Identity
agent:
    name: "Hermes Agent"
    version: "0.14.0"

# LLM Model Configuration
model:
    provider: "openrouter"
    model: "openrouter/gpt-4o"
    auth_mode: "api_key"

    # Fallback chain (if primary fails)
    fallback_chain:
        - provider: "openrouter"
          model: "meta-llama/llama-3.3-70b"
        - provider: "google"
          model: "gemini-2.0-flash"

# API Configuration
openrouter:
    api_key: "${OPENROUTER_API_KEY}"
    base_url: "https://openrouter.ai/api/v1"
    response_cache: true
    response_cache_ttl: 3600

# Terminal Backend
terminal:
    backend: "local" # local, docker, ssh, modal, singularity

    # For Docker backend
    docker:
        image: "nikolaik/python-nodejs:python3.11-nodejs20"
        binary: "/usr/bin/docker" # or podman path

    # For SSH backend
    ssh:
        host: "${TERMINAL_SSH_HOST}"
        user: "${TERMINAL_SSH_USER}"
        key: "${TERMINAL_SSH_KEY}"
        port: 22

    # Timeouts & Limits
    timeout_seconds: 60
    max_output_bytes: 50000
    max_lines: 2000

# MCP Server Configuration
mcp_servers:
    filesystem:
        type: "stdio"
        command: "stdio"

    docker:
        type: "stdio"
        command: "docker"
        enabled: true

    playwright:
        type: "stdio"
        command: "playwright"
        enabled: true

# Toolsets (Enable/Disable)
enabled_toolsets:
    - "web"
    - "terminal"
    - "file"
    - "vision"
    - "search"

# Agent Behavior
agent_settings:
    max_turns: 90
    max_retries: 3
    timeout_ms: 3000
    tool_output_max_bytes: 50000

# Memory & Persistence
memory:
    enabled: true
    storage_path: "~/AppData/Local/hermes/memory/"
    auto_save: true

# Logging
logging:
    level: "INFO"
    format: "json"
    file: "~/AppData/Local/hermes/hermes.log"
```

### Key Sections Explained

#### Model Provider

```yaml
model:
    provider: "openrouter" # Primary provider
    model: "openrouter/gpt-4o" # Specific model
    max_tokens: 4096 # Response limit
    temperature: 0.7 # Creativity (0-1)
```

#### Terminal Backend Options

```yaml
# Local (default)
terminal:
  backend: "local"
  timeout_seconds: 60

# Docker
terminal:
  backend: "docker"
  docker:
    image: "nikolaik/python-nodejs:python3.11-nodejs20"

# SSH (Remote)
terminal:
  backend: "ssh"
  ssh:
    host: "192.168.1.100"
    user: "agent"
    key: "~/.ssh/id_rsa"

# Singularity
terminal:
  backend: "singularity"
  singularity:
    image: "docker://nikolaik/python-nodejs:python3.11-nodejs20"

# Modal (Cloud)
terminal:
  backend: "modal"
```

#### MCP Servers

```yaml
mcp_servers:
    filesystem:
        type: "stdio"
        command: "fs"
        enabled: true

    docker:
        type: "stdio"
        command: "docker"
        enabled: true
        env:
            DOCKER_BINARY: "/usr/bin/docker"

    playwright:
        type: "stdio"
        enabled: true
```

---

## Project Configuration (.hermes.md)

### Overview

Similar to `.cursorrules` (Cursor), `CLAUDE.md` (Claude Code), and `.windsurfrules` (Windsurf).

Per-repository configuration that persists with your code and survives sessions.

### Location

```
.hermes.md                 # Primary
HERMES.md                  # Fallback
.cursorrules               # Falls back to Cursor rules
```

### Structure

```yaml
---
version: 1
project: "My Project Name"
description: "What this project does"
---

# Project Context

## Overview
Describe your project, its purpose, and scope.

## Conventions

### Code Style
- Use TypeScript, not JavaScript
- Format with Prettier
- Lint with ESLint

### Commit Style
- Format: `type: description`
- Types: feat, fix, docs, refactor, test, chore
- Example: `feat: add Docker MCP server support`

### File Organization
- `src/` — Source code
- `tests/` — Test files
- `docs/` — Documentation
- `scripts/` — Automation scripts

## Guidelines

### When to Use Each Tool
- File operations: `file` toolset
- Terminal commands: `terminal` toolset
- Docker: `docker` MCP server
- Web research: `web` toolset

### Constraints
- Never modify `.env` files
- Always backup before destructive changes
- Run tests before committing
- Follow the verification order

## Verification Order
1. Format: `bun run format`
2. Type check: `bun run typecheck`
3. Lint: `bun run lint:strict`
4. Tests: `bun run test`

## Helpful Related Prompts
- `/research` — Research phase
- `/plan` — Planning phase
- `/execute` — Execution phase
- `/commit` — Git operations
- `/review` — Code review
```

### Discovery & Loading

**Discovery Order (first found wins):**

1. `.hermes.md`
2. `HERMES.md`
3. Falls back to `.cursorrules`

**Injection into system prompt:**

```
══════════════════════════════════════════════
PROJECT CONTEXT (from .hermes.md)
══════════════════════════════════════════════
[contents injected here]
```

### Best Practices

✅ **DO:**

- Include project goals and conventions
- Define team standards
- Specify verification procedures
- Document when to use which tool
- Keep it concise (< 2KB)

❌ **DON'T:**

- Store secrets or API keys
- Include binary files or large data
- Duplicate global configuration
- Create conflicting instructions

---

## API Key Setup

### OpenRouter (Recommended)

1. **Sign up:** https://openrouter.ai/
2. **Create key:** Dashboard → API Keys
3. **Set in Hermes:**

```bash
hermes config set OPENROUTER_API_KEY sk-or-v1-xxxxx
hermes config set model openrouter/gpt-4o
```

### Google Gemini

1. **Get API Key:** https://aistudio.google.com/app/apikey
2. **Set in Hermes:**

```bash
hermes config set GOOGLE_API_KEY AIzaSyxxxxxxxxxxxx
hermes config set model gemini-2.0-flash
```

### OpenAI GPT-4

1. **Get API Key:** https://platform.openai.com/api-keys
2. **Set in Hermes:**

```bash
hermes config set OPENAI_API_KEY sk-proj-xxxxx
hermes config set model gpt-4o
```

### Anthropic Claude

1. **Get API Key:** https://console.anthropic.com/
2. **Set in Hermes:**

```bash
hermes config set ANTHROPIC_API_KEY sk-ant-xxxxx
hermes config set model claude-3.5-sonnet
```

### Verify API Key

```bash
hermes chat "Hello, what is 2 + 2?"
```

Expected: "2 + 2 = 4"

---

## MCP Server Configuration

### Available MCP Servers (7/8 enabled)

| Server                  | Type  | Purpose            | Status         |
| ----------------------- | ----- | ------------------ | -------------- |
| **filesystem**          | stdio | File operations    | ✓ Enabled      |
| **sequential-thinking** | stdio | Reasoning/analysis | ✓ Enabled      |
| **next-devtools**       | stdio | Next.js dev tools  | ✓ Enabled      |
| **playwright**          | stdio | Browser automation | ✓ Enabled      |
| **context7**            | HTTP  | Doc lookup         | ✓ Enabled      |
| **gh_grep**             | HTTP  | GitHub search      | ✓ Enabled      |
| **docker**              | stdio | Docker management  | ✓ Enabled      |
| **docker-gateway**      | stdio | Docker gateway     | ✗ Windows only |

### Docker MCP Server (40+ Tools)

#### Enable Docker Support

```bash
# Set terminal backend to docker
hermes config set terminal.backend docker

# Or use local backend with docker tools
hermes config set terminal.backend local
```

#### List Docker Tools

```bash
hermes tools list | grep docker
```

#### Docker MCP Tools Available

**Container Management:**

- `docker_container_list` — List containers
- `docker_container_start` — Start container
- `docker_container_stop` — Stop container
- `docker_container_restart` — Restart
- `docker_container_remove` — Remove
- `docker_container_logs` — View logs
- `docker_container_stats` — Resource usage
- `docker_container_exec` — Execute command

**Image Management:**

- `docker_image_list` — List images
- `docker_image_build` — Build image
- `docker_image_pull` — Pull from registry
- `docker_image_push` — Push to registry
- `docker_image_remove` — Remove image
- `docker_image_inspect` — Get details

**Compose Management:**

- `docker_compose_up` — Start services
- `docker_compose_down` — Stop services
- `docker_compose_ps` — List services
- `docker_compose_logs` — View logs
- `docker_compose_exec` — Execute in service

**Database Operations:**

- `docker_db_query` — Execute SQL
- `docker_db_backup` — Create backup
- `docker_db_restore` — Restore backup
- `docker_db_status` — Check status

### Configure Custom MCP Server

```yaml
mcp_servers:
    custom_server:
        type: "stdio"
        command: "npx custom-server"
        enabled: true
        env:
            API_KEY: "${CUSTOM_API_KEY}"
```

Or via CLI:

```bash
hermes mcp add custom_server --type stdio --command "npx custom-server"
```

---

## Terminal Backend Setup

### Local Backend (Default)

**Best for:** Development, single machine

```yaml
terminal:
    backend: "local"
    timeout_seconds: 60
    max_output_bytes: 50000
```

### Docker Backend

**Best for:** Isolation, containerized workflows

```yaml
terminal:
    backend: "docker"
    docker:
        image: "nikolaik/python-nodejs:python3.11-nodejs20"
        binary: "/usr/bin/docker" # or podman
```

### SSH Backend (Remote)

**Best for:** Cloud deployment, security

```yaml
terminal:
    backend: "ssh"
    ssh:
        host: "192.168.1.100"
        user: "agent"
        port: 22
        key: "~/.ssh/id_rsa"
```

**Benefits:**

- Agent cannot read `.env` (API keys protected)
- Agent cannot modify its own code
- Remote server acts as sandbox
- Can enable passwordless sudo on remote

### Setup SSH Remote

On your server:

```bash
# Create agent user
sudo useradd -m agent

# Create SSH key
ssh-keygen -t ed25519 -f ~/.ssh/hermes_key

# Copy public key to server
ssh-copy-id -i ~/.ssh/hermes_key agent@192.168.1.100

# Allow passwordless sudo (optional)
echo "agent ALL=(ALL) NOPASSWD:ALL" | sudo tee /etc/sudoers.d/agent
```

In Hermes config:

```bash
hermes config set terminal.backend ssh
hermes config set terminal.ssh.host 192.168.1.100
hermes config set terminal.ssh.user agent
hermes config set terminal.ssh.key ~/.ssh/hermes_key
```

---

## Verification & Testing

### Check Installation

```bash
hermes --version
```

### Verify Configuration

```bash
hermes config show
```

### List All Available Tools

```bash
hermes tools list
```

Expected: 250+ tools

### List MCP Servers

```bash
hermes mcp list
```

Expected: 7/8 enabled

### Test LLM Connection

```bash
hermes chat "What is your name?"
```

Expected: LLM responds with its identity

### Test File Operations

```bash
hermes chat "Create a file called test.txt with the content 'Hello, World!'"
```

Check: `ls -la test.txt`

### Test Docker Operations

```bash
hermes chat "List all Docker containers"
```

Expected: Container list

### Test Web Search

```bash
hermes chat "Search for latest AI news"
```

Expected: Search results

### Test Terminal Execution

```bash
hermes chat "Run 'echo Hello from Hermes' in terminal"
```

Expected: "Hello from Hermes"

---

## Troubleshooting

### Issue: "hermes: command not found"

**Solution:**

```bash
# Check if installer added to PATH
echo $PATH | grep hermes

# If not, add manually
export PATH="$HOME/.hermes/bin:$PATH"
echo 'export PATH="$HOME/.hermes/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

### Issue: "API key not configured"

**Solution:**

```bash
# Set API key
hermes config set OPENROUTER_API_KEY sk-or-v1-xxxxx

# Verify
hermes config show | grep OPENROUTER
```

### Issue: "MCP server not responding"

**Solution:**

```bash
# Restart MCP servers
hermes mcp restart

# Check status
hermes mcp list
```

### Issue: "Terminal timeout"

**Solution:**

```bash
# Increase timeout
hermes config set terminal.timeout_seconds 120

# Or use docker backend for more isolation
hermes config set terminal.backend docker
```

### Issue: "Out of memory"

**Solution:**

```bash
# Reduce output limit
hermes config set agent_settings.tool_output_max_bytes 25000

# Or use SSH backend
hermes config set terminal.backend ssh
```

### Enable Debug Logging

```bash
hermes config set logging.level DEBUG

# View logs
tail -f ~/AppData/Local/hermes/hermes.log
```

---

## Quick Reference

### Essential Commands

```bash
hermes --version                           # Check version
hermes setup                               # Run setup wizard
hermes config show                         # Show config
hermes config set KEY value                # Set config
hermes chat "Your prompt"                  # Chat with Hermes
hermes tools list                          # List all tools
hermes mcp list                            # List MCP servers
hermes mcp restart                         # Restart MCP
```

### Common Configurations

```bash
# Use GPT-4o
hermes config set model gpt-4o

# Use Docker backend
hermes config set terminal.backend docker

# Use SSH remote
hermes config set terminal.backend ssh

# Disable specific toolset
hermes config set enabled_toolsets -web

# Increase timeout
hermes config set terminal.timeout_seconds 120
```

---

**Document Version:** 1.0  
**Hermes Version:** v0.14.0+  
**Last Updated:** May 25, 2026  
**Author:** Alexa

# Use SSH remote

hermes config set terminal.backend ssh

# Disable specific toolset

hermes config set enabled_toolsets -web

# Increase timeout

hermes config set terminal.timeout_seconds 120

```

---

**Document Version:** 1.0
**Hermes Version:** v0.14.0+
**Last Updated:** May 25, 2026
**Author:** Alexa
```

