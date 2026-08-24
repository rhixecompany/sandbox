# Audit Report: Hermes Profiles & AI Agent Configs Inventory

**Generated:** 2026-08-24T23:59:59Z  
**Workspace:** C:/Users/Alexa/Desktop/SandBox  
**Hermes Home:** C:/Users/Alexa/AppData/Local/hermes  

---

## Executive Summary

| Category | Count | Status |
|----------|-------|--------|
| Hermes Profiles | 14 | 13 complete, 1 (default) missing files |
| Root Hermes Files | 3 | All present |
| Workspace Root Context Files | 6 | 5 present, 1 missing (copilot-instructions.md) |
| Subprojects with Context Files | 18 | All have AGENTS.md |
| AI Agent Configs | 4 | OpenCode, Codex, VS Code (2), Copilot (none) |

---

## 1. Hermes Profiles Inventory (14 profiles)

### Root Files (C:/Users/Alexa/AppData/Local/hermes/)
| File | Lines | Size | Modified | Frontmatter |
|------|-------|------|----------|-------------|
| SOUL.md | 253 | 12,135 B | 2026-08-20 | ✓ |
| memories/USER.md | 39 | 1,817 B | 2026-08-20 | ✓ |
| memories/MEMORY.md | 35 | 4,272 B | 2026-08-20 | ✗ (MD041 §-delimited) |

### Profile Files (14 profiles × 3 files = 42 files expected)

| Profile | SOUL.md | USER.md | MEMORY.md | Total | Notes |
|---------|---------|---------|-----------|-------|-------|
| alexa | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| code-architect | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| creative-director | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| cto | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| **default** | **MISSING** | **MISSING** | **MISSING** | **0/3** | **Root IS default** |
| designer | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| dev | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| exec-assistant | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| ops | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| patient-tutor | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| pm | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| qa | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| research-analyst | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |
| security | 55 lines | 26 lines | 5 lines | 3/3 | ✓ |

**Key Findings:**
- **14 profiles exist** (not 7 as assumed in plan) — cto, designer, dev, pm, qa, security are additional
- **default profile has NO files** in profiles/default/ — root files serve as default
- **All profile SOUL.md files are 55 lines** — identical Multi-File Change Protocol block (DRY violation)
- **All profile USER.md files are 26 lines** — identical content (DRY violation)  
- **All profile MEMORY.md files are 5 lines** — minimal stubs, not leveraging root MEMORY.md facts

---

## 2. Workspace Context Files Inventory

### SandBox Root (C:/Users/Alexa/Desktop/SandBox/)
| File | Lines | Size | Modified | Frontmatter | Purpose |
|------|-------|------|----------|-------------|---------|
| .hermes.md | 90 | 5,336 B | — | ✓ | Hermes project overrides |
| AGENTS.md | 638 | 35,242 B | — | ✗ | Canonical agent guidance |
| CLAUDE.md | 7 | 307 B | — | ✓ | Thin stub → AGENTS.md |
| .cursorrules | 8 | 322 B | — | ✗ | Thin stub → AGENTS.md |
| copilot-instructions.md | **MISSING** | — | — | — | Should be at root |
| .github/copilot-instructions.md | 685 | 25,236 B | — | ✗ | Copilot instructions |

### Subprojects (18 projects)
All 18 subprojects have **AGENTS.md**. Distribution of other files:

| Subproject | AGENTS.md | CLAUDE.md | .cursorrules | copilot-instructions.md | .github/copilot-instructions.md |
|------------|-----------|-----------|--------------|------------------------|----------------------------------|
| Banking | ✓ | — | — | ✓ | ✓ |
| Bash | ✓ | — | — | ✓ | — |
| comicwise | ✓ | — | ✓ | ✓ | ✓ |
| cookiecutter-django-tailwind | ✓ | — | — | — | ✓ |
| Django-Scrapy-Selenium | ✓ | — | ✓ | ✓ | ✓ |
| docs | ✓ | — | — | — | — |
| ecom | ✓ | — | — | ✓ | ✓ |
| mcp-servers | ✓ | — | — | — | — |
| profile | ✓ | — | — | — | ✓ |
| Python-projects | ✓ | — | — | — | ✓ |
| Resume_maker | ✓ | — | — | ✓ | ✓ |
| rhixecompany-comics | ✓ | — | — | ✓ | ✓ |
| rhixe_scans | ✓ | — | — | ✓ | ✓ |
| selenium_webdriver | ✓ | — | — | ✓ | ✓ |
| university-libary-jsm | ✓ | — | — | — | ✓ |
| xamehi | ✓ | — | — | — | ✓ |
| xamehi.tv | ✓ | — | — | ✓ | ✓ |
| youtube-downloader | ✓ | — | — | — | ✓ |

