---
name: github
title: "GitHub Workflow"
description: "Complete GitHub workflow: auth, repos, issues, PRs, code review, CI/CD — via gh CLI or git+curl"
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [imported]
metadata:
  hermes:
    tags: [imported]
---
# GitHub Workflow

Complete guide for GitHub operations — authentication, repositories, issues, pull requests, code reviews, and CI/CD. Every section shows the `gh` CLI way first, then the `git` + `curl` fallback for machines without `gh`.

## Prerequisites

- Inside a git repository with a GitHub remote (for most operations)
- GitHub authentication configured (see **Authentication** section below)

### Quick Auth Detection — Run Once Per Session

```bash
# Determine which method to use
if command -v gh &>/dev/null && gh auth status &>/dev/null; then
  AUTH="gh"
else
  AUTH="git"
  # Ensure we have a token for API calls
  if [ -z "$GITHUB_TOKEN" ]; then
    if [ -f ~/.hermes/.env ] && grep -q "^GITHUB_TOKEN=" ~/.hermes/.env; then
      GITHUB_TOKEN=$(grep "^GITHUB_TOKEN=" ~/.hermes/.env | head -1 | cut -d= -f2 | tr -d '\n\r')
    elif grep -q "github.com" ~/.git-credentials 2>/dev/null; then
      GITHUB_TOKEN=$(grep "github.com" ~/.git-credentials 2>/dev/null | head -1 | sed 's|https://[^:]*:\\([^@]*\\)@.*|\\1|')
    fi
  fi
fi
echo "Using: $AUTH"
```

### Extract Owner/Repo from Git Remote

```bash
# Works for both HTTPS and SSH remote URLs
REMOTE_URL=$(git remote get-url origin)
OWNER_REPO=$(echo "$REMOTE_URL" | sed -E 's|.*github\\.com[:/]||; s|\\.git$||')
OWNER=$(echo "$OWNER_REPO" | cut -d/ -f1)
REPO=$(echo "$OWNER_REPO" | cut -d/ -f2)
echo "Owner: $OWNER, Repo: $REPO"
```

---

## 1. Authentication

### Method 1: Git-Only (No gh, No sudo)

**Option A: HTTPS with Personal Access Token (Recommended)**

```bash
# 1. Create token at https://github.com/settings/tokens (classic)
#    Scopes: repo, workflow, read:org
# 2. Configure git credential helper
git config --global credential.helper store
# 3. Test — git will prompt once, then cache
git ls-remote https://github.com/<username>/<any-repo>.git
#    Username: <github-username>
#    Password: <paste-token>
# 4. Set git identity
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

**Option B: SSH Key**

```bash
# Generate key
ssh-keygen -t ed25519 -C "you@example.com" -f ~/.ssh/id_ed25519 -N ""
cat ~/.ssh/id_ed25519.pub  # Add to https://github.com/settings/keys
# Test
ssh -T git@github.com
# Configure git to use SSH for GitHub
git config --global url."git@github.com:".insteadOf "https://github.com/"
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

### Method 2: gh CLI

```bash
# Interactive (desktop)
gh auth login

# Token-based (headless)
echo "<TOKEN>" | gh auth login --with-token
gh auth setup-git

# Verify
gh auth status
```

### API Access Without gh

```bash
export GITHUB_TOKEN="<token>"
curl -s -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/user
```

---

## 2. Repository Management

### Clone

```bash
# Git
git clone https://github.com/owner/repo.git
git clone --depth 1 https://github.com/owner/repo.git  # shallow

# gh
gh repo clone owner/repo
```

### Create

```bash
# gh
gh repo create my-project --public --clone
gh repo create my-project --private --description "Desc" --license MIT --clone
gh repo create org/project --public --clone

# curl
curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/user/repos \
  -d '{"name":"my-project","private":false,"auto_init":true,"license_template":"mit"}'
```

### Fork & Sync

```bash
# gh
gh repo fork owner/repo --clone

# git
curl -X POST -H "Authorization: token $GITHUB_TOKEN" https://api.github.com/repos/owner/repo/forks
git clone https://github.com/$GH_USER/repo.git
cd repo && git remote add upstream https://github.com/owner/repo.git

# Sync fork
git fetch upstream && git checkout main && git merge upstream/main && git push origin main
```

