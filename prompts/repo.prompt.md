---
license: MIT
author: Hermes Agent
version: 1.0.0
name: repo
title: Repo Research Pipeline
trigger: /repo
description: >
  Research all 14 projects: web-search for similar projects, guides,
  cheatsheets; create or update RESEARCH_REPORT.md per project in crisp
  markdown. One report per project root. Update projects/RESEARCH_INDEX.md.
mode: agent
system: |
  You are a research agent executing a structured web research pipeline.
  Your job is to produce accurate, web-backed research reports — not to
  invent findings. Every claim must trace to a real web_search result.
  You stop at Phase 5. You do not start branch normalization or migration.
tags:
  - hermes
  - repos
  - research
  - websearch
  - documentation
  - guides
  - cheatsheets
  - pipeline
dependencies:
  - prompt:context-map
  - prompt:update-implementation-plan
  - skill:brainstorming
  - skill:plans-and-specs
  - skill:systematic-debugging
  - skill:context7
  - skill:spike
  - skill:writing-skills
  - skill:content-research-writer
skills:
---

## CRITICAL RULES

> These rules override all other instructions. Violating them produces invalid output.

1. **NO FABRICATION** — Every best practice, pitfall, or resource must trace to a real
   `web_search` result. If search returns nothing useful, write "No new findings" — never
   invent content.
2. **VERIFY BEFORE CLAIMING** — Never report a file count without running
   `find | wc -l`. Never embed a URL without `web_extract` confirming it loads.
3. **SCOPE GUARD** — This prompt covers Phases 0–5 (research + reporting) only.
   Branch normalization, Bun migration, consolidation, and CI setup are secondary goals
   listed in `## Secondary Goals`. Do NOT start them until all 14 reports are verified.
4. **CONSISTENT FORMAT** — All 14 reports must follow the exact template in
   `## Report Template`. Same section headers, same table formats, same ordering.
5. **SIZE GATE** — Reports must be 1KB–5KB. Trim anything over 5KB. Expand anything
   under 1KB. Every section must be actionable for this specific project.

---

## Goal

Research each of the 14 projects under `projects/`. For every project:

1. **Web-search** for similar projects, guides, cheatsheets, best practices.
2. **Extract** useful content: architecture patterns, tool recommendations,
   common pitfalls, performance tips, security hardening.
3. **Update** `RESEARCH_REPORT.md` if it exists — refresh findings, verify
   links, add new discoveries.
4. **Create** `RESEARCH_REPORT.md` if missing — new report from the template in
   `## Report Template`.

**Output:** one `RESEARCH_REPORT.md` per project root. Updated `projects/RESEARCH_INDEX.md`.

---

## Context

**Workspace:** `$HOME/Desktop/SandBox` (resolves to `C:\Users\Alexa\Desktop\SandBox`)

All 14 reports currently exist on disk. Default action is **UPDATE** (refresh findings,
verify links). Only fall back to **CREATE** if a report was deleted between sessions.

### Repo Inventory (14 projects)

| #  | Project                      | Type                                    | Action   |
|----|------------------------------|-----------------------------------------|----------|
| 1  | Banking                      | Fintech (Next.js 16, Drizzle, Plaid/Dwolla) | ✅ Update |
| 2  | comicwise                    | Comic streaming (Next.js 15, Prisma, Stripe) | ✅ Update |
| 3  | cookiecutter-django-tailwind | Django + Tailwind template              | ✅ Update |
| 4  | Django-Scrapy-Selenium       | Web scraping (Django, Scrapy, Selenium) | ✅ Update |
| 5  | ecom                         | Ecommerce (DRF + React/Redux, PayPal)   | ✅ Update |
| 6  | profile                      | Blog/CMS (Django, GCS, CKEditor)        | ✅ Update |
| 7  | Python-projects              | 18 beginner Python scripts              | ✅ Update |
| 8  | rhixe_scans                  | Comic reader (Next.js 15, Prisma, Stripe/PayPal) | ✅ Update |
| 9  | rhixecompany-comics          | Comics platform (Django + Next.js 16)   | ✅ Update |
| 10 | selenium_webdriver           | Browser automation (Node.js, ChromeDriver) | ✅ Update |
| 11 | university-libary-jsm        | Library mgmt (Next.js 15, Drizzle, Neon, Redis) | ✅ Update |
| 12 | xamehi                       | Full-stack (Django + Express + React)   | ✅ Update |
| 13 | xamehi.tv                    | Streaming (DRF + React 17, Redux, MUI)  | ✅ Update |
| 14 | youtube-downloader           | YouTube CLI (yt-dlp, curl_cffi)         | ✅ Update |

