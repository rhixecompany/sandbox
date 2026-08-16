# GitHub Pull Request Workflow (absorbed: github-pr-workflow)

Complete guide for managing the PR lifecycle: branch, commit, open, CI, merge,
and close. `gh` way first, then `git` + `curl` fallback.

## Setup

Run the shared setup first (`shared-setup.md` / `scripts/gh-env.sh`): auth
detection + owner/repo extraction.

## 1. Branch Creation

```bash
git fetch origin
git checkout main && git pull origin main
git checkout -b feat/add-user-authentication
```

Branch naming: `feat/`, `fix/`, `refactor/`, `docs/`, `ci/` prefixes.

## 2. Making Commits

```bash
git add src/auth.py src/models/user.py tests/test_auth.py
git commit -m "feat: add JWT-based user authentication

- Add login/register endpoints
- Add User model with password hashing
- Add auth middleware for protected routes
- Add unit tests for auth flow"
```

Conventional Commits: `type(scope): short description`, body wrapped at 72
chars. Types: `feat`, `fix`, `refactor`, `docs`, `test`, `ci`, `chore`, `perf`.
See `references/conventional-commits.md`.

## 3. Pushing and Creating a PR

```bash
git push -u origin HEAD

gh pr create \
  --title "feat: add JWT-based user authentication" \
  --body "## Summary\n- Adds login and register API endpoints\n\nCloses #42" \
  --draft --reviewer user1,user2 --label "enhancement" --base develop
```

curl: `POST /repos/$GH_OWNER/$GH_REPO/pulls` with `{"title","body","head","base","draft":true}`.
The response includes the PR `number` — save it.

## 4. Monitoring CI Status

```bash
gh pr checks                # one-shot
gh pr checks --watch        # poll every 10s
```

curl: `GET /repos/$GH_OWNER/$GH_REPO/commits/$SHA/status` (combined status) and
`GET .../commits/$SHA/check-runs` (Actions runs). Polling loop: check every 30s,
break on success/failure/error.

## 5. Auto-Fixing CI Failures

1. Get failure details: `gh run list --branch <branch> --limit 5` +
   `gh run view <RUN_ID> --log-failed` (curl: download `actions/runs/<id>/logs`
   zip and read the txt files).
2. Fix with `patch`/`write_file`, commit, push.
3. Re-check CI; repeat up to 3 attempts, then ask the user.

Diagnosis by failure signature (test/lint/type/build/permission/timeout/docker):
`references/ci-troubleshooting.md`.

## 6. Merging

```bash
gh pr merge --squash --delete-branch       # cleanest for feature branches
gh pr merge --auto --squash --delete-branch  # auto-merge when checks pass
```

curl: `PUT /repos/$GH_OWNER/$GH_REPO/pulls/$PR_NUMBER/merge` with
`{"merge_method":"squash","commit_title":"feat: ... (#N)"}`, then delete the
remote branch and switch back to main. Auto-merge needs GraphQL
(`enablePullRequestAutoMerge` mutation with the PR node id) — REST doesn't
support it. Merge methods: `merge`, `squash`, `rebase`.

## 7. Complete Workflow Example

```bash
git checkout main && git pull origin main
git checkout -b fix/login-redirect-bug
# (agent makes code changes with file tools)
git add src/auth/login.py tests/test_login.py
git commit -m "fix: correct redirect URL after login"
git push -u origin HEAD
# create PR (gh or curl) → monitor CI → merge when green
```

## Useful Commands Reference

| Action | gh | git + curl |
|--------|-----|-----------|
| List my PRs | `gh pr list --author @me` | `GET /repos/{o}/{r}/pulls?state=open` |
| View PR diff | `gh pr diff` | `git diff main...HEAD` |
| Add comment | `gh pr comment N --body "..."` | `POST .../issues/N/comments` |
| Request review | `gh pr edit N --add-reviewer user` | `POST .../pulls/N/requested_reviewers` |
| Close PR | `gh pr close N` | `PATCH .../pulls/N` `{"state":"closed"}` |
| Check out someone's PR | `gh pr checkout N` | `git fetch origin pull/N/head:pr-N && git checkout pr-N` |
