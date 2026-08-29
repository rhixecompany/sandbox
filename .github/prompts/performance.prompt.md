---
name: performance
title: Performance Baseline and Optimization
description: Establishes measurable performance baselines, identifies high-impact bottlenecks, and applies targeted optimizations with before/after verification.
trigger: /performance
version: 1.0.0
author: Hermes Agent
tags:
  - performance
  - optimization
  - measurement
  - refactor
  - backend
  - frontend
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
  - [Phase 1: Baseline and Bottleneck Discovery](#phase-1:-baseline-and-bottleneck-discovery)
  - [Phase 2: Targeted Optimization](#phase-2:-targeted-optimization)
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



- [Goal](#goal)
- [Description](#description)
- [Context](#context)
- [Skills Required](#skills-required)
- [Subagents](#subagents)
- [Personas](#personas)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Baseline and Bottleneck Discovery](#phase-1:-baseline-and-bottleneck-discovery)
- [Phase 2: Targeted Optimization](#phase-2:-targeted-optimization)
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





Use when "Comprehensive performance prompt focused on measurable improvements and safe optimizations." to accomplish the associated tasks and objectives.

## Description

Improve application performance through measured, high-impact optimizations across data access, rendering, and caching paths.


Use this prompt when performance issues are suspected or when implementing features that can affect latency, throughput, bundle size, or query cost.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Performance profiling and bottleneck analysis
- Query and caching strategy optimization
- Frontend bundle and rendering optimization

## Subagents

| Subagent | Role | When to Use || --

- | --- | --- || Performance Analyst | Identifies bottlenecks and baseline metrics | Always || Data Optimizer | Improves DB/query and pagination behavior | Data-heavy changes || Frontend Optimizer | Reduces client bundle and render cost | UI-heavy changes |

## Personas

- Performance Analyst: Requires evidence before recommending optimization.
- Data Optimizer: Prioritizes caching, pagination, and query efficiency.
- Frontend Optimizer: Minimizes JS shipped to clients and avoids unnecessary hydration.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Measure before optimizing and report baseline and delta when possible.
- Prioritize highest-impact bottlenecks first.
- Use pagination for large result sets.
- Prefer server-side execution where possible to reduce client bundle size.
- Avoid speculative micro-optimizations without evidence.


### Phase 1: Baseline and Bottleneck Discovery

### Phase 2: Targeted Optimization

## Steps

1. Collect baseline metrics and identify hotspots.
2. Rank bottlenecks by user impact and frequency.
3. Implement minimal optimizations for top-ranked bottlenecks.
4. Re-measure and compare against baseline.
5. Document gains, limits, and next candidates.

## Tasks

- Task 1.1 — Establish baseline metrics for key paths.
- Task 1.2 — Identify and rank bottlenecks with evidence.
- Task 1.3 — Optimize queries, caching, rendering, or bundles where needed.
- Task 1.4 — Re-run measurements and verify non-regression.
- Task 1.5 — Record impact and future optimization backlog.

## Subtasks

- Subtask 1.1.1 — Capture latency, throughput, and resource usage indicators.
- Subtask 1.2.1 — Distinguish CPU, IO, and network constraints.
- Subtask 1.3.1 — Add pagination and caching for expensive read paths.
- Subtask 1.4.1 — Validate no change in correctness or security behavior.
- Subtask 1.5.1 — Summarize measurable wins and remaining bottlenecks.

## Actions Summary

1. Measure first.
2. Optimize the biggest bottlenecks only.
3. Re-measure and validate correctness.
4. Report measurable outcomes.

## Template References

Templates in `templates/performance/`:- `phases.md`

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