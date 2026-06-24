---
title: "Dev Init Implementation Plan"
source: "docs/dev-init-implementation-plan.md"
---

# Dev Init Implementation Plan

## Scope

This document starts implementation for the Dev Init workflow defined in [Prompts/dev-init.prompts.md](../Prompts/dev-init.prompts.md).

The plan covers these workflow prompts:
- [convert-plaintext-to-md](../.github/prompts/convert-plaintext-to-md.prompt.md)
- [context-map](../.github/prompts/context-map.prompt.md)
- [boost-prompt](../.github/prompts/boost-prompt.prompt.md)
- [ai-prompt-engineering-safety-review](../.github/prompts/ai-prompt-engineering-safety-review.prompt.md)
- [update-implementation-plan](../.github/prompts/update-implementation-plan.prompt.md)
- [prompt-builder](../.github/prompts/prompt-builder.prompt.md)

## Objectives

1. Convert and normalize prompt assets from Prompts/*.txt into Prompts/*.md.
2. Generate a deterministic context map for each target prompt before modifications.
3. Apply enhancement and safety review passes without dropping critical constraints.
4. Build final reusable prompts from normalized markdown sources.
5. Keep all outputs reproducible and idempotent.

## Feature Specifications

### Feature 1: Prompt Conversion Pipeline

Purpose:
- Convert plaintext prompt files to markdown while preserving intent and operational constraints.

Inputs:
- Source files in Prompts/*.txt.

Outputs:
- Converted markdown prompts in Prompts/*.md.
- Conversion audit summary in docs/.

Acceptance Criteria:
- YAML frontmatter exists and is valid in all generated markdown files.
- Required sections are preserved (rules, actions, validation criteria where applicable).
- No unsafe simplification of operational instructions.

### Feature 2: Context Mapping

Purpose:
- Build a dependency and reference map before edits.

Inputs:
- Converted prompts and related docs.

Outputs:
- Context reports under docs/ with file relationships, dependencies, and risk flags.

Acceptance Criteria:
- Each prompt has a context map that includes source files, template dependencies, and affected outputs.
- High-risk references are explicitly flagged before enhancement.

### Feature 3: Prompt Enhancement and Safety Review

Purpose:
- Improve clarity, structure, and actionable steps while preserving mandatory safety constraints.

Inputs:
- Context maps and converted markdown prompts.

Outputs:
- Enhanced prompts.
- Safety findings report with explicit pass/fail checks.

Acceptance Criteria:
- Constraint preservation audit is completed.
- Any removed or changed rule has documented rationale.
- Safety review confirms critical safeguards are retained.

### Feature 4: Plan Synchronization

Purpose:
- Keep implementation plans and progress aligned with evolving prompt definitions.

Inputs:
- Existing implementation plans and latest prompt revisions.

Outputs:
- Updated plan docs with clear deltas and unresolved items.

Acceptance Criteria:
- Plan updates are traceable and include changed assumptions.
- Open risks and blockers are current.

### Feature 5: Prompt Builder Packaging

Purpose:
- Produce final ready-to-run prompts from normalized markdown files.

Inputs:
- Enhanced markdown prompts.

Outputs:
- Built prompt artifacts and index metadata.

Acceptance Criteria:
- Build outputs are deterministic.
- Source-to-output mapping is documented.

## Integration Points and File References

Core prompt definitions:
- [Prompts/dev-init.prompts.md](../Prompts/dev-init.prompts.md)
- [Prompts/dev-init.prompts.txt](../Prompts/dev-init.prompts.txt)

Template prompts:
- [convert-plaintext-to-md](../.github/prompts/convert-plaintext-to-md.prompt.md)
- [context-map](../.github/prompts/context-map.prompt.md)
- [boost-prompt](../.github/prompts/boost-prompt.prompt.md)
- [ai-prompt-engineering-safety-review](../.github/prompts/ai-prompt-engineering-safety-review.prompt.md)
- [update-implementation-plan](../.github/prompts/update-implementation-plan.prompt.md)
- [prompt-builder](../.github/prompts/prompt-builder.prompt.md)

Likely output locations:
- [docs](.) for reports and verification artifacts
- [Prompts](../Prompts) for normalized prompt markdown

## Starter Code Samples

### Sample 1: Deterministic discovery of plaintext prompts

```bash
rg --files Prompts | rg "\\.txt$"
```

### Sample 2: Validate markdown frontmatter quickly

```bash
rg -n "^---$|^title:|^trigger:|^tags:" Prompts/*.md
```

### Sample 3: Detect potential constraint removal

```bash
rg -n "CRITICAL|must|never|forbidden|safety|approval" Prompts/*.md docs/*.md
```

### Sample 4: Basic idempotency marker pattern (TypeScript)

```ts
import { readFileSync, writeFileSync, existsSync } from "node:fs";

const markerPath = "docs/.dev-init-marker.json";
const marker = existsSync(markerPath)
  ? JSON.parse(readFileSync(markerPath, "utf8"))
  : { runs: 0, processed: [] as string[] };

function markProcessed(file: string) {
  if (!marker.processed.includes(file)) marker.processed.push(file);
}

marker.runs += 1;
markProcessed("Prompts/dev-init.prompts.md");
writeFileSync(markerPath, JSON.stringify(marker, null, 2));
```

## Implementation Guide

### Phase A: Baseline and Inventory

1. Verify required template prompts exist.
2. Inventory current Prompts/*.txt and Prompts/*.md files.
3. Record initial state and known risks.

### Phase B: Conversion

1. Convert plaintext prompts to markdown with stable formatting.
2. Validate frontmatter and required sections.
3. Save conversion report.

### Phase C: Context and Risk Analysis

1. Generate context map for each prompt.
2. Identify dependency and template gaps.
3. Block enhancement if critical templates are missing.

### Phase D: Enhancement and Safety

1. Apply prompt enhancement rules.
2. Run safety review and constraint preservation checks.
3. Document all substantive rule changes.

### Phase E: Build and Verify

1. Build final prompt artifacts.
2. Verify deterministic output and idempotent rerun behavior.
3. Publish final implementation summary.

## Open Risks

- Template drift between prompt files and usage expectations.
- Over-aggressive enhancement causing hidden constraint loss.
- Inconsistent section naming across historical prompt files.

## Immediate Next Actions

1. Generate a dedicated inventory report for Prompts/*.txt to be converted.
2. Draft an initial constraint-preservation checklist per prompt file.
3. Run first conversion pass on a small batch and verify idempotency.
