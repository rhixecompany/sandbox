---
author: Alexa
description: "Use when auditing plan files (.hermes/plans/*.md) for quality, completeness, and adherence to the implementation plan standard."
license: MIT
metadata:
  hermes:
    category: qa
    tags:
      - plans
      - judge
      - audit
      - quality
      - implementation
name: plans-judge
tags:
  - plans
  - judge
  - audit
  - quality
  - implementation
title: Plans Judge
version: 1.0.0
---

# Plans Judge

## Description

Audits plan files in `.hermes/plans/` for quality, completeness, and adherence to the implementation plan standard. Ensures all plans are actionable, well-structured, and contain necessary checkpoints.

## When to Use

- When a new plan is created for a feature or project
- When reviewing existing plans for quality
- Before executing a plan
- As part of the skills/judge audit pipeline

## Quality Rubric (0-100)

| Dimension      | Points | Criteria                                                          |
| -------------- | ------ | ----------------------------------------------------------------- |
| Frontmatter    | 15     | Valid YAML with name, date, status, phases                        |
| Structure      | 20     | Phases, tasks, checkpoints clearly defined                        |
| Task Breakdown | 20     | Each task is actionable with clear deliverables                   |
| Verification   | 20     | Each phase has verification criteria/gates                        |
| Completeness   | 15     | All required sections present (overview, prerequisites, timeline) |
| Dependencies   | 10     | Task dependencies and ordering are clear                          |

## Scoring Criteria

### 95-100 (PASS)

- All dimensions satisfied
- Every task has clear deliverables and verification criteria
- Phases have explicit gates
- Dependencies documented

### 80-94 (WARN)

- Minor gaps in one dimension
- Missing verification criteria for 1-2 tasks
- Usable but could be more detailed

### 60-79 (FAIL)

- Missing required sections or vague task descriptions
- No verification criteria
- Unclear task ordering

### Below 60 (FAIL - rewrite)

- Fundamentally broken structure
- Most tasks are vague or missing
- No clear phases or gates

## Workflow

1. Scan `.hermes/plans/` for all `.md` files
2. Parse each file for YAML frontmatter validity
3. Check for all required sections (Overview, Phases, Tasks, Verification)
4. Verify each phase has explicit gates/checkpoints
5. Score each dimension
6. Generate summary report with pass/fail/warn counts
7. Flag specific issues for each failing plan

## Usage

```bash
hermes plans-judge
# Or:
hermes plans-judge --path .hermes/plans/
# Generates: .github/judge_results/plans_audit.md
```

## Related Skills

- `specs-judge`: Audits spec files
- `prompts-judge`: Audits prompt files
- `skill-judge`: Scores individual skills
- `audit-skills-judge-fix`: Full pipeline including plans judge
