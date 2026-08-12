---
name: repo
title: Repo Research Pipeline + Quick Onboarding
description: 'Research all 17 projects via delegated sub-prompts: web search for similar projects, guides, cheatsheets; create or update RESEARCH_REPORT.md per project in crisp markdown. Delegates web research to web-research-pipeline.prompt.md and post-research ops to repo-management.prompt.md. Also includes Quick Repo Onboarding (Q1-Q4): summarize repo in 5 bullets, find main entrypoint, check current directory, set up GitHub PR workflow, check disk usage.'
version: 2.2.0
license: MIT
author: Hermes Agent
toolsets:
- browser
- code_execution
- file
- mcp
- terminal
- vision
- web
scripts: []
skills:
- brainstorming
- code-wiki
- content-research-writer
- gh-cli
- git-commit
- git-submodule-workflow
- github-repo-management
- plans-and-specs
- spike
- systematic-debugging
- web-research-pipeline
- writing-clearly-and-concisely
- writing-skills
- subagent-driven-development
- firecrawl-search
- firecrawl-scrape
formatter: default
plan: null
dependencies:
- prompt:context-map
- prompt:repo-management
- prompt:repo-research-pipeline
- prompt:repo-story-time
- prompt:update-implementation-plan
- prompt:web-research-pipeline
- skill:brainstorming
- skill:code-wiki
- skill:content-research-writer
- skill:gh-cli
- skill:git-commit
- skill:git-submodule-workflow
- skill:github-repo-management
- skill:plans-and-specs
- skill:spike
- skill:systematic-debugging
- skill:web-research-pipeline
- skill:writing-clearly-and-concisely
- skill:writing-skills
- skill:subagent-driven-development
- skill:firecrawl-search
- skill:firecrawl-scrape
- tool:mcp-filesystem
- tool:mcp-github
- tool:mcp-memory
- tool:mcp-sequential-thinking
- tool:mcp-tavily
tags:
- architecture
- frontend
- git
- mcp
- onboarding
- performance
- prompts
- security
- typescript
- vscode
trigger: /repo
metadata:
  hermes: {}
mode: agent
system: You are a research orchestrator. Delegate web research to web-research-pipeline sub-prompt. Stop at Phase 4 (verification). Do not start branch normalization or migration — those live in repo-management.prompt.md.
---

## Goal

Research each of the 17 projects under `projects/`. For every project:

1. **Web-search** for similar projects, guides, cheatsheets, best practices.

2. **Extract** useful content: architecture patterns, tool recommendations, common pitfalls, performance tips, security hardening.

3. **Update** `RESEARCH_REPORT.md` if it exists — refresh findings, verify links, add new discoveries.

4. **Create** `RESEARCH_REPORT.md` if missing — new report from the template in the Report Template section.

**Output:** one `RESEARCH_REPORT.md` per project root. Updated `projects/RESEARCH_INDEX.md`.

---

## Context

**Workspace:** `$HOME/Desktop/SandBox` (resolves to `C:\Users\Alexa\Desktop\SandBox`)

All 16 reports currently exist on disk; 1 project (`mcp-servers`) needs its report created.
Default action is **UPDATE** (refresh findings, verify links). Only fall back to **CREATE** if a report was deleted or for `mcp-servers`.

### Repo Inventory (17 projects)

