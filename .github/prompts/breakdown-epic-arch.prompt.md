---
agent: "agent"
description: "Prompt for creating the high-level technical architecture for an Epic, based on a Product Requirements Document."
---

## Goal

Prompt for creating the high-level technical architecture for an Epic, based on a Product Requirements Document.

## Context

Use when you need to work on the current workspace or task.

## Inputs

- The current workspace, repo, or document state.
- The specific request, diff, spec, or files provided by the user.
- Any prompt variables, paths, or constraints named in the original instructions.

## Outputs

- A complete result that matches the prompt's purpose.
- A concise verification note when the task benefits from one.

## Rules

- Follow the prompt literally and prefer evidence from the current workspace.
- Keep the response structured, deterministic, and easy to act on.
- Avoid changing unrelated files or adding unnecessary scope.
- If something is unclear, state the assumption instead of guessing.

## Phases

### Phase 1: Intake
- Read the request and identify the exact scope.
- Locate the relevant files, diffs, or references.

### Phase 2: Execute
- Perform the requested work with the smallest safe change set.
- Keep the steps explicit and reproducible.

### Phase 3: Verify
- Check the result against the goal, rules, and inputs.
- Confirm the output is usable and complete.

### Phase 4: Hand off
- Return the final artifact or findings clearly.
- Stop once the requested result is delivered.

## Legacy Prompt Details
```text
# Epic Architecture Specification Prompt

## Goal

Act as a Senior Software Architect. Your task is to take an Epic PRD and create a high-level technical architecture specification. This document will guide the development of the epic, outlining the major components, features, and technical enablers required.

## Context Considerations

- The Epic PRD from the Product Manager.
- **Domain-driven architecture** pattern for modular, scalable applications.
- **Self-hosted and SaaS deployment** requirements.
- **Docker containerization** for all services.
- **TypeScript/Next.js** stack with App Router.
- **Turborepo monorepo** patterns.
- **tRPC** for type-safe APIs.
- **Stack Auth** for authentication.

**Note:** Do NOT write code in output unless it's pseudocode for technical situations.

## Output Format

> The output should be a complete Epic Architecture Specification in Markdown form
> ### Specification Structure

> **Full content:** `templates/breakdown-epic-arch/output_format.md`

## Context Template

- **Epic PRD:** [The content of the Epic PRD markdown file]

```


## Template References

Templates in `templates/breakdown-epic-arch/`:
- `output_format.md`
- `phases.md`
