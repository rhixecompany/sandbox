# Cross-Skill Orchestration Pipeline

## Pattern: enhance-markdown → skill-judge → executing-plans

When a user chains `/enhance-markdown --batch` with `/skill-judge --batch` and `/executing-plans --batch`, the following reusable pipeline applies:

## Pipeline Steps

### Step 1: Discover Targets (enhance-markdown Phase 0)
Use `/enhance-markdown --glob "*.prompt.md"` or `--batch` to discover all target files.
Write batch context with file list and resolved purposes.

### Step 2: Extract Referenced Skills
From each target file, extract the `skills:` frontmatter field and/or `Skills Required` table.
Deduplicate across all files.
Write to batch context for the judge step.

### Step 3: Judge Skills (skill-judge Phase 1-2)
Run `/skill-judge --batch <skill1> <skill2> ...` in batches of 7.
For each skill, evaluate on 5 dimensions (Frontmatter, Structure, Content, DRY, References).
Write per-batch results to `judge_results/batch_N_results.md`.

### Step 4: Fix Below-Threshold Skills
Any skill scoring below 80 needs remediation before execution proceeds:
- Missing frontmatter → add `version`, `author`, `license`, `tags`
- Broken YAML artifacts (stray `---metadata:` in body) → remove
- Missing Skills Required table → add with cross-references
- Re-judge after fix to confirm score ≥ 80

### Step 5: Check Plan Requirements
Verify each target prompt file has a built-in plan (phases, tasks, verification).
If any prompt lacks a plan, create one via `/create-implementation-plan`.
If any prompt has a plan but needs updating, use `/update-implementation-plan`.

### Step 6: Generate Execution Prompt
Create `.hermes/plans/batch-execute-prompts-plan.md` with:
- Ordered target list
- Sequential "only then" constraints
- Verification gates per phase

### Step 7: Execute Plans (executing-plans Phase 1-4)
Run `/executing-plans --batch` with the execution prompt.
Each prompt completes with verification before the next begins.
Track progress in a shared artifact.

## When to Use This Pipeline
- User chains multiple skill commands with "only then" constraints
- Source files reference skills that need quality validation before execution
- The workflow spans markdown enhancement → skill quality → plan execution
- Multiple independent prompt files need sequential processing

## Pitfalls
- **Judge before fix**: Always judge all skills before fixing any. A single judge pass identifies the full remediation scope.
- **Don't re-judge unfixed skills**: After fixing, only re-judge the skills that were patched.
- **Plan check is separate from skill check**: Prompts may have valid plans even if their referenced skills need work.
- **Batch size discipline**: Judge in batches of 7; fix in batches of 7; execute one prompt at a time.
- **Execution order matters**: The "only then" constraint is absolute — never skip ahead.

## Reference
Discovered in session 2026-06-22: user invoked `/enhance-markdown --batch ./*.prompt.md`, then `/skill-judge --batch` in batches, debug/refactor/verify all skills ≥ 80, then `/executing-plans --batch`.
