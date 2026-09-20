---
name: init-cross-agent-context
version: 1.0.0
status: complete
run: init-copilot-hermes-opencode-cursor-agent-20260919T194300Z
---

# Cross-Agent Context Initialization

## Clarification Gate

Before verification or implementation, ask exactly three focused questions per turn until all material decisions are answered. Cover:

- changes between the old and new request;
- scope and out-of-scope surfaces;
- remaining work;
- blockers and missing inputs;
- required, optional, and recommended behavior;
- approval gates and irreversible actions.

If the user cannot answer, apply the documented recommended defaults and record the assumption.

## Execution Contract

1. Read the nearest `AGENTS.md`, tool adapter, project manifest, and relevant tests.
2. Use `AGENTS.md` as the canonical shared contract.
3. Keep Copilot, Hermes, Cursor, Claude, and OpenCode adapters thin.
4. Treat each `projects/*` directory as autonomous.
5. Create/update the current run's spec, plan, and prompt before and during implementation.
6. Do not read or modify protected secrets or unrelated worktree changes.
7. Run all selected validation gates.
8. Mark all current-run artifacts `complete` only after scoped validation passes; record unrelated pre-existing validation failures as blockers with exact evidence.

## Deliverable

Align root and project-level agent context files, preserve project-specific commands, eliminate stale canonical paths, and leave a durable completion record.

## Completion Evidence

The current run completed with 48 changed adapter/artifact files linted successfully, diff/structure/reference checks passing, and 11 unrelated pre-existing recursive-lint findings recorded without modifying their files.
