---
name: git-gh-commands
title: Git & GitHub CLI Commands
description: "Quick-reference skill for everyday git operations (pull, push, commit, add, diff, clone, checkout, stash, status) and gh CLI (PR, issue, repo, workflow, API)."
version: 1.0.0
author: Alexa
license: MIT
tags: [git, gh, github, cli, commands, reference]
related_skills:
  - git-helper
  - github-pr-workflow
  - github-auth
  - github-repo-management
  - git-submodule-workflow
  - using-git-worktrees
---
## Goal
Quick-reference skill for everyday git operations (pull, push, commit, add, diff, clone, checkout, stash, status) and gh CLI (PR, issue, repo, workflow, API).


# Git & GitHub CLI Commands

> Compact reference for daily git + gh operations. Use with any Hermes profile.

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


## When to Use

- Need to run git pull/push/commit/add/diff/clone/checkout/stash/status
- Need to create or manage PRs via gh CLI
- Need to script git operations across multiple repos
- Need to verify or debug git state
- Need to scan or inventory a multi-repo workspace (batch `git -C <dir>` operations)
- Need safe filesystem traversal for repo inventories; see `references/multi-repo-scan-pitfalls.md`

## When NOT to Use

- Complex merge conflict resolution → use `git-helper`
- Full PR lifecycle → use `github-pr-workflow`
- Git auth setup → use `github-auth`
- Submodule management → use `git-submodule-workflow`
- Worktree isolation → use `using-git-worktrees`

## Environment

```bash
# Verify git is available
git --version

# Verify gh is available
gh --version

# Verify auth status
gh auth status

# Current git context
git status --short
git branch -a
```

## Git Command Reference

### Core Operations

| Operation | Command | Notes |
|-----------|---------|-------|
| Status | `git status --short` | Compact view: `M`=modified, `??`=untracked |
| Add | `git add <path>` | Use `-A` for all, `-p` for interactive patch |
| Commit | `git commit -m "type: description"` | Types: feat, fix, docs, refactor, test, chore, perf |
| Pull | `git pull --ff-only` | Prevents accidental merge commits |
| Push | `git push origin <branch>` | Add `-u` for first push to set upstream |

### Branching

| Operation | Command | Notes |
|-----------|---------|-------|
| List | `git branch -a` | Local + remote |
| Create | `git checkout -b <name>` | Branch from current HEAD |
| Switch | `git checkout <name>` | Or `git switch <name>` |
| Rename | `git branch -m <old> <new>` | Works on current branch if 1 arg |
| Delete local | `git branch -D <name>` | Force delete (use `-d` for safe) |
| Delete remote | `git push origin --delete <name>` | Also: `git push origin :<name>` |

### Diff & Log

| Operation | Command | Notes |
|-----------|---------|-------|
| Working diff | `git diff` | Unstaged changes |
| Staged diff | `git diff --cached` | What will be committed |
| Branch diff | `git diff <a>..<b> --stat` | File stats between branches |
| Show commit | `git show <hash>` | Full diff for a commit |
| Log (compact) | `git log --oneline -10` | Last 10 commits, one line each |
| Log (graph) | `git log --oneline --all --graph` | Full branch topology |

### Stash

| Operation | Command | Notes |
|-----------|---------|-------|
| Push | `git stash push -m "description"` | Stash with descriptive message |
| List | `git stash list` | Show all stashes |
| Pop | `git stash pop` | Apply + remove latest |
| Apply | `git stash apply stash@{n}` | Apply without removing |
| Drop | `git stash drop stash@{n}` | Remove specific stash |
| Clear | `git stash clear` | Remove ALL stashes (irreversible) |

### Undo & Fixup

| Operation | Command | Notes |
|-----------|---------|-------|
| Unstage | `git restore --staged <file>` | Keep working changes |
| Discard working | `git checkout -- <file>` | Discard unstaged changes |
| Amend commit | `git commit --amend -m "new msg"` | Only if not pushed |
| Undo last commit | `git reset --soft HEAD~1` | Keep changes staged |
| Reset hard | `git reset --hard <ref>` | **DESTRUCTIVE** — discards working changes |
| Revert committed | `git revert <hash>` | Safe: creates inverse commit |

### Remote

