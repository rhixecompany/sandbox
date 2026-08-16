# GitHub Code Review (absorbed: github-code-review)

Review local changes before pushing, or review open PRs on GitHub. Most of this
uses plain `git` — the `gh`/`curl` split only matters for PR-level interactions.

## 1. Reviewing Local Changes (Pre-Push)

```bash
git diff --staged                          # staged changes
git diff main...HEAD                       # all changes vs main
git diff main...HEAD --name-only           # file names only
git diff main...HEAD --stat                # insertion/deletion summary
git log main..HEAD --oneline               # commits in the branch
```

Review strategy:
1. Big picture first (`--stat`, `--oneline`).
2. Review file by file — `read_file` the changed files for context, the diff for changes.
3. Scan for common issues:
   ```bash
   git diff main...HEAD | grep -n "print(\|console\.log\|TODO\|FIXME\|HACK\|XXX\|debugger"
   git diff main...HEAD --stat | sort -t'|' -k2 -rn | head -10       # large files
   git diff main...HEAD | grep -in "password\|secret\|api_key\|token.*=\|private_key"  # secrets
   git diff main...HEAD | grep -n "<<<<<<\|>>>>>>\|======="            # conflict markers
   ```
4. Present findings as Critical / Warnings / Suggestions / Looks Good.

## 2. Reviewing a Pull Request on GitHub

```bash
gh pr view 123
gh pr diff 123
gh pr diff 123 --name-only
gh pr checkout 123                          # check out locally for full review
```

curl: `GET .../pulls/$PR_NUMBER` (metadata) and `GET .../pulls/$PR_NUMBER/files`
(changed files with add/delete counts). Local checkout without gh:
`git fetch origin pull/123/head:pr-123 && git checkout pr-123`.

### Leave Comments

```bash
gh pr comment 123 --body "Overall looks good, a few suggestions below."
```

Inline comment (gh api):
```bash
HEAD_SHA=$(gh pr view 123 --json headRefOid --jq '.headRefOid')
gh api repos/$GH_OWNER/$GH_REPO/pulls/123/comments --method POST \
  -f body="This could be simplified with a list comprehension." \
  -f path="src/auth/login.py" -f commit_id="$HEAD_SHA" -f line=45 -f side="RIGHT"
```

### Submit a Formal Review (Approve / Request Changes)

```bash
gh pr review 123 --approve --body "LGTM!"
gh pr review 123 --request-changes --body "See inline comments."
gh pr review 123 --comment --body "Some suggestions, nothing blocking."
```

curl — atomic multi-comment review:
`POST .../pulls/$PR_NUMBER/reviews` with `{"commit_id","event":"APPROVE|REQUEST_CHANGES|COMMENT","comments":[{"path","line","side","body"}]}`.
`line` refers to the NEW version of the file; deleted lines use `"side": "LEFT"`.

### Step 8: Post a summary comment

Leave a top-level summary in addition to inline comments, using the structure
from `references/review-output-template.md`.

## 3. Review Checklist

- **Correctness:** does it do what it claims; edge cases (empty, null, large,
  concurrent); error paths handled.
- **Security:** no hardcoded secrets/credentials/API keys; input validation; no
  SQL injection/XSS/path traversal; auth/authz where needed.
- **Code Quality:** clear naming; no unnecessary complexity; DRY; focused functions.
- **Testing:** new code paths tested; happy path and error cases; readable tests.
- **Performance:** no N+1 queries; caching where beneficial; no blocking ops in async code.
- **Documentation:** public APIs documented; non-obvious logic commented; README updated.

## 4. End-to-End PR Review Recipe

1. Set up env (`scripts/gh-env.sh`).
2. Gather PR context: `gh pr view 123`, `gh pr diff 123 --name-only`, `gh pr checks 123`.
3. Check out the PR locally (`gh pr checkout 123`).
4. Read the diff; `read_file` around changes for context.
5. Run automated checks locally (pytest/npm test/go test; ruff/eslint).
6. Apply the checklist (section 3).
7. Post the review (approve / request-changes with inline comments).
8. Post a summary comment.
9. Clean up: `git checkout main && git branch -D pr-123`.

**Decision:** Approve = no critical/warning issues. Request Changes = any
critical or warning issue. Comment = observations only (drafts, uncertainty).
