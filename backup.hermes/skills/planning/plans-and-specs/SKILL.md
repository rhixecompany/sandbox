---
category: planning
title: Plans And Specs
name: plans-and-specs
description: Use when drafting implementation plans, specs, and decomposition for features.
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags:
      - imported
      - priority
    related_skills: []
---## Goal
drafting implementation plans, specs, and decomposition for features. to accomplish the associated tasks and objectives.


# Plans And Specs

## Description

Detailed instructions for using planning tools. Create plans, roadmaps, break down work into steps, document specs and requirements, link requirements to plans, and mark work complete.

## When to Use

- Creating plans or roadmaps
- Breaking down work into steps
- Documenting specs or requirements
- Linking requirements to plans
- Marking work as complete
- Planning multi-phase projects
- Organizing complex tasks

## When NOT to Use

- Simple single-task work
- Real-time task management
- Non-structured work
- Exploratory projects

## Workflow

### Phase 1: Create Plan

- Define plan name and description
- Identify phases or batches
- List all tasks
- Define dependencies
- **SandBox usage:** Use for Bash/ script consolidation, GitHub workflow orchestration, or projects/*/PLAN.md decomposition

### Phase 2: Create Specs

- Document requirements
- Define acceptance criteria
- Link specs to plan
- Verify completeness
- **SandBox usage:** Reference `.github/instructions/` for project-specific spec templates

### Phase 3: Execute Plan

- Work through phases sequentially
- Track progress
- Update plan as needed
- Document decisions
- **SandBox usage:** Follow the 6-phase execution model for multi-language projects; run validation gates from Bash/package.json

### Phase 4: Mark Complete

- Verify all tasks done — use `verification-before-completion` skill for structured plan-execution cross-referencing
- Update plan status
- Archive completed work
- Document lessons learned
- **SandBox usage:** Confirm test suite passes (`bash test-all.sh` from Bash/), then commit to git with tag

---

## Prompt File Conversion (Class Pattern)

For projects that maintain `.prompt.md` files (Copilot/Hermes/OpenCode prompts) and need to convert plaintext `.txt` drafts into properly formatted prompt files:

### 4-Phase Conversion Model

1. **INVENTORY** — Catalog all `.txt` sources and existing `.prompt.md` targets; identify which are plaintext vs. already formatted
2. **STRUCTURE** — For each plaintext source, produce a formatted `.prompt.md` with:
   - YAML frontmatter (`title`, `trigger`, `tags`)
   - `## Skills Required` table (skill name + purpose)
   - Phased workflow (`Phase 1..N` with steps and verification)
   - `## Description` / `## Goal` / `## Overview` narrative sections
3. **FORMAT & CONSISTENCY** — Apply uniform header levels, list style, code-block annotations, and verification checklists across all files in the batch
4. **VERIFY** — Confirm frontmatter validity, section completeness, and cross-reference consistency

### File Convention

```
target-path/
├── my-prompt.prompts.txt         # Plaintext source (short-form)
├── my-prompt.prompts.md          # Formatted output (frontmatter + phases)
└── .github/prompts/task.prompt.md  # Production prompt (full .prompt.md spec)
```

### Key Patterns

- **Frontmatter first**: Every `.prompt.md` must open with `---` delimited YAML (title, trigger, tags). See `references/prompt-file-conventions.md`.
- **Trigger match**: The `trigger: /name` in frontmatter should match the filename stem.
- **Skills Required**: Always present as a markdown table with Skill and Purpose columns.
- **Phased structure**: Use `Phase N: Title` with numbered steps or sub-tables.
- **Verification checklist**: Close every prompt file with a bullet checklist of acceptance criteria.

See `references/prompt-file-conventions.md` for the frontmatter template, section templates, and real file-name conventions used in the SandBox repo.

## Multi-Language Script Projects (Class Pattern)

For projects consolidating scripts across shell, PowerShell, batch, and shared implementations:

### 6-Phase Execution Model

1. **AUDIT & INVENTORY** — Catalog all scripts, identify issues, verify dependencies
2. **DEBUG & FIX** — Resolve all issues found in Phase 1 (fix imports, missing steps, timeout bugs)
3. **CONSOLIDATION** — Centralize logic (src/*.ts), standardize wrappers, enforce DRY
4. **ENHANCEMENT** — Document flags, environment variables, logging, exit codes
5. **EXECUTE & TEST** — Automated test suite (test-all.sh), 100% pass rate gate
6. **DOCUMENTATION** — PLAN.md, SPECS.md, README.md, SUMMARY.md, test suite

### Deliverables Structure

```
project/
├── PLAN.md          What needs to be done (phases, timeline, risks)
├── SPECS.md         How to build it (requirements, acceptance criteria per script)
├── README.md        How to use it (quick start, flags, examples, troubleshooting)
├── SUMMARY.md       Completion report (what was done, test results, metrics)
├── test-all.sh      Automated test suite (run all scripts with --help, verify exit codes)
├── src/             TypeScript implementations (single source of truth)
└── logs/            Auto-created log directory (./logs/, timestamped files)
```

## Multi-Target Execution Pattern

When a scope definition (e.g., a `.prompts.md` file) lists multiple distinct targets to process, use this pattern for systematic end-to-end execution:

> Reference: `references/multi-target-execution-pattern.md` for the general pattern, and `references/repo-management-workflow.md` for repo-inventory / branch-normalization work.

### Multi-Repo Management Prompt Pattern

Use this when a prompt drives work across many repositories (inventory, normalize, audit, cross-reference, then document):

1. Read the prompt file first and extract its phase order.
2. Verify live system state before planning.
3. Pick the Hermes profile that matches the task class instead of defaulting blindly.
4. Inventory repositories from live git state, not from stale docs.
5. Write a snapshot doc before deeper mutations so later phases have a stable baseline.

### 5-Phase Execution Model

1. **BRAINSTORM & PLAN** — Load required skills (brainstorming, plans-and-specs). Create a single comprehensive plan document at `docs/{task}-comprehensive-plan.md` with:
   - Per-target spec (purpose, path, acceptance criteria)
   - File references for each target
   - Cross-reference matrix showing relationships between targets

2. **PER-TARGET EXECUTION** — For each target in defined order: load current state, apply transformations, check per-target AC, flag discrepancies.

3. **SWEEP VERIFICATION** — After all targets processed, run a cross-reference sweep: verify ALL targets have complete frontmatter (`---`, `trigger:`, `description:`, `tags:`, `dependencies:`, `skills:`). Common gap: files using `title:` instead of `description:`.

4. **FIX GAPS** — Patch discrepancies found during sweep before commit.

5. **COMMIT & REPORT** — One commit per cycle. Summary table of targets, status, files changed.

### Acceptance Criteria Template

| Criterion | Check |
|-----------|-------|
| YAML frontmatter (`---` ... `---`) | `head -1` contains `---` |
| `trigger:` field | `head -10 | grep trigger:` |
| `description:` field | `head -10 | grep description:` |
| `tags:` field | `head -10 | grep tags:` |
| `dependencies:` field | `head -20 | grep dependencies:` |
| `skills:` field | `head -20 | grep skills:` |
| Source fidelity | Derived file size >= source (formatting adds structure) |

### Multi-Phase Workflow Document Maintenance

When a driving `.prompts.md` or `PLAN.md` has a structured phase list and you need to add, remove, or reorder phases, every cross-reference section that enumerates phases must be updated in the **same pass** — not a follow-up sweep. The following sections are interdependent in a well-structured workflow document:

**Cross-reference sections that must stay in sync:**

| Section | What to update |
|---------|---------------|
| Frontmatter `description:` | Bump phase counts, add new priorities |
| Frontmatter `tags:` | Add new domain tags (e.g. `bun`, `ci`, `dependency-management`) |
| Frontmatter `dependencies:` / `skills:` | Add skills needed by new phases |
| Top-level summary | Renumber priorities, extend text |
| Priority tiers table | Insert new tiers, renumber subsequent |
| Phase sections (the body) | Insert new `### Phase N:` blocks |
| Skill cross-reference table | Add rows for each new phase |
| Verification gate script | Add checks for new phase deliverables |
| Pitfalls list | Add phase-specific pitfalls |
| Actions list | Add tool/skill refs needed by new phases |

**Rule:** If you add a phase but miss any of the above, the document becomes self-contradictory. The reader (or future agent) will see a phase in the body but no cross-ref entry, or a verification gate that doesn't test the new phase's outputs.

**Phase ordering rule:** Per-repo optimization/debt work (dependency audit, tool migration, CI setup) must come BEFORE consolidation/merge phases. Clean sources first, then combine. If you add phases that improve individual repos, insert them after the categorization phase but before the consolidation phase.

**Duplicate detection:** Before closing a multi-phase document edit, always check the tail of the file for orphaned duplicate sections. Files that have been edited across multiple sessions accumulate stale code blocks, repeated sections, or unclosed fences. A `tail -50` scan and a `grep -c '\`\`\`'` parity check catches these.

See `references/workflow-prompt-phase-maintenance.md` for the worked example (adding dep audit + bun migration + CI workflow phases to a 14-repo management prompt).

## Cross-Platform Agent Inventory (Class Pattern)

For environments with multiple AI coding platforms (Copilot, Hermes, OpenCode, Claude Code, Codex) where agent definitions need to be discovered, audited, and cross-referenced:

### 5-Phase Inventory Model

1. **DISCOVER** — For each platform, locate agent definitions:
   - **Copilot**: Per-repo agent definitions (`.agent.md` files in the `.github/agents/` directory)
   - **Hermes**: Profile list via `hermes profile list`; profiles are model+setting bundles, not logic agents
   - **OpenCode**: Agent definitions in the user's global config directory under `agents/`
   - **Claude Code**: Project-local setup files referencing agent behaviors
   - **Codex**: Project-local prompt config files
2. **INVENTORY** — Per platform, document: agent name, format, file path, purpose, tools/permissions, model, mode (primary/subagent/profile)
3. **CROSS-REFERENCE** — Map agents by function across platforms (e.g., architecture agent → code-architect profile → OpenCoder primary). Identify which functions are covered by each platform vs. gaps.
4. **AUDIT INCONSISTENCIES** — Check for: missing cross-references, divergent naming conventions, format differences, undocumented agents, stale agents
5. **FIX & DOCUMENT** — Create cross-reference document (e.g., `docs/agents-cross-reference.md`), update platform instructions to mention peer agents, recommend gap closures

### Inventory Template

| Platform | Agent | Format | File | Purpose | Cross-Ref |
|----------|-------|--------|------|---------|-----------|
| Copilot | `architect` | `.agent.md` | `.github/agents/` | Architecture planning | → Hermes: code-architect → OpenCode: OpenCoder |

### Pitfalls

- Global config files may be absent in the project root — check user home config directory for global config
- Agent file patterns differ: Copilot uses `.agent.md`, OpenCode uses `.md`, Codex uses `.prompt.md`, Hermes uses hierarchical YAML profile configs
- Some OpenCode agents use `mode: primary`, others use `mode: subagent` — this affects discoverability
- Hermes plugins may disable a provider plugin even when the active profile uses it — the session may bypass the gateway

See `references/agents-cross-reference-worked-example.md` for the full worked example from SandBox (Copilot × Hermes × OpenCode, 27 agents, 7 profiles, 4 inconsistencies found).

## Tools & References

- **Related Skills**: writing-plans, executing-plans
- **Worked Example**: See `references/multi-target-execution-pattern.md` for multi-target prompt library standardization (8 targets, frontmatter sweep)
- **Worked Example (Scripts)**: See `references/sandbox-bash-worked-example.md` for multi-language script consolidation case study
- **Worked Example (Agents)**: See `references/agents-cross-reference-worked-example.md` for cross-platform agent inventory (3 platforms, 27 agents mapped)
- **Plan Format**: Markdown with clear structure
- **Specs**: Linked to plan tasks
- **Tracking**: Status and progress

## Best Practices

- Create detailed plans before starting
- Link specs to plan tasks
- Update plan regularly
- Track progress clearly
- Document decisions
- Archive completed plans
- Share plans with team

## Overview

Planning and specification skill for structured project decomposition. Guides creation of phased plans with linked specifications, progress tracking, and completion verification to ensure organized execution.

## Verification Checklist

- [ ] Plan name, phases, and tasks are clearly defined
- [ ] Each task has a linked specification with acceptance criteria
- [ ] Progress is being tracked against the plan
- [ ] Completion verification has been performed
- [ ] Lessons learned are documented after completion
