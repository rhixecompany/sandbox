---
name: hermes-breakdown-test
title: Hermes Breakdown Test
description: 'Hermes-equivalent: generate a test strategy, issue checklist, and QA plan from feature artifacts.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - ai-assistant
  - debugging
  - frontend
  - generator
  - ml
  - planning
  - prompts
  - specification
  - testing
  - typescript
trigger: /hermes-breakdown-test
dependencies: []
metadata:
  hermes: {}
---

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
|| ------- | ----------- ||
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
|| --- | ------ | ----------- ||
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
|| ------- | --------- ||
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