| Operation | Command | Notes |
|-----------|---------|-------|
| List remotes | `git remote -v` | Shows fetch + push URLs |
| Add remote | `git remote add origin <url>` | Standard origin naming |
| Remove remote | `git remote remove <name>` | |
| Fetch all | `git fetch --all --prune` | Prune stale remote tracking |
| Prune local | `git remote prune origin` | Remove stale remote branches locally |

### Tags

| Operation | Command | Notes |
|-----------|---------|-------|
| List | `git tag -l` | All tags |
| Create | `git tag <tagname>` | Lightweight |
| Annotated | `git tag -a v1.0 -m "release"` | With message |
| Push | `git push origin --tags` | Push all tags |
| Delete local | `git tag -d <tagname>` | |
| Delete remote | `git push origin --delete <tagname>` | |

### Submodules

| Operation | Command | Notes |
|-----------|---------|-------|
| Init | `git submodule init` | After clone with submodules |
| Update | `git submodule update` | Checkout pinned commits |
| Init+Update | `git submodule update --init --recursive` | Full recursive init |
| Add | `git submodule add <url> <path>` | |

### Worktrees

| Operation | Command | Notes |
|-----------|---------|-------|
| Add | `git worktree add <path> <branch>` | Isolated workspace |
| List | `git worktree list` | All worktrees |
| Remove | `git worktree remove <path>` | Prune after done |
| Prune | `git worktree prune` | Clean stale worktree refs |

## GitHub CLI (gh) Reference

### Authentication

```bash
gh auth login                  # Interactive login
gh auth status                 # Verify auth
gh auth token                  # Print current token (careful!)
```

### Pull Requests

```bash
gh pr create --fill            # Create PR from current branch
gh pr create -t "title" -b "body"  # Create with explicit content
gh pr checkout <number>        # Check out PR locally
gh pr list -s <open|closed|merged> # List PRs
gh pr view <number>            # View PR details
gh pr review <number> -a       # Approve PR
gh pr review <number> -c       # Comment
gh pr merge <number> -m        # Merge with commit message
gh pr diff <number>            # Show PR diff
```

### Issues

```bash
gh issue create -t "title" -b "body"  # Create issue
gh issue list -s open          # List open issues
gh issue view <number>         # View issue details
gh issue close <number>        # Close issue
gh issue reopen <number>       # Reopen issue
gh issue comment <number> -b "text"  # Add comment
```

### Repositories

```bash
gh repo create <name> [--public|--private]  # Create repo
gh repo clone <owner>/<repo>    # Clone via gh (SSH auth)
gh repo fork <owner>/<repo>    # Fork to your account
gh repo view [owner/repo]      # View repo README in terminal
gh repo sync [owner/repo]      # Sync fork with upstream
```

### Workflows & Actions

```bash
gh workflow list               # List workflows
gh workflow run <name>         # Trigger workflow_dispatch
gh run list -L 10              # Recent runs
gh run view <id>               # Run details + logs
gh run watch <id>              # Watch run in real-time
```

### Releases

```bash
gh release list                # List releases
gh release create v1.0 --notes "notes"  # Create release
gh release upload v1.0 <file>  # Upload asset
gh release download v1.0       # Download assets
```

### API

```bash
gh api repos/:owner/:repo      # Get repo info (JSON)
gh api repos/:owner/:repo/branches  # List branches
gh api -X PATCH repos/:owner/:repo -f default_branch=production  # Update repo
gh api repos/:owner/:repo/hooks  # List webhooks
gh api search/repositories -q "q=org:rhixecompany topic:comics"  # Search
```

## Common Workflows

### Daily Save
```bash
git add -A && git commit -m "type: short description" && git push
```

### Sync Fork with Upstream
```bash
gh repo sync <owner>/<fork> -b development
```

### Create Feature Branch + PR
```bash
git checkout -b feat/my-thing
# ... make changes ...
git add -A && git commit -m "feat: my thing description"
git push -u origin feat/my-thing
gh pr create --fill
```

### Safe Rollback (pushed commit)
```bash
git revert HEAD --no-edit
git push
```

### Diff Against Production
```bash
git log --oneline production..development
git diff production..development --stat
```

## Multi-Repo Batch Operations

Scan, inventory, or verify multiple repos in a workspace with `git -C <dir>` loops.

### Batch Scan — Remote, Branch, and Owner

