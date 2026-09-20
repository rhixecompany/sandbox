---
name: design-md-prompts
title: "PROMPTS — Design-MD feature prompts (design-md-20260919-212743)"
version: 1.0
date_created: 2026-09-19
last_updated: 2026-09-19
owner: Alexa
status: In progress
---

# Design-MD Prompts

## PROMPT-001 — Design-MD Scope → `docs/scope/design-md.md`

Role: scope maintainer. Create/update `docs/scope/design-md.md`: At a glance (design-md feature table), feature sections with Done when, checkbox tasks referencing `design-md` skill. Preserve identity (DRY refs: `.github/skills/claude-design/`, `AGENTS.md`, `.hermes.md`). Blockers honest.

## PROMPT-002 — Design Token Spec → Design artifacts

Role: design-token specialist. Author/update design-token artifacts using `design-md` rules (token categories: color, typography, spacing, layout, component; WCAG contrast verification; Tailwind/DTCG export). Reference workspace identity colors (`.hermes.md`). No synthetic claims.

## PROMPT-003 — Skill-Judge Audit → Design skills

Role: judge reviewer. Audit design-related skills (`design-md`, `creative` category). Score ≥98. Verify: frontmatter complete, description accurate, cross-references verified, no synthetic capabilities. Blockers: profile MISSING, MSYS2 FAIL, rate-limit 403, vision REJECTS.

## PROMPT-004 — Skills Overhaul Migration

Role: skills curator. Use `local-skills.txt` (generated from `hermes skills list --source local > ./local-skills.txt`). For skills without categories (`agentic-workflow`, `weather-plugin`): either assign category (from workspace categories) or delete if unneeded. Confirm deletion list before destructive action. Deduplicate (31 duplicate candidates — confirm before deletion). Keep only categorized skills.
