---
toolsets:
  - edit
  - search
  - runCommands
  - runTasks
  - changes
  - testFailure
  - openSimpleBrowser
  - fetch
  - githubRepo
  - todos
license: MIT
author: Hermes Agent
version: 1.0.0
title: Suggest Awesome GitHub Copilot Custom Agents
name: suggest-awesome-github-copilot-agents
description: "Find GitHub Copilot custom agent files that add coverage the repo lacks and flag local duplicates or outdated copies."
tags:
  - agents
  - ai-assistant
  - git
  - ml
  - prompts
  - specification
  - typescript
  - agents
  - ai-assistant
  - ci-cd
  - documentation
  - github
  - planning
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - suggest-awesome-github-copilot-agents.prompt

trigger: suggest-awesome-github-copilot-agents

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - suggest-awesome-github-copilot-agents.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - suggest-awesome-github-copilot-agents.prompt

## Goal

Suggest GitHub Copilot custom agent files that add coverage the repo lacks, and flag local duplicates or outdated copies.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules
> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)


- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Process

> 1. **Fetch Available Custom Agents**: Extract Custom Agents list and description
> 2. **Scan Local Custom Agents**: Discover existing custom agent files in `.githu

> **Full content:** `templates/suggest-awesome-github-copilot-agents/local_agent_discovery_pro.md`

## Context Analysis Criteria

🔍 **Repository Patterns**:

- Programming languages used (.cs, .js, .py, etc.)
- Framework indicators (ASP.NET, React, Azure, etc.)
- Project types (web apps, APIs, libraries, tools)
- Documentation needs (README, specs, ADRs)

🗨️ **Chat History Context**:

- Recent discussions and pain points
- Feature requests or implementation needs
- Code review patterns
- Development workflow requirements

## Output Format

Display analysis results in structured table comparing awesome-copilot custom agents with existing repository custom agents:

| Awesome-Copilot Custom Agent | Description | Already Installed | Similar Local Custom Agent | Suggestion Rationale |
| --- | --- | --- | --- | --- |
| [amplitude-experiment-implementation.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/amplitude-experiment-implementation.agent.md) | This custom agent uses Amplitude's MCP tools to deploy new experiments inside of Amplitude, enabling seamless variant testing capabilities and rollout of product features | ❌ No | None | Would enhance experimentation capabilities within the product |
| [launchdarkly-flag-cleanup.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/launchdarkly-flag-cleanup.agent.md) | Feature flag cleanup agent for LaunchDarkly | ✅ Yes | launchdarkly-flag-cleanup.agent.md | Already covered by existing LaunchDarkly custom agents |
| [principal-software-engineer.agent.md](https://github.com/github/awesome-copilot/blob/main/agents/principal-software-engineer.agent.md) | Provide principal-level software engineering guidance with focus on engineering excellence, technical leadership, and pragmatic implementation. | ⚠️ Outdated | principal-software-engineer.agent.md | Tools configuration differs: remote uses `'web/fetch'` vs local `'fetch'` - Update recommended |

## Local Agent Discovery Process

1. List all `*.agent.md` files in `.github/agents/` directory
2. For each discovered file, read front matter to extract `description`
3. Build comprehensive inventory of existing agents
4. Use this inventory to avoid suggesting duplicates

## Version Comparison Process

1. For each local agent file, construct the raw GitHub URL to fetch the remote version:
   - Pattern: `https://raw.githubusercontent.com/github/awesome-copilot/main/agents/<filename>`
2. Fetch the remote version using the `fetch` tool
3. Compare entire file content (including front matter, tools array, and body)
4. Identify specific differences:
   - **Front matter changes** (description, tools)
   - **Tools array modifications** (added, removed, or renamed tools)
   - **Content updates** (instructions, examples, guidelines)
5. Document key differences for outdated agents
6. Calculate similarity to determine if update is needed

## Requirements

- Use `githubRepo` tool to get content from awesome-copilot repository agents folder
- Scan local file system for existing agents in `.github/agents/` directory
- Read YAML front matter from local agent files to extract descriptions
- Compare local agents with remote versions to detect outdated agents
- Compare against existing agents in this repository to avoid duplicates
- Focus on gaps in current agent library coverage
- Validate that suggested agents align with repository's purpose and standards
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot agents and similar local agents
- Clearly identify outdated agents with specific differences noted
- Don't provide any additional information or context beyond the table and the analysis

## Icons Reference

- ✅ Already installed and up-to-date
- ⚠️ Installed but outdated (update available)
- ❌ Not installed in repo

## Update Handling

When outdated agents are identified:

1. Include them in the output table with ⚠️ status
2. Document specific differences in the "Suggestion Rationale" column
3. Provide recommendation to update with key changes noted
4. When user requests update, replace entire local file with remote version
5. Preserve file location in `.github/agents/` directory


## Template References

Detailed templates in `templates/suggest-awesome-github-copilot-agents/`:


## Template References

Templates in `templates/suggest-awesome-github-copilot-agents/`:
- `context_analysis_criteria.md`
- `icons_reference.md`
- `inputs.md`
- `local_agent_discovery_pro.md`
- `output_format.md`
- `phases.md`
- `process.md`
- `requirements.md`
- `rules.md`
- `update_handling.md`
- `version_comparison_proces.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
