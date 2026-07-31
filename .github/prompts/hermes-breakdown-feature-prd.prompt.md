---

name: hermes-breakdown-feature-prd

title: Hermes Breakdown Feature Prd

description: 'Hermes-equivalent: create a Feature PRD from a feature idea or parent epic.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

scripts: []

skills: []

formatter: default

plan: None

tags:

  - ai-assistant

  - frontend

  - ml

  - planning

  - prompts

  - specification

  - typescript

trigger: /hermes-breakdown-feature-prd

dependencies: []

metadata:

  hermes: {}

---

## Goal

Produce a feature PRD that is ready to hand off for implementation planning.

## Context

- Use when the user needs a structured `prd.md` for a single feature.
- Base the PRD on a parent epic or a clearly stated feature idea.
- Keep the content concrete and user-facing.
- Do not add implementation detail beyond what is needed for the PRD.

## Inputs

- Parent epic path or feature idea text

## Outputs

- `/docs/ways-of-work/plan/{epic-name}/{feature-name}/prd.md`

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. Include the feature name and the epic reference.
2. Describe the problem, solution, and intended impact.
3. Write user stories in a clear, testable form.
4. Include functional and non-functional requirements.
5. Include acceptance criteria using checklist items or Given/When/Then.
6. List out-of-scope items and dependencies.

## Phases

### Phase 1: Understand the feature

> **Goal:** capture the feature idea and the parent epic context.

## Actions Summary

1. Read the feature idea and epic context.
2. Draft the PRD structure and content.
3. Add stories, requirements, and acceptance criteria.
4. Verify completeness and file path.

## Template References

Templates in `templates/hermes-breakdown-feature-prd/`:- `phases.md`

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
