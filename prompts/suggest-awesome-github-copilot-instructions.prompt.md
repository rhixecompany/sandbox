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
title: Suggest Awesome GitHub Copilot Instructions
name: suggest-awesome-github-copilot-instructions
description: "Find GitHub Copilot instruction files that add coverage the repo lacks and flag local duplicates or outdated copies."
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
    - suggest-awesome-github-copilot-instructions.prompt

trigger: suggest-awesome-github-copilot-instructions

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - suggest-awesome-github-copilot-instructions.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - suggest-awesome-github-copilot-instructions.prompt

## Goal

Suggest GitHub Copilot instruction files that add coverage the repo lacks, and flag local duplicates or outdated copies.

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

> 1. **Fetch Available Instructions**: Extract instruction list and descriptions f
> 2. **Scan Local Instructions**: Discover existing instruction files in `.github/

> **Full content:** `templates/suggest-awesome-github-copilot-instructions/process.md`

## Context Analysis Criteria

🔍 **Repository Patterns**:

- Programming languages used (.cs, .js, .py, .ts, etc.)
- Framework indicators (ASP.NET, React, Azure, Next.js, etc.)
- Project types (web apps, APIs, libraries, tools)
- Development workflow requirements (testing, CI/CD, deployment)

🗨️ **Chat History Context**:

- Recent discussions and pain points
- Technology-specific questions
- Coding standards discussions
- Development workflow requirements

## Output Format

Display analysis results in structured table comparing awesome-copilot instructions with existing repository instructions:

| Awesome-Copilot Instruction | Description | Already Installed | Similar Local Instruction | Suggestion Rationale |
| --- | --- | --- | --- | --- |
| [blazor.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/blazor.instructions.md) | Blazor development guidelines | ✅ Yes | blazor.instructions.md | Already covered by existing Blazor instructions |
| [reactjs.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/reactjs.instructions.md) | ReactJS development standards | ❌ No | None | Would enhance React development with established patterns |
| [java.instructions.md](https://github.com/github/awesome-copilot/blob/main/instructions/java.instructions.md) | Java development best practices | ⚠️ Outdated | java.instructions.md | applyTo pattern differs: remote uses `'**/*.java'` vs local `'*.java'` - Update recommended |

## Local Instructions Discovery Process

1. List all `*.instructions.md` files in the `instructions/` directory
2. For each discovered file, read front matter to extract `description` and `applyTo` patterns
3. Build comprehensive inventory of existing instructions with their applicable file patterns
4. Use this inventory to avoid suggesting duplicates

## Version Comparison Process

1. For each local instruction file, construct the raw GitHub URL to fetch the remote version:
   - Pattern: `https://raw.githubusercontent.com/github/awesome-copilot/main/instructions/<filename>`
2. Fetch the remote version using the `#fetch` tool
3. Compare entire file content (including front matter and body)
4. Identify specific differences:
   - **Front matter changes** (description, applyTo patterns)
   - **Content updates** (guidelines, examples, best practices)
5. Document key differences for outdated instructions
6. Calculate similarity to determine if update is needed

## File Structure Requirements

Based on GitHub documentation, copilot-instructions files should be:

- **Repository-wide instructions**: `.github/copilot-instructions.md` (applies to entire repository)
- **Path-specific instructions**: `.github/instructions/NAME.instructions.md` (applies to specific file patterns via `applyTo` frontmatter)
- **Community instructions**: `instructions/NAME.instructions.md` (for sharing and distribution)

## Front Matter Structure

Instructions files in awesome-copilot use this front matter format:

```markdown
---
description: "Brief description of what this instruction provides"
applyTo: "**/*.js,**/*.ts" # Optional: glob patterns for file matching
---
```

## Requirements

- Use `githubRepo` tool to get content from awesome-copilot repository instructions folder
- Scan local file system for existing instructions in `.github/instructions/` directory
- Read YAML front matter from local instruction files to extract descriptions and `applyTo` patterns
- Compare local instructions with remote versions to detect outdated instructions
- Compare against existing instructions in this repository to avoid duplicates
- Focus on gaps in current instruction library coverage
- Validate that suggested instructions align with repository's purpose and standards
- Provide clear rationale for each suggestion
- Include links to both awesome-copilot instructions and similar local instructions
- Clearly identify outdated instructions with specific differences noted
- Consider technology stack compatibility and project-specific needs
- Don't provide any additional information or context beyond the table and the analysis

## Icons Reference

- ✅ Already installed and up-to-date
- ⚠️ Installed but outdated (update available)
- ❌ Not installed in repo

## Update Handling

When outdated instructions are identified:

1. Include them in the output table with ⚠️ status
2. Document specific differences in the "Suggestion Rationale" column
3. Provide recommendation to update with key changes noted
4. When user requests update, replace entire local file with remote version
5. Preserve file location in `.github/instructions/` directory


## Template References

Detailed templates in `templates/suggest-awesome-github-copilot-instructions/`:


## Template References

Templates in `templates/suggest-awesome-github-copilot-instructions/`:
- `context_analysis_criteria.md`
- `file_structure_requiremen.md`
- `front_matter_structure.md`
- `icons_reference.md`
- `inputs.md`
- `local_instructions_discov.md`
- `output_format.md`
- `phases.md`
- `process.md`
- `requirements.md`
- `rules.md`
- `update_handling.md`
- `version_comparison_proces.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
