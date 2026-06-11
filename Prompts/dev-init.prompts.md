---
title: Dev Init - Prompt Conversion and Enhancement Planning
trigger: /dev-init
description:
    Create a comprehensive plan for converting plaintext prompts to markdown,
    enhancing prompt quality, and updating related implementation plans.
tags: [hermes, copilot, planning, prompts, conversion, enhancement]
dependencies:
    - prompt:.github/prompts/context-map.prompt.md
    - prompt:.github/prompts/convert-plaintext-to-md.prompt.md
    - prompt:.github/prompts/boost-prompt.prompt.md
    - prompt:.github/prompts/ai-prompt-engineering-safety-review.prompt.md
    - prompt:.github/prompts/update-implementation-plan.prompt.md
    - prompt:.github/prompts/prompt-builder.prompt.md
    - skill:brainstorming
    - skill:plans-and-specs
    - skill:writing-skills
    - skill:writing-plans
    - skill:acpx-executor
    - skill:executing-plans
    - skill:simplify
skills:
    - prompt:context-map — Map source, destination, and dependency impact before
      conversion
    - convert-plaintext-to-md — Convert plaintext prompts to markdown
    - boost-prompt — Improve prompt quality and structure
    - ai-prompt-engineering-safety-review — Review prompts for safety and clarity
    - update-implementation-plan — Track the plan that drives the prompt refresh
    - prompt-builder — Scaffold new prompt files
    - brainstorming — Explore conversion and enhancement approaches
    - plans-and-specs — Create detailed specs with file references
    - writing-skills — Craft and optimize prompts and instructions
    - writing-plans — Structure the plan and its sections
    - acpx-executor — Execute a prompt via any ACPX provider
    - executing-plans — Execute written implementation plans in isolated steps
    - simplify — Keep the output concise and non-redundant
---

> Create a detailed prompt-library plan with file references, conversion steps,
> and verification criteria.

## Goal

Plan the prompt-library refresh end to end: convert plaintext prompts to
markdown, improve prompt quality, review safety, and keep the implementation
plan current.

## Context

Use this prompt when a prompt-library refresh needs planning before
implementation. The primary workflow is:

1. `.github/prompts/context-map`
2. `.github/prompts/convert-plaintext-to-md`
3. `.github/prompts/boost-prompt`
4. `.github/prompts/ai-prompt-engineering-safety-review`
5. `.github/prompts/update-implementation-plan`
6. `.github/prompts/prompt-builder`
7. `Prompts/*.md`

Reference artifacts:

- `docs/dev-init-comprehensive-plan.md`
- `docs/dev-init-spec.md`
- `docs/prompts-cross-reference-registry.md`
- `docs/prompt-conversion-enhancement-plan.md`
- `Bash/archive/artifacts/context-maps/dev-init.context.json`

## Inputs

- Source inventory for `Prompts/*.txt`
- Existing `Prompts/*.md` files
- Related `.github/prompts/*.prompt.md` workflows
- Workspace context and implementation constraints

## Outputs

- A conversion and enhancement plan
- A safety and quality review checklist
- File references and integration points
- An implementation guide with verification steps

## Rules

1. Run `context-map` before any conversion or planning work.
2. Keep the pipeline idempotent and safe to re-run.
3. Preserve the original task intent while improving clarity and structure.
4. Keep manual safety notes unless they are wrong.
5. Use git for rollback; do not create backup copies.
6. Update the implementation plan when scope or requirements change.
7. Prefer file-backed evidence over inference.

## Skills Required

| Skill                                 | Purpose                                                          |
| ------------------------------------- | ---------------------------------------------------------------- |
| `context-map` (prompt)                | Map source, destination, and dependency impact before conversion |
| `convert-plaintext-to-md`             | Convert plaintext prompts to markdown                            |
| `boost-prompt`                        | Improve prompt quality and structure                             |
| `ai-prompt-engineering-safety-review` | Review prompts for safety and clarity                            |
| `update-implementation-plan`          | Keep the implementation plan current                             |
| `prompt-builder`                      | Scaffold new prompt files                                        |
| `brainstorming`                       | Explore conversion and enhancement approaches                    |
| `plans-and-specs`                     | Create detailed specs with file references                       |
| `writing-skills`                      | Craft and optimize prompts and instructions                      |
| `writing-plans`                       | Structure the plan and its sections                              |
| `acpx-executor`                       | Execute a prompt via any ACPX provider                           |
| `executing-plans`                     | Execute implementation steps in order                            |
| `simplify`                            | Keep the output concise and non-redundant                        |

