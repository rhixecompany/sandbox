---
trigger: /execute-batch-prompts
description: >
  Batch execute all 5 workspace .prompt.md files using executing-plans skill.
  Each prompt runs to completion with "only then" sequential constraints.
tags: [orchestrator, batch, sequential, executing-plans]
skills:
  - using-superpowers
  - user-communication-preferences
  - executing-plans
  - plans-and-specs
  - verification-before-completion
---

# Execute All Prompts — Batch Orchestrator

> Sequentially execute all 5 `.prompt.md` files. Each completes (with verification) before the next begins.

## Required Skills
- `/executing-plans` — batch execution framework
- `/verification-before-completion` — checkpoint verification
- All 13 judged skills verified ≥ 80 ✓

## Target Files (in order)

| # | Prompt File | Phases | Est. Time |
|---|-------------|--------|-----------|
| 1 | `audit-skills-judge-fix.prompt.md` | 7 phases | 30-45 min |
| 2 | `agents-system-prompt-context-fix.prompt.md` | 3 phases | 20-30 min |
| 3 | `sync-hermes-copilot-codex.prompt.md` | 4 phases | 15-20 min |
| 4 | `test-providers-models.prompt.md` | 6 phases | 30-45 min |
| 5 | `execute-all-prompts.prompt.md` | 4 meta-phases | Reference only |

## Execution Rules

1. **Strict sequential** — Each prompt fully completes before next begins
2. **Verification gates** — Each prompt's verification checklist must pass
3. **Progress tracking** — Append to `docs/orchestrator-progress.md`
4. **No reordering** — Execute in the exact order listed
5. **Skills already verified** — All 13 referenced skills scored ≥ 80

## ⛔ "Only Then" Constraint

Prompt N+1 starts ONLY after Prompt N's verification checklist is 100% complete.

## Actions Summary

1. Load `/executing-plans` → Phase 0: discover targets
2. Execute Prompt 1 (audit-skills-judge-fix) all 7 phases → verify
3. Execute Prompt 2 (agents-system-prompt-context-fix) all 3 phases → verify
4. Execute Prompt 3 (sync-hermes-copilot-codex) all 4 phases → verify
5. Execute Prompt 4 (test-providers-models) all 6 phases → verify
6. Execute Prompt 5 (execute-all-prompts) meta phases → verify
7. Update SESSION_REPORT.md with results
