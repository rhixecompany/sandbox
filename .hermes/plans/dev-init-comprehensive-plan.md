---
title: Dev-Init Comprehensive Plan — Prompt Library Standardization
author: dev-init pipeline
version: 1.1
status: active
targets:
  - Prompts/dev-init.prompts.md
  - .github/prompts/context-map.prompt.md
  - .github/prompts/convert-plaintext-to-md.prompt.md
  - .github/prompts/boost-prompt.prompt.md
  - .github/prompts/ai-prompt-engineering-safety-review.prompt.md
  - .github/prompts/update-implementation-plan.prompt.md
  - .github/prompts/prompt-builder.prompt.md
  - Prompts/*.txt
  - Prompts/*.md
---

# Dev-Init: Prompt Library Standardization Plan

## Overview

Standardize and cross-reference the prompt library across `Prompts/` and `.github/prompts/`. The dev-init workflow should produce a concrete plan, then hand off to conversion and audit prompts without losing safety notes or source fidelity.

## Implementation Artifacts

| File | Purpose |
| --- | --- |
| `Prompts/dev-init.prompts.md` | Planning prompt for the workflow |
| `docs/dev-init-spec.md` | Implementation spec with goals, inputs, risks, and examples |
| `docs/dev-init-comprehensive-plan.md` | High-level execution plan and target inventory |
| `docs/prompts-cross-reference-registry.md` | Cross-reference registry for prompts and skills |
| `Bash/archive/artifacts/context-maps/dev-init.context.json` | Confirmed dependency snapshot |

## Reference Workflow

1. Run `/context-map` on the dev-init target set.
2. Verify the conversion and audit templates exist.
3. Plan `Prompts/*.txt` → `Prompts/*.md` conversion.
4. Plan audits for the related `.github/prompts/*.prompt.md` files.
5. Confirm all audit targets reference `context-map`.
6. Produce a final plan and completion report.

## Code Samples

### Preflight check

```bash
rg -n "trigger: /context-map|context-map" .github/prompts Prompts
```

### Conversion pass

```bash
/enhance-markdown --txt-to-md Prompts/dev-init.prompts.txt
```

### Verification pass

```bash
for f in Prompts/*.md; do head -1 "$f"; done
```

## File References

| File | Role | Notes |
| --- | --- | --- |
| `Prompts/dev-init.prompts.md` | modify | The prompt being implemented |
| `docs/dev-init-spec.md` | modify | Canonical implementation spec |
| `docs/dev-init-comprehensive-plan.md` | modify | Execution plan artifact |
| `Prompts/*.txt` | dependency | Source briefs |
| `Prompts/*.md` | dependency/test | Converted outputs |
| `.github/prompts/context-map.prompt.md` | dependency | Required first step |

## Acceptance Criteria

- [x] The prompt references `/context-map` before conversion.
- [x] The prompt explicitly lists source and target prompt families.
- [x] The prompt contains phase tables, steps, tasks, and subtasks.
- [x] The supporting docs link the prompt to the relevant artifacts.
- [x] The workflow is safe to re-run and preserves safety notes.

## Implementation Status

- Phase 1 is underway and the repository state has been verified against the prompt plan.
- The cross-reference targets already contain `context-map` references, so the next work item is the actual prompt-batch implementation step.
- Keep the plan artifacts in sync as prompt files are updated.

## Risks

- Cross-file prompt changes can drift if `Prompts/*.txt` and `Prompts/*.md` are updated separately.
- Missing `.github/prompts/*.prompt.md` templates can block conversion planning.
- The plan should avoid broad rewrites that erase manually added safety notes.
