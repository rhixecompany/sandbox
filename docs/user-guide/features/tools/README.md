# Tools & Toolsets | Hermes Agent

## Overview

Tools extend the agent's capabilities and are organized into **toolsets** that can be enabled/disabled per platform. Hermes ships with a broad built-in tool registry covering web search, browser automation, terminal execution, file editing, memory, delegation, RL training, messaging, Home Assistant, and more.

> **Note:** Honcho cross-session memory is available as a memory provider plugin (`plugins/memory/honcho/`), not as a built-in toolset. See [Plugins](/docs/user-guide/features/plugins) for installation.

---

## Available Tools by Category

| Category | Tools | Description |
|----------|-------|-------------|
| **Web** | `web_search`, `web_extract` | Search the web and extract page content |
| **X Search** | `x_search` | Search X (Twitter) posts via xAI's built-in Responses tool — gated on xAI credentials (SuperGrok OAuth or `XAI_API_KEY`); off by default, opt in via `hermes tools` → 🐦 X (Twitter) Search |
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

**Authoritative references:** [Built-in Tools Reference](/docs/reference/tools-reference) | [Toolsets Reference](/docs/reference/toolsets-reference)

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

See [Toolsets Reference](/docs/reference/toolsets-reference) for the full set.

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

### Configuration (`~/.hermes/config.yaml`)

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

**Key behavior:** One persistent container, shared across the whole process.

- Hermes starts a single long-lived container on first use: `docker run -d ... sleep 2h`
- All terminal, file, and `execute_code` calls route through `docker exec` into that same container
- Working-directory changes, installed packages, environment tweaks, and files in `/workspace` persist across tool calls, `/new`, `/reset`, and `delegate_task` subagents
- Container stopped and removed on shutdown

> This means the Docker backend behaves like a persistent sandbox VM, not a fresh container per command. If you `pip install foo` once, it's there for the rest of the session. If you `cd /workspace/project`, subsequent `ls` calls see that directory.

**Persistence across restarts:** Controlled by `container_persistent` flag (see [Configuration → Docker Backend](/docs/user-guide/configuration#docker-backend)).

---

## SSH Backend (Recommended for Security)

```yaml
terminal:
  backend: ssh
```

```bash
# Set credentials in ~/.hermes/.env
TERMINAL_SSH_HOST=my-server.example.com
TERMINAL_SSH_USER=myuser
TERMINAL_SSH_KEY=~/.ssh/id_ed25519
# or
TERMINAL_SSH_PASSWORD=***
```

**Why SSH:** Keeps the agent's execution environment separate from your development machine. If the agent runs `rm -rf /`, it affects the remote sandbox, not your laptop.

---

## Modal Backend (Serverless)

```yaml
terminal:
  backend: modal
  modal_app: "hermes-sandbox"
```

Requires Modal account and `modal setup`. Good for burst workloads, no persistent server cost.

---

## MCP Tool Integration

MCP servers appear as **dynamic toolsets** named `mcp-<server_name>`. Tools are registered at runtime based on server capabilities and your `tools.include` / `tools.exclude` filters.

```bash
# List MCP-backed tools
hermes tools --platform cli | grep mcp-
```

---

## Tool Reference Quick Links

| Reference | URL |
|-----------|-----|
| Built-in Tools Reference | `/docs/reference/tools-reference` |
| Toolsets Reference | `/docs/reference/toolsets-reference` |
| MCP Integration | `/docs/user-guide/features/mcp` |
| Adding Custom Tools (Plugins) | `/docs/developer-guide/adding-tools` |

---

## Common Patterns

### Minimal CLI (web + terminal only)
```bash
hermes chat --toolsets "web,terminal"
```

### Full Coding Agent
```bash
hermes chat --toolsets "web,terminal,file,browser,skills,code_execution,delegation,memory"
```

### Bot with Messaging
```bash
hermes chat --toolsets "web,terminal,file,skills,messaging" --platform telegram
```

### Research Only
```bash
hermes chat --toolsets "web,search,skills,memory,session_search"
```

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Tool not available | Check `hermes tools` — is toolset enabled for platform? |
| Terminal fails | Check backend config; try `local` first |
| Browser not working | Ensure `npx` available; try `browser_vision` for debug |
| MCP tools missing | `/reload-mcp`; check `tools.include` in config |
| Image gen fails | Verify tool gateway or provider credentials |

---

**Source:** [Hermes Agent Docs - Tools](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)  
**Extracted:** 2026-06-08