| #  | Project                      | Type                                             | Action   |
| -- | ---------------------------- | ------------------------------------------------ | -------- |
| 1  | Banking                      | Fintech (Next.js 16, Drizzle, Plaid/Dwolla)      | ✅ Update |
| 2  | comicwise                    | Comic streaming (Next.js 15, Prisma, Stripe)     | ✅ Update |
| 3  | cookiecutter-django-tailwind | Django + Tailwind template                       | ✅ Update |
| 4  | Django-Scrapy-Selenium       | Web scraping (Django, Scrapy, Selenium)          | ✅ Update |
| 5  | ecom                         | Ecommerce (DRF + React/Redux, PayPal)            | ✅ Update |
| 6  | profile                      | Blog/CMS (Django, GCS, CKEditor)                 | ✅ Update |
| 7  | Python-projects              | 18 beginner Python scripts                       | ✅ Update |
| 8  | rhixe_scans                  | Comic reader (Next.js 15, Prisma, Stripe/PayPal) | ✅ Update |
| 9  | rhixecompany-comics          | Comics platform (Django + Next.js 16)            | ✅ Update |
| 10 | selenium_webdriver           | Browser automation (Node.js, ChromeDriver)       | ✅ Update |
| 11 | university-libary-jsm        | Library mgmt (Next.js 15, Drizzle, Neon, Redis)  | ✅ Update |
| 12 | xamehi                       | Full-stack (Django + Express + React)            | ✅ Update |
| 13 | xamehi.tv                    | Streaming (DRF + React 17, Redux, MUI)           | ✅ Update |
| 14 | youtube-downloader           | YouTube CLI (yt-dlp, curl_cffi)                  | ✅ Update |
| 15 | Bash                         | Automation Toolkit (Bun/TypeScript)              | ✅ Update |
| 16 | Resume_maker                 | Job Documents Generator (Bun/CLI)                | ✅ Update |
| 17 | mcp-servers                  | Multi-language MCP server implementations        | ❌ Create |

## Constraints

- **Tavily MCP-first:** Use `mcp__tavily__tavily_search` for web search and `mcp__tavily__tavily_extract` for content extraction. Fall back to `mcp__fetch__get_markdown` then `web_extract` if Tavily is unavailable.
- Use `context7` for library-specific API docs and patterns. Do not swap them.
- **Sub-prompt delegation:** Phase 1 delegates to `web-research-pipeline.prompt.md`. Do NOT re-implement web research inline — run the sub-prompt and use its output.
- Use `dispatching-parallel-agents` to process 3–4 projects concurrently. Each subagent receives: project name, tech stack, query list, target report path.
- Every report's `## Related Projects` section must cross-reference other workspace projects sharing its tech stack. Use each project's `AGENTS.md` for tech overlap.
- Symmetric cross-references: if A references B, B must reference A.
- Do not advance to secondary goals until Phase 4 verification passes for all 17 reports.

## Phases

### Phase 0: Prerequisites

Verify tools and workspace before research begins.

**Steps:**

1. Test `mcp__tavily__tavily_search` with one real query — confirm results return.
2. Confirm working dir: `pwd` → `$HOME/Desktop/SandBox`
3. Scan disk: `find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | sort`
4. Confirm count = 16 (existing), flag `mcp-servers` as CREATE target.

**Tasks:**

- [ ] `mcp__tavily__tavily_search` reachable (1 test query returns results)
- [ ] `pwd` matches workspace path
- [ ] 16 existing reports found, 1 flagged for CREATE

**Actions:**

```python
tool_call(name="mcp__tavily__tavily_search", arguments={"query": "Next.js 16 best practices 2026", "max_results": 3})
terminal("pwd")
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | sort")
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l")
```

---

### Phase 1: Web Research (delegated)

> Full workflow lives in `prompts/web-research-pipeline.prompt.md`.
> Orchestrator at `prompts/repo-research-pipeline.prompt.md`.

Delegate per-project web research. For each of the 17 projects:

1. Read `projects/<name>/README.md` and `AGENTS.md` to extract tech stack.
2. Run `web-research-pipeline.prompt.md` trigger with project name + stack params.
3. Let the sub-prompt handle: query generation, `mcp__tavily__tavily_search`, `mcp__tavily__tavily_extract`, and top-N URL synthesis.

**Parallel execution:** Dispatch 3–4 projects concurrently via `delegate_task`.
Each subagent receives: project name, tech stack, query list, target report path.

**Tasks:**

- [ ] 1.1–1.17 README + AGENTS.md read for all 17 projects
- [ ] `docs/per-project-research-queries.md` written per project
- [ ] All 17 delegated web-research runs completed

**Actions:**

```python
read_file("projects/<name>/README.md")
read_file("projects/<name>/AGENTS.md")
# Delegate to sub-prompt:
delegate_task(goal="Run web-research-pipeline prompt for project <name> with stack <tech>", toolsets=["web", "file", "mcp"])
```

---

### Phase 2: Report Writing

Write or update `RESEARCH_REPORT.md` per project using the template in `## Report Template`. Research data comes from Phase 1's delegated runs.

