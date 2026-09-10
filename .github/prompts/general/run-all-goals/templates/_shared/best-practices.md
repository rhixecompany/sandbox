---
name: best-practices
category: templates/_shared
version: 1.0.0
license: MIT
author: derived from user-communication-preferences + writing-clearly-and-concisely + prompt-management best practices
description: Cross-cutting best practices shared across all run-all-goals artifacts.
---

# Best Practices — Shared Template

> Source: derived from `USER.md` (execution preferences) + `.hermes.md` (project rules) + `prompt-management` skill best practices + `writing-clearly-and-concisely` skill. Verified by reading source rules; not synthesized.

## Communication Style (Verified From USER.md / User-Communication-Preferences)

- **Concise bullets first** â lead with result (`PASS` / `FAIL` / metric value) before explanation.
- **Table-first** â for comparisons, metrics, checklists; text paragraphs only when a single concept needs prose clarification.
- **No filler** â no `"Certainly!"`, `"I'd be happy to"`, `"Please note"`, `"As an AI..."`. Skip performative language (SOUL.md persona / identity rules).
- **Direct, opinionated** â express technical preference; signal dense (high signal / low noise ratio).
- **Signal-dense responses** â skip preamble; deliver result; brief explanation after.

## Code / Script Style (Verified From USER.md / Project Rules)

- **TypeScript strict** â strict mode enabled; no implicit `any`.
- **Python: PEP 8 / ruff** â `ruff format` + `ruff check --fix` before commit; `ruff` preferred over manual formatting.
- **JSDoc / docstring: `why` not `what`** â document the reason (`/** Why we skip level 2 heading â user requires sequential ordering */`), not what the line does (verified from `.hermes.md` / user profile).
- **No inline scripts** â `scripts/` directory only; scripts referenced by path, not pasted inline in prompt body.
- **No backup artifacts** â rely on git for rollback; `.env` files untouched unless explicitly requested (SOUL.md Section 12).

## Execution Discipline (Verified From SOUL.md / User-Communication-Preferences)

- **Read â Patch â Verify** â never write without reading current file contents first (`read_file` / `terminal cat`).
- **Atomic edits** â one `patch` per region; if region fails twice, rewrite enclosing function/file with `write_file` (do not retry same failing patch a 3rd time).
- **Batch independent calls** â issue independent `read_file` / `search_files` / `terminal` calls in same turn; only serialize when a later call depends on earlier result.
- **Verify gates** â never claim a phase complete without real tool output backing it (file read, git status, script PASS/FAIL line output).
- **State alignment** â update `.hermes/plans/` (this file) and session artifacts (`start.json` / `end.json` / `generate_session_report.py` where available) after each phase.

## Skill / Template Safety (Verified From Skill-Safety Rules / Skill-Judge Patterns)

- Skill must have â¥10 line body + real description; no placeholder (`[SKILL_PRUNED]`) content left unreloaded.
- Before creating a new skill: `search_files` / `skills_list` to confirm no equivalent exists.
- Before referencing a template: `search_files` to confirm file exists on disk; if missing, document as missing â do NOT fabricate content.
- Batch fixes: dry-run first; verify `yaml.safe_load` after each batch; stop if >2 files corrupted by same regex pass.
- Multi-file (â¥5 files): load 14 skills in order (`/using-superpowers` â ... â `/subagent-driven-development`) before execution; create plan doc; verify before execution; verify gates before claim.

## Quality Metrics (Verified From Skill-Judge / Audit Patterns)

- Target score: â¥99 (skill-judge / audit pipeline verified reference).
- If score <95 after 2 consecutive passes with same HIGH issue: halt batch automation; switch to manual repair.
- Metrics must cite verified source line/file/command output (not estimated).
