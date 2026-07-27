---
name: setup-enhanced
title: "ComicWise \u2014 AI Agent Setup & Implementation Guide"
description: "Enhanced ComicWise AI agent setup \u2014 workflow, implementation strategy, and DRY\
  \ practices"
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills:
  - subagent-driven-development
formatter: default
plan: ''
dependencies:
  - skill:subagent-driven-development
tags:
  - agents
  - backend
  - configuration
  - data
  - database
  - frontend
  - linting
  - ml
  - prompts
  - setup
  - sql
  - typescript
  - workflow
trigger: /setup-enhanced
---

## 1. 🚀 Quick Start```bashpnpm install                              # Install dependenciescp .env.local.example .env.local          # Configure DATABASE_URL, AUTH_SECRETpnpm db:push                              # Apply schema to databasepnpm type-check                           # Verify zero TypeScript errorspnpm dev                                  # Start dev server (port 3000)```---## 2. ✅ Quality Gate (Before Every PR)```bashpnpm type-check          # 0 TypeScript errors requiredpnpm lint:fix            # ESLint + Prettier auto-fixpnpm test                # Vitest unit tests (jsdom)pnpm build               # Production build validation```All four commands must pass before merging any code.---## 3. 📚 Reference Resolution Hierarchy> When implementing features, consult these sources in priority order:>> ### Tier 1 — Latest Standards (Primary)> **Full content:** `templates/setup-enhanced/3__reference_resolution_hierar.md`## 4. 🔧 DRY Implementation Practices> Every piece of logic should exist in exactly one place. When implementing featur>> ### Strategy 1: DAL Classes — Parameterized Query Methods> **Full content:** `templates/setup-enhanced/4__dry_implementation_practice.md`## 5. 📋 Implementation Workflow (10 Steps)> Follow these steps for every new feature. Each step references the relevant docu>> ### Step 1: Search & Document> **Full content:** `templates/setup-enhanced/5__implementation_workflow_10_.md`## 6. 🏗️ Feature Implementation Phases> ### Phase 1: Foundation>> Infrastructure setup — database schema, base DAL, core validation, auth flow.> **Full content:** `templates/setup-enhanced/6__feature_implementation_phas.md`## 7. 🔗 Content Integration Rules (DRY Enforcement)> ### When Adding Documentation>> - ✅ Link to relevant sections in existing docs rather than duplicating content> **Full content:** `templates/setup-enhanced/7__content_integration_rules_d.md`## 8. 🧭 How to Use This Guide### For New Features1. Identify which **Phase** (Section 6) your feature belongs to2. Follow the **Implementation Workflow** (Section 5) step by step3. Apply **DRY Practices** (Section 4) throughout4. Run the **Quality Gate** (Section 2) before submitting### For Bug Fixes1. Check the **Reference Resolution Hierarchy** (Section 3) to find relevant code2. Apply the correct pattern from the appropriate reference file3. Run `pnpm type-check && pnpm lint:fix && pnpm test` to validate### For Questions1. Check the **Reference Resolution Hierarchy** (Section 3) for the right source file2. Consult `docs/dev.content.md` for expanded technical details3. Look at existing implementations in `src/` for concrete examples4. Check git history for similar patterns---## 9. 🎭 AI Personas for Copilot CLI> Use these personas when running tasks in Copilot CLI to get specialized behavior>> ### Architect Persona> **Full content:** `templates/setup-enhanced/9__ai_personas_for_copilot_cli.md`## 10. 🔄 Anti-Rate-Limiting Strategy> When using this prompt with Copilot CLI, follow these practices to avoid token e>> ### Chunked Execution> **Full content:** `templates/setup-enhanced/10__anti-rate-limiting_strateg.md`## 11. 📋 Phase Execution Checklists> ### Phase 1: Foundation>> - [ ] `pnpm install` — dependencies installed> **Full content:** `templates/setup-enhanced/11__phase_execution_checklists.md`## 12. 📖 Full Reference Files| File | Purpose || --- | --- || `docs/dev.content.md` | Complete developer reference (25 sections) — patterns, code examples, architecture || `docs/database-context-map.md` | Entity relationship details, constraints, cascade behavior || `.github/copilot-instructions.md` | Quick-reference coding rules and conventions || `.github/instructions/` | File-pattern coding standards (TypeScript, Next.js, security, testing, performance) || `src/database/schema.ts` | All 30+ Drizzle tables, enums, relations || `src/dal/base-dal.ts` | Abstract `BaseDal<T>` base class || `src/actions/types.ts` | `ActionResult<T>` type definition || `src/lib/env.ts` | Zod-validated environment variables |---**Last Updated:** March 2026## Template ReferencesDetailed section templates in `templates/setup-enhanced/`:- `10__anti-rate-limiting_strateg.md`- `11__phase_execution_checklists.md`- `3__reference_resolution_hierar.md`- `4__dry_implementation_practice.md`- `5__implementation_workflow_10_.md`- `6__feature_implementation_phas.md`- `7__content_integration_rules_d.md`- `9__ai_personas_for_copilot_cli.md`