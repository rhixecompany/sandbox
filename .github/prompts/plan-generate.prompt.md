---
name: plan-generate
title: Generate Implementation Plan
description: Generate a detailed, structured implementation plan from a goal or specification.
  Produces a phased plan with dependencies, references, and verification gates. Replaces
  ad-hoc plan-* prompts (debugger, features-seed, updateAiAgentSetupPrompt, etc.)
  with a single reusable generator.
version: 1.0.0
license: MIT
author: Hermes Agent (consolidated)
toolsets:
  - file
  - terminal
scripts: []
skills:
  - plans-and-specs
  - writing-plans
  - simplify
  - brainstorming
  - systematic-debugging
  - verification-before-completion
formatter: default
plan: ''
dependencies:
  - skill:plans-and-specs
  - skill:writing-plans
  - skill:simplify
  - skill:brainstorming
  - skill:systematic-debugging
  - skill:verification-before-completion
  - prompt:context-map.prompt.md
tags:
  - ai-assistant
  - generator
  - ml
  - planning
  - prompts
  - specification
  - ai-assistant
  - generator
  - ml
  - planning
  - prompts
  - specification
  - typescript
trigger: /plan-generate
---

> **Shared template references:**>> - [Frontmatter patterns](templates/_shared/frontmatter.md)> - [Core rules](templates/_shared/rules-core.md)> - [Section skeleton](templates/_shared/section-skeleton.md)> - [Verification checklist](templates/_shared/verification-checklist.md)## GoalGenerate a complete, phased implementation plan from a high-level goal or specification. The output is a self-contained `.prompt.md` file (or an `.hermes/plans/` plan document) that can be loaded and executed by `plan-execute`.## Core RulesSee [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md).Additional plan-specific rules:1. **Phases must be sequential** — Each phase must complete before the next begins.2. **Each phase has a verification gate** — Explicit checks that phase is done.3. **Dependencies are explicit** — Every skill, prompt, and tool referenced must exist.4. **DRY output** — Generated plans reference shared templates where possible.5. **One plan = one goal** — Never combine unrelated goals into a single plan.## Workflow### Phase 1: Context gathering1. Read the user's goal/specification.2. Run `context-map` (prompt) to identify impacted files, dependencies, and scope.3. Use `brainstorming` to explore approach options.4. Use `systematic-debugging` to identify edge cases and risks.### Phase 2: Plan structureGenerate a plan with these sections:```markdown## GoalConcise statement of what this plan achieves.## Inputs- Files, APIs, data sources the plan consumes## Outputs- Files, reports, artifacts the plan produces## Phases### Phase N: <Name>**Gate:** <condition that confirms completion>**Dependencies:** <prior phases or external deps>**Steps:**1. <action>2. <action>3. Verify: <validation step>## Verification Checklist- [ ] All phases completed- [ ] All outputs verified- [ ] No orphaned references```### Phase 3: Write1. Create the plan file at `.github/prompts/<name>.prompt.md` or `.hermes/plans/<name>.md`.2. Use `writing-plans` skill for structured plan writing.3. Apply `simplify` to remove redundancy.### Phase 4: Verify1. Run the verification checklist below.2. Confirm all referenced skills/prompts/tools exist.3. If the plan targets `.github/prompts/*.prompt.md`, validate frontmatter.4. Run the plan through `dry_run_prompts.py` for smoke-testing.## Verification Checklist- [ ] Goal is clearly stated and scoped- [ ] All phases have explicit verification gates- [ ] Every `skill:`, `prompt:`, `tool:` reference resolves to an existing asset- [ ] Plan is self-contained (no missing context)- [ ] Phase ordering is logical (no circular dependencies)- [ ] DRY: no duplicated content that belongs in `_shared/`- [ ] If `.prompt.md` output: frontmatter has `name`, `title`, `version`, `description`, `tags`