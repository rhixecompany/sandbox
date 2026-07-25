# Local Git Fixup After Repo Migration

After migrating repos between GitHub accounts (org → user, user → org, or
account rename), local clones still point to the old remote URL and may be
in a broken state (detached HEAD from aborted rebase, stale remotes,
untracked files blocking checkout). This reference documents the cleanup.

## Phase 1: Inventory Stale Remotes

Scan all local project clones for remotes pointing to the old account:

```bash
for d in projects/*/; do
  if [ -f "$d/.git/config" ]; then
    remote=$(grep -A2 'remote "origin"' "$d/.git/config" | grep url)
    echo "$(basename $d) → $remote"
  fi
done
```

Spot-check for the old owner name:

```bash
grep -r "OldOwner" projects/*/.git/config
```

## Phase 2: Update Remote URLs

Single repo:
```bash
git remote set-url origin https://github.com/new-owner/repo.git
```

Batch — loop over repos:
```bash
for repo in repo1 repo2 repo3; do
  git -C "projects/$repo" remote set-url origin \
    "https://github.com/new-owner/$repo.git"
done
```

**Heads-up:** If the repo name changed during transfer (e.g. `xamehitv` →
`xamehi`), update both the URL path and the directory name, or set the
new URL on the old local directory.

## Phase 3: Fix Stuck Git State

After an aborted migration or interrupted rebase, repos are often in
detached HEAD with no active branch:

```
## HEAD (no branch)
# or
## HEAD (no branch, rebasing development)
```

### 3a. Abort Rebase

```bash
git rebase --abort
# If it fails with "untracked files would be overwritten", proceed to 3b
```

### 3b. Stash Conflicting Untracked Files

Workspace-injected files (`.vscode/`, `RESEARCH_REPORT.md`, `tech-stack.md`)
are untracked in the repo but block branch checkout because the target
branch has its own versions. Move them aside:

```bash
git stash --include-untracked
# This stashes both tracked modifications and untracked files
```

**Alternative** for larger untracked file sets:
```bash
mkdir -p /tmp/repo-fix
git ls-files --others --exclude-standard | while IFS= read -r f; do
  [ -f "$f" ] && cp "$f" "/tmp/repo-fix/$(basename $f)" 2>/dev/null
done
```

### 3c. Checkout the Target Branch

```bash
git checkout development
# Or: git checkout main / master / production
```

If `git stash --include-untracked` was used, restore the files:
```bash
git stash pop   # restores both stashed tracked changes and untracked files
```

If files were manually copied instead, restore and decide whether to keep
them (workspace docs like tech-stack.md are typically worth keeping and
committing; `.vscode/` settings are machine-local and should be `.gitignore`d).

### 3d. Check Ahead/Behind

```bash
git rev-list --left-right --count origin/development...HEAD
# Output: "N\tM"  where N=ahead (local), M=behind (remote)
```

If behind → pull:
```bash
git pull origin development --ff-only
```

If ahead → push:
```bash
git push origin development
```

## Phase 4: Verify Clean State

```bash
# All repos on named branch, not detached
for d in projects/*/; do
  branch=$(cd "$d" && git branch --show-current 2>/dev/null)
  [ -z "$branch" ] && echo "DETACHED: $d"
done

# No stale remotes
grep -r "old-owner" projects/*/.git/config && echo "STALE FOUND" || echo "CLEAN"
```

## Pitfalls

- **MSYS path rewriting on Git Bash** — Always quote `git` paths and GitHub
  API endpoints. Unquoted `/repos/` gets rewritten to `C:/Program Files/Git/repos/`.
- **`git stash --include-untracked` blocks `stash pop`** — If you stash
  untracked files then create new ones with the same name, `git stash pop`
  will refuse with "would be overwritten." Resolve by deleting or renaming
  the new files first.
- **Case-insensitive directory names** — `projects/Banking` vs `projects/banking`.
  MSYS preserves case; always use the exact path from `ls`.
- **Aborted rebase leaves orphaned commits** — After `git rebase --abort`,
  check `git reflog` for orphaned commits that might hold work worth saving.
  They are NOT pushed to any branch and will be garbage-collected.
