---
name: repo-story-time
title: Repo Story Time
description: Transform any repository's git history into REPOSITORY_SUMMARY.md (technical overview) and THE_STORY_OF_THIS_REPO.md (narrative from commit history) using evidence-based analysis.
trigger: /repo-story-time
version: 1.0.0
author: Hermes Agent
tags: [repo, git, narrative, summary, history, documentation]
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
date: '2026-08-25'
---
## Table of Contents

## Goal

## Context

## Phases






# Table of Contents

- [Goal](#goal)
- [Workflow](#workflow)
  - [Phase 1: Repository Exploration](#phase-1:-repository-exploration)
  - [Phase 2: Analysis](#phase-2:-analysis)
  - [Phase 3: Write Files](#phase-3:-write-files)
- [Rules](#rules)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Tasks](#tasks)
- [Related Prompts](#related-prompts)



- [Goal](#goal)
- [Workflow](#workflow)
- [Phase 1: Repository Exploration](#phase-1:-repository-exploration)
- [Phase 2: Analysis](#phase-2:-analysis)
- [Phase 3: Write Files](#phase-3:-write-files)
- [Rules](#rules)
- [Personas](#personas)
- [Personality](#personality)
- [Context](#context)
- [Best Practices](#best-practices)
- [Verification Checklist](#verification-checklist)
- [Dependencies](#dependencies)
- [Subgoals](#subgoals)
- [Skills Required](#skills-required)
- [MCP Servers & Tools](#mcp-servers-&-tools)
- [Hooks](#hooks)
- [Scripts](#scripts)
- [Tasks](#tasks)
- [Related Prompts](#related-prompts)





Transform any repository's git history into two deliverables:

1. **REPOSITORY_SUMMARY.md** — Technical architecture and purpose overview
2. **THE_STORY_OF_THIS_REPO.md** — Narrative story from commit history analysis

For a lighter 5-bullet summary instead of a full story, use the
**Quick Repo Onboarding** section in `repo.prompt.md` (Q1: summarize + entrypoint).

## Workflow

### Phase 1: Repository Exploration

```bash
git log --oneline --since="1 year ago" | wc -l # commit count
git shortlog -sn # contributor stats
git diff --stat origin/main..HEAD | tail -3 # recent changes
ls -la projects/<name>/src # structure overview
```

### Phase 2: Analysis

- Identify tech stack, key components, data flow
- Extract contributor patterns, seasonal activity, major themes
- Cross-reference with AGENTS.md and README.md for context

### Phase 3: Write Files

Create both markdown files at the repo root using `write_file`:

| File | Content |
| --------------------------- | -------------------------------------------------------------------------------------- |
| `REPOSITORY_SUMMARY.md` | Overview, Architecture, Key Components, Technologies, Data Flow, Team |
| `THE_STORY_OF_THIS_REPO.md` | Year-in-numbers, Contributors, Seasonal Patterns, Themes, Plot Twists, Current Chapter |

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. **Be Specific** — Use actual file names, commit messages, and contributor names.
2. **Evidence-Based** — Support observations with actual git data (never fabricate).
3. **Write files, don't print content** — Use `write_file` to create the actual files.
4. **Balance narrative with technical accuracy** — Make it readable for non-technical audiences.

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona | When to Use |
| ------------- | -------------------------------------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer** | Code review, quality assurance |
| **User** | General purpose, operations |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes


Use for the task described in the Goal section. Follow structured workflow and verify results.

## Best Practices

See [`templates/_shared/best-practices.md`](templates/_shared/best-practices.md) for cross-cutting best practices.

1. **DRY** — Reference shared templates instead of duplicating content.
2. **Structured output** — Use clear sections with consistent heading levels.
3. **Verification gates** — Always verify before claiming completion.
4. **Minimal changes** — Fix root cause, not symptoms.

## Verification Checklist

| # | Gate | Criterion |
| - | ---------- | ----------------------------------- |
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
| -------------------------------- | ----------------------------- |
| `using-superpowers` | Foundational skill workflow |
| `systematic-debugging` | Root cause analysis and fix |
| `git-patch-management` | Patch creation and management |
| `executing-plans` | Execute plans step by step |
| `verification-before-completion` | Validate before claiming done |

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| Server | Purpose |
| --------------------- | ------------------------------------------ |
| `tavily` | Web search + URL extraction (repo context) |
| `github` | GitHub API operations (commit history) |
| `filesystem` | File read/write operations |
| `sequential-thinking` | Structured reasoning for complex problems |
| `ast-grep` | AST-based code search and replace |
| `fetch` | Web page content extraction |
| `playwright` | Browser automation for interactive pages |

## Hooks

The following workspace hooks run around this prompt's execution (see `.github/hooks/README.md`):

| Hook | When | Behavior |
| ------------------------ | ----------------- | ---------------------------- |
| `session-logger` | session start/end | Logs session metadata |
| `governance-audit` | session events | Audits governance compliance |
| `session-auto-commit` | session end | Auto-commits session state |
| `pre-exec-validate.sh` | before commands | Validates command execution |
| `post-exec-state-log.py` | after commands | Appends state log |

## Scripts

- `.github/hooks/*` — Hook implementations listed in the Hooks section

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions

## Related Prompts

Same-family prompts:

- [`repo-init.prompt.md`](repo-init.prompt.md)
- [`repo-management.prompt.md`](repo-management.prompt.md)
- [`repo-research-pipeline.prompt.md`](repo-research-pipeline.prompt.md)
- [`repo-tooling-implementation.prompt.md`](repo-tooling-implementation.prompt.md)
- [`repo.prompt.md`](repo.prompt.md)