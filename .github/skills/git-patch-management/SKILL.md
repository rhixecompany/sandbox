---
name: git-patch-management
description: Manage Git patch files across multi-project workspaces. Use when creating, applying, organizing, or cleaning up patch files across multiple repositories in a monorepo or workspace.
category: devops
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - git
  - patch
  - workspace
  - version-control
title: Git Patch Management
metadata:
  hermes:
    tags: []
---
# Git Patch Management

Manage Git patch files across multi-project workspaces. Use when creating, applying, organizing, or cleaning up patch files across multiple repositories.

## Overview

Automated reasoning and workflow tool for `git-patch-management`. Execute multi-step tasks with deterministic quality controls and structured outputs.

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

## Pitfalls

- **None documented yet.**
- Add common pitfalls, edge cases, and failure modes specific to this skill.

## Verification Checklist

- [ ] All tasks completed
- [ ] Output verified
- [ ] Edge cases handled

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## When to Use


- creating, applying, organizing, or cleaning up patch files across multiple repositories in a monorepo or workspace
- creating, applying, organizing, or cleaning up patch files across multiple repositories
- **Triggers**: "git patch management" required for a project

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
