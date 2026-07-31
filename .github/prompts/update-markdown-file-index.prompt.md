---

name: update-markdown-file-index

title: Update Markdown File Index

description: Update a markdown file section with an index/table of files from a specified folder.

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - web

scripts: []

skills: []

formatter: default

plan: None

tags:

  - maintenance

  - markdown

  - ml

  - prompts

  - specification

  - typescript

trigger: /update-markdown-file-index

dependencies: []

metadata:

  hermes: {}

---

## Goal

Update a markdown file section with an index/table of files from a specified folder.

## Context

Use when you need to work on the current workspace or task.

## Input

s

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Output

s

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

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

- [filename.ext](path/to/filename.ext) - Description- [filename2.ext](path/to/filename2.ext) - Description```

### Option 2: Detailed Table

| File                                   | Type      | Description || -------------------------------------

- | --------- | ----------- || [filename.ext](path/to/filename.ext)   | Extension | Description || [filename2.ext](path/to/filename2.ext) | Extension | Description |

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

Templates in `templates/update-markdown-file-index/`:- `files_in_folder.md`- `phases.md`

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

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

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
|---|------|-----------|
| 1 | Scope | Change matches the original request |
| 2 | Quality | Meets project standards |
| 3 | Tests | Tests pass (if applicable) |
| 4 | Regression | No unintended side effects |
| 5 | Docs | Changes documented if needed |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Goal

Update a markdown file section with an index/table of files from a specified folder.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

| Skill | Purpose |
|-------|---------|
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

