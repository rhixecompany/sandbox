# Session Startup Protocol (Mandatory)

> Authoritative reference for the 5-skill mandatory session startup sequence. Updated 2026-06-21 per user directive.

## Overview

Every Hermes session MUST execute this exact sequence before any response or task. No exceptions.

## The 5 Mandatory Skills (Load Order)

| # | Skill | Purpose | Verification |
|---|-------|---------|--------------|
| 1 | `using-superpowers` | Foundational skill workflow, task identification, skill discovery | Loaded first; establishes Phase 1-4 workflow |
| 2 | `user-communication-preferences` | Concise action-first responses, DRY, blunt+technical tone | Loaded second; applies to all subsequent output |
| 3 | `session-audit-report` | Generate SESSION_REPORT.md with full previous session audit | Loaded third; writes report to cwd |
| 4 | `hermes-profiles` | Profile identity, provider enumeration, system maintenance, **profile-per-task routing** | Loaded fourth; enables `hermes profile use <name>` |
| 5 | `validate-memories` | Validate USER.md/MEMORY.md across all profiles | Loaded fifth; reports drift/issues |

## Verification Checklist (After Each Skill Load)

- [ ] Skill loaded via `skill_view()` — not just invoked
- [ ] Skill content reviewed and workflow understood
- [ ] Any session-derived updates in skill applied
- [ ] Cross-references to other mandatory skills noted

## Post-Startup Actions (After All 5 Loaded)

1. **Read SESSION_REPORT.md** — Search SandBox, read completely, explain back before proceeding
2. **Verify global USER.md & SOUL.md** — Exist and are current at `~/.hermes/USER.md`, `~/.hermes/SOUL.md`
3. **Check model/profile match** — If different from report, update self-identification
4. **Run `hermes profile use <name>`** — Match task type per routing table below
5. **MCP-first tool selection** — Before any native tool, check MCP server availability

## Profile-Per-Task Routing Table

| Task Type | Profile | Model | Provider |
|-----------|---------|-------|----------|
| Code implementation, debugging, refactoring | `code-architect` | nemotron-3-ultra-free | opencode-zen |
| Deep research, literature review, synthesis | `research-analyst` | nemotron-3-ultra-free | opencode-zen |
| Design, content creation, brainstorming | `creative-director` | nemotron-3-ultra-free | opencode-zen |
| Planning, coordination, admin | `exec-assistant` | nemotron-3-ultra-free | opencode-zen |
| Tutorials, explanations, teaching | `patient-tutor` | nemotron-3-ultra-free | opencode-zen |
| System operations, DevOps, infra | `adminbot` | nemotron-3-ultra-free | opencode-zen |
| General purpose | `default` | gpt-5.4-mini | openai-codex |

## MCP Server Precedence (11 Configured)

Before using native tools, check these MCP servers:

| Server | Capability | Native Equivalent |
|--------|------------|-------------------|
| filesystem | Project file access (sandboxed) | `read_file`, `write_file`, `search_files`, `terminal` |
| github | GitHub API operations | `gh` CLI via terminal |
| ast-grep | Code pattern searching (AST) | `grep`/`rg` via terminal |
| memory | Persistent memory backend | `memory` tool |
| playwright | Browser automation | `browser` toolset |
| sequential-thinking | Structured reasoning | Manual reasoning |
| cli | Built-in CLI tools | `terminal` |
| code-sandbox | Node.js code execution | `execute_code` |
| fetch | Web content fetching | `web_extract` |
| mcp-docker | Docker container management | `docker` via terminal |

## Context Files Updated (2026-06-21)

All context files now encode this protocol:

- **SOUL.md** — Core Rule #6: Session Startup (Mandatory)
- **USER.md** — Execution Preferences: Session Startup (Mandatory)
- **MASTER_RULES.md** — Level 1 Rule #6: Session Startup (Mandatory)
- **PROJECT_RULES.md** — Level 1 Rules #4-6: Session Startup, MCP First, Profile Per Task
- **AGENTS.md** — Quick Rules #6-8: Session Startup, MCP First, Profile Per Task
- **.hermes.md** — Session Startup Rules section (full detail)

## Enforcement

- If any skill missing → load immediately via skill tool
- If profile not switched → run `hermes profile use <name>` before task
- If native tool used when MCP available → redo with MCP tool
- This is a hard constraint — not a suggestion

## Related References

- `references/session-reporting.md` — SESSION_REPORT.md templates and verification
- `references/skill-library-hygiene.md` — Skill maintenance patterns
- `using-superpowers` skill — Phase 1-4 workflow with MCP-first and profile routing integrated