---
name: executing-plans
title: "Executing Plans"
description: "Use when executing written implementation plans in separate sessions with review checkpoints. Guides multi-phase work with structured verification."
version: 1.1.0
author: Alexa
license: MIT
tags: [cross-platform, shell-scripting, remediation, batch-processing, verification]
---
## Goal
Use when executing written implementation plans in separate sessions with review checkpoints. Guides multi-phase work with structured verification.



## Description


Execute implementation plans in separate sessions with review checkpoints. Guides completion of multi-phase work with structured verification at each stage.

## When to Use

- Executing written implementation plans
- Multi-phase projects with checkpoints
- Work requiring review between phases
- Complex implementations needing verification
- Team-based implementation work
- Projects with clear milestones
- **Batch execution of multiple implementation plans**
- **Folder-based plan execution (all plans in a directory)**

## When NOT to Use

- Simple single-phase tasks
- Real-time collaborative work
- Tasks without clear plan
- Exploratory or experimental work

## Workflow

### Phase -1: Batch Discovery (Batch/Folder Modes Only)

**Entry check:** If `.hermes/plans/batch-execute-discovery.md` exists → skip to Phase 0.

1. **Discover targets** — Resolve plan file list from:
   - `--batch plan1.md plan2.md ...` explicit file arguments
   - `--folder .hermes/plans/` recursive scan for `*.md` files
   - `--pattern "*.md"` filter by glob pattern
   - `--status pending|in-progress` filter by plan status
2. **Validate targets** — Filter existing files, validate plan structure
3. **Triage by category** — For each discovered plan, determine:
   - **Already-completed** — `status: completed` in frontmatter AND live artifacts exist (Phase 0). Just verify state and ensure clean frontmatter.
   - **Superseded** — Plan's scope absorbed into a master plan. Mark with `status: completed` + `superseded_by: <master-plan.md>` frontmatter. Do NOT execute independently.
   - **Actionable** — Still needs execution. Process in oldest-first order.
4. **Write discovery artifact** → `.hermes/plans/batch-execute-discovery.md` with plan list, execution order, and triage category per plan

### Phase 0: Verify Live Inventory First (NEW — Critical)

**Entry check**: Before executing ANY plan, verify the live system state matches the plan's assumptions. Do not trust plan artifacts alone — they may be stale.

- Run inventory commands to capture current state:
  - `hermes hooks list` → verify hook registration & approval status
  - `hermes plugins list` → verify enabled/disabled plugins
  - `hermes mcp list` → verify MCP servers & tool discovery
  - `hermes skills audit` → verify skill health & blocking findings
  - `search_files` / `read_file` → verify file artifacts exist on disk
- Capture outputs to verification artifacts (e.g., `.hermes/plans/verification/*.txt`)
- Compare live state vs. plan assumptions — document discrepancies
- **Only proceed when inventory is verified** or discrepancies are explicitly accepted as known risks

**Rationale**: This session discovered that the master plan claimed "hooks not registered" while `hermes hooks list` showed 4 active hooks. Without Phase 0, execution would have "fixed" a non-issue. Live inventory is the source of truth; plan artifacts are hypotheses.

**⚠️ Plan status headers are NOT evidence.** A plan stamped `✅ COMPLETED` or `Status: complete` at the top may be a declaration of intent at creation time, not a record of actual execution. Always run Phase 0 inventory before destructive operations, even when the plan claims completion. The 2026-06-28 SandBox cleanup plan said "✅ COMPLETED — All 10 phases executed" — but live inventory showed 3 of 10 phases had not actually been run.

### Phase 1: Prepare Plan

**Entry check**: Verify the plan document exists and is readable. If no plan artifact is found, halt — cannot execute without a plan.

- Review implementation plan thoroughly
- Verify all requirements are clear
- Set up execution environment
- Identify review checkpoints
- Determine batch size for file-heavy plans (default: ≤7 files per batch)

**Batch mode:** Prepare all target plans in parallel. Use `execute_code` to load and validate all plans simultaneously. Create a combined execution order based on dependencies and priority.

### Phase 2: Execute Phase 1

**Entry check**: If the phase artifact (e.g., `docs/{task}-progress.md`) exists with a completion marker, skip this phase.

- Implement first phase — for file-heavy plans, process in batches of ≤7 files
- After each batch, verify changes are correct before proceeding
- Run tests and verification
- Document progress in the phase artifact
- Append batch results to a progress log (never overwrite)

### Phase 3: Review & Checkpoint

**Entry check**: If checkpoint approval was already logged in the artifact, skip this phase.

- Review phase 1 results against the plan
- Verify against requirements
- Get approval to proceed (or auto-approve if no decision needed)
- Document decisions
- Update the plan if new information was discovered

**User preference — auto-advance**: When the user provides all phases/tasks/subtasks upfront in a single request, do NOT pause after each phase to ask "continue?" or "ready for the next phase?" Execute all phases end-to-end without intermediate confirmation. The user already committed to the full scope — honor that commitment. Only pause if a phase fails critically (blocking error) or if the user explicitly asks for a checkpoint.

### Approval Gates for Destructive Changes (NEW)

