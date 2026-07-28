---
name: create-technical-spike
title: Create Technical Spike Document
description: Create time-boxed technical spike documents for researching and resolving critical development decisions before implementation.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets:
  - web
scripts: []
skills: []
formatter: default
plan: None
tags:
  - architecture
  - generator
  - prompts
  - specification
  - typescript
trigger: /create-technical-spike
dependencies: []
metadata:
  hermes: {}
---
## Goal

Create time-boxed technical spike documents for researching and resolving critical development decisions before implementation.

title: "${input:SpikeTitle}"category: "${input:Category|Technical}"status: "🔴 Not Started"priority: "${input:Priority|High}"timebox: "${input:Timebox|1 week}"created: [YYYY-MM-DD]updated: [YYYY-MM-DD]owner: "${input:Owner}"---# ${input:SpikeTitle}

## Summary**Spike Objective:** [Clear, specific question or decision that needs resolution]**Why This Matters:** [Impact on development/architecture decisions]**Timebox:** [How much time allocated to this spike]**Decision Deadline:** [When this must be resolved to avoid blocking development]

## Research Question(s)**Primary Question:** [Main technical question that needs answering]**Secondary Questions:**- [Related question 1]- [Related question 2]- [Related question 3]

## Investigation Plan

### Research Tasks- [ ] [Specific research task 1]- [ ] [Specific research task 2]- [ ] [Specific research task 3]- [ ] [Create proof of concept/prototype]- [ ] [Document findings and recommendations]

### Success Criteria**This spike is complete when:**- [ ] [Specific criteria 1]- [ ] [Specific criteria 2]- [ ] [Clear recommendation documented]- [ ] [Proof of concept completed (if applicable)]

## Technical Context**Related Components:** [List system components affected by this decision]**Dependencies:** [What other spikes or decisions depend on resolving this]**Constraints:** [Known limitations or requirements that affect the solution]

## Research Findings

### Investigation Results[Document research findings, test results, and evidence gathered]

### Prototype/Testing Notes[Results from any prototypes, spikes, or technical experiments]

### External Resources- [Link to relevant documentation]- [Link to API references]- [Link to community discussions]- [Link to examples/tutorials]

## Decision

### Recommendation[Clear recommendation based on research findings]

### Rationale[Why this approach was chosen over alternatives]

### Implementation Notes[Key considerations for implementation]

### Follow-up Actions- [ ] [Action item 1]- [ ] [Action item 2]- [ ] [Update architecture documents]- [ ] [Create implementation tasks]

## Status History| Date   | Status         | Notes                    || ------ | -------------- | ------------------------ || [Date] | 🔴 Not Started | Spike created and scoped || [Date] | 🟡 In Progress | Research commenced       || [Date] | 🟢 Complete    | [Resolution summary]     |---_Last updated: [Date] by [Name]_```

## Categories for Technical Spikes> - Third-party API capabilities and limitations> - Integration patterns and authentication> **Full content:** `templates/create-technical-spike/categories_for_technical_spike.md`

## File Naming ConventionsUse descriptive, kebab-case names that indicate the category and specific unknown:**API/Integration Examples:**- `api-copilot-chat-integration-spike.md`- `api-azure-speech-realtime-spike.md`- `api-vscode-extension-capabilities-spike.md`**Performance Examples:**- `performance-audio-processing-latency-spike.md`- `performance-extension-host-limitations-spike.md`- `performance-webrtc-reliability-spike.md`**Architecture Examples:**- `architecture-voice-pipeline-design-spike.md`- `architecture-state-management-spike.md`- `architecture-error-handling-strategy-spike.md`

## Best Practices for AI Agents1. **One Question Per Spike:** Each document focuses on a single technical decision or research question2. **Time-Boxed Research:** Define specific time limits and deliverables for each spike3. **Evidence-Based Decisions:** Require concrete evidence (tests, prototypes, documentation) before marking as complete4. **Clear Recommendations:** Document specific recommendations and rationale for implementation5. **Dependency Tracking:** Identify how spikes relate to each other and impact project decisions6. **Outcome-Focused:** Every spike must result in an actionable decision or recommendation

## Research Strategy

### Phase 1: Information Gathering1. **Search existing documentation** using search/fetch tools2. **Analyze codebase** for existing patterns and constraints3. **Research external resources** (APIs, libraries, examples)

### Phase 2: Validation & Testing1. **Create focused prototypes** to test specific hypotheses2. **Run targeted experiments** to validate assumptions3. **Document test results** with supporting evidence

### Phase 3: Decision & Documentation1. **Synthesize findings** into clear recommendations2. **Document implementation guidance** for development team3. **Create follow-up tasks** for implementation

## Tools Usage- **search/searchResults:** Research existing solutions and documentation- **fetch/githubRepo:** Analyze external APIs, libraries, and examples- **codebase:** Understand existing system constraints and patterns- **runTasks:** Execute prototypes and validation tests- **editFiles:** Update research progress and findings- **vscodeAPI:** Test VS Code extension capabilities and limitationsFocus on time-boxed research that resolves critical technical decisions and unblocks development progress.

## Template ReferencesDetailed templates in `templates/create-technical-spike/`:- `categories_for_technical_spike.md`

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


