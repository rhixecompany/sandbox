---
name: sync-hermes-opencode
title: Sync Hermes OpenCode Codex
description: Bidirectional sync of skills, plugins, hooks, prompts, agents, and instructions across Hermes, OpenAI Codex, and OpenCode environments, with verification of parity after each sync.
trigger: /sync-hermes-opencode
category: general
version: 1.0.0
author: Hermes Agent
tags: 
metadata: 
hermes: 
profile: code-architect
priority: medium
copilot: 
model_required: sonnet
opencode: 
enabled: true
codex: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
license: MIT
---

## Table of Contents

## Goal
Bidirectional sync of skills, plugins, hooks, prompts, agents, and instructions across Hermes, OpenAI Codex, and OpenCode environments, with verification of parity after each sync.

## Context

## Phases

# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Rules](#rules)
- [Phases](#phases)
- [Verification Checklist](#verification-checklist)
- [Personas](#personas)
- [Personality](#personality)
- [Workflow](#workflow)
- [Best Practices](#best-practices)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)



- [Goal](#goal)
- [Context](#context)
- [Rules](#rules)
- [Phases](#phases)
- [Verification Checklist](#verification-checklist)
- [Personas](#personas)
- [Personality](#personality)
- [Workflow](#workflow)
- [Best Practices](#best-practices)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)





Bidirectional sync of skills, plugins, hooks, prompts, agents, and instructions across Hermes, OpenAI Codex, and OpenCode environments with verification.


- **Hermes root:** `C:\Users\Alexa\AppData\Local\hermes`
- **Workspace root:** `C:\Users\Alexa\Desktop\SandBox`
- **Progress artifact:** `docs/orchestrator-progress.md`
- **Verification artifact:** `docs/orchestrator-verification.md`
- **Agent roots:**
- Hermes → `~/AppData/Local/hermes/` (skills/, plugins/, hooks/, profiles/)
- OpenAI Codex → `~/.codex/` (agents/*.toml, skills/)
- OpenCode → `~/.opencode/` (config) and workspace `opencode.json`

## Rules

> Core rules: [`templates/rules-core.md`](templates/rules-core.md)

1. Execute phases in order; do not reorder.
2. Each phase must pass its gate before advancing.
3. Conflicts should be resolved or documented, not silently dropped.
4. **One platform at a time** — sync Hermes, Codex, and OpenCode sequentially, verifying each before the next.
5. **No backup files** — use git history for rollback; never create `.bak`, `.old`, or timestamped copies.


Full phase instructions live in `templates/phases.md`.

| Order | Phase | Gate |
| --- | --- | --- |
| 1 | Inventory Instructions & Agents | inventories complete; personality/profile mappings created |
| 2 | Identify Agent Roots | all 3 roots confirmed; paths documented |
| 3 | Bidirectional Sync | sync report written; conflicts resolved or documented |
| 4 | Verify Completion | verification report written; all critical assets in sync |

## Verification Checklist

- [ ] Phase 1 completed and verified
- [ ] Phase 2 completed and verified
- [ ] Phase 3 completed and verified
- [ ] Phase 4 completed and verified
- [ ] Progress logged in `docs/orchestrator-progress.md`
- [ ] Final verification report in `docs/orchestrator-verification.md`

## Personas

See [`templates/personas.md`](templates/personas.md) for shared persona templates.

| Persona | When to Use |
| ------- | ----------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/personality.md`](templates/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Workflow

See [`templates/section-skeleton.md`](templates/section-skeleton.md) for workflow structure.

1. **Diagnose** — Run diagnostics on all 3 agent roots.
2. **Plan** — Determine minimal changes; map per-platform asset formats.
3. **Fix** — Apply changes incrementally, one platform at a time.
4. **Verify** — Confirm fix works via file-backed evidence.
5. **Document** — Note what changed in the progress artifact.

## Best Practices

See [`templates/best-practices.md`](templates/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Dependencies

See [`templates/deps-core.md`](templates/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/skills-table-core.md`](templates/skills-table-core.md) for shared skills table.

| Skill | Purpose |
| ------- | --------- |
| `multi-agent-sync` | Canonical multi-platform sync workflow (Hermes, Codex, OpenCode) |
| `hermes-profiles` | Profile identity & state across Hermes |
| `opencode` | OpenCode CLI usage, roots, and verification |
| `systematic-debugging` | Root cause analysis and fix |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| Server | Purpose |
| ------ | ------- |
| `ast-grep` | AST-based code search and replace |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |
| `github` | GitHub API operations |

## Tasks

- [ ] Understand requirements and scope (3 platforms)
- [ ] Inventory each platform's assets and agent roots
- [ ] Plan approach and identify per-platform format mappings
- [ ] Execute work incrementally, one platform at a time
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section
```
# Prompt template
Execute the workflow defined in this file.
```
