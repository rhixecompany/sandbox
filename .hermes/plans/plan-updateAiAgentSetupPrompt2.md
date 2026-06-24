---
title: "Plan: Update AI Agent Setup Prompt for ComicWise"
category: "IMPL_PLAN"
source: "prompts/plan-updateAiAgentSetupPrompt2.prompt.md"
---

# Plan: Update AI Agent Setup Prompt for ComicWise

**TL;DR:** Update `.github/prompts/setup.prompt.md` from 824 lines/20 sections to ~1200-1400 lines/24 sections. Corrects 6 factual inaccuracies, adds 15 undocumented schema tables/fields, merges ~35 conventions from 6 instruction files, adds 8 missing commands, documents Next.js 16-specific patterns, adds a technical debt register, and prominently flags the Drizzle relations gap. Model stays as "Claude Haiku 4.5 (copilot)".

---

## Phase 1: Fix Inaccuracies (6 items)

> ### Step 1 — Fix `comic.rating` type in §4
> Clarify dual types: `comic.rating` is `decimal(10,1)` (aggregate display), `rati

> **Full content:** `templates/plan-updateAiAgentSetupPrompt2/phase_1_fix_inaccuracies_6_ite.md`

## Phase 2: Add Missing Schema Knowledge (9 items)

> ### Step 7 — Add RBAC tables to §4
> - `role` (id, name, description, isSystem)

> **Full content:** `templates/plan-updateAiAgentSetupPrompt2/phase_2_add_missing_schema_kno.md`

## Phase 3: Merge Instruction File Conventions (6 items)

> ### Step 16 — Add TypeScript conventions to §20
> From `.github/instructions/typescript.instructions.md`:

> **Full content:** `templates/plan-updateAiAgentSetupPrompt2/phase_3_merge_instruction_file.md`

## Phase 4: Add Missing Commands & Workflows (4 items)

> ### Step 22 — Add missing commands to §2
> # ── Database (additional) ──

> **Full content:** `templates/plan-updateAiAgentSetupPrompt2/phase_4_add_missing_commands__.md`

## Phase 5: Add Missing Patterns (8 items)

> ### Step 26 — Add Next.js 16 `searchParams` pattern to §14
> In Next.js 16, `searchParams` is a **Promise** that must be `await`ed:

> **Full content:** `templates/plan-updateAiAgentSetupPrompt2/phase_5_add_missing_patterns_8.md`

## Phase 6: New Sections (4 items)

> ### Step 34 — Add §21: Known Technical Debt
> ### Step 35 — Add §22: Feature Implementation Workflow

> **Full content:** `templates/plan-updateAiAgentSetupPrompt2/phase_6_new_sections_4_items.md`

## Verification Checklist

- [ ] Cross-check every table name against actual `src/database/schema.ts` (27 tables verified)
- [ ] Cross-check every command against `package.json` scripts
- [ ] Validate env var list against active + commented fields in `src/lib/env.ts`
- [ ] Verify all DAL query patterns match actual code (`db.query.*.findMany/findFirst` with `.with()` primary; `db.select()` for simple lookups)
- [ ] Confirm all instruction file conventions are accurately merged
- [ ] Run `pnpm type-check` after implementation
- [ ] Run `pnpm lint:fix` after implementation

---

## Decisions Log

| Decision | Rationale |
| --- | --- |
| **Model:** Keep "Claude Haiku 4.5 (copilot)" | User preference |
| **`comic.rating` dual-type:** Document both columns | `comic.rating` = decimal(10,1), `rating.rating` = integer — prevents confusion |
| **Raw `process.env` in auth:** Document as known exception | Auth files load before app init; pragmatic choice |
| **No Drizzle `relations()`:** Flag prominently in §6 + §21 | Explain FK inference works for simple cases, list what breaks (parentId, custom names) |
| **RBAC tables:** Document as present in schema | Available for use — don't write aspirational middleware |
| **React Compiler conflict:** Setup prompt is authoritative | Flag performance instructions as needing update |
| **All code samples:** Real, not aspirational | Only include patterns verified in actual source files |
| **Estimated final size:** ~1200-1400 lines (up from 824) | Significant expansion justified by discovered gaps |

---

## Sources Analyzed

| Source | Files Read | Key Findings |
| --- | --- | --- |
| `.github/prompts/setup.prompt.md` | 1 (824 lines) | Existing 20-section prompt — baseline |
| `.github/instructions/*.md` | 7 files | 35+ conventions missing from setup prompt |
| `docs/*.md` | 9 files | Gaps in schema, auth, seeding, feature patterns |
| `src/database/schema.ts` | 1 (604 lines) | 27 tables, 4 enums, no `relations()`, soft delete, JSONB settings |
| `src/dal/*.ts` | 18 files | `db.query.*` with `.with()` primary pattern; `db.select()` for simple lookups |
| `src/auth*.ts` + `proxy.ts` | 5 files | Raw `process.env` violations, proxy only guards `/dashboard` |
| `src/lib/env.ts` | 1 (165 lines) | Only 6 active validations, 60+ commented |
| `package.json` | 1 | Zod v4, Zustand v5, Vitest v4, Commander in devDeps |
| `next.config.ts` | 1 (174 lines) | staleTimes, staticGeneration tuning, webpack polyfill fallbacks |
| `appConfig.ts` | 1 (101 lines) | Mostly empty stubs |
| `.references/comicr/*` | 5 files | Architecture blueprint, RBAC, requirements, system patterns |
| `.references/comicwise/*` | 2 files | Architecture, onboarding patterns |
| `eslint.config.mts` | 1 (39 lines) | Only 3 active rules, plugins registered without rules |


## Template References

Detailed templates in `templates/plan-updateAiAgentSetupPrompt2/`:
- `phase_1_fix_inaccuracies_6_ite.md`
- `phase_2_add_missing_schema_kno.md`
- `phase_3_merge_instruction_file.md`
- `phase_4_add_missing_commands__.md`
- `phase_5_add_missing_patterns_8.md`
- `phase_6_new_sections_4_items.md`
