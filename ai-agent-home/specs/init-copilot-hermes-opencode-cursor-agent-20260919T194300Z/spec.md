# Cross-Agent Initialization Specification

**Status:** COMPLETE  
**Run:** `init-copilot-hermes-opencode-cursor-agent-20260919T194300Z`

## Objective

Align GitHub Copilot, Hermes, OpenCode, Cursor Agent, Claude, and all autonomous project context adapters around the repository's canonical `AGENTS.md` contract. Add a repeatable clarification-first workflow and durable timestamped spec/plan/prompt artifacts.

## Confirmed Decisions

- Ask all required, optional, recommended, blocker, and approval questions before verification or implementation; ask three questions per turn.
- Update all discovered root and project-level adapters.
- Defer on missing prerequisites and record exact blockers without fabricating state.
- Proceed on reversible changes; pause for destructive, secret/profile, broad-delete, or materially ambiguous actions.
- Use UTC run names: `<kebab-name>-YYYYMMDDTHHMMSSZ`.
- Mark artifacts complete only after implementation and all selected gates pass.

## Acceptance Criteria

- Every autonomous project has a usable Copilot adapter or explicit documented delegation.
- No project Copilot adapter references nonexistent `../../$HERMES_HOME.md`.
- Canonical root contract remains in `AGENTS.md`; adapters stay thin.
- Current run contains spec, plan, and prompt artifacts with final status and evidence.
- Structural, reference, markdown, diff, and relevant project-local checks pass.

## Non-Goals

- Do not invent an OpenCode configuration schema.
- Do not modify protected secrets or external Hermes profile state.
- Do not revert unrelated project worktree modifications.

## Completion Evidence

- 48 changed root/project adapter and run-artifact Markdown files passed markdownlint.
- `git diff --check` passed.
- 87 project context files were audited; root project adapters delegate to `AGENTS.md` and no stale `$HERMES_HOME.md` references remain.
- 99 context/artifact files passed local relative-link validation.
- Required root adapters and all current-run artifacts exist.
- Broader recursive lint remains blocked by 11 pre-existing issues in untouched Banking Cursor rules, Bash docs guidance, and a Django Cursor stub; those files were not changed.
