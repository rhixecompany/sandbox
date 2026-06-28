---
name: git-patch-management
description: Manage Git patch files across multi-project workspaces. Use when creating, applying, organizing, or cleaning up patch files across multiple repositories in a monorepo or workspace.
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - git
  - patch
  - workspace
  - version-control
---

# Git Patch Management

Manage Git patch files across multi-project workspaces. Use when creating, applying, organizing, or cleaning up patch files across multiple repositories.

## Workflow

1. **Create** — Generate patches from staged/unstaged changes
2. **Organize** — Categorize patches by project and purpose
3. **Apply** — Apply patches in correct order across repos
4. **Cleanup** — Remove stale or merged patches

## Usage

```bash
# Create a patch
git format-patch -1 HEAD

# Apply patches in order
git apply --whitespace=fix <patch-file>

# List all patches in workspace
git-patch-management list
```

## Verification

- [ ] Patches apply cleanly across all repos
- [ ] Patch files organized by project
- [ ] Stale patches cleaned up
- [ ] Git history preserved
