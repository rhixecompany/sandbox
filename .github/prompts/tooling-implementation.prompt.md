---
name: tooling-implementation
title: "Full Tooling Implementation: python-quality / tooling-lint / tooling-config across ./ and subrepos"
description: 'Execute the tooling-implementation plan: verify, check, fix, and validate the python-quality, tooling-lint, and tooling-config stacks across the SandBox root and all projects/ subrepos, then write the artifact.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
  - skills
  - todo
scripts:
  - ~/AppData/Local/hermes/scripts/tooling_full_check.py
skills:
  - devops/tooling-implementation
  - software-development/executing-plans
  - software-development/executing-prompt-workflows
  - development/execute-workflow
  - software-development/python-quality
  - devops/tooling-lint
  - devops/tooling-config
---

# Full Tooling Implementation Workflow

## Goal

Execute the written plan at `.hermes/plans/2026-08-01_tooling-implementation.md` against the REAL workspace: verify the tooling matrix, run every checker, apply the FIX-scope changes, re-verify, and write the declared artifact. Deliver a working, verified tooling state — not a description of one.

## Context

- Workspace root `C:/Users/Alexa/Desktop/SandBox` + 14 `projects/*` git submodules. `hermes-profiles/` is gitignored and EXCLUDED from all tooling.
- Config matrix already landed: ruff/pyright ×9, eslint ×8, prettier ×7, cspell ×8, editorconfig ×14, pre-commit ×13, cliff.toml ×13.
- 3 MCP servers patched (temp-file capture, PATH augmentation, cspell v10 `lint` glob): `~/AppData/Local/hermes/scripts/{python_quality,tooling_lint,tooling_config}_mcp_server.py`.
- Baseline debt (2026-08-01): ruff lint root ~3167 errors (1611 safe-fixable), pyright 1428 errors, prettier 515 root files, cspell 179 root issues (domain terms), markdownlint MD012/MD026 in curated prompts.
- Shell is git-bash (MSYS) on Windows. Use POSIX syntax in terminal. Python venv = `python` (hermes venv, has mcp installed).

## Inputs

- Plan: `.hermes/plans/2026-08-01_tooling-implementation.md`
- Verifier: `~/AppData/Local/hermes/scripts/tooling_full_check.py`
- Quick commands: `~/AppData/Local/hermes/scripts/tooling-quick-commands.sh`
- Configs at root + per subrepo (see Context)

## Outputs

- **Artifact (REQUIRED):** `results/tooling-implementation.prompt.output.md` — per-phase findings, changes-applied with before/after, flagged-but-not-edited items, verification table.
- Updated plan with `status: completed` + verification table.
- Real file changes from FIX scope (ruff --fix, prettier --write, hook F821 fix, cspell words).

## Rules

1. **Truth is disk, not plan text.** Verify every assumption with terminal/read before acting (executing-plans Phase 0).
2. **FIX scope only** (safe, reversible): `ruff check --fix` safe fixes; `prettier --write` on root EXCLUDING `.github/prompts` (curated — add to `.prettierignore` first and document); real undefined-name (F821) bugs; cspell word additions for domain terms.
3. **REPORT scope** (flag, do NOT auto-edit): ruff non-fixable debt, pyright errors, markdownlint findings in curated prompts (`.enhance` pipeline owns them), cspell terms in docs/artifacts.
4. **Never touch** `hermes-profiles/`, `node_modules/`, `.git/`, `.env`, credentials.
5. **Subprocess capture on Windows:** if running node CLIs (prettier/cspell/eslint) via subprocess, capture via temp files + `CREATE_NO_WINDOW` + `stdin=DEVNULL` and prepend `C:\nvm4w\nodejs` + `%APPDATA%\npm` to PATH — `capture_output` deadlocks.
6. **cspell v10:** use `cspell lint "**/*"` (check is file-only; `--no-progress` removed).
7. **Markdownlint config filename** must be `.markdownlintrc.json` (server hardcodes it).
8. **Auto-advance:** the user committed to full scope in one request — do NOT pause between phases for approval unless a phase fails critically.
9. **Verify after each phase.** Re-run the verifier before and after fixes; record numbers.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `devops/tooling-implementation` | Umbrella workflow + pitfalls |
| `software-development/executing-plans` | Phase discipline, checkpoints, verification |
| `software-development/executing-prompt-workflows` | Executing this prompt artifact |
| `development/execute-workflow` | Script-backed workflow execution |
| `software-development/python-quality` | ruff/pyright specifics |
| `devops/tooling-lint` | eslint/prettier/cspell/markdownlint specifics |
| `devops/tooling-config` | gitignore/editorconfig/pre-commit/git-cliff specifics |

