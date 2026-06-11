# Skill Audit: `python-debugpy`

**Category:** software-development  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\software-development\python-debugpy\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 1 minor  

---

## Frontmatter Check

```yaml
name: python-debugpy
title: Python Debugpy
description: "Debug Python: pdb REPL + debugpy remote (DAP)."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos]
metadata:
  hermes:
    tags: [debugging, python, pdb, debugpy, breakpoints, dap, post-mortem]
    related_skills: [systematic-debugging, node-inspect-debugger, debugging-hermes-tui-commands]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |

## Sections Present

- ✅ `## Workflow`
- • `## Overview`
- ✅ `## When to Use`
- • `## pdb Quick Reference`
- • `## Recipe 1: Local breakpoint`
- • `## Recipe 2: Launch a script under pdb (no source edits)`
- • `## Recipe 3: Debug a pytest test`
- • `## Recipe 4: Post-mortem on any exception`
- • `## Recipe 5: Remote debug with debugpy (attach to running process)`
- • `## Debugging Hermes-specific Processes`
- • `## Common Pitfalls`
- • `## Verification Checklist`
- • `## One-Shot Recipes`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
