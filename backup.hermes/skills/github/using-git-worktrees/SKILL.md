---
category: github
title: Using Git Worktrees
name: using-git-worktrees
description: "Use when starting feature work needing isolation from current workspace or before executing implementation plans. Ensures isolated workspace via native tools or git worktree fallback."
---
## Goal
Use when starting feature work needing isolation from current workspace or before executing implementation plans. Ensures isolated workspace via native tools or git worktree fallback.

version: 2.0
updated: 2026-06-01
author: Alexa
---

## Description

Use when starting feature work that needs isolation or when merging diverged repositories. Provides isolation via `git worktree` with patterns for asset-level merging, Windows cleanup, and rollback.

## When to Use

- Starting feature work needing isolation from current workspace
- Before executing implementation plans
- Merging diverged repos with no common ancestor (asset extraction pattern)
- Parallel feature development
- Experimental work isolation
- Bulk asset migration between repos (dotfiles, agent files, CI configs)

## When NOT to Use

- Simple bug fixes
- Quick patches
- Shared workspace work
- True upstream merges (prefer rebase/merge directly)

## Workflow

### Phase 1: Prepare Workspace

- Commit or stash pending changes: `git status` must be clean
- Determine source branch (e.g., `main`) and worktree branch name
- Create the worktree branch:
  ```bash
  git branch feat/merge-task main
  git worktree add ../repo-merge-wt feat/merge-task
  ```

### Phase 2: Asset Identification (Diverged Repo Merge Pattern)

When merging repos with **unrelated histories** (no common ancestor), do NOT attempt `git merge --allow-unrelated-histories` directly — it produces a tangled history. Instead, extract unique assets file-by-file:

1. **Identify unique files** via `diff -rq`:
   ```bash
   cd projects/target-repo
   diff -rq --exclude='.git' ../target/ ../source/ | grep "Only in ../source"
   ```

2. **Classify assets into tiers:**
   | Tier | Type | Merge Rule |
   |------|------|-----------|
   | Root dotfiles | .editorconfig, .gitattributes, .env.example | Copy if absent in target |
   | Agent/instruction files | .github/agents/, .github/instructions/ | Merge: keep target's existing, add unique source files |
   | CI/config | .github/workflows/, .github/dependabot.yml | Copy unique, keep target for conflicts |
   | Source code | src/, lib/ | Keep target (has commit history) unless file absent in target |

3. **Merge agents** (with "if not exists" guard):
   ```bash
   cd worktree/.github/agents
   for f in ../../source-repo/.github/agents/*.md; do
     base=$(basename "$f")
     [ ! -f "$base" ] && cp "$f" .
   done
   ```

4. **Copy tier-1 assets** (unique dotfiles, .github subdirs):
   ```bash
   cp ../source-repo/.editorconfig .
   cp -r ../source-repo/.github/copilot/* .github/copilot/
   ```

5. **Preserve target's authoritative files** — for any file present in both repos, keep the target version (it has commit history). Only take source version if target file is absent or empty.

### Phase 3: Commit & Verify

- Stage and commit in the worktree:
  ```bash
  git add -A
  git commit -m "chore: merge <source> assets into <target>"
  ```
- Verify asset counts (e.g., `ls .github/agents/ | wc -l`), dotfile presence, `.github/` structure
- Run project-specific checks: `npm install && npx tsc --noEmit` or equivalent

### Phase 4: Integrate & Cleanup

1. **Switch to target repo**, merge the worktree branch:
   ```bash
   cd ../target-repo
   git checkout main
   git merge feat/merge-task --no-ff
   ```

2. **Remove the worktree:**
   ```bash
   git worktree remove ../repo-merge-wt
   ```
   > **Windows pitfall**: `git worktree remove` can fail with `Permission denied` due to MSYS2 file locking. Fallback:
   > ```bash
   > rm -rf ../repo-merge-wt   # Works, but leaves .git/worktrees/ entry
   > git worktree prune        # Clean up stale worktree metadata
   > ```

3. **Remove temporary remote** (if added for source access):
   ```bash
   git remote remove source-remote
   ```

4. **Delete the source directory** only after verification:
   ```bash
   rm -rf ../source-repo
   ```

## Pitfalls

### Windows worktree removal fails with Permission denied

**Symptom:** `git worktree remove` exits with `error: failed to delete 'path': Permission denied`

**Root cause:** MSYS2 holds file locks on worktree files. Common after large merge commits.

**Fix:** Delete manually, then prune:
```bash
rm -rf ../worktree-dir
git worktree prune
```
This leaves no stale metadata — `git worktree list` will show clean state.

### Diverged repos with no common ancestor

**Symptom:** `git pull origin main` fails with `fatal: refusing to merge unrelated histories`

**Root cause:** Local repo was initialized independently from remote. They share a name but zero commits in common.

**Fix:** Do NOT force-push — the local state is the authoritative version (has all work + commits). Create `production`/`development` branches from local state and push with `--force` only after confirming the remote is stale/empty.

### "Only in source" shows files that exist in target

**Symptom:** `diff -rq` shows source-only files that you know exist in target.

**Root cause:** The files exist but with different content — `diff -rq` compares both presence AND content. A "Only in source" means the file is absent in target (not present at all), while diff output without "Only in" means files differ.

**Fix:** Use `-q` for speed, but verify by checking file existence before copying.

## References

- `git help worktree` — native documentation
- Related: `using-git-worktrees/references/diverged-repo-merge.md` — full transcript of a real Phase 1a merge (152 files, 32K lines, comicwise_push_clean → comicwise)

## Best Practices

- Create worktree branches from `main` or `production` (stable base)
- Prefer cherry-pick/copy over `--allow-unrelated-histories` for diverged repos
- Keep commit messages descriptive: asset counts, merge rules used
- Verify agent counts before/after merge
- Always use `--no-ff` for worktree merges — preserves branch topology
- One worktree at a time per repo — multiple worktrees on same repo can conflict during checkout
- Clean up immediately after merge — stale worktrees cause confusion

