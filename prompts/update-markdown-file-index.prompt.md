---
toolsets:
  - changes
  - search/codebase
  - edit/editFiles
  - extensions
  - web/fetch
  - findTestFiles
  - githubRepo
  - openSimpleBrowser
  - problems
  - runCommands
  - runTasks
  - runTests
  - search
  - search/searchResults
  - runCommands/terminalLastCommand
  - runCommands/terminalSelection
  - testFailure
  - usages
  - vscodeAPI
license: MIT
author: Hermes Agent
version: 1.0.0
title: Update Markdown File Index
name: update-markdown-file-index
description: "Update a markdown file section with an index/table of files from a specified folder."
tags: []
---


## Goal

Update a markdown file section with an index/table of files from a specified folder.

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

- **Name**: Filename with or without extension based on context
- **Type**: File extension and category (e.g., `.md`, `.js`, `.py`)
- **Description**: First line comment, header, or inferred purpose
- **Size**: File size for reference (optional)
- **Modified**: Last modified date (optional)

## Table Structure Options

Choose format based on file types and existing content:

### Option 1: Simple List

```markdown
## Files in ${folder}

- [filename.ext](path/to/filename.ext) - Description
- [filename2.ext](path/to/filename2.ext) - Description
```

### Option 2: Detailed Table

| File                                   | Type      | Description |
| -------------------------------------- | --------- | ----------- |
| [filename.ext](path/to/filename.ext)   | Extension | Description |
| [filename2.ext](path/to/filename2.ext) | Extension | Description |

### Option 3: Categorized Sections

Group files by type/category with separate sections or sub-tables.

## Update Strategy

- 🔄 **Update existing**: If table/index section exists, replace content while preserving structure
- ➕ **Add new**: If no existing section, create new section using best-fit format
- 📋 **Preserve**: Maintain existing markdown formatting, heading levels, and document flow
- 🔗 **Links**: Use relative paths for file links within the repository

## Section Identification

Look for existing sections with these patterns:

- Headings containing: "index", "files", "contents", "directory", "list"
- Tables with file-related columns
- Lists with file links
- HTML comments marking file index sections

## Requirements

- Preserve existing markdown structure and formatting
- Use relative paths for file links
- Include file descriptions when available
- Sort files alphabetically by default
- Handle special characters in filenames
- Validate all generated markdown syntax


## Template References

Templates in `templates/update-markdown-file-index/`:
- `files_in_folder.md`
- `phases.md`
