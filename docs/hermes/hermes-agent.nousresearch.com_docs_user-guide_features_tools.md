# Source: https://hermes-agent.nousresearch.com/docs/user-guide/features/tools

# Tools & Toolsets | Hermes Agent

## Overview

Tools extend the agent's capabilities and are organized into **toolsets** that can be enabled/disabled per platform. Hermes ships with a broad built-in tool registry covering web search, browser automation, terminal execution, file editing, memory, delegation, RL training, messaging, Home Assistant, and more.

> **Note:** Honcho cross-session memory is available as a memory provider plugin (`plugins/memory/honcho/`), not as a built-in toolset. See [Plugins](/docs/user-guide/features/plugins) for installation.

---

## Available Tools by Category

| Category | Tools | Description |
|----------|-------|-------------|
| **Web** | `web_search`, `web_extract` | Search the web and extract page content |
| **X Search** | `x_search` | Search X (Twitter) posts/threads via xAI's built-in Responses tool — **gated on xAI credentials** (SuperGrok OAuth or `XAI_API_KEY`); off by default, opt in via `hermes tools` → 🐦 X (Twitter) Search |
| **Terminal & Files** | `terminal`, `process`, `read_file`, `patch` | Execute commands and manipulate files |
| **Browser** | `browser_navigate`, `browser_snapshot`, `browser_vision` | Interactive browser automation with text and vision support |
| **Media** | `vision_analyze`, `image_generate`, `text_to_speech` | Multimodal analysis and generation |
| **Agent Orchestration** | `todo`, `clarify`, `execute_code`, `delegate_task` | Planning, clarification, code execution, subagent delegation |
| **Memory & Recall** | `memory`, `session_search` | Persistent memory and session search |
| **Automation & Delivery** | `cronjob`, `send_message` | Scheduled tasks (create/list/update/pause/resume/run/remove) + outbound messaging |
| **Integrations** | `ha_*`, MCP server tools | Home Assistant, MCP, and other integrations |

### Tool Gateway (Nous Portal Subscribers)
Paid [Nous Portal](https://portal.nousresearch.com) subscribers can use web search, image generation, TTS, and browser automation through the **Tool Gateway** — no separate API keys needed.

```bash
# Enable via model config
hermes model

# Or configure individual tools
hermes tools
```

**References:** [Built-in Tools Reference](/docs/reference/tools-reference) | [Toolsets Reference](/docs/reference/toolsets-reference)

---

## Using Toolsets

```bash
# Use specific toolsets
hermes chat --toolsets "web,terminal"

# See all available tools
hermes tools

# Configure tools per platform (interactive)
hermes tools
```

### Common Toolsets
`web`, `search`, `terminal`, `file`, `browser`, `vision`, `image_gen`, `moa`, `skills`, `tts`, `todo`, `memory`, `session_search`, `cronjob`, `code_execution`, `delegation`, `clarify`, `homeassistant`, `messaging`, `spotify`, `discord`, `discord_admin`, `debugging`, `safe`

### Platform Presets
- `hermes-cli` — CLI default
- `hermes-telegram` — Telegram bot
- `mcp-<server>` — Dynamic MCP toolsets

**Full reference:** [Toolsets Reference](/docs/reference/toolsets-reference)

---

## Terminal Backends

The terminal tool executes commands in different environments:

| Backend | Description | Use Case |
|---------|-------------|----------|
| `local` | Run on your machine (default) | Development, trusted tasks |
| `docker` | Isolated containers | Security, reproducibility |
| `ssh` | Remote server | Sandboxing, keep agent away from its own code |
| `singularity` | HPC containers | Cluster computing, rootless |
| `modal` | Cloud execution | Serverless, scale |
| `daytona` | Cloud sandbox workspace | Persistent remote dev environments |

### Configuration (`~/AppData/Local/hermes/config.yaml`)

```yaml
terminal:
  backend: local        # or: docker, ssh, singularity, modal, daytona
  cwd: "."              # Working directory
  timeout: 180          # Command timeout in seconds
```

---

## Docker Backend (Persistent Sandbox)

```yaml
terminal:
  backend: docker
  docker_image: python:3.11-slim
```

**Key behavior:** Hermes starts **one persistent container** on first use (`docker run -d ... sleep 2h`) and routes all `terminal`, `file`, and `execute_code` calls through `docker exec` into that same container.

- Working-directory changes, installed packages, environment tweaks, and files in `/workspace` persist across tool calls
- Survives `/new`, `/reset`, and `delegate_task` subagents for the lifetime of the Hermes process
- Container stopped/removed on shutdown
- Behaves like a persistent sandbox VM, not a fresh container per command

```bash
# Example: pip install persists for session
pip install foo
cd /workspace/project
ls  # sees that directory
```

**Persistence across restarts:** Controlled by `container_persistent` flag (default: `true`) — when enabled, `/workspace` and `/root` survive Hermes restarts.

---

## SSH Backend (Recommended for Security)

```yaml
terminal:
  backend: ssh
```

```bash
# Set credentials in ~/AppData/Local/hermes/.env
TERMINAL_SSH_HOST=my-server.example.com
TERMINAL_SSH_USER=myuser
TERMINAL_SSH_KEY=~/.ssh/id_rsa
```

> Agent cannot modify its own code when running via SSH backend — ideal for untrusted operations.

---

## Tool Configuration

Tools can be configured per-toolset or globally. Use `hermes tools` for interactive configuration, or edit `~/AppData/Local/hermes/config.yaml` directly.

Example tool config:
```yaml
tools:
  web_search:
    max_results: 10
    default_backend: "duckduckgo"
  terminal:
    backend: ssh
    timeout: 300
```