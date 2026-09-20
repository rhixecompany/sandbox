---
title: writing-prompt
version: 1.0.0
date_created: 2026-09-19
owner: default
status: active
tags: [skill, prompt, writing, prompt-engineering, platform-setup-diagnostics]
---

# writing-prompt Skill

Use this skill when creating, authoring, validating, or templating prompts for the Hermes platform and its sub-projects.

## Purpose

The `writing-prompt` skill provides the structure, conventions, and workflow for producing high-quality prompts. It defines where prompts live, how they are structured, and how they are verified before being considered ready for use.

## Location

Prompts created with this skill live under `.github/prompts/<category>/<trigger>/`.

For the Hermes Platform Setup & Diagnostics prompts, the location is:

```
.github/prompts/hermes-platform-setup-diagnostics/platform-setup-diagnostics/
```

## Folder Structure

A complete prompt skill directory contains:

```
<trigger>/
├── prompt.md              # The main prompt definition (frontmatter + body)
├── templates/             # Prompt templates for recurring patterns
│   └── README.md
├── scripts/               # Automation scripts for prompt validation/generation
│   └── README.md
└── verification/          # Verification evidence that the prompt works
    └── README.md
```

### prompt.md

The main prompt file. Must include:

- **Frontmatter**: `title`, `version`, `date_created`, `owner`, `status`, `tags`
- **Context**: What situation this prompt is for
- **Instructions**: What the AI should do when this prompt is invoked
- **Constraints**: What the AI must not do
- **Output format**: What the AI should produce

### templates/

Reusable prompt templates for common patterns within the domain. See `templates/README.md`.

Template files use `{{variable}}` syntax for substitution points and are rendered before use.

### scripts/

Scripts that validate, generate, or transform prompts. See `scripts/README.md`.

Supported platforms: Python, TypeScript, PowerShell, Bash — matching the spec skill's script conventions.

### verification/

Evidence that the prompt produces correct, useful output. See `verification/README.md`.

Contains validation outputs, sample invocations, and gate-pass evidence.

## Usage

1. **Create a new prompt**: Place a `prompt.md` with valid frontmatter and body in the trigger directory.
2. **Add templates**: Populate `templates/` with reusable prompt fragments for recurring patterns.
3. **Add scripts**: Populate `scripts/` with validation and generation scripts.
4. **Run verification**: Execute the verification scripts and capture evidence in `verification/`.
5. **Gate check**: Confirm the prompt produces correct output and verification evidence passes.

## Conventions

- Category directories use lowercase with hyphens: `<category>/`
- Trigger directories use lowercase with hyphens: `<trigger>/`
- Frontmatter fields are mandatory: `title`, `version`, `date_created`, `owner`, `status`, `tags`
- Status values: `draft`, `in_progress`, `active`, `closed`, `archived`
- Tags are lowercase hyphenated words in a YAML list
- Templates use `{{variable}}` syntax for substitution points
- Scripts must be runnable from their directory without external dependencies beyond what the Hermes environment provides

## Validation

A prompt is valid when:

- `prompt.md` exists with complete frontmatter
- The prompt produces the intended output when invoked
- All templates are syntactically valid (no unclosed `{{` without `}}`)
- All scripts in `scripts/` are syntactically valid (lint passes)
- The `verification/` directory contains evidence that the prompt works

## Related Skills

- `writing-spec` — for specifying what the prompt implements
- `writing-plan` — for planning the work the prompt supports
- `prompt-engineering` — for prompt design best practices
- `prompt-engineering-patterns` — for proven prompt patterns
- `prompts-judge` — for evaluating prompt quality
- `multi-file-change-protocol` — for managing changes across multiple files