## Phases

### Phase 1: Discover and verify

Confirm the source files, target prompts, and required templates before planning
changes.

### Phase 2: Plan conversion

Define how `Prompts/*.txt` should convert to `Prompts/*.md` and what must be
preserved.

### Phase 3: Plan audits and fixes

Specify how to audit `boost-prompt`, `ai-prompt-engineering-safety-review`,
`update-implementation-plan`, and `prompt-builder`.

### Phase 4: Review and hand off

Produce a compact completion report with execution steps, risk notes, and exit
criteria.

## Steps

1. Load `context-map`, `brainstorming`, and `plans-and-specs`.
2. Verify the conversion and audit templates exist.
3. Map the prompt-library dependencies.
4. Plan `Prompts/*.txt` → `Prompts/*.md` conversion.
5. Plan audits for the related `.github/prompts/*.prompt.md` files.
6. Confirm the target prompts reference `context-map` where relevant.
7. Produce the final plan and handoff notes.

## Tasks

- [ ] Read the source inventory and target prompt files
- [ ] Confirm the conversion and audit templates exist
- [ ] Define the TXT→MD conversion scope and idempotency rules
- [ ] Capture the feature specs, file references, and safety checks
- [ ] List the prompts that need audit and cross-reference updates
- [ ] Document the risk items and missing dependency links
- [ ] Compile a concise completion report for implementation

## Subtasks

- [ ] Map `Prompts/*.txt` to their `.md` counterparts
- [ ] Preserve source intent and safety notes in each converted file
- [ ] Check for `context-map` references in each audit target
- [ ] Record any missing template or format assumptions

## Actions

- `read_file(".github/prompts/context-map.prompt.md")` — Load the dependency map
  before planning
- `skill_view(name="brainstorming")` — Expand workflow options and tradeoffs
- `skill_view(name="plans-and-specs")` — Produce the detailed plan artifact
- `skill_view(name="acpx-executor")` — Dispatch tasks to ACPX providers
- `search_files(pattern, target)` — Locate related prompt files and templates
- `delegate_task(goal, toolsets)` — Split audit work when multiple files are
  involved

---

## Reference: `/enhance-markdown` Prompt

> Full definition: `_archive/dev-init.prompts.txt` (lines 99–836)

The `/enhance-markdown` prompt is the four-phase markdown auditor and enhancer
used by the TXT→MD conversion pipeline. Key properties:

```bash
/enhance-markdown <file> [slug]       # audit + enhance mode
/enhance-markdown --txt-to-md [file]  # TXT→MD conversion mode (batch or single)
```

- **9-section template**: Skills → Subagents → Personas → Rules → Phases → Steps
  → Tasks → Subtasks → Actions
- **Batch size**: exactly 7 files per batch
- **Resumable**: each phase checks for existing artifacts before re-running
- **Plugin planning**: uses `createPlan`/`createSpec`/`appendSpec` with
  companion markdown fallback

---

## Phase 5: Execute Implementation Plan

> Run the conversion and enhancement pipeline end-to-end. Idempotent — safe to re-run.

### Entry Check

```
IF docs/prompt-conversion-enhancement-plan.md EXISTS → read it, skip to Step 5.3
ELSE IF docs/dev-init-comprehensive-plan.md EXISTS → plan exists, skip to Step 5.2
ELSE → run Phase 1–4 first, then return here
```

### Step 5.1 — Load Plan Artifacts

```bash
read_file("docs/dev-init-comprehensive-plan.md")
read_file("docs/dev-init-spec.md")
read_file("Bash/archive/artifacts/context-maps/dev-init.context.json")
```

### Step 5.2 — Run `context-map`

1. Load `.github/prompts/context-map.prompt.md`
2. Map all `Prompts/*.txt` → `Prompts/*.md` pairs
3. Map all `.github/prompts/*.prompt.md` dependencies
4. Write `docs/prompts-cross-reference-registry.md`

### Step 5.3 — Run `convert-plaintext-to-md`

For each `Prompts/*.txt` file:

