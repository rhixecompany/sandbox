---
author: Alexa
description: Use when modifying an existing implementation plan — adding/removing/reordering
  phases, updating task status, patching requirements, or syncing cross-reference
  sections after structural changes.
license: MIT
name: update-implementation-plan
tags:
- imported
title: Update Implementation Plan
version: 1.0.0

---
# Update Implementation Plan

## When to Use

- Adding new phases or tasks to an existing plan
- Removing or deprecating phases/tasks
- Reordering phases (e.g., inserting dependency-audit before consolidation)
- Updating task completion status or dates
- Syncing cross-reference sections after structural changes
- Patching requirements, constraints, or dependencies
- Fixing broken frontmatter or template compliance
- **Batch updating multiple implementation plans in a folder**
- **Batch applying same change (e.g., new phase) across multiple plans**

## Goal

Safely mutate an existing implementation plan file while preserving template integrity, cross-reference consistency, and git history. **Supports single plan and batch processing of multiple plans.**

## Prerequisites

- Read the target plan file with `read_file` before any edits
- Identify all cross-reference sections that enumerate phases/tasks
- Create a backup: `cp <file> <file>.bak` (only if git is not available)

## Workflow

### Phase 0: Batch Discovery (Batch/Folder Modes Only)

**Entry check:** If `.hermes/plans/batch-update-discovery.md` exists → skip to Phase 1.

1. **Discover targets** — Resolve plan file list from:
   - `--batch plan1.md plan2.md ...` explicit file arguments
   - `--folder .hermes/plans/` recursive scan for `*.md` files
   - `--pattern "*.md"` filter by glob pattern
2. **Validate targets** — Filter existing files, validate frontmatter
3. **Write discovery artifact** → `.hermes/plans/batch-update-discovery.md` with plan list

### Phase 1: Read & Analyze

1. Read the full plan file with `read_file`
2. Identify the current phase count and task IDs
3. Map all cross-reference sections:
   - Frontmatter `description:` — phase counts, priorities
   - Frontmatter `tags:` — domain tags
   - Frontmatter `dependencies:` / `skills:` — required skills
   - Top-level summary — priority text
   - Priority tiers table
   - Phase sections (the body) — `### Phase N:` blocks
   - Skill cross-reference table
   - Verification gate script
   - Pitfalls list
   - Actions list
4. Determine what needs to change and which sections are affected

### Phase 2: Apply Changes

**For adding a phase:**
1. Insert new `### Phase N:` block at the correct position
2. Renumber all subsequent phases
3. Update every cross-reference section that lists phases
4. Add new TASK-IDs sequentially (don't reuse deleted IDs)

**For removing a phase:**
1. Delete the `### Phase N:` block
2. Renumber all subsequent phases
3. Update every cross-reference section
4. Mark affected TASK-IDs as deprecated (don't renumber existing completed tasks)

**For reordering phases:**
1. Move the phase block
2. Renumber all phases
3. Update every cross-reference section
4. Verify no task dependencies break

**For updating task status:**
1. Find the task row in the phase table
2. Update the `Completed` column (✅ or empty)
3. Update the `Date` column if completing

**For frontmatter changes:**
1. Patch the specific field
2. Validate YAML syntax after edit

**Batch mode:** Apply the same change across all target plans using `execute_code` with a bulk update script. Each plan gets its own commit. Use `delegate_task` for parallel processing if plans are independent.

### Phase 3: Verify

After every mutation, run these checks:

```bash
# 1. Validate YAML frontmatter
head -20 <file> | python3 -c "import sys,yaml; yaml.safe_load(sys.stdin)" && echo "YAML OK"

# 2. Check phase numbering is sequential
grep '^### Phase' <file> | nl

# 3. Verify no orphaned cross-references
grep -c 'Phase' <file>  # count should match in all cross-ref sections

# 4. Check for duplicate section headers
grep '^## ' <file> | sort | uniq -d

# 5. Verify template compliance (all required sections present)
for section in "Introduction" "Requirements" "Implementation Steps" "Alternatives" "Dependencies" "Files" "Testing" "Risks"; do
  grep -q "## $section" <file> || echo "MISSING: $section"
done
```

**Batch mode:** Run verification across all modified plans in parallel using `execute_code`. Aggregate results to `.hermes/plans/batch-verification-report.md` with per-plan pass/fail status.

## Cross-Reference Sync Rule

**When you add/remove/reorder a phase, you MUST update ALL of these sections in the same edit pass:**

| Section | What to update |
|---------|---------------|
| Frontmatter `description:` | Phase count, priority list |
| Frontmatter `tags:` | Add domain tags if new phase introduces new domain |
| Frontmatter `dependencies:` / `skills:` | Add skills needed by new phases |
| Top-level summary | Renumber priorities, extend text |
| Priority tiers table | Insert/remove tiers, renumber subsequent |
| Phase sections (body) | Insert/remove/reorder `### Phase N:` blocks |
| Skill cross-reference table | Add/remove rows for each phase |
| Verification gate script | Add/remove checks for phase deliverables |
| Pitfalls list | Add/remove phase-specific pitfalls |
| Actions list | Add/remove tool/skill refs for phases |

**Rule:** If you change a phase but miss any cross-reference section, the document becomes self-contradictory. Always do a final grep sweep.

## Pitfalls

- **Orphaned cross-references:** After adding Phase 5, the summary still says "4 phases." Always grep-sweep.
- **Duplicate section headers:** Files edited across sessions accumulate stale sections. Run `grep -c '```'` parity check for fenced blocks.
- **Task ID collision:** Don't reuse TASK-IDs from deleted tasks. Keep a monotonic counter.
- **Frontmatter drift:** After patching body, re-read frontmatter to confirm it still matches.
- **Stale verification gates:** If you add a phase, the verification script must test its outputs.

## Template Reference

See `create-implementation-plan` skill for the full plan template structure. This skill assumes the plan already exists and follows that template.

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

