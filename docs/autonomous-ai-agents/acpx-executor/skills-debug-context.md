# Skill Audit: `acpx-executor`

**Category:** autonomous-ai-agents  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\autonomous-ai-agents\acpx-executor\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 2 minor  

---

## Frontmatter Check

```yaml
name: acpx-executor
title: ACPX Universal Executor
description: "Execute a prompt via any ACPX provider (qwen, copilot, opencode) — single unified interface, correct CLI per provider."
version: 1.1.0
author: Alexa
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ACPX, Dispatch, Universal-Executor, Agent-Orchestration]
    related_skills: [qwen-code, copilot-cli, opencode, acpx-agent-routing]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: stale_model: old model name big-pickle |
| MINOR | C3 | Table pipe count inconsistency: {4, 5, 6} |

## Sections Present

- • `## Goal`
- ✅ `## Workflow`
- ✅ `## When to Use`
- • `## When NOT to Use`
- • `## Provider CLI Reference`
- • `## Procedure`
- • `## Fallback Chain`
- • `## Per-Provider Pitfalls`
- • `## All-Agents-Failed Recovery`
- • `## Read-Only vs Read-Write Guidance`
- • `## Verification`

## Recommendations

- Fix `C1`: Stale pattern: stale_model: old model name big-pickle
- Fix `C3`: Table pipe count inconsistency: {4, 5, 6}
