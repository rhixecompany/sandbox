# Execute All Prompts — Phases

> Full operational phases for `prompts/execute-all-prompts.prompt.md`.

## Phase 1: Audit Skills Judge Fix

- Execute `audit-skills-judge-fix.prompt.md`.
- Gate: final verification report shows zero unresolved issues.

## Phase 2: Agents System Prompt Context Fix

- Execute `agents-system-prompt-context-fix.prompt.md`.
- Gate: context docs are generated for root and each subproject; VS Code configs are triaged/verified.

## Phase 3: Sync Hermes Copilot Codex

- Execute `sync-hermes-copilot-codex.prompt.md`.
- Gate: sync report written; conflicts resolved or documented; verification report complete.

## Phase 4: Test Providers & Models

- Execute `test-providers-models.prompt.md`.
- Gate: comparison/report artifacts exist and fallback notes are documented.

## Completion

- Append progress after each phase.
- Append evidence to `docs/orchestrator-verification.md` after each phase.
- If any phase is blocked by a missing file/path, stop and report the exact blocker instead of fabricating work.