---

## Constraints

- Use `context7` for library-specific API docs and patterns.
  Use `web_search` for broader research (similar projects, guides). Do not swap them.
- Use `dispatching-parallel-agents` to process 3–4 projects concurrently.
  Each subagent receives: project name, tech stack, query list, target report path.
- Every report's `## Related Projects` section must cross-reference other workspace
  projects sharing its tech stack. Use each project's `AGENTS.md` for tech overlap.
- Symmetric cross-references: if A references B, B must reference A.
- Do not advance to secondary goals until Phase 5 verification passes for all 14 reports.

---

## Phases

### Phase 0: Prerequisites

Verify tools and workspace before research begins.

**Steps:**

1. Test `web_search` with one real query — confirm results return.
2. Confirm working dir: `pwd` → `$HOME/Desktop/SandBox`
3. Scan disk: `find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | sort`
4. Confirm count = 14. Flag any missing as CREATE targets.

**Tasks:**

- [ ] `web_search` reachable (1 test query returns results)
- [ ] `pwd` matches workspace path
- [ ] 14 reports found on disk

**Actions:**

```
web_search("Next.js 16 best practices 2026", limit=1)
terminal("pwd")
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | sort")
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l")
```

---

### Phase 1: Per-Project Discovery

Gather local context before web research. Read README/AGENTS.md per project to extract
tech stack and generate targeted queries.

**Steps per project:**

1. Read `projects/<name>/README.md` or `package.json` description.
2. Read `projects/<name>/AGENTS.md` — extract framework, database, auth, payments, key tools.
3. Generate 3–5 queries:
   - `"<framework> best practices 2026"`
   - `"<framework> similar open source projects github"`
   - `"<framework> performance optimization cheatsheet"`
   - `"<framework> common pitfalls security hardening"`
   - `"<project-type> architecture guide patterns 2026"`

**Output:** `docs/per-project-research-queries.md` — per-project query matrix.

**Tasks:**

- [ ] README or package.json read for all 14 projects
- [ ] AGENTS.md read for all 14 projects
- [ ] Query list (3–5 queries) generated per project
- [ ] `docs/per-project-research-queries.md` written

**Actions:**

```
read_file("projects/<name>/README.md")
read_file("projects/<name>/AGENTS.md")
write_file("docs/per-project-research-queries.md", content=<query matrix>)
```

---

### Phase 2: Web Research

Execute web searches per project. Extract useful content from top results.

**Steps per project:**

1. Run 3–5 queries from Phase 1 query list.
2. `web_extract` top 3 relevant URLs (official docs, guides — not Wikipedia or bare GitHub READMEs).
3. Synthesize: what is actionable and specific to this project's stack.
4. Note version gaps: latest stable vs. what the project currently uses.

**Parallel execution:** Dispatch 3–4 projects concurrently via `dispatching-parallel-agents`.
Each subagent writes its own `RESEARCH_REPORT.md` directly.

**Per-project tasks:**

- [ ] 2.1 Banking — Next.js 16 + Drizzle + Plaid/Dwolla
- [ ] 2.2 comicwise — Next.js 15 + Prisma + Tailwind + shadcn
- [ ] 2.3 cookiecutter-django-tailwind — Django 5 + Tailwind template
- [ ] 2.4 Django-Scrapy-Selenium — Django 4 + Scrapy + Selenium
- [ ] 2.5 ecom — DRF + React 18 + PayPal
- [ ] 2.6 profile — Django 3 + CKEditor + GCS
- [ ] 2.7 Python-projects — Python scripts collection
- [ ] 2.8 rhixe_scans — Next.js 15 + Prisma + Stripe/PayPal
- [ ] 2.9 rhixecompany-comics — Django 5 + Next.js 16 + Celery + Scrapy
- [ ] 2.10 selenium_webdriver — Node.js + selenium-webdriver
- [ ] 2.11 university-libary-jsm — Next.js 15 + Drizzle + Neon + Upstash
- [ ] 2.12 xamehi — Django DRF + Express + React 18
- [ ] 2.13 xamehi.tv — DRF + React 17 + MUI
- [ ] 2.14 youtube-downloader — yt-dlp + curl_cffi

**Actions:**

```
web_search("<framework> best practices 2026", limit=5)
web_search("<framework> similar open source projects github", limit=5)
web_search("<framework> common pitfalls security hardening", limit=5)
web_extract([top 3–5 relevant URLs from search results])
delegate_task(goal="research <project> and write RESEARCH_REPORT.md", toolsets=["web","file"])
```

