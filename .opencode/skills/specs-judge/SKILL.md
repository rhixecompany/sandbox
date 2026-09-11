---
author: Alexa
description: "Use when auditing spec files (.hermes/specs/*.md) for quality, completeness, and adherence to the specification standard."
license: MIT
metadata:
  hermes:
    category: qa
    tags:
      - specs
      - judge
      - audit
      - quality
      - specification
name: specs-judge
tags:
  - specs
  - judge
  - audit
  - quality
  - specification
title: Specs Judge
version: 1.0.0
---

# Specs Judge

## Description

Audits specification files in `.hermes/specs/` for quality, completeness, and adherence to the specification standard. Ensures all specs are precise, testable, and serve as a solid foundation for implementation.

## When to Use

- When a new spec is created for a feature or system
- When reviewing existing specs for quality
- Before converting a spec to an implementation plan
- As part of the skills/judge audit pipeline

## Quality Rubric (0-100)

| Dimension    | Points | Criteria                                                                        |
| ------------ | ------ | ------------------------------------------------------------------------------- |
| Frontmatter  | 15     | Valid YAML with name, version, status, date, author                             |
| Clarity      | 20     | Requirements are unambiguous and precisely stated                               |
| Completeness | 20     | All required sections present (overview, requirements, constraints, acceptance) |
| Testability  | 20     | Each requirement has a verifiable acceptance criterion                          |
| Constraints  | 15     | Technical constraints, dependencies, and assumptions documented                 |
| Consistency  | 10     | Terminology consistent throughout, no contradictions                            |

## Scoring Criteria

### 95-100 (PASS)

- All dimensions satisfied
- Every requirement has a clear acceptance criterion
- No contradictions or ambiguous language
- All constraints documented

### 80-94 (WARN)

- Minor gaps in completeness or testability
- Some requirements lack explicit acceptance criteria
- Usable but could be more precise

### 60-79 (FAIL)

- Missing required sections or ambiguous requirements
- No acceptance criteria for major requirements
- Internal contradictions

### Below 60 (FAIL - rewrite)

- Fundamentally broken structure
- Most requirements are vague
- Cannot serve as implementation foundation

## Workflow

1. Scan `.hermes/specs/` for all `.md` files
2. Parse each file for YAML frontmatter validity
3. Check for all required sections (Overview, Requirements, Constraints, Acceptance Criteria)
4. Verify each requirement has a testable acceptance criterion
5. Check for terminology consistency and contradictions
6. Score each dimension
7. Generate summary report with pass/fail/warn counts
8. Flag specific issues for each failing spec

## Usage

```bash
hermes specs-judge
# Or:
hermes specs-judge --path .hermes/specs/
# Generates: .github/judge_results/specs_audit.md
```

## Related Skills

- `plans-judge`: Audits plan files
- `prompts-judge`: Audits prompt files
- `skill-judge`: Scores individual skills
- `audit-skills-judge-fix`: Full pipeline including specs judge
