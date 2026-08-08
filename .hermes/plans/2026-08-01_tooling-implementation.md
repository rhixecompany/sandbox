---
name: tooling-implementation
title: "Full Tooling Implementation: python-quality / tooling-lint / tooling-config across ./ and subrepos"
description: "Implement, debug, fix, and validate the three tooling stacks across the SandBox workspace root and all projects/ subrepos, then execute via a workflow prompt."
version: 1.1.0
author: Hermes Agent
license: MIT
status: completed
tags: [tooling, ruff, pyright, eslint, prettier, cspell, markdownlint, pre-commit, git-cliff, mcp]
created: 2026-08-01
completed: 2026-08-01
---

# Full Tooling Implementation Plan

## Goal

Fully implement and validate three tooling stacks across `./` (SandBox root) and all 14 `projects/` subrepos, then package the workflow as reusable plan, skills, scripts, quick-commands, and a self-contained workflow prompt. "Implement fully" = every applicable repo has working configs, every checker runs without tooling-level failure, safe fixes are applied, and remaining debt is documented with disposition.

## Current Context / Assumptions (verified Phase 0)

- Root `C:/Users/Alexa/Desktop/SandBox` + 14 `projects/*` git submodules; `hermes-profiles/` is gitignored and EXCLUDED from all tooling.
- Config matrix already landed (previous sessions): ruff/pyright ×9, eslint ×8, prettier ×7, cspell ×8, editorconfig ×14, pre-commit ×13, cliff.toml ×13.
- 3 MCP servers patched (temp-file capture, PATH augmentation, cspell v10 `lint` glob, check_all counter regex) — `.github/scripts/{python_quality,tooling_lint,tooling_config}_mcp_server.py`.
- Known debt (baseline, 2026-08-01): ruff lint root ~3167 errors (1611 safe-fixable), pyright 1428 errors, prettier 515 root files, cspell 179 root + 6762 workspace (domain terms), markdownlint MD012/MD026 in curated prompts.
- Tools available: ruff, pyright, eslint, prettier, cspell v10, markdownlint-cli2, pre-commit 4.6.0, git-cliff.

## Proposed Approach

Three-stage delivery with verification gates between stages:

1. **Stage A — Artifacts**: plan (this file) + umbrella skill + verifier script + quick-commands. Verify: script runs end-to-end, skills yaml-valid, shell syntax OK.
2. **Stage B — Prompt**: self-contained `.prompt.md` executing the plan via `execute-workflow` / `executing-plans` / `executing-prompt-workflows`. Verify: frontmatter yaml-valid, phases+outputs declared.
3. **Stage C — Execute**: run the prompt against the real workspace; apply FIX-scope changes; write artifact; close plan with verification table.

## Step-by-Step Plan

### Phase 0 — Inventory (DONE)

- [x] Verify config matrix on disk (root + subrepos)
- [x] Confirm 3 MCP servers present
- [x] Record debt baseline

### Phase 1 — Artifacts: plan, skill, scripts, quick-commands

- [ ] Write `.hermes/plans/2026-08-01_tooling-implementation.md` (this file)
- [ ] Create umbrella skill `devops/tooling-implementation` (triggers, workflow, pitfalls, verification) referencing `python-quality`, `tooling-lint`, `tooling-config`
- [ ] Patch `tooling-lint` + `tooling-config` + `python-quality` skills to cross-link umbrella and carry current pitfalls
- [ ] Create `.github/scripts/tooling_full_check.py` — per-repo verifier (ruff check/format, eslint, prettier, cspell lint, markdownlint, pre-commit validate; bounded timeouts; writes report)
- [ ] Create `scripts/tooling-quick-commands.sh` — bounded bash one-liners per check
- [ ] VERIFY GATE A: run `tooling_full_check.py` end-to-end; `python -c yaml.safe_load` each SKILL.md; `bash -n` quick-commands

### Phase 2 — Prompt artifact

- [ ] Create `.github/prompts/tooling-implementation.prompt.md` (frontmatter + Goal/Context/Inputs/Phases/Steps/Outputs/Rules)
- [ ] VERIFY GATE B: yaml frontmatter parses; phases ≥3; outputs path declared (`results/tooling-implementation.prompt.output.md`)

### Phase 3 — Execute (FIX scope)

- [ ] Run full-check verifier, capture fresh baseline
- [ ] `ruff check --fix` (safe fixes) on root + all 9 python repos
- [ ] Add `.github/prompts` to root `.prettierignore` (curated artifacts), then `prettier --write` remaining root files
- [ ] Fix real F821 bug: `.github/hooks/session-auto-commit/hook.py` undefined `log_debug`
- [ ] cspell: add workspace domain words to root `cspell.json`; fix real `libary` → `library` typo in prose (repo names unchanged + added to words)
- [ ] Re-run verifier; record before/after numbers

### Phase 4 — Validate + report

- [ ] Confirm all checkers complete without tooling-level failure
- [ ] Write `results/tooling-implementation.prompt.output.md` artifact (per-phase findings, changes, flagged items, verification table)
- [ ] Mark plan `status: completed`, add verification table + lessons learned

## Files Likely to Change

