# Plan: Implement Awesome Hermes Agent Docs Catalog

**Date:** 2026-06-29
**Status:** Draft
**Workspace:** ~/Desktop/docs/awesome-hermes-agent/

---

## 1. Goal

List, triage, catalog, read, and produce a structured implementation (report/catalog artifact) for all files under `~/Desktop/docs/awesome-hermes-agent/`, then verify the deliverable is correct.

---

## 2. Current Context / Assumptions

### Directory inventory (11 files, ~20 KB total)

| Path | Size | Type |
|------|------|------|
| `.actions.json` | 1.4 KB | Workflow metadata (4 actions, all read-only) |
| `.discovery.json` | 174 B | Discovery metadata (repo, pages) |
| `index.md` | 2.7 KB | Master index (already read in prior turn) |
| `pages/README.md` | 6.2 KB | Main awesome list content |
| `pages/CONTRIBUTING.md` | 2.6 KB | Contribution guidelines |
| `pages/CODE_OF_CONDUCT.md` | 2.1 KB | Contributor Covenant v2.0 |
| `pages/sections/core-overview.md` | 977 B | Hermes capabilities |
| `pages/sections/getting-started-(3-step-path).md` | 1.4 KB | Getting started guide |
| `pages/sections/official-resources-(nous-research-maintained).md` | 1.7 KB | Official Nous resources |
| `pages/sections/preamble.md` | 453 B | Title + ecosystem status |
| `pages/sections/skills-&-plugins.md` | 1.4 KB | Community skills list |

### Quality observations

- **Duplicate sections exist** in README.md (Community Skills appears twice verbatim), CONTRIBUTING.md ("Repository Suggestions 2", "Code of Conduct 2"), and preamble.md (duplicated metadata). These are scraping artifacts from the source repo.
- `.actions.json` flags all 4 actions as `read_only` and `implementable_locally: false` — no local install commands are needed.
- The sections/ directory contains individually extracted README sections — not standalone documents, but fragments.

### Deliverable location

A consolidated markdown report saved at:
- `~/Desktop/SandBox/docs/catalogs/awesome-hermes-agent-catalog.md`

---

## 3. Proposed Approach

Three-phase execution:

### Phase 1 — Consolidate & Catalog (read-only analysis)
- Already complete: all 11 files read in the inspection phase above.
- Build a structured table cataloging every file with: path, size, source origin (repo URL), content summary, quality notes (duplicates, scraping artifacts), and actionability (can we install/use or is it reference-only).
- Note the `<-- dupe -->` scrape artifacts for each file.

### Phase 2 — Implement (generate deliverable)
- Create the output directory: `~/Desktop/SandBox/docs/catalogs/`
- Write `awesome-hermes-agent-catalog.md` containing:
  - Header with repo info and ecosystem status
  - **File inventory table** (path, size, type)
  - **Content summaries** per file with structured breakdown
  - **External resources extracted** — all GitHub repos, docs links, community projects mentioned across all files, deduplicated
  - **Quality notes** — scrape artifacts, duplicates, stale data
  - **Actionability matrix** — which items are reference-only vs. can be locally installed/configured
  - **Cross-reference to existing Hermes setup** — which items are already present in this Hermes instance's skills/plugins

### Phase 3 — Verify
- Read back the generated file, confirm all sections are present
- Verify every URL referenced exists and resolves
- Cross-check against the raw source files to ensure no omissions
- Confirm the deliverable covers all 11 files

---

## 4. Step-by-Step Plan

### Step 1: Create output directory (if missing)
- Path: `~/Desktop/SandBox/docs/catalogs/`
- Command: `mkdir -p ~/Desktop/SandBox/docs/catalogs/`

### Step 2: Write catalog report
- File: `~/Desktop/SandBox/docs/catalogs/awesome-hermes-agent-catalog.md`
- Structure:
  1. Overview (repo, discovered date, file count)
  2. File inventory table (11 rows)
  3. Per-file content summaries (group by directory)
  4. Consolidated resource list (deduplicated external links)
  5. Cross-reference: Hermes skills already present matching community repos
  6. Quality/drift notes
  7. Actionability matrix

### Step 3: Verify
- Read back `awesome-hermes-agent-catalog.md`
- Confirm all 11 files accounted for
- Confirm no placeholder/boilerplate sections
- Count section headers match plan

---

## 5. Files Likely to Change

| File | Action |
|------|--------|
| `~/Desktop/SandBox/docs/catalogs/awesome-hermes-agent-catalog.md` | CREATE |

No existing files are modified.

---

## 6. Tests / Validation

- **Completeness check:** grep through the generated catalog for each of the 11 source filenames — all must appear
- **URL check:** spot-check 3-5 URLs from the external resources table resolve to valid pages
- **Duplicate audit:** confirm the "Quality notes" section flags the known duplications in README.md, CONTRIBUTING.md, preamble.md, and skills-&-plugins.md

---

## 7. Risks, Tradeoffs, and Open Questions

| Risk | Mitigation |
|------|------------|
| URLs in the awesome list may be stale (repo moved, deleted) | The catalog notes the discovery date and flags items as "not verified at write time" |
| Section files in `pages/sections/` may drift from README.md content | Catalog notes they are extracted fragments and may not be in sync |
| The awesome-list repo may have been updated since the 2026-05-06 snapshot | Include a "Last synced" marker in the catalog header |

### Open Questions
1. Should the catalog be a standalone reference doc or should we also install any of the community skills listed?
2. Do we want to cross-reference the community skills (wondelai/skills, litprog-skill, hermes-plugins, etc.) against the current Hermes skill inventory?

---

## 8. Verification Checklist

- [ ] All 11 files are listed in the inventory table
- [ ] Each file has a content summary (1-3 paragraphs)
- [ ] External resources are consolidated and deduplicated
- [ ] Scrape artifacts/duplicates are documented
- [ ] Actionability matrix classifies each file
- [ ] No placeholder/TODO text in the deliverable
- [ ] Deliverable saved under `~/Desktop/SandBox/docs/catalogs/`
