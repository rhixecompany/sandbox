---
name: context-map
title: context map
description: Prompt for context-map
version: "1.0.0"
tags: [analysis, architecture, planning, tool, visualization]
trigger: context-map
metadata:
  hermes:
    profile: default
    priority: medium
    categories: []
  copilot:
    model_required: claude-opus
    context_length: medium
  opencode:
    enabled: true
    compatibility: compatible
  codex:
    enabled: false
    model_preferred: text-davinci-003

---
name: context-map
title: Context Map
description: Build a dependency and reference map before making changes so implementation
  starts from the right files.
version: 2.0.0
license: MIT
author: Hermes Agent
toolsets:
- file
- terminal
scripts: []
skills:
- codemap
formatter: default
plan: null
dependencies:
- skill:codemap
tags:
- audit
- frontend
- prompts
- specification
- testing
- typescript
- audit
- frontend
- prompts
- specification
- testing
- typescript
trigger: /context-map
metadata:
  hermes: None
  related_skills:
  - codemap
name: context-map
title: Context Map
description: Build a dependency and reference map before making changes so implementation
  starts from the right files.
version: 2.0.0
license: MIT
author: Hermes Agent
toolsets:
- file
- terminal
scripts: []
skills:
- codemap
formatter: default
plan: null
dependencies:
- skill:codemap
tags:
- audit
- frontend
- prompts
- specification
- testing
- typescript
- audit
- frontend
- prompts
- specification
- testing
- typescript
trigger: /context-map
metadata:
  hermes: None
  related_skills:
  - codemap
---

## Goal

Build a dependency and reference map before making changes so implementation starts from the right files.

# context-map> Build a dependency-aware context map before implementation begins.

## Context

- Use when the task needs a safe pre-change inventory
- Focus on direct dependencies, related tests, and nearby patterns
- Keep the map concrete and file-driven
- Do not proceed to implementation until the map is reviewed

## Inputs

- Task description
- Optional target area, feature, or bug report
- Optional constraints or known files

## Outputs

- A context map with files to modify, dependencies, tests, and reference patterns
- A short risk assessment
- Present the context map as a Markdown table with columns: File | Role (modify/dependency/test) | Notes
- Follow with a bulleted risk assessment of 3-5 items max

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. If the task description is too vague to identify specific files, stop and ask the user to clarify the target area before proceeding to Phase 1
2. Search for the files directly related to the task
3. Identify imports, exports, and other dependencies
4. Identify the likely test files
5. If no related test files are found, explicitly state "No related tests identified" in the map and flag it as a risk item
6. Find 2-3 existing code examples in the codebase that demonstrate the same pattern (for example, same hook usage, same module export style) that the new change should follow
7. Call out breaking-change risks clearly
8. Stop after mapping; do not implement yet

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill | Purpose |
| --- | --- |
| `codemap` | Codebase discovery and dependency mapping (loads symbol tables, dependency trees, and cross-file references) |

## Phases

### Phase 1: Discover the scope

> **Goal:** find the files and relationships that matter.>

## Actions Summary

1. **Phase 1:** Discover the scope
2. **Phase 2:** Map dependencies, tests, and reference patterns
3. **Phase 3:** Record the risks and review completeness
4. **Phase 4:** Return the context map and stop

## Template References

Templates in `templates/context-map/`:- `phases.md`

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

