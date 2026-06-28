---
name: project-consolidation
description: Five-phase workflow for cleaning up and restructuring a project. Use when consolidating duplicate scripts, standardizing file layout, and reconciling divergent project structures.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - consolidation
  - project
  - restructuring
  - cleanup
---

# Project Consolidation

Five-phase workflow for cleaning up and restructuring a project.

## Phases

### Phase 1: Inventory
Scan the workspace, index all files by type and purpose.

### Phase 2: Cross-reference
Map equivalent files, detect duplicates, identify orphans.

### Phase 3: Planning
Design the canonical layout, plan migrations.

### Phase 4: Execution
Move/merge/delete files according to plan.

### Phase 5: Verification
Validate structure, run tests, verify no breaks.

## When to use

- Duplicate scripts littered across the workspace
- Divergent project structures between repos
- After a migration that left orphan files
- Before onboarding new team members

## Verification

| Phase | Check |
|-------|-------|
| 1 | All files discovered and categorized |
| 2 | Duplicate mapping complete |
| 3 | Migration plan reviewed |
| 4 | Files moved without data loss |
| 5 | All tests pass, structure clean |
