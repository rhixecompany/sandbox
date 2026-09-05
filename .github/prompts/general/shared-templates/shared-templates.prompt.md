---
name: templates-index
title: Prompt Templates Index
description: Index of all prompt templates under prompts/templates/ are the canonical source for frontmatter schema, skill references, and verification gates.
version: 1.1.0
author: Hermes Agent
license: MIT
tags: [templates, index, prompts, shared, DRY]
trigger: /shared-templates
category: general
toolsets: 
formatter: markdown
---

# Prompt Templates Index

> Updated: 2026-08-29
> Location: `prompts/templates/
├── _shared/                    # Canonical shared templates (NEW 2026-08-29)
│   ├── frontmatter.md          # YAML frontmatter schema + validation rules
│   ├── skill-refs.md           # Hermes skill reference tables
│   └── verification-checklist.md  # Standard verification gates by task type
├── _index.md                   # This file
├── platform_evaluation.md      # Per-prompt template
├── RESEARCH_REPORT.template.md # Per-prompt template
└── weekly_routine.md           # Per-prompt template
```

## Shared Templates (DRY source of truth)

| Template | Purpose | When to reference |
|---|---|---|
| `_shared/frontmatter.md` | Canonical YAML schema, controlled tag vocabulary, validation rules | Every `.prompt.md` — must conform |
| `_shared/skill-refs.md` | Tier 1/2/3 skill tables, multi-file-change protocol | Any prompt that invokes skills |
| `_shared/verification-checklist.md` | 8 gate sets (code, docs, plan, diagnostic, multi-file, MCP, git) | Any prompt with acceptance criteria |

## Usage pattern in prompts

```markdown
---
<frontmatter per _shared/frontmatter.md>
---

# <Title>

> Frontmatter: see [shared schema](../_shared/frontmatter.md)
> Skills: see [shared references](../_shared/skill-refs.md)
> Verification: see [shared checklist](../_shared/verification-checklist.md)

## Verification

<copy relevant section from _shared/verification-checklist.md>
```

## Per-Prompt Templates

Each existing per-prompt template folder contains:
1. `README.md` — Section inventory, size, frontmatter type, usage notes
2. Extracted long sections (when applicable, sections >40 lines)
3. Additional reference templates (when applicable)

## Migration status (2026-08-29)

- [x] `_shared/frontmatter.md` created
- [x] `_shared/skill-refs.md` created
- [x] `_shared/verification-checklist.md` created
- [x] Index updated to v1.1.0
- [ ] Migrate 231 `.prompt.md` files to reference `_shared/` (next pass)
- [ ] Fix 25 broken-fence files
- [ ] Add frontmatter to 1 missing-file (`repo.prompt.md`)

## DRY Principle

## Goal
Index of all prompt templates under prompts/templates/ are the canonical source for frontmatter schema, skill references, and verification gates.

## Context

## Workflow

<content>

<content>

<content>

**Before adding a section to a new prompt, check `_shared/` first.** If the section is cross-cutting (frontmatter, skills, verification, "When to Use", "Pitfalls"), add it to the canonical shared template and reference it from your prompt. Duplication is technical debt.
