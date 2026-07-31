---

name: multi-agent-research-template

title: Multi-Agent Research and Implementation Template

description: 'Reusable prompt for Codex, Copilot, and Hermes. It preserves the current research targets while factoring out the shared workflow.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

  - web

scripts: []

skills: []

formatter: default

plan: None

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

trigger: /multi-agent-research-template

metadata:

  hermes: None

  related_skills:

    - codex

    - copilot

    - hermes

    - research

    - planning

    - automation

dependencies: []

---

## Goal

Reusable prompt for Codex, Copilot, and Hermes. It preserves the current research targets while factoring out the shared workflow.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill | Purpose |
| ------- | --------- |
| codex | Codex agent execution |
| copilot | Copilot agent execution |
| hermes | Hermes agent execution |
| research | Research workflow |
| planning | Planning workflow |
| automation | Automation workflow |# PurposeThis prompt is a reusable template for Codex, Copilot, and Hermes.Keep the default research targets below unless the user replaces them.When a target depends on native agent syntax, use the active agent'sequivalent command style and preserve the order of operations.

## Template Variables

<!-- Template variables use Jinja2-style {{var}} syntax --

> | Variable | Value || ---------- | ------- || `{{workspace_root}}` | `` `$HOME/Desktop/SandBox` `` (resolves to `C:\Users\Alexa\Desktop\SandBox`) || `{{docs_root}}` | `` `docs/` `` || `{{agent_name}}` | `Codex` \| `Copilot` \| `Hermes` || `{{native_plan}}` | the active agent's planning or update command || `{{native_search}}` | the active agent's search command || `{{native_extract}}` | the active agent's content extraction command || `{{native_files}}` | the active agent's file read/write command |

## Agent Mapping

| Agent | Approach | Notes || ------

- | ---------- | ------- || Codex | Use terminal commands and workspace-local file edits. | || Copilot | Use the equivalent Copilot workflow tools available in the current environment. | || Hermes | Use Hermes CLI commands exactly as written in the target steps. | || Fallback | If a capability is missing, choose the closest safe equivalent and note the substitution before continuing. | |

## Shared Rules

> These are guiding principles, not actionable tasks.- [ ] If a plan already exists, update it before starting anything else.- [ ] Research first, then extract, then write docs, then plan, then implement, then verify.- [ ] Preserve the current research targets unless the user explicitly changes them.- [ ] Keep each stage reversible and easy to resume.- [ ] Write extracted findings to Markdown under `docs/` with a clear index.- [ ] Do not mark work complete until the relevant verification checks pass.- [ ] If a step depends on a native agent command, use the active agent's equivalent instead of forcing one syntax across all agents.- [ ] Keep the prompt reusable: replace only the template variables, not the workflow.

## Core Workflow

The 7-step workflow is executed across the 6 phases below:1. **Update plan** — Phase 1 begins with `/plan` if a plan exists2. **Execute targets** — Phases 1–6 run the research target sets sequentially3. **Extract to Markdown** — Phases 2–3 "For this Phase" steps handle extraction4. **Organize & index** — Phases 2–3 create docs/ subfolders and index catalogs5. **Synthesize plan** — Phases 2–3 "For this Phase" step: read files, update plan6. **Implement** — Phases 2–3 "For this Phase" step: implement after plan is ready7. **Verify** — Verification Gates (below) and Phase "For this Phase" verification steps---

## Default Research Targets

## Phase 1: Skills Discovery and Audit

- [ ] Start with `/plan` if a plan already exists; update it.- [ ] Execute Hermes skills browse to list everything available.- [ ] Search and filter the top 50 best skills that are not already installed or available.- [ ] Execute Hermes skills search with the skill name to find skills by keyword.- [ ] Install all matching skills after a security scan.- [ ] Run `/skills audit`.- [ ] Run `/systematic-debugging` to debug and fix all issues.

## Phase 2: MCP Server and Tool Research

> Make comprehensive research for install, test, and verify steps for these MCP>
>
> - sequential-thinking
> **Full content:**

## Phase 3: Hermes Docs and Ecosystem

Research these sources and extract each page into Markdown:

