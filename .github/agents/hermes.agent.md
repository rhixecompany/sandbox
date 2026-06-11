---
description: >
  'Hermes AI orchestration agent for multi-step workflows, delegation, platform
  integrations, hooks, plugins, and memory-intensive tasks via ACPX'
tools: ["terminal", "search", "filesystem", "web/fetch", "browser", "image_gen"]
model: "openrouter/owl-alpha (adminbot profile)"
---

# Hermes Agent

Delegate orchestration, multi-agent, platform-integration, and governance tasks to Hermes.

## When to Use

- Multi-step workflows with agent delegation
- Platform integrations (Slack, Discord, webhooks, cron)
- Kanban/todo-driven automation
- Memory-intensive or long-running sessions
- Security auditing or sensitive environment tasks
- Tasks requiring skills from Hermes's skills hub
- Hook and plugin management
- Profile maintenance (USER.md, SOUL.md, MEMORY.md)

## How to Invoke

```bash
# Headless one-shot via ACPX
acpx hermes exec "<prompt>"

# With auto-approval
acpx --approve-all hermes exec "<prompt>"

# Named session (stateful)
acpx hermes -s my-session exec "<prompt>"

# Direct Hermes CLI
hermes "<prompt>"
hermes acp  # ACP server mode
```

## ACP Mode

Hermes exposes an ACP server via `hermes acp`. ACPX routes to it using the agent name `hermes`.

## Config

- Main config: `~/AppData/Local/hermes/config.yaml`
- Skills hub: `~/AppData/Local/hermes/skills/`
- Hooks: `~/AppData/Local/hermes/hooks/`
- Plugins: `~/AppData/Local/hermes/plugins/`
- Logs: `~/AppData/Local/hermes/logs/`

## Profiles

| Profile           | Model                             | Use Case                |
| ----------------- | --------------------------------- | ----------------------- |
| **adminbot** ◆    | openrouter/owl-alpha              | General/devops (active) |
| default           | nvidia/nemotron-3-super-120b-a12b | Default fallback        |
| code-architect    | openrouter/owl-alpha              | Implementation          |
| creative-director | openrouter/owl-alpha              | Creative work           |
| exec-assistant    | openrouter/owl-alpha              | Administrative          |
| patient-tutor     | openrouter/owl-alpha              | Teaching                |
| research-analyst  | openrouter/owl-alpha              | Research/synthesis      |

Switch: `hermes profile use <name>`

## ACPX Agents

| Agent       | Version | Best For                               |
| ----------- | ------- | -------------------------------------- |
| Copilot CLI | 1.0.56  | Quick explanations, PRs (~50 req/week) |

## Active Hooks

| Hook                | Events                                        | Skip Flag                    |
| ------------------- | --------------------------------------------- | ---------------------------- |
| session-logger      | on_session_start, on_session_end, pre_llm_call | `SKIP_LOGGING=true`          |
| session-auto-commit | on_session_end                                | `SKIP_AUTO_COMMIT=true`      |
| governance-audit    | on_session_start, on_session_end, pre_llm_call | `SKIP_GOVERNANCE_AUDIT=true` |

## Active Plugins

- `disk-cleanup` — Disk cleanup utilities
- `model-providers/openrouter` — OpenRouter model provider
- `security-guidance` — Security guidance

## Skills (Selection)

| Skill                            | Purpose                                         |
| -------------------------------- | ----------------------------------------------- |
| `hermes-hooks-manager`           | Create, update, delete, test, debug hooks       |
| `hermes-plugins-manager`         | Create, update, delete, enable, disable plugins |
| `profile-maintenance`            | Audit/update USER.md, SOUL.md, MEMORY.md        |
| `user-communication-preferences` | Alexa's communication preferences               |

## Git

- Convention: `type: description` (feat, fix, docs, refactor, test, chore, perf)
- No backups (`.bak`, `.backup`, `.old`) — use git for rollback
- Hermes root: `~/AppData/Local/hermes/`
- Workspace: `C:\Users\Alexa\Desktop\SandBox`
