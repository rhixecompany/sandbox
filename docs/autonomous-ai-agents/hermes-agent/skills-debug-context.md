# Skill Audit: `hermes-agent`

**Category:** autonomous-ai-agents  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\autonomous-ai-agents\hermes-agent\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 2 minor  

---

## Frontmatter Check

```yaml
name: hermes-agent
title: Hermes Agent
description: "Configure, extend, or contribute to Hermes Agent."
version: 2.1.0
author: Hermes Agent + Teknium
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [hermes, setup, configuration, multi-agent, spawning, cli, gateway, development]
    homepage: https://github.com/NousResearch/hermes-agent
    related_skills: [claude-code, codex, opencode]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |
| MINOR | C3 | Table pipe count inconsistency: {8, 3, 4} |

## Sections Present

- • `## Goal`
- ✅ `## Workflow`
- • `## Quick Start`
- • `## CLI Reference`
- • `## Slash Commands (In-Session)`
- • `## Key Paths & Config`
- • `## Security & Privacy Toggles`
- • `## Voice & Transcription`
- • `## Spawning Additional Hermes Instances`
- • `## Durable & Background Systems`
- • `## Windows-Specific Quirks`
- ✅ `## When to Use`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
- Fix `C3`: Table pipe count inconsistency: {8, 3, 4}
