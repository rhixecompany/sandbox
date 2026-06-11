# Skill Audit: `parallel-cli`

**Category:** (root)  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\parallel-cli\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 2 minor  

---

## Frontmatter Check

```yaml
name: parallel-cli
description: Optional vendor skill for Parallel CLI — agent-native web search, extraction, deep research, enrichment, FindAll, and monitoring. Prefer JSON output and non-interactive flows.
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Research, Web, Search, Deep-Research, Enrichment, CLI]
    related_skills: [duckduckgo-search, mcporter]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |
| MINOR | C1 | Stale pattern: supply_chain: npm install -g detected |

## Sections Present

- • `## When to use it`
- ✅ `## Workflow`
- • `## Installation`
- • `## Authentication`
- • `## Core rule set`
- • `## Quick reference`
- • `## Common flags and patterns`
- • `## Search`
- • `## Extraction`
- • `## Deep research`
- • `## Enrichment`
- • `## FindAll`
- • `## Monitor`
- • `## Recommended Hermes usage patterns`
- • `## Error handling and exit codes`
- • `## Maintenance`
- • `## Pitfalls`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
- Fix `C1`: Stale pattern: supply_chain: npm install -g detected
