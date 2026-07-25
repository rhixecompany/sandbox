---
author: Alexa
description: 'Structured workflow for executing web research across multiple projects using MCP tools (mcp-github, mcp-fetch, mcp-smithery, mcp-filesystem) plus skills: web-research-pipeline, domain-intel, firecrawl-*. Produces RESEARCH_REPORT.md files with verified sources.'
license: MIT
name: repo-research-pipeline
tags:
- research
- repo
- github
- mcp
- reporting
title: Repo Research Pipeline (MCP-Enhanced)
version: 2.0.0

---
# Repo Research Pipeline (MCP-Enhanced)

Structured workflow for executing web research across multiple projects and writing actionable RESEARCH_REPORT.md files per project. Uses MCP tools (mcp-github, mcp-fetch, mcp-smithery, mcp-filesystem) and related research skills for deeper, verified results.

## Skills Required

| Skill | Purpose |
|-------|---------|
| `mcp-github` | Search repos, code, issues for similar projects/patterns |
| `mcp-fetch` | Fetch API docs, READMEs, documentation pages |
| `mcp-smithery` | Context7 library docs, GitHub search, toolbox management |
| `mcp-filesystem` | File read/write operations (MCP-first) |
| `mcp-sequential-thinking` | Reason through research findings per project |
| `web-research-pipeline` | Full web search→extract→save pipeline for per-project research |
| `domain-intel` | Passive domain recon for project-related domain analysis |
| `firecrawl-scrape` | JS-rendered documentation extraction |
| `firecrawl-map` | Discover all URLs on project documentation sites |
| `context7` | Library/API docs and patterns (referenced for non-MCP contexts) |

## MCP Tool Precedence (New)

Before calling built-in tools, prefer MCP equivalents:

| Task | Built-in | MCP First | Fallback |
|------|----------|-----------|----------|
| Search repos/projects | `web_search` | `mcp_github_search_repositories` | `mcp_smithery_github_search_repositories` |
| Search code patterns | `search_files` | `mcp_github_search_code` | `mcp_smithery_github_search_code` |
| Search issues/PRs | `web_search` | `mcp_github_search_issues` | `mcp_smithery_github_search_issues` |
| Fetch documentation | `web_extract` | `mcp_fetch_get_markdown` | `firecrawl_scrape` |
| Library API docs | — | `mcp_smithery_context7_mcp_query_docs` | `context7` skill |
| File operations | `terminal`/`write_file` | `mcp_filesystem_read_text_file`, `mcp_filesystem_write_file` | built-in |
| Similar projects | `web_search` | `mcp_github_search_repositories(query="topic:<stack>")` | — |
| Reasoning through findings | — | `mcp_sequential_thinking_sequentialthinking` | — |

## When to Use

- Running research pipelines across multiple projects
- Refreshing stale RESEARCH_REPORT.md files with new findings
- Bootstrapping reports for projects that have none
- Auditing report completeness and cross-reference symmetry

## When NOT to Use

- Single-project research (use `web-research-pipeline` directly)
- When repo management (branch norm, Bun migration, CI) is the goal
- When reports are current and no web research is needed

## Critical Rules

1. **NO FABRICATION** — Every finding must trace to a real search result (mcp_github or web_search). Write "No new findings" rather than inventing content.
2. **VERIFY BEFORE CLAIMING** — Never report a count without running the terminal or MCP command. Never embed a URL without `mcp_fetch_get_markdown` or `web_extract` confirming it loads.
3. **SCOPE GUARD** — This skill covers research and reporting only. Do not start branch normalization, migration, or CI work.
4. **SIZE GATE** — Reports 1KB-5KB. Trim over 5KB. Expand under 1KB.
5. **SYMMETRIC CROSS-REFS** — If report A references project B, report B must reference project A.
6. **MCP-FIRST** — Use mcp-github → mcp-fetch → mcp-smithery before falling back to built-in tools.
7. **MULTI-BACKEND EXTRACTION** — If mcp-fetch fails (JS-rendered page), retry with firecrawl-scrape before giving up.

