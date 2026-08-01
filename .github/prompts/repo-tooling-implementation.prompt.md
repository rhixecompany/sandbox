---
name: repo-tooling-implementation
title: "Repo Tooling Implementation (Prompt-Managed)"
description: 'Execute the repo-tooling master plan: per-repo PLAN.md/SPEC.md via prompt-management on repo-*.prompt.md, then full python-quality/tooling-config/tooling-lint implementation across ./ and subrepos, with verification gates. Runs AFTER scripts consolidation (Stage A) and artifact creation (Stage B).'
version: 1.0.0
license: MIT
author: Hermes Agent
trigger: /repo-tooling-implementation
tags:
  - repo
  - tooling
  - implementation
  - planning
  - prompt-management
toolsets:
  - browser
  - code_execution
  - file
  - mcp
  - terminal
  - web
scripts:
  - ~/AppData/Local/hermes/scripts/repo-plan-spec.py
  - ~/AppData/Local/hermes/scripts/repo-planning-quick-commands.sh
  - ~/AppData/Local/hermes/scripts/tooling_full_check.py
skills:
  - executing-plans
  - executing-prompt-workflows
  - prompt-management
  - repo-planning
  - tooling-implementation
  - python-quality
  - tooling-config
  - tooling-lint
---

# Repo Tooling Implementation (Prompt-Managed)

## Purpose

Fully implement the repo-tooling master plan (`.hermes/plans/2026-08-01_repo-tooling.md`):

1. Run prompt-management over the three `repo-*.prompt.md` prompts to produce per-repo plans and specs.
2. Implement the full tooling stack (`python-quality`, `tooling-config`, `tooling-lint`) across `./` and all `projects/` subrepos.
3. Debug, fix, and validate every bug, issue, error, and warning encountered.
4. Close with a verification report.

Strict ordering: planning artifacts BEFORE tooling fixes; verification AFTER fixes. Only then mark the master plan complete.

## Phase 1 — Per-Repo Plans + Specs

1. Load `repo-planning` skill and read `.github/prompts/repo-management.prompt.md`, `repo-research-pipeline.prompt.md`, `repo-story-time.prompt.md`.
2. Generate PLAN.md + SPEC.md for the root and every `projects/*/` subrepo:
   - `python ~/AppData/Local/hermes/scripts/repo-plan-spec.py --root` (dry-run) → `python ~/AppData/Local/hermes/scripts/repo-plan-spec.py --root --apply`
   - Never overwrite an existing PLAN.md/SPEC.md (generator already refuses).
3. Verify: `python .github/scripts/tooling_full_check.py --plans` → expect **0 failures** (all repos have valid PLAN.md + SPEC.md frontmatter).

**Gate 1: `--plans` reports zero plan/spec failures before proceeding.**

## Phase 2 — Tooling Implementation

1. Load `tooling-implementation` + `python-quality` + `tooling-config` + `tooling-lint` skills.
2. For each repo (root + subrepos), apply the applicable stack:
   - `python-quality`: ruff + pyright configs (`.ruff.toml`, `pyrightconfig.json`)
   - `tooling-config`: `.gitignore`, `.editorconfig`, `.pre-commit-config.yaml`, `cliff.toml`
   - `tooling-lint`: `eslint.config.mjs`, `.prettierrc.json`, `cspell.json`, `.markdownlintrc.json`
3. Only create where MISSING — never overwrite customized configs.
4. Follow the canonical configs: ruff py311/120 select E/F/I/N/W/UP/B/SIM/ARG/RUF ignore E501/N818; root excludes `projects/`, `hermes-profiles/`, generated dirs.

**Gate 2: config matrix verified on disk (no missing configs for detected stack) before checking.**

## Phase 3 — Check

1. Run the canonical verifier: `python ~/AppData/Local/hermes/scripts/tooling_full_check.py` (per-repo).
2. Also run: `ruff check .`, `ruff format --check .`, `eslint .`, `prettier --check .`, `cspell lint "**/*"`, `markdownlint-cli2 --config .markdownlintrc.json "**/*.md"`, `pre-commit validate-config`.
3. Record findings per repo with exit-code classification (exit 2 = TOOLING FAIL = blocker; findings-only exits 0/1 = data).

**Gate 3: zero TOOLING FAIL rows (timeout / missing tool / unexpected exit) across all repos.**

## Phase 4 — Fix (safe subset)

Fix ONLY:

- Config/ignore/deps bugs (missing files, invalid UTF-8, wrong filenames, missing deps)
- Safe auto-fixes: `ruff check --fix`, `prettier --write` on code-only globs (`**/*.{js,ts,jsx,tsx,json,jsonc,css,scss,html}`)
- Real undefined-name bugs (F821) and broken hook imports

REPORT (do not blindly rewrite):

- Remaining ruff unsafe-only fixes, pyright errors, markdownlint debt in curated prompts, cspell long-tail terms
- For each FIX, record before/after counts.

**Gate 4: fixes are FIX-scope only; curated debt is documented as REPORT.**

## Phase 5 — Validate + Close

1. Re-run `python ~/AppData/Local/hermes/scripts/tooling_full_check.py` → **0 tooling-level failures**.
2. Re-run `python ~/AppData/Local/hermes/scripts/tooling_full_check.py --plans` → **0 plan/spec failures**.
3. Update the master plan: fill Lessons Learned, bump version, set `status: completed`.
4. Write final verification report to `.github/scripts/reports/VERIFICATION_REPORT.md` with before/after counts. (Report dir stays in-repo; scripts live in `~/AppData/Local/hermes/scripts/`.)

**Gate 5: fresh sweeps green + master plan completed + verification report written.**

## Completion Criteria

- [ ] Per-repo PLAN.md + SPEC.md exist and validate (Gate 1)
- [ ] Tooling configs present for every applicable repo (Gate 2)
- [ ] Verifier completes with zero tooling-level failures (Gate 3)
- [ ] Safe fixes applied; debt classified REPORT (Gate 4)
- [ ] Fresh sweeps green, plan `status: completed`, verification report written (Gate 5)
- [ ] MCP servers still live after any path changes (kill python.exe respawn pattern)

## Constraints

- `C:/Users/Alexa/Desktop/SandBox` is the root; 14 `projects/` are git submodules — do NOT commit inside them unless asked.
- LF-only writes; `.gitattributes` `*.md eol=lf`.
- Run verifier fresh whenever evidence is questioned (no stale reports).
- Report blockers honestly; never fabricate results.