### Settings, Secrets, Releases, Actions

```bash
# Settings
gh repo edit --description "New" --visibility public
gh repo edit --enable-wiki=false --add-topic "tag1,tag2"

# Secrets (gh is dramatically simpler)
gh secret set API_KEY --body "value"
gh secret list

# Releases
gh release create v1.0.0 --generate-notes
gh release create v1.0.0 ./dist/binary --notes "Notes"

# Actions
gh workflow list
gh run list --limit 10
gh run view <RUN_ID> --log-failed
gh run rerun <RUN_ID> --failed
gh workflow run ci.yml --ref main
```

---

## 3. Issues

### View & Search

```bash
# gh
gh issue list --state open --label bug
gh issue view 42

# curl
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  "https://api.github.com/repos/$OWNER/$REPO/issues?state=open&per_page=20" | \
  python3 -c "import sys,json; [print(f\"#{i['number']} {i['title']}\") for i in json.load(sys.stdin) if 'pull_request' not in i]"
```

### Create

```bash
# gh
gh issue create --title "Bug: login redirect" --body "## Steps\n1...\n## Expected\n..." --label bug,backend

# curl
curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/issues \
  -d '{"title":"Bug: login redirect","body":"## Steps\n1...\n## Expected\n...","labels":["bug","backend"]}'
```

### Manage (Labels, Assignees, Comments, Close)

```bash
# Labels
gh issue edit 42 --add-label "priority:high"
gh issue edit 42 --remove-label "needs-triage"

# Assign
gh issue edit 42 --add-assignee @me

# Comment
gh issue comment 42 --body "Investigating..."

# Close/Reopen
gh issue close 42 --reason "completed"
gh issue reopen 42
```

### Triage Workflow

1. List untriaged: `gh issue list --label needs-triage`
2. Read each issue
3. Apply labels/priority
4. Assign if owner clear
5. Comment with triage notes

---

## 4. Pull Request Workflow

### Branch & Commit

```bash
git fetch origin
git checkout main && git pull origin main
git checkout -b feat/description  # feat/, fix/, refactor/, docs/, ci/
# ... make changes with file tools ...
git add <files>
git commit -m "feat: short description

Longer explanation. Closes #42"
```

### Push & Create PR

```bash
git push -u origin HEAD

# gh
gh pr create --title "feat: ..." --body "## Summary\n...\nCloses #42" --label enhancement

# curl
BRANCH=$(git branch --show-current)
curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls \
  -d "{\"title\":\"feat: ...\",\"body\":\"## Summary\n...\nCloses #42\",\"head\":\"$BRANCH\",\"base\":\"main\"}"
```

### Monitor CI

```bash
# gh
gh pr checks --watch

# curl (poll)
SHA=$(git rev-parse HEAD)
for i in {1..20}; do
  STATUS=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
    https://api.github.com/repos/$OWNER/$REPO/commits/$SHA/status | \
    python3 -c "import sys,json; print(json.load(sys.stdin)['state'])")
  echo "Check $i: $STATUS"
  [[ "$STATUS" =~ ^(success|failure|error)$ ]] && break
  sleep 30
done
```

### Auto-Fix CI Failures

```bash
# 1. Get failure details
gh run list --branch $(git branch --show-current) --limit 5
gh run view <RUN_ID> --log-failed

# 2. Fix code with file tools
# 3. Commit & push
git add . && git commit -m "fix: resolve CI failure" && git push
# 4. Re-check (repeat up to 3 times)
```

### Merge

```bash
# gh
gh pr merge --squash --delete-branch
gh pr merge --auto --squash --delete-branch

# curl
curl -X PUT -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls/$PR_NUMBER/merge \
  -d '{"merge_method":"squash","commit_title":"feat: ... (#'$PR_NUMBER')"}'
git push origin --delete $BRANCH
git checkout main && git pull && git branch -d $BRANCH
```

---

## 5. Code Review

### Local Changes (Pre-Push)

```bash
# Scope
git diff main...HEAD --stat
git log main..HEAD --oneline

# Full diff
git diff main...HEAD

# Check for issues
git diff main...HEAD | grep -n "print(\|console\.log\|TODO\|FIXME\|HACK\|debugger"
git diff main...HEAD | grep -in "password\|secret\|api_key\|private_key"
```

