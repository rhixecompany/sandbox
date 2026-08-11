---
name: hermes-breakdown-feature-implementation
title: Hermes Breakdown Feature Implementation
description: 'Hermes-equivalent: produce a Feature Implementation Plan from a Feature PRD.'
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
  - api
  - architecture
  - data
  - deployment
  - frontend
  - ml
  - prompts
  - security
  - specification
  - typescript
trigger: /hermes-breakdown-feature-implementation
dependencies: []
metadata:
  hermes: {}
---

## Goal

Turn a feature PRD into an implementation plan that an engineering team can execute.

## Context

- Use when the feature PRD is already available.
- Focus on architecture, data flow, API shape, and delivery considerations.
- Keep the plan grounded in the source PRD and any technical notes.
- Do not omit deployment or security concerns.

## Inputs

- Feature PRD path: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`
- Optional: `technical-breakdown.md`, implementation constraints

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. Keep the plan tied to the PRD requirements.
2. Include architecture, schema, API, frontend, deployment, security, and performance.
3. Use Mermaid where diagrams add clarity.
4. Make the API section concrete with request and response shapes.
5. Surface migration strategy and CI/CD considerations explicitly.
6. Keep the document easy to hand to an engineer.

## Phases

### Phase 1: Analyze the PRD

> **Goal:** extract the technical work implied by the feature.

## Actions Summary

1. Read and analyze the feature PRD.
2. Draft the implementation plan structure.
3. Add architecture, schema, API, UI, and delivery notes.
4. Review the draft for completeness and clarity.

## Template References

Templates in `templates/hermes-breakdown-feature-implementation/`:- `phases.md`

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
