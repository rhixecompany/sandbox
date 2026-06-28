---
name: skill-creator
title: Skill Creator
description: "Use when authoring, scaffolding, and validating in-repo SKILL.md files and skill assets."
version: 1.0.0
author: Hermes Agent
license: MIT
tags: [skills, authoring, scaffolding, validation]
metadata:
  hermes:
    tags: [skills, authoring, validation]
    related_skills: [writing-skills, skill-judge]
---

# Skill Creator

## Overview

Use this skill when authoring, scaffolding, validating, or improving in-repo skills. It covers skill lifecycle planning, structure, validation, and optional optimization.

## When to Use

- Creating a new skill from scratch
- Improving or editing an existing skill
- Running validation on a skill
- Benchmarking or comparing skill variants
- Publishing or packaging skill updates
- Reviewing prior art before adding a new skill

## When NOT to Use

- Using existing skills for regular tasks
- Non-skill document changes
- Operations that do not require skill lifecycle changes
- Editing prompt libraries or template artifacts outside skill scope

## Skills Required

| Skill | Purpose |
|-------|---------|
| `writing-skills` | Create clear skill prose and structure |
| `skill-judge` | Audit skills against quality criteria |

## Workflow

### Phase 1: Plan

1. Identify purpose and triggers.
2. Define acceptance criteria and intended use cases.
3. Plan structure: frontmatter, sections, references, templates, validation.
4. Validate against similar existing skills.

### Phase 2: Scaffold

1. Create `SKILL.md` with validated frontmatter.
2. Add required sections.
3. Add supporting files in `references/`, `templates/`, and `scripts/` where needed.

### Phase 3: Validate

1. Review behavior and intended outputs.
2. Run lightweight validation or checks.
3. Fix frontmatter, section ordering, and referenced paths.
4. Normalize style and markdown structure.

### Phase 4: Optimize If Needed

1. Improve `description` for discoverability.
2. Remove redundancy and improve clarity.
3. Benchmark if evaluation is required.
4. Revise if metrics or feedback indicate gaps.

## Outputs

- Valid scaffolded skill files
- Confirmed working frontmatter and section structure
- Updated references or templates

## Verification Checklist

- [ ] Skill has clear purpose, use cases, and structured workflow
- [ ] Frontmatter is complete and valid
- [ ] Files are created in expected locations
- [ ] Behavior matches intended use cases
- [ ] Quality bar matches related skills

## Pitfalls

- Avoid duplicate skills when similar prior art exists.
- Do not embed unchanged template boilerplate without adapting it to the skill.
- Avoid partial scaffolding and leaving the skill unreviewed.
