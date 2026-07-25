---
name: git-helper
title: "Git Helper"
description: "Use when managing git branches, writing commit messages, resolving merge conflicts, planning git workflows, or optimizing commit history."
version: 1.0.0
author: Alexa
license: MIT
tags: [imported]
---
## Goal
Use when managing git branches, writing commit messages, resolving merge conflicts, planning git workflows, or optimizing commit history.




## Description

Git workflow assistance for branch management, commit message optimization, and version control best practices.

## When to Use

- Creating or managing git branches
- Writing commit messages
- Resolving merge conflicts
- Planning git workflow
- Optimizing commit history
- Managing multiple branches

## When NOT to Use

- Non-git version control systems
- Simple file operations
- Real-time collaboration tools
- Distributed systems beyond git

## Mass Remote Migration (multi-project)

Use when moving N repos between GitHub accounts (e.g., `Rhixe-company/*` → `rhixecompany/*`). Batch-iterate all project dirs.

### Step-by-step

```bash
# 1. Inventory all current remotes
for d in projects/*/; do
  [ ! -f "$d.git/config" ] && continue
  remote=$(grep -A2 'remote "origin"' "$d/.git/config" 2>/dev/null | grep url)
  echo "$(basename $d) → $remote"
done

# 2. Update all remotes with sed (old org → new user)
for d in projects/*/; do
  [ ! -f "$d/.git/config" ] && continue
  git -C "$d" remote set-url origin \
    $(git -C "$d" remote get-url origin | sed 's|Rhixe-company|rhixecompany|')
done

# 3. Verify no stale remotes remain
grep -r "Rhixe-company" projects/*/.git/config && echo "STALE FOUND" || echo "ALL CLEAN"
```

### Pitfalls

- **`gh repo list` is unreliable** — may show only 1 of 14 repos. Use `gh api users/<user>/repos --paginate --jq '.[].name'` instead for full inventory.
- **Remote URL pattern precision** — ensure sed replaces the full org prefix, not partial matches. Use `s|<old-org>|<new-org>|g` with the full repo URL path.
- **Rebase state after migration** — repos migrated mid-rebase land in detached HEAD. See "Stuck Rebase Recovery" below.

## Branch Normalization (multi-project)

