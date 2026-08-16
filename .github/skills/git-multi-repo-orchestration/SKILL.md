---
name: git-multi-repo-orchestration
title: Git Multi-Repo Orchestration
description: "Use when running git add/commit/push, submodule, and PRs."
version: 1.0.0
author: Alexa
license: MIT
tags: [git, github, submodules, pr, orchestration, multi-repo, workflow]
metadata:
  hermes:
    related_skills:
    - gh-cli
    - git-commit
    - git-helper
    - git-submodule-workflow
    - github-pr-workflow
    - github-repo-management
    - github-code-review
    - finishing-a-development-branch
    - monorepo-pr-workflow
    - workspace-audit
    - repo-management
---

# Git Multi-Repo Orchestration

## Overview

Orchestrate the full git lifecycle across **every repo in `./projects`** (SandBox parent + submodules):
add → commit → push → submodule sync → open/update/close PRs (`gh pr create`, review-then-merge) → merge directly into `development` → sync `development` → `production`. One loop, all repos, full audit trail.

## When to Use

- "sync all repos", "push everything", "update submodules", "run git across ./projects"
- Opening PRs for review-then-merge (never auto-merge without review)
- Merging feature work directly into `development` then pushing
- Syncing `development` → `production` across all project repos

## Skill Bundle — Load FIRST

Load all of these before starting (stacked `/` commands or `skill_view`):

`gh-cli` · `git-commit` · `git-helper` · `git-submodule-workflow` · `github-pr-workflow` · `github-repo-management` · `github-code-review` · `finishing-a-development-branch` · `git-history-preserving-migration` · `monorepo-pr-workflow` · `workspace-audit` · `repo-management`

## Branch Model

| Branch | Role | Writes |
|--------|------|--------|
| `development` | Main work branch | Direct commits + pushes (approved) |
| `production` | Release branch | Only synced FROM development (FF preferred) |
| `feat/*`, `fix/*` | PR branches | PR review-then-merge into development |

## Workflow

### Phase 0: Inventory

```bash
cd ~/Desktop/SandBox
gh auth status   # confirm active account + scopes (repo, workflow)
git submodule status   # all 13 submodules + parent state
# Repo list (exclude docs/artifacts; keep only git dirs)
for d in projects/*/; do [ -d "$d/.git" ] && echo "${d#projects/}"; done
```

**Gate:** record baseline (`git status --short | wc -l` per repo). Do NOT proceed if auth is missing.

### Phase 1: Per-Repo Commit & Push (development)

Loop over each repo, in this order: **changes first, submodule pointers last** (so the parent references final child SHAs).

```bash
cd projects/<repo>
git status --short
git add <files>            # or: git add -A after review of status
git commit -m "type(scope): subject

- bullet detail"
git push origin development   # push current branch if named development
```

- Conventional commit types: `feat`, `fix`, `refactor`, `docs`, `test`, `ci`, `chore`, `perf`.
- If repo is on a feature branch: push branch, open PR (Phase 3), do NOT merge directly.

### Phase 2: Submodule Sync

```bash
# Per-submodule operations (status + fetch first)
git submodule foreach 'git status --short && git fetch origin'
# Update all submodules to their remote development tip
git submodule update --remote development
git submodule sync
# Bump parent pointers (run from SandBox root AFTER child pushes)
git add projects/* && git commit -m "chore(submodules): bump project pointers"
git push origin development
```

**Pitfall:** run Phase 1 child pushes BEFORE the parent pointer commit, or the parent references stale SHAs.

### Phase 3: PR Lifecycle — Review-Then-Merge

Open PRs with `gh pr create` for **review**, not for auto-merge:

```bash
cd projects/<repo>
git checkout -b feat/<description> development
# ... make changes, commit, push
git push -u origin HEAD

gh pr create \
  --title "feat: <description>" \
  --body "## Summary
- <change 1>
- <change 2>

## Test Plan
- [ ] CI green
- [ ] Reviewed" \
  --base development
```

- **Update PR:** `gh pr edit <N> --title ... --body ...`; push more commits to the branch.
- **Review:** `gh pr diff <N>`, `gh pr checks <N> --watch`, request reviewers `gh pr edit <N> --add-reviewer <user>`.
- **Merge after review approved:** `gh pr merge <N> --merge --delete-branch` (or `--squash`). Merge method `--merge` preserves history; `--squash` for clean single-commit history.
- **Close without merge:** `gh pr close <N> --comment "reason"`.
- **After merge:** `git checkout development && git pull origin development`.

**Gate:** do NOT use `--auto` / admin-merge for review-then-merge flow; wait for review.

### Phase 4: Development → Production Sync

```bash
cd projects/<repo>
git checkout production && git pull origin production
git merge --ff-only development   # preferred — fast-forward
git push origin production
git checkout development
```

- If FF fails (diverged): **STOP and ask the user** — force-push (`git push --force origin production`) is destructive and requires explicit approval (record in `.copilot/session-state/` per prior convention).
- After sync, optionally tag: `git tag vX.Y.Z && git push origin vX.Y.Z`.

### Phase 5: Verification

```bash
# Full sweep from SandBox root
for d in projects/*/; do
  [ -d "$d/.git" ] || continue
  cd "$d"
  echo "== ${d#projects/}: $(git branch --show-current) | $(git status --short | wc -l) dirty"
  cd ~/Desktop/SandBox
done
git submodule status | grep -v '^ ' && echo "SUBMODULES DIRTY" || echo "SUBMODULES CLEAN"
gh pr list --state open --limit 50   # confirm expected open PRs only
```

## Safety Gates

1. **No commit/push unless asked** — user approval per repo batch.
2. **No force-push** to `production` without explicit user consent (log it).
3. **No auto-merge** — review-then-merge is the default PR flow.
4. **No branch deletion** without approval.
5. **Destructive git operations** (reset, rebase --force, filter-branch) require a recorded approval under `.hermes/approvals/`.

## Pitfalls

- **Submodule pointer drift** — always push child repos before bumping parent pointers.
- **MSYS path rewriting** — `gh api` endpoints must be double-quoted on git-bash: `gh api "repos/owner/repo"`.
- **Account switching** — org operations may require `gh auth switch --user <org-account>`; switch back after.
- **Unrelated histories** — 12/14 project repos had unrelated dev/prod histories; FF fails → approval-gated force-push was the only clean sync (see `PRODUCTION_FORCE_PUSH_LOG.md`).
- **git-bash + native Python** — use `MSYS_NO_PATHCONV=1` when invoking native Windows Python scripts.
- **Don't commit artifacts** — `.copilot/` (session workspace) is git-ignored; never `git add -A` at SandBox root blindly.

## Verification Checklist

- [ ] Auth verified (`gh auth status`) before first operation
- [ ] Baseline dirty counts recorded per repo
- [ ] Child repo pushes precede parent submodule-pointer commit
- [ ] PRs opened with review-then-merge (no auto-merge)
- [ ] `development` → `production` FF-only unless user approved force-push
- [ ] Final sweep: submodules clean, expected open PRs only
- [ ] Audit trail: commit messages + `.copilot/session-state/` logs

## Related Skills

- `gh-cli` — auth, API, repo transfer/migration
- `github-pr-workflow` — full PR lifecycle (create/checks/merge/close)
- `git-submodule-workflow` — submodule add/update/sync
- `finishing-a-development-branch` — branch finalization steps
- `repo-management` — branch normalization, .gitignore audit, CI setup

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
