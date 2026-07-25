---
author: Hermes Agent
description: Use when managing git worktrees, running parallel AI agents with worktrees,
  setting up hooks, configuring wt.toml, and automating per-worktree setup.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: worktrunk
tags:
- git
- worktree
- parallel-development
- automation
title: Worktrunk
version: 1.0.0

---
# Worktrunk

## Overview

Manage git worktrees for parallel development workflows. Create isolated worktree environments, configure per-worktree hooks and settings, and run multiple AI agents on different features simultaneously.

## When to Use

- Managing git worktrees for parallel feature development
- Running multiple AI agents on isolated worktrees
- Setting up worktree hooks and wt.toml configuration
- Automating per-worktree dev server/database setup
- Merging diverged clones from the same remote

## When NOT TO USE

- Simple feature branches (just use git branch)
- Single-worktree development
- Non-git workflows

## Skills Required

| Skill | Purpose |
|-------|---------|
| `using-git-worktrees` | Git worktree basics |
| `dispatching-parallel-agents` | Run agents on separate worktrees |

## Workflow

### Phase 1: Setup Worktrunk

```bash
# Install worktrunk CLI if needed
cargo install worktrunk

# Initialize wt.toml configuration
wt init

# Example wt.toml:
# [worktree]
# base_dir = "../wt-{branch}"
# hooks = ["post-create", "post-merge"]
```

### Phase 2: Create Worktrees

```bash
# Create a worktree for a feature
wt switch feature/new-ui

# Create with custom path
wt create feature/api-v2 --path ../api-v2-work

# List all worktrees
wt list
```

### Phase 3: Run Parallel Agents

1. Create worktrees for each parallel task
2. Dispatch agents to each worktree:
   ```bash
   # Agent 1: Frontend worktree
   cd ../wt-feature-ui && claude "Implement the new dashboard UI"

   # Agent 2: Backend worktree
   cd ../wt-feature-api && claude "Add the new API endpoints"
   ```
3. Collect results from each worktree

### Phase 4: Merge & Cleanup

```bash
# Merge a worktree branch
wt merge feature/new-ui

# Remove worktree after merge
wt remove feature/new-ui

# Clean up all merged worktrees
wt clean
```

## Merging a Diverged Clone

When two local directories point to the same remote but have diverged:

```bash
# 1. Find unique files
diff -rq projects/clone-a projects/clone-b --exclude='.git' > /tmp/diff.txt

# 2. Copy unique files
cp -r projects/clone-a/<unique-path> projects/<target>/

# 3. Commit and clean up
git add . && git commit -m "feat: import unique files from clone-a"
rm -rf projects/clone-a
```

## Verification Checklist

- [ ] Worktrees created and isolated
- [ ] Hooks configured in wt.toml
- [ ] Agents dispatched to separate worktrees
- [ ] Results collected and merged
- [ ] Stale worktrees cleaned up

## Pitfalls

- **Same remote ≠ same history:** Diverged clones share the remote URL but have independent commit graphs
- **Large diffs:** Review diffs before copying — don't blindly overwrite
- **Forgetting to clean up:** Stale worktrees consume disk space
- **Hook conflicts:** Per-worktree hooks can interfere with each other

Use for git worktree management, running parallel AI agents with worktrees, setting up hooks, configuring wt.toml, and automating dev server/database setup per worktree.

## When to Use

- Managing git worktrees
- Running parallel AI agents with worktrees
- Setting up worktree hooks
- Configuring wt.toml
- Automating per-worktree setup
- Parallel development workflows

## When NOT to Use

- Simple feature branches
- Single-worktree development
- Non-git workflows
- Real-time collaboration

## Workflow

### Phase 1: Setup Worktrunk

- Install Worktrunk CLI
- Configure wt.toml
- Set up hooks
- Prepare environment

### Phase 2: Create Worktrees

- Use `wt switch` to create
- Configure per-worktree setup
- Automate dev server startup
- Set up database if needed

### Phase 3: Run Parallel Agents

- Spawn multiple AI agents
- Each agent uses isolated worktree
- Agents work independently
- Collect results

### Phase 4: Merge & Cleanup

- Use `wt merge` to integrate
- Use `wt remove` to cleanup
- Verify integration
- Archive work

## Tools & References

- **Related Skills**: using-git-worktrees, dispatching-parallel-agents
- **Worktrunk CLI**: `wt` commands
- **Configuration**: wt.toml setup
- **Hooks**: Pre/post worktree hooks

## Merging a Diverged Clone (Same Remote)

Use `wt` isolation when two local directories point to the same remote but have diverged histories. Do NOT use `git merge --allow-unrelated-histories` — it pollutes history.

### Scenario
- `projects/comicwise` (79 commits, active)
- `projects/comicwise_push_clean` (3 commits, diverged, same remote URL)
- Goal: recover unique files from push_clean into comicwise, then delete push_clean

### Approach

```bash
# 1. Find files that exist in push_clean but not (or differ) in comicwise
git -C projects/comicwise_push_clean diff --name-only HEAD projects/comicwise/HEAD

# OR compare working trees directly
diff -rq projects/comicwise_push_clean projects/comicwise \
  --exclude='.git' > /tmp/diverge_diff.txt

# 2. Copy unique files into comicwise
cp -r projects/comicwise_push_clean/<unique-path> projects/comicwise/<target-path>

# 3. Commit in comicwise
cd projects/comicwise
git add .
git commit -m "feat: import unique assets from comicwise_push_clean"

# 4. Delete diverged clone (local only — same remote, so no remote delete needed)
rm -rf projects/comicwise_push_clean
```

### Pitfalls

- **Same remote ≠ same history**: diverged clones share the remote URL but have independent commit graphs. Never force-push from push_clean or you overwrite comicwise history.
- **1141 file diffs** is typical when a clone diverged early and accumulated different generated assets. Review the diff before copying — don't blindly overwrite.
- **`wt` isolation**: use a worktree in comicwise to stage the import so the main worktree stays clean during the copy.

## Best Practices

- Use consistent worktree naming
- Automate setup with hooks
- Keep worktrees focused
- Clean up after use
- Document worktree purpose
- Use LLM commit messages
- Archive important work

