---
name: breakdown-plan
title: Project Plan Breakdown
description: Generate a comprehensive project plan with Epic > Feature > Story/Enabler > Test hierarchy, dependencies, priorities, and automated tracking.
trigger: /breakdown-plan
version: 1.0.0
author: Hermes Agent
tags: 
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Generate a comprehensive project plan with Epic > Feature > Story/Enabler > Test hierarchy, dependencies, priorities, and automated tracking.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [GitHub Project Management Best Practices](#github-project-management-best-practices)
  - [Agile Work Item Hierarchy](#agile-work-item-hierarchy)
  - [Project Management Principles](#project-management-principles)
- [Input Requirements](#input-requirements)
  - [Core Feature Documents](#core-feature-documents)
  - [Related Planning Prompts](#related-planning-prompts)
- [Output Format](#output-format)
- [Epic Description](#epic-description)
- [Business Value](#business-value)
- [Epic Acceptance Criteria](#epic-acceptance-criteria)
- [Feature](#feature)
- [Definition of Done](#definition-of-done)
- [Labels](#labels)
- [Milestone](#milestone)
- [Estimate](#estimate)
  - [Feature Issue Template](#feature-issue-template)
- [Feature Description](#feature-description)
- [User Stories in this Feature](#user-stories-in-this-feature)
- [Technical Enablers](#technical-enablers)
- [Dependencies](#dependencies)
- [Acceptance Criteria](#acceptance-criteria)
- [Definition of Done](#definition-of-done)
- [Labels](#labels)
- [Epic#](#epic#)
- [Estimate](#estimate)
  - [User Story Issue Template](#user-story-issue-template)
- [Story Statement](#story-statement)
- [Acceptance Criteria](#acceptance-criteria)
- [Technical Tasks](#technical-tasks)
- [Test](#test)
- [Definition of Done](#definition-of-done)
- [Labels](#labels)
- [Feature](#feature)
- [Estimate](#estimate)
  - [Technical Enabler Issue Template](#technical-enabler-issue-template)
- [Enabler Description](#enabler-description)
- [Technical Requirements](#technical-requirements)
- [Implementation Tasks](#implementation-tasks)
- [User Stories Enabled](#user-stories-enabled)
- [Acceptance Criteria](#acceptance-criteria)
- [Definition of Done](#definition-of-done)
- [Labels](#labels)
- [Feature](#feature)
- [Estimate](#estimate)
  - [4. Priority and Value Matrix](#4-priority-and-value-matrix)
- [Sprint](#sprint)
- [Success Metrics](#success-metrics)
  - [Project Management KPIs](#project-management-kpis)
  - [Process Efficiency Metrics](#process-efficiency-metrics)
  - [Project Delivery Metrics](#project-delivery-metrics)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand off](#phase-4:-hand-off)
- [GitHub Project Management Best Practices](#github-project-management-best-practices)
- [Agile Work Item Hierarchy](#agile-work-item-hierarchy)
- [Project Management Principles](#project-management-principles)
- [Input Requirements](#input-requirements)
- [Core Feature Documents](#core-feature-documents)
- [Related Planning Prompts](#related-planning-prompts)
- [Output Format](#output-format)
- [Epic Description](#epic-description)
- [Business Value](#business-value)
- [Epic Acceptance Criteria](#epic-acceptance-criteria)
- [Feature](#feature)
- [Definition of Done](#definition-of-done)
- [Labels](#labels)
- [Milestone](#milestone)
- [Estimate](#estimate)
- [Feature Issue Template](#feature-issue-template)
- [Feature Description](#feature-description)
- [User Stories in this Feature](#user-stories-in-this-feature)
- [Technical Enablers](#technical-enablers)
- [Dependencies](#dependencies)
- [Acceptance Criteria](#acceptance-criteria)
- [Definition of Done](#definition-of-done)
- [Labels](#labels)
- [Epic#](#epic#)
- [Estimate](#estimate)
- [User Story Issue Template](#user-story-issue-template)
- [Story Statement](#story-statement)
- [Acceptance Criteria](#acceptance-criteria)
- [Technical Tasks](#technical-tasks)
- [Test](#test)
- [Definition of Done](#definition-of-done)
- [Labels](#labels)
- [Feature](#feature)
- [Estimate](#estimate)
- [Technical Enabler Issue Template](#technical-enabler-issue-template)
- [Enabler Description](#enabler-description)
- [Technical Requirements](#technical-requirements)
- [Implementation Tasks](#implementation-tasks)
- [User Stories Enabled](#user-stories-enabled)
- [Acceptance Criteria](#acceptance-criteria)
- [Definition of Done](#definition-of-done)
- [Labels](#labels)
- [Feature](#feature)
- [Estimate](#estimate)
- [4. Priority and Value Matrix](#4-priority-and-value-matrix)
- [Sprint](#sprint)
- [Success Metrics](#success-metrics)
- [Project Management KPIs](#project-management-kpis)
- [Process Efficiency Metrics](#process-efficiency-metrics)
- [Project Delivery Metrics](#project-delivery-metrics)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Issue Planning and Automation prompt that generates comprehensive project plans with Epic > Feature > Story/Enabler > Test hierarchy, dependencies, priorities, and automated tracking.


Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.


### Phase 1: Intake

- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute

- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify

- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off

- Return the final artifact or findings .
- Stop once the requested result is delivered.

## GitHub Project Management Best Practices

### Agile Work Item Hierarchy

- **Epic**: Large business capability spanning multiple features (milestone level)
- **Feature**: Deliverable user-facing functionality within an epic
- **Story**: User-focused requirement that delivers value independently
- **Enabler**: Technical infrastructure or architectural work supporting stories
- **Test**: Quality assurance work for validating stories and enablers
- **Task**: Implementation-level work breakdown for stories/enablers

### Project Management Principles

- **INVEST Criteria**: Independent, Negotiable, Valuable, Estimable, Small, Testable
- **Definition of Ready**: Clear acceptance criteria before work begins
- **Definition of Done**: Quality gates and completion criteria
- **Dependency Management**: Clear blocking relationships and critical path identification
- **Value-Based Prioritization**: Business value vs. effort matrix for decision making

## Input Requirements

Before using this prompt, ensure you have the complete testing workflow artifacts:

### Core Feature Documents

1. **Feature PRD**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}.md`
2. **Technical Breakdown**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/technical-breakdown.md`
3. **Implementation Plan**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/implementation-plan.md`

### Related Planning Prompts

- **Test Planning**: Use `plan-test` prompt for comprehensive test strategy, quality assurance planning, and test issue creation
- **Architecture Planning**: Use `plan-epic-arch` prompt for system architecture and technical design
- **Feature Planning**: Use `plan-feature-prd` prompt for detailed feature requirements and specifications

## Output Format

> Create two primary deliverables:>
>
> 1. **Project Plan**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/project
> **Full content:**`templates/breakdown-plan/output_format.md`

## Epic Description

Epic summary from PRD

## Business Value

- **Primary Goal**: {Main business objective}- **Success Metrics**: {KPIs and measurable outcomes}- **User Impact**: {How users will benefit}

## Epic Acceptance Criteria

- [ ] {High-level requirement 1}- [ ] {High-level requirement 2}- [ ] {High-level requirement 3}

## Feature

s in this Epic- [ ] #{feature-issue-number} - {Feature Name}

## Definition of Done

- [ ] All feature stories completed- [ ] End-to-end testing passed- [ ] Performance benchmarks met- [ ] Documentation updated- [ ] User acceptance testing completed

## Labels

- `epic`,

priority-level}`,`{value-tier}`

## Milestone

Release version/date

## Estimate

Epic-level t-shirt size: XS, S, M, L, XL, XXL}```

### Feature Issue Template

```markdown

# Feature: {Feature Name}

## Feature Description

Feature summary from PRD

## User Stories in this Feature

- [ ] #{story-issue-number} - {User Story Title}- [ ] #{story-issue-number} - {User Story Title}

## Technical Enablers

- [ ] #{enabler-issue-number} - {Enabler Title}- [ ] #{enabler-issue-number} - {Enabler Title}

## Dependencies

**Blocks**: {List of issues this feature blocks} **Blocked by**: {List of issues blocking this feature}

## Acceptance Criteria

- [ ] {Feature-level requirement 1}
- [ ] {Feature-level requirement 2}

## Definition of Done

- [ ] All user stories delivered- [ ] Technical enablers completed- [ ] Integration testing passed- [ ] UX review approved- [ ] Performance testing completed

## Labels

- `feature`,

priority-level}`, `{value-tier}`, `{component-name}`

## Epic#

epic-issue-number

## Estimate

Story points or t-shirt size}
```

### User Story Issue Template

```markdown

# User Story: {Story Title}

## Story Statement

As a **{user type}**, I want **{goal}** so that **{benefit}**.

## Acceptance Criteria

- [ ] {Specific testable requirement 1}
- [ ] {Specific testable requirement 2}
- [ ] {Specific testable requirement 3}

## Technical Tasks

- [ ] #{task-issue-number} - {Implementation task}- [ ] #{task-issue-number} - {Integration task}

## Test

ing Requirements- [ ] #{test-issue-number} - {Test implementation}

## Definition of Done

- [ ] Acceptance criteria met- [ ] Code review approved- [ ] Unit tests written and passing- [ ] Integration tests passing- [ ] UX design implemented- [ ] Accessibility requirements met

## Labels

- `user-story`,

priority-level}`, `frontend/backend/fullstack`, `{component-name}`

## Feature

#{feature-issue-number}

## Estimate

Story points: 1, 2, 3, 5, 8}
```

### Technical Enabler Issue Template

```markdown

# Technical Enabler: {Enabler Title}

## Enabler Description

Technical work required to support user stories

## Technical Requirements

- [ ] {Technical requirement 1}- [ ] {Technical requirement 2}

## Implementation Tasks

- [ ] #{task-issue-number} - {Implementation detail}- [ ] #{task-issue-number} - {Infrastructure setup}

## User Stories Enabled

This enabler supports:

- #{story-issue-number} - {Story title}- #{story-issue-number} - {Story title}

## Acceptance Criteria

- [ ] {Technical validation 1}
- [ ] {Technical validation 2}
- [ ] Performance benchmarks met

## Definition of Done

- [ ] Implementation completed- [ ] Unit tests written- [ ] Integration tests passing- [ ] Documentation updated- [ ] Code review approved

## Labels

- `enabler`,

priority-level}`, `infrastructure/api/database`, `{component-name}`

## Feature

#{feature-issue-number}

## Estimate

> {Story points or effort estimate}>

```

### 4. Priority and Value Matrix

> **Full content:** `templates/breakdown-plan/estimate.md`

## Sprint

N} Goal

> **Primary Objective**: {Main deliverable for this sprint}
> **Stories in Sprint**:
> **Full content:** `templates/breakdown-plan/sprint_n_goal.md`

## Success Metrics

### Project Management KPIs

- **Sprint Predictability**: >80% of committed work completed per sprint
- **Cycle Time**: Average time from "In Progress" to "Done" <5 business days
- **Lead Time**: Average time from "Backlog" to "Done" <2 weeks
- **Defect Escape Rate**: <5% of stories require post-release fixes
- **Team Velocity**: Consistent story point delivery across sprints

### Process Efficiency Metrics

- **Issue Creation Time**: <1 hour to create full feature breakdown
- **Dependency Resolution**: <24 hours to resolve blocking dependencies
- **Status Update Accuracy**: >95% automated status transitions working correctly
- **Documentation Completeness**: 100% of issues have required template fields
- **Cross-Team Collaboration**: <2 business days for external dependency resolution

### Project Delivery Metrics

- **Definition of Done Compliance**: 100% of completed stories meet DoD criteria
- **Acceptance Criteria Coverage**: 100% of acceptance criteria validated
- **Sprint Goal Achievement**: >90% of sprint goals successfully delivered
- **Stakeholder Satisfaction**: >90% stakeholder approval for completed features
- **Planning Accuracy**: <10% variance between estimated and actual delivery timeThis comprehensive GitHub project management approach ensures complete traceability from epic-level planning down to individual implementation tasks, with automated tracking and clear accountability for all team members.````

## Template References

Detailed templates in `templates/breakdown-plan/`:- `estimate.md`- `output_format.md`- `sprint_n_goal.md`

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

## Workflow

<content>

Same-family prompts:

- [`breakdown-epic-arch.prompt.md`](breakdown-epic-arch.prompt.md)
- [`breakdown-epic-pm.prompt.md`](breakdown-epic-pm.prompt.md)
- [`breakdown-feature-implementation.prompt.md`](breakdown-feature-implementation.prompt.md)
- [`breakdown-feature-prd.prompt.md`](breakdown-feature-prd.prompt.md)
- [`breakdown-test.prompt.md`](breakdown-test.prompt.md)