```bash
# Quick scan: remote URL + current branch per repo
for dir in projects/*/; do
  name=$(basename "$dir")
  if [ -d "$dir/.git" ]; then
    remote=$(git -C "$dir" remote get-url origin 2>/dev/null || echo "NO_REMOTE")
    branch=$(git -C "$dir" branch --show-current 2>/dev/null || echo "DETACHED")
    echo "$name | remote=$remote | current=$branch"
  fi
done
```

### Batch Branch Counts + Default Branch

```bash
# Per-repo: local branches, remote branches, GitHub default branch
for dir in projects/*/; do
  name=$(basename "$dir")
  if [ -d "$dir/.git" ]; then
    local_b=$(git -C "$dir" branch | wc -l)
    remote_b=$(git -C "$dir" branch -r 2>/dev/null | grep -v HEAD | wc -l)
    default=$(git -C "$dir" remote show origin 2>/dev/null | grep "HEAD branch" | awk '{print $NF}' || echo "N/A")
    echo "$name | LOCAL=$local_b | REMOTE=$remote_b | DEFAULT=$default"
  fi
done
```

### Detect Partial Normalization

This catches repos where local `production`/`development` branches exist but were never pushed:

```bash
for dir in projects/*/; do
  name=$(basename "$dir")
  if [ -d "$dir/.git" ]; then
    local_b=$(git -C "$dir" branch | wc -l)
    remote_b=$(git -C "$dir" branch -r 2>/dev/null | grep -v HEAD | wc -l)
    # 2 local + <2 remote = partial normalization
    if [ "$local_b" = "2" ] && [ "$remote_b" != "2" ]; then
      echo "PARTIAL: $name (local=$local_b, remote=$remote_b)"
    fi
  fi
done
```

### Extract Owner/Repo from Remote

```bash
REMOTE_URL=$(git remote get-url origin)
OWNER_REPO=$(echo "$REMOTE_URL" | sed -E 's|.*github\\.com[:/]||; s|\\.git$||')
OWNER=$(echo "$OWNER_REPO" | cut -d/ -f1)
REPO=$(echo "$OWNER_REPO" | cut -d/ -f2)
# For org repos: OWNER=Rhixe-company. For user repos: OWNER=rhixecompany
```

### Batch Set Default Branch (all repos)

```bash
# Danger: reads owner/repo from each remote and patches the default
for dir in projects/*/; do
  if [ -d "$dir/.git" ]; then
    remote=$(git -C "$dir" remote get-url origin 2>/dev/null) || continue
    owner_repo=$(echo "$remote" | sed -E 's|.*github\\.com[:/]||; s|\\.git$||')
    # Only patch if default isn't already production
    curr_default=$(git -C "$dir" remote show origin 2>/dev/null | grep "HEAD branch" | awk '{print $NF}')
    if [ "$curr_default" != "production" ]; then
      echo "FIX: $owner_repo (default=$curr_default → production)"
      gh api repos/$owner_repo -X PATCH -f default_branch=production
    fi
  fi
done
```

## Pitfalls

- **MSYS/PowerShell paths**: `terminal()` runs bash/MSYS. Use POSIX paths (`/c/Users/...`, not `C:\...`) inside terminal calls. Use forward slashes for gh API JSON paths.
- **CRLF warnings**: Git on Windows warns "LF will be replaced by CRLF" on `git add`. Harmless — ignore or configure `git config core.autocrlf input`.
- **`gh pr create --fill`** uses the commit message of the last commit — run `git commit` with a good message before `gh pr create`.
- **Destructive commands**: `git reset --hard`, `git branch -D`, `git stash clear`, `git push --force` are irreversible. Always `git stash list` and `git status` before these.
- **Windows long paths**: Some repos exceed 260-char Windows path limit. Use `git config --system core.longpaths true` (admin) to enable long path support.
- **Submodule gotchas**: After `git submodule update`, detached HEAD is normal. Enter each submodule dir and `git checkout <branch>` to make changes.

## Verification

```bash
# Quick health check
git --version && gh --version && gh auth status
# Working tree
git status --short
# Branch topology
git log --oneline --all --graph -10
```

## Best Practices

- Commit style: `type: description` (feat, fix, docs, refactor, test, chore, perf)
- Pull with `--ff-only` to avoid accidental merge commits
- `git stash push -m "desc"` not bare `git stash`
- Verify with `git status` before destructive ops
- Use `git diff --stat` for branch comparison summaries
- Prefer `git revert` over `git reset --hard` for shared branches
- Prune remote tracking: `git fetch --all --prune` periodically