**Steps per project:**

1. If report exists: read current content, merge new findings, remove stale links.
2. If report missing: create from template using Phase 1 research output.
3. Verify 2–3 key links with `mcp__tavily__tavily_extract` before embedding.
4. Enforce size gate: 1KB–5KB. Cut encyclopedic content.

**Tasks:**

- [ ] 2.1–2.17 All 17 RESEARCH_REPORT.md files written/updated (17 new for `mcp-servers`)

**Actions:**

```python
read_file("projects/<name>/RESEARCH_REPORT.md")  # if exists — for UPDATE
write_file("projects/<name>/RESEARCH_REPORT.md", content=<report>)
tool_call(name="mcp__tavily__tavily_extract", arguments={"urls": [url1, url2, url3]})  # verify key links
```

---

### Phase 3: Index & Cross-Reference

Update the master index. Verify cross-references are symmetric.

**Steps:**

1. Scan disk: `find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md'`
2. Rewrite `projects/RESEARCH_INDEX.md` — 17 rows, file size, last-updated date.
3. For each report, verify `## Related Projects` lists all workspace projects sharing its tech stack. Add missing references for `mcp-servers`.
4. Confirm symmetry: if A references B, read B and confirm B references A.

**Tasks:**

- [ ] Disk scan returns exactly 17 reports
- [ ] `projects/RESEARCH_INDEX.md` rewritten with size + date per report
- [ ] Cross-reference matrix symmetric across all 17 reports

**Actions:**

```python
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' -exec ls -lh {} \;")
write_file("projects/RESEARCH_INDEX.md", content=<updated index>)
```

---

### Phase 4: Verification

All gates must pass before this prompt is considered complete.

**Steps:**

1. Count: `find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l` → must be 17.
2. Sections: each report must have 9+ `##` sections.
3. URLs: spot-check 2 URLs per project (34 total) via `mcp__tavily__tavily_extract` — confirm non-404.
4. Size: every report between 1KB and 5KB.

**Tasks:**

- [ ] Count = 17
- [ ] Every report has ≥ 9 `##` sections
- [ ] 34 URL spot-checks pass
- [ ] All reports 1KB–5KB

**Actions:**

```python
terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l")
terminal("for f in projects/*/RESEARCH_REPORT.md; do echo \"=== $f ===\"; grep -c '^## ' \"$f\"; wc -c \"$f\"; done")
```

---

## Quick Repo Onboarding

Run these lightweight intros when the user asks simple questions about the repo itself (not the 17 project research pipeline).

### Q1: "Summarize this repo in 5 bullets and tell me what the main entrypoint is."

**Phase: Onboarding — Single Repo**

1. Read root files: `AGENTS.md`, `README.md`, `package.json`/`pyproject.toml`/`Cargo.toml`
2. List top-level structure: `ls -la`
3. Identify the main entrypoint (look for `main.py`, `index.ts`, `index.js`, `src/main.rs`, `cmd/`, `Program.cs`, or the `main`/`start`/`scripts` field in the manifest)
4. Summarize in 5 bullets: what the repo is, tech stack, architecture shape, build/test commands, and the main entrypoint path

**Actions:**

```bash
read_file("AGENTS.md")
read_file("README.md")
read_file("package.json") or read_file("pyproject.toml")
ls -la && find . -maxdepth 3 -not -path '*/\.*' -not -path '*/node_modules/*' -not -path '*/venv/*' | head -40
grep -E '"main"|"start"|main\.py|def main|if __name__|fn main' package.json pyproject.toml src/*.py src/*.ts 2>/dev/null | head -10
```

### Q2: "Check my current directory and tell me what looks like the main project file."

**Phase: Onboarding — Current Directory**

1. `pwd` to confirm current directory
2. `ls -la` for file listing, sorted by recency or size
3. Read the most likely manifest (whatever config/file the directory contains)
4. Report the dominant file type and the single most important file (the one with the entrypoint, build config, or primary data)

**Actions:**

```bash
pwd && ls -la
ls -la | head -30
file * 2>/dev/null | head -20
```

### Q3: "Help me set up a clean GitHub PR workflow for this codebase."

**Phase: Onboarding — CI/GitHub**