**Key Findings:**
- **18 subprojects** (not 17) — all have AGENTS.md
- **Inconsistent copilot-instructions.md locations** — some at project root, some in .github/
- **Only 3 subprojects have .cursorrules** — comicwise, Django-Scrapy-Selenium
- **docs/ has only AGENTS.md** — minimal project

---

## 3. AI Agent Configs Inventory

| Agent | Config File | Lines | Key Model Setting |
|-------|-------------|-------|-------------------|
| **OpenCode** | C:/Users/Alexa/Desktop/SandBox/opencode.json | 206 | `"model": "opencode/nemotron-3-ultra-free"` |
| **Codex** | C:/Users/Alexa/.codex/config.toml | 127 | `model = "gpt-5.4-mini"` |
| **VS Code (workspace)** | C:/Users/Alexa/Desktop/SandBox/.vscode/settings.json | 97 | Workspace settings |
| **VS Code (user)** | C:/Users/Alexa/AppData/Roaming/Code/User/settings.json | 503 | User settings |
| **Copilot CLI** | — | — | Not found |

**Key Findings:**
- **OpenCode uses opencode-zen provider** with nemotron-3-ultra-free (matches Hermes default profile)
- **Codex uses gpt-5.4-mini** — different provider/model than Hermes
- **No standalone Copilot CLI config found** — relies on VS Code settings
- **VS Code has both workspace and user settings** — potential conflicts

---

## 4. Hermes Live Config State

### Current Model (from `hermes config show`)
```
Model: nemotron-3-ultra-free
Provider: opencode-zen
Base URL: https://opencode.ai/zen/v1
```

### Authorized Providers (from `hermes auth list` - 11 providers)
| Provider | Credentials | Status |
|----------|-------------|--------|
| copilot | 3 | ✓ |
| deepseek | 1 | ✓ |
| gemini | 1 | ✓ |
| huggingface | 1 | ✓ |
| nous | 1 | ✓ (device_code) |
| ollama-cloud | 1 | ✓ |
| openai-codex | 1 | ✓ (device_code) |
| opencode-zen | 2 | ✓ |
| openrouter | 1 | ✓ |
| xai | 2 | ⚠ 1 auth failed (403) |
| xai-oauth | 1 | ✓ (device_code) |

### Active Profiles (from `hermes profile list` - 14 profiles)
| Profile | Model | Gateway | Alias |
|---------|-------|---------|-------|
| **default** | **nemotron-3-ultra-free** | running | — |
| alexa | deepseek-v4-flash-free | running | alexa |
| code-architect | deepseek-v4-flash-free | running | code-architect |
| creative-director | deepseek-v4-flash-free | running | creative-director |
| cto | deepseek-v4-flash-free | running | cto |
| designer | deepseek-v4-flash-free | running | designer |
| dev | deepseek-v4-flash-free | running | dev |
| exec-assistant | deepseek-v4-flash-free | running | exec-assistant |
| ops | deepseek-v4-flash-free | running | ops |
| patient-tutor | deepseek-v4-flash-free | running | patient-tutor |
| pm | deepseek-v4-flash-free | running | pm |
| qa | deepseek-v4-flash-free | running | qa |
| research-analyst | deepseek-v4-flash-free | running | research-analyst |
| security | deepseek-v4-flash-free | running | security |

**Critical Discrepancy:** 
- **Root SOUL.md** says: `Model: nemotron-3-ultra-free (opencode-zen)` 
- **All 13 profile SOUL.md files** say: `Model: deepseek-v4-flash-free (opencode-zen)`
- **hermes profile list** shows: default=nemotron, ALL OTHERS=deepseek-v4-flash-free
- **OpenCode config** uses: nemotron-3-ultra-free

