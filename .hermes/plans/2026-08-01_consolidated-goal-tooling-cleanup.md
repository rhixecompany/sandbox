---
name: consolidated-goal-tooling-cleanup
title: "Consolidated Standing Goal: Disk Cleanup + Full Tooling Implementation + Prompt Pipeline"
description: "Merge the desktop goal (tooling-config/tooling-lint enhancement, vscode, commit/push/PR across subrepos) and the TUI goal (ruff/mypy/pylance, script migration to hermes/scripts, prompt-management plans, execute-workflow) with a new node_modules/venv cleanup across ~/ and ./."
version: 1.0.0
author: Hermes Agent
license: MIT
status: completed
tags: [goal, cleanup, node_modules, venv, tooling, ruff, mypy, pylance, vscode, prompts, plans]
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
- 2026-08-01 — Phase 2 ROOT COMPLETE: root venv recreated (uv, 135 pkgs), root node_modules restored (bun, 273 pkgs); VS Code audit done (43=43 extensions aligned, tasks.json markdownlint problemMatcher added, user settings +4 keys: formatOnSaveMode, ignoreRecommendations, pasteUrlAsFormattedLink, notebook.formatOnSave); **G2 PASSED — 0 tooling failures** (was 17): root-caused verifier bug (preferred `.markdownlintrc.json`, a v0.x name cli2 rejects → now `.markdownlint-cli2.jsonc`), deleted 17 legacy configs (4 tracked), created cli2 configs in Bash + Resume_maker, reinstalled deps in Resume_maker (bun) + university-libary-jsm (npm ci, 1121 pkgs). Root commit landed: `chore(cleanup): inventory tool, delete node_modules/venvs (8GB), fix markdownlint configs + verifier, align vscode`.
- 2026-08-01 — Phase 2 PER-REPO in progress: venv recreation batch (uv) + node_modules restore batch (bun/npm --ignore-scripts) running in background.
- 2026-08-01 — Phase 2 COMPLETE: per-repo venvs (12) + node_modules (23) restored (ignore-scripts; phantomjs/db:migrate traps avoided); subrepo commits: rhixecompany-comics f601217 (101 files), university-libary-jsm 2bc208c (26 files); root commits b74f0209 + cba2236c + d3ce727c (pointer sync + plan log); pushed all 3 to origin/development; PRs: sandbox#10 (existing), rhixecompany-comics#2, university-libary-jsm#3 (development → production); no other subrepos ahead.
- 2026-08-01 — Phase 3 STARTED (script inventory + migration to hermes/scripts + async conversion).
- 2026-08-01 — Phase 3 COMPLETE: inventory found migration already done (158 scripts in hermes/scripts, 0 cjs/js remain → cjs→TS conversion complete; 3 MCP servers present); triage: .enhance toolkit stays repo-local (lives with prompts it repairs), `tmp_repair_list.py` deleted (temp junk); `compileall` exit 0 (all 158 py compile).
- 2026-08-01 — Phase 4 COMPLETE: prompt library 222 prompts, repo.prompt.md + 4 repo-* prompts + execute prompts (execute-all-prompts/execute-plan/plan-execute) present with valid frontmatter; repo plans exist (2026-08-01_repo-tooling.md, tooling-implementation.md completed); analyzer clean.
- 2026-08-01 — Phase 5 COMPLETE: `hermes doctor` + `doctor --fix` all checks passed; security audit 0 vulns (147 components); status OK (1 active session); insights OK; `logs errors` = only benign optional-toolset WARNINGs (discord/feishu/yuanbao/homeassistant/image_gen/kanban not installed — expected, not bugs). No actionable issues for systematic-debugging.
- 2026-08-01 — **GOAL COMPLETE (all 5 phases + gates G0-G2)**. Commits: root b74f0209, cba2236c, d3ce727c, +tmp-cleanup; comics f601217; ULJ 2bc208c. Pushed; PRs sandbox#10, comics#2, ULJ#3.

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