1. Detect project type (JS/TS → Bun or npm; Python → uv/pip; Rust → cargo; Go → go)
2. Create `.github/workflows/ci.yml` from the detected type template.
3. If `monorepo-pr-workflow` skill exists, load it for monorepo-specific branch/PR patterns.
4. Suggest: branch protection rules (`development` + `production`), conventional commits, PR template.

Templates cover:

- **JS/TS:** `oven-sh/setup-bun`, `bun install`, `bun run build`, `bun run test` (or `npm` equivalent)
- **Python:** `actions/setup-python`, `uv sync`/`pip install`, `ruff check`, `pytest`
- **Generic:** `actions/checkout`, `setup-language`, `lint`, `test`

**Actions:**

```bash
skill_view(name="monorepo-pr-workflow")
read_file("AGENTS.md")  # for existing CI patterns
ls .github/workflows/ 2>/dev/null || echo 'no workflows yet'
```

### Q4: "What's my disk usage? Show the top 5 largest directories."

**Phase: Onboarding — Disk Analysis**

1. Run disk usage scan from the repo root (or workspace root)
2. Exclude noise directories (`.git`, `node_modules`, `venv`, `.venv`, `__pycache__`, `dist`, `build`, `target`)
3. Show top 5 largest directories by size

**Actions:**

```bash
du -sh --exclude='.git' --exclude='node_modules' --exclude='venv' --exclude='__pycache__' --exclude='dist' --exclude='build' --exclude='target' */ 2>/dev/null | sort -rh | head -5
# Fallback for bare repos:
du -sh --exclude='.git' */ 2>/dev/null | sort -rh | head -5
```

---

## Report Template

Every `RESEARCH_REPORT.md` must follow this structure exactly. Do not add or remove top-level sections. Subsections under `## Key Findings` are tech-specific and variable.

```markdown
# RESEARCH_REPORT.md

## Project: <name>

**Type:** <project type>
**Tech Stack:** <framework>, <database>, <auth>, <other key tech>
**Status:** Active | Stale | Consolidation target

## Similar Projects

| Project | URL          | Why Relevant       |
| ------- | ------------ | ------------------ |
| <name>  | <github url> | <1-line relevance> |

## Key Findings

### <Technology/Topic>

- <2–3 crisp bullets — each backed by a web_search result>

### <Technology/Topic>

- <2–3 crisp bullets>

## Cheatsheets & Quick Reference

| Topic   | Resource | Type                      |
| ------- | -------- | ------------------------- |
| <topic> | <url>    | Cheatsheet / Guide / Docs |

## Best Practices

1. **<practice>** — <one-line why>
2. **<practice>** — <one-line why>
3. **<practice>** — <one-line why>
4. **<practice>** — <one-line why>
5. **<practice>** — <one-line why>

## Common Pitfalls

| Pitfall   | Impact   | Avoidance      |
| --------- | -------- | -------------- |
| <pitfall> | <impact> | <one-line fix> |

## Performance

<Top 3–5 performance optimizations specific to this project's stack>

## Security

<Top 3–5 security considerations for this project's stack>

## Related Projects (in workspace)

<Cross-references to other workspace projects sharing this tech stack.
List project name + shared technology. Must be symmetric.>

## Resources

| Resource      | URL   | Description               |
| ------------- | ----- | ------------------------- |
| Official Docs | <url> | <framework> documentation |
| Community     | <url> | Forum / Discord / Reddit  |
| Tutorial      | <url> | Key tutorial or guide     |
```

---

## Acceptance Criteria

| Gate                      | Condition                              | Verification Command                                     |        |
| ------------------------- | -------------------------------------- | -------------------------------------------------------- |        |
| All 17 reports exist      | count = 17                             | `find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' \ | wc -l` |
| Each report ≥ 9 sections  | `grep -c '^## '` ≥ 9                   | per-report loop                                          |        |
| No report under 1KB       | `wc -c` ≥ 1024                         | per-report loop                                          |        |
| No report over 5KB        | `wc -c` ≤ 5120                         | per-report loop                                          |        |
| 34 URL spot-checks pass   | `web_extract` non-404                  | Phase 4 step 3                                           |        |
| RESEARCH_INDEX.md current | 17 rows, size + date correct           | read + verify                                            |        |
| No fabricated findings    | every fact traces to `web_search`      | manual review                                            |        |
| Scope respected           | no branch/migration work started       | agent self-check                                         |        |
| Sub-prompts accessible    | `.github/prompts/*.prompt.md` resolves | file check                                               |        |

