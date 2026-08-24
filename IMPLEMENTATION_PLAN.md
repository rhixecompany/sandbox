# Comprehensive Implementation Plan: Configuration File Consolidation & Optimization

## Executive Summary

This plan outlines the systematic consolidation and optimization of configuration files across the SandBox monorepo. The workspace contains 13 `mcp.json` files (1 root + 12 project-level), 1 `opencode.json`, 1 `.mcp.json`, 100+ `.instructions.md` files, and no `omo.json` files. The goal is to eliminate duplication, establish canonical configurations, and create maintainable patterns.

---

## Current State Analysis

### Files Discovered

| File Type | Count | Locations | Status |
|-----------|-------|-----------|--------|
| `opencode.json` | 1 | Root workspace | Canonical (needs validation) |
| `.mcp.json` | 1 | Root workspace | Legacy format (MCP servers) |
| `mcp.json` | 12 | Root `.vscode/` + 11 project `.vscode/` | **High duplication** |
| `omo.json` | 0 | Not found | N/A |
| `.instructions.md` | 100+ | `docs/instructions/` | Canonical library |

### Duplication Patterns Identified

**MCP Server Configurations (CRITICAL - 95% duplicate):**
- 10 of 12 project `mcp.json` files are **identical** (26 servers each)
- Projects with identical configs: `mcp-server-typescript`, `youtube-downloader`, `university-libary-jsm`, `selenium_webdriver`, `comicwise`, `xamehi`, `xamehi.tv`, `rhixe_scans`, `rhixecompany-comics`, `profile`
- 2 unique configs: `Banking` (2 servers), root `.vscode/mcp.json` (27 servers)

**Root-level Configuration:**
- `opencode.json`: 21 MCP servers + 1 plugin
- `.mcp.json`: 26 MCP servers (VS Code format)
- `.vscode/mcp.json`: 27 MCP servers (identical to project templates)

---

## Phase 1: Discovery & Triage (Week 1)

### Milestone 1.1: File Inventory & Categorization (Days 1-2)
**Owner:** Configuration Engineer  
**Resources:** 1 FTE  
**Deliverable:** Complete inventory spreadsheet

| Task | Description | Effort | Dependencies |
|------|-------------|--------|--------------|
| 1.1.1 | Catalog all config files with metadata (path, size, modified, project) | 2h | None |
| 1.1.2 | Classify each file by type: `canonical`, `project-override`, `duplicate`, `legacy` | 3h | 1.1.1 |
| 1.1.3 | Generate SHA256 hashes for all `mcp.json` files to identify exact duplicates | 1h | 1.1.1 |
| 1.1.4 | Document purpose of each `.instructions.md` file | 4h | None |

### Milestone 1.2: Diff Analysis (Days 2-3)
**Owner:** Configuration Engineer  
**Resources:** 1 FTE  
**Deliverable:** Diff report with line-by-line comparisons

| Task | Description | Effort | Dependencies |
|------|-------------|--------|--------------|
| 1.2.1 | Compare all 12 project `mcp.json` files against root `.vscode/mcp.json` | 3h | 1.1.3 |
| 1.2.2 | Compare `opencode.json` MCP section against `.mcp.json` and `.vscode/mcp.json` | 2h | 1.1.1 |
| 1.2.3 | Identify project-specific server needs vs. inherited | 3h | 1.2.1 |
| 1.2.4 | Map `.instructions.md` files to their `applyTo` patterns | 4h | 1.1.4 |

---

## Phase 2: Consolidation Strategy Design (Week 1-2)

### Milestone 2.1: Architecture Decision Records (Days 3-5)
**Owner:** Lead Architect + Configuration Engineer  
**Resources:** 1.5 FTE  
**Deliverable:** ADR documents for each consolidation decision