---

### Phase 3: Report Writing

Write or update `RESEARCH_REPORT.md` per project using the template in `## Report Template`.

**Steps per project:**

1. If report exists: read current content, merge new findings, remove stale links.
2. If report missing: create from template using Phase 2 research.
3. Verify 2–3 key links with `web_extract` before embedding.
4. Enforce size gate: 1KB–5KB. Cut encyclopedic content.

**Per-project tasks:**

- [ ] 3.1 `projects/Banking/RESEARCH_REPORT.md`
- [ ] 3.2 `projects/comicwise/RESEARCH_REPORT.md`
- [ ] 3.3 `projects/cookiecutter-django-tailwind/RESEARCH_REPORT.md`
- [ ] 3.4 `projects/Django-Scrapy-Selenium/RESEARCH_REPORT.md`
- [ ] 3.5 `projects/ecom/RESEARCH_REPORT.md`
- [ ] 3.6 `projects/profile/RESEARCH_REPORT.md`
- [ ] 3.7 `projects/Python-projects/RESEARCH_REPORT.md`
- [ ] 3.8 `projects/rhixe_scans/RESEARCH_REPORT.md`
- [ ] 3.9 `projects/rhixecompany-comics/RESEARCH_REPORT.md`
- [ ] 3.10 `projects/selenium_webdriver/RESEARCH_REPORT.md`
- [ ] 3.11 `projects/university-libary-jsm/RESEARCH_REPORT.md`
- [ ] 3.12 `projects/xamehi/RESEARCH_REPORT.md`
- [ ] 3.13 `projects/xamehi.tv/RESEARCH_REPORT.md`
- [ ] 3.14 `projects/youtube-downloader/RESEARCH_REPORT.md`

**Actions:**

```
read_file("projects/<name>/RESEARCH_REPORT.md")        # if exists — for UPDATE
write_file("projects/<name>/RESEARCH_REPORT.md", content=<report>)
web_extract([url1, url2, url3])                         # verify key links
```

---

### Phase 4: Index & Cross-Reference

Update the master index. Verify cross-references are symmetric.

**Steps:**

1. Scan disk: `find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md'`
2. Rewrite `projects/RESEARCH_INDEX.md` — 14 rows, file size, last-updated date.
3. For each report, verify `## Related Projects` lists all workspace projects sharing
   its tech stack. Add missing references.
4. Confirm symmetry: if A references B, read B and confirm B references A.

**Tasks:**

- [ ] Disk scan returns exactly 14 reports
- [ ] `projects/RESEARCH_INDEX.md` rewritten with size + date per report
- [ ] Cross-reference matrix symmetric across all 14 reports

**Actions:**

```
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' -exec ls -lh {} \\;")
write_file("projects/RESEARCH_INDEX.md", content=<updated index>)
```

---

### Phase 5: Verification

All gates must pass before this prompt is considered complete.

**Steps:**

1. Count: `find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l` → must be 14.
2. Sections: each report must have 9+ `## ` sections.
3. URLs: spot-check 2 URLs per report (28 total) via `web_extract` — confirm non-404.
4. Size: every report between 1KB and 5KB.

**Tasks:**

- [ ] Count = 14
- [ ] Every report has ≥ 9 `## ` sections
- [ ] 28 URL spot-checks pass
- [ ] All reports 1KB–5KB

**Actions:**

```
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l")
terminal("for f in projects/*/RESEARCH_REPORT.md; do echo \"=== $f ===\"; grep -c '^## ' \"$f\"; wc -c \"$f\"; done")
```

---

## Report Template

Every `RESEARCH_REPORT.md` must follow this structure exactly. Do not add or remove
top-level sections. Subsections under `## Key Findings` are tech-specific and variable.