1. Read raw `.txt` content
2. Apply enhancement (Stanford/Anthropic patterns):
    - Critical rules in first 15%
    - Nesting depth ≤ 4
    - Instruction ratio 40–50%
    - Single source of truth (no rule repeated > 2×)
    - 3-tier prioritization: Safety → Core Workflow → Optimization
3. Apply 9-section template:
   `Skills → Subagents → Personas → Rules → Phases → Steps → Tasks → Subtasks → Actions`
4. Write to `Prompts/<same-stem>.md` (overwrite if exists)

### Step 5.4 — Run `boost-prompt`

For each `Prompts/*.md` file:

1. Load `.github/prompts/boost-prompt.prompt.md`
2. Apply quality enhancements:
    - Strengthen rule language (imperative, specific)
    - Add missing frontmatter (title, description, tags, trigger)
    - Ensure consistent heading hierarchy
    - Remove redundant sections
3. **Constraint Preservation Audit**: log any rule removals with justification
4. Write enhanced file back

### Step 5.5 — Run `ai-prompt-engineering-safety-review`

For each `Prompts/*.md` and `.github/prompts/*.prompt.md`:

1. Load `.github/prompts/ai-prompt-engineering-safety-review.prompt.md`
2. Check for:
    - Credential handling safety
    - Backup/rollback instructions present
    - Approval workflows for destructive ops
    - No fabricated verification claims
3. Add safety notes where missing
4. **Fail if critical safety constraints removed** — halt and report

### Step 5.6 — Run `prompt-builder`

For any missing prompts:

1. Load `.github/prompts/prompt-builder.prompt.md`
2. Scaffold new `.prompt.md` files from template
3. Populate with content from plan artifacts

### Step 5.7 — Run `update-implementation-plan`

1. Load `.github/prompts/update-implementation-plan.prompt.md`
2. Update `docs/dev-init-comprehensive-plan.md` with:
    - Actual files processed
    - Issues found and resolved
    - Remaining items
3. Mark completed phases

### Tasks

- [ ] Load all plan artifacts (Step 5.1)
- [ ] Run context-map and write cross-reference registry (Step 5.2)
- [ ] Convert all `Prompts/*.txt` → `Prompts/*.md` (Step 5.3)
- [ ] Boost all `Prompts/*.md` files (Step 5.4)
- [ ] Safety-review all prompts (Step 5.5)
- [ ] Build missing prompts (Step 5.6)
- [ ] Update implementation plan (Step 5.7)

---

## Phase 6: Verify All Prompts Optimal

> Independent verification — read Phase 1 outputs only, not Phase 5 outputs (prevents confirmation bias).

### Step 6.1 — Structural Audit

For each `Prompts/*.md`:

```bash
# Check frontmatter
head -10 Prompts/<name>.prompts.md | grep "^title:"
head -10 Prompts/<name>.prompts.md | grep "^description:"
head -10 Prompts/<name>.prompts.md | grep "^trigger:"
head -10 Prompts/<name>.prompts.md | grep "^tags:"

# Check required sections exist
grep -c "^## Goal" Prompts/<name>.prompts.md
grep -c "^## Phases" Prompts/<name>.prompts.md
grep -c "^## Steps" Prompts/<name>.prompts.md
grep -c "^## Tasks" Prompts/<name>.prompts.md
grep -c "^## Actions" Prompts/<name>.prompts.md
```

### Step 6.2 — Cross-Reference Validation

```bash
# Verify all internal references resolve
grep -o '\[.*\](\./[^)]*)' Prompts/<name>.prompts.md | while read ref; do
  path=$(echo "$ref" | sed 's/.*(\(.*\))/\1/')
  test -f "$path" || echo "BROKEN REF: $ref in Prompts/<name>.prompts.md"
done
```

### Step 6.3 — Conflict Detection

```bash
# Check for duplicate triggers across Prompts/
grep -h "^trigger:" Prompts/*.prompts.md | sort | uniq -d

# Check for duplicate titles
grep -h "^title:" Prompts/*.prompts.md | sort | uniq -d
```

### Step 6.4 — Quality Scoring

Score each `Prompts/*.md`:

| Criterion                             | Points | Detection                                        |
| ------------------------------------- | ------ | ------------------------------------------------ |
| YAML frontmatter complete             | +20    | title + description + trigger + tags present     |
| Summary paragraph present             | +15    | First paragraph after frontmatter is a summary   |
| All required sections                 | +20    | Goal, Phases, Steps, Tasks, Actions present      |
| Skills section references real skills | +10    | Each skill listed exists in `hermes skills list` |
| Actions use real tools                | +10    | Each action maps to an available tool            |
| No broken internal refs               | +15    | All relative paths resolve                       |
| Consistent heading hierarchy          | +10    | H1→H2→H3, no skipped levels                      |

