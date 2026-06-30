---
toolsets:
  - edit
  - search
  - runCommands
  - runTasks
  - think
  - changes
  - testFailure
  - openSimpleBrowser
  - web/fetch
  - githubRepo
  - todos
  - search
license: MIT
author: Hermes Agent
version: 1.0.0
title: Suggest Awesome GitHub Copilot Prompts
name: suggest-awesome-github-copilot-prompts
description: "Find GitHub Copilot prompt files that add coverage the repo lacks and flag local duplicates or outdated copies."
tags:
  - ai-assistant
  - git
  - ml
  - prompts
  - specification
  - typescript
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
    - suggest-awesome-github-copilot-prompts.prompt

trigger: suggest-awesome-github-copilot-prompts

---
metadata:
  hermes:
    related_skills: []
    tags:
    - suggest-awesome-github-copilot-prompts.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - suggest-awesome-github-copilot-prompts.prompt

## Goal

Suggest GitHub Copilot prompt files that add coverage the repo lacks, and flag local duplicates or outdated copies.

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

> 1. **Fetch Available Prompts**: Extract prompt list and descriptions from [aweso
> 2. **Scan Local Prompts**: Discover existing prompt files in `.github/prompts/` 

> **Full content:** `templates/suggest-awesome-github-copilot-prompts/process.md`

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

Display analysis results in structured table comparing awesome-copilot prompts with existing repository prompts:

| Awesome-Copilot Prompt | Description | Already Installed | Similar Local Prompt | Suggestion Rationale |
| --- | --- | --- | --- | --- |
| [code-review.prompt.md](https://github.com/github/awesome-copilot/blob/main/prompts/code-review.prompt.md) | Automated code review prompts | ❌ No | None | Would enhance development workflow with standardized code review processes |
| [documentation.prompt.md](https://github.com/github/awesome-copilot/blob/main/prompts/documentation.prompt.md) | Generate project documentation | ✅ Yes | create_oo_component_documentation.prompt.md | Already covered by existing documentation prompts |
| [debugging.prompt.md](https://github.com/github/awesome-copilot/blob/main/prompts/debugging.prompt.md) | Debug assistance prompts | ⚠️ Outdated | debugging.prompt.md | Tools configuration differs: remote uses `'codebase'` vs local missing - Update recommended |

## Local Prompts Discovery Process

1. List all `*.prompt.md` files in `.github/prompts/` directory
2. For each discovered file, read front matter to extract `description`
3. Build comprehensive inventory of existing prompts
4. Use this inventory to avoid suggesting duplicates

## Version Comparison Process

1. For each local prompt file, construct the raw GitHub URL to fetch the remote version:
   - Pattern: `https://raw.githubusercontent.com/github/awesome-copilot/main/prompts/<filename>`
2. Fetch the remote version using the `#fetch` tool
3. Compare entire file content (including front matter and body)
4. Identify specific differences:
   - **Front matter changes** (description, tools, mode)
   - **Tools array modifications** (added, removed, or renamed tools)
   - **Content updates** (instructions, examples, guidelines)
5. Document key differences for outdated prompts
6. Calculate similarity to determine if update is needed

## Requirements

- Use `githubRepo` tool to get content from awesome-copilot repository prompts folder
- Scan local file system for existing prompts in `.github/prompts/` directory
- Read YAML front matter from local prompt files to extract descriptions
- Compare local prompts with remote versions to detect outdated prompts
- Compare against existing prompts in this repository to avoid duplicates
- Focus on gaps in current prompt library coverage
- Validate that suggested prompts align with repository's purpose and standards
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot prompts and similar local prompts
- Clearly identify outdated prompts with specific differences noted
- Don't provide any additional information or context beyond the table and the analysis

## Icons Reference

- ✅ Already installed and up-to-date
- ⚠️ Installed but outdated (update available)
- ❌ Not installed in repo

## Update Handling

When outdated prompts are identified:

1. Include them in the output table with ⚠️ status
2. Document specific differences in the "Suggestion Rationale" column
3. Provide recommendation to update with key changes noted
4. When user requests update, replace entire local file with remote version
5. Preserve file location in `.github/prompts/` directory


## Template References

Detailed templates in `templates/suggest-awesome-github-copilot-prompts/`:


## Template References

Templates in `templates/suggest-awesome-github-copilot-prompts/`:
- `context_analysis_criteria.md`
- `icons_reference.md`
- `inputs.md`
- `local_prompts_discovery_p.md`
- `output_format.md`
- `phases.md`
- `process.md`
- `requirements.md`
- `rules.md`
- `update_handling.md`
- `version_comparison_proces.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
