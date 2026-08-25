---
title: Goal
description: Prompt for goal
date: '2026-08-25'
tags:
- prompt
version: 1.0.0
author: Hermes Agent
---
# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Read the feature artifacts](#phase-1:-read-the-feature-artifacts)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)


## Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Read the feature artifacts](#phase-1:-read-the-feature-artifacts)
- [Actions Summary](#actions-summary)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)




## Goal

Produce a QA package that turns feature artifacts into a clear test strategy and issue checklist.

## Context

- Use when feature planning needs QA structure and test coverage guidance.
- Prefer concrete, implementation-aware but not implementation-bound test planning.
- Keep the output useful for QA, engineering, and issue triage.
- Align the strategy with the available feature artifacts.

## Inputs

- Feature PRD path
- `technical-breakdown.md`
- `implementation-plan.md` (recommended)

## Outputs

- `/docs/ways-of-work/plan/{epic}/{feature}/test-strategy.md`
- `/docs/ways-of-work/plan/{epic}/{feature}/test-issues-checklist.md`
- `/docs/ways-of-work/plan/{epic}/{feature}/qa-plan.md`

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. Include test scope and quality-risk mapping.
2. Use ISTQB-style technique selection where helpful.
3. Map the feature to ISO25010 quality characteristics.
4. Include environment, data, and CI/CD considerations.
5. Provide concrete issue templates for unit, integration, e2e, performance, and security coverage.
6. Include labeling and prioritization guidance.

## Phases

### Phase 1: Read the feature artifacts

> **Goal:** understand the feature and the likely QA surface.

## Actions Summary

1. Read the feature artifacts.
2. Draft the test strategy, checklist, and QA plan.
3. Add risk mapping and coverage guidance.
4. Verify completeness and path correctness.

## Template References

Templates in `templates/hermes-breakdown-test/`:- `phases.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

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

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

Same-family prompts:

- [`hermes-breakdown-epic-arch.prompt.md`](hermes-breakdown-epic-arch.prompt.md)
- [`hermes-breakdown-epic-pm.prompt.md`](hermes-breakdown-epic-pm.prompt.md)
- [`hermes-breakdown-feature-implementation.prompt.md`](hermes-breakdown-feature-implementation.prompt.md)
- [`hermes-breakdown-feature-prd.prompt.md`](hermes-breakdown-feature-prd.prompt.md)
- [`hermes-breakdown-plan.prompt.md`](hermes-breakdown-plan.prompt.md)
- [`hermes-comprehensive-setup.prompt.md`](hermes-comprehensive-setup.prompt.md)
- [`hermes-doctor-systematic-debugging.prompt.md`](hermes-doctor-systematic-debugging.prompt.md)