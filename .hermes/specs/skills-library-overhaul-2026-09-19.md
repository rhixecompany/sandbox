---
name: skills-library-overhaul-2026-09-19
title: "Skills Library Overhaul (categorize · dedupe · judge ≥98)"
description: "Inventory all local Hermes skills, categorize + migrate uncategorized skills, consolidate duplicates, delete leftovers, and raise every categorized skill to skill-judge ≥98"
version: 1.0.0
date_created: 2026-09-19
status: Approved
goal: "Skills/ → 100% categorized, 0 duplicates, skill-judge ≥98 on every categorized skill"
---
Plan: `.hermes/plans/skills-library-overhaul-2026-09-19.md` (verified 6446 B; live SKILL.md count 1285; categories 154; `local-skills.txt` 106340 B; scope `docs/scope/scope.md` 16527 B updated with link).

# Skills Library Overhaul Spec (2026-09-19)

## Goal

Bring the local Hermes skill library (`~/AppData/Local/hermes/skills/`, ~1106 skills per `hermes skills list --source local`) to a fully categorized, duplicate-free state where every categorized skill scores ≥98/100 under the skill-judge rubric (qa/skill-judge v1.1.0: Frontmatter 20 · Structure 20 · Content 20 · DRY 20 · References 20).

## Approved decisions (clarify 2026-09-19)

- A1 (delete policy): Migrate every uncategorized skill into a category folder FIRST; hard-delete only what remains uncategorized.
- A2 (dedupe policy): Consolidate by canonical name — merge knowledge into the best-named/rated copy; delete duplicate copies. Verify ≥2 paths exist before any deletion (skill-judge reference: 2026-06-22 pitfall).
- A3 (categories): Map to existing repo category conventions (dev→development, ops→devops, testing→qa, images→creative, docs→productivity, ai→mlops, agents→agent-* or development, etc.); present the full mapping table in the final report.
- A4 (judge scope): ALL categorized skills; iterative batches judge → fix files → re-judge until ≥98; progress artifact; documented exceptions list for unsalvageable stubs only.
- A5 (gate): One-shot execution after docs verified. Skills task first; then resume the 39-paste actionable queue.

## Requirements

- REQ-01: Run `hermes skills list --source local > ./local-skills.txt` (repo root CWD) and verify the file (non-empty, header rows, expected skill count).
- REQ-02: Enumerate the library with `find <skills_dir> -name SKILL.md` (authoritative for paths) AND frontmatter `name:`/`category:` extraction (authoritative for category attribution — `hermes skills list` reads the `category:` field, not folders).
- REQ-03: Categorization = BOTH: add `category: <name>` to YAML frontmatter AND physically migrate into `<skills>/<category>/<skill>/`.
- REQ-04: Duplicate detection: duplicate `name:` across SKILL.md files (`grep -rh "^name:" ... | sort | uniq -d`) + near-name similarity (camel/snake/prefix variants). Never delete the only copy of a name; compare line counts/frontmatter richness; richer copy is canonical.
- REQ-05: Consolidation merges unique knowledge (references, scripts, templates, pitfalls) into the canonical copy, then deletes the copies.
- REQ-06: After migration+dedupe, re-scan: 100% of remaining skills have `category:` and live in category folders; ZERO duplicate names. Delete any residual uncategorized (per A1).
- REQ-07: Judge baseline: `batch_skill_judge.py` (scripts_unified) full run → judge_results/baseline.tsv. Then iterative fix batches (7 skills/batch) → re-judge → until every categorized skill ≥98 (0-100 scale, skill-judge rubric).
- REQ-08: Fix patterns per skill-judge calibration (priority High→Medium→Low): frontmatter completeness (name/title/description≤500 starting 'Use when…'/version/author/license/tags), Skills Required table, ≥3 phased workflow, Pitfalls, Verification Checklist, substantive references/ (no stubs), SKILL.md <250 lines (DRY), no placeholder text, no orphaned `---` fragments, CRLF-normalized, fence-aware heading checks.
- REQ-09: Scoring floors: placeholder text ⇒ ≤60; missing verification checklist ⇒ ≤70; >250 lines ⇒ DRY cap 10/20. ≥98 requires all five dims ≈20 — depth (examples, references) beats structural padding.
- REQ-10: Progress artifact: `.hermes/results/judge_results/` (batches + summary.tsv) + plan checkbox updates per phase. Exceptions list (documented, final report) for unsalvageable stubs only.
- REQ-11: Reuse existing tooling: `scripts_unified/categorize_skills.py`, `dedupe_skills.py`, `consolidate_skills.py`, `batch_skill_judge.py` (inspect --help first; novel tooling only where they fall short).
- REQ-12: Deliverables in the final report: full category mapping table (old path → category → new path), dedupe/consolidation manifest (kept vs deleted, with proof of ≥2 copies), residual deletions (expected 0), score dashboard before → after, exceptions list, and live evidence of each verify gate.
- REQ-13: Non-goals: do not edit bundled/hub-installed skills irreversibly (patch-only for pinned), do not touch other profiles' skills, do not modify supermemory/mcp config, no key material in any artifact.

## Acceptance

- AC-01: `local-skills.txt` exists, parseable, count matches find-derived inventory within known list-vs-find delta.
- AC-02: Inventory report: per-skill category state, duplicate groups, mapping table.
- AC-03: 100% of skills categorized (frontmatter + folder); 0 duplicate names.
- AC-04: judge baseline recorded; every categorized skill ≥98 post-remediation (except documented exceptions).
- AC-05: No uncategorized skills remain; deletions limited to verified duplicate copies or A1 residuals.
- AC-06: All evidence real (script outputs), no synthetic scores; progress artifact current.
