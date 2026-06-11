# Skill Audit: `claude-code`

**Category:** autonomous-ai-agents  
**Path:** `C:\Users\Alexa\AppData\Local\hermes\profiles\adminbot\skills\autonomous-ai-agents\claude-code\SKILL.md`  
**Audited:** 2026-06-04  
**Grade:** A-  
**Issues:** 0 critical / 0 major / 2 minor  

---

## Frontmatter Check

```yaml
name: claude-code
title: Claude Code
description: "Delegate coding to Claude Code CLI (features, PRs)."
version: 2.2.0
author: Hermes Agent + Teknium
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [Coding-Agent, Claude, Anthropic, Code-Review, Refactoring, PTY, Automation]
    related_skills: [codex, hermes-agent, opencode]
```

## Issues Found

| Severity | Code | Description |
|----------|------|-------------|
| MINOR | C1 | Stale pattern: supply_chain: npm install -g detected |
| MINOR | C1 | Stale pattern: placeholder: TODO/FIXME text present |

## Sections Present

- • `## Prerequisites`
- • `## Two Orchestration Modes`
- • `## PTY Dialog Handling (CRITICAL for Interactive Mode)`
- • `## CLI Subcommands`
- • `## Print Mode Deep Dive`
- • `## Complete CLI Flags Reference`
- • `## Settings & Configuration`
- • `## Interactive Session: Slash Commands`
- • `## Interactive Session: Keyboard Shortcuts`
- • `## PR Review Pattern`
- • `## Parallel Claude Instances`
- • `## CLAUDE.md — Project Context File`
- • `## Architecture`
- • `## Key Commands`
- • `## Code Standards`
- • `## Custom Subagents`
- • `## Hooks — Automation on Events`
- • `## MCP Integration`
- • `## Monitoring Interactive Sessions`
- • `## Environment Variables`
- • `## Cost & Performance Tips`
- • `## Pitfalls & Gotchas`
- • `## Rules for Hermes Agents`
- ✅ `## When to Use`

## Recommendations

- Fix `C1`: Stale pattern: supply_chain: npm install -g detected
- Fix `C1`: Stale pattern: placeholder: TODO/FIXME text present
