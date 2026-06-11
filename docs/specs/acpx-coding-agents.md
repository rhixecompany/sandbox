# Feature Spec: ACPX Coding Agent Integration

## Qwen Code · OpenCode · Hermes

**Version:** 1.0  
**Date:** 2026-05-29  
**Linked Plan:** `session-state/plan.md`  
**Status:** Active

---

## Overview

This spec covers the complete setup, configuration, authentication, and ACPX
integration of three coding agents in this workspace:

| Agent            | Version | Installed At                                                 | ACP Command    |
| ---------------- | ------- | ------------------------------------------------------------ | -------------- |
| **Qwen Code**    | 0.17.0  | `C:\nvm4w\nodejs\qwen.ps1`                                   | `qwen --acp`   |
| **OpenCode**     | 1.15.12 | `C:\Users\Alexa\.bun\bin\opencode.exe`                       | `opencode acp` |
| **Hermes Agent** | 0.15.1  | `%LOCALAPPDATA%\hermes\hermes-agent\venv\Scripts\hermes.exe` | `hermes acp`   |
| **ACPX**         | 0.10.0  | `C:\nvm4w\nodejs\acpx.ps1`                                   | — orchestrator |

**Goal:** Route all coding tasks through ACPX so agents are invoked headlessly
and results returned to the calling agent (Copilot CLI, Hermes, or scripts).

---

## Architecture

```text
User / Copilot CLI
      │
      ▼
  ACPX (~/.acpx/config.json)
  ├── agent: qwen  ──►  qwen --acp  (OpenRouter: qwen3.6-plus)
  ├── agent: opencode  ──► opencode acp  (GitHub Copilot / Qwen / Google)
  └── agent: hermes  ──►  hermes acp  (Hermes ACP server)

Hermes (orchestrator / persistent)
  ├── provider: copilot-acp  →  acp://copilot
  ├── provider: qwen-code  →  acp://qwen
  ├── OpenCode path: direct ACPX target (`acpx opencode exec`)
  ├── skill: qwen-code  (delegate coding tasks)
  ├── skill: opencode  (delegate coding tasks)
  └── skill: acpx-agent-routing  (intelligent routing)

OpenCode (~/.config/opencode/opencode.json)
  ├── plugin: opencode-handoff  (ACPX handoff)
  ├── mcp: context7, playwright, filesystem, memory, sequential-thinking
  └── agents: qwen-code subagent, hermes subagent
```

---

## Feature Areas

### F1: ACPX Global Agent Registry

**File:** `~/.acpx/config.json`

- Register `qwen` → `qwen --acp`
- Register `opencode` → `opencode acp`
- Register `hermes` → `hermes-acp`
- Default agent: `qwen` (fastest for coding tasks)
- Default approval mode: `approve-reads`

**Usage patterns:**

```bash
acpx qwen "fix the failing tests"
acpx opencode "refactor auth module"
acpx hermes "orchestrate: run tests and summarize"
acpx --approve-all qwen exec "one-shot: summarize repo"
```

### F2: Qwen Code Configuration

**Files:**

- `~/.qwen/settings.json` — global settings
- `SandBox/.qwen/settings.json` — project settings

**Requirements:**

- OpenRouter provider with `qwen/qwen3.6-plus` as default (free tier)
- Fallback: `openai/gpt-oss-120b:free` (free via OpenRouter)
- Z-ai GLM model as secondary free option
- `tools.approvalMode = "auto_edit"` for ACPX headless operation
- MCP servers: filesystem, context7, sequential-thinking, gh_grep, exa, memory

**Auth:** Already configured via `OPENROUTER_API_KEY` in `~/.qwen/settings.json`

### F3: Hermes Configuration

**File:** `~/.hermes/config.yaml` (at `%LOCALAPPDATA%\hermes\config.yaml`)

**Requirements:**

