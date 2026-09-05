---
name: profile-templates
title: Profile Templates — Hermes Profile scaffolding
description: Template files for Hermes profile scaffolding: SOUL.md, USER.md, MEMORY.md. Used when creating or updating Hermes profiles.
trigger: /profile-templates
category: general
version: 1.0.0
author: Hermes Agent
tags: [templates, profiles, hermes]
metadata: 
hermes: 
toolsets: 
skills: []
dependencies: []
formatter: markdown
license: MIT
---

# Profile Templates

> Location: `templates/`

Template files for scaffolding Hermes profiles. Each profile (default, alexa, code-architect, etc.) needs SOUL.md, USER.md, and MEMORY.md files. These templates provide the canonical starting point.

## Goal

Provide canonical template files for Hermes profile scaffolding so that new profiles can be created consistently and existing profiles can be updated against a known-good baseline.

## Context

Hermes profiles live under `~/AppData/Local/hermes/profiles/<profile-name>/`. Each profile needs:
- `SOUL.md` — agent identity, persona, boundaries
- `USER.md` — user profile, preferences, environment
- `MEMORY.md` — persistent notes, environment facts, lessons

These templates are referenced by profile-sync and profile-maintenance workflows.

## Workflow

### Creating a new profile

1. Copy templates from `templates/` to `~/AppData/Local/hermes/profiles/<name>/`
2. Customize SOUL.md with profile-specific persona
3. Customize USER.md with user-specific preferences
4. Initialize MEMORY.md as empty

### Updating profiles

1. Compare existing profile files against templates in `templates/`
2. Merge template updates into existing profile files
3. Preserve profile-specific customizations

## Structure

```
templates/
├── README.md
├── profile-soul.md.template
├── profile-user.md.template
└── profile-memory.md.template
```

## References

## Verification

<content>

- `shared-templates.prompt.md` — shared cross-prompt templates
- `hermes-profiles` skill — profile identity & state management
- `profile-directive-sync` skill — propagate root SOUL/USER/MEMORY changes to profiles