---

## 5. test-providers-models.prompt.md Analysis

### Current State (from prompt file)
The prompt defines:
- **Authorized providers:** copilot, deepseek, gemini, huggingface, nous, ollama-cloud, openai-codex, opencode-zen, openrouter, xai, xai-oauth (11) — **matches `hermes auth list`**
- **Verified working models (example baseline):**
  - opencode-zen: deepseek-v4-flash-free (128K, reasoning✓)
  - openrouter: nvidia/nemotron-3-ultra-550b-a55b:free (1M)
  - gemini: gemini-2.5-flash (1M, reasoning✓)
- **Excluded (example baseline):** deepseek (402), huggingface (400), nous (403), xai-oauth (402), openai-codex (429), copilot (n/a)

### Issues:
1. **Hardcoded example baselines** — not live probe results
2. **Nemotron model mismatch:** Prompt references `nvidia/nemotron-3-ultra-550b-a55b:free` on openrouter, but Hermes uses `nemotron-3-ultra-free` on opencode-zen
3. **No live verification gate** — prompt doesn't enforce re-probing before use
4. **Provider list in prompt** should be generated from `hermes auth list` dynamically

---

## 6. DRY Violations Catalog

### Multi-File Change Protocol (55 lines) — Repeated 13 times
**Location:** Every profile SOUL.md (lines 30-55)
**Content:** Identical 14-skill stack + protocol
**Fix:** Reference parent SOUL.md; keep only profile-specific identity/tone/rules in profile SOUL.md

### USER.md Content (26 lines) — Repeated 13 times
**Location:** Every profile memories/USER.md
**Content:** Identical identity, model, execution preferences, routing table
**Fix:** Template with profile-specific variables (name, model preferences)

### MEMORY.md Content (5 lines) — Repeated 13 times
**Location:** Every profile memories/MEMORY.md
**Content:** Minimal stub with multi-file protocol + profile name
**Fix:** Inherit from root MEMORY.md; add only profile-specific facts

### Profile Routing Table — Inconsistent
**Current:** `ops→alexa` (alexa is a profile, not a routing target)
**Correct:** `ops→adminbot` (per SOUL.md routing table)

---

## 7. File Count Summary

| Layer | Files | Total Lines | Est. Size |
|-------|-------|-------------|-----------|
| Root Hermes | 3 | 327 | ~18 KB |
| Profiles (14 × 3) | 42 | 1,162 | ~70 KB |
| Workspace Root | 5 | 1,428 | ~66 KB |
| Subprojects (18) | ~72 | ~varies | ~varies |
| AI Agent Configs | 4 | 933 | ~13 KB |
| **TOTAL** | **~126** | **~3,850** | **~167 KB** |

---

## 8. Recommended Action Priority

### P0 — Critical (Blockers)
1. **Fix default profile** — Create profiles/default/ or document root-as-default pattern
2. **Resolve model discrepancy** — Root SOUL.md vs profile SOUL.md vs hermes profile list
3. **Remove DRY violations** — Consolidate multi-file protocol, USER.md, MEMORY.md into templates

### P1 — High (Consistency)
4. **Update all 14 profile files** from templates (not 7 as planned)
5. **Sync test-providers-models.prompt.md** with live `hermes auth list` and verified models
6. **Add missing root copilot-instructions.md** or remove reference

### P2 — Medium (Quality)
7. **Standardize subproject context files** — consistent copilot-instructions.md location
8. **Add .cursorrules stubs** to subprojects missing them
9. **Align AI agent models** — OpenCode/Codex/VS Code to verified working models

### P3 — Low (Maintenance)
10. **Create verification script** for ongoing sync
11. **Document maintenance runbook**
12. **Tag baseline release**

---

## 9. Inventory Artifacts

Raw JSON inventories saved to `.hermes/plans/`:
- `audit-inventory.json` — Profile files detail
- `workspace-inventory.json` — Workspace context files detail  
- `agent-config-inventory.json` — AI agent configs detail

---

*This audit used MCP filesystem tools and terminal commands for live config state.*
*Next: Phase 2 — Design Consolidated Templates*