## Phases

### Phase 1: Verify plan, skills, scripts exist

Confirm `.hermes/plans/2026-08-01_tooling-implementation.md`, `~/AppData/Local/hermes/scripts/tooling_full_check.py`, `~/AppData/Local/hermes/scripts/tooling-quick-commands.sh`, and the three tooling skills are on disk. Record any missing item as a finding (do not fabricate).

### Phase 2: Baseline check (before)

Run `~/AppData/Local/hermes/scripts/tooling_full_check.py` end-to-end. Capture the report path and the per-repo issue counts. Any TOOLING FAIL rows (timeout / missing tool / unexpected exit) are BLOCKERS to fix now — they are tooling bugs, not findings.

### Phase 3: FIX scope

- `ruff check --fix` on root + all 9 python repos (safe fixes only).
- Add `.github/prompts` to root `.prettierignore`; then `prettier --write .` at root (prompts excluded). Count files touched.
- Fix the real F821 bug: `.github/hooks/session-auto-commit/hook.py` references undefined `log_debug` — locate the missing import and add it.
- Add workspace domain words (xamehi, comicwise, Dwolla, openrouter, rhixe, fintech, etc.) to root `cspell.json` `words`; fix real typos in prose (`libary` → `library`) but NOT repo names (add those to words instead).

### Phase 4: Re-verify (after)

Re-run the verifier. Record before/after counts for every checker that changed. Confirm no new TOOLING FAIL rows.

### Phase 5: Artifact + plan close

Write `results/tooling-implementation.prompt.output.md`: per-phase findings, changes-applied table (before/after), flagged-but-not-edited list with disposition, verification table (checker × before × after × status). Mark the plan `status: completed` and fill its Lessons Learned section.

## Steps

1. Read the plan file fully (Phase 1 of executing-prompt-workflows).
2. Run Phase 1 existence checks.
3. Run the verifier; record baseline into the artifact.
4. Apply Phase 3 FIX items one by one, verifying each with a targeted check.
5. Re-run the verifier; record after numbers.
6. Write the artifact; update the plan.

## Tasks

- [ ] Phase 1 verify plan/skills/scripts on disk
- [ ] Phase 2 baseline verifier run + report path captured
- [ ] Phase 3 ruff --fix applied + re-checked
- [ ] Phase 3 .prettierignore prompts exclusion + prettier --write applied
- [ ] Phase 3 hook F821 fixed + verified (ruff F821 clean on hook dir)
- [ ] Phase 3 cspell words added + root cspell re-run recorded
- [ ] Phase 4 re-verify: no tooling-level failures, before/after captured
- [ ] Phase 5 artifact written + plan status completed

## Actions

- `terminal` for all checker/fix runs (git-bash POSIX).
- `read_file`/`search_files` for discovery and verification.
- `patch` for targeted edits (hook.py, cspell.json, .prettierignore).
- `write_file` for the artifact and plan updates.

## Personas

- **Tech Lead**: owns FIX scope discipline (safe fixes only, report curated debt).
- **QA**: owns verification gates (verifier runs, before/after numbers).

## Personality

- Direct, evidence-first. Numbers from real tool output, never estimates.

## Best Practices

- One variable at a time: apply one FIX class, verify, then the next.
- Record before/after counts immediately after each verifier run.
- Flag (don't edit) anything needing a judgment call; document the disposition.

## Verification Checklist

- [ ] Verifier completes end-to-end with 0 tooling-level failures
- [ ] ruff check clean on `~/AppData/Local/hermes/scripts/tooling_full_check.py`
- [ ] Artifact written with before/after verification table
- [ ] Plan marked `status: completed`
- [ ] All FIX-scope changes reviewed via `git diff --stat`
- [ ] No curated prompt files modified by prettier
- [ ] No secrets, credentials, or `.env` touched

## Dependencies

- `ruff`, `pyright`, `eslint`, `prettier`, `cspell` v10, `markdownlint-cli2`, `pre-commit` available on PATH (venv + nvm4w + %APPDATA%\npm).

## Subgoals

1. Working verifier with real numbers
2. FIX-scope changes applied and verified
3. Artifact + completed plan
