---

name: projects-init

title: Projects Init

description: 'Three-phase workspace initialization: triage MD documentation files, migrate prompt files to prompts/, then create skills/scripts and update prompts. Eliminates duplicates and consolidates documentation.'

version: 1.0.0

license: MIT

author: Hermes Agent

toolsets:

  - file

  - terminal

scripts: []

skills:

  - enhance-markdown

  - hermes-skills

  - skill-creator

formatter: default

plan: None

dependencies:

  - skill:enhance-markdown

  - skill:hermes-skills

  - skill:skill-creator

tags:

  - debugging

  - documentation

  - git

  - markdown

  - migration

  - prompts

  - skills

  - typescript

trigger: /projects-init

metadata:

  hermes: None

  related_skills:

    - enhance-markdown

    - hermes-skills

    - skill-creator

---

## Goal

Three-phase workspace initialization: triage MD documentation files, migrate prompt files to prompts/, then create skills/scripts and update prompts. Eliminates duplicates and consolidates documentation.

# Projects Init> Initialize a workspace: triage docs, migrate prompts, create skills. Three sequential phases — each must finish before the next begins.

## Description

This prompt initialises a new or stale workspace by running a three-phase cleanup and consolidation pipeline. Phase 1 discovers and deduplicates all markdown documentation files. Phase 2 discovers prompt files, migrates them to `.github/prompts/`, and consolidates. Phase 3 indexes the new prompt directory, creates any needed skills and helper scripts, and updates all prompts to reference the skills they need.**Critical rules (must appear within the first 15% of execution):**- **Only then constraint** — Each phase completes fully before the next begins. No overlapping phases.- **Delete only after verification** — Before deleting any file, confirm the canonical copy exists in the target location.- **Count before and after** — Record file counts at each phase start and end; report deltas.

## Context

- **Source reference:** `projects-init.prompt.txt` (raw specification)
- **Target scope:** `pwd` (workspace root), `docs/`, `.github/prompts/`
- **Phase 1 outputs:** Consolidated markdown documentation inventory + deleted duplicates
- **Phase 2 outputs:** Prompt files migrated to `.github/prompts/` + deleted originals
- **Phase 3 outputs:** New skills/scripts in `~/AppData/Local/hermes/skills/` + updated prompt frontmatter
- **Execution environment:** Windows 11, bash (git-bash/MSYS), Hermes CLI

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill              | Purpose                                                 |
| ------------------ | ------------------------------------------------------- |
| `enhance-markdown` | Audit, enhance, convert, and consolidate markdown files |
| `hermes-skills`    | List, create, install, and manage skills                |
| `skill-creator`    | Scaffold new skills with validated frontmatter          |

## Rules

> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

1. **Strict sequential execution** — Phase 1 → Phase 2 → Phase 3. Each phase must complete (including verification) before the next starts.
2. **Verify before delete** — Always confirm the canonical copy exists at the target path before removing a source file.
3. **Count and report** — Log file counts before and after each phase. Report deltas in the phase summary.
4. **No destructive operations without confirmation** — For `rm` operations over 3+ files, show the list and ask before executing.

## Phases

## Phase 1: Triage Documentation

> **Goal:** Inventory all markdown documentation files, identify duplicates, conso
> **Inputs:** `pwd`, `docs/**` (and subdirectories)
> **Full content:**

## Phase 2: Migrate Prompts

> **Goal:** Discover all markdown prompt files, migrate them to `.github/prompts/`
> **Inputs:** `pwd`, `.github/prompts/` (if exists)
> **Full content:**

## Phase 3: Create Skills & Update

> **Goal:** Scan `.github/prompts/`, identify needed skills and scripts, create th
> **Inputs:** `.github/prompts/**`
> **Full content:**

## Actions Summary

1. List and triage all markdown documentation files in `pwd` and `docs/**`; consolidate and delete duplicates
2. List and triage all markdown prompt files in `pwd` and `.github/prompts/`; migrate prompts to `.github/prompts/`; consolidate; delete originals
3. List and triage the migrated `.github/prompts/` collection; create all needed skills and scripts; update all prompts with accurate skill references

## Template References

Detailed templates in `templates/projects-init/`:

## Template References

Templates in `templates/projects-init/`:- `actions_summary.md`- `context.md`- `description.md`- `phase_1_triage_documentat.md`- `phase_2_migrate_prompts.md`- `phase_3_create_skills__up.md`- `rules.md`- `skills_required.md`

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

## Context

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
4. **Report blockers** — State clearly when something fails.

## Phases

### Phase 1: Intake

- Read the request and identify scope.
- Locate relevant files, diffs, references.

### Phase 2: Execute

- Perform work with smallest safe change set.
- Keep steps explicit and reproducible.

### Phase 3: Verify

- Check result against goal, rules, inputs.
- Confirm output is usable and complete.

### Phase 4: Hand Off

- Return final artifact or findings clearly.
- Stop once the requested result is delivered.

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
