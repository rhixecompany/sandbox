---
name: multi-agent-research-template
title: Multi-Agent Research and Implementation Template
description: Reusable prompt for Codex, Copilot, and Hermes. It preserves the current research targets while factoring out the shared workflow.
tags:
  - agents
  - ai-assistant
  - frontend
  - ml
  - planning
  - prompts
  - skills
  - typescript
  - workflow
  - codex
  - copilot
  - hermes
  - research
  - planning
  - automation
trigger: /multi-agent-research
version: "1.0.0"
author: "Hermes Agent"
license: "MIT"
metadata:
  hermes:
    related_skills: [codex, copilot, hermes, research, planning, automation]
---

## Skills Required

> See full table with per-domain purposes:
> [`prompts/templates/_shared/skills-table-core.md`](../templates/_shared/skills-table-core.md#multi-agent-research-template)

| Skill | Purpose |
|-------|---------|
| codex | Codex agent execution |
| copilot | Copilot agent execution |
| hermes | Hermes agent execution |
| research | Research workflow |
| planning | Planning workflow |
| automation | Automation workflow |

# Purpose

This prompt is a reusable template for Codex, Copilot, and Hermes.
Keep the default research targets below unless the user replaces them.
When a target depends on native agent syntax, use the active agent's
equivalent command style and preserve the order of operations.

## Template Variables

<!-- Template variables use Jinja2-style {{var}} syntax -->

| Variable | Value |
|----------|-------|
| `{{workspace_root}}` | `` `$HOME/Desktop/SandBox` `` (resolves to `C:\Users\Alexa\Desktop\SandBox`) |
| `{{docs_root}}` | `` `docs/` `` |
| `{{agent_name}}` | `Codex` \| `Copilot` \| `Hermes` |
| `{{native_plan}}` | the active agent's planning or update command |
| `{{native_search}}` | the active agent's search command |
| `{{native_extract}}` | the active agent's content extraction command |
| `{{native_files}}` | the active agent's file read/write command |

## Agent Mapping

| Agent | Approach | Notes |
|-------|----------|-------|
| Codex | Use terminal commands and workspace-local file edits. | |
| Copilot | Use the equivalent Copilot workflow tools available in the current environment. | |
| Hermes | Use Hermes CLI commands exactly as written in the target steps. | |
| Fallback | If a capability is missing, choose the closest safe equivalent and note the substitution before continuing. | |

## Shared Rules

> These are guiding principles, not actionable tasks.

- [ ] If a plan already exists, update it before starting anything else.
- [ ] Research first, then extract, then write docs, then plan, then implement, then verify.
- [ ] Preserve the current research targets unless the user explicitly changes them.
- [ ] Keep each stage reversible and easy to resume.
- [ ] Write extracted findings to Markdown under `docs/` with a clear index.
- [ ] Do not mark work complete until the relevant verification checks pass.
- [ ] If a step depends on a native agent command, use the active agent's equivalent instead of forcing one syntax across all agents.
- [ ] Keep the prompt reusable: replace only the template variables, not the workflow.

## Core Workflow

The 7-step workflow is executed across the 6 phases below:

1. **Update plan** — Phase 1 begins with `/plan` if a plan exists
2. **Execute targets** — Phases 1–6 run the research target sets sequentially
3. **Extract to Markdown** — Phases 2–3 "For this Phase" steps handle extraction
4. **Organize & index** — Phases 2–3 create docs/ subfolders and index catalogs
5. **Synthesize plan** — Phases 2–3 "For this Phase" step: read files, update plan
6. **Implement** — Phases 2–3 "For this Phase" step: implement after plan is ready
7. **Verify** — Verification Gates (below) and Phase "For this Phase" verification steps

---

## Default Research Targets

## Phase 1: Skills Discovery and Audit

- [ ] Start with `/plan` if a plan already exists; update it.
- [ ] Execute Hermes skills browse to list everything available.
- [ ] Search and filter the top 50 best skills that are not already installed or available.
- [ ] Execute Hermes skills search with the skill name to find skills by keyword.
- [ ] Install all matching skills after a security scan.
- [ ] Run `/skills audit`.
- [ ] Run `/systematic-debugging` to debug and fix all issues.

## Phase 2: MCP Server and Tool Research

> Make comprehensive research for install, test, and verify steps for these MCP
> - sequential-thinking

> **Full content:** `templates/multi-agent-research-template/phase_2_mcp_server_and_tool_re.md`

## Phase 3: Hermes Docs and Ecosystem

Research these sources and extract each page into Markdown:

- [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)
- [Skills Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)
- [MCP Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)
- [Use MCP with Hermes Guide](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)
- [Personality Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)
- [Context Files Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)
- [Quickstart Guide](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [Tips and Workflow Guidance](https://hermes-agent.nousresearch.com/docs/guides/tips)
- [Tools Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)
- [Learning Path Guide](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)
- [Hooks Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)
- [Plugins Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)

For this Phase:

- [ ] Save a Markdown file for each page.
- [ ] Format each file with clean, readable Markdown.
- [ ] Create an index catalog in the current directory.
- [ ] Organize the output into `docs/` subfolders using proper names.
- [ ] Read the newly created Markdown files.
- [ ] Update the plan from those findings.
- [ ] Implement only after the plan is ready.
- [ ] Verify that the pages were extracted and cataloged.

## Phase 4: Profiles and Workspace Markdown

- [ ] Research all Markdown files in `docs/*`.
- [ ] Identify all available profiles.
- [ ] Create profiles with `hermes profile create {profile name} --clone-all`.
- [ ] Confirm the clones copy config, keys, `SOUL.md`, memories, skills, and sessions.
- [ ] Install, verify, test, debug, and fix issues in each profile.

## Phase 5: Docs Inventory

- [ ] Inspect `docs/*` for hooks, skills, and plugins.
- [ ] Install the plugins first.
- [ ] Verify, test, debug, and fix issues in the plugins.
- [ ] Then verify, test, debug, and fix issues in the hooks.
- [ ] Then verify, test, debug, and fix issues in the skills.

## Phase 6: Configuration Hierarchy Audit

- [ ] List all hooks, tools, skills, and plugins.
- [ ] List all MCP servers, hooks, tools, skills, and plugins.
- [ ] List all plugin hooks, tools, and skills.
- [ ] Create missing items when needed.
- [ ] Verify and enhance existing items when they are already present.
- [ ] Validate the configuration hierarchy in this order:
  `.hermes.md` -> `AGENTS.md` -> `CLAUDE.md` -> `.cursorrules`

## Output Requirements

| # | Requirement | Description |
|---|-------------|-------------|
| 1 | Preserve targets | Preserve the current research targets. |
| 2 | Reusable workflow | Keep the workflow reusable by changing only the template variables. |
| 3 | Markdown output | Use Markdown for extracted docs, indexes, and notes. |
| 4 | Strict sequence | Keep the sequence strict: plan → research → extract → plan update → implement → verify. |
| 5 | Report blockers | Report blockers clearly if any native capability is unavailable. |

## Verification Gates

| # | Gate | Criteria |
|---|------|----------|
| 1 | Target order | The research targets must be executed in order. |
| 2 | Markdown output | The extracted pages must be written to Markdown files. |
| 3 | Docs index | The docs index must list the new files. |
| 4 | Plan current | The plan must be updated from the research output. |
| 5 | Plan before implement | Implementation must not start until the plan is current. |
| 6 | Verify before complete | Verification must run before completion. |
| 7 | Native fallback | If the active agent cannot perform a step directly, the prompt must instruct it to use the nearest safe equivalent. |

---

## Verification Checklist

- [ ] Frontmatter has all required fields (`name`, `title`, `description`, `trigger`, `tags`)
- [ ] Frontmatter has recommended fields (`version`, `author`, `license`, `metadata.hermes.related_skills`)
- [ ] `Skills Required` table is present and populated
- [ ] Phase headings use H2 (`## Phase N:`) not H3
- [ ] All phase task lists use `- [ ]` checkbox format
- [ ] Phase 3 URLs are markdown links with descriptive titles
- [ ] Phase 2 "After research" uses Steps/Tasks structure
- [ ] Agent Mapping, Output Requirements, Verification Gates are markdown tables
- [ ] Core Workflow references phases (no duplicate detail)
- [ ] Template variables table uses inline code for paths
- [ ] No `mode` field in frontmatter
- [ ] Trigger matches filename stem convention
- [ ] File uses `.prompt.md` extension ✅ (renamed from `.txt`)


## Template References

Detailed templates in `templates/multi-agent-research-template/`:
- `phase_2_mcp_server_and_tool_re.md`