## Workflow

### Phase 1: Inventory

Establish ground truth before any research begins.

```bash
find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | sort
find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l
pwd
```

Or via MCP:
```
# Call: mcp_filesystem_search_files(...) for MCP-first equivalent
# Fallback: terminal as above
```

- Categorize each project: UPDATE (report exists) or CREATE (missing).
- Load docs/per-project-research-queries.md if it exists (reuse prior queries).

### Phase 2: Per-Project Discovery

For each project, read README.md + AGENTS.md to extract tech stack and generate 3-5 targeted search queries.

MCP-enhanced discovery:
```python
# Extract project info via MCP
# Call: mcp_filesystem_read_text_file(path="./projects/<name>/README.md", head: 50)
# Call: mcp_filesystem_read_text_file(path="./projects/<name>/AGENTS.md", head: 50)
# Or use terminal as fallback
```

**Query generation per project:**

| Query Type | MCP Tool | Purpose |
|------------|----------|---------|
| Similar open source projects | `mcp_github_search_repositories(query="topic:<framework> stars:>100")` | Find comparable projects |
| Best practices & patterns | `mcp_smithery_context7_mcp_query_docs(libraryId, query="best practices")` | Library-specific docs |
| Code patterns | `mcp_github_search_code(query="<framework> config language:<lang>")` | Real-world usage patterns |
| Issues & solutions | `mcp_github_search_issues(query="<framework> common error is:issue")` | Common pitfalls |
| Documentation | `mcp_fetch_get_markdown(url="https://<framework>.docs/guide")` | Official docs |
| Security advisories | `mcp_smithery_github_list_repository_security_advisories(...)` | Vulnerabilities |
| Tech stack domain recon | `domain_intel(domain="<project-domain>")` | Passive infrastructure intel |

Write docs/per-project-research-queries.md with the full query matrix.

### Phase 3: Parallel Web Research

Dispatch 3-4 projects concurrently via subagents.

Each subagent receives:
- Project name, tech stack, query list
- Target report path
- Reference to report template
- Access to: mcp-github, mcp-fetch, mcp-smithery, web-research-pipeline

```python
# Via delegate_task (batch mode)
from hermes_tools import delegate_task

tasks = [
    {
        "goal": "Research project <name>: run web-research-pipeline with MCP tools",
        "context": f"Project: {name}, Stack: {stack}, Queries: {queries}, Target: {target_path}",
        "toolsets": ["web", "terminal", "file", "skills"]
    }
    for name, stack, queries, target_path in projects_queries
]
delegate_task(tasks=tasks)
delegate_task(tasks=tasks)

> **Tip: Pre-read existing reports while subagents run.** See
> `references/concurrent-pre-read.md`. Reading all existing RESEARCH_REPORT.md
> files during subagent idle time reveals size violations, missing cross-refs,
> and stale content before Phase 2 starts — turning Phase 4 from discovery
> into re-check.

### Phase 4: Report Writing

For each project after research completes:

1. UPDATE path: read existing report, merge new MCP-backed findings, remove stale links.
   - Read target sections with full-context reads. If a structured block is truncated, increase `limit` or read the surrounding section before editing bounded markers like "Related Projects" or "Resources".
2. CREATE path: write fresh report from template.
3. Spot-check 2-3 key URLs with `mcp_fetch_get_markdown` or `web_extract` before embedding.
4. Enforce size gate: trim > 5KB, expand < 1KB.
5. Add a "Research Methodology" section noting which MCP backends were used.

**Report template enhancements (add at end):**

```markdown
### Research Methodology
- **Repository search:** mcp-github / mcp-smithery
- **Documentation:** mcp-fetch / firecrawl-scrape / web_extract
- **Code pattern analysis:** mcp-github search_code
- **Library docs:** Context7 via mcp-smithery
- **Domain intel:** domain-intel skill
- **Last verified:** <ISO timestamp>
```

Template location: Prompts/templates/RESEARCH_REPORT.template.md

### Phase 5: Index and Cross-Reference

```bash
find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' -exec ls -lh {} \;
```

- Rewrite projects/RESEARCH_INDEX.md — one row per project with file size, last-updated date, and MCP backends used.
- Verify each report's Related Projects section lists all workspace projects sharing its tech stack.
- Verify symmetry: if A references B, confirm B references A.

### Phase 6: Verification

```bash
find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l

