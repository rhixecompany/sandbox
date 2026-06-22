---
trigger: /execute-all-prompts
description: >
  Orchestrates sequential execution of all 4 workspace prompt files:
  audit-skills-judge-fix, agents-system-prompt-context-fix,
  sync-hermes-copilot-codex, and test-providers-models.
  Each prompt runs to completion before the next begins.
tags:
  - orchestrator
  - pipeline
  - sequential
  - audit
  - sync
  - benchmark
  - context
dependencies:
  - using-superpowers
  - user-communication-preferences
  - plans-and-specs
  - executing-plans
  - verification-before-completion
skills:
  - using-superpowers
  - user-communication-preferences
  - plans-and-specs
  - executing-plans
  - verification-before-completion
metadata:
  hermes:
    related_skills:
      - using-superpowers
      - user-communication-preferences
      - plans-and-specs
      - executing-plans
      - verification-before-completion
---

# Execute All Prompts Orchestrator

> Sequentially executes all 4 workspace prompt files. Each prompt must complete fully before the next begins ("only then" constraint).

## Description

This orchestrator runs 4 prompt files in order, each as a self-contained workflow. Execution is strictly sequential — Phase N+1 begins only after Phase N is fully verified complete.

**Critical rules:**
- Execute prompts in the exact order listed below
- Each prompt must be fully verified before moving to the next
- Do not skip phases within any prompt
- All Python scripts go to `~/AppData/Local/hermes/scripts/`
- Track progress in `docs/orchestrator-progress.md`

## Context

- **Workspace root:** `C:\Users\Alexa\Desktop\SandBox`
- **Prompt files:** 4 files in workspace root
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`

## Skills Required

| Skill | Purpose |
|-------|---------|
| `using-superpowers` | Workflow foundation, session startup |
| `user-communication-preferences` | Execution style and preferences |
| `plans-and-specs` | Phase planning and progress tracking |
| `executing-plans` | Execute written plans with checkpoints |
| `verification-before-completion` | Verify each phase before claiming done |

## Rules

1. **Strict sequential execution** — Prompts execute in order; each must complete before the next begins
2. **Phase integrity** — All phases within a prompt must complete; do not skip
3. **Verification gates** — Each prompt's verification checklist must pass before proceeding
4. **Progress tracking** — Append progress to `docs/orchestrator-progress.md` after each prompt
5. **No reordering** — The prompt order is fixed; do not reorder based on perceived priority

## Phases

> ### Phase 1: Audit Skills Judge Fix
> **Prompt file:** `audit-skills-judge-fix.prompt.md`

> **Full content:** `templates/execute-all-prompts/phases.md`

## Actions Summary

1. Run skills audit → categorize → dedupe → judge → remediate → consolidate → verify
2. Generate agent context files → audit VS Code configs → verify
3. Inventory instructions/agents → identify roots → sync assets → verify
4. Inventory providers → discover models → extract free → benchmark → report

## Verification Checklist (Orchestrator Level)

- [ ] Phase 1: Audit Skills Judge Fix — all 7 sub-phases complete
- [ ] Phase 2: Agents System Prompt Context Fix — all 3 sub-phases complete
- [ ] Phase 3: Sync Hermes Copilot Codex — all 4 sub-phases complete
- [ ] Phase 4: Test Providers & Models — all 6 sub-phases complete
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`

## Pitfalls

- **Skipping phases:** Never skip sub-phases within a prompt; each builds on the previous
- **Stale artifacts:** Re-read prompt files from disk before executing; don't rely on cached context
- **Context limits:** Each prompt is a large workflow; process in batches and write progress artifacts
- **Credential constraints:** API keys (especially OPENROUTER_API_KEY) are in Hermes' secure store, not env vars; route through `hermes chat -q --provider`
- **Sequential constraint:** The "only then" rule is absolute — never start a prompt before the previous one is verified complete


## Template References

Detailed templates in `templates/execute-all-prompts/`:
- `phases.md`
