---
name: seed-review-and-create
title: Seed System Review & Enhancement
description: Review seed system files, create new seeders, fix issues, and implement improvements
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - terminal
  - file
scripts: []
skills: []
formatter: default
plan: ''
tags:
  - audit
  - documentation
  - fix
  - ml
  - prompts
  - specification
  - typescript
trigger: /seed-review-and-create
---

# Seed System Review & EnhancementAs **Reviewer persona**, research the codebase for additional context and dependencies, research the seeding system and identify how images are being managed and linked to their respective entities. Update seeding system images management to ensure proper linking, set a default callback image for all failed entities to the default image or the placeholder image or the image url, update documentation, and seeders accordingly.As **Reviewer persona**, review all `src/scripts/seed/**/*.ts` files. Understand the architecture, identify issues, and implement improvements.## Context Files (Read First)1. `src/database/schema.ts` — All table definitions, relations, and enums2. `src/scripts/seed/types.ts` — Core types: `SeedConfig`, `SeedOptions`, `LookupCache`, `EntityResult`, `SeedReport`3. `src/scripts/seed/seeders/base-seed.ts` — Abstract `BaseSeeder<T>` template method pattern4. `src/scripts/seed/seed-orchestrator.ts` — Entity ordering, cache management, seeder dispatch5. `src/scripts/seed/index.ts` — Central exports6. `src/schemas/seed/` — Zod validation schemas for each entity## ArchitectureThe seed system uses the **Template Method Pattern**:```BaseSeeder<T>.seed() → loadData() → validateData() → processBatches() → insertBatch()```- **Abstract methods** each seeder must implement: `getDataSources()`, `getUniqueField()`, `transformData()`, `insertBatch()`- **LookupCache** is shared across all seeders for deduplication (entity name → ID maps)- **SeedOrchestrator** manages dependency order and coordinates seeding- **Entity order**: users → types → authors → artists → genres → comics → comic-images → chapters → chapter-images## Tasks> ### 1. Review Existing Seeders>> Review all files in `src/scripts/seed/seeders/` for:> **Full content:** `templates/seed-review-and-create/tasks.md`## Quality GateAfter all changes, run:```bashpnpm type-check    # Must be 0 TypeScript errorspnpm lint:strict   # Must be 0 Lint errors```## Reference- **Password hashing**: `bcryptjs` with 10 salt rounds (project standard)- **DB driver**: Drizzle ORM with `db.query.*` and `db.insert()` patterns- **Schema location**: `src/database/schema.ts` (27 tables, 4 enums)- **Zod schemas**: `src/schemas/seed/*.seed.ts`## Template ReferencesTemplates in `templates/seed-review-and-create/`:- `tasks.md`