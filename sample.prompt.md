---
title: Multi-Agent Research and Implementation Template
description: Reusable prompt for Codex, Copilot, and Hermes. It preserves the current research targets while factoring out the shared workflow.
tags: [codex, copilot, hermes, research, planning, automation]
---

# Purpose

This prompt is a reusable template for Codex, Copilot, and Hermes. It defines a strict 6-phase workflow (Skills Audit → MCP Research → Hermes Docs → Profiles → Docs Inventory → Config Audit) with template variables for cross-agent compatibility. Research targets are preserved unless explicitly overridden.

## Context

This template is designed for multi-agent research and implementation workflows. It provides a structured approach that works across Codex (terminal commands), Copilot (workflow tools), and Hermes (CLI commands). The template preserves research targets while allowing agent-specific command syntax substitution.

**Target Agents:** Codex, Copilot, Hermes
**Workspace:** `C:\Users\Alexa\Desktop\SandBox`
**Documentation Root:** `docs/`
**Execution Model:** Sequential phases with verification gates
Keep the default research targets below unless the user replaces them.
When a target depends on native agent syntax, use the active agent's
equivalent command style and preserve the order of operations.

## Template Variables

| Variable             | Value                                         |
| -------------------- | --------------------------------------------- |
| `{{workspace_root}}` | `C:\\Users\\Alexa\\Desktop\\SandBox`          |
| `{{docs_root}}`      | `docs/`                                       |
| `{{agent_name}}`     | `Codex` / `Copilot` / `Hermes`                |
| `{{native_plan}}`    | the active agent's planning or update command |
| `{{native_search}}`  | the active agent's search command             |
| `{{native_extract}}` | the active agent's content extraction command |
| `{{native_files}}`   | the active agent's file read/write command    |

## Agent Mapping

| Agent              | Approach                                                                    |
| ------------------ | --------------------------------------------------------------------------- |
| Codex              | Terminal commands + workspace-local file edits                              |
| Copilot            | Copilot workflow tools available in the current environment                 |
| Hermes             | Hermes CLI commands exactly as written in the target steps                  |
| Missing capability | Use the closest safe equivalent and note the substitution before continuing |

### Command Examples

```bash
# Codex
hermes profile create code-architect --clone-all

# Copilot
# Use equivalent Copilot workflow tools

# Hermes
hermes skills audit && hermes skills update
hermes mcp install linear
```

## Shared Rules

1. If a plan already exists, update it before starting anything else.
2. Research first, then extract, then write docs, then plan, then implement, then verify.
3. Preserve the current research targets unless the user explicitly changes them.
4. Keep each stage reversible and easy to resume.
5. Write extracted findings to Markdown under `docs/` with a clear index.
6. Do not mark work complete until the relevant verification checks pass.
7. If a step depends on a native agent command, use the active agent's equivalent instead of forcing one syntax across all agents.
8. Keep the prompt reusable: replace only the template variables, not the workflow.

## Core Workflow

1. Update the plan if one already exists.
2. Execute the current research target set.
3. Extract source pages or links into Markdown files.
4. Organize the results under `docs/` with subfolders and an index.
5. Read the generated Markdown files and turn them into a concrete plan.
6. Implement only after the plan is complete and current.
7. Verify, debug, and fix issues before claiming success.

## Default Research Targets

### Phase 1: Skills Discovery and Audit

- [ ] Start with `/plan` if a plan already exists; update it.
- [ ] Execute Hermes skills browse to list everything available.
- [ ] Search and filter the top 50 best skills that are not already installed or available.
- [ ] Execute Hermes skills search with the skill name to find skills by keyword.
- [ ] Install all matching skills after a security scan.
- [ ] Run `/skills audit`.
- [ ] Run `/systematic-debugging` to debug and fix all issues.

### Phase 2: MCP Server and Tool Research

Research install, test, and verify steps for:

- vitest
- playwright
- django
- sequential-thinking
- context7
- sentry
- github official
- gitmcp
- fetch
- scrapegraph
- time
- memory
- youtube transcripts
- Desktop Commander
- filesystem
- node.js sandbox
- redis
- markitdown
- google maps
- ast-grep
- npm sentinel
- sqlite
- hacker news
- markdownify
- postman
- cloud run
- stripe
- apify
- chroma
- python refactoring assistant
- neo4j memory
- api gateway
- next.js devtools
- python interpreter
- gemini api docs
- hostinger api
- google flights
- neon
- shadcn
- uv
- linear
- mcp-docker

