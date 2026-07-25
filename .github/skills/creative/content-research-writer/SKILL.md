---
name: content-research-writer
title: "Content Research Writer"
description: "Use when writing blog posts, articles, newsletters, or tutorials that need research, citations, structured outlines, and iterative feedback."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [writing, research, content, articles, newsletters]
metadata:
  hermes:
    tags: [imported]
---
# Content Research Writer

## Overview

Collaborative writing workflow for research-assisted content creation. Use this skill to structure outlines, gather sources, draft, and revise while preserving voice and source accuracy.

## When to Use

- Blog posts, articles, newsletters, or tutorials needing citations
- Content needing structured research and verified sources
- Explanatory or thought-leadership writing
- Multiple drafts and iterative refinement

## When NOT to Use

- Short social posts without research requirements
- Code documentation
- Real-time collaborative editing with external parties
- Internal memos without external sourcing needs

## Skills Required

| Skill | Purpose |
|-------|---------|
| `writing-clearly-and-concisely` | Improve clarity, flow, and readability |
| `humanizer` | Preserve natural voice during revision |

## Workflow

### Phase 1: Structure and Outline

1. Define purpose, audience, constraints, and success criteria.
2. Create a structured outline for the content.
3. Identify high-priority research questions early.
4. Note likely citation formats and required evidence.

### Phase 2: Research and Verify

1. Search for reputable sources aligned with the outline.
2. Prioritize authoritative or primary sources.
3. Record source metadata for citation.
4. Flag claims that remain unsupported.

### Phase 3: Draft and Revise

1. Write section drafts with integrated citations.
2. Refine hooks and transitions between sections.
3. Check consistency and flow after each revision.
4. Use iterated edits rather than large rewrites when possible.

### Phase 4: Finalize and Verify

1. Confirm citations and source attribution.
2. Check links or references if included.
3. Deliver as clean prose or cleaned markup as required.
4. Summarize remaining assumptions or unresolved gaps.

## Verification Checklist

- [ ] Outline confirmed with purpose and topic constraints
- [ ] Sources reviewed and organized
- [ ] Drafts cover intended sections
- [ ] Citations and claims verified
- [ ] Final output polished and consistent

## Pitfalls

- Treating unverified claims as conclusions weakens credibility.
- Skipping citation verification can introduce incorrect references.
- Overediting can remove voice; use revision passes instead.
- Missing the audience or publication context reduces usefulness.

### Research Pipeline Pitfalls

- **Subagent delegation for web research is unreliable** — `delegate_task` with web toolsets consistently times out at 600s on multi-query extraction workflows. **Direct main-thread execution** with `web_search` + `web_extract` is significantly more reliable for research passes.
- **Cross-reference symmetry must be verified** — in multi-project workspaces, if Project A references Project B in `## Related Projects`, Project B must reciprocate. Automate verification or add to gate checklist.
- **Phase-gating enforcement** — secondary/dependent goals (migration, consolidation, CI setup) must be explicitly locked until all primary phase verification gates pass. Add gate enforcement to the workflow.
- **Size gates can conflict with comprehensiveness** — reports exceeding upper bounds (5KB) may still be valuable; document the exception rationale in verification logs rather than truncating actionable content.
