# AI-Readiness Scoring Criteria

Each markdown file is scored 0–100 across 5 criteria. Score >=70 = AI-ready.

## Criteria

| # | Criterion | Max | Why it matters |
|---|-----------|-----|----------------|
| 1 | **YAML frontmatter** | +20 | AI tools parse structured metadata (title, description, tags) before reading body. Missing frontmatter = zero context. |
| 2 | **Summary paragraph after H1** | +15 | First 2-3 sentences after the heading become the file's abstract. Without this, AI has to infer purpose from the full body. |
| 3 | **Language-tagged code blocks** | +30 (10 each, max 3) | ` ```sh `, ` ```python `, ` ```json ` — language tags enable syntax-aware parsing. Untagged ` ``` ` is opaque. |
| 4 | **Resolvable cross-references** | +20 (10 each, max 2) | Relative links (`[text](../other.md)`) that actually resolve. Creates a navigable knowledge graph. |
| 5 | **Section header density** | +15 | H2/H3 every <200 lines. Long unbroken text is harder to navigate and summarize. |
| **Wall-of-text penalty** | **−20** | >500 lines with zero H2/H3 headers. Text must be structured. |

## Standard YAML Frontmatter Template

```yaml
---
title: Document Title — Project Context
description: One-sentence summary of what this document covers and who it's for.
status: draft | review | active | final | archived
tags: [keyword1, keyword2, category]
generated: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

## Quick Hygiene Check

Before marking docs as "done":
- `grep -r '^---' docs/` — every file should start with `---`
- First line after `---` should be `title:`
- After H1, first 2 lines should be ≥30 chars of prose summary
- All ` ``` ` blocks should have a language tag (`` ```bash ``, `` ```python ``)
- No markdown file >500 lines without H2 headers

## Scoring Tool

```bash
python scripts/score-docs.py <target_directory>
```

Generates `docs/ai-readiness-report.md` with full per-file breakdown, summary statistics, and top issues.
