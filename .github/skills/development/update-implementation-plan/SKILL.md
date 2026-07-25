---
author: Hermes Agent
description: Use when modifying an existing implementation plan — adding/removing/reordering tasks, adjusting scope, or updating milestones. Maintains plan integrity and traceability.
license: MIT
metadata:
  hermes:
    tags: [imported, planning, implementation, plan-management]
name: update-implementation-plan
tags:
- imported
- planning
- implementation
- plan-management
- scripts
title: Update Implementation Plan
version: 1.1.0
---

# Update Implementation Plan

## Overview

Modify an existing implementation plan by adding, removing, or reordering tasks, adjusting scope, or updating milestones. Maintains plan integrity and traceability throughout changes.

## When to Use

- Adding new tasks to an existing plan
- Removing completed or deprecated tasks
- Reordering tasks based on priority changes
- Updating milestones or deadlines
- Adjusting scope based on new requirements

## When NOT to Use

- Creating a new plan from scratch (use `create-implementation-plan`)
- Executing plan tasks (use `executing-plans`)
- Reviewing plan progress (use `session-audit-report`)

## Workflow

### Phase 1: Load Existing Plan

```bash
# Find plan file
ls .hermes/plans/*.md

# Read current plan
cat .hermes/plans/plan-name.md
```

### Phase 2: Analyze Changes

Identify what needs modification:
- **Add tasks:** New requirements discovered
- **Remove tasks:** Deprecated or completed
- **Reorder tasks:** Priority shifts
- **Update metadata:** Milestones, deadlines, owners

### Phase 3: Apply Changes

Apply changes while preserving:
- Task IDs (never reuse)
- Dependency chains
- Traceability to requirements

### Phase 4: Validate & Save

```bash
# Validate structure
update-implementation-plan --validate .hermes/plans/plan-name.md

# Save updated plan
update-implementation-plan --save .hermes/plans/plan-name.md
```

## Usage Examples

```bash
# Add task to plan
update-implementation-plan --add "New task description" --after "TASK-123"

# Remove task
update-implementation-plan --remove "TASK-456"

# Reorder
update-implementation-plan --move "TASK-789" --before "TASK-101"

# Update milestone
update-implementation-plan --milestone "M2" --date "2026-08-01"
```

## Error Handling

- **Plan not found:** Exits with code 1, lists available plans
- **Invalid task ID:** Exits with code 2, prints valid IDs
- **Dependency cycle:** Warns, prevents save
- **Permission denied:** Exits with code 2, prints path

## Verification Checklist

- [ ] All task IDs unique and preserved
- [ ] Dependencies still valid after reordering
- [ ] Milestones updated to reflect changes
- [ ] Traceability to requirements maintained
- [ ] No orphaned tasks

## Pitfalls

- **Reusing task IDs:** Never reuse IDs — breaks traceability
- **Breaking dependencies:** Reordering without checking dependencies
- **Skipping validation:** Always validate before saving

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## Related Skills

- `create-implementation-plan` — Create new plans
- `executing-plans` — Execute plan tasks
- `writing-plans` — Plan authoring guidelines

## References

- `references/plan-management.md` — Plan structure and lifecycle
- `references/dependency-management.md` — Handling task dependencies