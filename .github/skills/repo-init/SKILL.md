---
name: repo-init
title: Repo Init for All Installed AI Agents
description: Use when initializing a repo for all installed AI agents.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
- repo-init
- ai-agents
- inventory
- scaffolding
- cross-platform
---

# Repo Init for All Installed AI Agents

## Overview

Detect every installed AI coding agent on this machine (Hermes, OpenCode, Codex, Copilot, Claude, Cursor, GitHub CLI), report where each agent's system prompt and context files live, and scaffold a repo so any new or existing project starts agent-ready.

## When to Use

- User says "init this repo for all agents", "make this repo agent-ready", "repo init"
- User asks which AI agents are installed and where their prompts/context files are
- User wants a new repo to include AGENTS.md / CLAUDE.md / .cursorrules / agent docs
- Verifying a repo's agent-context coverage

## Prerequisites

- Python 3.10+ on PATH
- Script lives at `scripts/repo-init.py` in the workspace (SandBox)
- On Windows/MSYS use `MSYS_NO_PATHCONV=1` prefix; pass Windows-style paths (bash `/tmp` maps differently than `C:\tmp`)

## Workflow

### Phase 1: Inventory agents

```bash
cd <workspace>
MSYS_NO_PATHCONV=1 python scripts/repo-init.py --list-agents
MSYS_NO_PATHCONV=1 python scripts/repo-init.py --list-agents --json   # machine-readable
```

Output: one row per platform with agent count, detail, system prompt path, context file paths.

Refresh the committed inventory doc:

```bash
MSYS_NO_PATHCONV=1 python scripts/repo-init.py --list-agents > docs/ai-agents-inventory.md
```

### Phase 2: Scaffold a repo

```bash
MSYS_NO_PATHCONV=1 python scripts/repo-init.py --init <target-dir>
MSYS_NO_PATHCONV=1 python scripts/repo-init.py --init .   # current repo
MSYS_NO_PATHCONV=1 python scripts/repo-init.py --init . --force  # overwrite existing
```

Creates (idempotent, skips existing): `AGENTS.md`, `docs/ai-agents-inventory.md`, `.github/agents/README.md`.

### Phase 3: Verify

```bash
MSYS_NO_PATHCONV=1 python scripts/repo-init.py --verify <target-dir>
# exit 0 + "RESULT: OK" when all templates present
```

## Detection Roots (Windows 11, this machine)

| Platform | CLI / root | System prompt | Context files |
|----------|------------|---------------|---------------|
| Hermes | `~/AppData/Local/hermes/` | root `SOUL.md` | `memories/USER.md`, `memories/MEMORY.md`, `profiles/<name>/` |
| OpenCode | `~/.opencode/` | `~/.opencode/command/*.md` | workspace `opencode.json`, `~/.opencode/skills/` |
| Codex | `~/.codex/` | `~/.codex/agents/*.toml` | `~/.codex/config.toml`, `~/.codex/skills/hermes-auto/` |
| Copilot | `~/.copilot/` | `.github/agents/*.agent.md` | `~/.copilot/config.json` |
| Claude | `~/.claude/` | `~/.claude/` (global CLAUDE.md optional) | workspace `CLAUDE.md` |
| Cursor | — | workspace `.cursorrules` | `.cursorrules` |
| GitHub CLI | `gh` | n/a (tool, not an agent) | n/a |

Detection is runtime-probed — paths may drift; always re-run `--list-agents` for current state.

## Pitfalls

- **MSYS path trap**: git-bash `/tmp` is NOT `C:\tmp`. Pass `C:\Users\...` Windows paths or MSYS-mapped ones; `os.path.abspath` on `/tmp/x` resolves to `C:\tmp\x` which does not exist.
- **Idempotency by design**: `--init` never overwrites existing files. An existing real `.github/agents/*.agent.md` set is preserved. Use `--force` only when you intend to replace templates.
- **No secrets**: templates are generic. Never add user-specific absolute paths or credentials to committed AGENTS.md/CLAUDE.md content.
- **Hermes memories**: root `USER.md`/`MEMORY.md` live under `memories/`, NOT the hermes root. Script probes both; do not assume one location.
- **Profile context is machine-local**: do not copy per-profile Hermes context into a repo; AGENTS.md carries a pointer instead.

## Verification Checklist

- [ ] `--list-agents` prints all installed platforms with real paths
- [ ] `--init <dir>` creates AGENTS.md + inventory + agents README
- [ ] `--verify <dir>` exits 0 with RESULT: OK
- [ ] Second `--init` is a no-op (idempotent)
- [ ] `docs/ai-agents-inventory.md` regenerated from live output

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
