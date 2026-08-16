# Branch Normalization Gotchas (repo-management Phase 1)

Condensed recipe + failure modes discovered while flipping `master` → `production`
as the GitHub default in a monorepo. Pair with the SKILL.md Phase 1 notes.

## Sequence — GitHub refuses to delete the default branch
1. **Confirm scope** (subdir may not be its own repo):
   ```bash
   git rev-parse --show-toplevel
   gh repo view --json name -q .name
   ```
   A dir like `docs/` can be a subdir of a larger repo (e.g. `sandbox`). Branch/default
   ops then affect the WHOLE repo. Operate on the correct `gh` target.
2. **Flip GitHub default FIRST:**
   ```bash
   gh repo edit <owner>/<repo> --default-branch production
   ```
3. **Delete remote master:**
   ```bash
   git push origin --delete master
   ```
4. **Prune:**
   ```bash
   git fetch -p
   ```
5. **Fix stale `origin/HEAD`** (still points at deleted master after the flip):
   ```bash
   git remote set-head origin production
   ```
6. **Delete local master if desired:**
   ```bash
   git branch -D master   # may be flagged destructive / need approval on some hosts
   ```
   Remote delete does NOT require a prior local delete.

## Gotcha: forgetting the order
Deleting `master` while it is the GitHub default fails with a refusal. Always
`--default-branch` before `git push --delete`.

## Gotcha: stale origin/HEAD
After `--default-branch production` + deleting master, `git symbolic-ref
refs/remotes/origin/HEAD` may still report `origin/master`. Run
`git remote set-head origin production` to resync; otherwise downstream
`origin/HEAD` assumptions break.

## Gotcha: subdirectory ≠ repo
`docs/`, `projects/*` are subdirs of the monorepo. Branch/default ops affect the
whole repo. Confirm with `gh repo view --json name` before running `gh` commands.

## Gotcha: dirty monorepo tree
Never `git add -A` to commit a CI file amid unrelated uncommitted changes. Stage
only the intended paths. Snapshot pre-change state in a `PRESTATE_*.md` first.

## Gotcha: stale index.lock
Error `Unable to create '.../.git/index.lock': File exists`. Verify no git
process (`tasklist | grep -i git` / `ps aux | grep '[g]it'`) and check mtime
(`stat -c '%y' .git/index.lock`). If stale, `rm -f .git/index.lock` then retry.