| Path                                                      | Action                     |
| --------------------------------------------------------- | -------------------------- |
| `.hermes/plans/2026-08-01_tooling-implementation.md`      | create (this)              |
| `~/.hermes/skills/devops/tooling-implementation/SKILL.md` | create                     |
| `tooling-lint`, `tooling-config`, `python-quality` skills | patch cross-links/pitfalls |
| `.github/scripts/tooling_full_check.py`                   | create                     |
| `scripts/tooling-quick-commands.sh`                       | create                     |
| `.github/prompts/tooling-implementation.prompt.md`        | create                     |
| `results/tooling-implementation.prompt.output.md`         | create (artifact)          |
| root `.prettierignore`                                    | add `.github/prompts`      |
| root `cspell.json`                                        | add domain words           |
| `.github/hooks/session-auto-commit/hook.py`               | fix F821                   |
| root + subrepo python files                               | ruff safe autofixes        |

## Tests / Validation

- `tooling_full_check.py` exits 0 (all checkers complete; per-tool exit codes recorded)
- Per-repo report written to `.github/scripts/reports/`
- SKILL.md frontmatter parses via `yaml.safe_load`
- Prompt frontmatter parses; phases ≥3; outputs path declared
- `bash -n scripts/tooling-quick-commands.sh` passes
- Final artifact includes verification table with before/after counts

## Risks & Tradeoffs

| Risk                                        | Likelihood | Impact | Mitigation                                                                                        |
| ------------------------------------------- | ---------- | ------ | ------------------------------------------------------------------------------------------------- |
| ruff --fix touches many files               | High       | Med    | Safe fixes only; review `git diff --stat`; reversible                                             |
| prettier --write large diff                 | High       | Med    | Exclude curated `.github/prompts`; review count                                                   |
| MCP servers need respawn after script edits | Med        | Low    | Known kill+respawn pattern (gateway respawns on next call)                                        |
| Auto-fix changes curated prompt formatting  | Med        | High   | Prompts excluded from prettier; markdownlint findings REPORT-only (`.enhance` pipeline owns them) |
| pyright 1428 errors are code debt           | High       | Low    | Report-only; not tooling                                                                          |

## Open Questions

- None blocking. Disposition defaults: safe fixes applied; curated/analysis debt reported with pointers.

## Lessons Learned (filled at completion)

### Phase 0–2 (inventory, plan, skills)

- Ruff/globbing gotcha: `{{cookiecutter.project_slug}}/` in `.ruff.toml` exclude is **brace-expanded** by ruff's glob engine, so the Jinja template dir was NOT excluded → ruff hard-failed (exit 2) parsing the template `pyproject.toml`. Brace-free pattern `*cookiecutter*` excludes correctly.
- Skill descriptions are **≤60 chars** enforced at create time (61 with a trailing period is rejected).

### Phase 3 (fixes — this run)

- Prettier exit 2 ≠ formatting debt: it is a **parse error** on a file prettier cannot read. Root cause classes: Django/allauth `templates/*.html` with Jinja `{% slot %}` / `</{% if %}>`, and a generated `docs/reports/pyright-report.json` that is not valid JSON. Fix = add the offending paths to `.prettierignore` (`**/templates/`, `docs/reports/`), not a code change.
- ESLint exit 2 classes:
  - Legacy `eslint.config.mjs` using `next/core-web-vitals` via FlatCompat requires `eslint-config-next` + `@rushstack/eslint-patch`; missing deps → hard fail. Replaced rhixe_scans with canonical flat config.
  - `npm config get omit` is **`dev`** globally on this machine → `npm install`/`npm ci` silently skip devDependencies. Must pass `--include=dev` (or `npm ci --include=dev`). uni-libary needed `npm ci --include=dev --ignore-scripts` (its postinstall `db:migrate` fails headless).
  - FlatConfig: `parserOptions` must live under `languageOptions.parserOptions`; `project: true` needs a `files: ['**/*.{ts,tsx}']` scoped block plus a `**/*.config.{js,mjs,cjs}` override with `project: false` and typed rules (`restrict-template-expressions` etc.) disabled.
  - A **global eslint 10.7.0** shadows repo-local 9.x; version-sensitive configs fail. Verifier now prefers `node_modules/.bin` local binaries for eslint/prettier/cspell.
  - Legacy `.eslintignore` → ESLintIgnoreWarning; migrate into flat-config `ignores:` and delete the file.
- cspell: `cspell lint --no-progress .` gives the Unknown-word list; high-frequency workspace/domain terms go into `cspell.json "words"` (was empty). Repo-name spellings like `libary` (university-libary-jsm) are intentional — added to words, not "fixed".
- Hook F821: `log_debug` was used in `session-auto-commit/hook.py` but not imported from `lib`. Pyright's "unknown import symbol" after adding it is a false positive (sys.path-injected `lib`); ruff F821 confirms clean.

### Phase 4 (verify — this run)

- Final sweep: **20/20 repos, 0 tooling-level failures** (timeout/missing tool/unexpected exit). All checkers complete end-to-end.
- Remaining counts are report-scope lint findings (curated debt, not auto-rewritten): root ruff 1557 (was 3167; 1611 auto-fixed pre-run + more now), ruff format 512 files, eslint 24, cspell domain terms, markdownlint prompt findings, per-repo eslint 482–744 in Banking/DSS.
