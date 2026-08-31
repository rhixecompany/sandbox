---
name: list-all-installed-vscode-extension
title: List Installed VS Code Extensions
description: Inventories all installed VS Code extensions, researches their documentation, and applies findings to optimize user and workspace settings.
trigger: /list-all-installed-vscode-extension
version: 1.0.0
author: Hermes Agent
date: 2026-08-25
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
Inventories all installed VS Code extensions, researches their documentation, and applies findings to optimize user and workspace settings.

## Context

## Phases



# Table of Contents

- [Goal](#goal)
- [Input](#input)
- [Output](#output)
- [Workflow](#workflow)
  - [Phase 1: Inventory — List Installed Extensions](#phase-1:-inventory-—-list-installed-extensions)
  - [Phase 2: Research — Document Each Extension](#phase-2:-research-—-document-each-extension)
- [Description](#description)
- [Contributed Settings](#contributed-settings)
- [Notes](#notes)
  - [Phase 3: Synthesize — Identify Conflicts, Gaps, and Optimizations](#phase-3:-synthesize-—-identify-conflicts-gaps-and-optimizations)
  - [Phase 4: Apply — Modify Settings](#phase-4:-apply-—-modify-settings)
- [Context Injection](#context-injection)
- [Error Handling](#error-handling)
- [Success Criteria](#success-criteria)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
  - [Domain Rules](#domain-rules)
  - [Standing Rules](#standing-rules)
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
- [Input](#input)
- [Output](#output)
- [Workflow](#workflow)
- [Phase 1: Inventory — List Installed Extensions](#phase-1:-inventory-—-list-installed-extensions)
- [Phase 2: Research — Document Each Extension](#phase-2:-research-—-document-each-extension)
- [Description](#description)
- [Contributed Settings](#contributed-settings)
- [Notes](#notes)
- [Phase 3: Synthesize — Identify Conflicts, Gaps, and Optimizations](#phase-3:-synthesize-—-identify-conflicts-gaps-and-optimizations)
- [Phase 4: Apply — Modify Settings](#phase-4:-apply-—-modify-settings)
- [Context Injection](#context-injection)
- [Error Handling](#error-handling)
- [Success Criteria](#success-criteria)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Rules](#rules)
- [Domain Rules](#domain-rules)
- [Standing Rules](#standing-rules)
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





Inventory all installed VS Code extensions, research their documentation, and apply findings to improve user and workspace settings. Multi-phase: discover → research → synthesize → configure.

## List All Installed VS Code Extensions — Full Lifecycle

Analyze every installed VS Code extension, research its documentation and purpose, then apply findings to create, update, debug, and fix user and workspace settings.

Use this when onboarding to a new machine, auditing your extension footprint, or optimising settings around installed tooling.

## Input

- **`${input:profile:default}`** — optional VS Code profile name to scope the inventory (e.g. `"Web Development"`, `"Data Science"`). Defaults to the active profile.
- **`${input:scope:all}`** — scope of work: `all` (research + apply settings), `inventory` (list only), `research` (list + document), `apply` (existing inventory, skip list).

## Output

1. **Extension Inventory** — saved to `.vscode/extension-inventory.md` with name, version, publisher, category, description
2. **Extension Dossier** — saved to `docs/vscode-extensions/<publisher.extension>/README.md` per extension with usage notes and config relevance
3. **Settings Report** — list of recommended changes to `settings.json` (user + workspace)
4. **Changes Applied** — modifications to `C:\Users\Alexa\AppData\Roaming\Code\User\settings.json` and/or `.vscode/settings.json`

## Workflow

### Phase 1: Inventory — List Installed Extensions

1. Run `code --list-extensions --show-versions` to get the full list with versions.
- If a profile was provided, add `--profile "<profile>"`.
- If VS Code CLI is not in PATH, see **Error Handling** below.
2. Capture the output. Each line is `publisher.extension-name` optionally with `@version` when `--show-versions` is used.
3. Save the raw list to `.vscode/extension-inventory.md` with YAML frontmatter:

```yaml
---
generated: <ISO date>
profile: <profile name or "default">
count: <N>
---
```

4. Enrich the inventory: for each extension, derive a rough category (language support, theme, linter, debugger, snippets, etc.) from the publisher and extension name. Don't web-search at this stage — just note the heuristic.
5. **Verification gate:** Confirm the count matches what the Extensions panel shows. If `code --list-extensions` returns 0 or errors, escalate.

### Phase 2: Research — Document Each Extension

For each extension, do NOT fetch docs individually (too many round-trips). Instead:

1. **Batch by market page:** For each unique `publisher.extension-name`, fetch `https://marketplace.visualstudio.com/items?itemName=<publisher>.<extension>` using `web_extract`.
2. Extract: short description, categories/tags, known settings this extension contributes, and any notable configuration guidance.
3. Save per-extension dossier to `docs/vscode-extensions/<publisher>.<extension>/README.md`:

```markdown
# <Display Name>
- **ID:** `publisher.extension` - **Version:** X.Y.Z
- **Category:** <theme/linter/language/etc.>
- **Marketplace:** [link](https://marketplace.visualstudio.com/...)

## Description
<from marketplace>

## Contributed Settings
<extension-specific settings prefixes, if discoverable>

## Notes
<your analysis: is this active? does it overlap with other installed extensions?>
```

4. **Failover:** If `web_extract` fails for a specific extension page (network, 404, rate-limit), log the failure in the dossier with `[FETCH_FAILED]` but continue with the others. Do NOT block Phase 2 on a single extension — the extension name alone carries signal.

### Phase 3: Synthesize — Identify Conflicts, Gaps, and Optimizations

1. Read the collected dossiers and identify:
- **Overlapping extensions** (e.g. two Python linters, two theme packs)
- **Inactive/discontinued extensions** (check `--list-extensions` against marketplace status)
- **Extensions relevant to the current workspace** (match against project files, `package.json`, `requirements.txt`, etc.)
- **Extensions missing but suggested by project files** (e.g. a `pyproject.toml` without Python extension)
2. Cross-reference: Check if the current user `settings.json` references settings from these extensions (search `C:\Users\Alexa\AppData\Roaming\Code\User\settings.json` for extension-prefixed keys).
3. Produce a **Settings Report** as `.vscode/settings-report.md` with sections:
- Extensions to keep
- Extensions to review (potential duplicates)
- Settings to add/update/remove with reasoning
- Settings changes scoped to workspace vs. user

### Phase 4: Apply — Modify Settings

1. **Always confirm before writing.** Use `vscode/askQuestions` to present the Settings Report and ask which changes to apply.
2. Apply changes:
- **User settings:** `patch` against `C:\Users\Alexa\AppData\Roaming\Code\User\settings.json`
- **Workspace settings:** `patch` against `.vscode/settings.json` (create if absent)
3. **One variable at a time** — apply settings in logical groups (theme first, then linter config, then language-specific), verifying after each group.
4. **Never batch independent fixes** — each settings change group is a separate patch.

## Context Injection

Reference these files by their Markdown links rather than duplicating their content:

- [VS Code CLI — extension management](https://code.visualstudio.com/docs/configure/command-line#_working-with-extensions)
- [VS Code settings documentation](https://code.visualstudio.com/docs/getstarted/settings)
- [VS Code extension marketplace](https://marketplace.visualstudio.com/)
- Current workspace config: [.vscode/settings.json](.vscode/settings.json) (if exists)
- User settings: `C:\Users\Alexa\AppData\Roaming\Code\User\settings.json`

## Error Handling

| Error | Handling |
| ------- | ---------- |
| `code` CLI not in PATH | On Windows, the default path is `C:\Users\Alexa\AppData\Local\Programs\Microsoft VS Code\bin`. Fall back to the full path `"C:\Users\Alexa\AppData\Local\Programs\Microsoft VS Code\bin\code.cmd" --list-extensions`. If still not found, install VS Code or add to PATH. |
| Marketplace page 404 | Extension may be unpublished or private. Log as `[UNPUBLISHED]` and skip. |
| Rate-limited by marketplace | Back off 5 seconds between fetches. If still blocked, surface the failure and continue without that dossier — partial data is actionable. |
| `settings.json` write conflict | Read the file first, merge rather than overwrite, and validate JSON before writing. |
| Profile not found | `code --list-extensions --profile "X"` on a non-existent profile creates it empty. Warn and use `--profile "X"` anyway (the list will be empty, which is a signal the user should switch profiles). |

## Success Criteria

- [ ] All installed extensions are inventoried and documented
- [ ] Settings Report is generated with actionable recommendations
- [ ] User confirmed changes before write
- [ ] `code --list-extensions` output still shows the same extensions after changes (no accidental uninstalls)
- [ ] VS Code settings JSON is valid after all patches
- [ ] Workspace `.vscode/settings.json` is valid JSON and checked into version control

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


Use when fixing, repairing, or synchronizing files or configs. Diagnose first, apply minimal changes, verify each fix.

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State when something fails.

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

## Related Prompts

Same-family prompts:

- [`execute-all-prompts.prompt.md`](execute-all-prompts.prompt.md)