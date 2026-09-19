---
name: skills-library-overhaul
title: "Skills Library Overhaul Pipeline"
description: "Executable prompt: snapshot skills list, analyze, categorize+migrate, dedupe+consolidate, delete residuals, judge-fix-rejudge every categorized skill to ≥98, report"
version: 1.0.0
date_created: 2026-09-19
status: active
---

# Skills Library Overhaul Pipeline Prompt

You are executing the approved skills-library overhaul (spec/plan 2026-09-19, clarify A1-A5). Library: `~/AppData/Local/hermes/skills/`. Judge rubric: `qa/skill-judge` (5 dims × 20; /skill-judge <name> or --batch). Do NOT edit bundled/hub skills irreversibly (patch-only). Never delete the only copy of a skill name (verify ≥2 paths first).

## STEPS

1. SNAPSHOT: `cd ~/Desktop/SandBox && hermes skills list --source local > ./local-skills.txt`. Verify non-empty; record list count vs `find ~/AppData/Local/hermes/skills -name SKILL.md | wc -l`.
2. ANALYZE: python inventory over the skills dir (CRLF-normalize; frontmatter `name:`/`category:`; path; lines; mtime). Output `.hermes/results/skills-inventory-2026-09-19.json/md` + duplicate-name groups + uncategorized sets. Build the full category assignment table (conventions: dev→development, ops→devops, testing→qa, images→creative, docs→productivity, ai→mlops, web→web-development, research→research, fonts/tools→misc) → `.hermes/results/skills-category-map-2026-09-19.md`.
3. CATEGORIZE+MIGRATE: patch frontmatter `category:`; move each skill into `skills/<category>/<name>/`. Prefer `scripts_unified/categorize_skills.py` — inspect `--help` first; always dry-run before real run.
4. DEDUPE: for each duplicate name: prove ≥2 paths, canonical = richer file (more lines/version/license/metadata), merge unique references into canonical, delete copies; record manifest.
5. DELETE RESIDUALS: any remaining uncategorized (no category: and flat-root) → hard delete per A1; expected 0. Log each.
6. JUDGE LOOP (the long pole): baseline via `scripts_unified/batch_skill_judge.py` (fix its known pitfalls: SKILL.md double-append, CRLF, fence-aware headings) → sort ascending → batches of 7 → fix (frontmatter → Skills Required → phases ≥3 → Pitfalls → Verification Checklist → references substantive → <250 lines → no placeholders → remove stray `---` fragments) → re-judge → update `.hermes/results/judge_results/summary.tsv`. Iterate until all ≥98 or documented exceptions (two failed fix passes). Parallel-safe: delegate independent batches to subagents with the rubric copied into their context.
7. VERIFY + REPORT: re-scan (100% categorized, 0 dups); score dashboard before→after; mapping table + dedupe manifest + deletions in the final report; then resume the 39-paste actionable queue.

## RULES

- Evidence only: every claim backed by script output; no synthetic scores.
- Judge floors: placeholder ⇒ ≤60; missing checklist ⇒ ≤70; >250 lines ⇒ DRY 10/20.
- Any deletion requires proof (≥2 paths for dups; A1 residual for uncategorized).
- Keep the progress artifact current after every batch; plan checkboxes updated.
- Never hardcode keys or touch other profiles; no key material in artifacts.