| Decision | Options | Recommended | Rationale |
|----------|---------|-------------|-----------|
| **MCP Server Config Location** | A) Root only + project inheritance<br>B) Root template + project overrides<br>C) Per-project only | **A + selective B** | 90% identical; root as source of truth |
| **Format Standard** | A) VS Code `mcp.json`<br>B) OpenCode `opencode.json`<br>C) Both (synced) | **C** | Different tools, different formats |
| **Inheritance Model** | A) File-level merge<br>B) Server-level merge<br>C) Explicit extends | **B** | Granular control per server |
| **Sync Mechanism** | A) Manual sync<br>B) Build-time generation<br>C) Pre-commit hook | **B + C** | Prevents drift |

### Milestone 2.2: Consolidation Plan (Days 5-7)
**Owner:** Lead Architect  
**Resources:** 1 FTE  
**Deliverable:** Detailed consolidation specification

**Target Architecture:**
```
C:\Users\Alexa\Desktop\SandBox\
├── opencode.json                    # Canonical OpenCode config (21 servers)
├── .mcp.json                        # Canonical MCP servers (26 servers) 
├── .vscode/mcp.json                 # Generated from .mcp.json (synced)
├── projects/
│   ├── Banking/
│   │   └── .cursor/mcp.json         # Project-specific (2 servers - exa, mcp-docker)
│   ├── comicwise/
│   │   └── .vscode/mcp.json         # Generated from root (if needed) or deleted
│   └── [other-projects]/
│       └── .vscode/mcp.json         # DELETED - inherit from root
└── docs/instructions/               # 100+ files - canonical, no deduping needed
```

---

## Phase 3: Implementation (Week 2-3)

### Milestone 3.1: Root Configuration Canonicalization (Days 8-10)
**Owner:** Configuration Engineer  
**Resources:** 1 FTE  
**Deliverable:** Validated root configs

| Task | Description | Effort | Validation |
|------|-------------|--------|------------|
| 3.1.1 | Audit `opencode.json` - verify all 21 servers work | 3h | `opencode mcp list` |
| 3.1.2 | Audit `.mcp.json` - verify all 26 servers work | 3h | `mcp-client test` |
| 3.1.3 | Create `.vscode/mcp.json` generator script | 2h | Diff matches current |
| 3.1.4 | Add sync validation to pre-commit | 2h | CI passes |
| 3.1.5 | Document server purpose in each config | 4h | README updated |

### Milestone 3.2: Project-Level Cleanup (Days 10-14)
**Owner:** Configuration Engineer  
**Resources:** 1 FTE  
**Deliverable:** Clean project configs

| Project | Action | Effort | Validation |
|---------|--------|--------|------------|
| `mcp-server-typescript` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `youtube-downloader` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `university-libary-jsm` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `selenium_webdriver` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `comicwise` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `xamehi` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `xamehi.tv` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `rhixe_scans` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `rhixecompany-comics` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `profile` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `cookiecutter-django-tailwind` | **DELETE** `.vscode/mcp.json` | 0.5h | No config drift |
| `Banking` | **KEEP** `.cursor/mcp.json` (unique) | 0.5h | Unique servers validated |

### Milestone 3.3: `.instructions.md` Verification (Days 12-14)
**Owner:** Documentation Engineer  
**Resources:** 1 FTE  
**Deliverable:** Verified instruction library

| Task | Description | Effort | Validation |
|------|-------------|--------|------------|
| 3.3.1 | Verify all 100+ files have valid frontmatter (`description`, `applyTo`) | 3h | Schema validation |
| 3.3.2 | Check for duplicate `applyTo` patterns | 2h | No conflicts |
| 3.3.3 | Validate file naming convention (`kebab-case.md`) | 1h | All pass |
| 3.3.4 | Cross-reference with project AGENTS.md files | 2h | Consistent guidance |
| 3.3.5 | Generate instruction index | 2h | `docs/instructions/INDEX.md` |

---

## Phase 4: Automation & Guardrails (Week 3-4)

### Milestone 4.1: Automated Sync Scripts (Days 15-18)
**Owner:** DevOps Engineer  
**Resources:** 1 FTE  
**Deliverable:** Production-ready sync automation

