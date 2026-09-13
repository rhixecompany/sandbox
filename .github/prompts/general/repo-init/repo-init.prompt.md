---
name: repo-init
title: Repo Init for All Installed AI Agents
description: Initialize a new or existing repo for every installed AI coding agent — inventory agents,
  scaffold context files, verify resolution.
version: 1.1.0
license: MIT
author: Hermes Agent
trigger: /repo-init
toolsets:
- file
- terminal
skills: []
dependencies:
- skill:repo-init
- skill:verification-before-completion
formatter: default
metadata:
  hermes:
    profile: code-architect
    mcp_servers: []
    context_size: large
  copilot:
    context_size: large
    extensions: []
    keybinding: null
  opencode:
    command: opencode /repo-init
    flags: {}
    help: Initialize a new or existing repo for every installed AI coding agent — inven...
  codex:
    model_override: null
    system_prompt_id: null
    temperature: null
    max_tokens: null
tags:
- agent-type:hermes
- agents
- ai-assistant
- generator
- git
- ml
- prompts
- typescript
scripts:
- scripts/repo-init.py
## Goal

Initialize a new or existing repo for **all installed AI coding agents**: inventory every agent (Hermes, OpenCode, Codex, Copilot, Claude, Cursor, GitHub CLI) with its system prompt and context file locations, scaffold generic context files, and verify the result.

## Context

- **Script:** `scripts/repo-init.py` (workspace root: `C:\Users\Alexa\Desktop\SandBox`)
- **Inventory doc:** `docs/ai-agents-inventory.md` (regenerated from live output)
- **Detection:** runtime-probed filesystem; do not hardcode agent lists
- **Windows/MSYS:** prefix commands with `MSYS_NO_PATHCONV=1`; pass Windows-style paths

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

1. Execute phases in order; do not reorder.
2. Each phase must pass its gate before advancing.
3. **Idempotent only** — `--init` never overwrites existing files unless `--force` is explicit.
4. **No secrets** — never write credentials or user-specific absolute paths into committed templates.
5. **No backup files** — use git for rollback; never create `.bak`/`.old` copies.

## Phases

| Order | Phase                 | Gate                                                 |
| ----- | --------------------- | ---------------------------------------------------- |
| 1     | Inventory agents      | `--list-agents` prints all platforms with real paths |
| 2     | Refresh inventory doc | `docs/ai-agents-inventory.md` regenerated, committed |
| 3     | Scaffold target repo  | `--init <dir>` exit 0, files created                 |
| 4     | Verify resolution     | `--verify <dir>` exit 0, RESULT: OK                  |

## Verification Checklist

- [ ] `MSYS_NO_PATHCONV=1 python scripts/repo-init.py --list-agents` shows Hermes, OpenCode, Codex, Copilot, Claude, Cursor, GitHub CLI
- [ ] Inventory doc contains every agent's system prompt + context files
- [ ] `--init <dir>` created AGENTS.md, docs/ai-agents-inventory.md, .github/agents/README.md
- [ ] Second `--init` is a no-op (idempotency confirmed)
- [ ] `--verify <dir>` exits 0 with RESULT: OK
- [ ] markdownlint passes on this prompt and all new `.md` files

## Personas

| Persona       | When to Use                                        |
| ------------- | -------------------------------------------------- |
| **Developer** | Running the init on a repo, verifying output       |
| **Reviewer**  | Checking idempotency, no-secrets, and completeness |

## Personality

- **Tone**: Direct, practical
- **Style**: Structured phases with explicit gates
- **Avoid**: Guessing agent paths — probe the filesystem
- **Encourage**: Verification before claiming completion

## Workflow

1. **Diagnose** — Run `--list-agents`; record current agent landscape.
2. **Plan** — Determine target repo and whether `--force` is warranted.
3. **Fix** — Run `--init`; idempotent by default.
4. **Verify** — Run `--verify`; confirm exit 0.
5. **Document** — Regenerate inventory doc; note any path drift.

## Best Practices

1. **Runtime detection** — never assume agent paths; probe every run.
2. **Idempotency** — preserve existing agent files (e.g., real `.github/agents/*.agent.md`).
3. **Verification gates** — verify before claiming completion.
4. **Minimal changes** — only scaffold what is missing.

## Dependencies

- Python 3.10+ on PATH
- `scripts/repo-init.py` present in the workspace

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| Server                | Purpose                                             |
| --------------------- | --------------------------------------------------- |
| `filesystem`          | File read/write operations                          |
| `github`              | GitHub API operations (agent inventory cross-check) |
| `sequential-thinking` | Structured reasoning for complex problems           |
| `ast-grep`            | AST-based code search and replace                   |
| `fetch`               | Web page content extraction                         |
| `playwright`          | Browser automation for interactive pages            |
| `tavily`              | Web search + URL extraction                         |

## Hooks

The following workspace hooks run around this prompt's execution (see `.github/hooks/README.md`):

| Hook                     | When              | Behavior                     |
| ------------------------ | ----------------- | ---------------------------- |
| `session-logger`         | session start/end | Logs session metadata        |
| `governance-audit`       | session events    | Audits governance compliance |
| `session-auto-commit`    | session end       | Auto-commits session state   |
| `pre-exec-validate.sh`   | before commands   | Validates command execution  |
| `post-exec-state-log.py` | after commands    | Appends state log            |

## Scripts

- `scripts/repo-init.py` — Agent inventory + scaffold + verify (this prompt's engine)
- `docs/ai-agents-inventory.md` — Regenerated inventory doc output
- `.github/hooks/*` — Hook implementations listed in the Hooks section

## Subgoals

1. **Prepare** — Confirm script exists and Python works.
2. **Execute** — Inventory → refresh doc → scaffold → verify.
3. **Verify** — All gates pass; idempotency confirmed.
4. **Document** — Inventory doc committed with "as of" date.

## Related Prompts

Same-family prompts:

- [`repo-management.prompt.md`](repo-management.prompt.md)
- [`repo-research-pipeline.prompt.md`](repo-research-pipeline.prompt.md)
- [`repo-story-time.prompt.md`](repo-story-time.prompt.md)
- [`repo-tooling-implementation.prompt.md`](repo-tooling-implementation.prompt.md)
- [`repo.prompt.md`](repo.prompt.md)