Use when a workspace has messy branch history (main, master, audit/*, dependabot/*, feat/*) and needs normalization to a clean `development` / `production` pair.

### Strategy

- `production` = renamed from `main` or `master`; set as GitHub default branch
- `development` = branched from `production`; active checkout; synced via rebase
- All other branches: hard-deleted locally and remotely

### Step-by-step

```bash
# 0. Detect prior state — check if normalization is already partially done
LOCAL_COUNT=$(git -C projects/<name> branch | wc -l)
REMOTE_COUNT=$(git -C projects/<name> branch -r | grep -v HEAD | wc -l)
if [ "$LOCAL_COUNT" = "2" ] && [ "$REMOTE_COUNT" = "0" ]; then
  echo "PARTIAL: local production/development exist, need to push"
  git -C projects/<name> push origin production
  git -C projects/<name> push origin development
  # Set default branch (extract owner from remote)
  REMOTE_URL=$(git -C projects/<name> remote get-url origin)
  OWNER_REPO=$(echo "$REMOTE_URL" | sed -E 's|.*github\\.com[:/]||; s|\\.git$||')
  gh api repos/$OWNER_REPO -X PATCH -f default_branch=production
  git -C projects/<name> checkout development
  git -C projects/<name> branch -a
  exit 0
fi

# 1. Identify source branch (main or master, whichever exists)
git -C projects/<name> branch -a

# 2. Create production from source
git -C projects/<name> checkout <source>
git -C projects/<name> pull origin <source>
git -C projects/<name> checkout -b production
git -C projects/<name> push origin production

# 3. Set production as GitHub default via API
# NOTE: Extract owner from remote — works for both org and user repos
REMOTE_URL=$(git -C projects/<name> remote get-url origin)
OWNER_REPO=$(echo "$REMOTE_URL" | sed -E 's|.*github\\.com[:/]||; s|\\.git$||')
gh api repos/$OWNER_REPO -X PATCH -f default_branch=production

# 4. Create development from production
git -C projects/<name> checkout -b development
git -C projects/<name> push origin development

# 5. Delete all other remote branches (except production and development)
git -C projects/<name> branch -r | grep -v 'production\|development\|HEAD' \
  | sed 's|origin/||' | xargs -I{} git push origin --delete {}

# 6. Delete all other local branches (except production and development)
git -C projects/<name> branch | grep -v 'production\|development' \
  | xargs git -C projects/<name> branch -D

# 7. Checkout development (active branch)
git -C projects/<name> checkout development

# 8. Verify: expect 2 local, 2 remote
git -C projects/<name> branch -a
```

### Verification gate

```bash
LOCAL=$(git -C projects/<name> branch | wc -l)
REMOTE=$(git -C projects/<name> branch -r | grep -v HEAD | wc -l)
# Expect LOCAL=2, REMOTE=2
```

### Pitfalls

- **Never delete the remote default branch** — set `production` as GitHub default before deleting `main`/`master`, or the push will be rejected.
- **dependabot/* branches**: safe to delete unconditionally — regenerated by GitHub automatically.
- **Per-project source branch**: most projects use `main`; some use `master` only. Check each before assuming.
- **Partial normalization**: Local `production`/`development` branches may exist but never be pushed. The verification gate (LOCAL=2, REMOTE=2) catches this. Recovery: `git push origin production && git push origin development && gh api repos/<owner>/<name> -X PATCH -f default_branch=production`.
- **Cross-org default branch set**: The `gh api repos/Org-here/<name>` pattern only works for org repos. For user repos (github.com/users), the API path is `repos/<username>/<name>`. Extract dynamically: `OWNER=$(git remote get-url origin | sed -E 's|.*github\\\\.com[:/]||; s|/.*||')`.
- **Push `production` before setting as default** — `gh api repos/... -X PATCH -f default_branch=production` fails with HTTP 422 if `production` hasn't been pushed. Always push first: `git push origin production && gh api repos/... -X PATCH -f default_branch=production`.
- **Stuck rebase recovery** — Repos stuck in detached HEAD (`(no branch, rebasing development)`) block normalization. Recovery: `git stash --include-untracked && git rebase --abort 2>/dev/null || git checkout development 2>/dev/null`.
- **Untracked workspace files block checkout** — Files like `RESEARCH_REPORT.md`, `tech-stack.md` injected by tools prevent branch switch. Move aside with: `git stash --include-untracked`, checkout, then `git stash pop`.
- **Batch verification across repos**: After normalizing, run a global check:
  ```bash
  for dir in projects/*/; do
    name=$(basename "$dir")
    if [ -d "$dir/.git" ]; then
      local_b=$(git -C "$dir" branch | wc -l)
      remote_b=$(git -C "$dir" branch -r | grep -v HEAD | wc -l)
      default=$(git -C "$dir" remote show origin 2>/dev/null | grep "HEAD branch" | awk '{print $NF}')
      echo "$name: LOCAL=$local_b REMOTE=$remote_b DEFAULT=$default"
    fi
  done
  ```
- See `references/branch-normalization-inventory.md` for a per-project source branch map.

## Workflow

### Phase 1: Plan Workflow

- Determine branching strategy
- Identify main and feature branches
- Plan commit structure

### Phase 2: Create & Manage Branches

- Create feature branches
- Keep branches up to date
- Manage branch lifecycle

### Phase 3: Commit & Message

- Write clear commit messages
- Follow commit conventions
- Organize commits logically

### Phase 4: Merge & Cleanup

- Resolve conflicts if needed
- Merge to main branch
- Clean up feature branches

## Tools & References

- **Related Skills**: finishing-a-development-branch, requesting-code-review
- **Git Commands**: branch, commit, merge, rebase
- **Commit Format**: Conventional Commits

## Best Practices

- Use descriptive branch names
- Write clear commit messages
- Keep commits atomic and focused
- Rebase before merging
- Delete merged branches
- Use meaningful tags
- Document workflow for team


## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

