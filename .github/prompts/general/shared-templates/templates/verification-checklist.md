---
name: shared-verification-checklist
title: Shared Verification Checklist
description: Standard verification gates for prompt-driven workflows. Copy the relevant section into your prompt's "Verification" section.
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [shared, verification, gates, prompts]
---
## Goal

<!-- Shared template — see file body for goal content -->

## Context

<!-- Shared template — see file body for context content -->

## Workflow

<!-- Shared template — see file body for workflow content -->

## Verification

<!-- Shared template — see file body for verification content -->


# Shared Verification Checklist

## Usage

Copy the verification block that matches your task type into your prompt's "Verification" or "Acceptance Criteria" section. Always include concrete commands the agent can run to prove success.

## Common gates (apply to all tasks)

- [ ] All named acceptance criteria are verified
- [ ] No new errors or warnings introduced
- [ ] Existing tests still pass (`bun run check` or equivalent)
- [ ] Output matches the requested format
- [ ] State changes verified by reading back the target (not by trusting the tool call)

## Code-implementation gates

- [ ] Tests written and pass (`bun test` / `pytest`)
- [ ] Linter clean (`bun run lint` / `ruff check`)
- [ ] Type checker clean (`bun run typecheck` / `pyright`)
- [ ] Formatter applied (`bun run format` / `ruff format`)
- [ ] No new dependencies added without approval

## Documentation gates

- [ ] Markdown lint clean (`bun run markdownlint`)
- [ ] Spell check clean (`bun run spellcheck` or `cspell`)
- [ ] No AI puffery (per `writing-clearly-and-concisely`)
- [ ] Active voice throughout
- [ ] All file references resolve to actual paths

## Plan/spec gates

- [ ] Plan name, phases, tasks clearly defined
- [ ] Each task has linked spec with acceptance criteria
- [ ] Dependencies documented
- [ ] Verification commands runnable
- [ ] Plan < 250 lines (split if larger)

## Diagnostic/repair gates

- [ ] `hermes doctor` exits 0
- [ ] `bun run check` clean
- [ ] All repair steps verified by re-running the diagnostic
- [ ] Rollback command documented
- [ ] No destructive ops without recorded approval

## Multi-file-change gates (≥5 files modified)

- [ ] 14-skill bundle loaded at session start
- [ ] Plan written to `.hermes/plans/`
- [ ] Plan verified before execution
- [ ] Execution via `/executing-plans` or `/subagent-driven-development`
- [ ] All gates pass before claiming completion
- [ ] SESSION_REPORT.md updated

## MCP server gates

- [ ] `hermes mcp list` shows all expected servers enabled
- [ ] `hermes mcp test <server>` passes for each
- [ ] Disk configs (`opencode.json`, `codex/mcp.json`, etc.) synced
- [ ] At least 1 live call per server confirmed (not just config-valid)

## Git/commit gates

- [ ] `git status` shows only expected changes
- [ ] Commit message follows `type: description` convention
- [ ] No secrets in diff (`git diff --stat` review)
- [ ] No backup files (`.bak`, `.old`, `.tmp`)
- [ ] Branch hygiene (no accidental commits to main)

## References

- `../_index.md` — templates index