### Review PR on GitHub

```bash
# View PR
gh pr view 123
gh pr diff 123 --name-only

# Check out locally
git fetch origin pull/123/head:pr-123
git checkout pr-123
git diff main...pr-123
```

### Submit Review (Inline Comments + Formal Review)

```bash
# Inline comment (gh)
HEAD_SHA=$(gh pr view 123 --json headRefOid --jq '.headRefOid')
gh api repos/$OWNER/$REPO/pulls/123/comments \
  --method POST \
  -f body="Use parameterized queries" \
  -f path="src/auth.py" -f commit_id="$HEAD_SHA" -f line=45 -f side="RIGHT"

# Formal review (gh)
gh pr review 123 --approve --body "LGTM!"
gh pr review 123 --request-changes --body "See comments."

# Formal review with multiple inline comments (curl — atomic)
HEAD_SHA=$(curl -s -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls/123 | \
  python3 -c "import sys,json; print(json.load(sys.stdin)['head']['sha'])")

curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/$OWNER/$REPO/pulls/123/reviews \
  -d "{
    \"commit_id\": \"$HEAD_SHA\",
    \"event\": \"REQUEST_CHANGES\",
    \"body\": \"## Review\n\nFound issues. See inline.\",
    \"comments\": [
      {\"path\": \"src/auth.py\", \"line\": 45, \"body\": \"🔴 **Critical:** SQL injection risk.\"},
      {\"path\": \"src/models.py\", \"line\": 23, \"body\": \"⚠️ **Warning:** Plaintext password.\"}
    ]
  }"
```

### Review Checklist

| Category | Checks |
|----------|--------|
| **Correctness** | Does it work? Edge cases? Error handling? |
| **Security** | No secrets? Input validation? No injection? Auth checks? |
| **Quality** | Clear naming? No duplication? Focused functions? |
| **Testing** | New paths tested? Happy + error cases? |
| **Performance** | No N+1? Caching? No blocking in async? |
| **Documentation** | Public APIs documented? Non-obvious logic explained? |

---

## Quick Reference

| Action | gh | git + curl |
|--------|-----|-----------|
| Auth status | `gh auth status` | Check `GITHUB_TOKEN` / `~/.git-credentials` |
| Clone | `gh repo clone o/r` | `git clone https://github.com/o/r.git` |
| Create repo | `gh repo create n --public` | `curl POST /user/repos` |
| Fork | `gh repo fork o/r --clone` | `curl POST /repos/o/r/forks` + clone |
| List issues | `gh issue list` | `GET /repos/o/r/issues` |
| Create issue | `gh issue create ...` | `POST /repos/o/r/issues` |
| View PR | `gh pr view N` | `GET /repos/o/r/pulls/N` |
| Create PR | `gh pr create ...` | `POST /repos/o/r/pulls` |
| PR diff | `gh pr diff` | `git diff main...HEAD` |
| Check CI | `gh pr checks` | `GET /repos/o/r/commits/SHA/status` |
| Merge PR | `gh pr merge --squash` | `PUT /repos/o/r/pulls/N/merge` |
| Review PR | `gh pr review N --approve` | `POST /repos/o/r/pulls/N/reviews` |
| List workflows | `gh workflow list` | `GET /repos/o/r/actions/workflows` |
| Rerun CI | `gh run rerun ID` | `POST /repos/o/r/actions/runs/ID/rerun` |
| Set secret | `gh secret set KEY` | `PUT /repos/o/r/actions/secrets/KEY` |

---

## When to Use

- Any GitHub repository, issue, PR, or CI/CD task
- When you need to automate GitHub workflows from the terminal
- When `gh` is unavailable — every operation has a `git` + `curl` fallback
- **Triggers**: "GitHub", "PR", "issue", "repo", "CI", "code review"

---

## Workflow Phases

### Phase 1: Setup
Verify prerequisites and configure authentication.

### Phase 2: Execute
Perform the GitHub operations following the patterns above.

### Phase 3: Verify
Check outputs against expected results (PR merged, issue closed, CI green).

### Phase 4: Cleanup
Document outcomes, clean up temp branches, update local main.
## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

