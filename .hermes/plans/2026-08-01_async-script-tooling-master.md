---
name: async-script-tooling-master
title: "Async Script Migration + Full Tooling Implementation Master Plan"
description: "Install/test ruff-mypy-pyright, triage+migrate scripts to hermes/scripts, convert cjs/js→async TS and py→async python, prompt-management plans/specs, full tooling on ./+subrepos, workflow prompt, execute, hermes doctor chain."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [planning, tooling, async, typescript, python, ruff, mypy, pyright, prompt-management, subrepos, hermes-doctor]
status: in_progress
created: 2026-08-01
---

# Async Script Migration + Full Tooling Implementation — Master Plan

## Goal

Execute the user's 8-phase strictly-sequential pipeline on `C:/Users/Alexa/Desktop/SandBox` + `~/AppData/Local/hermes/scripts`:

| Phase | Scope                                                                                                                                          | Gate                                                         |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| 1     | Install/setup/config/test **ruff, mypy, pylance(pyright)**                                                                                     | all 3 run clean on smoke test                                |
| 2     | List + triage all py at `./`, `.github/` → migrate canonical to `~/AppData/Local/hermes/scripts`, update all affected refs                     | md5 parity + zero dangling refs                              |
| 3     | Convert cjs/js in hermes/scripts → **async TS**; py → **async Python**; update all affected refs                                               | each converted script runs (--help/dry-run), callers updated |
| 4     | `/prompt-management .github/prompts/repo.prompt.md,.github/prompts/repo-*.prompt.md` → create+verify plans/specs for all repos/subrepos        | PLAN.md+SPEC.md × all repos, frontmatter valid               |
| 5     | `/python-quality /tooling-config /tooling-lint` fully on `./` + subrepos; debug/fix/validate ALL bugs/issues/errors/warnings                   | `tooling_full_check.py` 0 tooling failures                   |
| 6     | **ONLY THEN** create+verify prompt for `/execute-workflow /execute-plans /executing-prompt-workflows`                                          | prompt frontmatter valid, phases ≥3                          |
| 7     | **ONLY THEN** start+complete the prompt and plan                                                                                               | artifact written, plan status completed                      |
| 8     | `hermes doctor && doctor --fix && security audit && status && insights && logs {list,errors,desktop,gateway,gui,agent}` + systematic-debugging | all bugs/issues/warnings fixed or documented                 |

## Current Context / Assumptions (verified Phase 0)

