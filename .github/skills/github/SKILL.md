---
name: github
title: "GitHub Workflow (auth, PRs, code review, issues)"
description: "End-to-end GitHub class: authentication, PR lifecycle (branch/commit/CI/merge), code review, and issue triage — via gh CLI or curl fallback."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [GitHub, Git, gh-cli, PRs, Code-Review, Issues, CI-CD]
---

# GitHub Workflow (umbrella)

Class-level skill covering the full GitHub surface from the agent: **authentication →
PR lifecycle → code review → issue management**. Every section gives the `gh` CLI
path first, then the `git` + `curl` fallback for machines without `gh`.

## Shared prerequisites & auth detection

Authenticate once (see **§1 Auth**). Most commands need `owner/repo` — extract it:

```bash
REMOTE_URL=$(git remote get-url origin)
OWNER_REPO=$(echo "$REMOTE_URL" | sed -E 's|.*github\.com[:/]||; s|\.git$||')
OWNER=$(echo "$OWNER_REPO" | cut -d/ -f1)
REPO=$(echo "$OWNER_REPO"  | cut -d/ -f2)
```

For a one-shot env helper (sets `GH_AUTH_METHOD`, `GITHUB_TOKEN`, `GH_OWNER`,
`GH_REPO`), source `scripts/gh-env.sh`:
```bash
source "${HERMES_HOME:-$HOME/.hermes}/skills/github/scripts/gh-env.sh"
```

---

## 1. Authentication (`github-auth`)

- **`gh` present & authed** → use `gh` for everything (`gh auth login` / `echo $TOKEN | gh auth login --with-token`).
- **git-only (no gh, no sudo)** → HTTPS PAT or SSH:
  - HTTPS PAT: `git config --global credential.helper store` then `git ls-remote https://github.com/<user>/<repo>.git` (enter token as password).
  - SSH: `ssh-keygen -t ed25519 -C "<email>"`; add `~/.ssh/id_ed25519.pub` at github.com/settings/keys; `ssh -T git@github.com`.
- **API without gh**: export `GITHUB_TOKEN`, then `curl -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user`.
  Token can be recovered from `~/.git-credentials` or the Hermes `.env` (`^GITHUB_TOKEN=`).

| Problem | Fix |
|---------|-----|
| `git push` asks for password | Use a PAT as password, or switch to SSH |
| `fatal: Authentication failed` | `git credential reject` then re-auth |
| SSH port 22 blocked | Add `Host github.com / Port 443 / Hostname ssh.github.com` to `~/.ssh/config` |

---

## 2. Pull Request Lifecycle (`github-pr-workflow`)

### Branch → commit → push
```bash
git fetch origin && git checkout main && git pull origin main
git checkout -b feat/add-auth
# ... edit with write_file/patch ...
git add src/auth.py tests/test_auth.py
git commit -m "feat: add JWT-based user authentication

- Add login/register endpoints
- Add User model with password hashing
- Closes #42"
git push -u origin HEAD
```
Conventional-commit types: `feat fix refactor docs test ci chore perf style build revert`
(full guide in `references/conventional-commits.md`).

### Open the PR
```bash
# gh
gh pr create --title "feat: add JWT auth" --body "$(cat templates/pr-body-feature.md)"
# curl
curl -s -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls \
  -d "{\"title\":\"feat: add JWT auth\",\"head\":\"$(git branch --show-current)\",\"base\":\"main\"}"
```

### Monitor CI
```bash
gh pr checks                 # or: gh pr checks --watch
# curl: GET /repos/$OWNER/$REPO/commits/$(git rev-parse HEAD)/status
# + /check-runs for GitHub Actions
```
CI failure diagnosis (logs, common patterns, auto-fix loop) → `references/ci-troubleshooting.md`.

### Merge
```bash
gh pr merge --squash --delete-branch          # or: --auto for auto-merge
# curl: PUT /repos/$OWNER/$REPO/pulls/$N/merge  {"merge_method":"squash"}
```
Branch naming: `feat/`, `fix/`, `refactor/`, `docs/`, `ci/`. PR body templates:
`templates/pr-body-feature.md`, `templates/pr-body-bugfix.md`.

---

## 3. Code Review (`github-code-review`)

### Local pre-push review (pure git)
```bash
git diff main...HEAD --stat
git diff main...HEAD | grep -in "password\|secret\|api_key\|TODO\|FIXME\|debugger"
git diff main...HEAD | grep -n "<<<<<<\|>>>>>>\|======"
```
### Review a PR on GitHub
```bash
gh pr view 123 && gh pr diff 123
git fetch origin pull/123/head:pr-123 && git checkout pr-123   # full local context
gh pr review 123 --request-changes --body "See inline comments."
```
Inline comments & atomic multi-comment reviews via `gh api` or `curl` to
`/repos/$OWNER/$REPO/pulls/$N/comments` and `/reviews`.

**Review checklist** (systematically): Correctness · Security (no hardcoded secrets,
no injection) · Code Quality (DRY, naming) · Testing · Performance · Documentation.

Summary-comment template (severity-graded) → `references/review-output-template.md`.

---

## 4. Issues (`github-issues`)

```bash
gh issue list --label "bug" --state open
gh issue create --title "..." --body "$(cat ../github/templates/bug-report.md)" --label "bug,backend"
gh issue edit 42 --add-label "priority:high" --add-assignee @me
gh issue close 42 --reason "not planned"
```
Templates: `templates/bug-report.md`, `templates/feature-request.md`.
Triage loop: list untriaged → read → label/priority → assign → comment.

Quick-reference tables for `gh` vs `curl` endpoints live in the original
per-topic skills (now consolidated here); the patterns above cover the common cases.

---

## See also
- `systematic-debugging` — root-cause methodology before you fix CI/build failures
- `github-repo-management` — clone/fork/release repo administration
