# Skill Audit: `windows-maintenance-operations`

**Category:** devops  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\devops\windows-maintenance-operations\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A  
**Issues:** 0 critical / 0 major / 0 minor  

---

## Frontmatter Check

```yaml
name: windows-maintenance-operations
title: Windows Maintenance Operations
author: Alexa
trigger: |
  User asks to run cleanup, maintenance, or destructive operations on Windows:
  • Disk cleanup (delete dependencies, caches, temp files)
  • System cache clearing (NPM, Docker, WinGet, VS Code, etc.)
  • Package upgrades
  • Dependency removal
  • Any operation marked --dry-run or requiring explicit approval
description: |
  Execute destructive maintenance operations on Windows with safety, validation,
  and recovery procedures. Pattern: discover → preview → execute with approval →
  validate before/after → document recovery.
tags:
  - windows
  - maintenance
  - cleanup
  - disk-management
  - safety-critical
```

## Issues Found

_No issues — skill passes all checks._

## Sections Present

- • `## Trigger Conditions`
- • `## Workflow: Discovery → Preview → Execute → Validate`
- • `## Recovery Procedures`
- • `## Safety Guardrails`
- • `## Common Cleanup Targets & Space Freed (Typical Windows Dev Machine)`
- • `## Pitfalls`
- • `## Quick Reference`
- • `## References`
- • `## Verification Checklist`
- • `## Overview`
- ✅ `## When to Use`

## Recommendations

- None. Skill is well-formed.