for f in projects/*/RESEARCH_REPORT.md; do
  echo "=== $f ==="
  grep -c '^## ' "$f"
  wc -c "$f"
done
```

| Gate | Condition | Check Method |
|------|-----------|--------------|
| Count | equals target N | `find \| wc -l` or `mcp_filesystem_list_directory` |
| Sections | >= 9 per report | `grep -c '^## '` |
| Size min | >= 1KB per report | `wc -c` |
| Size max | <= 5KB per report | `wc -c` |
| URL checks | 2 per report via mcp-fetch → non-404 | `mcp_fetch_get_markdown` |
| Index current | RESEARCH_INDEX.md has N rows | `wc -l` or `mcp_filesystem_read_text_file` |
| Cross-refs | symmetric in both directions | grep in each file |
| Backend diversity | >= 2 MCP backends used per report | grep "mcp-" in methodology section |

## Reference Files

- `references/concurrent-pre-read.md` — Pattern for pre-reading existing reports during subagent idle time

## Pitfalls (MCP-Specific)

- **MCP server availability:** `mcp-github` requires `GITHUB_TOKEN`. `mcp-smithery` requires OAuth. Check with `get_toolbox_status` before dispatching subagents.
- **GitHub rate limits:** 5,000 req/hr across ALL MCP servers using the same token. Stagger parallel search calls in subagents.
- **Context7 requires library ID resolution:** Call `context7_mcp_resolve_library_id` first, then `context7_mcp_query_docs`. Don't skip the resolve step.
- **mcp-fetch + JS pages:** `mcp_fetch_get_markdown` returns server-side HTML only. Use `firecrawl_scrape` for SPA documentation.
- **Subagent MCP access:** Subagents inherit parent's MCP server access. If they can't find tools, check `tool_search` in the subagent context.
- **Multi-backend exhaust:** Try mcp-github → mcp-smithery → web_search → firecrawl. Don't give up after one backend fails.
- **Fabricated counts** — Always run `find | wc -l` to confirm. Never trust an agent self-report without verification.
- **Stale URLs** — Always `mcp_fetch_get_markdown` or `web_extract` before embedding a URL.
- **Scope creep** — Branch normalization, Bun migration, and CI setup belong elsewhere. Do not start them during research phases.
- **Asymmetric cross-refs** — Check both directions. If A references B, B must reference A.
- **Report bloat** — Keep under 5KB. Cut anything not immediately actionable.

## Verification Checklist

- [ ] All N reports exist on disk (`find | wc -l = N` or `mcp_filesystem_search_files`)
- [ ] Every report has >= 9 sections (`grep -c '^## '`)
- [ ] All reports 1KB-5KB (`wc -c`)
- [ ] 2 URL spot-checks per report pass via `mcp_fetch_get_markdown`
- [ ] RESEARCH_INDEX.md has N rows with size, date, and MCP backends used
- [ ] Every Related Projects cross-reference is symmetric
- [ ] No fabricated findings — every fact traces to mcp-github, mcp-fetch, or web_search
- [ ] >= 2 distinct MCP backends used per report (methodology section)
- [ ] Scope respected — no branch or migration work started
- [ ] `mcp_smithery_get_toolbox_status` confirmed all servers healthy before starting

### Final verification commands

```bash
find projects -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l

find projects -maxdepth 2 -name 'RESEARCH_REPORT.md' | sort | while read -r f; do
  echo === "$f" ===
  grep -c '^## ' "$f"
  wc -c < "$f"
done
```
