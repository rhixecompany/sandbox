# PRESTATE — SandBox root repo (repo-management Phase 1 + Phase 4)

Recorded: 2026-07-16
Repo: rhixecompany/sandbox (https://github.com/rhixecompany/sandbox.git)
Local path: C:/Users/Alexa/Desktop/SandBox
Operator: Hermes subagent (task explicitly approved 'run everything')

## Local branches (git branch)
- development   (CURRENT, checked out)
- master
- production

## Remote branches (git branch -a / live API)
- origin/HEAD -> origin/master
- origin/development
- origin/master
- origin/production

Live API branch list (gh api repos/rhixecompany/sandbox/branches): development, master, production

## GitHub default branch (live API)
- master   (gh repo view --json defaultBranchRef -> "master")

## CI workflow state before change
- .github/workflows/ci.yml EXISTED (untracked) but scoped to projects/Bash with strict
  typecheck/lint:strict/test/format:check steps using oven-sh/setup-bun@v2.
- OVERWRITTEN by this task with the task-specified minimal CI:
    name: CI
    on: [push, pull_request]
    jobs.build: checkout -> oven-sh/setup-bun@v1 -> bun install -> bun run build || true -> bun run test || true

## Working tree note
Pre-existing uncommitted modifications to many files (.hermes, .vscode, prompts/, scripts/,
projects/*) were present before this task. This task commits ONLY the CI workflow change
(.github/workflows/ci.yml). It does NOT stage or commit the unrelated prior modifications.

## Planned mutations (post pre-state capture)
1. git add .github/workflows/ci.yml && git commit (CI only)
2. git branch -D master            # delete local stray master
3. git push origin --delete master # delete remote master
4. gh repo edit rhixecompany/sandbox --default-branch production   # repoint default
5. git push origin development production
6. git fetch -p

## Expected post-state
- Local: development, production only
- Remote: development, production only (master gone)
- GitHub default: production
