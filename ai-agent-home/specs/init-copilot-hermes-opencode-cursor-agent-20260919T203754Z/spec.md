# Agent Initialization Specification

**Status:** COMPLETE  
**Run:** `init-copilot-hermes-opencode-cursor-agent-20260919T203754Z`  
**Updated:** 2026-09-19

## Objective

Provide one durable, repository-local operating contract for GitHub Copilot, Hermes, OpenCode, and Cursor Agent. Each tool-specific adapter must defer to the canonical context instead of creating conflicting rulebooks.

## Scope

- `AGENTS.md` is the canonical shared repository context.
- `.github/copilot-instructions.md` is the Copilot adapter.
- `.hermes.md` contains Hermes-only routing and profile overrides.
- `.cursorrules` and `.cursor/rules/sandbox.mdc` provide Cursor Agent adapters.
- OpenCode uses repository `AGENTS.md` discovery; no unsupported OpenCode schema is invented.
- Root `copilot-instructions.md` and `CLAUDE.md` remain thin pointers.
- Every objective maintains a timestamped spec, plan, and prompt under `ai-agent-home/`.

## Behavioral Contract

1. Locate the nearest applicable instructions, manifest, and tests.
2. Understand acceptance criteria and existing patterns.
3. Clarify first when interaction is available, asking at most three focused questions per turn.
4. Cover scope, old/new request differences, remaining tasks, blockers, optional recommendations, and approval gates.
5. Create or update the current run's spec, plan, and prompt before implementation.
6. Implement the smallest complete change while preserving unrelated worktree state.
7. Verify exact behavior with the narrowest relevant checks.
8. Update all run artifacts to `COMPLETE` only after validation.

## Defaults When the User Is Unavailable

- Use the recommended clarification policy.
- Proceed with reversible routine decisions.
- Stop or report blockers for destructive, security-sensitive, or materially ambiguous actions.
- Record the assumption in the current run artifacts.

## Acceptance Criteria

- All four requested agents have a discoverable adapter or documented discovery path.
- Shared rules are centralized in `AGENTS.md`.
- Clarification and artifact lifecycle rules are present in the adapters.
- No protected secret contents are read or changed.
- The current run has complete spec, plan, and prompt artifacts.
- Markdown and stale-reference validation passes.