---

## Skills Required

> See full table with per-domain purposes:
> [`templates/_shared/skills-table-core.md`](templates/_shared/skills-table-core.md)

| Skill                           | Phase | Purpose                                       |
| ------------------------------- | ----- | --------------------------------------------- |
| `brainstorming`                 | 1     | Explore research angles per project           |
| `plans-and-specs`               | 0     | Structure research plan                       |
| `systematic-debugging`          | 0, 4  | Detect stale/missing reports                  |
| `context7`                      | 1     | Library API docs and patterns                 |
| `spike`                         | 0     | Prototype report format before batch          |
| `writing-skills`                | 2     | Crisp, compact markdown writing               |
| `content-research-writer`       | 2     | Research synthesis                            |
| `repo-management`               | —     | Post-research: branch norm, CI, consolidation |
| `repo-story-time`               | —     | Git history analysis and repo narrative       |
| `web-research-pipeline`         | 1     | Delegated web search + extraction             |
| `repo-research-pipeline`        | 1     | Multi-project research orchestrator           |
| `github-repo-management`        | —     | GitHub repo operations for post-research      |
| `code-wiki`                     | —     | Repo analysis for repo-story-time             |
| `writing-clearly-and-concisely` | —     | Clean writing for repo-story-time             |

---

## Actions

- `mcp__tavily__tavily_search` — Search the web for guides, similar projects, cheatsheets (Tavily MCP)
- `mcp__tavily__tavily_extract` — Extract content from URLs, verify links before embedding (Tavily MCP)
- `mcp__tavily__tavily_research` — Deep research on a topic across multiple sources (Tavily MCP)
- `read_file("projects/<name>/README.md")` — Read project description
- `read_file("projects/<name>/AGENTS.md")` — Read tech stack and setup commands
- `read_file("projects/<name>/RESEARCH_REPORT.md")` — Read existing report for UPDATE
- `write_file(path, content)` — Create or update RESEARCH_REPORT.md
- `terminal("find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l")` — Count reports
- `terminal("for f in projects/*/RESEARCH_REPORT.md; do wc -c \"$f\"; done")` — Check sizes
- `search_files(pattern="^## ", path="projects/<name>/RESEARCH_REPORT.md")` — Verify sections
- `skill_view(name="content-research-writer")` — Load research writing skill
- `skill_view(name="writing-skills")` — Load crisp writing skill
- `delegate_task(goal, toolsets=["web","file","mcp"])` — Delegate per-project research

---

## Secondary Goals

> Execute ONLY after Phase 4 verification passes for all 17 reports.
> Full specifications live in `prompts/repo-management.prompt.md`.

| # | Goal                                                                                          | Priority |
| - | --------------------------------------------------------------------------------------------- | -------- |
| 1 | Consolidation — comicwise + Django-Scrapy-Selenium + selenium_webdriver → rhixecompany-comics | P1       |
| 2 | Branch normalization — `development` + `production` only per repo                             | P2       |
| 3 | Ignore file audit — fix all `.*ignore` files                                                  | P3       |
| 4 | Dependency audit — clean package.json / requirements.txt                                      | P4       |
| 5 | Bun migration — npm/pnpm → bun for JS/TS repos                                                | P5       |
| 6 | CI workflow setup — GitHub Actions for all repos                                              | P6       |

---

## Related Prompts

| Prompt                    | Location                                   | Purpose                                       |
| ------------------------- | ------------------------------------------ | --------------------------------------------- |
| `/bash-scripts-fix`       | `prompts/bash-scripts-fix.prompt.md`       | Script modernization for all 16 projects      |
| `/workspace-consolidate`  | `prompts/workspace-consolidate.prompt.md`  | Workspace-level consolidation                 |
| `/repo-management`        | `prompts/repo-management.prompt.md`        | Branch norm, Bun migration, CI, consolidation |
| `/repo-story-time`        | `prompts/repo-story-time.prompt.md`        | Git history analysis and repo narrative       |
| `/web-research-pipeline`  | `prompts/web-research-pipeline.prompt.md`  | Web search + extraction per project           |
| `/repo-research-pipeline` | `prompts/repo-research-pipeline.prompt.md` | Multi-project research orchestrator           |

