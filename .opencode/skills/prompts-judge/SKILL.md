---
author: Alexa
description: "Use when auditing prompt files (*.prompt.md) for correctness, quality, formatting, and completeness. Ensures all prompts meet the workspace standard."
license: MIT
metadata:
  hermes:
    category: qa
    tags:
      - prompts
      - judge
      - audit
      - quality
      - markdown
name: prompts-judge
tags:
  - prompts
  - judge
  - audit
  - quality
  - markdown
title: Prompts Judge
version: 1.0.0
---

# Prompts Judge

## Description

Audits all prompt files (*.prompt.md) in the `.github/prompts/` directory for correctness, quality, formatting, and completeness. Ensures every prompt meets the workspace standard for agent consumption.

## When to Use

- When new prompts are added to the library
- When prompt audit results are stale
- Before running a major deployment or release
- As part of the skills/judge audit pipeline

## Quality Rubric (0-100)

| Dimension       | Points | Criteria                                                    |
| --------------- | ------ | ----------------------------------------------------------- |
| Frontmatter     | 20     | Valid YAML with name, description, triggers, category       |
| Structure       | 20     | Proper headings, sections for context/instructions/examples |
| Content Quality | 20     | Clear, actionable, no placeholders or TODOs                 |
| Formatting      | 20     | Proper markdown, consistent style, valid syntax             |
| Completeness    | 20     | All required sections present, examples provided            |

## Scoring Criteria

### 95-100 (PASS)

- All dimensions satisfied
- No placeholders, all sections complete
- Follows naming conventions (kebab-case.prompt.md)

### 80-94 (WARN)

- Minor formatting issues or missing one section
- Content is usable but could be more specific

### 60-79 (FAIL)

- Missing required sections or formatting issues
- Contains TODO/placeholder text
- Naming convention violations

### Below 60 (FAIL - rewrite)

- Fundamentally broken structure
- Unusable content
- Multiple sections missing

## Workflow

1. Scan `.github/prompts/` for all `.prompt.md` files
2. Parse each file for YAML frontmatter validity
3. Check for all required sections (Context, Instructions, Examples, Edge Cases)
4. Verify naming conventions and file structure
5. Score each dimension
6. Generate summary report with pass/fail/warn counts
7. Flag specific issues for each failing prompt

## Usage

```bash
hermes prompts-judge
# Or:
hermes prompts-judge --path .github/prompts/
# Generates: .github/judge_results/prompts_audit.md
```

## Output

- `.github/judge_results/prompts_audit.json` — Machine-readable results
- `.github/judge_results/prompts_audit.md` — Human-readable report
- Summary with counts: PASS / WARN / FAIL by category

## Related Skills

- `skill-judge`: Scores individual skill files
- `plans-judge`: Audits plan files
- `specs-judge`: Audits spec files
- `audit-skills-judge-fix`: Full pipeline including prompt judge
