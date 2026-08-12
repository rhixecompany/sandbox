---
name: update-avm-modules-in-bicep
title: Update Azure Verified Modules in Bicep Files
description: Update Azure Verified Modules (AVM) to latest versions in Bicep files.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - web
scripts: []
skills: []
formatter: default
plan: 'None'
tags:
  - azure
  - maintenance
  - ml
  - prompts
  - specification
  - testing
  - typescript
trigger: /update-avm-modules-in-bicep
dependencies: []
metadata:
  hermes: {}
---

## Goal

Update Azure Verified Modules (AVM) to latest versions in Bicep files.

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

1. **Scan**: Extract AVM modules and current versions from `${file}`
1. **Identify**: List all unique AVM modules used by matching `avm/res/{service}/{resource}` using `#search` tool
1. **Check**: Use `#fetch` tool to get latest version of each AVM module from MCR: `https://mcr.microsoft.com/v2/bicep/avm/res/{service}/{resource}/tags/list`
1. **Compare**: Parse semantic versions to identify AVM modules needing update
1. **Review**: For breaking changes, use `#fetch` tool to get docs from: `https://github.com/Azure/bicep-registry-modules/tree/main/avm/res/{service}/{resource}`
1. **Update**: Apply version updates and parameter changes using `#editFiles` tool
1. **Validate**: Run `bicep lint` and `bicep build` using `#runCommands` tool to ensure compliance.
1. **Output**: Summarize changes in a table format with summary of updates below.

## Tool Usage

Always use tools `#search`, `#searchResults`,`#fetch`, `#editFiles`, `#runCommands`, `#todos` if available. Avoid writing code to perform tasks.

## Breaking Change Policy⚠️ **PAUSE for approval** if updates involve:

- Incompatible parameter changes- Security/compliance modifications- Behavioral changes

## Output Format

Only display results in table with icons:```markdown| Module | Current | Latest | Status | Action | Docs || --- | --- | --- | --- | --- | --- || avm/res/compute/vm | 0.1.0 | 0.2.0 | 🔄 | Updated | [📖](link) || avm/res/storage/account | 0.3.0 | 0.3.0 | ✅ | Current | [📖](link) |

### Summary of Updates

Describe updates made, any manual reviews needed or issues encountered.

```

## Icons

- 🔄 Updated- ✅ Current- ⚠️ Manual review required- ❌ Failed- 📖 Documentation

## Requirements

- Use MCR tags API only for version discovery
- Parse JSON tags array and sort by semantic versioning
- Maintain Bicep file validity and linting compliance

## Template References

Templates in `templates/update-avm-modules-in-bicep/`:- `phases.md`

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

