# Prompt File Debugging Patterns

Session: 2026-05-29 — debugging and enhancing `Prompts/repo.prompts.md`

## Bug Taxonomy for Structured `.prompts.md` Files

When debugging a multi-phase prompt file, check these categories in order:

### 1. Count/number mismatches
- Summary sections with hard-coded totals that do not match the actual inventory.
- Fix: grep for all literal counts; cross-reference against the canonical source (e.g., an index file, a directory listing).

### 2. Broken Markdown tables (missing closing pipe)
- A table row missing the trailing pipe renders as a paragraph, breaking table display.
- Pattern: `| col1 | col2 | value` with no trailing pipe.
- Fix: scan every table row for balanced pipe count. Each row needs pipes at both ends.

### 3. Skills list vs load-step divergence
- Skills-Required section lists N skills; a phase step that loads skills names only N-2 of them.
- Skills listed but never loaded are dead weight; skills loaded but not listed are undocumented deps.
- Fix: diff the skills-required list against every "load skills" step — they must match exactly.

### 4. Label conflicts in staged code blocks
- Stage labels inside a sequential generator list can collide with later sub-step labels when parsed flat.
- Example: Stage B generator labeled `e:` collides with Stage E sub-steps `e1/e2/e3`.
- Fix: use non-colliding namespaces for final-stage sub-steps (e.g., `s1/s2/s3`).

### 5. Contradictory conditional logic
- Step A says "skip X if condition Y"; Step B runs X unconditionally regardless.
- Fix: rewrite Step B as "only if condition Y is false", making the conditional explicit in both steps.

---

## Pre-Enhancement Workflow for `.prompts.md` Files

Before editing any structured prompt file:

1. Scan the prompts directory for related prompts that should be referenced or integrated.
   - Look for: workflow runners, full-spec companions, orchestrators, optimization passes.
   - Any prompt called by or calling into the target workflow belongs in a Recommended Workflow Prompts table.

2. Check for an authoritative pre-computed inventory file before adding filesystem scan steps.
   - If an index or inventory file exists, make the scan step conditional (skip if index present and non-empty).
   - Unconditional scans that ignore a pre-computed index create contradictory logic (Bug #5 above).

3. Check for missing prerequisite phases.
   - Multi-step workflows often need a setup/refresh phase before the main generators run.
   - If generators depend on evidence files, add a Phase 0 that produces those files and gate Phase 1 on its completion.

4. Verify version footer before saving — bump minor version, update date, add change summary.

---

## Per-Project Generator Context Loading Order

When running a generator for any project, load context in this order before invoking the generator:

1. Load any pre-computed research/inventory report — extract detected stack, project type, findings.
2. Load the project-local setup/guidance file — extract commands, entrypoints, constraints.
3. Feed setup commands to structure and workflow generators.
4. Feed test commands to code-exemplars generators.
5. If the setup/guidance file is missing or stale, re-trigger the file's refresh step for this project only, then continue.
