# Orchestrator Prompt Pattern

## When to Use

When the user asks you to create a prompt that sequentially executes multiple existing prompts/plans, follow this pattern instead of executing them inline. The orchestrator prompt becomes a reusable, self-documenting artifact that can be triggered later.

## Pattern

### Structure

An orchestrator prompt is a `.prompt.md` file with YAML frontmatter and phased workflow that wraps multiple existing prompts.

### Key Elements

1. **Frontmatter**: Include `trigger`, `description`, `tags`, `dependencies`, `skills`, and `metadata.hermes.related_skills`
2. **Rules section**: Explicitly state "strict sequential execution" and "only then" constraints
3. **Phases**: One H3 phase per prompt to execute, each with:
   - Prompt file reference and trigger
   - Goal statement
   - Sub-phases mapping to the target prompt's phases
   - Verification checklist for that prompt
   - "**Only then** proceed to Phase N+1" gate
4. **Verification Checklist (Orchestrator Level)**: Top-level checklist covering all phases
5. **Pitfalls**: Include orchestration-specific pitfalls (skipping phases, stale artifacts, context limits)

### Phase Template

```markdown
### Phase N: [Prompt Name]

**Prompt file:** `prompt-name.prompt.md`
**Trigger:** `/prompt-trigger`

**Goal:** [One-line goal]

**Sub-phases:**
1. **Phase N.1:** [Description]
2. **Phase N.2:** [Description]

**Verification:**
- [ ] [Checklist item 1]
- [ ] [Checklist item 2]

**Only then** proceed to Phase N+1.
```

### Execution Rules

- **Auto-advance**: When the user provides all phases upfront, execute all phases end-to-end without intermediate confirmation. Only pause on critical failure.
- **Progress tracking**: Write progress to `docs/orchestrator-progress.md` after each phase completes
- **Verification artifacts**: Write final verification to `docs/orchestrator-verification.md`
- **Stale artifact check**: Before executing each phase, check if its artifacts already exist (resumability)

## Pitfalls

- **Creating an orchestrator when inline execution suffices**: If the user just wants the prompts executed now, don't create an orchestrator — just execute. Create an orchestrator only when the user explicitly asks for a reusable prompt file.
- **Over-nesting**: Don't create orchestrators of orchestrators. One level of orchestration is enough.
- **Losing phase fidelity**: When mapping sub-phases, preserve the target prompt's phase structure exactly — don't collapse or skip phases.
- **Missing verification gates**: Each phase must have explicit verification before the "only then" gate. Never omit the gate.