```markdown
# RESEARCH_REPORT.md

## Project: <name>

**Type:** <project type>
**Tech Stack:** <framework>, <database>, <auth>, <other key tech>
**Status:** Active | Stale | Consolidation target

## Similar Projects

| Project | URL | Why Relevant |
|---------|-----|--------------|
| <name>  | <github url> | <1-line relevance> |

## Key Findings

### <Technology/Topic>

<2–3 crisp bullets — each backed by a web_search result>

### <Technology/Topic>

<2–3 crisp bullets>

## Cheatsheets & Quick Reference

| Topic | Resource | Type |
|-------|----------|------|
| <topic> | <url> | Cheatsheet / Guide / Docs |

## Best Practices

1. **<practice>** — <one-line why>
2. **<practice>** — <one-line why>
3. **<practice>** — <one-line why>
4. **<practice>** — <one-line why>
5. **<practice>** — <one-line why>

## Common Pitfalls

| Pitfall | Impact | Avoidance |
|---------|--------|-----------|
| <pitfall> | <impact> | <one-line fix> |

## Performance

<Top 3–5 performance optimizations specific to this project's stack>

## Security

<Top 3–5 security considerations for this project's stack>

## Related Projects (in workspace)

<Cross-references to other workspace projects sharing this tech stack.
List project name + shared technology. Must be symmetric.>

## Resources

| Resource      | URL   | Description                  |
|---------------|-------|------------------------------|
| Official Docs | <url> | <framework> documentation    |
| Community     | <url> | Forum / Discord / Reddit     |
| Tutorial      | <url> | Key tutorial or guide        |
```

---

## Acceptance Criteria

| Gate | Condition | Verification Command |
|------|-----------|----------------------|
| All 14 reports exist | count = 14 | `find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' \| wc -l` |
| Each report ≥ 9 sections | `grep -c '^## '` ≥ 9 | per-report loop |
| No report under 1KB | `wc -c` ≥ 1024 | per-report loop |
| No report over 5KB | `wc -c` ≤ 5120 | per-report loop |
| 28 URL spot-checks pass | `web_extract` non-404 | Phase 5 step 3 |
| RESEARCH_INDEX.md current | 14 rows, size + date correct | read + verify |
| No fabricated findings | every fact traces to `web_search` | manual review |
| Scope respected | no branch/migration work started | agent self-check |

---

## Skills Required

| Skill | Phase | Purpose |
|-------|-------|---------|
| `brainstorming` | 1 | Explore research angles per project |
| `plans-and-specs` | 0 | Structure research plan |
| `systematic-debugging` | 0, 5 | Detect stale/missing reports |
| `context7` | 2 | Library API docs and patterns |
| `spike` | 0 | Prototype report format before batch |
| `writing-skills` | 3 | Crisp, compact markdown writing |
| `content-research-writer` | 3 | Research synthesis |

---

## Actions

- `web_search("<query>", limit=5)` — Search for guides, similar projects, cheatsheets
- `web_extract([urls])` — Extract content from URLs; verify links before embedding
- `read_file("projects/<name>/README.md")` — Read project description
- `read_file("projects/<name>/AGENTS.md")` — Read tech stack and setup commands
- `read_file("projects/<name>/RESEARCH_REPORT.md")` — Read existing report for UPDATE
- `write_file(path, content)` — Create or update RESEARCH_REPORT.md
- `terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l")` — Count reports
- `terminal("for f in projects/*/RESEARCH_REPORT.md; do wc -c \"$f\"; done")` — Check sizes
- `search_files(pattern="^## ", path="projects/<name>/RESEARCH_REPORT.md")` — Verify sections
- `skill_view(name="content-research-writer")` — Load research writing skill
- `skill_view(name="writing-skills")` — Load crisp writing skill
- `delegate_task(goal, toolsets=["web","file"])` — Delegate per-project research
- `dispatching-parallel-agents` — Research 3–4 projects concurrently

---

## Secondary Goals

> Execute ONLY after Phase 5 verification passes for all 14 reports.
> Full specifications live in `.github/prompts/repo-management.prompt.md`.

| # | Goal | Priority |
|---|------|----------|
| 1 | Consolidation — comicwise + Django-Scrapy-Selenium + selenium_webdriver → rhixecompany-comics | P1 |
| 2 | Branch normalization — `development` + `production` only per repo | P2 |
| 3 | Ignore file audit — fix all `.*ignore` files | P3 |
| 4 | Dependency audit — clean package.json / requirements.txt | P4 |
| 5 | Bun migration — npm/pnpm → bun for JS/TS repos | P5 |
| 6 | CI workflow setup — GitHub Actions for all repos | P6 |

---

## Related Prompts

| Prompt | Location | Purpose |
|--------|----------|---------|
| `/bash-scripts-fix` | `.github/prompts/bash-scripts-fix.prompt.md` | Script modernization for all 14 projects |
| `/workspace-consolidate` | `.github/prompts/workspace-consolidate.prompt.md` | Workspace-level consolidation |
| `/repo-management` | `.github/prompts/repo-management.prompt.md` | Branch norm, Bun migration, CI, consolidation |

## Template References

Templates in `templates/repo.prompts/`:
- `README.md` — Section inventory