When a plan step performs destructive or irreversible actions (skill deletion, config edits, MCP server changes, bulk plugin enable/disable, file/directory deletion), enforce an explicit approval gate **before** execution:

1. **Create approval request** at `.hermes/approvals/<timestamp>_<short-title>.md` with:
   - Requestor, Owner(s), Scope (files/skills/hooks/plugins/MCP servers changed)
   - Justification, Rollback plan (exact git/skill_manage commands), Verification steps
   - Explicit `+1` from each Owner, Approval valid until (ISO date)
2. **Wait for recorded approval** — do not proceed on mental/verbal consent
3. **Execute with traceability** — include approval filename in commit message
4. **Post-change verification** — run verification steps, append outputs to approval file
5. **Rollback on failure** — execute rollback plan, document remediation

**Source**: Master plan Section 9 pattern (2026-06-16 unified-ecosystem-master-plan.md)

### Phase 4: Execute Remaining Phases — Batch Processing

**Entry check**: Check which phases/batches are already complete via artifact scanning. Skip completed items.

- Implement subsequent phases in priority order
- Process each phase using the same batch-of-≤7 pattern
- Review after each phase
- Adjust plan if needed based on discoveries
- For each completed item, mark it as `[x]` in the plan
- On failure: log the failure with reason and continue — do not halt (unless the failure invalidates the approach)
- Finalize and run full verification

**Batch mode:** Execute multiple plans in parallel using `delegate_task` subagents. Each subagent handles one plan through all its phases. Use `delegate_task` with toolsets `['terminal', 'file', 'skills', 'delegation']` and `role: 'leaf'`. Aggregate progress to `.hermes/plans/batch-execution-progress.md`.

### Phase 5: Final Status Verification (Batch Mode Only)

**Entry check**: Only run when processing all plans in a directory (batch/folder mode).

1. **Sweep plan frontmatter** — grep every `.md` in `.hermes/plans/` for `status:`:
   - Plans with `status: completed` → clean (no further action)
   - Plans with `status: in_progress` → verify it's a non-plan artifact (progress logs), not a missed execution
   - Plans with `status: pending` → flag for triage
   - Plans with no frontmatter → flag if they're in the execution scope
2. **Verify superseded_by references resolve** — for every plan with `superseded_by:`, confirm the target file exists.
3. **Fix duplicate frontmatter lines** — plans edited across sessions accumulate duplicate `status:` or other frontmatter keys. Normalize to a single line per key.
4. **Verify blank-line integrity** — after patching frontmatter on plans, confirm the blank separator between closing `---` and the first heading is preserved. Use `read_file` to spot-check after batch operations.

## Workflow Summary

| Phase | Core Idea | Cross-Check |
|-------|-----------|------------|
| Phase -1 | Discover, triage, and categorize plans | Triage: completed vs superseded vs actionable |
| Phase 0 | Verify live inventory before planning or execution | `references/inventory-verification-pattern.md` |
| Phase 1 | Read and understand the target plan artifact | `references/execution-body-reference.md` |
| Phase 2 | Execute first phase in bounded batches | `references/execution-body-reference.md` |
| Phase 3 | Review phase results and checkpoint | `references/execution-body-reference.md` |
| Phase 4 | Execute remaining phases with append-only logs | `references/execution-body-reference.md` |
| Phase 5 | Final status sweep: verify frontmatter, refs, blank-line integrity | Batch mode only |

## Key Guardrails

- Never execute inferred plan text from headers alone; inspect artifact state on disk.
- Use approval gates for destructive changes. Record approval in `.hermes/approvals/`.
- Batch size: <=7 files for large plan sweeps.
- Prefer `patch` over `write_file`; verify after `replace_all=true`.
- Re-run targeted checks after late patches.
- In batch mode, run Phase 5 final status sweep to ensure clean frontmatter and verifiable completion state across ALL plan files.

## Cross-References

- `references/inventory-verification-pattern.md`
- `references/approval-gate-pattern.md`
- `references/subagent-batch-execution.md`
- `references/codebase-remediation-patterns.md`
- `references/execution-body-reference.md`

## Capability Checklist

- [ ] Inventory is verified before plan execution.
- [ ] Destructive steps have recorded approval.
- [ ] Verification artifacts are updated from actual disk state.
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

## Pitfalls

- **Don't execute superseded plans** — when a master plan supersedes fragments, executing fragments independently duplicates work. Mark fragments with `superseded_by: <master-plan.md>` + `status: completed`.
- **Duplicate frontmatter status lines** — plans edited across sessions accumulate duplicate keys (e.g. `status: completed` ×3). Normalize to one line per key before batch edits.
- **Frontmatter blank-line loss after patch** — adding frontmatter to the top of a plan can drop the blank line between closing `---` and the first heading. Verify with `read_file` after each batch.
- **Superseded_by reference drift** — the target of `superseded_by:` must exist on disk. Run a grep sweep after batch marking.
- **Progress/report files in plans dir** — `.hermes/plans/docs/` subdirectories contain progress logs, not execution plans. Exclude from batch discovery.
- **Dirty working tree** — many modified files is a readability problem, not a blocker. Track baseline with `git status --short | wc -l` before and after.