| Script | Purpose | Location | Trigger |
|--------|---------|----------|---------|
| `scripts/sync-mcp-config.ts` | Generate `.vscode/mcp.json` from `.mcp.json` | Root | Pre-commit, CI |
| `scripts/validate-mcp-config.ts` | Validate all MCP configs against schema | Root | CI, pre-push |
| `scripts/audit-instructions.ts` | Verify instruction library integrity | Root | CI weekly |
| `scripts/generate-instruction-index.ts` | Create `INDEX.md` | Root | On change |

### Milestone 4.2: Quality Gates (Days 18-20)
**Owner:** DevOps Engineer  
**Resources:** 1 FTE  
**Deliverable:** CI pipeline integration

| Gate | Tool | Config | Threshold |
|------|------|--------|-----------|
| MCP Config Schema | JSON Schema + custom validator | `.github/schemas/mcp.json` | 0 errors |
| Config Drift Detection | `sync-mcp-config.ts --check` | Root CI | 0 diffs |
| Instruction Frontmatter | Custom validator | `docs/instructions/` | 100% valid |
| Duplicate Detection | Hash-based comparison | All configs | 0 unexpected dupes |

### Milestone 4.3: Skill Development (Days 19-21)
**Owner:** Configuration Engineer + AI Agent Specialist  
**Resources:** 1.5 FTE  
**Deliverable:** Reusable skills for ongoing maintenance

| Skill | Purpose | Category |
|-------|---------|----------|
| `mcp-config-sync` | Sync root → project MCP configs | `devops` |
| `mcp-config-validate` | Validate MCP server configurations | `qa` |
| `instruction-library-audit` | Audit `.instructions.md` library | `docs` |
| `config-drift-detect` | Detect configuration drift | `devops` |

---

## Phase 5: Validation & Documentation (Week 4)

### Milestone 5.1: End-to-End Validation (Days 22-24)
**Owner:** QA Engineer  
**Resources:** 1 FTE  
**Deliverable:** Validation report

| Test | Description | Pass Criteria |
|------|-------------|---------------|
| 5.1.1 | OpenCode can connect to all 21 servers | All `enabled: true` servers connect |
| 5.1.2 | VS Code MCP extension loads all 26 servers | No connection errors |
| 5.1.3 | Project-specific configs work (Banking) | 2 servers connect |
| 5.1.4 | Deleted project configs don't break anything | No errors in projects |
| 5.1.5 | Instruction library loads in Copilot/Claude | All `applyTo` patterns match |

### Milestone 5.2: Documentation & Handoff (Days 24-26)
**Owner:** Technical Writer + Lead Architect  
**Resources:** 1.5 FTE  
**Deliverable:** Complete documentation package

| Document | Audience | Location |
|----------|----------|----------|
| `CONFIG_ARCHITECTURE.md` | All engineers | `docs/architecture/` |
| `MCP_SERVER_REFERENCE.md` | Agent users | `docs/reference/` |
| `INSTRUCTION_LIBRARY_GUIDE.md` | AI agents | `docs/instructions/README.md` |
| `SYNC_PROCEDURES.md` | Maintainers | `docs/maintenance/` |
| `TROUBLESHOOTING.md` | Support | `docs/troubleshooting/` |

---

## Resource Allocation Summary

| Role | Week 1 | Week 2 | Week 3 | Week 4 | Total FTE-Weeks |
|------|--------|--------|--------|--------|-----------------|
| Lead Architect | 1.0 | 0.5 | 0.0 | 0.5 | 2.0 |
| Configuration Engineer | 1.0 | 1.0 | 1.0 | 0.5 | 3.5 |
| DevOps Engineer | 0.0 | 0.0 | 1.0 | 1.0 | 2.0 |
| Documentation Engineer | 0.5 | 0.5 | 0.5 | 1.0 | 2.5 |
| QA Engineer | 0.0 | 0.0 | 0.0 | 1.0 | 1.0 |
| **Total** | **2.5** | **2.0** | **2.5** | **4.0** | **11.0** |

