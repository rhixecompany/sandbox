---
name: writing-skills
title: Writing Skills
description: Use when crafting prompts, guidelines, and examples for writing effective in-repo skills.
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags:
      - imported
      - priority
    related_skills: []
---## Goal
crafting prompts, guidelines, and examples for writing effective in-repo skills. to accomplish the associated tasks and objectives.


# Writing Skills

## Description

Use when creating new skills, editing existing skills, or verifying skills work before deployment. Guides skill creation, improvement, and quality assurance.

## When to Use

- Creating new skills from scratch
- Editing or improving existing skills
- Verifying skills work correctly
- Deploying skills
- Maintaining skill library
- Ensuring skill quality

## When NOT to Use

- Using existing skills
- Non-skill development
- Quick one-off tasks
- Real-time skill testing

## Workflow

### Phase 1: Plan Skill

- Identify skill purpose
- Define use cases
- Plan structure
- Outline workflow

### Phase 2: Create Skill

- Write SKILL.md file
- Define sections
- Create workflow
- Add references

### Phase 3: Test & Validate

- Test skill triggering
- Verify workflow
- Check documentation
- Get feedback

### Phase 4: Deploy & Maintain

- Deploy skill
- Monitor usage
- Gather feedback
- Update as needed

### Phase 5: Audit Library (Periodic Maintenance)

Run this systematic scan across the entire skills library to catch structural issues:

1. **Inventory** — `hermes skills list` catalogs all skills, sources (builtin vs local), and status
2. **Duplicate detection** — Compare `hermes skills list` against the directory tree; check for skills existing in both root-level (uncategorized) and categorized paths
3. **Frontmatter integrity** — Scan for embedded line-numbered content (`"1|---"` or `"1|#"` patterns in the content body using grep)
4. **Completeness check** — Detect skills with `(To be filled.)` placeholders in Overview/Verification sections
5. **Category consistency** — Verify all local skills live under a category directory, not at root level
6. **Dependency verification** — Cross-reference `related_skills` entries to ensure referenced skills still exist
7. **Remove orphaned duplicates** — When a root-level v1.0.0 skill has a categorized v1.1.0 replacement, remove the old root copy

## Tools & References

- **Related Skills**: skill-creator, skill-judge
- **Skill Format**: SKILL.md structure
- **Template**: template-skill for reference
- **Standards**: Skill quality standards
- **Reference**: `references/skills-library-auditing.md` — detailed commands and patterns

## Best Practices

- Start with clear purpose
- Follow skill format
- Test thoroughly
- Document clearly
- Get peer review
- Maintain and update
- Archive old versions
- Audit the skills library periodically — structural issues compound over time
- Fix frontmatter corruption immediately when detected — it degrades skill rendering
- When consolidating duplicates, confirm the newer version is fully functional first

## Overview

Skill authoring guide for creating, editing, and maintaining the skills library. Covers the full lifecycle from planning and creation through testing, deployment, and periodic library auditing.

## Verification Checklist

- [ ] Skill has clear purpose and well-defined use cases
- [ ] SKILL.md follows the standard format with all required sections
- [ ] Skill triggers correctly on expected query patterns
- [ ] Documentation is clear, complete, and up to date
- [ ] Skills library is periodically audited for structural issues
