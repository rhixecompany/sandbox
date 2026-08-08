---
name: plan-audit
title: Audit Agent Stack
description: 'Audit the full agent stack across Hermes, GitHub Copilot, and shared infrastructure. Inventory agents, plugins, MCP tools, custom agents, instructions, and prompt files. Report gaps, duplicates, and registration issues.'
version: 1.0.0
license: MIT
author: Hermes Agent (consolidated)
toolsets:
  - file
  - terminal
scripts: []
skills:
  - context-map
  - systematic-debugging
  - verification-before-completion
  - brainstorming
  - simplify
  - subagent-driven-development
formatter: default
plan: 'None'
dependencies:
  - "skill:context-map"
  - "skill:systematic-debugging"
  - "skill:verification-before-completion"
  - "skill:brainstorming"
  - "skill:simplify"
  - "skill:subagent-driven-development"
  - "tool:terminal"
  - "tool:search_files"
tags:
  - agents
  - ai-assistant
  - audit
  - configuration
  - git
  - planning
  - prompts
  - skills
  - typescript
trigger: /plan-audit
metadata:
  hermes: {}
---

## Goal

Audit the full agent stack across Hermes, GitHub Copilot, and shared infrastructure. Inventory agents, plugins, MCP tools, custom agents, instructions, and prompt files. Report gaps, duplicates, and registration issues.

> **Shared template references:**>> - [Core rules](templates/_shared/rules-core.md)> - [Skills table](templates/_shared/skills-table-core.md)> - [Verification checklist](templates/_shared/verification-checklist.md)

## Input

- **Scope** — Which platforms to audit: `hermes`, `copilot`, `shared`, or `all`
- **Target** — Specific agent/skill to focus on (optional, default: full inventory)
- **Output format** — Markdown report, JSON inventory, or both

## Core Rules

See [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md).Additional audit-specific rules:1. **One platform at a time** — Audit Hermes, then Copilot, then cross-reference.2. **File-backed evidence** — Every finding must reference a specific file or config.3. **Explicit mapping** — Use cross-reference tables, not heuristics.4. **No silent omissions** — Report every platform even if it has zero agents.5. **DRY inventory** — Shared agent definitions belong in one place; flag duplicates.

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

Write to `docs/agent-stack-audit-report.md`:| Platform | Agents | Skills | Plugins | MCP Tools | Issues ||----------|--------|--------|---------|-----------|--------|| Hermes   | N      | N      | N       | N         | N      || Copilot  | N      | N      | N/A     | N/A       | N      || Shared   | N      | N      | N       | N         | N      |Issues table:- **Duplicates** — Same agent registered in multiple places- **Broken refs** — Dependencies pointing to missing assets- **Orphans** — Files referenced by nothing- **Registration gaps** — Agents not properly wired

## Verification Checklist

- [ ] Hermes skills/plugins/MCP inventoried
- [ ] Copilot agents/instructions inventoried
- [ ] Cross-reference table built
- [ ] All duplicate agents flagged
- [ ] All broken references flagged
- [ ] Report written with actionable findings
- [ ] Inventory saved to `docs/agent-stack-audit-report.md`

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Context

Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.

## Phases

### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings clearly.
- Stop once the requested result is delivered.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions
