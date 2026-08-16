# GitHub Issues Management (absorbed: github-issues)

Create, search, triage, and manage GitHub issues. `gh` first, then `curl` fallback.

## Setup

Run the shared setup first (see `shared-setup.md` / `scripts/gh-env.sh`): detect
auth method, export the token, resolve owner/repo.

## 1. Viewing Issues

```bash
gh issue list
gh issue list --state open --label "bug"
gh issue list --assignee @me
gh issue list --search "authentication error" --state all
gh issue view 42
```

curl: `GET /repos/$GH_OWNER/$GH_REPO/issues?state=open&per_page=20` — filter out
PRs with `'pull_request' not in i` (GitHub returns PRs in `/issues`); filter by
label with `&labels=bug`; search via `GET /search/issues?q=...`.

## 2. Creating Issues

```bash
gh issue create --title "Login redirect ignores ?next= parameter" \
  --body "## Description\n...\n## Steps to Reproduce\n1...\n## Expected Behavior\n..." \
  --label "bug,backend" --assignee "username"
```

curl: `POST /repos/$GH_OWNER/$GH_REPO/issues` with `{"title", "body", "labels", "assignees"}`.
Templates: `templates/bug-report.md`, `templates/feature-request.md`.

## 3. Managing Issues

```bash
gh issue edit 42 --add-label "priority:high,bug"     # / --remove-label "needs-triage"
gh issue edit 42 --add-assignee username             # or @me
gh issue comment 42 --body "Investigated — root cause is in auth middleware."
gh issue close 42 --reason "not planned"             # reasons: completed, not planned, ...
gh issue reopen 42
```

curl equivalents: `POST .../issues/N/labels`, `DELETE .../issues/N/labels/<name>`,
`GET .../labels`, `POST .../issues/N/assignees`, `POST .../issues/N/comments`,
`PATCH .../issues/N` with `{"state":"closed","state_reason":"completed"}` /
`{"state":"open"}`.

**Linking issues to PRs:** PR bodies containing `Closes #42` / `Fixes #42` /
`Resolves #42` auto-close the issue on merge. Branch from an issue:
`gh issue develop 42 --checkout`.

## 4. Issue Triage Workflow

1. List untriaged: `gh issue list --label "needs-triage" --state open`
2. Read and categorize each (view details, understand bug/feature)
3. Apply labels and priority
4. Assign if the owner is clear
5. Comment with triage notes

## 5. Bulk Operations

```bash
# Close all issues with a label (gh)
gh issue list --label "wontfix" --json number --jq '.[].number' | \
  xargs -I {} gh issue close {} --reason "not planned"
```

curl: loop `GET .../issues?labels=wontfix&state=open` → `PATCH .../issues/N`.

## Quick Reference

| Action | gh | curl endpoint |
|--------|-----|--------------|
| List issues | `gh issue list` | `GET /repos/{o}/{r}/issues` |
| View issue | `gh issue view N` | `GET /repos/{o}/{r}/issues/N` |
| Create issue | `gh issue create ...` | `POST /repos/{o}/{r}/issues` |
| Add labels | `gh issue edit N --add-label ...` | `POST /repos/{o}/{r}/issues/N/labels` |
| Assign | `gh issue edit N --add-assignee ...` | `POST /repos/{o}/{r}/issues/N/assignees` |
| Comment | `gh issue comment N --body ...` | `POST /repos/{o}/{r}/issues/N/comments` |
| Close | `gh issue close N` | `PATCH /repos/{o}/{r}/issues/N` |
| Search | `gh issue list --search "..."` | `GET /search/issues?q=...` |
