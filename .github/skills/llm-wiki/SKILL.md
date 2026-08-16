---
author: Hermes Agent
description: 'Karpathy''s LLM Wiki: build/query interlinked markdown KB.'
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: llm-wiki
tags:
- imported
title: LLM Wiki
version: 2.1.0
---
# Karpathy's LLM Wiki

Build and maintain a persistent, compounding knowledge base as interlinked markdown files.
Based on [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).

Unlike traditional RAG (which rediscovers knowledge from scratch per query), the wiki compiles knowledge once and keeps it current. Cross-references are already there. Contradictions have already been flagged.

**Division of labor:** The human curates sources and directs analysis. The agent summarizes, cross-references, files, and maintains consistency.

## Overview

Automated reasoning and workflow tool for `llm-wiki`. Execute multi-step tasks with deterministic quality controls and structured outputs.

## When to Use

- Asked to create, build, or start a wiki or knowledge base
- Asked to ingest, add, or process a source into their wiki
- Asked about a topic where an existing wiki is present at the configured path
- Asked to lint, audit, or health-check their wiki
- User references their wiki, knowledge base, or notes in a research context

## Wiki Location

**Location:** Set via `WIKI_PATH` environment variable (e.g., in `~/AppData/Local/hermes/.env`). Defaults to `~/wiki`.

```bash
WIKI="${WIKI_PATH:-$HOME/wiki}"
```

The wiki is just a directory of markdown files — open it in Obsidian, VS Code, or any editor.

## Architecture: Three Layers

```
wiki/
├── SCHEMA.md           # Conventions, structure rules, domain config
├── index.md            # Sectioned content catalog with one-line summaries
├── log.md              # Chronological action log (append-only, rotated yearly)
├── raw/                # Layer 1: Immutable source material
├── entities/           # Layer 2: Entity pages (people, orgs, products, models)
├── concepts/           # Layer 2: Concept/topic pages
├── comparisons/        # Layer 2: Side-by-side analyses
└── queries/            # Layer 2: Filed query results worth keeping
```

## Resuming an Existing Wiki (mandatory every session)

Always orient yourself before doing anything:

1. Read `SCHEMA.md` — understand the domain, conventions, and tag taxonomy
2. Read `index.md` — learn what pages exist and their summaries
3. Scan recent `log.md` — read the last 20-30 entries

## Core Operations

### 1. Ingest

1. Capture the raw source (URL → `web_extract`, PDF, pasted text) to `raw/`
2. Add raw frontmatter (`source_url`, `ingested`, `sha256`)
3. Discuss takeaways with the user (skip in automated contexts)
4. Check what already exists via `index.md` and `search_files`
5. Write or update wiki pages with cross-references and tags
6. Update `index.md` and append to `log.md`
7. Report what changed to the user

### 2. Query

1. Read `index.md` to identify relevant pages
2. For wikis 100+ pages, also `search_files` across all `.md` files
3. Read relevant pages and synthesize an answer citing wiki pages
4. File valuable answers to `queries/` or `comparisons/`
5. Update `log.md`

### 3. Lint

See `references/lint-reference.md` for the full lint checklist (orphan pages, broken wikilinks, index completeness, frontmatter validation, stale content, contradictions, quality signals, source drift, page size, tag audit, log rotation).

## Searching the Wiki

```bash
# Find pages by content
search_files "transformer" path="$WIKI" file_glob="*.md"
# Find pages by filename
search_files "*.md" target="files" path="$WIKI"
# Recent activity
read_file "$WIKI/log.md" offset=<last 20 lines>
```

## Bulk Ingest

When ingesting multiple sources: read all first, identify all entities across all sources, check existing pages in one pass, create/update in one pass, update `index.md` once, write one log entry.

## Archiving

Move superseded pages to `_archive/`, remove from `index.md`, update inbound wikilinks, log the action.

## Reference Files

- `references/schema-template.md` — Full SCHEMA.md template with conventions, frontmatter, tag taxonomy
- `references/index-templates.md` — index.md and log.md templates with scaling rules
- `references/lint-reference.md` — Complete lint checklist with 11 audit points
- `references/obsidian-integration.md` — Obsidian desktop vault setup and headless sync for servers

## Pitfalls

- **Never modify files in `raw/`** — sources are immutable. Corrections go in wiki pages
- **Always orient first** — read SCHEMA + index + recent log before any operation
- **Always update index.md and log.md** — these are the navigational backbone
- **Don't create pages for passing mentions** — follow the Page Thresholds
- **Don't create pages without cross-references** — every page must link to at least 2 others
- **Handle contradictions explicitly** — don't silently overwrite; note both claims with dates
- **Tags must come from the taxonomy** — freeform tags decay into noise
- **Rotate the log** — when log.md exceeds 500 entries, rename it `log-YYYY.md`

## Verification Checklist

- [ ] WIKI_PATH environment variable set (or default ~/wiki used)
- [ ] SCHEMA.md, index.md, log.md exist in wiki root
- [ ] Orientation steps completed before operations
- [ ] All ingest steps followed correctly
- [ ] Lint passes before claiming wiki health

## Workflow

### Phase 1: Preparation

Set up required environment, dependencies, and configuration for LLM Wiki.

### Phase 2: Execution

Run the primary LLM Wiki operations according to the defined requirements.

### Phase 3: Verification

Verify output, handle any errors, and confirm results meet expectations.

### Phase 4: Completion

Document results, clean up resources, and finalize any deliverables.

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
