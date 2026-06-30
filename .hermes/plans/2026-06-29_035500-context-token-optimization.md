---
status: completed
status: completed
status: completed
---
# Context File Token Optimization Plan

**Goal:** Eliminate cross-file redundancy to reduce per-turn token consumption.
**Strategy:** DRY consolidation — each fact lives in one file, others reference it.
**Net saving:** ~32KB (8,000 tokens per turn)

---

## Phase 1 — Trim SOUL.md (5.5KB → ~2.0KB)

**Changes:**
- Remove `## File Operations` — covered by MASTER_RULES.md L2 rules 7-8
- Remove `## Code Quality` — covered by MASTER_RULES.md L3 rules 12-14
- Remove `## Response Style` — covered by MASTER_RULES.md L4 rules 16-21
- Remove `## Security` — covered by MASTER_RULES.md L5 rules 22-26
- Remove `## Workspace` — paths are in USER.md + .hermes.md
- Remove `## Environment Corrections` — lives in USER.md
- Keep: Identity & Tone, 7 Core Non-Negotiables, See references

## Phase 2 — Trim MASTER_RULES.md (9.6KB → ~5.0KB)

**Changes:**
- Convert from markdown table format → compact bullet list (saves ~40% whitespace)
- Remove redundant `|` `---` `|` table boilerplate
- Each rule becomes one line: `1. Session Start — search/read/explain SESSION_REPORT.md`
- Consolidate Rules 6 & 7 (both are DRY rules) into one entry
- Total: 36 rules → same 36 rules, but ~5KB instead of ~9.6KB

## Phase 3 — Trim USER.md (1.3KB → ~0.6KB)

**Changes:**
- Remove `## Active Model & Providers` — already in .hermes.md provider chain
- Remove `## Path Safety` — says "See SOUL.md" already; redundant
- Condense execution preferences to one line

## Phase 4 — Trim .hermes.md (12.3KB → ~6.0KB)

**Changes:**
- Remove duplicate `Profile Inventory` table (lines 91-117 includes 16 unconfigured profiles — wasted space)
- Remove duplicate `MCP Server Tools Summary` (lines 76-93 — tool names already in table above)
- Compact MCP `Server table` — remove Transport/Command columns (unnecessary context), short descriptions
- Condense plugins table to compact list format
- Remove `Session Startup Rules` section (lines 176-187) — already in SOUL.md + MASTER_RULES.md
- Remove `Environment Corrections` appendix (lines 189-193) — already in USER.md

## Phase 5 — Trim AGENTS.md (9.5KB → ~4.0KB)

**Changes:**
- Remove `## Hermes Config` section (lines 62-88) — fully duplicated in .hermes.md
- Remove `## Profile Inventory` section (lines 91-117) — duplicate of .hermes.md
- Keep: Structure, Conventions, Toolkit Validation, Quick Rule Summary (8 rules)

## Phase 6 — Trim PROJECT_RULES.md (7.1KB → ~3.0KB)

**Changes:**
- Remove `Level 3: Profile Routing` — fully duplicated in .hermes.md
- Compact `Level 2: Environment Facts` — convert from table to flat list
- Keep: Level 1 session lifecycle rules, compact env facts, see references

## Verification

- Read each file after update
- Confirm JSON/markdown validity
- Confirm no broken cross-references
- Confirm no unique content was lost

## Total Impact

| File | Before | After | Saving |
|------|--------|-------|--------|
| SOUL.md | 5.5KB | 2.0KB | 3.5KB |
| MASTER_RULES.md | 9.6KB | 5.0KB | 4.6KB |
| USER.md | 1.3KB | 0.6KB | 0.7KB |
| MEMORY.md | 2.1KB | 1.5KB | 0.6KB |
| .hermes.md | 12.3KB | 6.0KB | 6.3KB |
| AGENTS.md | 9.5KB | 4.0KB | 5.5KB |
| PROJECT_RULES.md | 7.1KB | 3.0KB | 4.1KB |
| **Total** | **47.4KB** | **22.1KB** | **~25KB (6,500 tok)** |
