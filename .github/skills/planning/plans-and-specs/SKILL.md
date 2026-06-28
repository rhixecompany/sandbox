---
name: plans-and-specs
title: Plans And Specs
description: "Use when drafting implementation plans, specs, and decomposition for features. Create plans, roadmaps, break down work into steps, document specs and requirements, link requirements to plans, and mark work complete."
version: 1.1.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags:
      - planning
      - specs
      - decomposition
    related_skills:
      - brainstorming
      - prompt-planning-orchestration
      - executing-plans
---

# Plans And Specs

## Goal
Draft implementation plans, specs, and feature decomposition. Produce phased plans with linked specifications, progress tracking, and completion verification.

## Subgoals
1. **Plan** — Define plan name, phases, tasks, dependencies
2. **Spec** — Document requirements, acceptance criteria, link to plan
3. **Execute** — Work through phases sequentially, track progress
4. **Complete** — Verify all tasks done, document lessons learned

## Personas
| Persona | When to Use |
|---------|-------------|
| **Project Manager** | Creating roadmaps, tracking progress |
| **Tech Lead** | Breaking down features, defining specs |
| **Developer** | Executing plan tasks |
| **QA** | Verifying acceptance criteria |

## Personality & Tone
- **Tone**: Structured, methodical, clear
- **Style**: Phased approach with explicit dependencies and acceptance criteria
- **Avoid**: Vague plans without measurable outcomes, skipping verification
- **Encourage**: Small batches, clear ownership, documented decisions

## Profile Selection
| Task Type | Recommended Profile |
|-----------|---------------------|
| Feature planning | `exec-assistant` |
| Technical specs | `code-architect` |
| Research planning | `research-analyst` |
| Creative planning | `creative-director` |
| General purpose | `default` |

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
- Exploratory projects (use `brainstorming` first)

## Skills Required
| Skill | Purpose |
|-------|---------|
| `brainstorming` | Explore options before planning |
| `executing-plans` | Execute written plans |
| `writing-plans` | Document plans in markdown |
| `verification-before-completion` | Structured plan-execution cross-referencing |

## Workflow

### Phase 1: Create Plan
- Define plan name and description
- Identify phases or batches
- List all tasks
- Define dependencies
- **SandBox usage:** Use for Bash/script consolidation, GitHub workflow orchestration, or projects/*/PLAN.md decomposition

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
- Verify all tasks done — use `verification-before-completion` skill
- Update plan status
- Archive completed work
- Document lessons learned
- **SandBox usage:** Confirm test suite passes, then commit to git with tag

## Class Patterns

Detailed class pattern documentation has been moved to reference files to keep this SKILL.md concise:

- **Prompt File Conversion**: See `references/prompt-file-conversion.md`
- **Multi-Language Script Projects**: See `references/multi-language-script-projects.md`
- **Multi-Target Execution**: See `references/multi-target-execution-pattern.md`
- **Multi-Group Skill Library Consolidation**: See `references/skill-library-consolidation.md`
- **Cross-Platform Agent Inventory**: See `references/cross-platform-agent-inventory.md`
- **Multi-Phase Workflow Maintenance**: See `references/workflow-phase-maintenance.md`
- **Development Implementation Manager (dev-imp)**: See `references/dev-imp-pattern.md`

## Pitfalls
- **No specs**: Plans without linked specs lead to ambiguous acceptance criteria
- **Over-planning**: Don't plan every detail upfront; iterate as you learn
- **Missing dependencies**: Always document task dependencies to avoid blockers
- **No verification**: Always verify completion before marking done
- **Stale plans**: Update plans regularly; a stale plan is worse than no plan
- **Over-length SKILL.md**: Detailed patterns belong in `references/`, not inline
- **read_file dedup blocking**: The `read_file` tool blocks repeated reads of unchanged files. When you need to re-inspect a file after edits, use `terminal` + `python3` or `grep` to extract specific sections. Do NOT loop on `read_file` for the same path — it will fail after 3-4 calls.

## Best Practices
- Create detailed plans before starting
- Link specs to plan tasks
- Update plan regularly
- Track progress clearly
- Document decisions
- Archive completed plans

## Verification Checklist

- [ ] Plan name, phases, and tasks are clearly defined
- [ ] Each task has a linked specification with acceptance criteria
- [ ] Progress is being tracked against the plan
- [ ] Completion verification has been performed
- [ ] Lessons learned are documented after completion
- [ ] SKILL.md is under 250 lines (move detail to references/)
