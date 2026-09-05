---
name: update-markdown-file-index
title: Update Markdown File Index
description: Update a markdown section with an index or table of files from a specified folder using simple list, detailed table, or categorized section formats.
trigger: /update-markdown-file-index
category: documentation
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
Update a markdown section with an index or table of files from a specified folder using simple list, detailed table, or categorized section formats.

## Context

## Phases


# Table of Contents

- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
  - [Phase 1: Intake](#phase-1:-intake)
  - [Phase 2: Execute](#phase-2:-execute)
  - [Phase 3: Verify](#phase-3:-verify)
  - [Phase 4: Hand off](#phase-4:-hand-off)
- [Process](#process)
- [File Analysis](#file-analysis)
- [Table Structure Options](#table-structure-options)
  - [Option 1: Simple List](#option-1:-simple-list)
- [Files in $](#files-in-$)
  - [Option 2: Detailed Table](#option-2:-detailed-table)
  - [Option 3: Categorized Sections](#option-3:-categorized-sections)
- [Update Strategy](#update-strategy)
- [Section Identification](#section-identification)
- [Requirements](#requirements)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Context](#context)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Rules](#rules)
- [Phases](#phases)
- [Phase 1: Intake](#phase-1:-intake)
- [Phase 2: Execute](#phase-2:-execute)
- [Phase 3: Verify](#phase-3:-verify)
- [Phase 4: Hand off](#phase-4:-hand-off)
- [Process](#process)
- [File Analysis](#file-analysis)
- [Table Structure Options](#table-structure-options)
- [Option 1: Simple List](#option-1:-simple-list)
- [Files in $](#files-in-$)
- [Option 2: Detailed Table](#option-2:-detailed-table)
- [Option 3: Categorized Sections](#option-3:-categorized-sections)
- [Update Strategy](#update-strategy)
- [Section Identification](#section-identification)
- [Requirements](#requirements)
- [Template References](#template-references)
- [Personas](#personas)
- [Personality](#personality)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Tasks](#tasks)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Related Prompts](#related-prompts)





Update a markdown file section with an index/table of files from a specified folder.


Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/rules-core.md`](templates/rules-core.md)

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.


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

- Return the final artifact or findings .
- Stop once the requested result is delivered.

## Process

1. **Scan**: Read the target markdown file `${file}` to understand existing structure
2. **Discover**: List all files in the specified folder `${input:folder}` matching pattern `${input:pattern}`
3. **Analyze**: Identify if an existing table/index section exists to update, or create new structure
4. **Structure**: Generate appropriate table/list format based on file types and existing content
5. **Update**: Replace existing section or add new section with file index
6. **Validate**: Ensure markdown syntax is valid and formatting is consistent

## File Analysis

For each discovered file, extract:

- **Name**: Filename with or without extension based on context- **Type**: File extension and category (e.g., `.md`, `.js`, `.py`)- **Description**: First line comment, header, or inferred purpose- **Size**: File size for reference (optional)- **Modified**: Last modified date (optional)

## Table Structure Options

Choose format based on file types and existing content:

### Option 1: Simple List

```markdown

## Files in $

folder

- [filename.ext](path/to/filename.ext) - Description- [filename2.ext](path/to/filename2.ext) - Description
```

### Option 2: Detailed Table

| File | Type | Description || -------------------------------------

- | --------- | ----------- || [filename.ext](path/to/filename.ext) | Extension | Description || [filename2.ext](path/to/filename2.ext) | Extension | Description |

### Option 3: Categorized Sections

Group files by type/category with separate sections or sub-tables.

## Update Strategy

- 🔄 **Update existing**: If table/index section exists, replace content while preserving structure- ➕ **Add new**: If no existing section, create new section using best-fit format- 📋 **Preserve**: Maintain existing markdown formatting, heading levels, and document flow- 🔗 **Links**: Use relative paths for file links within the repository

## Section Identification

Look for existing sections with these patterns:

- Headings containing: "index", "files", "contents", "directory", "list"- Tables with file-related columns- Lists with file links- HTML comments marking file index sections

## Requirements

- Preserve existing markdown structure and formatting
- Use relative paths for file links
- Include file descriptions when available
- Sort files alphabetically by default
- Handle special characters in filenames
- Validate all generated markdown syntax

## Template References

Templates in `templates/`:- `files_in_folder.md`- `phases.md`

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

## Best Practices

See [`templates/best-practices.md`](templates/best-practices.md) for cross-cutting best practices.

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

## Hooks

Shared workspace hooks run around this prompt's execution — see [`.github/hooks/README.md`](../hooks/README.md): `session-logger`, `session-auto-commit`, `governance-audit`, `pre-exec-validate.sh`, `post-exec-state-log.py`.

## Scripts

Prompt-library tooling (see `.enhance/`):

- `.enhance/analyze_prompts.py` — prompt-library analyzer (Phase 5/7 gate)
- `.enhance/verify_phase3.py`, `.enhance/fix_class_e.py`, `.enhance/fix_frontmatter_plan.py` — Class C–E repair/verify tooling
- `.github/hooks/*` — hook implementations referenced in the Hooks section

## Related Prompts

## Workflow

<content>

Same-family prompts:

- [`update-avm-modules-in-bicep.prompt.md`](update-avm-modules-in-bicep.prompt.md)
- [`update-docs-on-code-change.prompt.md`](update-docs-on-code-change.prompt.md)
- [`update-implementation-plan.prompt.md`](update-implementation-plan.prompt.md)
- [`update-llms.prompt.md`](update-llms.prompt.md)
- [`update-oo-component-documentation.prompt.md`](update-oo-component-documentation.prompt.md)
- [`update-specification.prompt.md`](update-specification.prompt.md)
