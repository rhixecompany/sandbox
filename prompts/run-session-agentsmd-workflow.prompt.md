---
description: "Execution prompt for AGENTS.md generation, per-repo git operations, branch reconciliation, and final repo-branch-SHA reporting"
agent: "agent"
---

## Goal
Use when "Execution prompt for AGENTS.md generation, per-repo git operations, branch reconciliation, and final repo-branch-SHA reporting" to accomplish the associated tasks and objectives.


## Description

Execute the full AGENTS.md workflow using one argument.

Supported argument values:

- A single target directory name, for example: Bash or Resume_maker.
- projects-all, meaning process every direct child directory under projects/.

## Context

Use this prompt when the user wants the workflow executed, not just designed.

This prompt executes the implementation pattern defined in:

- .github/prompts/session-agentsmd-full-workflow.prompt.md

Argument contract:

- If no argument is provided, default to projects-all.
- If an argument does not resolve to an existing target directory, fail fast and report valid options.

## Skills Required

- Workspace discovery and path resolution.
- AGENTS.md authoring from local evidence.
- Nested git repository handling.
- Robust push/retry logic and fallback branch publishing.
- Compact verification reporting.

## Subagents

- Explore: optional for large repository context discovery.
- reviewer: optional for final output consistency checks.

Subagents are optional and should only be used when they improve speed or reliability.

## Personas

- Role: Automation Executor.
- Objective: complete the requested workflow end-to-end in one run.
- Style: deterministic, explicit, and minimal-risk.

## Rules

- Execute all phases unless genuinely blocked.
- Resolve targets only from the provided argument and existing workspace paths.
- For AGENTS.md generation:
  - use local manifest and README evidence.
  - include practical setup, workflow, testing, style, security, and troubleshooting sections.
- For git operations:
  - stage only AGENTS.md.
  - commit message must be: docs: add or update AGENTS.md for agent guidance.
  - push to normalized PR branch names:
    - chore/agentsmd-YYYYMMDD-<repo>
- If hooks fail due missing dependencies, retry commit with no-verify and record this.
- If push fails because of remote divergence or oversized local history, use a clean-clone fallback and publish the branch.
- Never force-push.
- Always output a compact final table with:
  - repo | branch | commit SHA | status.
- Include explicit blocker notes for any failed repo.

## Phases

> ### Phase 1: Resolve Scope
> ### Phase 2: Generate AGENTS

> **Full content:** `templates/run-session-agentsmd-workflow/phases.md`

## Steps

1. Parse argument and resolve targets.
2. Discover evidence files for each target.
3. Generate or update AGENTS.md per target.
4. Validate and fix markdown diagnostics if any.
5. Stage only AGENTS.md in each target repo.
6. Commit using the required message.
7. Push to normalized branch naming pattern.
8. Apply fallback publish path for failed pushes.
9. Verify remote branch SHA for each target.
10. Return compact final table and blockers.

## Tasks

- Task 1.1 — Parse and validate workflow argument.
- Task 1.2 — Resolve target directories.
- Task 2.1 — Generate AGENTS.md content per target.
- Task 2.2 — Validate diagnostics for changed prompt/docs files.
- Task 3.1 — Stage and commit AGENTS.md per repository.
- Task 3.2 — Push PR-ready branch per repository.
- Task 4.1 — Verify remote branch and SHA mapping.
- Task 4.2 — Output final compact summary table.

## Subtasks

- Subtask 1.1.1 — Apply default argument projects-all when omitted.
- Subtask 1.1.2 — Fail fast on invalid target names.
- Subtask 1.2.1 — Expand projects-all to direct child directories of projects/.
- Subtask 2.1.1 — Use manifest-driven command discovery where possible.
- Subtask 2.1.2 — Preserve useful existing AGENTS.md context when updating.
- Subtask 2.2.1 — Run diagnostics and fix markdown issues introduced by edits.
- Subtask 3.1.1 — Commit only AGENTS.md to avoid unrelated changes.
- Subtask 3.1.2 — Retry with no-verify if hooks fail due unavailable local tooling.
- Subtask 3.2.1 — Publish branch chore/agentsmd-YYYYMMDD-<repo>.
- Subtask 3.2.2 — Use clean clone fallback for history-size or divergence failures.
- Subtask 4.1.1 — Confirm remote refs exist for every target repo branch.
- Subtask 4.2.1 — Include repo, branch, commit SHA, and status in final output.

## Actions Summary

- Run the AGENTS workflow from one argument.
- Generate/update AGENTS.md per target.
- Commit and push per target repo.
- Reconcile branch naming for PR readiness.
- Return compact repo-branch-SHA-status report.


## Template References

Detailed templates in `templates/run-session-agentsmd-workflow/`:
- `phases.md`
