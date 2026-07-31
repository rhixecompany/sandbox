---

name: session-agentsmd-full-workflow

title: Session Agents.md Full Workflow

description: 'Execute the full session workflow: load agent context, read AGENTS.md, apply rules, and report.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

scripts: []

skills:

  - subagent-driven-development

formatter: default

plan: None

dependencies:

  - skill:subagent-driven-development

tags:

  - agents

  - architecture

  - generator

  - git

  - prompts

  - specification

  - typescript

  - workflow

trigger: /session-agentsmd-full-workflow

metadata:

  hermes: {}

---

## Goal

Use when "Comprehensive session workflow for generating AGENTS.md files, committing per project repo, reconciling PR branches, and reporting repo-branch-SHA output" to accomplish the associated tasks and objectives.

## Description

Run a full AGENTS.md generation and git reconciliation workflow across explicitly requested targets in this repository.This prompt is designed to cover all tasks requested in one session:- Generate AGENTS.md for a specific target project folder.
- Repeat generation for each project under projects/.- Perform git add, commit, and push in each project repository.
- Reconcile to consistent PR-ready branch names.
- Output a compact final table with repo, branch, and commit SHA.

## Context

Use this prompt when the user asks for AGENTS.md generation and git automation for one or more subprojects.Expected workspace shape:- projects/ contains multiple project repositories.
- Some projects may already have AGENTS.md.
- The top-level workspace may track projects as nested repos/submodules.Supported target styles:- Single target argument, for example: Bash or Resume_maker.
- Batch target argument, for example: each project in projects/.

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

- Repository discovery and workspace navigation.
- Markdown authoring for AGENTS.md quality guidance.
- Git operations in nested repositories.
- Conflict-safe branch publishing strategies.
- Deterministic reporting and verification.

## Subagents

- Explore: gather read-only context in large workspaces.
- reviewer: optional for final quality checks.Use subagents only when needed for speed or isolation.

## Personas

- Role: Repository Automation Operator.
- Focus: determinism, minimal risk, auditable outputs.
- Style: concise, explicit, execution-first.

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

- Follow the nearest AGENTS.md and repository instructions when present.
- Prefer evidence from local files over assumptions.
- Avoid unrelated edits.
- For AGENTS.md generation:  - include project overview, setup, workflow, testing, style, security, PR guidance, troubleshooting, and monorepo precedence notes.  - keep commands executable and scoped to that project.
- For git operations:  - stage only AGENTS.md for the target repo.  - use one commit message format consistently: docs: add or update AGENTS.md for agent guidance.  - push safely without rewriting remote history.
- If hooks fail due missing local tooling, retry with no-verify and record that decision.
- If push to default branch is rejected, publish a PR-ready branch instead.
- Normalize PR branch names consistently:  - chore/agentsmd-YYYYMMDD-<repo>
- Always end with a compact table:  - repo | branch | commit SHA.
- Report blockers clearly and provide the safest fallback.

## Phases

### Phase 2: Generate AGENTS

### Phase 3: Git Commit and Push

## Steps

1. Resolve target scope from user input.
2. Enumerate in-scope directories and detect which are git repositories.
3. For each target project, inspect local manifests and README.
4. Create or update AGENTS.md with project-specific guidance.
5. Run markdown diagnostics for changed AGENTS.md files where available.
6. In each target repo, run git add AGENTS.md.
7. Commit with the standard message.
8. Push to a PR-ready normalized branch name.
9. Verify remote branch SHA for each push.
1
10. Emit final compact table and blocker notes.

## Tasks

- Task 1.1 — Discover and validate requested targets.
- Task 1.2 — Collect command and stack evidence per target.
- Task 2.1 — Generate or update AGENTS.md for each target.
- Task 2.2 — Validate markdown diagnostics and fix issues.
- Task 3.1 — Stage and commit AGENTS.md per target repo.
- Task 3.2 — Push commits to normalized PR branches.
- Task 4.1 — Reconcile branch naming consistency across repos.
- Task 4.2 — Verify remote refs and compile final table.

## Subtasks

- Subtask 1.1.1 — Expand argument shortcuts into concrete directories.
- Subtask 1.1.2 — Separate git repos from non-repo folders.
- Subtask 1.2.1 — Read package manager and script data from manifests.
- Subtask 1.2.2 — Read README for execution and troubleshooting context.
- Subtask 2.1.1 — Apply AGENTS.md structure with project-specific commands.
- Subtask 2.1.2 — Preserve existing useful project guidance when present.
- Subtask 2.2.1 — Run diagnostics and correct markdown structure issues.
- Subtask 3.1.1 — Stage only AGENTS.md to avoid unrelated changes.
- Subtask 3.1.2 — Retry commit with no-verify when local hooks are unavailable.
- Subtask 3.2.1 — Push commit SHA to branch chore/agentsmd-YYYYMMDD-<repo

> .- Subtask 3.2.2 — If history is oversized or push fails, use a clean clone fallback branch publish.
- Subtask 4.1.1 — Check remote branch existence and SHA match.
- Subtask 4.2.1 — Output compact table sorted by repo name.

## Actions Summary

- Discover targets and repository boundaries.
- Generate AGENTS.md in requested targets.
- Stage, commit, and push AGENTS.md changes in each target repo.
- Normalize PR-ready branch naming.
- Verify remote commit SHAs.
- Return compact repo-branch-SHA table with exceptions.

## Template References

Detailed templates in `templates/session-agentsmd-full-workflow/`:- `phases.md`

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