- `qwen-code` provider: OpenRouter with `qwen/qwen3.6-plus` ✅ (exists)
- `copilot-acp` provider: `acp://copilot` ✅ (exists)
- Skills search paths include new ACPX coding skills
- Fallback chain should not assume Hermes OpenCode provider unless explicitly
  validated

### F4: Hermes Skills

**Location:** `%LOCALAPPDATA%\hermes\skills\`

Skills to create/update:

| Skill                         | Purpose                                     |
| ----------------------------- | ------------------------------------------- |
| `qwen-code/SKILL.md`          | Delegate coding tasks to Qwen Code via ACPX |
| `opencode/SKILL.md`           | Delegate coding tasks to OpenCode via ACPX  |
| `acpx-agent-routing/SKILL.md` | Intelligent routing across all three agents |
| `copilot-cli/SKILL.md`        | Use Copilot CLI for GitHub-native tasks     |

### F5: Hermes Hooks

**Location:** `%LOCALAPPDATA%\hermes\hooks\`

Hooks to create:

- `coding-task-start.sh` — announce + start ACPX session
- `coding-task-done.sh` — summarize + log result

### F6: OpenCode Integration

**File:** `~/.config/opencode/opencode.json`

**Requirements:**

- Verify `opencode-handoff` plugin is functioning (ACPX handoff)
- Add `qwen-code` subagent entry (invokes via acpx)
- Add `hermes` subagent entry (invokes via acpx)
- Add MCP: `exa` for web search (already present ✅)

### F7: Project-Level Qwen Settings

**File:** `SandBox/.qwen/settings.json`

- `tools.approvalMode = "auto_edit"` — non-interactive for ACPX
- Override model to `qwen/qwen3-coder-plus:free` if available
- Enable MCP servers for SandBox workspace

### F8: Copilot Agents

**Location:** `SandBox/.github/agents/`

New agent files:

- `qwen-code.agent.md` — delegate coding tasks to Qwen Code via ACPX
- `hermes.agent.md` — use Hermes for orchestration and persistent tasks

### F9: Docs Update

**File:** `SandBox/docs/agents-cross-reference.md`

Update the table with accurate version info, ACP commands, and skill names for
all three platforms.

---

## Authentication Summary

| Tool      | Method                                             | Key/Config                                      |
| --------- | -------------------------------------------------- | ----------------------------------------------- |
| Qwen Code | OpenRouter API Key                                 | `OPENROUTER_API_KEY` in `~/.qwen/settings.json` |
| OpenCode  | GitHub Copilot token (auto) + OpenRouter           | `~/.config/opencode/.env.local`                 |
| Hermes    | OpenRouter (qwen-code provider) + Copilot fallback | `~/.hermes/.env`                                |
| ACPX      | None (orchestrator only)                           | Inherits from agent env                         |

---

## MCP Servers (Shared)

All three agents should have access to:

| MCP Server            | Purpose                  | Protocol       |
| --------------------- | ------------------------ | -------------- |
| `filesystem`          | File read/write access   | local (bunx)   |
| `context7`            | Library docs lookup      | remote         |
| `gh_grep`             | GitHub code search       | remote         |
| `exa`                 | Web search               | remote         |
| `sequential-thinking` | Chain-of-thought         | local (bunx)   |
| `memory`              | Persistent KV store      | local (bunx)   |
| `playwright`          | Browser automation       | local (bunx)   |
| `MCP_DOCKER`          | Docker tools via gateway | local (docker) |

---

## Success Criteria

- [ ] `acpx qwen exec "what does this repo do?"` returns a response
- [ ] `acpx opencode exec "list top 3 files"` returns a response (NDJSON
      preamble warnings acceptable if response completes)
- [ ] `hermes doctor` reports no critical errors
- [ ] Hermes `/qwen-code` skill executes a coding task
- [ ] Hermes `/opencode` skill executes a coding task
- [ ] `acpx --format json qwen exec "hello"` returns valid NDJSON
- [ ] OpenCode loads qwen-code subagent without errors
- [ ] All three agents share the same MCP server configs
