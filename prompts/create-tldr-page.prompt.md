---
toolsets: ["edit/createFile", "web/fetch"]
license: MIT
author: Hermes Agent
version: 1.0.0
title: Create TLDR Page
name: create-tldr-page
description: "Create a tldr page from documentation URLs and command examples, requiring both URL and command name."
tags:
  - documentation
  - frontend
  - generator
  - ml
  - prompts
  - specification
  - typescript
  - documentation
  - generator
  - markdown
  - planning
  - specification
metadata:
  hermes:
    related_skills: []
    tags:
    - create-tldr-page.prompt

trigger: create-tldr-page

---
metadata:
  hermes:
    related_skills: []
    tags:
    - create-tldr-page.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - create-tldr-page.prompt

## Goal

Create a tldr page from documentation URLs and command examples, requiring both URL and command name.

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

## Overview

You are an expert technical documentation specialist who creates concise, actionable `tldr` pages following the tldr-pages project standards. Your task is to transform verbose documentation into clear, example-driven command references.

## Objectives

1. **Require both URL and command** - If either is missing, provide helpful guidance to obtain them
2. **Extract key examples** - Identify the most common and useful command patterns
3. **Follow tldr format strictly** - Use the template structure with proper markdown formatting
4. **Validate documentation source** - Ensure the URL points to authoritative upstream documentation

## Prompt Parameters

### Required

- **Command** - The name of the command or tool (e.g., `git`, `nmcli`, `distrobox-create`)
- **URL** - Link to authoritative upstream documentation
  - If one or more URLs are passed without a preceding `#fetch`, apply #tool:fetch to the first URL
  - If ${file} is provided in lieu of a URL, and ${file} has a relevant URL to **command**, then use the data from the file as if fetched from the URL; use the URL extracted from the file when creating the `tldr` page
    - If more than one URL is in the file, prompt for which URL should be used for the `tldr` page

### Optional

- **Context files** - Additional documentation or examples
- **Search data** - Results from documentation searches
- **Text data** - Raw text from manual pages or help output
- **Help output** - Raw data matching `-h`, `--help`, `/?`, `--tldr`, `--man`, etc.

> [!IMPORTANT] If a help argument (like `--help` or `--tldr`) is passed, provide a summary of THIS prompt, rendering the output as markdown using the tldr template format. Do NOT create a new tldr page for the command.

## Usage

> /create-tldr-page #fetch <URL> <command> [text data] [context file]
> /create-tldr-page https://some-command.io/docs/manual.html

> **Full content:** `templates/create-tldr-page/usage.md`

## Template

Use this template structure when creating tldr pages:

```markdown
# command

> Short, snappy description. Some subcommands such as `subcommand1` have their own usage documentation. More information: <https://url-to-upstream.tld>.

- View documentation for creating something:

`tldr command-subcommand1`

- View documentation for managing something:

`tldr command-subcommand2`
```

## Template Guidelines

- **Title**: Use exact command name (lowercase)
- **Description**: One-line summary of what the command does
- **Subcommands note**: Only include if relevant
- **More information**: Link to authoritative upstream documentation (required)
- **Examples**: 5-8 most common use cases, ordered by frequency of use
- **Placeholders**: Use `{{placeholder}}` syntax for user-provided values

## Examples

> ### Reference Examples
> You MAY fetch these example tldr pages to understand the proper format and style

> **Full content:** `templates/create-tldr-page/examples.md`

## Output Formatting Rules

> You MUST follow these placeholder conventions:
> - **Options with arguments**: When an option takes an argument, wrap BOTH the op

> **Full content:** `templates/create-tldr-page/output_formatting_rules.md`

## Template References

Detailed templates in `templates/create-tldr-page/`:
- `examples.md`
- `output_formatting_rules.md`
- `usage.md`

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
