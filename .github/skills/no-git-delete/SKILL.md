---
name: no-git-delete
description: "Constraint flag: never delete git history, branches, tags, or repository structure. Prevents destructive git operations during automated workflows."
version: 1.0.0
author: Hermes Agent
license: MIT
tags:
  - constraint
  - git
  - safety
  - preservation
---

# No Git Delete

**Constraint flag**: never delete git history, branches, tags, or repository structure.

When this skill is active, the agent may NOT:
- Delete or force-push branches
- Remove git tags
- Delete `.git` directory or contents
- Squash or rebase history destructively
- Run `git clean -fd` or similar

The agent MAY:
- Create new branches
- Commit changes
- View git history and status

## When to use

- During automated agent workflows where git safety is paramount
- When multiple agents work on the same repository
- As safety constraint during experimentation

## Verification

- [ ] Git history fully preserved
- [ ] No branches deleted
- [ ] No force pushes performed
- [ ] All original commits intact
