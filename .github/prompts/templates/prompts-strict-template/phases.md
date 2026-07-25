---
name: prompts-strict-template-phases
title: Prompts Strict Template — Phases
description: >-
  Full phase definitions for the /prompts-strict-template prompt. Implements
  Structural Intake and Template Normalization as executable phases with
  Field/Details tables and a compliance report contract.
version: 1.0.0
tags: [template, prompts, phases, normalization, compliance]
---

# Phases — `/prompts-strict-template`

These two phases turn a non-conforming `.prompt.md` into a strict-template-compliant
file **without losing the author's original intent**. Run them in order, one pass at
a time, and verify after each pass (per `templates/_shared/rules-core.md` rule 3).

The 11 required top-level sections, in exact order, are:

1. `## Goal`
2. `## Description`
3. `## Context`
4. `## Skills Required`
5. `## Personas`
6. `## Rules`
7. `## Phases`
8. `## Steps`
9. `## Tasks`
10. `## Subtasks`
11. `## Actions Summary`

Any other section (e.g. `## Template References`) is allowed **after** the required 11,
but must not displace them.

---

### Phase 1: Structural Intake

Inventory the target file before changing a single character. The goal is a precise
drift report you can act on in Phase 2.

| Field | Details |
| --- | --- |
| **Phase** | 1 — Structural Intake |
| **Input** | Path to the target `.prompt.md` (and, if referenced, its `templates/<name>/` directory). |
| **Output** | A drift report: ordered list of present sections, list of missing/extra/out-of-order sections, and frontmatter field inventory. |
| **Validation** | Every `##` section heading in the target is accounted for exactly once; the drift report lists all 11 required sections as Present/Missing/OutOfOrder; frontmatter parses as valid YAML. |

Concrete steps:

1. **Parse frontmatter.** Read the leading `---` block. Extract and record:
   - `name` (kebab-case, matches filename stem),
   - `title`,
   - `trigger` (must be `/<name>`),
   - `description`,
   - dependency fields (`skills`, `toolsets`, `scripts`, `tags`).
   Confirm the block is valid YAML; if not, flag it as the first structural defect.
2. **Extract top-level sections.** Collect every line beginning with `##` (exactly two hashes, not `###`). Record them in document order, preserving their exact heading text.
3. **Compare against the 11 required sections** from the ordered list above:
   - **Missing** — a required section absent from the document.
   - **Extra** — a section present that is not one of the 11 and is not an allowed trailing section.
   - **OutOfOrder** — a required section present but at the wrong index relative to the others.
4. **Inspect phase structure** (the `## Phases` block, if present): for each `### Phase N:` heading, check whether it is followed by a Field/Details table whose mandatory rows (`Phase`, `Input`, `Output`, `Validation`) all exist.
5. **Inspect numbering** in `## Tasks` and `## Subtasks`: verify items follow `Task N.x` and `Subtask N.x.y` patterns (e.g. `Task 1.1`, `Subtask 1.1.1`). Record any malformed entries (plain bullets, `1.`, `Step A`, etc.).
6. **Emit the drift report** as a compact list so Phase 2 can be executed mechanically. Do not mutate the target yet.

---

### Phase 2: Template Normalization

Apply the fixes identified in Phase 1, in required-section order, preserving the
author's wording, trigger, and intent.

| Field | Details |
| --- | --- |
| **Phase** | 2 — Template Normalization |
| **Input** | The target `.prompt.md` plus the Phase 1 drift report. |
| **Output** | A rewritten target file where all 11 required sections exist, are ordered correctly, each Phase has a valid Field/Details table, and Tasks/Subtasks use strict numbering; plus a compliance report. |
| **Validation** | Re-running Phase 1 on the result yields zero Missing/OutOfOrder/Extra findings; every Phase table has all four mandatory rows; all Task/Subtask items match `Task N.x` / `Subtask N.x.y`; `enhance-markdown`-style lint reports no new diagnostics. |

Concrete steps:

1. **Insert missing sections in exact required order.** For each Missing section from the drift report, add a stub at the correct position using the canonical heading text. Seed each with the minimum compliant content (non-empty) so the section is present and valid; never leave a required section empty.
2. **Reorder out-of-order sections.** Move any OutOfOrder required section to its correct index. Allowed trailing sections (e.g. `## Template References`) stay after the 11; if one was displaced into the required block, move it back below `## Actions Summary`.
3. **Normalize every Phase block.** For each `### Phase N:`:
   - Insert a Field/Details table immediately under the heading.
   - Ensure the mandatory rows are present and filled: `Phase`, `Input`, `Output`, `Validation`.
   - Keep `Phase` value consistent with the heading number.
4. **Rewrite list numbering.** Convert `## Tasks` items to `Task N.x` form and `## Subtasks` items to `Subtask N.x.y` form, preserving their semantic content. Map old bullets to the new numbering by section so cross-references stay sensible.
5. **Run `enhance-markdown`-style checks.** Normalize heading hierarchy, list markers, table alignment, and code-fence language tags. Confirm no new markdown diagnostics are introduced by the edits.
6. **Preserve source intent.** Diff the result against the original (excluding structure-only changes). The author's declared purpose, trigger, persona guidance, and domain wording must be retained verbatim unless they were themselves structurally invalid.
7. **Emit a compliance report** summarizing: sections added/reordered, phases normalized (with row counts), numbering rewrites applied, lint result, and a final PASS/FAIL against the 11-section contract. If FAIL, list the residual findings so the next run is idempotent.

> **Idempotency note:** Re-running `/prompts-strict-template` on an already-compliant file must produce a PASS report with zero mutations (per `rules-core.md` rule 7).