- [awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent)- [Skills Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/skills)- [MCP Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp)- [Use MCP with Hermes Guide](https://hermes-agent.nousresearch.com/docs/guides/use-mcp-with-hermes)- [Personality Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/personality)- [Context Files Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files)- [Quickstart Guide](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)- [Tips and Workflow Guidance](https://hermes-agent.nousresearch.com/docs/guides/tips)- [Tools Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/tools)- [Learning Path Guide](https://hermes-agent.nousresearch.com/docs/getting-started/learning-path)- [Hooks Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks)- [Plugins Feature Documentation](https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins)For this Phase:- [ ] Save a Markdown file for each page.- [ ] Format each file with clean, readable Markdown.- [ ] Create an index catalog in the current directory.- [ ] Organize the output into `docs/` subfolders using proper names.- [ ] Read the newly created Markdown files.- [ ] Update the plan from those findings.- [ ] Implement only after the plan is ready.- [ ] Verify that the pages were extracted and cataloged.

## Phase 4: Profiles and Workspace Markdown

- [ ] Research all Markdown files in `docs/*`.- [ ] Identify all available profiles.- [ ] Create profiles with `hermes profile create {profile name} --clone-all`.- [ ] Confirm the clones copy config, keys, `SOUL.md`, memories, skills, and sessions.- [ ] Install, verify, test, debug, and fix issues in each profile.

## Phase 5: Docs Inventory

- [ ] Inspect `docs/*` for hooks, skills, and plugins.- [ ] Install the plugins first.- [ ] Verify, test, debug, and fix issues in the plugins.- [ ] Then verify, test, debug, and fix issues in the hooks.- [ ] Then verify, test, debug, and fix issues in the skills.

## Phase 6: Configuration Hierarchy Audit

- [ ] List all hooks, tools, skills, and plugins.- [ ] List all MCP servers, hooks, tools, skills, and plugins.- [ ] List all plugin hooks, tools, and skills.- [ ] Create missing items when needed.- [ ] Verify and enhance existing items when they are already present.- [ ] Validate the configuration hierarchy in this order:  `.hermes.md` -

> `AGENTS.md` -
> `CLAUDE.md` -
> `.cursorrules`

## Output Requirements

| # | Requirement | Description || --

- | ------------- | ------------- || 1 | Preserve targets | Preserve the current research targets. || 2 | Reusable workflow | Keep the workflow reusable by changing only the template variables. || 3 | Markdown output | Use Markdown for extracted docs, indexes, and notes. || 4 | Strict sequence | Keep the sequence strict: plan → research → extract → plan update → implement → verify. || 5 | Report blockers | Report blockers clearly if any native capability is unavailable. |

## Verification Gates

| # | Gate | Criteria || --

- | ------ | ---------- || 1 | Target order | The research targets must be executed in order. || 2 | Markdown output | The extracted pages must be written to Markdown files. || 3 | Docs index | The docs index must list the new files. || 4 | Plan current | The plan must be updated from the research output. || 5 | Plan before implement | Implementation must not start until the plan is current. || 6 | Verify before complete | Verification must run before completion. || 7 | Native fallback | If the active agent cannot perform a step directly, the prompt must instruct it to use the nearest safe equivalent. |---

## Verification Checklist

- [ ] Frontmatter has all required fields (`name`, `title`, `description`, `trigger`, `tags`)
- [ ] Frontmatter has recommended fields (`version`, `author`, `license`, `metadata.hermes.related_skills`)
- [ ] `Skills Required` table is present and populated
- [ ] Phase headings use H2 (`

## Phase N:`) not H3

- [ ] All phase task lists use `- [ ]` checkbox format- [ ] Phase 3 URLs are markdown links with descriptive titles- [ ] Phase 2 "After research" uses Steps/Tasks structure- [ ] Agent Mapping, Output Requirements, Verification Gates are markdown tables- [ ] Core Workflow references phases (no duplicate detail)- [ ] Template variables table uses inline code for paths- [ ] No `mode` field in frontmatter- [ ] Trigger matches filename stem convention- [ ] File uses `.prompt.md` extension ✅ (renamed from `.txt`)

## Template References

Detailed templates in `templates/multi-agent-research-template/`:- `phase_2_mcp_server_and_tool_re.md`

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

## Verification Checklist

| # | Gate | Criterion |
| --- | ------ | ----------- |
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

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
