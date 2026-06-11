# Skill Audit: `fastmcp`

**Category:** (root)  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\fastmcp\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 1 minor  

---

## Frontmatter Check

```yaml
name: fastmcp
description: Build, test, inspect, install, and deploy MCP servers with FastMCP in Python. Use when creating a new MCP server, wrapping an API or database as MCP tools, exposing resources or prompts, or preparing a FastMCP server for Claude Code, Cursor, or HTTP deployment.
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [MCP, FastMCP, Python, Tools, Resources, Prompts, Deployment]
    homepage: https://gofastmcp.com
    related_skills: [native-mcp, mcporter]
prerequisites:
  commands: [python3]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: pip install detected |

## Sections Present

- ✅ `## When to Use`
- • `## Prerequisites`
- • `## Included Files`
- ✅ `## Workflow`
- • `## Common Patterns`
- • `## Quality Bar`
- • `## Troubleshooting`
- • `## References`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: pip install detected
