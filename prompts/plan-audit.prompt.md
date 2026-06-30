---
trigger: plan-audit
name: plan-audit
title: "Audit Agent Stack"
description: >
  Audit the full agent stack across Hermes, GitHub Copilot, and shared
  infrastructure. Inventory agents, plugins, MCP tools, custom agents,
  instructions, and prompt files. Report gaps, duplicates, and
  registration issues.
version: 1.0.0
author: "Hermes Agent (consolidated)"
license: MIT
tags:
  - audit
  - agents
  - automation
  - hermes
  - prompts
  - stack
  - dry
dependencies:
  - skill:context-map
  - skill:systematic-debugging
  - skill:verification-before-completion
  - skill:brainstorming
  - skill:simplify
  - skill:subagent-driven-development
  - tool:terminal
  - tool:search_files
skills:
  - context-map
  - systematic-debugging
  - verification-before-completion
  - brainstorming
  - simplify
  - subagent-driven-development
metadata:
  hermes:
    related_skills: []
    tags:
    - plan-audit.prompt

---
metadata:
  hermes:
    related_skills: []
    tags:
    - plan-audit.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - plan-audit.prompt

> **Shared template references:**
> - [Core rules](../prompts/templates/_shared/rules-core.md)
> - [Skills table](../prompts/templates/_shared/skills-table-core.md)
> - [Verification checklist](../prompts/templates/_shared/verification-checklist.md)

## Goal

Perform a comprehensive audit of all agents across configured platforms (Hermes, Copilot, Codex). Inventory their definitions, capabilities, tool exposure, and cross-references. Report inconsistencies, duplicates, and registration gaps.

**Consolidates:** `plan-acpx-agent-stack-audit-hermes`,
`plan-acpx-agent-stack-audit-shared`,
`plan-acpx-agent-stack-audit-copilot`
(three separate prompts that shared the same audit approach).

## Input

- **Scope** — Which platforms to audit: `hermes`, `copilot`, `shared`, or `all`
- **Target** — Specific agent/skill to focus on (optional, default: full inventory)
- **Output format** — Markdown report, JSON inventory, or both

## Core Rules

See [`prompts/templates/_shared/rules-core.md`](../prompts/templates/_shared/rules-core.md).

Additional audit-specific rules:

1. **One platform at a time** — Audit Hermes, then Copilot, then cross-reference.
2. **File-backed evidence** — Every finding must reference a specific file or config.
3. **Explicit mapping** — Use cross-reference tables, not heuristics.
4. **No silent omissions** — Report every platform even if it has zero agents.
5. **DRY inventory** — Shared agent definitions belong in one place; flag duplicates.

## Workflow

### Phase 1: Hermes audit

1. Inventory Hermes skills: `find ~/AppData/Local/hermes/skills/ -name "SKILL.md"`
2. Extract: skill name, description, tags, dependencies from frontmatter.
3. Inventory Hermes plugins: `ls ~/AppData/Local/hermes/plugins/`
4. Inventory Hermes MCP server config: `grep -A5 'mcp_servers' ~/AppData/Local/hermes/config.yaml`
5. Cross-reference: every `dependencies: - skill:xxx` in prompts against ~/AppData/Local/hermes/skills/

### Phase 2: Copilot audit

1. Inventory Copilot custom agents: search `.github/copilot-instructions.md`, `.github/agents/`, `.github/copilot-agent.md`
2. Extract: agent name, description, instructions file reference.
3. Note: Copilot workspaces may have zero custom agents — that's valid.

### Phase 3: Shared / cross-reference

1. Map every agent by name across Hermes + Copilot.
2. Identify duplicates: same name in both platforms, same purpose.
3. Identify broken references: prompts referencing skills that don't exist.
4. Identify orphan agents: agent files with no cross-references.

### Phase 4: Report

Write to `docs/agent-stack-audit-report.md`:

| Platform | Agents | Skills | Plugins | MCP Tools | Issues |
|----------|--------|--------|---------|-----------|--------|
| Hermes   | N      | N      | N       | N         | N      |
| Copilot  | N      | N      | N/A     | N/A       | N      |
| Shared   | N      | N      | N       | N         | N      |

Issues table:
- **Duplicates** — Same agent registered in multiple places
- **Broken refs** — Dependencies pointing to missing assets
- **Orphans** — Files referenced by nothing
- **Registration gaps** — Agents not properly wired

## Verification Checklist
- [ ] Hermes skills/plugins/MCP inventoried
- [ ] Copilot agents/instructions inventoried
- [ ] Cross-reference table built
- [ ] All duplicate agents flagged
- [ ] All broken references flagged
- [ ] Report written with actionable findings
- [ ] Inventory saved to `docs/agent-stack-audit-report.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
