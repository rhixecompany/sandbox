---
name: template-skill
title: Template Skill
description: Use when creating new skills from a lightweight template; includes minimal guidance.
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags:
      - imported
      - priority
    related_skills: []
---

# Template Skill

## Description

Use when creating new skills from a lightweight template; includes minimal guidance.

## When to Use

- Creating a new skill from scratch
- Standardizing skill format
- Using as template for new skills
- Learning skill structure
- Ensuring consistent formatting

## When NOT to Use

- Modifying existing skills
- Non-skill content
- Quick one-off tasks
- Real-time skill development

## Workflow

### Phase 1: Copy Template

- Copy template-skill directory
- Rename to new skill name
- Update frontmatter
- Customize structure

### Phase 2: Fill Content

- Write skill description
- Define when to use
- Add workflow phases
- Include tools and references

### Phase 3: Validate Format

- Check formatting consistency
- Verify all sections present
- Test skill triggering
- Review content

### Phase 4: Deploy

- Move to skills directory
- Register skill
- Test in environment
- Document skill

## Tools & References

- **Related Skills**: skill-creator, writing-skills
- **Template Location**: template-skill directory
- **Format**: SKILL.md structure
- **Guidelines**: Skill creation guidelines

## Best Practices

- Start with clear purpose
- Follow template structure
- Use consistent formatting
- Include examples
- Document workflow clearly
- Test before deploying
- Maintain and update regularly

## Overview

Lightweight skill template for scaffolding new skills with consistent structure. Provides minimal guidance to quickly create standardized skills with proper frontmatter, workflow phases, tools references, and best practices.

## Verification Checklist

- [ ] Template is correctly copied and renamed to the new skill name
- [ ] Frontmatter fields are updated (name, description, author, version)
- [ ] Workflow phases reflect the new skill's specific process
- [ ] Tools & References link to relevant related skills
- [ ] Skill renders correctly and triggers on expected queries