**Threshold**: ≥80 = optimal, 60–79 = needs work, <60 = rewrite required.

### Step 6.5 — Write Verification Report

```markdown
# docs/dev-init-verification-report.md

## Summary

- Total .md files: N
- Optimal (≥80): N
- Needs work (60–79): N
- Rewrite required (<60): N

## Per-File Scores

| File | Score | Issues |
| ---- | ----- | ------ |
| ...  | ...   | ...    |

## Conflicts Found

| Type              | Files | Resolution |
| ----------------- | ----- | ---------- |
| Duplicate trigger | ...   | ...        |

## Broken References

| File | Reference | Status |
| ---- | --------- | ------ |
| ...  | ...       | ...    |
```

### Tasks

- [ ] Structural audit all `Prompts/*.md` files
- [ ] Validate all cross-references resolve
- [ ] Detect duplicate triggers/titles
- [ ] Score each file against quality criteria
- [ ] Write verification report to `docs/dev-init-verification-report.md`
- [ ] Fix any files scoring <80
- [ ] Re-verify after fixes

---

## Phase 7: Cross-Reference Registry

> Build the master registry of all prompts and their relationships.

### Step 7.1 — Build Registry

Write `docs/prompts-cross-reference-registry.md`:

```markdown
# Prompts Cross-Reference Registry

## Prompts/\*.md (Conversion Targets)

| File                  | Trigger     | Status | Score | Depends On                           |
| --------------------- | ----------- | ------ | ----- | ------------------------------------ |
| skills-fix.prompts.md | /skills-fix | ✅     | 85    | context-map, skill-judge             |
| dev-init.prompts.md   | /dev-init   | ✅     | 90    | context-map, convert-plaintext-to-md |
| ...                   | ...         | ...    | ...   | ...                                  |

## .github/prompts/\*.prompt.md (Workflow Prompts)

| File                              | Purpose             | Used By             |
| --------------------------------- | ------------------- | ------------------- |
| context-map.prompt.md             | Dependency mapping  | All dev-init phases |
| convert-plaintext-to-md.prompt.md | TXT→MD conversion   | Phase 5.3           |
| boost-prompt.prompt.md            | Quality enhancement | Phase 5.4           |
| ...                               | ...                 | ...                 |

## Conflict Log

| Conflict | Files | Resolution |
| -------- | ----- | ---------- |
| ...      | ...   | ...        |
```

### Step 7.2 — Final Verification

```bash
# Count total prompts
ls Prompts/*.prompts.md | wc -l
ls .github/prompts/*.prompt.md | wc -l

# Verify registry matches disk
# Every file on disk is in registry
# Every registry entry exists on disk
```

### Tasks

-map.prompt.md | Dependency mapping | All dev-init phases |
| convert-plaintext-to-md.prompt.md | TXT→MD conversion | Phase 5.3 |
| boost-prompt.prompt.md | Quality enhancement | Phase 5.4 |
| ... | ... | ... |

## Conflict Log

| Conflict | Files | Resolution |
| -------- | ----- | ---------- |
| ...      | ...   | ...        |

````

### Step 7.2 — Final Verification

```bash
# Count total prompts
ls Prompts/*.prompts.md | wc -l
ls .github/prompts/*.prompt.md | wc -l

# Verify registry matches disk
# Every file on disk is in registry
# Every registry entry exists on disk
````

### Tasks

- [ ] Build cross-reference registry
- [ ] Verify registry matches disk state
- [ ] Commit all changes with `git commit -m "dev-init: complete prompt-library refresh"`

---

## Execution Summary

When all 7 phases are complete, output:

```
========================================
DEV INIT — PROMPT LIBRARY REFRESH COMPLETE
========================================
Phases executed:    7/7
Prompts converted:  N/N (.txt → .md)
Prompts boosted:    N/N
Safety reviews:     N passed, N failed
Quality score ≥80:  N/N
Conflicts resolved: N
Broken refs fixed:  N
Registry:           docs/prompts-cross-reference-registry.md
Verification:       docs/dev-init-verification-report.md
========================================
```
