---
name: best-practices
category: templates/_shared
version: 2.0.0
license: MIT
author: derived from user-communication-preferences + writing-clearly-and-concisely + prompt-management + tree.prompt.txt best practices
description: Cross-cutting best practices shared across all run-all-goals artifacts. tree.prompt.txt is PRIMARY source.
---

# Best Practices — Shared Template

> Sources: derived from `USER.md` (execution preferences) + `.hermes.md` (project rules) + `prompt-management` skill best practices + `writing-clearly-and-concisely` skill + **`tree.prompt.txt`** (cleanup-first execution, mjs->mts conversion, config validation). Verified by reading source rules; not synthesized.

## Communication Style (Verified From USER.md / User-Communication-Preferences)

- **Concise bullets first** — lead with result (`PASS` / `FAIL` / metric value) before explanation.
- **Table-first** — for comparisons, metrics, checklists; text paragraphs only when a single concept needs prose clarification.
- **No filler** — no `"Certainly!"`, `"I'd be happy to"`, `"Please note"`, `"As an AI..."`. Skip performative language (SOUL.md persona / identity rules).
- **Direct, opinionated** — express technical preference; signal dense (high signal / low noise ratio).
- **Signal-dense responses** — skip preamble; deliver result; brief explanation after.

## Code / Script Style (Verified From USER.md / Project Rules)

- **TypeScript strict** — strict mode enabled; no implicit `any`.
- **Python: PEP 8 / ruff** — `ruff format` + `ruff check --fix` before commit; `ruff` preferred over manual formatting.
- **JSDoc / docstring: `why` not `what`** — document the reason (`/** Why we skip level 2 heading — user requires sequential ordering */`), not what the line does (verified from `.hermes.md` / user profile).
- **No inline scripts** — `scripts/` directory only; scripts referenced by path, not pasted inline in prompt body.
- **No backup artifacts** — rely on git for rollback; `.env` files untouched unless explicitly requested (SOUL.md Section 12).

## Tree-Primary Execution Practices (From tree.prompt.txt)

- **Cleanup-First** — tree.prompt.txt defines cleanup-first execution. Always delete workspace clutter (.enhance, .goals, .hermes_diagnostics, .mcp, .*_cache, .worktrees, logs, etc.) before any construction or modification work.
- **mjs->mts Conversion** — Convert all *.mjs to *.mts as an early phase. No .mjs files should remain without .mts counterparts.
- **Config Validation** — Validate and update all config files (.editorconfig, .gitignore, .markdownlint, .prettier, *.toml, *.yaml, requirements.txt, tsconfig.json, package.json, pyrightconfig.json) as a dedicated phase.
- **Config Cleanup** — Delete *.json (except package.json, pyrightconfig.json), *-report.md, *.log, *.txt (skip *.prompt.txt files) early in the pipeline.
- **Source Migration** — Create src directory; migrate *.py/*.mjs/*.mts files into src and subdirectories.
- **Docs Cleanup** — Cleanup/update *.md files (PLAN.md, SOUL.md, SPEC.md, USER.md, docs) before final verification.

## Execution Discipline (Verified From SOUL.md / User-Communication-Preferences)

- **Read -> Patch -> Verify** — never write without reading current file contents first (`read_file` / `terminal cat`).
- **Atomic edits** — one `patch` per region; if region fails twice, rewrite enclosing function/file with `write_file` (do not retry same failing patch a 3rd time).
- **Batch independent calls** — issue independent `read_file` / `search_files` / `terminal` calls in same turn; only serialize when a later call depends on earlier result.
- **Verify gates** — never claim a phase complete without real tool output backing it (file read, git status, script PASS/FAIL line output).
- **State alignment** — update `.hermes/plans/` (this file) and session artifacts (`start.json` / `end.json` / `generate_session_report.py` where available) after each phase.

## Skill / Template Safety (Verified From Skill-Safety Rules / Skill-Judge Patterns)

- Skill must have >=10 line body + real description; no placeholder (`[SKILL_PRUNED]`) content left unreloaded.
- Before creating a new skill: `search_files` / `skills_list` to confirm no equivalent exists.
- Before referencing a template: `search_files` to confirm file exists on disk; if missing, document as missing — do NOT fabricate content.
- Batch fixes: dry-run first; verify `yaml.safe_load` after each batch; stop if >2 files corrupted by same regex pass.
- Multi-file (>=5 files): load 14 skills in order (`/using-superpowers` -> ... -> `/subagent-driven-development`) before execution; create plan doc; verify before execution; verify gates before claim.

## Quality Metrics (Verified From Skill-Judge / Audit Patterns)

- Target score: >=99 (skill-judge / audit pipeline verified reference).
- If score <95 after 2 consecutive passes with same HIGH issue: halt batch automation; switch to manual repair.
- Metrics must cite verified source line/file/command output (not estimated).
- tree.prompt.txt verification: all tree-specific checks (cleanup, mjs->mts, config validation) must PASS before claiming completion.
