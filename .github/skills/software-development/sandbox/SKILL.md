---
author: Hermes Agent
description: Use when experimenting, prototyping, and running throwaway agent workflows
  in a safe isolated environment.
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: sandbox
tags:
- sandbox
- experimentation
- prototyping
- isolated-environment
title: Sandbox
version: 1.1.0

---
# Sandbox

## Overview

Provide a safe experimentation environment for agent workflows, configuration changes, and prototyping. The sandbox pattern isolates experimental code from production systems.

## When to Use

- Experimenting with new libraries, patterns, or architectures
- Prototyping agent workflows or configurations
- Running throwaway code that should not affect production
- Testing OpenCode/agent configuration changes
- Developing and testing new prompt files

## When NOT TO USE

- Production code changes
- Work that needs to be committed to the main branch
- Long-term feature development (use proper branching instead)

## Skills Required

| Skill | Purpose |
|-------|---------|
| `spike` | Time-boxed experiments |
| `test-driven-development` | Validate experimental code |

## Workflow

### Phase 1: Setup Sandbox

1. Create an isolated directory:
   ```bash
   mkdir -p sandbox/experiment-name
   cd sandbox/experiment-name
   git init  # optional: track experimental changes
   ```

2. Ensure the sandbox is in `.gitignore`:
   ```bash
   grep -q "sandbox/" .gitignore || echo "sandbox/" >> .gitignore
   ```

### Phase 2: Execute Experiment

1. Make changes freely within the sandbox
2. Test ideas without worrying about breaking production
3. Document findings as you go

### Phase 3: Validate Results

1. Verify the experiment achieved its goal
2. Document what worked and what didn't
3. Identify any patterns worth integrating into production

### Phase 4: Integrate or Cleanup

**If successful:**
1. Move validated code to the proper production location
2. Add proper tests and documentation
3. Remove the sandbox version

**If unsuccessful:**
1. Document lessons learned
2. Delete the sandbox directory
3. No production impact

## Verification Checklist

- [ ] Sandbox directory created and isolated
- [ ] Sandbox is in .gitignore (not committed)
- [ ] Experiment completed and documented
- [ ] Results validated
- [ ] Production code updated (if successful) or sandbox cleaned up (if not)

## Pitfalls

- **Sandbox creep:** Don't let experimental code become production code without proper review
- **Forgetting to clean up:** Delete sandboxes after experiments complete
- **Not documenting findings:** Always record what you learned, even from failed experiments
- **Sharing state between sandbox and production:** Keep them completely isolated

### Directory Architecture

```
SandBox/
├── .opencode/              # Agentic/OpenCode configuration (distributed via agentic pull)
│   ├── agents/             # 18 subagent definitions (codebase-locator, opencoder, etc.)
│   ├── commands/           # 22 slash commands (/ticket, /research, /plan, /execute, etc.)
│   ├── rules/              # 22 rule files + rules-catalog.md meta-doc
│   ├── skills/             # 63 specialized skills
│   ├── plugins/            # 17 active plugins + plugins-archive/
│   ├── projects/           # 26 project YAML configs
│   ├── hooks/              # Session-start hooks
│   ├── config/             # error-handling-workflow.md, path-constants, directory-structure-standards
│   └── opencode.json       # Main OpenCode config (MCP servers, model, plugins)
├── Prompts/                # 10 structured prompt .md files
├── scripts/                # 5-phase Rhixe audit system
├── rhixecompany/           # Multiple repos: Banking, ecom, profile, etc.
├── Rhixe-company/          # Additional repos: comicwise, cookiecutter-django-tailwind, etc.
├── Resume_maker/           # TypeScript resume generator
├── Bash/                   # Cache cleanup and upgrade scripts
├── docs/                   # Audit reports, plans, specs, context docs
├── thoughts/               # Knowledge base with continuity ledgers
└── .superpowers/           # Superpowers skill reference
```

### Agent Frontmatter Pattern

All agents in `.opencode/agents/` use YAML frontmatter with:
- `mode: subagent | primary` — execution mode
- `model:` — model override (default: `opencode/qwen3.6-plus-free`)
- `temperature:` — typically 0.1 for deterministic behavior
- `permission:` block with per-tool allow/deny/ask per path glob
- Read-only agents (locator, analyzer) deny write/edit/bash
- OpenCoder has granular bash rules: `rm -rf *` → ask, `sudo *` → deny, env files → deny

