# Approval Request — SandBox node_modules/.venv Cleanup (SAFE set)

- **Requestor**: Hermes Agent (default profile)
- **Owners**: Alexa
- **Created**: 2026-08-01
- **Status**: PENDING (+1 required from each Owner before execution)

## Scope

Delete 27 gitignored `node_modules` / `.venv` / `venv` directories under
`C:\Users\Alexa\Desktop\SandBox` (root + `projects/*`) — see
`results/cleanup-dry-run.md` for the exact list. Reclaimable: **~8,070.9 MB**.

All 27 are classified SAFE: repo-local, verified gitignored (`git check-ignore`
passed for each — no tracked files are affected), reinstallable from lockfiles.

## Justification

- Standing goal Phase 1 (consolidated-goal-tooling-cleanup): reclaim disk,
  force fresh dependency installs before the tooling phase recreates venvs via uv.
- Nothing build-critical is lost: manifests + lockfiles (`package.json`,
  `package-lock.json`, `requirements.txt`, `pyproject.toml`, `uv.lock`) stay.

## Excluded (never touched)

- SYSTEM set (69 dirs): `.vscode/extensions/*`, `.bun/install/global`, `.opencode`,
  `.config/opencode`, `.copilot/plugin-data`, `pipx`, `.git`, `hermes-profiles/`
- ASK set (1 dir, 284.5 MB): `~/.cache/codex-runtimes/.../node_modules`
  (Codex CLI runtime cache — per-item decision, NOT in this approval)

## Rollback plan

Reinstall per repo (exact commands):
- npm/bun: `bun install` or `npm ci` in each repo root / frontend / docs
- python: `uv venv && uv pip install -r requirements.txt` (or `uv sync`)
- Root: `bun install`; `.venv` via uv per requirements.txt
Phase 2 (tooling implementation) will recreate the required venvs anyway.

## Verification steps (post-delete)

1. `git status --porcelain` in SandBox root + each projects/* repo → no deletions
   of tracked files (all 27 pre-verified ignored)
2. `results/cleanup-dry-run.md` shows 0 SAFE entries remaining
3. Reclaimed space recorded in SESSION_REPORT.md changelog

## Approval

- [x] +1 Alexa — approved for execution (date: 2026-08-01)
- **Recorded via clarify on 2026-08-01** — choice: "Approve SAFE deletion — delete 27 dirs (~8 GB) and continue to Phase 2"
