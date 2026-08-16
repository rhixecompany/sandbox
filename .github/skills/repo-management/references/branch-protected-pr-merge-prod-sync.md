# Branch-Protected PR Merge & Development→Production Sync

Battle-tested sequence for: open PR → merge feature branch into `development` →
sync `development` → `production` → cleanup, across a parent repo + all
`projects/**` submodules. Verified 2026-07-31 on `rhixecompany/sandbox` (PR #9).

## 1. Open the PR

```bash
gh pr create --repo <owner>/<repo> \
  --base development --head <feature-branch> \
  --title "..." --body "$(cat <<'EOF'
...markdown body, include verification evidence...
EOF
)"
```

## 2. Merge — branch protection WILL block a naive `gh pr merge`

Symptom:
```
X Pull request <owner>/<repo>#N is not mergeable: the base branch policy prohibits the merge.
```

Root cause: `development` branch protection lists required status checks
(e.g. `lint-and-test`) that do NOT match the workflow's actual check names
(e.g. `Validate PR`, `build`, `PR Summary`, `Root checks`), and requires
`required_pull_request_reviews=1` while reviews are disabled for the base
branch. The PR can never satisfy the stated policy → blocked forever.

Procedure:
1. Read the protection: `gh api repos/<owner>/<repo>/branches/development/protection --jq '{required_checks: .required_status_checks.contexts, required_reviews: .required_pull_request_reviews.required_approving_review_count}'`
2. Wait for ACTUAL checks to finish: poll `gh pr checks <N>` until no
   `pending`/`in_progress` remain (loop with `sleep 15`).
3. Confirm every real check passed.
4. Merge with admin override (explicit user approval required — destructive-op
   rule): `gh pr merge <N> --merge --admin`
5. Verify: `gh pr view <N> --json state,mergedAt,mergeCommit --jq '{state, mergedAt, mergeCommit: .mergeCommit.oid}'` → expect `MERGED`.

Alternative if the user wants policy-compliant merges in the future: enable
reviews on the base branch OR align protection check names to the real workflow
jobs.

## 3. Sync development → production

Fast path (production unprotected, no divergence): push the refspec directly —
this AVOIDS the local submodule descent problem in step 4 entirely:

```bash
git push origin development:production
git fetch origin production:production   # sync local ref
# verify: both rev-list counts == 0
git rev-list --count origin/production..origin/development
git rev-list --count origin/development..origin/production
```

## 4. Pitfall: parent branch switch fails on submodule gitlink conflicts

Symptom (only when production's gitlinks point to OLDER submodule commits):
```
git checkout production
error: The following untracked working tree files would be overwritten by checkout:
    projects/Banking/.all-contributorsrc
    projects/Banking/.claude/skills/... (hundreds of files)
Aborting
```

Why: the target branch's gitlink for a submodule points to a commit whose
tracked files exist as UNTRACKED files in the current submodule working tree
(e.g. agent-injected `.claude/skills`, font assets). Git descends into the
submodule during checkout and refuses to overwrite them.

`git -c submodule.recurse=false checkout production` does NOT help — git still
descends to reconcile the gitlink change.

Fixes (pick by situation):
- **Refspec push (preferred when production is unprotected and a clean FF):**
  `git push origin development:production` from the current branch. No local
  checkout of the old tree, no submodule descent. Verify with rev-list counts.
- **Local merge when a checkout is truly needed:** `git submodule deinit -f <name>`
  for the conflicting submodules, checkout, merge, then
  `git submodule update --init --recursive` to restore. (Restores from
  `.git/modules`, fast.)

## 5. Unrelated dev/prod histories in submodules

After a repo migration, `development` (workspace snapshot, few commits) and
`production` (legacy original history, many commits) can share NO merge base:

```bash
git merge-base origin/development origin/production   # EMPTY output = unrelated
```

Check the default branch first: `gh repo view <owner>/<repo> --json defaultBranchRef --jq .defaultBranchRef.name`.
Production is usually the default and holds the legacy history.

Options (present to user with trade-offs; never pick silently):
- Leave production untouched (safest — parent gitlinks track development).
- Force-push development → production (destructive: orphans legacy history;
  survives in reflog/GitHub objects until GC).
- `--allow-unrelated-histories` merge (giant merge commits; on Banking-sized
  repos this was 398 files changed / 37,397 deletions).
- Archive legacy first: capture SHAs, then force.

**If force-push is approved**, ALWAYS capture legacy SHAs first to a recovery
log (e.g. `.copilot/session-state/PRODUCTION_FORCE_PUSH_LOG.md`):

```bash
git -C projects/<name> push --force origin origin/development:refs/heads/production
# expected: "+ <legacy>...<dev> origin/development -> production (forced update)"
```

Verify per repo: `dev-ahead=0 prod-ahead=0 dirty=0` (fetch first).

## 6. Final verification gate

- All submodules: `git -C projects/<name> fetch origin --quiet && rev-list --count origin/production..origin/development` = 0 AND reverse = 0 AND `status --porcelain` = 0.
- Parent: on `development`, synced with `production` (0/0), tree clean.
- PR state MERGED; feature branch deleted local + remote
  (`git push origin --delete <branch>`).
- Note: dependabot PRs on submodules are automated — leave untouched unless the
  user asks.
