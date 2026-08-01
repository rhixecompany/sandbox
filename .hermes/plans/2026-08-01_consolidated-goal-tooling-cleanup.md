---
name: consolidated-goal-tooling-cleanup
title: "Consolidated Standing Goal: Disk Cleanup + Full Tooling Implementation + Prompt Pipeline"
description: "Merge the desktop goal (tooling-config/tooling-lint enhancement, vscode, commit/push/PR across subrepos) and the TUI goal (ruff/mypy/pylance, script migration to hermes/scripts, prompt-management plans, execute-workflow) with a new node_modules/venv cleanup across ~/ and ./."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [goal, cleanup, node_modules, venv, tooling, ruff, mypy, pylance, vscode, prompts, plans]
status: active
created: 2026-08-01
---

# Consolidated Standing Goal — Cleanup + Tooling + Prompt Pipeline

## Goal Statement

Execute ONE standing goal combining the prior desktop goal, the prior TUI goal, and a new disk cleanup:

1. **CLEANUP (new)**: inventory, size, and remove `node_modules`, `.venv`, and `venv` directories across `~/` and `./`, protecting system-managed installs, then verify nothing build-critical is lost (manifests + lockfiles stay).
2. **TOOLING (desktop goal)**: enhance tooling-config/tooling-lint MCP servers, skills, scripts, plans, prompts with ruff/mypy/pylance cleanup + markdownlint verification; update package.json/requirements.txt; recreate venvs via uv and install deps; audit/fix/load VS Code skills, extensions, user+workspace configs, tasks/launch; fix all VS Code notifications bugs/issues/errors/warnings; commit/push/PR; repeat across all subrepos.
3. **SCRIPTS + PROMPTS (TUI goal)**: triage all python scripts at `./` and `.gitHub/`, migrate them into `%LOCALAPPDATA%/hermes/scripts`, convert any cjs/js to async TypeScript and any py to async Python; run /prompt-management on `.github/prompts/repo.prompt.md` + `repo-*.prompt.md` to create verified plan+specs for every repo/subrepo; implement /python-quality /tooling-config /tooling-lint fully; ONLY THEN create+verify an `/execute-workflow` prompt fully implementing the plan; ONLY THEN execute it to completion.
4. **VERIFY**: run `hermes doctor && hermes doctor --fix && hermes security audit && hermes status && hermes insights && hermes logs list && hermes logs errors && hermes logs desktop && hermes logs gateway && hermes logs gui && hermes logs agent` + /systematic-debugging until 0 bugs/issues/warnings/errors.

Hard stop condition (user standard): do not stop until the plan is created, verified, executed, and completed without errors, warnings, or issues.

## Phase 0 — Cleanup Inventory (VERIFIED 2026-08-01)

Survey result (Python os.walk, pruned recursion):

- SandBox `./`: **16 node_modules** (root + Banking, Django-Scrapy-Selenium, Resume_maker, comicwise, ecom/docs, ecom/frontend, mcp-server-typescript, mcp-servers/copilot-studio, mcp-servers/typescript, rhixe_scans, rhixecompany-comics/frontend, selenium_webdriver, university-libary-jsm, xamehi.tv/frontend, xamehi) + **11 venvs** (root .venv + Banking, Django-Scrapy-Selenium, Python-projects, cookiecutter-django-tailwind, ecom, mcp-servers/python, rhixe_scans, rhixecompany-comics/backend, xamehi.tv, youtube-downloader)
- Known sizes: SandBox root `node_modules` ~85M, root `.venv` ~435M (per-project sizes TBD in dry-run)
- Home `~/`: 23 node_modules + 9 venvs at shallow scan (includes system dirs — see protection list)
- Home top-level also has: `myvenv`, `pipx`, `package.json`, `package-lock.json`, `biome.exe`, `bunfig.toml`, `postgresql_18.exe`, `upgrade.sh`, `vscode-remote-wsl`

## Phase 1 — Cleanup Execution

1. Build a Python inventory script in `scripts/` (repo convention: no inline scripts) that lists every node_modules/.venv/venv under `~/` and `./`, computes reclaimable bytes (bounded du or os.walk sum with timeouts), and classifies each path:
   - **SAFE** — repo-local dirs in SandBox root + `projects/*` (gitignored, reinstallable from lockfiles)
   - **SYSTEM (never touch)** — `.vscode/extensions/*/node_modules`, `.bun/install/global`, `.opencode`, `.config/opencode`, `.copilot/plugin-data`, `pipx`, `.git` internals
   - **ASK** — home-root `~/node_modules`, `~/myvenv`, `~/pipx`, any dir whose removal could affect a tool install