After research:

## Steps

1. Web search for installation, testing, and configuration guidance for each MCP server/tool
2. Web extract all relevant links and save as Markdown files
3. Build an index cataloging the pages in the current directory
4. Create a `docs/` folder with subfolders named for the page titles
5. Read the newly created Markdown files
6. Create or update the plan from those findings
7. Implement the plan only after the research and extraction work is complete
8. Verify the implementation only after the plan has been executed

## Tasks

- [ ] Web search for installation, testing, and configuration guidance
- [ ] Web extract all relevant links
- [ ] Save one Markdown file per page
- [ ] Build an index that catalogs the pages in the current directory
- [ ] Create a `docs/` folder with subfolders named for the page titles
- [ ] Read the new Markdown files
- [ ] Create or update the plan
- [ ] Implement the plan only after the research and extraction work is complete
- [ ] Verify the implementation only after the plan has been executed

### Phase 3: Hermes Docs and Ecosystem

Research and extract each page into Markdown:

- [Awesome Hermes Agent](https://github.com/0xNyk/awesome-hermes-agent)
- [Skills System](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [MCP (Model Context Protocol)](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [Use MCP with Hermes](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)
- [Personality & SOUL.md](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)
- [Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
- [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [Tips & Best Practices](https://hermes-agent.nousresearch.com/docs/guides/tips)
- [Tools & Toolsets](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)
- [Learning Path](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)
- [Event Hooks](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)
- [Plugins](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)

**Generated Output:** [Phase 3 Index](./docs/hermes/index.md) — catalog of all extracted pages

**Follow Core Workflow steps 3-7** for extraction, organization, planning, implementation, and verification.

### Phase 4: Profiles and Workspace Markdown

**Reference:** [Phase 4 Profiles Log](./docs/phase4-profiles-log.md) — profile creation and clone verification

**Follow Core Workflow steps 1-7** for profile research, creation, verification, and debugging.

### Phase 5: Docs Inventory

**Follow Core Workflow steps 1-7** for inventory inspection, plugin/hook/skill verification, and debugging.

### Phase 6: Configuration Hierarchy Audit

**Follow Core Workflow steps 1-7** for hierarchy listing, validation, enhancement, and auditing.

## Skills

- `hermes-skills` — Browse, search, install, audit skills (used in Phase 1)
- `hermes-mcp` — MCP server catalog, install, configure (used in Phase 2)
- `web-search` / `web-extract` — Research and content extraction (Phases 2-3)
- `delegate-task` — Subagent delegation for parallel research (all phases)

## Subagents

> Research Analyst — Specialized profile for dependency scanning, batch analysis, and synthesis across Phases 1-3.
> Code Architect — Specialized profile for fix planning, batched application, and verification.
> Exec Assistant — Orchestration profile for readiness checks and fix execution.

## Personas

> **Research Analyst** — Systematic, thorough, cites sources, produces structured catalogs.
> **Code Architect** — Pragmatic senior engineer, prefers simple systems, pushes back on bad ideas.
> **Exec Assistant** — Organized, tracks progress, ensures verification gates pass.

## Output Requirements

| Requirement               | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| Preserve research targets | Keep the current research targets unless explicitly changed  |
| Template variables only   | Change only template variables, not the workflow             |
| Markdown output           | Use Markdown for extracted docs, indexes, and notes          |
| Strict sequence           | plan → research → extract → plan update → implement → verify |
| Report blockers           | Clearly report if any native capability is unavailable       |

## Verification Gates

| Gate | Description                                                  |
| ---- | ------------------------------------------------------------ |
| 1    | Research targets executed in order                           |
| 2    | Extracted pages written to Markdown files                    |
| 3    | Docs index lists the new files                               |
| 4    | Plan updated from research output                            |
| 5    | Implementation starts only after plan is current             |
| 6    | Verification runs before completion                          |
| 7    | Nearest safe equivalent used for missing native capabilities |

## Actions

- `hermes profile create <name> --clone-all` — Create fully-cloned profiles
- `hermes skills audit && hermes skills update` — Validate skill library health
- `hermes mcp install <server>` — Install additional MCP servers
- `web-search` / `web-extract` — Research and content extraction
- `delegate-task` — Parallel subagent delegation
- `patch` / `write_file` — Targeted file modifications
