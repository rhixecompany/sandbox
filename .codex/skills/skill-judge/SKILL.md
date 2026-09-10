---
author: Alexa
description: "Use when scoring individual skills against quality criteria. Assigns a 0-100 score based on structure, completeness, and content quality."
license: MIT
metadata:
  hermes:
    category: qa
    tags:
    - skills
    - judge
    - scoring
    - quality
    - audit
name: skill-judge
tags:
- skills
- judge
- scoring
- quality
- audit
title: Skill Judge
version: 1.0.0
---

# Skill Judge

## Description

Scores individual skill files (SKILL.md) against a defined quality rubric. Assigns a 0-100 score based on five dimensions: structure, completeness, content quality, references, and verification.

## When to Use

- When evaluating a single skill's quality
- When a skill fails or warns in the audit pipeline
- Before publishing or sharing a skill
- As part of the batch skills remediation pipeline

## Quality Rubric (0-100)

| Dimension | Points | Criteria |
|-----------|--------|----------|
| Structure | 20 | YAML frontmatter (name, version, description, triggers, category), proper headings |
| Completeness | 20 | All required sections present (What it does, When to use, When NOT to use) |
| Content Quality | 20 | Clear instructions, no placeholders, actionable examples |
| References | 20 | Has a `references/` directory with relevant supporting files |
| Verification | 20 | Has verification checklist, test criteria, or acceptance gates |

## Scoring Criteria

### 95-100 (PASS)
- All 5 dimensions fully satisfied
- No placeholders or TODO markers
- References directory populated with 3+ files
- Verification checklist present and specific

### 80-94 (WARN)
- 3-4 dimensions fully satisfied
- Minor issues: missing one reference, vague instructions
- No critical gaps

### 60-79 (FAIL - needs remediation)
- 2-3 dimensions satisfied
- Missing required sections or references
- Contains TODO/placeholder text

### Below 60 (FAIL - needs rewrite)
- 1 or fewer dimensions satisfied
- Major structural gaps
- Unusable as-is

## Workflow

1. Read the SKILL.md file
2. Check YAML frontmatter for all required fields
3. Verify all required sections exist
4. Evaluate each dimension (0-20 points)
5. Sum total score (0-100)
6. Assign PASS/WARN/FAIL rating
7. Generate report with specific improvement suggestions

## Usage

```bash
hermes skill-judge <path-to-skill/SKILL.md>
# Or use as part of batch pipeline:
hermes batch-skill-judge --all
```

## Related Skills

- `audit-skills-judge-fix`: Full pipeline including judge, remediate, consolidate
- `batch-skills-remediation`: Remediate failing skills after judge scoring
- `prompts-judge`: Audits prompt files for quality
- `plans-judge`: Audits plan files for quality
- `specs-judge`: Audits spec files for quality
