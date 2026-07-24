# Agents System Prompt Context Fix — Phases

> Full operational phases for `prompts/agents-system-prompt-context-fix.prompt.md`.

## Phase 1: Generate Agent Context Files

- Generate context documentation for the repo root and each subproject.
- Gate: context docs generated for root and each subproject.

## Phase 2: Audit VS Code Configuration

- Audit all VS Code JSON configs in the workspace.
- Gate: all VS Code JSON configs triaged and verified.

## Phase 3: Verify & Implement

- Review generated artifacts and close remaining issues.
- Gate: verification report written and issues closed.

## Completion

- Append progress after each phase.
- Append evidence to `docs/orchestrator-verification.md` after each phase.
