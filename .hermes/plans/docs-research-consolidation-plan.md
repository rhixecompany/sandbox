---
name: docs-research-consolidation-plan
title: "Docs & Research Consolidation Plan"
description: "Multi-phase plan to list, triage, read, consolidate, dedupe, and delete duplicate markdown files across docs/ and research/ — then extract content, create needed infrastructure, and implement via executing-plans."
version: 2.0.0
author: Alexa
tags: [docs, research, consolidation, dedup, plan, infrastructure]
dependencies: [plans-and-specs, executing-plans, create-implementation-plan, update-implementation-plan]
---

# Docs & Research Consolidation Plan

> **Scope:** `./docs/*/*.md` (593→133 files) + `./research/*/*.md` (25 files)
> **Phase 1-4 complete:** 459 auto-generated files deleted (1.1MB reclaimed)
> **Extracted content:** See `.hermes/plans/extracted-content/` — 3 full extracts + JSON summary

---

## ✅ Phases 0-4: Complete (Inventory, Triage, Read, Dedup, Delete)

- Phase 0: Full inventory captured — 616 files cataloged ✓
- Phase 1: Triage by category — P0/P1/P2/P3/P4 priorities ✓
- Phase 2: All content read — subagents + direct reads ✓
- Phase 3: Dedup report — 459 files identified as auto-generated duplicates ✓
- Phase 4: 459 auto-generated files deleted (approved via approval gate) ✓
- Phase 4.5: Final extracted content compiled to `.hermes/plans/` ✓

---

## Phase 5: Infrastructure from Extracted Content

Based on the extracted content analysis, the following infrastructure is needed:

### 5.1 Skills to Create

| # | Skill | Source | Rationale |
|---|-------|--------|-----------|
| 5.1.1 | `mcp-server-catalog` | mcp-research/ (34 files) | Reference skill listing all 34 researched MCP servers with notes, URLs, and setup status |
| 5.1.2 | `project-architecture-index` | Project_Architecture/ (51→17 files) | Reference skill linking to all 17 project architecture docs |
| 5.1.3 | `api-tutorial-catalog` | research/*/ (25 files) | Reference skill for 9 API tutorial categories |
| 5.1.4 | `hermes-docs-reference` | hermes/ (13 files) | Consolidated reference for official Hermes docs |

### 5.2 Hooks to Create/Configure

| # | Hook | Purpose |
|---|------|---------|
| 5.2.1 | `docs-cleanup-verifier` | Post-session hook to verify docs/ and research/ cleanliness (no orphaned auto-generated artifacts) |

### 5.3 MCP Servers to Configure

Based on mcp-research content, verify these MCP servers are configured:
- **Already configured:** filesystem, github, memory, playwright, sequential-thinking, fetch, ast-grep, code-sandbox, mcp-docker, linear, mindstudio, copilot-mcp, codex
- **New candidates from research:** context7 (already integrated), sentry (for monitoring), scrapegraph (for web scraping), vitest (for testing)

### 5.4 Scripts to Create

| # | Script | Purpose |
|---|--------|---------|
| 5.4.1 | `archive-old-docs.py` | Archive docs/ files older than 60 days to a compressed backup |
| 5.4.2 | `docs-inventory-report.py` | Generate periodic inventory of docs/ and research/ with file counts per subdir |

### 5.5 Tools

Existing Hermes toolsets are sufficient. No new toolsets needed.

---

## Phase 6: Create Infrastructure

### 6.1 Create Skills

**6.1.1 — mcp-server-catalog skill**
- `skill_manage(action='create', name='mcp-server-catalog', content=...)` 
- Contains: table of all 34 MCP servers from research, installation commands, config examples
- Category: `mcp` or `reference`

**6.1.2 — api-tutorial-catalog skill**
- `skill_manage(action='create', name='api-tutorial-catalog', content=...)`
- Contains: summary of 9 API tutorial topics with key concepts
- Category: `reference`

**6.1.3 — project-architecture-index skill**
- `skill_manage(action='create', name='project-architecture-index', content=...)`
- Contains: listing of all 17 projects with architecture summary
- Category: `reference`

### 6.2 Create Hook

**6.2.1 — docs-cleanup-verifier hook**
- Shell script at `~/AppData/Local/hermes/hooks/docs-cleanup-verify.sh`
- Checks that skills-reports/ and skills-audit/ don't have auto-generated artifacts
- Verifies docs/ size under threshold

### 6.3 Configure MCP Servers

**6.3.1 — Audit existing vs researched MCP servers**
- Cross-reference 34 researched servers with 13 configured ones
- Add missing ones where useful (sentry, scrapegraph, etc.)

### 6.4 Create Scripts

**6.4.1 — docs-inventory-report.py**
- Python script at `~/AppData/Local/hermes/scripts/`
- Generates markdown inventory of docs/ and research/ by subdirectory

---

## Phase 7: Execute via executing-plans

**7.1 — Generate execution prompt**
- Create `.hermes/plans/docs-research-execution-prompt.md`
- Self-contained prompt that uses `/executing-plans` skill
- References this plan and extracted content

**7.2 — Load executing-plans skill**
- `skill_view(name='executing-plans')`
- Follow its batch processing pattern

**7.3 — Execute phases**
- Create skills (6.1) → Verify
- Create hooks (6.2) → Verify
- Configure MCP servers (6.3) → Verify
- Create scripts (6.4) → Verify

---

## File Manifest

| Artifact | Purpose | Status |
|----------|---------|--------|
| `.hermes/plans/docs-research-consolidation-plan.md` | This master plan | ✅ Updated v2 |
| `.hermes/plans/inventory/` | Phase 0 — baseline file metadata | ✅ Done |
| `.hermes/plans/triage-report.md` | Phase 1 — categorized file groups | ✅ Done |
| `.hermes/plans/extracted-content/` | Phase 2 — extracted file content | ✅ 3 files |
| `.hermes/plans/extracted-content-summary.md` | Phase 2 — summary | ✅ Done |
| `.hermes/plans/dedup-report.md` | Phase 3 — duplicate analysis | ✅ Done |
| `.hermes/plans/deletion-execution-log.md` | Phase 4 — deletion results | ✅ Done |
| `.hermes/approvals/2026-06-22-docs-dedup.md` | Phase 4 — approval gate | ✅ Approved |
| `.hermes/plans/final-extracted-content.json` | Phase 4.5 — final content JSON | ✅ Done |
| `.hermes/plans/docs-research-execution-prompt.md` | Phase 7 — execution prompt | ⏳ Next |

## Risk Notes

| Risk | Mitigation |
|------|------------|
| Skill creation may fail if skill_manage input is too large | Create skills with compact content, use references for bulk |
| MCP server config changes may break existing workflows | Add new servers, don't remove existing ones |
| Scripts may conflict with existing ones at same path | Check for name collisions before creating |
