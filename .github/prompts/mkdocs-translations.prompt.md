---
name: mkdocs-translations
title: MkDocs Translations
description: Generates a language translation for an MkDocs documentation stack, preserving structure and Markdown semantics.
version: 1.0.0
author: Hermes Agent
date: '2026-08-25'
tags:
  - mkdocs
  - translation
  - documentation
  - i18n
  - automation
  - tooling
metadata:
  hermes:
    profile: code-architect
    priority: medium
  copilot:
    model_required: sonnet
  opencode:
    enabled: true
  codex:
    enabled: true
---
## Table of Contents

## Goal

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
- [Role](#role)
- [Required Input](#required-input)
- [Objective](#objective)
- [File Listing and Translation Order](#file-listing-and-translation-order)
- [Folder Structure and Output](#folder-structure-and-output)
- [Include Path Updates](#include-path-updates)
- [MkDocs Configuration Update](#mkdocs-configuration-update)
- [Translation Rules](#translation-rules)
- [Translating Includes (`docs/docs/includes/en`)](#translating-includes-`docs/docs/includes/en`)
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
- [Role](#role)
- [Required Input](#required-input)
- [Objective](#objective)
- [File Listing and Translation Order](#file-listing-and-translation-order)
- [Folder Structure and Output](#folder-structure-and-output)
- [Include Path Updates](#include-path-updates)
- [MkDocs Configuration Update](#mkdocs-configuration-update)
- [Translation Rules](#translation-rules)
- [Translating Includes (`docs/docs/includes/en`)](#translating-includes-`docs/docs/includes/en`)
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





Generate a language translation for a mkdocs documentation stack.


Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

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

## Role

You are a professional technical writer and translator.

## Required Input

**Before proceeding, ask the user to specify the target translation language and locale code.** Examples:

- Spanish (`es`)- French (`fr`)- Brazilian Portuguese (`pt-BR`)- Korean (`ko`)Use this value consistently in folder names, translated content paths, and MkDocs configuration updates. Once confirmed, proceed with the instructions below.---

## Objective

Translate all documentation from the `docs/docs/en` and `docs/docs/includes/en` folders into the specified target language. Preserve the original folder structure and all Markdown formatting.---

## File Listing and Translation Order

The following is the task list you must complete. Check each item off as it is done and report that to the user.

- [ ] Begin by listing all files and subdirectories under `docs/docs/en`.- [ ] Then list all files and subdirectories under `docs/docs/includes/en`.- [ ] Translate **every file** in the list **one by one** in the order shown. Do not skip, reorder, or stop after a fixed number of files.
- [ ] After each translation, **check whether there are remaining files** that have not yet been translated. If there are, **continue automatically** with the next file.
- [ ] Do **not** prompt for confirmation, approval, or next steps—**proceed automatically** until all files are translated.
- [ ] Once completed, confirm that the number of translated files matches the number of source files listed. If any files remain unprocessed, resume from where you left off.---

## Folder Structure and Output

Before starting to create **any** new files, create a new git branch using the terminal command `git checkout -b docs-translation-<language

> `.- Create a new folder under`docs/docs/` named using the ISO 639-1 or locale code provided by the user. Examples: - `es` for Spanish - `fr` for French - `pt-BR` for Brazilian Portuguese- Mirror the exact folder and file structure from the original `en` directories.

- For each translated file: - Preserve all Markdown formatting, including headings, code blocks, metadata, and links. - Maintain the original filename. - Do **not** wrap the translated content in Markdown code blocks. - Append this line at the end of the file: _Translated using GitHub Copilot and GPT-4o._ - Save the translated file into the corresponding target language folder.---

## Include Path Updates

- Update include references in files to reflect the new locale. Example: `includes/en/introduction-event.md` → `includes/es/introduction-event.md` Replace `es` with the actual locale code provided by the user.---

## MkDocs Configuration Update

- [ ] Modify the `mkdocs.yml` configuration: - [ ] Add a new `locale` entry under the `i18n` plugin using the target language code. - [ ] Provide appropriate translations for: - [ ] `nav_translations` - [ ] `admonition_translations`---

## Translation Rules

> - Use accurate, clear, and technically appropriate translations.
> - Always use computer standard terminology.
> **Full content:**

## Translating Includes (`docs/docs/includes/en`)

- Create a new folder under `docs/docs/includes/` using the target language code provided by the user.
- Translate each file using the same rules as above.
- Maintain the same file and folder structure in the translated output.
- Save each translated file in the appropriate target language folder.

## Template References

Templates in `templates/mkdocs-translations/`:- `folder_structure_and_outp.md`- `phases.md`- `translation_rules.md`

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

## Skills Required

See [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md) for shared skills table.

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