---
trigger: plan-execute
name: plan-execute
title: "Execute Implementation Plan"
description: >
  Load and execute any implementation plan step-by-step. Reads the plan
  from a `.prompt.md` or `.md` file, runs each phase sequentially with
  verification gates. Replaces all ad-hoc execute-plan-* prompts with a
  single generic executor.
version: 1.0.0
author: "Hermes Agent (consolidated)"
license: MIT
tags:
  - execution
  - automation
  - hermes
  - prompts
  - plan
  - dry
dependencies:
  - skill:plans-and-specs
  - skill:subagent-driven-development
  - skill:verification-before-completion
  - skill:writing-plans
  - tool:terminal
  - tool:search_files
skills:
  - plans-and-specs
  - subagent-driven-development
  - verification-before-completion
  - writing-plans
metadata:
  hermes:
    related_skills: []
    tags:
    - plan-execute.prompt

---


## Actions

- Follow the prompt workflow as specified.
- Produce the requested deliverable(s) in the exact structure requested.
- Validate output against acceptance criteria before finishing.
metadata:
  hermes:
    related_skills: []
    tags:
    - plan-execute.promptmetadata:
  hermes:
    related_skills: []
    tags:
    - plan-execute.prompt

> **Shared template references:**
> - [Core rules](../prompts/templates/_shared/rules-core.md)
> - [Section skeleton](../prompts/templates/_shared/section-skeleton.md)
> - [Verification checklist](../prompts/templates/_shared/verification-checklist.md)

## Goal

Execute a structured implementation plan from start to finish. Load the plan file, process each phase in order with verification gates, and report completion or blockers.

**Consolidates:** All previous `execute-plan-*` and `execute-*plan*` prompts
(comicwise-session, debugger, eslint, optimization, setup, skills-debug,
acpx-agent-integration, bash-scripts-plan, dev-init, docs, hermes-config,
orchestrator, per-repo, prompt-conversion, sandbox-projects-merge, etc.)

## Input

- **Plan file path** — e.g. `prompts/plan-xxx.prompt.md` or `.hermes/plans/xxx.md`
- **Optional overrides** — phase to start from, env vars, profile selections

## Core Rules

See [`prompts/templates/_shared/rules-core.md`](../prompts/templates/_shared/rules-core.md).

Additional execution-specific rules:

1. **Strict sequential** — Never skip ahead. Complete each phase, verify its gate, then proceed.
2. **No silent failures** — If a phase fails, stop and report before retrying or continuing.
3. **Git checkpoint per phase** — After each successful phase, `git add && git commit` with descriptive message.
4. **Idempotent phases** — Each phase should be safe to re-run if it fails mid-way.
5. **Plan is read-only** — Never modify the plan file during execution; log progress separately.

## Workflow

### Phase 1: Load plan
1. Read the plan file (`read_file`).
2. Parse phases, gates, dependencies, and outputs.
3. Verify all referenced skills/prompts/tools exist.
4. Write session start marker to `.hermes/plans/docs/<plan-name>-progress.md`.

### Phase 2: Execute phases
For each phase in order:

1. **Pre-check** — Confirm verification gate from previous phase is met.
2. **Execute** — Run the steps using appropriate tools.
3. **Verify** — Run the phase's verification gate explicitly.
4. **Checkpoint** — `git add -A && git commit -m "feat(plan): <plan-name> phase <N>: <name>"`
5. **Log** — Update progress doc with phase result.

### Phase 3: Final verification
1. Run the plan's full verification checklist.
2. Confirm all outputs exist and match expected format.
3. Write session summary to progress doc.

### Phase 4: Report
Summarise:
- Phases completed / total
- Any skipped phases and why
- All verification gates passed
- Outputs produced
- Git commit SHAs for each phase

## Verification Checklist
- [ ] Plan loaded and parsed successfully
- [ ] All phase dependencies resolved
- [ ] Each phase executed in strict order
- [ ] Verification gate passed for every phase
- [ ] Git checkpoint committed after each phase
- [ ] No dangling processes or background jobs
- [ ] All expected outputs exist and are valid
- [ ] Progress doc written with complete trail

## Hooks

- Wire this prompt into a `only then` execution chain when appropriate.
