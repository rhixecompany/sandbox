---
category: software-development
title: Project Docs
name: project-docs
description: Use when generating, auditing, or optimizing project documentation — including frontmatter, AI-readiness scoring, and 11-artifact symmetry validation.
---

# project-docs

Generate, audit, and optimize documentation structures. Covers initial doc creation (README, ARCHITECTURE, etc.) AND ongoing quality optimization (YAML frontmatter, AI-readiness scoring, doc symmetry checking).

## When to Use

- Creating documentation for new projects
- Auditing or restructuring existing docs
- Adding YAML frontmatter to unmarked docs
- Running AI-readiness quality scoring
- Checking generator-orchestrator 11-artifact completeness
- Standardizing documentation across projects

## When NOT to Use

- Quick inline comments (use code-docs)
- Non-project documentation (internal notes)
- Code-level docstrings (use code-docs)

## Workflow

### Phase 1: Analyze Project

- Identify project type and language
- Determine audience
- Review existing documentation
- Identify gaps

### Phase 2: Plan Documentation

- Outline required documents
- Determine structure
- Identify key sections
- Plan content
- For multi-repo audits, define a live-filesystem verification pass before trusting any index or summary

### Phase 3: Generate Documentation

- Create README with overview
- Write ARCHITECTURE for design
- Create USER_GUIDE for users
- Write DEVELOPER_GUIDE for contributors
- Add CONTRIBUTING guidelines

### Phase 4: Optimize (AI-Readiness & Quality)

Run after initial docs are created or when improving existing docs:

1. **Add YAML frontmatter** — every `.md` file needs `title`, `description`, `status`, `tags` at minimum. Use the template from `references/ai-readiness-criteria.md`.
2. **Verify summary paragraphs** — first 2-3 sentences after H1 must be ≥30 chars of prose describing the document.
3. **Tag code blocks** — every fenced block needs a language tag (` ```sh `, ` ```python `, ` ```json `). Untagged ` ``` ` is opaque to AI parsers.
4. **Add cross-references** — relative links (`[text](../other.md)`) between related docs create a navigable knowledge graph.
5. **Break up wall-of-text** — any file >500 lines without H2/H3 headers gets −20 penalty. Add section headers every <200 lines.
6. **Score docs** — run `python scripts/score-docs.py <target>` to generate `docs/ai-readiness-report.md`. Target score: ≥70/100.

See `references/ai-readiness-criteria.md` for the complete scoring rubric and hygiene checklist.

### Phase 5: Verify Symmetry (Generator-Orchestrator Pattern)

When using the generator-orchestrator framework, each project should produce 11 documentation artifacts:

| # | Artifact | Purpose |
|---|----------|---------|
| 1 | technology-stack.md | Languages, frameworks, tools used |
| 2 | folder-structure.md | Directory tree with purpose annotations |
| 3 | architecture.md | System design, component relationships |
| 4 | project-workflow.md | Dev lifecycle, CI/CD, release process |
| 5 | code-exemplars.md | Key code patterns with explanations |
| 6 | copilot-instructions.md | AI-assistant context rules |
| 7 | readme.md | Project overview and quickstart |
| 8 | artifact-manifest.json | Machine-readable doc index |
| 9 | cross-linking-report.md | Internal link integrity report |
| 10 | validation-report.md | Doc quality validation results |
| 11 | execution-summary.md | Orchestrator run summary |

All 11 artifacts live under `docs/project-docs/<project-name>/`. To verify completeness, check each project directory for all 11 files.

## Support Files

- `references/ai-readiness-criteria.md` — Complete scoring rubric (5 criteria, 0-100 scale), YAML frontmatter template, hygiene checklist
- `references/template.md` — Basic documentation template
- `references/repo-audit-notes.md` — Multi-repo documentation audit notes: live filesystem verification, stale index detection, per-repo instruction synthesis
- `scripts/score-docs.py` — Reusable AI-readiness scorer; run `python scripts/score-docs.py <target_dir>` to generate report


## Best Practices

- Keep documentation up to date
- Use consistent formatting and YAML frontmatter
- Include examples and diagrams
- Make documentation searchable with tags
- Version control documentation
- Get feedback from users
- Maintain documentation regularly
- Run AI-readiness scoring before doc review cycles