---

## Template References

- Shared templates: `templates/_shared/` (rules-core, personas, personality, section-skeleton, deps-core, skills-table-core, best-practices)
- Report template: `## Report Template` section above (canonical)

## Personas

See [`templates/_shared/personas.md`](templates/_shared/personas.md) for shared persona templates.

| Persona       | When to Use                            |
| ------------- | -------------------------------------- |
| **Developer** | Implementation, debugging, refactoring |
| **Reviewer**  | Code review, quality assurance         |
| **User**      | General purpose, operations            |

## Personality

See [`templates/_shared/personality.md`](templates/_shared/personality.md) for shared personality guidelines.

- **Tone**: Direct, practical, actionable
- **Style**: Structured with clear steps and verification
- **Avoid**: Ambiguity, assumptions, scope creep
- **Encourage**: Evidence-based decisions, minimal changes

## Rules

See core rules: [`templates/_shared/rules-core.md`](templates/_shared/rules-core.md)

### Domain Rules

- Fix root causes, not symptoms.
- Check siblings for the same flaw.
- Restore from git clean before retrying.

### Standing Rules

1. **Map before touch** — Understand before making changes.
2. **Smallest safe change** — Minimal change that achieves the goal.
3. **Verify before claim** — Test before reporting complete.
4. **Report blockers** — State clearly when something fails.

## Workflow

See [`templates/_shared/section-skeleton.md`](templates/_shared/section-skeleton.md) for workflow structure.

1. **Diagnose** — Run diagnostics.
2. **Plan** — Determine minimal changes.
3. **Fix** — Apply changes incrementally.
4. **Verify** — Confirm fix works.
5. **Document** — Note what changed.

## Verification Checklist

| # | Gate       | Criterion                           |
| - | ---------- | ----------------------------------- |
| 1 | Scope      | Change matches the original request |
| 2 | Quality    | Meets project standards             |
| 3 | Tests      | Tests pass (if applicable)          |
| 4 | Regression | No unintended side effects          |
| 5 | Docs       | Changes documented if needed        |

## Dependencies

See [`templates/_shared/deps-core.md`](templates/_shared/deps-core.md) for shared dependency patterns.

## Subgoals

1. **Prepare** — Understand requirements and prerequisites.
2. **Execute** — Follow structured workflow with incremental progress.
3. **Verify** — Confirm output meets requirements and standards.
4. **Document** — Record results, decisions, and lessons learned.

## MCP Servers & Tools

The following MCP servers and tools are available for this task. Use them in preference to native equivalents per MCP-first tooling policy.

| Server                | Purpose                                                |
| --------------------- | ------------------------------------------------------ |
| `tavily`              | Web search + URL extraction (primary research backend) |
| `fetch`               | Web page content extraction fallback                   |
| `filesystem`          | File read/write operations                             |
| `github`              | GitHub API operations                                  |
| `memory`              | Persistent memory operations                           |
| `sequential-thinking` | Structured reasoning for complex problems              |
| `context7`            | Library API docs and patterns                          |
| `ast-grep`            | AST-based code search and replace                      |
| `playwright`          | Browser automation for interactive pages               |

## Hooks

The following workspace hooks run around this prompt's execution (see `.github/hooks/README.md`):

| Hook                     | When              | Behavior                     |
| ------------------------ | ----------------- | ---------------------------- |
| `session-logger`         | session start/end | Logs session metadata        |
| `governance-audit`       | session events    | Audits governance compliance |
| `session-auto-commit`    | session end       | Auto-commits session state   |
| `pre-exec-validate.sh`   | before commands   | Validates command execution  |
| `post-exec-state-log.py` | after commands    | Appends state log            |

## Tasks

- [ ] Understand requirements and scope
- [ ] Plan approach and identify resources
- [ ] Execute work incrementally
- [ ] Verify against acceptance criteria
- [ ] Document results and decisions
