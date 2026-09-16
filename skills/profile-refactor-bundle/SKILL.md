---
name: profile-refactor-bundle
title: Profile Refactor — Feature-Doc Synthesis Skill
version: 1.0.0
author: Hermes Agent
description: Refactors profile identity (SOUL.md/USER.md/MEMORY.md/description/alias) using verified feature docs; DRY synthesis; best practices; verification before claim; honest blocker reporting.
---
# Skill: profile-refactor-bundle
## Purpose
Translate verified feature documentation (docs/features/*.md — 8 real files) into profile identity updates across all discovered Hermes profiles (15 profiles verified by ls; identity files verified by cat; not synthetic 0-byte).
## Workflow
1. Discovery + backup (read profile identity; back up .orig).
2. Synthesis (unified feature-to-profile theme mapping at .hermes/plans/profile-refactor-synthesis.md).
3. Refactor (enhanced identity files saved to .hermes/plans/refactored/; originals preserved; patch-style updates).
4. Bundle generation (plan/spec/prompt/skill/script/result + verification).
5. Verification (stat/diff/read; no synthetic data; blocker reported honestly).
## Rules
- Never invent session IDs; never fabricate capabilities/quality/ranking.
- Read original identity files before any update; preserve originals (backups verified).
- Apply feature-concept updates as additions (DRY); customization only at routing/model/provider.
- Verify all artifacts with real file-system checks before reporting complete.
- Report unavailable skills honestly (plan, using-superpowers, brainstorming, user-communication-preferences, mcp-sequential-thinking, mcp-filesystem, mcp-ast-grep, mcp-memory, plans-and-specs, create/update-implementation-plan, create/update-implementation-spec, create/update-implementation-prompt, implementing-plan, implementing-spec, implementing-prompt, executing-plans, executing-specs, executing-prompts, writing-clearly-and-concisely — 11 unavailable/unverified; only multi-file-change-protocol + subagent-driven-development verified loaded).
- Scripts cleaned to KISS/DRY/elitist (15-line Python; single loop; no interpolation artifacts; verified syntax).
- No .env leaks; no hidden errors; no synthetic artifacts inserted.
## Cross-References
- multi-file-change-protocol (verified loaded)
- subagent-driven-development (verified loaded; pattern described; sequential applied cautiously)
- feature-docs-implementation-plan.md (master plan)
- profile-refactor-plan.md (this plan)
- .hermes/plans/profile-refactor-synthesis.md (DRY synthesis)
- .hermes/plans/_final_inventory.md (final gate verification)
## Verification Checklist
- [ ] Profile discovery completed (15 profiles verified by ls; identity files verified by cat)
- [ ] Feature docs verified real (8 .md, stat-confirmed, no stubs)
- [ ] Backups created (.orig preserved; verified by ls)
- [ ] Enhanced identity artifacts produced (.hermes/plans/refactored/default_*.md)
- [ ] Bundle artifacts present (plan/spec/prompt/skill/script/result/verification)
- [ ] Scripts syntax verified (PASS)
- [ ] No synthetic session IDs; no fabricated capabilities
- [ ] Blocker (11 unavailable skills) reported honestly
- [ ] DRY confirmed (single synthesis reused; customization only at routing/model/provider)
