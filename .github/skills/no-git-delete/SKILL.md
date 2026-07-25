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
title: No Git Delete
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


## When to Use

- Use when _(describe scenario 1)_
- Use when _(describe scenario 2)_
- Use when _(describe scenario 3)_



## When NOT to Use

- When the task is outside this skill's domain
- When simpler approaches are more effective
- When required dependencies are unavailable



## Workflow

### Phase 1: Preparation

_Set up dependencies, gather inputs, validate the environment._

### Phase 2: Execution

_Run the primary workflow._

### Phase 3: Verification & Cleanup

_Validate results, document outcomes, clean up temporary resources._


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
