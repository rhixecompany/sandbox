---
license: MIT
author: Hermes Agent
version: 1.0.0
title: convert-plaintext-to-md
name: convert-plaintext-to-md
trigger: /convert-plaintext-to-md
description: >-
  Convert plaintext documentation to properly formatted markdown using explicit instructions, documented options, or reference files.
tags: []
  - hermes
  - copilot
  - markdown
  - conversion
  - documentation
dependencies:
  - skill:enhance-markdown
  - skill:/context-map
skills:
  - enhance-markdown — TXT→MD conversion and enhancement pipeline
---

# convert-plaintext-to-md

> Convert a text-based document to markdown following explicit instructions, documented options, or a reference file as a template.

## Goal

Convert plaintext or generic text-based documentation files to properly formatted markdown, preserving all technical content while applying markdown best practices.

## Context

Use when you need to convert a plaintext documentation file to markdown format, with optional parameters for fine-tuning the conversion.

## Inputs

- The plaintext file to convert (`#file:{{file}}`)
- Optional conversion parameters as defined in the Parameters table
- Optional predefined instructions (`pre=<name>`)
- Optional reference `.md` file as a formatting template

## Outputs

- A properly formatted markdown file at `{{file}}.md`
- A verification note listing: (1) total sections converted, (2) any inferred formatting decisions made without explicit instructions, and (3) any content skipped due to `--stop`. Omit if the source file is a single flat section with no ambiguous structure.

## Rules

- Run `/context-map` before conversion to map source, destination, and dependency impact.
- Preserve all technical content accurately - do not modify data unless instructions clearly specify
- Use markdown best practices: proper headers, lists, code blocks, and other elements
- Follow the prompt literally and prefer evidence from the current workspace
- Keep the response structured, deterministic, and easy to act on
- Avoid changing unrelated files or adding unnecessary scope
- When in doubt, always use markdown best practices and reference the URLs below
- Do not stop the conversion process when encountering `exit()`, `kill`, `quit`, or similar documented procedures
- If `#file:{{file}}` cannot be located or read, stop immediately and respond: "Error: source file `{{file}}` not found. Please provide a valid file path and retry." Do not create any output file.
- **Idempotent behavior:** If `{{file}}.md` already exists, treat its current content as the plaintext source data and overwrite `{{file}}.md` with newly formatted output
- When both `guide` and `instructions` are provided, `instructions` takes precedence over the guide template for any directly conflicting formatting decisions

## Skills Required

| Skill | Purpose |
| --- | --- |
| `context-map` | Preflight file/dependency mapping before conversion edits |
| `writing-plans` | Structured conversion plan for complex documents |
| `simplify` | Ensure output is concise and non-redundant |

## Phases

> **Goal:** Read the request and identify the exact scope.
> 1. Read the request and identify the exact scope

> **Full content:** `templates/convert-plaintext-to-md/phases.md`

## Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| `#file:{{file}}` | Yes | Plaintext file to convert. If `{{file}}.md` exists, treat existing content as source data |
| `finalize` | No | Trim spaces, indentation, and sloppy formatting after conversion |
| `guide #file:{{reference-file}}` | No | Use a previously converted `.md` file as formatting template |
| `instructions` | No | Additional text instructions for the conversion |
| `platform={{name}}` | No | Target platform: GitHub (default), StackOverflow, VS Code, GitLab, CommonMark |
| `--header [1-4]` | No | Add markdown header tags at specified level (level range: 1 to 4) |
| `-p, --pattern <name|file>` | No | Apply a named structural pattern (for example, `api-doc`, `changelog`) or reference a local `.md` file as a layout pattern. If no pattern is found, fall back to markdown best practices |
| `-s, --stop <N|eof>` | No | Convert only up to line N of the source plaintext (1-based), then write the partial result to `{{file}}.md`. Use `eof` to explicitly convert the entire file (default behavior) |

## Predefined Instructions

| Name | Description |
| --- | --- |
| `rm-head-digits` | Remove prepending numbers from headers during conversion |
| `mv-head-level(x, y)` | Change heading level from `x` to `y` |
| `rm-indent(x)` | Decrease paragraph/raw text indentation by `x` |

> **Note:** Match `pre=<name>` only by exact string equality against the Name column in this table. Partial or case-insensitive matches are not valid; treat them as no-match and disregard.

## Reference

- [GitHub Markdown Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [Markdown Guide Extended Syntax](https://www.markdownguide.org/extended-syntax/)
- [Azure DevOps Markdown Guidance](https://learn.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=azure-devops)


## Template References

Detailed templates in `templates/convert-plaintext-to-md/`:
- `phases.md`