### Command Frontmatter Pattern

Commands in `.opencode/commands/` use:
- `trigger: /commandname` — slash command trigger
- `description:` — command purpose
- `$ARGUMENTS` placeholder at end of file for user input

### Rule Files

All `.opencode/rules/*.md` files have:
- `description:`, `applyTo:`, `priority:`, `category:`, `tags:`
- `canonicalSource: AGENTS.md` — points to AGENTS.md as source
- `date:` and `lastReviewed:` for maintenance tracking

### OpenCoder 6-Stage Workflow

1. **Discover** — Read-only, load context files via ContextScout
2. **Propose** — Present summary to user for approval
3. **InitSession** — Create session dir, persist context
4. **Plan** — Break into subtasks via TaskManager
5. **Execute** — Parallel batches (1-4 tasks → CoderAgent direct, 5+ → BatchExecutor)
6. **ValidateAndHandoff** — Integration testing, handoff

Critical rules: NEVER write without context first, NEVER skip approval gate, NEVER auto-fix errors, ALWAYS validate after each step.

### 5-Phase Audit System

Located in `scripts/`, runs sequentially:
1. **Deep Triage** — Diagnostics on CRITICAL+HIGH repos
2. **Light Inventory** — Quick snapshot of MEDIUM+LOW repos
3. **Consolidation** — Merge findings, propose fixes, group batches
4. **Batch Execution** — Apply fixes with verification, max 7 files/batch
5. **Final Summary** — Generate executive report

Master script: `bash ./scripts/run-audit.sh`

### Plugin System

17 active plugins in `.opencode/plugins/`, 40+ archived in `plugins-archive/`.
Key plugins: superpowers, octto, planning-toolkit, subtask2, cost-guard, rate-limit.
Plugin format: YAML files in `.opencode/plugins/` or npm packages.

### OpenCode Config

- Model: `opencode/qwen3.6-plus-free`
- MCP servers: context7, exa, filesystem, gh_grep, MCP_DOCKER, memory, next-devtools, playwright, sequential-thinking
- 22 rule files loaded via `instructions` array
- Plugins loaded via `plugin` array (file paths and npm packages)
- `share: disabled` — no session sharing

### Prompts Folder Structure

`Prompts/` contains 10 structured `.md` prompt files, each following a consistent 9-section format:
1. **Metadata** — target, context docs, plan namespace
2. **Skills** — skill slugs with descriptions
3. **Subagents / Personas** — table: role → responsibility
4. **Rules** — numbered constraints
5. **Phases** — numbered phases with Tasks + Step tables
6. **Context Documents** — reference tables
7. **Reference** — frontmatter specs, fix patterns
8. **Subtasks Checklist** — todo items
9. **Actions Summary** — ordered flat action list

Files: agentsfixprompts.md, commandsfixprompts.md, rulesfixprompts.md, skillsfixprompts.md, generalprompts.md, pluginsfixprompts.md, repoprompts.md, reusableprompts.md, bashscriptsfixprompts.md, updateopencodeconfigsprompts.md

### Skill Frontmatter Pattern

All `.opencode/skills/*/SKILL.md` files use only `name:` + `description:` in frontmatter:

```yaml
---
name: skill-name
description: Use when [specific trigger condition — one sentence].
---
```

- No `tools:` array — None of the 63 skill files have or need a tools frontmatter field
- Description must be a single sentence stating when to invoke the skill
- Skills in `.opencode/skills/` are separate from superpowers skills in `.opencode/plugin-src/superpowers/skills/`

## When to Use

- Experimenting with new libraries, patterns, or architectures
- Prototyping agent workflows or configurations
- Running throwaway code that should not affect production
- Testing OpenCode/agent configuration changes
- Developing and testing new prompt files

## Overview

Sandbox skill providing a safe experimentation environment for agent workflows, configuration changes, and prototyping. Documents the full SandBox project structure including OpenCode configuration, agent definitions, command systems, audit tools, and prompt engineering conventions.

## Verification Checklist

- [ ] Changes are isolated to sandbox directories and do not affect production
- [ ] Any new patterns or configurations are documented
- [ ] Experimental code is cleaned up or properly integrated after validation
- [ ] Directory structure changes are reflected in this document
- [ ] Agent and command configurations follow documented frontmatter patterns

