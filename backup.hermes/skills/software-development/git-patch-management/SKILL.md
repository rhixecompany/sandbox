---
name: git-patch-management
title: Git Patch Management
description: >
  Workflow for managing Git patch files across a multi-project workspace:
  inventory, verify (git apply --check, SHA matching), classify, apply, and
  organize patches into canonical subdirectories.
author: Alexa
tags: [git, patches, migration, workspace-organization, verification]
trigger: |
  User asks to "fix patches", "debug patches", "apply patches",
  "organize patches", "check patches", "find dead patches",
  or mentions .patch files in the workspace
---## Goal
Use when > to accomplish the associated tasks and objectives.


# Git Patch Management

Systematic workflow for verifying, classifying, applying, and organizing Git patches across projects.

## Workflow
### Phase 1: Preparation

- Understand the context and requirements.
- Gather necessary tools and resources.

### Phase 2: Execution

- Perform the core actions required by the skill.
- Apply the techniques and procedures outlined.

### Phase 3: Verification

- Verify the results against the expected outcomes.
- Confirm that the task has been completed successfully.


## Phase 1: Inventory

1. Find all `.patch` files in the workspace
2. Note each patch's target project path from `diff --git` lines
3. List all project directories under `projects/`

## Phase 2: Verify Each Patch

For each patch, run:

```bash
cd <target-project> && git apply --check <path-to-patch>
```

### Interpretation of results:

| Result | Meaning | Classification |
|--------|---------|---------------|
| Applies cleanly | Patch is valid and pending | **PENDING-APPLY** |
| "already exists in working directory" | Files already present (not via this patch) | Check commit SHAs |
| "patch does not apply" / "hunk failed" | Files conflict with current state | **CONFLICT** |
| Error about path not found | Target project doesn't exist | **MISSING-TARGET** |

### Commit SHA verification

For "already exists" patches, extract commit SHAs from the patch headers:

```
grep '^From [a-f0-9]' <patch>
```

Verify each in the target git history:

```bash
cd <target-project> && git cat-file -t <SHA> 2>/dev/null
```

If all SHAs found → **PRE-APPLIED** (commits already in history).
If some missing → partial application needed.

## Phase 3: Classify

| Class | Meaning | Action |
|-------|---------|--------|
| **PRE-APPLIED** | Commits already in git history | Move to `patches/pre-applied/` |
| **MISSING-TARGET** | Target project doesn't exist | Create project OR map to correct target |
| **ENHANCED** | Valid patch for existing project (was mislabeled obsolete) | Move to `patches/enhanced/` |
| **OBSOLETE** | Truly dead — template/scaffolding, no active target | Keep in `patches/obsolete/` |

## Phase 4: Execute

1. **MISSING-TARGET**: Create project dir and apply patch
   - `mkdir -p projects/<name> && cd projects/<name> && git init && git apply ../../<patch>`
   - Commit: `feat: initial project from <patch-name>`
   
2. **Reclassify mislabeled**: Move from `patches/obsolete/` to `patches/enhanced/`

3. **PRE-APPLIED**: Move to `patches/pre-applied/`

## Phase 5: Final Layout

```
patches/
├── pre-applied/     # Commits already in project git history
├── enhanced/        # Valid patches for existing projects
├── obsolete/        # Truly dead — no active project target
├── archive/         # Historical backups (older versions)
└── regenerate/      # Queued for regeneration
```

## Pitfalls

- **"already exists in working directory"** is NOT a failure — it usually means the commit is already applied. Always check SHA history before classifying.
- **Case sensitivity**: Patch targets may use lowercase while project dirs use mixed case (e.g., `python-projects.patch` → `projects/Python-projects/`)
- **V4A format patches** (multi-file, not standard git format-patch) need special handling — check content with `grep '^diff --git'` or `grep '^Update File:'`
- **Obsolete patches** may target projects that exist with matching commits. Always test with `git cat-file -t <SHA>` before classifying as obsolete.
- **Do NOT create backup files** — use git for version control (SOUL.md rule).


