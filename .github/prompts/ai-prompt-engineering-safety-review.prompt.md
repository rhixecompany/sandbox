---
name: ai-prompt-engineering-safety-review
title: AI Prompt Engineering Safety Review
description: 'Review a prompt for safety, bias, security, clarity, and effectiveness, then produce a safer improved version.'
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - file
  - terminal
scripts: []
skills:
  - prompt-engineering
  - systematic-debugging
  - context-map
formatter: default
plan: None
dependencies:
  - skill:prompt-engineering
  - skill:systematic-debugging
  - skill:context-map
tags:
  - audit
  - frontend
  - ml
  - prompts
  - security
  - typescript
trigger: /ai-prompt-engineering-safety-review
metadata:
  hermes: {}
---
## Goal

Review a prompt for safety, bias, security, clarity, and effectiveness, then produce a safer improved version.

# ai-prompt-engineering-safety-review> Review an input prompt for safety, bias, security, clarity, and effectiveness, then return a stronger version.

## GoalReview an input prompt for safety, bias, security, clarity, and effectiveness, then return a stronger version.

## Context- Use when the user wants a prompt reviewed or improved before reuse- Prefer concrete recommendations over theory- Keep the rewritten prompt aligned with the original intent and required constraints; clarity edits must not remove necessary requirements- Call out safety or security issues explicitly

## Inputs- The original prompt- Optional task context or target domain- Optional constraints, output format, or policy requirements- If no prompt is provided, or if the input is not recognizable as a prompt (for example, raw code, a URL, or plain data), respond with: "No prompt detected. Please provide the prompt text you want reviewed."

## Outputs- A prompt analysis report- A revised prompt- A short checklist of safety and quality improvements

## Rules>> Core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)1. Check harmful content, misinformation, and illegal activity risk first2. Check bias, privacy, and prompt-injection risk3. Assess clarity, specificity, constraints, and output format4. If the prompt's primary purpose is to produce harmful, illegal, or unethical output and no safe rewrite is possible, stop and return only a refusal explaining why the prompt cannot be improved5. Preserve the useful task intent when rewriting6. Add safeguards only when a specific risk was identified in Phase 1 analysis; do not add generic safety disclaimers unrelated to identified risks7. Keep the improved prompt shorter and clearer when possible, but never at the expense of required intent or constraints

## Skills Required> See full table with per-domain purposes:> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)| Skill | Purpose || --- | --- || `context-map` | Preflight mapping for prompt sources, references, and impacted files || `prompt-engineering` | Research-backed prompt optimization patterns (scope analysis, clarity assessment) || `systematic-debugging` | Systematic detection of prompt safety and quality issues (risk detection, bias, clarity checks) |

## Phases>

### Phase 1: Analyze the prompt>> **Goal:** understand what the prompt asks for and where it may fail.> **Full content:** `templates/ai-prompt-engineering-safety-review/phases.md`

## Actions Summary1. Analyze the prompt for safety and quality issues2. Rewrite the prompt to reduce risk and improve clarity3. Validate the revised prompt4. Return the improved prompt and key notes

## Template ReferencesDetailed templates in `templates/ai-prompt-engineering-safety-review/`:- `phases.md`

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

Use when implementing, modifying, or debugging code. Read the codebase first, understand patterns, then apply changes with tests.


## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Read existing code before writing new code.
- Match project conventions and style.
- Add tests for new functionality.

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
|---|------|-----------|
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
|-------|---------|
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