2. **DRY-RUN FIRST**: emit `results/cleanup-dry-run.md` with per-path size + classification + total reclaimable. Present to user for approval before any deletion.
3. After approval: delete SAFE set (`rm -rf` per path with gitignore sanity check first — confirm each path is ignored, e.g. `git check-ignore` inside the owning repo; never delete a path that is tracked).
4. Verify per repo: `git status --porcelain` shows no deletions of tracked files; manifests (`package.json`, `package-lock.json`, `requirements.txt`, `pyproject.toml`, `uv.lock`) untouched.
5. Do NOT reinstall in this phase — the Tooling phase recreates required venvs via uv and installs deps from updated manifests.
6. Record reclaimed space in the goal output + SESSION_REPORT.md changelog.

## Phase 2 — Tooling Implementation (desktop goal)

- Enhance `tooling-config` + `tooling-lint` MCP servers, skills, scripts, plans, prompts: ruff, mypy, pylance cleanup; verify markdownlint config.
- Update `package.json` / `requirements.txt` with all dependencies, packages, scripts; set up venv via uv and install.
- Search, audit, debug, fix, load, use all VS Code skills; read all VS Code extension docs; install recommended/missing extensions; update+verify user and workspace configs per best practices; ensure extensions, file types, MCP servers, tasks, launch are correct; fix all VS Code notification bugs/issues/errors/warnings.
- Git commit, push, PR — repeat in ALL subrepos (14 repos, development branch).

## Phase 3 — Script Migration (TUI goal)

- install/setup/config/test ruff, mypy, pylance.
- List + triage all python scripts at `./` and `.gitHub/`; migrate them all into `%LOCALAPPDATA%/hermes/scripts`; update all affected files.
- Convert any cjs/js in `%LOCALAPPDATA%/hermes/scripts` to async TypeScript; any py to async Python; update all affected files.

## Phase 4 — Prompt/Plan Pipeline (TUI goal, strictly sequential)

1. `/prompt-management .github/prompts/repo.prompt.md,.github/prompts/repo-*.prompt.md` — create and verify comprehensive plan + specs for all repos/subrepos in `./`.
2. `/python-quality /tooling-config /tooling-lint` — implement fully on `./` and all subrepos; debug/fix/validate all bugs, issues, errors, warnings.
3. ONLY THEN: create and verify a prompt for `/execute-workflow /execute-plans /executing-prompt-workflows` fully implementing the plan.
4. ONLY THEN: start and complete the prompt and plan.

## Phase 5 — Hermes Diagnostic Chain + Systematic Debugging

Run the full diagnostic chain (see Goal Statement #4) + `/systematic-debugging` until all bugs, issues, warnings, errors are fixed. Verify with `tooling_full_check.py` re-run to 0 tooling-level failures.

## Protection Rules (HARD)

- NEVER delete: `.vscode/extensions/**`, `.bun/install/global/**`, `.opencode/**`, `.config/opencode/**`, `.copilot/plugin-data/**`, `pipx/**`, `.git/**`, `hermes-profiles/**` (gitignored mirror — exclude from tooling AND cleanup).
- Dry-run + explicit user approval before ANY deletion. Cleanup is destructive: `rm -rf` requires approval per batch.
- Never delete a tracked path: verify `git check-ignore` (or status) first in the owning repo.
- Commits/pushes/PRs only within the Tooling phase scope and only when the user asks (session-auto-commit requires follow-up approval; don't commit unless asked).

## Verification Gates

### Progress Log (append-only)

- 2026-08-01 — **Phase 1 COMPLETE**: `scripts/cleanup_inventory.py` built; dry-run at `results/cleanup-dry-run.md` (27 SAFE / 1 ASK / 69 SYSTEM); approval recorded `.hermes/approvals/20260801_cleanup-delete-safe.md` (+1 Alexa via clarify); **deleted 27 dirs (~8,070.9 MB), 0 skipped**; re-scan shows 0 SAFE; tracked-deletion sweep across root + 14 repos clean.
- 2026-08-01 — Phase 2 STARTED (root venv + deps recreation, tooling check, VS Code audit).

- G0: inventory script runs, classifications correct (spot-check 5 paths)
- G1: dry-run report exists + user approved; SAFE deletions done; `git status` clean of tracked deletions
- G2: tooling_full_check.py → 0 TOOLING FAIL
- G3: scripts migrated + converted; affected files updated (spot-check compile: `bun build` / `python -m py_compile`)
- G4: repo.prompt.md plans created + verified for all repos
- G5: execute-workflow prompt created + verified (frontmatter parses, phases+outputs declared)
- G6: prompt executed to completion, artifacts verified on disk
- G7: diagnostic chain + systematic-debugging → 0 bugs/issues/warnings/errors

## Reinstall Reference (post-cleanup)

- npm/bun: `bun install` (or `npm ci` where lockfile present) in each repo root/frontend
- python: `uv venv` + `uv pip install -r requirements.txt` (or `uv sync` where pyproject/uv.lock present) per repo
- Root: `bun install`; `.venv` via uv per requirements.txt
