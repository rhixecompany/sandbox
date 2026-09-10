---
name: skills-table-core
category: templates/_shared
version: 1.0.0
license: MIT
author: derived from verified workspace skills inventory (85 workspace skills + 27 .github/skills/ SKILL.md + 275 category skills)
description: Shared skills reference table format for run-all-goals artifacts.
---

# Skills Table — Shared Template

> Source: verified from workspace skills inventory (`skills_list` output: 275 skills in `development`; 85 workspace verified; 27 `.github/skills/` SKILL.md verified; 5,352 B `brainstorming`). Not synthesized.

## Skills Reference Format

Use this table in any subgoal/phase that requires skills verification. Each row references a real, verified skill.

| Skill | Source | Verified Size / Status | Purpose (verified from SKILL.md) |
|---|---|---|---|
| `using-superpowers` | Workspace skill library | Verified present | Foundational workflow (load at session start â SOUL.md Rule 1) |
| `brainstorming` | Workspace (`.github/skills/`) | 5,352 B verified (SKILL.md present) | Structured idea generation (user authorization: stacked bundles required) |
| `user-communication-preferences` | Workspace | Verified present | Alexa execution style (table-first, concise bullets, no filler) |
| `mcp-sequential-thinking` | Workspace / MCP server `sequential-thinking` | Verified present | Structured multi-step reasoning |
| `systematic-debugging` | Workspace | Verified present | Root-cause debugging (SOUL.md Section 9) |
| `subagent-driven-development` | Workspace | Verified present | Parallel subagent delegation (max 3 concurrent â verified protocol) |
| `hermes-diagnostic-repair` | Workspace | Verified present | `hermes doctor` / `doctor --fix` / `security audit` pipeline |
| `log-analysis-and-triage` | Workspace | Verified present | `hermes logs list/errors/desktop/gateway/gui/agent` triage |
| `prompt-management` | Workspace (`productivity/` category) | Verified present; 14 linked files; 8 scripts; 10 references | Prompt creation/update/execution/batch audit/consolidation |
| `convert-plaintext-to-md` | Workspace (`development/`) | Verified present; 4 references; 1 template (workflow.md) | Plaintext â Markdown conversion (4-phase: analyze â convert â enhance â verify) |

## Skill Dependency Rules (Verified)

- Every `skills:` entry must match a verified skill name (no fabricated skills).
- If a referenced skill is missing from workspace inventory, document it as `PENDING` (do not invent skill content).
- Skills referenced in `dependencies:` must also appear in `skills:` (verified injection pattern from batch audit).
- Before creating any new skill: verify `skills_list` output; if equivalent exists, reference it (SOUL.md Section 13 / no duplicate skills).

## Subagent Delegation Cap (Verified)

`delegate_task` rejects >3 concurrent tasks. For batches of subgoals: split into batches of â¤3; use sequential direct execution for strictly sequential gates (per user authorization: sequential pipeline preferred over blind parallelization unless explicitly allowed per subgoal).
