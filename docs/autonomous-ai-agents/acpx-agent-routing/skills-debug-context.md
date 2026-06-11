# Skill Audit: `acpx-agent-routing`

**Category:** autonomous-ai-agents  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\autonomous-ai-agents\acpx-agent-routing\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 2 minor  

---

## Frontmatter Check

```yaml
name: acpx-agent-routing
title: ACPX Agent Routing
description: "Route coding tasks to the optimal ACPX agent (Qwen Code, OpenCode, Copilot CLI) based on task type."
version: 1.1.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ACPX, Agent-Routing, Multi-Agent, Orchestration]
    related_skills: [qwen-code, opencode, copilot-cli, dispatching-parallel-agents]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: stale_model: old model name big-pickle |
| MINOR | C3 | Table pipe count inconsistency: {4, 5, 7} |

## Sections Present

- ✅ `## When to Use`
- ✅ `## Workflow`
- • `## Agent Routing Table`
- • `## Recommended Models`
- • `## ACPX Delegation Patterns`
- • `## Procedure`
- • `## Pitfalls`
- • `## Read-Only vs Read-Write Task Split Pattern`
- • `## Verification Checklist`

## Recommendations

- Fix `C1`: Stale pattern: stale_model: old model name big-pickle
- Fix `C3`: Table pipe count inconsistency: {4, 5, 7}
