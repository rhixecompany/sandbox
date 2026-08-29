---
name: refresh-agent-inventory
title: Refresh Agent Inventory
description: Refresh the workspace customization inventory by reconciling discovered assets against the canonical report and proposing precise edits for stale AGENTS and instruction references.
trigger: /refresh-agent-inventory
version: 1.0.0
author: Hermes Agent
tags: [inventory, agents, copilot, audit, remediation, workspace]
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
- [Description to accomplish the associated tasks and objectives.](#description-to-accomplish-the-associated-tasks-and-objectives)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Discover and compare](#phase-1:-discover-and-compare)
  - [Phase 2: Propose and apply scoped updates](#phase-2:-propose-and-apply-scoped-updates)
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
- [Description to accomplish the associated tasks and objectives.](#description-to-accomplish-the-associated-tasks-and-objectives)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Discover and compare](#phase-1:-discover-and-compare)
- [Phase 2: Propose and apply scoped updates](#phase-2:-propose-and-apply-scoped-updates)
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





Use when

## Description to accomplish the associated tasks and objectives.

## Description

Refresh the workspace customization inventory by reconciling discovered assetsagainst the canonical report, then propose precise edits for stale AGENTS andcopilot instruction references.


- Workspace is monorepo-style with root and subproject overrides.
- Canonical report path: - reports/copilot-skills-agents-hooks-plugins-prompts-instructions-report.md
- Primary customization files: - AGENTS.md - .github/copilot-instructions.md

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)- customization-audit- context-map

## Subagents

- Explore (optional): read-only discovery of inventory, duplicates, and stale references.

## Personas

- Maintainer persona: prioritize deterministic, low-risk edits.
- Auditor persona: prioritize verifiable findings with file evidence.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow nearest-file precedence for AGENTS and instructions.
- Link to existing documents instead of embedding long copied content.
- Keep edits minimal and scoped to customization files.
- If no changes are needed, output a no-op report with evidence.


### Phase 1: Discover and compare

| Field | Details || ---------

- | -------------------------------------------------------------------------- || Goal | Build a current inventory snapshot and compare it to the canonical report. || Inputs | Workspace files, report file, AGENTS.md, .github/copilot-instructions.md. || Outputs | Drift list with concrete path-level evidence. || Validation | Every drift item cites at least one path and one mismatch type. |

### Phase 2: Propose and apply scoped updates

| Field | Details || ---------

- | ------------------------------------------------------------------------ || Goal | Produce minimal customization-file updates that remove drift. || Inputs | Phase 1 drift list and current customization file contents. || Outputs | Patch-ready update plan and optional applied edits. || Validation | Updated references are path-valid and do not introduce duplicate assets. |

## Steps

1. Discover AGENTS.md files and customization assets under .github.
2. Read the canonical inventory report and compare counts and references.
3. Identify stale lists, missing paths, and duplicate-purpose customizations.
4. Prepare minimal edits for AGENTS.md and .github/copilot-instructions.md if needed.
5. Summarize outcomes as a remediation report.

## Tasks

- Task 1.1 — Discover AGENTS and customization asset files.
- Task 1.2 — Compare discovered inventory with report-backed counts and references.
- Task 2.1 — Draft minimal updates for stale customization references.
- Task 2.2 — Validate paths and precedence logic after updates.
- Task 2.3 — Publish remediation summary with risk notes.

## Subtasks

- Subtask 1.1.1 — Enumerate AGENTS files by workspace path.
- Subtask 1.2.1 — Record count deltas for instructions, prompts, and skills.
- Subtask 2.1.1 — Patch stale override lists and refresh commands.
- Subtask 2.2.1 — Verify no broken links or invalid paths in changed files.
- Subtask 2.3.1 — Report fixed items, remaining risks, and next actions.

## Actions Summary

- Discover current customization inventory.
- Compare against canonical report and precedence rules.
- Apply or propose minimal customization-file fixes.
- Deliver a concise remediation report with evidence.

## Template References

Templates in `templates/refresh-agent-inventory/`:- `phases.md`

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

- [`finalize-agent-prompt.prompt.md`](finalize-agent-prompt.prompt.md)
- [`multi-agent-research-template.prompt.md`](multi-agent-research-template.prompt.md)