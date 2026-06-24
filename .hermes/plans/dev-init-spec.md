---
title: "Dev Init Spec"
source: "docs/dev-init-spec.md"
---

# Dev Init — Implementation Spec

**Source:** `Prompts/dev-init.prompts.md`  
**Scope:** Prompt-library planning for `Prompts/*.txt`, `Prompts/*.md`, and related `.github/prompts/*.prompt.md` workflows.

## Problem

The repository has a large prompt library split across `Prompts/` and `.github/prompts/`. The dev-init workflow needs a repeatable planning artifact that can:
- verify source/template files before changes
- map dependencies with `/context-map`
- plan TXT→MD conversion work
- plan audits for related prompt files
- preserve idempotency and safety notes

## Goals

1. Produce a file-backed context map before implementation.
2. Create a prompt-conversion plan for `Prompts/*.txt` → `Prompts/*.md`.
3. Create an audit plan for `.github/prompts/boost-prompt.prompt.md`, `ai-prompt-engineering-safety-review.prompt.md`, `update-implementation-plan.prompt.md`, and `prompt-builder.prompt.md`.
4. Keep the workflow safe to re-run without duplicating work.
5. Ensure every target prompt references `.github/prompts/context-map.prompt.md` where appropriate.

## Inputs

| File | Role | Notes |
| --- | --- | --- |
| `Prompts/dev-init.prompts.md` | source | Defines the workflow and output requirements |
| `Prompts/*.txt` | source | Raw prompt briefs to convert |
| `Prompts/*.md` | dependency | Existing prompt outputs to validate |
| `.github/prompts/context-map.prompt.md` | dependency | Required preflight mapping prompt |
| `.github/prompts/convert-plaintext-to-md.prompt.md` | dependency | TXT→MD conversion workflow |
| `.github/prompts/boost-prompt.prompt.md` | dependency | Audit target |
| `.github/prompts/ai-prompt-engineering-safety-review.prompt.md` | dependency | Audit target |
| `.github/prompts/update-implementation-plan.prompt.md` | dependency | Audit target |
| `.github/prompts/prompt-builder.prompt.md` | dependency | Audit target |
| `docs/dev-init-comprehensive-plan.md` | output | Planning artifact |
| `docs/dev-init-spec.md` | output | Implementation spec |
| `docs/prompts-cross-reference-registry.md` | dependency | Cross-reference source |
| `Bash/archive/artifacts/context-maps/dev-init.context.json` | dependency | Verified context snapshot |

## Workflow

### Phase 1: Discover and verify

- Confirm the source prompt and related templates exist.
- Map the prompt-library dependency surface with `/context-map`.
- Record direct references and likely follow-up files.

### Phase 2: Plan conversion

- Define the TXT→MD conversion scope.
- Preserve source intent, safety notes, and formatting fidelity.
- Document idempotent behavior for reruns.

### Phase 3: Plan audits and fixes

- List the audit targets.
- Capture expected fixes and dependency updates.
- Require a `context-map` reference for each target where missing.

### Phase 4: Review and hand off

- Produce a completion report.
- Call out residual risks.
- Stop after the planning handoff.

## Code Samples

### Context-map preflight

```bash
/context-map Prompts/dev-init.prompts.md
```

### TXT→MD conversion batch

```bash
/enhance-markdown --txt-to-md Prompts/dev-init.prompts.txt
```

### Cross-reference check

```bash
rg -n "context-map" Prompts/*.md .github/prompts/*.prompt.md
```

## Acceptance Criteria

- [x] `Prompts/dev-init.prompts.md` contains the full planning workflow.
- [x] `docs/dev-init-comprehensive-plan.md` exists and names the target files.
- [x] `docs/dev-init-spec.md` captures the implementation scope and risks.
- [x] The workflow references `/context-map` before conversion.
- [x] The workflow is idempotent and safe to rerun.
- [x] The prompt-library audit targets are explicitly listed.

## Implementation Status

- Phase 1 is started: the prompt and supporting docs are aligned.
- The audited prompt targets already reference `.github/prompts/context-map.prompt.md`.
- The next implementation pass should focus on any remaining prompt-batch fixes or prompt-library conversions identified by the plan.

## Risks

- Prompt-library conversion can drift if source `.txt` and `.md` files are both edited without a clear source-of-truth rule.
- Missing template files can block the conversion pipeline.
- Cross-reference updates can become inconsistent if they are made outside the same planning pass.
- The workflow should avoid inventing content not present in the source brief.
