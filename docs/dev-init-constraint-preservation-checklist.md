# Dev Init Constraint Preservation Checklist

Date: 2026-05-27
Source Prompt: [Prompts/dev-init.prompts.md](../Prompts/dev-init.prompts.md)

Evidence index: [docs/dev-init-constraint-line-findings.md](dev-init-constraint-line-findings.md)

Use this checklist before and after enhancement or safety-review edits.

## Global Checks

- [ ] Critical constraints are identified before edits.
- [ ] Constraint change log created for each modified prompt.
- [ ] Any removed rule has explicit written rationale.
- [ ] Safety requirements still present after edits.
- [ ] Approval workflow constraints are unchanged.
- [ ] Idempotency expectations remain explicit.

## Per-File Checklist

### 1) [Prompts/agents-fix.prompts.md](../Prompts/agents-fix.prompts.md)

- [ ] Trigger and tags preserved.
- [ ] Goal statements preserved.
- [ ] Required safety sections preserved.
- [ ] No critical instruction removed without rationale.

### 2) [Prompts/bash-scripts-fix.prompts.md](../Prompts/bash-scripts-fix.prompts.md)

- [ ] Trigger and tags preserved.
- [ ] Script migration and cleanup constraints preserved.
- [ ] Safety protocol sections preserved.
- [ ] No critical instruction removed without rationale.

### 3) [Prompts/commands-fix.prompts.md](../Prompts/commands-fix.prompts.md)

- [ ] Trigger and tags preserved.
- [ ] Command validation constraints preserved.
- [ ] Safety and verification sections preserved.
- [ ] No critical instruction removed without rationale.

### 4) [Prompts/dev-init.prompts.md](../Prompts/dev-init.prompts.md)

- [ ] Trigger and tags preserved.
- [ ] Template dependency verification preserved.
- [ ] Constraint preservation audit preserved.
- [ ] No critical instruction removed without rationale.

### 5) [Prompts/general.prompts.md](../Prompts/general.prompts.md)

- [ ] Trigger and tags preserved.
- [ ] Core workflow instructions preserved.
- [ ] Safety and validation sections preserved.
- [ ] No critical instruction removed without rationale.

### 6) [Prompts/repo.prompts.md](../Prompts/repo.prompts.md)

- [ ] Trigger and tags preserved.
- [ ] Repository scope and workflow constraints preserved.
- [ ] Safety and risk controls preserved.
- [ ] No critical instruction removed without rationale.

### 7) [Prompts/skills-fix.prompts.md](../Prompts/skills-fix.prompts.md)

- [ ] Trigger and tags preserved.
- [ ] Skill loading and execution constraints preserved.
- [ ] Safety and verification sections preserved.
- [ ] No critical instruction removed without rationale.

## Constraint Change Log Template

- File: <path>
- Constraint changed: <old wording>
- New wording: <new wording>
- Reason: <why required>
- Risk assessment: <low, medium, high>
- Reviewer: <name>
- Date: <yyyy-mm-dd>