---

## Timeline Overview

```
Week 1: ████████████░░░░░░░░░░░░░░░░░░░░░░░░  (Discovery & Triage)
Week 2: ░░░░████████████████░░░░░░░░░░░░░░░░  (Strategy & Root Canonicalization)
Week 3: ░░░░░░░░░░████████████████████░░░░░░  (Project Cleanup & Automation)
Week 4: ░░░░░░░░░░░░░░░░░░██████████████████  (Validation & Documentation)
```

---

## Risk Mitigation

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| MCP server connection failures after cleanup | Medium | High | Test each server before deletion; keep backups |
| Agent tooling breaks due to config changes | Medium | High | Validate with OpenCode, VS Code, Copilot |
| Project-specific needs overlooked | Low | Medium | Interview project owners; document exceptions |
| Instruction library becomes stale | Low | Low | Automated weekly audit; owner assignment |
| Sync script fails in CI | Low | Medium | Comprehensive test suite; manual override |

---

## Success Criteria

1. **Zero Duplication:** No two `mcp.json` files have identical content (except generated)
2. **Single Source of Truth:** Root `.mcp.json` and `opencode.json` are canonical
3. **Automated Sync:** Pre-commit hook prevents drift; CI validates
4. **Project Autonomy:** Projects can opt-out/inherit via explicit mechanism
5. **Instruction Library:** 100% valid frontmatter; searchable index; no conflicting `applyTo`
6. **Agent Compatibility:** OpenCode, VS Code, Copilot, Hermes all work without config changes
7. **Documentation:** Complete architecture docs with troubleshooting guide

---

## Post-Implementation Maintenance

| Frequency | Task | Owner |
|-----------|------|-------|
| Per PR | Sync validation | CI (automated) |
| Weekly | Instruction library audit | Documentation Engineer |
| Monthly | MCP server health check | DevOps Engineer |
| Quarterly | Architecture review | Lead Architect |
| On-demand | New project onboarding | Configuration Engineer |

---

## Appendix: File Reference Matrix

### Root Configuration Files
| File | Purpose | Format | Servers | Status |
|------|---------|--------|---------|--------|
| `opencode.json` | OpenCode agent config | OpenCode schema | 21 | Canonical |
| `.mcp.json` | MCP server definitions | VS Code MCP schema | 26 | Canonical |
| `.vscode/mcp.json` | VS Code MCP extension | VS Code MCP schema | 27 | Generated |
| `.hermes.md` | Hermes agent profile | Custom | N/A | Canonical |

### Project Configuration Files (Post-Cleanup)
| Project | Config File | Servers | Source |
|---------|-------------|---------|--------|
| Banking | `.cursor/mcp.json` | 2 (exa, mcp-docker) | Project-specific |
| All others | *(none - inherit from root)* | 0 | Root `.mcp.json` |

### Instruction Files (Representative Sample)
| Category | Count | Example Files |
|----------|-------|---------------|
| Language-specific | 15 | `typescript.instructions.md`, `python.instructions.md`, `rust.instructions.md` |
| Framework-specific | 25 | `nextjs.instructions.md`, `reactjs.instructions.md`, `django.instructions.md` |
| Tool-specific | 20 | `testing.instructions.md`, `security.instructions.md`, `performance.instructions.md` |
| Platform-specific | 15 | `vercel.instructions.md`, `aws.instructions.md`, `azure.instructions.md` |
| Practice/Process | 15 | `code-review.instructions.md`, `documentation.instructions.md`, `git-workflow.instructions.md` |
| **Total** | **~90** | *(100+ files, some duplicates/legacy)* |

---

## Approval & Sign-off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Lead Architect | | | |
| Configuration Engineer | | | |
| DevOps Lead | | | |
| Documentation Lead | | | |

**Plan Version:** 1.0  
**Created:** 2026-01-24  
**Target Completion:** 2026-02-21