---
agent: "agent"
description: "Issue Planning and Automation prompt that generates comprehensive project plans with Epic > Feature > Story/Enabler > Test hierarchy, dependencies, priorities, and automated tracking."
---

## Goal

Issue Planning and Automation prompt that generates comprehensive project plans with Epic > Feature > Story/Enabler > Test hierarchy, dependencies, priorities, and automated tracking.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

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
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Legacy Prompt Details
````text
# GitHub Issue Planning & Project Automation Prompt

## Goal

Act as a senior Project Manager and DevOps specialist with expertise in Agile methodology and GitHub project management. Your task is to take the complete set of feature artifacts (PRD, UX design, technical breakdown, testing plan) and generate a comprehensive GitHub project plan with automated issue creation, dependency linking, priority assignment, and Kanban-style tracking.

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

> Create two primary deliverables:
> 1. **Project Plan**: `/docs/ways-of-work/plan/{epic-name}/{feature-name}/project

> **Full content:** `templates/breakdown-plan/output_format.md`

## Epic Description

{Epic summary from PRD}

## Business Value

- **Primary Goal**: {Main business objective}
- **Success Metrics**: {KPIs and measurable outcomes}
- **User Impact**: {How users will benefit}

## Epic Acceptance Criteria

- [ ] {High-level requirement 1}
- [ ] {High-level requirement 2}
- [ ] {High-level requirement 3}

## Features in this Epic

- [ ] #{feature-issue-number} - {Feature Name}

## Definition of Done

- [ ] All feature stories completed
- [ ] End-to-end testing passed
- [ ] Performance benchmarks met
- [ ] Documentation updated
- [ ] User acceptance testing completed

## Labels

`epic`, `{priority-level}`, `{value-tier}`

## Milestone

{Release version/date}

## Estimate

{Epic-level t-shirt size: XS, S, M, L, XL, XXL}
```

### Feature Issue Template

```markdown
# Feature: {Feature Name}

## Feature Description

{Feature summary from PRD}

## User Stories in this Feature

- [ ] #{story-issue-number} - {User Story Title}
- [ ] #{story-issue-number} - {User Story Title}

## Technical Enablers

- [ ] #{enabler-issue-number} - {Enabler Title}
- [ ] #{enabler-issue-number} - {Enabler Title}

## Dependencies

**Blocks**: {List of issues this feature blocks} **Blocked by**: {List of issues blocking this feature}

## Acceptance Criteria

- [ ] {Feature-level requirement 1}
- [ ] {Feature-level requirement 2}

## Definition of Done

- [ ] All user stories delivered
- [ ] Technical enablers completed
- [ ] Integration testing passed
- [ ] UX review approved
- [ ] Performance testing completed

## Labels

`feature`, `{priority-level}`, `{value-tier}`, `{component-name}`

## Epic

#{epic-issue-number}

## Estimate

{Story points or t-shirt size}
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

- [ ] #{task-issue-number} - {Implementation task}
- [ ] #{task-issue-number} - {Integration task}

## Testing Requirements

- [ ] #{test-issue-number} - {Test implementation}

## Dependencies

**Blocked by**: {Dependencies that must be completed first}

## Definition of Done

- [ ] Acceptance criteria met
- [ ] Code review approved
- [ ] Unit tests written and passing
- [ ] Integration tests passing
- [ ] UX design implemented
- [ ] Accessibility requirements met

## Labels

`user-story`, `{priority-level}`, `frontend/backend/fullstack`, `{component-name}`

## Feature

#{feature-issue-number}

## Estimate

{Story points: 1, 2, 3, 5, 8}
```

### Technical Enabler Issue Template

```markdown
# Technical Enabler: {Enabler Title}

## Enabler Description

{Technical work required to support user stories}

## Technical Requirements

- [ ] {Technical requirement 1}
- [ ] {Technical requirement 2}

## Implementation Tasks

- [ ] #{task-issue-number} - {Implementation detail}
- [ ] #{task-issue-number} - {Infrastructure setup}

## User Stories Enabled

This enabler supports:

- #{story-issue-number} - {Story title}
- #{story-issue-number} - {Story title}

## Acceptance Criteria

- [ ] {Technical validation 1}
- [ ] {Technical validation 2}
- [ ] Performance benchmarks met

## Definition of Done

- [ ] Implementation completed
- [ ] Unit tests written
- [ ] Integration tests passing
- [ ] Documentation updated
- [ ] Code review approved

## Labels

`enabler`, `{priority-level}`, `infrastructure/api/database`, `{component-name}`

## Feature

#{feature-issue-number}

## Estimate

> {Story points or effort estimate}
> ### 4. Priority and Value Matrix

> **Full content:** `templates/breakdown-plan/estimate.md`

## Sprint {N} Goal

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
- **Planning Accuracy**: <10% variance between estimated and actual delivery time

This comprehensive GitHub project management approach ensures complete traceability from epic-level planning down to individual implementation tasks, with automated tracking and clear accountability for all team members.

````


## Template References

Detailed templates in `templates/breakdown-plan/`:
- `estimate.md`
- `output_format.md`
- `sprint_n_goal.md`
