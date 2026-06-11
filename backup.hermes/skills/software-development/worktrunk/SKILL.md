---
category: software-development
title: Worktrunk
name: worktrunk
description: "Use when managing git worktrees, running parallel AI agents with worktrees, setting up hooks, configuring wt.toml, and automating per-worktree setup."
---


## Description


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

