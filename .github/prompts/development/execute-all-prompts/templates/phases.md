# Execute All Prompts — Phase Instructions

> Extracted from `execute-all-prompts.prompt.md`. Strict sequential execution; Phase N+1 begins only after Phase N is fully verified.

## Phase 1 — Audit Skills Judge Fix

- **Prompt file**: `audit-skills-judge-fix.prompt.md`
- **Work**: Inventory skills, run skill-judge audit, fix failing sections, re-audit to zero.
- **Gate**: audit report shows WITH_ISSUES=0 (or documented accepted exceptions).

## Phase 2 — Agents System Prompt Context Fix

- **Prompt file**: `agents-system-prompt-context-fix.prompt.md`
- **Work**: Repair/align agent system-prompt context files (Hermes + OpenCode).
- **Gate**: verification pass confirms all referenced context files exist and are valid.

## Phase 3 — Sync Hermes OpenCode

- **Prompt file**: `sync-hermes-opencode.prompt.md`
- **Work**: Bidirectional sync of skills, plugins, hooks, prompts, agents, instructions across Hermes/Codex/OpenCode with verification.
- **Gate**: sync report written; all critical assets in sync; conflicts resolved or documented.

## Phase 4 — Test Providers & Models

- **Prompt file**: `test-providers-models.prompt.md`
- **Work**: Inventory authorized providers, test model availability/response quality.
- **Gate**: provider/model report written with live test results.

## Progress & Verification Artifacts

- **Progress**: `docs/orchestrator-progress.md` — append after each phase.
- **Verification**: `docs/orchestrator-verification.md` — append evidence after each phase.

---

> TODO-to-author: update phase list when the orchestrator set changes.
