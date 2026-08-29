---
name: prompts-strict-template
title: Prompts Strict Template
description: Normalize and validate .prompt.md files against the strict required structure, enforcing section order, phase table format, and Task/Subtask numbering without losing intent.
trigger: /prompts-strict-template
version: 1.0.0
author: Hermes Agent
tags: [prompts, template, normalization, validation, lint, refactor]
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
date: '2026-08-25'
---
## Table of Contents

## Goal

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Structural Intake](#phase-1:-structural-intake)
  - [Phase 2: Template Normalization](#phase-2:-template-normalization)
- [Steps](#steps)
- [Tasks](#tasks)
- [Subtasks](#subtasks)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Structural Intake](#phase-1:-structural-intake)
- [Phase 2: Template Normalization](#phase-2:-template-normalization)
- [Steps](#steps)
- [Tasks](#tasks)
- [Subtasks](#subtasks)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Use when "Comprehensive prompt for enforcing strict .prompt.md template structure and formatting rules." to accomplish the associated tasks and objectives.

## Description

Normalize and validate prompt markdown files so they follow the repository's strict required structure, section order, phase table format, and task numbering conventions.


Use this prompt when creating, editing, reviewing, or repairing files that match .prompt.md naming conventions.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Markdown structure and lint-aware formatting
- Template compliance verification
- Controlled normalization without intent loss

## Subagents

| Subagent | Role | When to Use || --

- | --- | --- || Template Enforcer | Applies required section order and presence checks | Always || Structure Validator | Validates phase tables and numbering syntax | Always || Intent Preserver | Prevents semantic drift during normalization | Existing prompt migrations |

## Personas

- Template Enforcer: Treats required section order as non-negotiable.
- Structure Validator: Rejects malformed phases, tables, and numbering patterns.
- Intent Preserver: Keeps original prompt purpose and guidance intact.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Ensure all required top-level sections exist and are non-empty.
- Keep required section order exact.
- Include at least one phase with required Field/Details table and mandatory rows.
- Enforce Task N.x and Subtask N.x.y numbering patterns.
- Preserve source intent and wording as much as possible.


### Phase 1: Structural Intake

Inventory the target `.prompt.md` before editing: parse its frontmatter (name/trigger/description/dependencies), list its top-level `##` sections in order, and compare against the 11 required sections — flagging any that are missing, extra, or out of order. Also inspect each Phase block for a Field/Details table with the mandatory `Phase`/`Input`/`Output`/`Validation` rows and check `Task N.x` / `Subtask N.x.y` numbering. Emits a drift report; mutates nothing.

### Phase 2: Template Normalization

Apply the Phase 1 findings: insert missing sections in exact required order, reorder out-of-order ones, give every Phase a Field/Details table with the four mandatory rows, and rewrite list items to strict `Task N.x` / `Subtask N.x.y` numbering. Then run `enhance-markdown`-style checks, preserve the source's intent and wording, and emit a compliance report. Safe to re-run (idempotent).

> **Full content:** `templates/prompts-strict-template/phases.md`

## Steps

1. Parse prompt content and compare with strict template requirements.
2. Add missing sections in exact required order.
3. Normalize phase formatting and table rows.
4. Correct Tasks and Subtasks numbering syntax.
5. Validate final structure and preserve original intent.

## Tasks

- Task 1.1 — Detect missing or out-of-order top-level sections.
- Task 1.2 — Ensure Phase sections include required table schema and rows.
- Task 1.3 — Normalize Tasks and Subtasks numbering patterns.
- Task 1.4 — Preserve source intent while restructuring content.
- Task 1.5 — Produce final compliance validation output.

## Subtasks

- Subtask 1.1.1 — Check exact sequence of all 11 required sections.
- Subtask 1.2.1 — Verify Goal, Inputs, Outputs, and Validation rows exist.
- Subtask 1.3.1 — Rewrite list entries to Task N.x and Subtask N.x.y format.
- Subtask 1.4.1 — Retain meaningful prompt semantics and role guidance.
- Subtask 1.5.1 — Confirm no new markdown diagnostics were introduced.

## Actions Summary

1. Detect structural drift.
2. Normalize to strict template.
3. Validate numbering and phase tables.
4. Deliver compliance-preserving updates.

## Template References

Templates in `templates/prompts-strict-template/`:- `phases.md`

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`prompts-fix.prompt.md`](prompts-fix.prompt.md)