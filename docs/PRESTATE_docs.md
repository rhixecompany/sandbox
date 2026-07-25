# PRESTATE_docs.md

Captured before any mutation as part of repo-management Phase 1 (branch
normalization) + Phase 3/4 (CI) for the `docs` tree.

> NOTE: `docs/` is a SUBDIRECTORY of the `rhixecompany/sandbox` monorepo, not a
> standalone `docs` repo. Git operations therefore apply to the whole `sandbox`
> repo. Repo name resolved via `gh repo view --json name`: **sandbox**.

## Local branches (git branch -vv)

- `* development` b8b86b0f — [origin/development] "feat: add Bash + Resume_maker to repo prompt, expand 14→16 project refs" (current branch)
- `master`      0792d250 — [origin/master] "updates"
- `production`  0792d250 — [origin/production] "updates"

## Remote branches (git branch -r)

- `origin/HEAD -> origin/master`
- `origin/development`
- `origin/master`
- `origin/production`

## GitHub default branch (gh repo view --json defaultBranchRef)

- **master**  (master is the current GitHub default; origin/HEAD points to origin/master)

## Remote / origin

- origin  <https://github.com/rhixecompany/sandbox.git> (fetch)
- origin  <https://github.com/rhixecompany/sandbox.git> (push)

## CI workflow pre-existing state

- `.github/workflows/ci.yml` already present (untracked, 655 bytes) — Bun-based CI
  running on push to `development` / PR to `development`+`production` (typecheck,
  lint:strict, test, format:check in `projects/Bash`). Kept as the intended CI;
  NOT replaced with the generic markdown-lint template from the task brief.

## Working-tree warning

- The working tree had a large volume of UNRELATED uncommitted changes (prompt
  deletions, `.hermes` plan deletions, vscode edits, untracked audit scripts,
  etc.). To honor "never commit unrelated work", only the CI workflow and this
  prestate file were staged — `git add -A` was deliberately NOT used.

Captured: 2026-07-16
