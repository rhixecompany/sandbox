# boost-prompt — Refinement Execution Report

> Generated: 2026-07-09 |  Source prompt: `prompts/boost-prompt.prompt.md`
> Mode: **labeled dry-run** (no live user interrogation; Joyride clipboard unavailable in this non-interactive context)
> Deliverable: refined workspace prompt `what-context-needed` → see `## Refined Prompt` below

## Why this is a labeled dry-run

- **No Joyride / clipboard**: `boost-prompt` requires the VS Code Joyride extension to copy the final markdown to the system clipboard. This environment has no VS Code/Joyride, so rule #6 (clipboard delivery) is **skipped and labeled**. The refined markdown is delivered as a file artifact instead.
- **No live interrogator**: The original workflow interrogates the user interactively (Phase 1). Here I substitute a context-driven self-interrogation using the real workspace prompts as evidence (file-backed, per rules-core #8).
- Everything else from the workflow is executed for real on a real workspace prompt.

## Interrogation (Phase 1 — self-answered from workspace context)

| Question | Answer (evidence-backed) |
| --- | --- |
| What is the prompt's job? | Ask an AI assistant which files it must read before answering a question, with rationale and uncertainty notes. Source: `prompts/what-context-needed.prompt.md` Goal + "My Question" section. |
| Who is the audience? | A coding agent (Copilot / Hermes) operating inside a repo, about to answer or act on a question. |
| What is the deliverable format? | A markdown block: `## Files I Need` with Must-See / Should-See / Optional tiers, rationale per file, already-seen notes, and explicit uncertainties. |
| What constraints apply? | Do NOT read or edit files (only enumerate what *should* be read). Be reproducible and evidence-based. Honor rules-core (no backup files, verify, idempotent). |
| What is missing in the draft? | Thin Goal; generic Phases; no `trigger`; no explicit output schema; no rule forbidding speculative file lists; no tiered prioritization. |

## Exploration (Phase 2)

- Confirmed `prompts/what-context-needed.prompt.md` is a real workspace draft prompt (92 lines, frontmatter incomplete: no `trigger`, no `title`).
- Confirmed sibling prompts (`task-implementation`, `dev-init`) use the 9-section template and complete frontmatter — used as the quality target.
- `boost-prompt` itself references `templates/boost-prompt/phases.md` and `tools_required.md` — **not present** in repo (only `templates/_shared/` exists); skipped gracefully, applied `templates/_shared/rules-core.md` instead.

## Refinement (Phase 3 — structured output)

Applied patterns from `dev-init` §5.4 (imperative rules, complete frontmatter, consistent hierarchy, remove redundancy) and the Stanford/Anthropic heuristics.

### Refined Prompt

````markdown
---
license: MIT
author: Hermes Agent
version: 1.1.0
title: What Context Do You Need?
name: what-context-needed
trigger: /what-context-needed
description: >-
  Ask the assistant to enumerate, with rationale, exactly which files it must
  read before answering a question — plus what it has already seen and what it
  is uncertain about. Read-only; never edits or executes.
tags:
  - ai-assistant
  - ml
  - prompts
  - specification
  - planning
  - documentation
---

# What Context Do You Need?

> Read-only scoping prompt. Ask the assistant which files it needs to examine
> before answering, so it grounds its response in the right evidence instead of
> guessing.

## Goal

Given a question and the current workspace state, produce a prioritized,
evidence-backed list of the files the assistant must read to answer accurately,
explain why each is relevant, note what it has already seen, and surface its
uncertainties.

> Critical rules (read before proceeding):
> 1. **DO NOT read, edit, or execute anything** — only *list* the files that
>    should be read. This is a scoping step, not an action step.
> 2. **Justify every file** with a concrete reason tied to the question.
> 3. **No speculation** — only list files you can locate or that the user
>    provided. Mark any inferred path as "UNVERIFIED".

## Inputs

- `{{question}}` — the question the user wants answered.
- The current workspace, repo, or document state (for discovery only).
- Any diffs, specs, or files the user already supplied.

## Outputs

A single markdown block:

```markdown
## Files I Need

### Must See (required for an accurate answer)
- `path/to/file.ts` — [why it is required]

### Should See (strongly helpful)
- `path/to/other.md` — [why it helps]

### Optional (nice to have)
- `path/to/extra.ts` — [marginal value]

## Already Seen
- `path/to/seen.md` — read earlier in this conversation

## Uncertainties
- [What you still cannot determine, and which file would resolve it]
```

## Rules

> Core rules: [`prompts/templates/_shared/rules-core.md`](../templates/_shared/rules-core.md)

1. List only; never open, modify, or run files.
2. Tie every listed file to a specific part of the question.
3. Prefer files that exist on disk; flag inferred paths as UNVERIFIED.
4. Group files into Must See / Should See / Optional tiers.
5. State uncertainties explicitly instead of guessing.
6. Keep the response deterministic and reproducible.

## Phases

### Phase 1: Intake
- Parse `{{question}}` and identify its exact scope and unknowns.
- Note any files the user already provided or that were seen in conversation.

### Phase 2: Discover
- Locate candidate files in the workspace by name, path, or relevance.
- Do not open them — only confirm existence and relevance.

### Phase 3: Prioritize
- Sort candidates into Must See / Should See / Optional.
- Write one justification line per file.

### Phase 4: Report
- Emit the output block above.
- List uncertainties and which file would resolve each.

## Actions Summary

1. Decode the question's scope.
2. Enumerate candidate files (existence check only).
3. Justify and tier each file.
4. Emit the "Files I Need" block with uncertainties.

## Template References

Templates in `templates/what-context-needed/`: (none — uses shared rules-core only)
````

## Verification (Phase 4)

- [x] Frontmatter complete (title, description, trigger, tags, version bumped 1.0.0 → 1.1.0)
- [x] Critical rules placed in first 15% of body (the blockquote under `#`)
- [x] Nesting depth ≤ 4 (H1 → H2 → H3 → list; no deeper)
- [x] Rules rewritten in imperative, specific language
- [x] Redundant/duplicate tags removed (was `ai-assistant` and `specification` each listed twice)
- [x] Explicit output schema added (was only a fragment in the draft)
- [x] Read-only constraint made explicit and upfront
- [x] No fabricated references introduced (template dir noted as absent)

## Skipped References (graceful)

| Reference | Status | Substituted by |
| --- | --- | --- |
| `templates/boost-prompt/phases.md` | not present in repo | inline Phases section + `templates/_shared/phases.md` |
| `templates/boost-prompt/tools_required.md` | not present in repo | Joyride requirement noted as skipped (no clipboard) |
| Joyride clipboard copy (rule #6) | unavailable (no VS Code) | delivered as file artifact at `results/boost-prompt.output.md` |

## How to apply the refined prompt

Copy the block under `### Refined Prompt` into `prompts/what-context-needed.prompt.md`
(overwrite), then call it with `/what-context-needed` and a `{{question}}`. In an
interactive VS Code session, run Joyride to push the markdown to the clipboard.

---
_End of report · 2026-07-09 · boost-prompt executed as labeled dry-run_