- Tools: ruff 0.15.10 ✅, pyright 1.1.411 ✅, **mypy NOT installed** ❌, tsc 5.9.3 ✅, bun 1.3.14 ✅, node v26.5.0 ✅, Hermes v0.19.1.
- hermes/scripts: **153 entries** = 113 py, 12 sh, 9 json, **6 cjs + 1 js**, 5 ps1, 3 md, 1 txt, dirs (archive/, memory_repair_artifacts/, **pycache**/). **0 ts**.
- Known duplicate cluster: `audit-227.js` + `audit-227.cjs` + `audit-227.cjs` variants (memory: audit-227/-cjs/-js dupes) — dedupe during triage.
- Root `./*.py`: only `eslint_count.py` remains (previous sessions already consolidated the rest).
- `.github/scripts/*.py`: EMPTY (3 MCP servers were `git rm`'d last session; canonical now in hermes/scripts — config.yaml MCP paths already canonical).
- `.github/prompts/.enhance/*.py`: **26 files** — repo-local prompt-repair toolkit, path-coupled to `.github/prompts/` (analysis/fix pipeline). TRIAGE decision: keep in-repo (moving breaks the pipeline), document in report.
- `.github/hooks/*/hook.py`: 3 Hermes hook files — repo artifacts executed by Hermes from repo path; keep in-repo (already noqa'd E402).
- Previous plans `.hermes/plans/2026-08-01_repo-tooling.md` + `2026-08-01_tooling-implementation.md` both marked completed, but SESSION_REPORT shows Phase-3 subrepo fixes were INTERRUPTED: remaining ruff errors at interrupt — Django-Scrapy-Selenium 20, profile 24 (E711/E712/E722 fixes in flight), rhixe_scans 58, xamehi.tv 53.
- Baseline git: 942 modified/untracked entries (large dirty tree, pre-existing). Branch `development`.

## Triage Decisions (Phase 2)

| Source                          | Count | Decision                                                   |
| ------------------------------- | ----- | ---------------------------------------------------------- |
| root `eslint_count.py`          | 1     | Migrate → hermes/scripts + update refs                     |
| `.github/scripts/*.py`          | 0     | Already canonical in hermes/scripts                        |
| `.github/prompts/.enhance/*.py` | 26    | **Keep in-repo** (path-coupled pipeline); record in report |
| `.github/hooks/*/hook.py`       | 3     | **Keep in-repo** (Hermes executes from repo path)          |
| hermes/scripts js/cjs           | 7     | Dedupe → convert to async TS                               |
| hermes/scripts py               | 113   | Convert to async Python (class-dependent)                  |

## Async Conversion Protocol (Phase 3)

**Python (113 files):**

- CLI contract preserved: argv parsing, exit codes, stdout format identical.
- Network I/O (`requests`/`urllib`/`http.client`) → `httpx.AsyncClient` (or `aiohttp` where pattern exists).
- File I/O where hot path → `aiofiles`; light I/O stays sync inside `async def`.
- Entry pattern: `async def main()` + `if __name__ == "__main__": asyncio.run(main())`.
- Long-running servers (MCP servers in hermes/scripts) → full async event loop.
- CPU-bound validators → keep sync logic wrapped in async main (no pointless churn).
- Verify: run `--help` + dry-run/real invocation, `python -m py_compile`, ruff check.

**JS/CJS (7 files) → async TypeScript:**

- Dedupe audit-227.js/.cjs first (keep most complete, delete twin).
- Convert each to `src`-less `.ts` with `async function main()` + `await` for all I/O (fs/promises, child_process promisified).
- Add `tsconfig.json` (target es2022, module nodenext, strict) + build via tsc → keep `.cjs` runtime output OR run via bun (bun runs .ts natively) — prefer bun runtime to avoid build step, fallback tsc.
- Verify: `bun run file.ts --help` / `tsc --noEmit` + real invocation.

## Phase 3 Progress (live)

- **JS/CJS → async TS: DONE (6 files, 0 js/cjs remain)**
  - `audit-227.ts` (merged audit-227.js+.cjs dupes), `fix-frontmatter-yaml.ts`, `phase4-reconstruct.ts`, `prompt-audit-all.ts`, `session-audit-227.ts`, `verify-frontmatter.ts`
  - All pass `tsc --strict` (typescript 5.9.3 local; npm `--include=dev` needed due to global `omit=dev` pitfall) and run via `bun run` (5) or `node` (session-audit-227 needs better-sqlite3 native — bun can't load it; node 26 native TS-strip works)
  - package.json + tsconfig.json added to hermes/scripts (devDeps @types/node, typescript, @types/better-sqlite3; runtime better-sqlite3)
- **MCP servers → async: DONE (3 files, verified)**
  - `tooling_lint_mcp_server.py`, `python_quality_mcp_server.py`, `tooling_config_mcp_server.py`
  - `_run`/`_run_cmd` → `_run_async` via `asyncio.create_subprocess_exec` + temp-file capture; preserved PATH augmentation (C:\nvm4w\nodejs + %APPDATA%\npm), CREATE_NO_WINDOW, stdin=DEVNULL; timeout→`asyncio.wait_for`+kill. Tools now `async def`.
  - Verified: py_compile ✅, ruff clean ✅ (fixed E741 `l`×2), async subprocess smoke exit=0 ✅
  - config.yaml MCP paths already canonical (gateway respawns next call)
- **Sync py → async: IN PROGRESS** — 29 sync files dispatched to 3 parallel subagents (deleg_b438b9af):
  - A(10): _pathutil, add_mcp_servers, analyze_prompt_library(_v2), build_env, build_registry, env_sync, eslint_count, fix_github_prompts(_inline_lists)
  - B(10): fix_github_prompts_remaining, fix_prompt_library, fix_prompts, fix_repo_body(2), generate_session_report, health_check, normalize-frontmatter, purge_dead_keys, register-instruction-personalities
  - C(9): remediate_skills, repo-plan-spec, session_audit, test_providers_models, tooling_full_check, validate_services, verify-frontmatter-normalization, verify_prompt_library, verify_templates_after_create
  - Protocol: async def main()+asyncio.run; subprocess→to_thread/create_subprocess_exec; requests→to_thread (NO httpx — not in plain python3); CLI contract preserved; verify py_compile+ruff+--help
- **Ref updates: DONE for JS/CJS** — only historical docs/spawn-trees/session logs reference old names (no action). hermes-profiles mirror has no scripts dir.

## Phase Gates

- **Gate 1**: `ruff --version`, `mypy --version`, `pyright --version` all succeed; smoke test passes.
- **Gate 2**: md5 parity root→hermes/scripts for migrated; `rg` zero dangling repo-path refs.
- **Gate 3**: all converted scripts execute; `tsc --noEmit` (or bun run) clean; callers (prompts, quick-commands, MCP config, copilot-instructions, AGENTS.md) updated.
- **Gate 4**: `validate_prompts.py --file <prompt> --fail-on-error` × repo prompts; PLAN.md/SPEC.md present per repo.
- **Gate 5**: `tooling_full_check.py` → 0 tooling-level failures; subrepo ruff residuals addressed (genuine bugs fixed, conventions ignored per-file).
- **Gate 6**: workflow prompt frontmatter parses, phases ≥3, outputs path declared.
- **Gate 7**: artifact at `results/<prompt>.output.md`; plan status completed.
- **Gate 8**: hermes doctor --fix exit 0; security audit clean; status/insights/logs reviewed; findings fixed or documented.

## Files Likely to Change

- `~/AppData/Local/hermes/scripts/*.py` (113, async conversion)
- `~/AppData/Local/hermes/scripts/*.ts` (new, from js/cjs)
- `~/AppData/Local/hermes/scripts/eslint_count.py` (new migrate)
- `~/AppData/Local/hermes/scripts/tsconfig.json` (new)
- root `eslint_count.py` (deleted after migrate)
- `~/AppData/Local/hermes/config.yaml` (MYPY/pyright tooling refs if needed)
- `.github/prompts/*.prompt.md`, `templates/`, quick-commands, AGENTS.md/README/copilot-instructions (ref updates)
- `projects/*/PLAN.md`, `projects/*/SPEC.md`
- `projects/*` Python/JS sources (tooling fixes)
- `results/tooling-implementation.prompt.output.md` (final artifact)

## Risks / Tradeoffs

| Risk                                                                 | Likelihood | Impact | Mitigation                                                                     |
| -------------------------------------------------------------------- | ---------- | ------ | ------------------------------------------------------------------------------ |
| Async conversion breaks canonical tooling (MCP servers, hooks, cron) | Med        | High   | Preserve CLI contract; verify each script runs; MCP respawn after edits        |
| 113-file conversion is context-heavy                                 | High       | Med    | Delegate in batches ≤3 subagents with exact protocol; verify artifacts on disk |
| cjs→ts breaks node-only callers                                      | Med        | Med    | Run via bun (native ts); keep `.cjs` output name for node callers              |
| .enhance toolkit "not migrated" conflicts with literal instruction   | Med        | Low    | Triage documented; path-coupled pipeline stays in-repo (judgment call)         |
| mypy on legacy codebase yields thousands of errors                   | High       | Low    | Report-only debt; fix genuine bugs only                                        |
| Pre-existing dirty tree (942 files) complicates diff review          | High       | Low    | Track before/after counts; commit only at user request                         |

## Open Questions

- None blocking. Auto-advance per user preference (all phases given upfront); pause only on critical phase failure.
