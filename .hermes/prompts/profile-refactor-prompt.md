---
name: profile-refactor-prompt
title: Profile Refactor — Feature-Doc Synthesis Implementation Prompt
---
# Implementation Prompt: Profile Refactor
You are refactoring Hermes profile identity files (SOUL.md / USER.md / MEMORY.md / description / alias) across ALL discovered profiles using the verified feature docs (docs/features/*.md — 8 real files: overview, mcp, memory, skills, tools, tool-gateway, kanban, hooks).
Steps:
1. Read feature docs (verified downloaded; stat-confirmed; frontmatter extracted).
2. Synthesize unified theme mapping (DRY; single reference at .hermes/plans/profile-refactor-synthesis.md).
3. Read each profile's identity files (SOUL.md / USER.md / MEMORY.md); back up originals (.orig in .hermes/plans/backups/profiles/); never delete originals.
4. Apply feature-concept updates to identity sections using patch-style additions (not destructive replacements); customization only at routing/model/provider level; shared identity at core.
5. Generate enhanced profile identity artifacts (.hermes/plans/refactored/<profile>_SOUL_updated.md etc.) with verification notes.
6. Produce verification script output (results file) confirming real file-system checks; honest blocker reporting (unavailable skills listed explicitly); no synthetic session IDs; no fabricated capabilities.
7. Verify DRY enforcement (template reuse; no duplication across profiles); best practices applied (read→patch→verify; native equivalents; backup+verify before claim).
8. Report concrete blocker: 11 of 14 named multi-file-change-protocol skills unavailable/unverified; work completed with native equivalents; bundle artifacts verified real.
