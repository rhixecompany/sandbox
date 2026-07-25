---
name: project-docs
title: "Project Docs"
description: "Use when generating, auditing, or optimizing project documentation — including frontmatter, AI-readiness scoring, and 11-artifact symmetry validation."
version: 1.0.0
author: Alexa
license: MIT
tags: [imported]
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

## Synchronous Research Report Maintenance (`RESEARCH_REPORT.md`)

Many workspace projects carry a `RESEARCH_REPORT.md` that must be regenerated/updated via web research on a schedule. It has a **hard contract** that differs from the 11-artifact generator pattern:

- **9+ `##` (H2) sections** minimum — Typical sections: Similar Projects, Key Findings, Cheatsheets & Quick Reference, Best Practices, Common Pitfalls, Performance, Security, Related Projects, Resources, Methodology. Below 9 sections fails the gate.
- **Size gate: 1 KB–5 KB (1024–5120 bytes)** of the final on-disk file.
- **Template:** H1 title, a `>` blockquote header (Type / Stack / Status / Updated date), `---`, then the `##` sections, ending with a one-line inline methodology note (synced from web searches + `web_extract`).

**Update workflow:**
1. Read the existing report; preserve its section structure and the trailing methodology note.
2. Run web searches (8–10) + `web_extract` on key sources; verify primary URLs return 200 (a PyPI extract can 404 even when the GitHub repo is live — substitute the verified repo URL).
3. Merge fresh findings; never fabricate — only cite sources actually retrieved.
4. Write, then **verify byte count + section count** (see pitfall below). If over 5 KB, trim: drop the redundant "### Research Methodology" footer block, shorten resource tables, tighten prose. If under 1 KB, expand with a Cheatsheets/Resources section.

**Pitfall — CRLF inflates `wc -c` past the 5 KB gate.** On Windows/MSYS, `wc -c` counts 2 bytes per `\r\n` line ending, so a perfectly-sized report reads ~50–110 bytes over 5120 and falsely fails the gate. Fix: `sed -i 's/\r$//' file.md` to normalize to LF, OR count characters (`wc -m`) — LF content is usually already under 5120. Always check with `grep -c '^## '` for the section count separately.

**Pitfall — `write_file` re-adds CRLF?** No: `write_file` emits LF. The bloat comes from editing with tools that normalize to CRLF (e.g. some `patch`/`terminal` round-trips). Re-normalize before final verification.

## Repo Narrative Docs (REPOSITORY_SUMMARY.md + THE_STORY_OF_THIS_REPO.md)

A frequent deliverable set (e.g. `/repo-story-time` requests): for each repo write `REPOSITORY_SUMMARY.md` (factual) and `THE_STORY_OF_THIS_REPO.md` (narrative retelling of git history).

**Evidence-first workflow:**
1. Per repo, gather git stats: `git rev-list --count HEAD`, `git shortlog -sn`, `git log --pretty=format:"%ad|%s" --date=short` (dates + subjects), `git log --pretty=format:"%an <%ae>" | sort | uniq -c` (author tally).
2. Read the project's README, ARCHITECTURE, AGENTS, and technology-stack docs for factual structure.
3. Write `REPOSITORY_SUMMARY.md` from those docs: overview, architecture, key components, tech, data flow, team (contributor stats), git evidence appendix.
4. Write `THE_STORY_OF_THIS_REPO.md` from the git stats: year-in-numbers table, contributors, seasonal patterns, themes, plot twists, current chapter (latest 3 commits + reading of present).

**Pitfall — synthetic git history (the big one).** When repos are vendored as local submodules, the git log is often uniform: ONE author (e.g. `rhixecompany`), all commits within a few weeks, subjects like `initial local project setup`, `vscode config audit`, `update RESEARCH_REPORT.md ... trim to size gate`. This is workspace setup/maintenance — NOT the project's real development history. DO NOT fabricate a "story" from it. Derive product facts from the repo files; in THE_STORY explicitly state: "This git history is the local submodule's history (setup + maintenance by X). It does not capture the upstream project's original commit lineage." Always pair the narrative with an evidence appendix (commit counts, date range, author) so claims are verifiable. Flag repos that carry larger upstream artifacts (e.g. a 234 KB `CHANGELOG.md` + 45 KB `CONTRIBUTORS.md` inside a 5-commit repo) — that IS the real lineage; note it.

**Pitfall — concurrent sibling writes.** If subagents split the work per repo, a sibling can overwrite your output with its own version. Always verify final on-disk content (`head -1` + `wc -l`) after writing; prefer a deterministic single-writer or verify-and-rewrite.

**Templates / skeletons:** see `references/repo-narrative.md`.

## Support Files

- `references/ai-readiness-criteria.md` — Complete scoring rubric (5 criteria, 0-100 scale), YAML frontmatter template, hygiene checklist
- `references/template.md` — Basic documentation template
- `references/repo-audit-notes.md` — Multi-repo documentation audit notes: live filesystem verification, stale index detection, per-repo instruction synthesis
- `references/research-report-contract.md` — RESEARCH_REPORT.md size/section contract, verification recipe, and a condensed bank of verified 2026 framework facts (Django 5.2/6.0, Next.js 16/Turbopack, Python 3.14, Prisma 6, Selenium 4/BiDi) reusable across comic/Django/Python projects
- `scripts/score-docs.py` — Reusable AI-readiness scorer; run `python scripts/score-docs.py <target_dir>` to generate report
- `references/repo-narrative.md` — Deliverable format + git-evidence recipe for `REPOSITORY_SUMMARY.md` / `THE_STORY_OF_THIS_REPO.md`, and the synthetic-git-history caveat


## Best Practices

- Keep documentation up to date
- Use consistent formatting and YAML frontmatter
- Include examples and diagrams
- Make documentation searchable with tags
- Version control documentation
- Get feedback from users
- Maintain documentation regularly
- Run AI-readiness scoring before doc review cycles


## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

