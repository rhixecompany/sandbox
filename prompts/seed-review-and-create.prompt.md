---
toolsets:
  - codebase
  - editFiles
  - terminalLastCommand
  - runInTerminal
license: MIT
author: Hermes Agent
version: 1.0.0
title: Seed System Review & Enhancement
name: seed-review-and-create
description: "Review seed system files, create new seeders, fix issues, and implement improvements"
tags:
  - audit
  - documentation
  - fix
  - ml
  - prompts
  - specification
  - typescript
  - documentation
  - linux
  - planning
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - seed-review-and-create.prompt

trigger: seed-review-and-create

---
metadata:
  hermes:
    related_skills: []
    tags:
    - seed-review-and-create.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - seed-review-and-create.prompt

# Seed System Review & Enhancement

As **Reviewer persona**, research the codebase for additional context and dependencies, research the seeding system and identify how images are being managed and linked to their respective entities. Update seeding system images management to ensure proper linking, set a default callback image for all failed entities to the default image or the placeholder image or the image url, update documentation, and seeders accordingly.

As **Reviewer persona**, review all `src/scripts/seed/**/*.ts` files. Understand the architecture, identify issues, and implement improvements.

## Context Files (Read First)

1. `src/database/schema.ts` — All table definitions, relations, and enums
2. `src/scripts/seed/types.ts` — Core types: `SeedConfig`, `SeedOptions`, `LookupCache`, `EntityResult`, `SeedReport`
3. `src/scripts/seed/seeders/base-seed.ts` — Abstract `BaseSeeder<T>` template method pattern
4. `src/scripts/seed/seed-orchestrator.ts` — Entity ordering, cache management, seeder dispatch
5. `src/scripts/seed/index.ts` — Central exports
6. `src/schemas/seed/` — Zod validation schemas for each entity

## Architecture

The seed system uses the **Template Method Pattern**:

```
BaseSeeder<T>.seed() → loadData() → validateData() → processBatches() → insertBatch()
```

- **Abstract methods** each seeder must implement: `getDataSources()`, `getUniqueField()`, `transformData()`, `insertBatch()`
- **LookupCache** is shared across all seeders for deduplication (entity name → ID maps)
- **SeedOrchestrator** manages dependency order and coordinates seeding
- **Entity order**: users → types → authors → artists → genres → comics → comic-images → chapters → chapter-images

## Tasks

> ### 1. Review Existing Seeders
> Review all files in `src/scripts/seed/seeders/` for:

> **Full content:** `templates/seed-review-and-create/tasks.md`

## Quality Gate

After all changes, run:

```bash
pnpm type-check    # Must be 0 TypeScript errors
pnpm lint:strict   # Must be 0 Lint errors
```

## Reference

- **Password hashing**: `bcryptjs` with 10 salt rounds (project standard)
- **DB driver**: Drizzle ORM with `db.query.*` and `db.insert()` patterns
- **Schema location**: `src/database/schema.ts` (27 tables, 4 enums)
- **Zod schemas**: `src/schemas/seed/*.seed.ts`


## Template References

Templates in `templates/seed-review-and-create/`:
- `tasks.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
