---
name: template
title: Template
description: "Use as a starting template when creating a new skill. Provides the standard SKILL.md structure with frontmatter, sections, and format guidelines."
---

# Template Skill

## Overview

This is the **starter template** for creating new skills. Copy this file to a new skill directory and fill in the content.

## When to Use

- Creating a new skill from scratch
- Adding a new process, pattern, or reference guide

## Structure

### Frontmatter (Required)

## `yaml

name: skill-name description: "Use when [specific triggering conditions] — keep under 500 chars, start with 'Use when...'"

---

`plaintext **Required fields:** `name`, `description`

**Optional fields:** `license`, `version`, `author`, `type`, `category`, `tags`

### Body Sections (Suggested)

1. **Overview** — What this skill does in 1-2 sentences
2. **When to Use** — Triggers, symptoms, use cases (with flowchart if decision non-obvious)
3. **Core Pattern** — The main technique or pattern (before/after code if applicable)
4. **Quick Reference** — Tables or bullets for scanning
5. **Common Mistakes** — What goes wrong + fixes
6. **Real-World Impact** (optional) — Concrete results/benefits

## Naming Conventions

- **File**: `SKILL.md` (uppercase, hyphenated if needed)
- **Directory**: match the skill name (e.g., `skill-name/SKILL.md`)
- **name field**: lowercase, hyphens only (`skill-name`)
- **Description**: Start with "Use when..." — focus on when to trigger, not what it does

## Tips

- Keep descriptions under 500 characters
- Use flowcharts for decision trees
- Include before/after code comparisons for technique skills
- Cross-reference other skills with: `**REQUIRED SUB-SKILL:** use skill-name`
- Include real-world impact when available

## See Also

- `writing-skills` skill for detailed TDD-based skill creation process
- `skill-judge` skill for evaluating skill quality



