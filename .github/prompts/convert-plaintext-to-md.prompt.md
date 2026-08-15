---
name: convert-plaintext-to-md
title: Convert Plaintext to Markdown
description: Convert plaintext documentation to properly formatted markdown using explicit instructions,
  documented options, or reference files.
version: 1.0.0
license: MIT
author: Hermes Agent
trigger: /convert-plaintext-to-md
toolsets:
- file
- terminal
- web
skills:
- enhance-markdown
- context-map
dependencies:
- skill:enhance-markdown
- skill:context-map
formatter: default
metadata:
  hermes:
    profile: code-architect
    mcp_servers: []
    context_size: large
  copilot:
    context_size: large
    extensions: []
    keybinding: null
  opencode:
    command: opencode /convert-plaintext-to-md
    flags: {}
    help: Convert plaintext documentation to properly formatted markdown using explicit...
  codex:
    model_override: null
    system_prompt_id: null
    temperature: null
    max_tokens: null
tags:
- agent-type:hermes
- conversion
- documentation
- markdown
- ml
- prompts
- typescript
scripts: []
---

## Goal

Convert plaintext documentation to properly formatted markdown using explicit instructions, documented options, or reference files.

# convert-plaintext-to-md> Convert a text-based document to markdown following explicit instructions, documented options, or a reference file as a template.

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

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

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

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill | Purpose |
| --- | --- |
| `context-map` | Preflight file/dependency mapping before conversion edits |
| `writing-plans` | Structured conversion plan for complex documents |
| `simplify` | Ensure output is concise and non-redundant |

## Phases

> **Goal:** Read the request and identify the exact scope.>
>
> 1. Read the request and identify the exact scope

## Parameters

| Parameter | Required | Description || --- | --- | --- || `#file:{{file}}` | Yes | Plaintext file to convert. If `{{file}}.md` exists, treat existing content as source data || `finalize` | No | Trim spaces, indentation, and sloppy formatting after conversion || `guide #file:{{reference-file}}` | No | Use a previously converted `.md` file as formatting template || `instructions` | No | Additional text instructions for the conversion || `platform={{name}}` | No | Target platform: GitHub (default), StackOverflow, VS Code, GitLab, CommonMark || `--header [1-4]` | No | Add markdown header tags at specified level (level range: 1 to 4) || `-p, --pattern <name | file

> ` | No | Apply a named structural pattern (for example, `api-doc`,`changelog`) or reference a local`.md` file as a layout pattern. If no pattern is found, fall back to markdown best practices || `-s, --stop <N | eof>` | No | Convert only up to line N of the source plaintext (1-based), then write the partial result to `{{file}}.md`. Use`eof` to explicitly convert the entire file (default behavior) |

## Predefined Instructions

| Name | Description || --- | --- || `rm-head-digits` | Remove prepending numbers from headers during conversion || `mv-head-level(x, y)` | Change heading level from `x` to `y` || `rm-indent(x)` | Decrease paragraph/raw text indentation by `x` |

> **Note:** Match `pre=<name>` only by exact string equality against the Name column in this table. Partial or case-insensitive matches are not valid; treat them as no-match and disregard.

## Reference

- [GitHub Markdown Syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)- [Markdown Guide Extended Syntax](https://www.markdownguide.org/extended-syntax/)- [Azure DevOps Markdown Guidance](https://learn.microsoft.com/en-us/azure/devops/project/wiki/markdown-guidance?view=azure-devops)

## Template References

Detailed templates in `templates/convert-plaintext-to-md/`:- `phases.md`

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