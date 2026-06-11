# Skill Audit: `xurl`

**Category:** social-media  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\social-media\xurl\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 1 minor  

---

## Frontmatter Check

```yaml
name: xurl
title: Xurl
description: "X/Twitter via xurl CLI: post, search, DM, media, v2 API."
version: 1.1.1
author: xdevplatform + openclaw + Hermes Agent
license: MIT
platforms: [linux, macos]
prerequisites:
  commands: [xurl]
metadata:
  hermes:
    tags: [twitter, x, social-media, xurl, official-api]
    homepage: https://github.com/xdevplatform/xurl
    upstream_skill: https://github.com/openclaw/openclaw/blob/main/skills/xurl/SKILL.md
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: npm install -g detected |

## Sections Present

- • `## Secret Safety (MANDATORY)`
- • `## Installation`
- • `## One-Time User Setup (user runs these outside the agent)`
- • `## Quick Reference`
- • `## Command Details`
- • `## Raw API Access`
- • `## Global Flags`
- • `## Streaming`
- • `## Output Format`
- • `## Common Workflows`
- • `## Error Handling`
- • `## Agent Workflow`
- • `## Troubleshooting`
- • `## Notes`
- • `## Attribution`
- ✅ `## When to Use`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: npm install -g detected
