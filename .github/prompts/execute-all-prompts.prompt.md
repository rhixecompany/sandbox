---
name: execute-all-prompts
title: "Execute All Prompts Orchestrator"
description: 'Orchestrates sequential execution of 4 workspace prompt workflows: audit-skills-judge-fix,
  agents-system-prompt-context-fix, sync-hermes-copilot-codex, and test-providers-models.
  Each prompt runs to completion before the next begins.'
version: 1.0.0
license: MIT
author: Hermes Agent
tags:
- audit
- execution
- fix
- prompts
- workflow
trigger: /execute-all-prompts
formatter: default
dependencies:
- skill:using-superpowers
- skill:user-communication-preferences
- skill:verification-before-completion
- skill:subagent-driven-development
metadata:
  hermes:
    related_skills:
    - using-superpowers
    - user-communication-preferences
    - verification-before-completion
    - subagent-driven-development
toolsets:
- file
- terminal
scripts: []
skills: []
plan: ''
---

# Execute All Prompts Orchestrator

> Strict sequential execution. Phase N+1 begins only after Phase N is fully verified complete.

## Context

- **Workspace root:** `C:\Users\Alexa\Desktop\SandBox`
- **Hermes prompts root:** `C:\Users\Alexa\AppData\Local\hermes\prompts`
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`

## Execution Rule

- This workflow is intended to be run through the available Hermes task interface.
- If a dedicated `hermes prompt run ...` command is unavailable, execute this workflow by processing the referenced prompt files in sequence, preserving strict ordering and phase gates.
- Only advance after the current phase passes its gate.

## Rules

1. Execute prompts in order. Do not reorder.
2. Each prompt must pass its own verification before advancing.
3. All Python scripts/outputs go under the Hermes scripts path unless the prompt states otherwise.
4. Append progress after each phase; append evidence to verification after each phase.
5. If a prompt file is missing, pause and report the exact missing path instead of fabricating work.

## Phase Contents

Full phase instructions live in `templates/execute-all-prompts/phases.md`.

| Order | Phase | Prompt File |
|------|-------|-----------|
| 1 | Audit Skills Judge Fix | `audit-skills-judge-fix.prompt.md` |
| 2 | Agents System Prompt Context Fix | `agents-system-prompt-context-fix.prompt.md` |
| 3 | Sync Hermes Copilot Codex | `sync-hermes-copilot-codex.prompt.md` |
| 4 | Test Providers & Models | `test-providers-models.prompt.md` |

## Verification Checklist (Orchestrator Level)

- [ ] Phase 1 completed and verified
- [ ] Phase 2 completed and verified
- [ ] Phase 3 completed and verified
- [ ] Phase 4 completed and verified
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`
