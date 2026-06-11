---
name: opencode
title: Opencode
description: "Delegate coding to OpenCode CLI (features, PR review)."
version: 1.2.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, OpenCode, Autonomous, Refactoring, Code-Review]
    related_skills: [claude-code, codex, hermes-agent]
---
## Goal
Delegate coding to OpenCode CLI (features, PR review).


# OpenCode CLI

Use [OpenCode](https://opencode.ai) as an autonomous coding worker orchestrated by Hermes terminal/process tools. OpenCode is a provider-agnostic, open-source AI coding agent with a TUI and CLI.

## Workflow
### Phase 1: Preparation

- Understand the context and requirements.
- Gather necessary tools and resources.

### Phase 2: Execution

- Perform the core actions required by the skill.
- Apply the techniques and procedures outlined.

### Phase 3: Verification

- Verify the results against the expected outcomes.
- Confirm that the task has been completed successfully.


## When to Use

- User explicitly asks to use OpenCode
- You want an external coding agent to implement/refactor/review code
- You need long-running coding sessions with progress checks
- You want parallel task execution in isolated workdirs/worktrees
- ACPX integration: use `opencode acp` to start ACP server mode
- Run coding tasks with GitHub Copilot, Qwen, or Google Gemini models
- Leverage LSP-based code intelligence (type-checking, symbol lookup)
- Manage multi-session coding workflows with persistent storage
- Use OpenCode's rich plugin ecosystem (18+ plugins including DCP, subtask2, smart-codebase)
- File change tracking and diff visualization during coding sessions

## Prerequisites

- OpenCode installed: `npm i -g opencode-ai@latest` or `brew install anomalyco/tap/opencode`
- Auth configured: `opencode auth login` or set provider env vars (OPENROUTER_API_KEY, etc.)
- Verify: `opencode auth list` should show at least one provider
- Git repository for code tasks (recommended)
- `pty=true` for interactive TUI sessions

## Binary Resolution (Important)

Shell environments may resolve different OpenCode binaries. If behavior differs between your terminal and Hermes, check:

```
terminal(command="which -a opencode")
terminal(command="opencode --version")
```

If needed, pin an explicit binary path:

```
terminal(command="$HOME/.opencode/bin/opencode run '...'", workdir="~/project", pty=true)
```

## One-Shot Tasks

Use `opencode run` for bounded, non-interactive tasks:

```
terminal(command="opencode run 'Add retry logic to API calls and update tests'", workdir="~/project")
```

Attach context files with `-f`:

```
terminal(command="opencode run 'Review this config for security issues' -f config.yaml -f .env.example", workdir="~/project")
```

Show model thinking with `--thinking`:

```
terminal(command="opencode run 'Debug why tests fail in CI' --thinking", workdir="~/project")
```

Force a specific model:

```
terminal(command="opencode run 'Refactor auth module' --model openrouter/anthropic/claude-sonnet-4", workdir="~/project")
```

## Interactive Sessions (Background)

For iterative work requiring multiple exchanges, start the TUI in background:

```
terminal(command="opencode", workdir="~/project", background=true, pty=true)
# Returns session_id

# Send a prompt
process(action="submit", session_id="<id>", data="Implement OAuth refresh flow and add tests")

# Monitor progress
process(action="poll", session_id="<id>")
process(action="log", session_id="<id>")

# Send follow-up input
process(action="submit", session_id="<id>", data="Now add error handling for token expiry")

# Exit cleanly — Ctrl+C
process(action="write", session_id="<id>", data="\x03")
# Or just kill the process
process(action="kill", session_id="<id>")
```

**Important:** Do NOT use `/exit` — it is not a valid OpenCode command and will open an agent selector dialog instead. Use Ctrl+C (`\x03`) or `process(action="kill")` to exit.

### TUI Keybindings

| Key | Action |
|-----|--------|
| `Enter` | Submit message (press twice if needed) |
| `Tab` | Switch between agents (build/plan) |
| `Ctrl+P` | Open command palette |
| `Ctrl+X L` | Switch session |
| `Ctrl+X M` | Switch model |
| `Ctrl+X N` | New session |
| `Ctrl+X E` | Open editor |
| `Ctrl+C` | Exit OpenCode |

### Resuming Sessions

After exiting, OpenCode prints a session ID. Resume with:

```bash
terminal(command="opencode -c", workdir="~/project", background=true, pty=true)  # Continue last session
terminal(command="opencode -s ses_abc123", workdir="~/project", background=true, pty=true)  # Specific session
## ACPX Integration

**Note:** OpenCode does NOT function as a Hermes ACP model provider (`acp://opencode` is not supported by Hermes). Use OpenCode via direct CLI commands with the `terminal` tool.

### ACP Server Mode (Standalone)

OpenCode can run as an ACP server for external clients, but Hermes does not have a built-in client for it:

OpenCode supports ACP (Agent Client Protocol) server mode:

```bash
# Start OpenCode ACP server
opencode acp

# Then connect from Hermes via ACP provider
```

### Via ACPX exec (preferred)

OpenCode is fully accessible via the `acpx` binary (v0.10.0+), which handles session management, permissions, and dispatch:

```bash
# One-shot task (recommended)
acpx --approve-all --timeout 60 opencode exec "explain the auth flow in this project"

# Persistent named session
acpx opencode -s feature-auth "implement OAuth2 login"

# JSON output for orchestration
acpx --format json --approve-all --timeout 60 opencode exec "list all TODO comments" > todos.ndjson

# Parallel workstreams
acpx --approve-all --timeout 120 opencode -s tests "write unit tests for src/auth/" &
acpx --approve-all --timeout 120 opencode -s docs "generate API documentation" &
wait
```

### Via terminal tool (direct CLI)

```python
# Quick one-shot task (direct)
terminal(command="opencode run 'Add error handling to API routes' --model opencode/big-pickle", workdir="~/project", timeout=300)

# Chained: {prompt} then {then command}
terminal(command="opencode run '{prompt}' --model opencode/big-pickle && opencode run '{then}' --model opencode/big-pickle", timeout=600)
```

### Via ACPX exec (preferred — uses acpx binary v0.10.0+)

```bash
# Quick one-shot task via ACPX
acpx --approve-all --timeout 60 opencode exec 'Add error handling to API routes'

# Chained via ACPX
acpx --approve-all --timeout 60 opencode exec '{prompt}' && acpx --approve-all --timeout 60 opencode exec '{then}'

# Specific model via ACPX
acpx --approve-all --timeout 60 opencode exec 'Refactor auth module' --model opencode/claude-sonnet-4-6

# Plan agent via ACPX
acpx --approve-all --timeout 60 opencode exec 'Review the auth module for security issues'
```

### Agent Selection for ACPX

OpenCode has two built-in agents:

| Agent | Role | Best For |
|-------|------|----------|
| `build` | Default. Full file/tool access | Development, implementation, debugging |
| `plan` | Read-only. Asks permission before edits | Code review, architecture analysis, planning |

Switch with Tab key in TUI or `--agent` flag:

```bash
opencode run "Review the auth module for security issues" --agent plan
```

## Common Flags

| Flag | Use |
|------|-----|
| `run 'prompt'` | One-shot execution and exit |
| `--continue` / `-c` | Continue the last OpenCode session |
| `--session <id>` / `-s` | Continue a specific session |
| `--agent <name>` | Choose OpenCode agent (build or plan) |
| `--model provider/model` | Force specific model |
| `--format json` | Machine-readable output/events |
| `--file <path>` / `-f` | Attach file(s) to the message |
| `--thinking` | Show model thinking blocks |
| `--variant <level>` | Reasoning effort (high, max, minimal) |
| `--title <name>` | Name the session |
| `--attach <url>` | Connect to a running opencode server |
| `acp` | Start ACP server mode |
| `--model opencode/<name>` | Model prefix must include `opencode/` (e.g. `opencode/claude-haiku-4-5`) |

## Procedure

1. Verify tool readiness:
   - `terminal(command="opencode --version")`
   - `terminal(command="opencode auth list")`
2. For bounded tasks, use `opencode run '...'` (no pty needed).
3. For iterative tasks, start `opencode` with `background=true, pty=true`.
4. Monitor long tasks with `process(action="poll"|"log")`.
5. If OpenCode asks for input, respond via `process(action="submit", ...)`.
6. Exit with `process(action="write", data="\x03")` or `process(action="kill")`.
7. Summarize file changes, test results, and next steps back to user.

## PR Review Workflow

OpenCode has a built-in PR command:

```
terminal(command="opencode pr 42", workdir="~/project", pty=true)
```

Or review in a temporary clone for isolation:

```
terminal(command="REVIEW=$(mktemp -d) && git clone https://github.com/user/repo.git $REVIEW && cd $REVIEW && opencode run 'Review this PR vs main. Report bugs, security risks, test gaps, and style issues.' -f $(git diff origin/main --name-only | head -20 | tr '\n' ' ')", pty=true)
```

## Parallel Work Pattern

Use separate workdirs/worktrees to avoid collisions:

```
terminal(command="opencode run 'Fix issue #101 and commit'", workdir="/tmp/issue-101", background=true, pty=true)
terminal(command="opencode run 'Add parser regression tests and commit'", workdir="/tmp/issue-102", background=true, pty=true)
process(action="list")
```

## Session & Cost Management

List past sessions:

```
terminal(command="opencode session list")
```

Check token usage and costs:

```
terminal(command="opencode stats")
terminal(command="opencode stats --days 7 --models anthropic/claude-sonnet-4")
```

## Pitfalls

- Interactive `opencode` (TUI) sessions require `pty=true`. The `opencode run` command does NOT need pty.
- `/exit` is NOT a valid command — it opens an agent selector. Use Ctrl+C to exit the TUI.
- PATH mismatch can select the wrong OpenCode binary/model config.
- If OpenCode appears stuck, inspect logs before killing:
  - `process(action="log", session_id="<id>")`
- Avoid sharing one working directory across parallel OpenCode sessions.
- Enter may need to be pressed twice to submit in the TUI (once to finalize text, once to send).
- **Model names require `opencode/` prefix** — `opencode run --model "claude-haiku-4-5"` fails because the model must be `opencode/claude-haiku-4-5`.
- `opencode run` may time out if the provider model takes too long to respond — set high timeouts or use `--format json` for streaming output.
- `bun-pty` may be unavailable on Windows installs — PTY tools will be disabled but `run` still works.

## Model Configuration

**Default model:** `opencode/big-pickle`

This is the primary model for all OpenCode coding tasks. Set it as the default in `opencode.json`:
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "opencode/big-pickle"
}
```

### Recommended Models

| Model | Use Case | Notes |
|-------|----------|-------|
| `opencode/big-pickle` | **Default** — all coding tasks | Same model as the Hermes agent, fast and reliable |
| `opencode/qwen3.6-plus-free` | OpenCode Zen provider | Free tier, good for testing |
| `opencode/claude-haiku-4-5` | Quick, lightweight tasks | Fast, cheap (GitHub Copilot provider) |
| `opencode/claude-sonnet-4-6` | Complex reasoning | Higher quality but slower |
| `opencode/gpt-5-mini` | Fast generation | GitHub Copilot provider |

## Key Plugins Active

- `opencode-handoff` — ACPX handoff support
- `@tarquinen/opencode-dcp` — Dynamic context protocol
- `@spoons-and-mirrors/subtask2` — Subtask decomposition
- `smart-codebase` — Codebase intelligence
- `oh-my-opencode-slim` — Enhanced UX
- `@howaboua/opencode-planning-toolkit` — Planning support

### Best Practices for Plugin Usage

1. OpenCode's LSP integration makes it ideal for TypeScript/JavaScript projects
2. Use `subtask2` plugin for complex multi-step coding tasks
3. Use `opencode-handoff` to transfer sessions between agents
4. OpenCode has auto-compact enabled — long sessions are automatically summarized
5. For unattended CI tasks, always use `--approve-all`

## Verification

Smoke tests (three tiers):

**Tier 1 — Quick (always works):**
```
acpx --approve-all --timeout 30 opencode exec 'Reply with exactly: OPENCODE_SMOKE_OK'
```

**Tier 2 — Direct CLI:**
```
terminal(command="opencode --version")
terminal(command="opencode run 'Respond with exactly: OPENCODE_SMOKE_OK' --model opencode/big-pickle", timeout=120)
```

**Tier 3 — ACP server mode:**
```
terminal(command="opencode acp --help")
```

Success criteria:
- `acpx opencode exec` returns result with expected output
- `--version` returns a version string (1.15.12+)
- `acp --help` shows ACP server options (port, hostname, cors)
- If model call succeeds: output includes `OPENCODE_SMOKE_OK`
- For code tasks: expected files changed and tests pass

## Rules

1. Prefer `opencode run` for one-shot automation — it's simpler and doesn't need pty.
2. Use interactive background mode only when iteration is needed.
3. Always scope OpenCode sessions to a single repo/workdir.
4. For long tasks, provide progress updates from `process` logs.
5. Report concrete outcomes (files changed, tests, remaining risks).
6. Exit interactive sessions with Ctrl+C or kill, never `/exit`.
```
