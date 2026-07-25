---
author: Hermes Agent
description: Discover, install, update, configure, and manage Hermes skills across profiles. This skill provides workflows for maintaining the skill library quality and organization. Also covers the skill-curator security gate (dangerous-findings / unloaded-SKILL.md) and how to re-enable skills blocked by it.
license: MIT
metadata:
  hermes:
    related_skills:
    - hermes-skills
    - skill-creator
    - skill-judge
    - hermes-setup
    tags:
    - skills
    - management
    - configuration
    - hermes
name: skill-management
tags:
- skills
- management
- configuration
- hermes
- scripts
title: Skill Management
version: 1.2.0
---

# Skill Management

## Overview

Discover, install, update, configure, and manage Hermes skills across profiles. This skill maintains the skill library's quality and organization.

**Renamed from `skills`** because a skill named `skills` auto-registers the slash command `/skills`, which collides with a core Hermes command (the agent logs `Skill 'skills' generates slash command '/skills' which collides with a core Hermes command; skipping auto-registration`). Use `/skill skill-management` to invoke it.

## When to Use

- Installing new skills from the community or custom sources
- Updating existing skills to latest versions
- Auditing skill library quality with skill-judge
- Managing skills across multiple Hermes profiles
- Creating or modifying skills (use skill-creator for authoring)

## Commands

```bash
# List installed skills
hermes skills list

# Install / update a skill
hermes skills install <name|url>

# View a skill
hermes skill <name>

# Open the skill library
hermes skills
```

## Curator Security Gate (important)

When the agent patches a skill, the curator guard may block with:

- `Agent-created skill blocked (dangerous findings): Requires confirmation` — the skill scan flagged risky patterns. Resolve the findings or explicitly approve.
- `Refusing <op> for skill 'X': the current SKILL.md content has not been loaded in this review turn. Call skill_view(name) for SKILL.md, then retry.` — load the skill with `skill_view(name)` before patching in the same turn.

## Skill Hygiene (per repo policy)

- No stub/placeholder skills. Every skill must earn its place with substantive content.
- Before creating a skill, search existing skills + the hub for equivalents.
- Delete dead/unreferenced skills on sight.
- Class-level umbrella skills over one-off task artifacts.
