---
author: Alexa
description: ''
license: MIT
metadata:
  hermes:
    tags:
    - imported
name: repo-research-pipeline
tags:
- imported
title: Repo Research Pipeline
version: 1.0.0

---
# Repo Research Pipeline

## Description

Structured workflow for executing web research across multiple projects and
writing actionable RESEARCH_REPORT.md files per project. Handles query
generation from local project context, parallel web research via subagents,
report writing to a fixed template, index maintenance, and verification.

Use this skill whenever a prompt drives research across N projects and needs
consistent, web-backed output reports.


## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## When to Use

- Running /repo or any research pipeline prompt across multiple projects
- Refreshing stale RESEARCH_REPORT.md files with new findings
- Bootstrapping reports for projects that have none
- Auditing report completeness and cross-reference symmetry

## When NOT to Use

- Single-project research (use content-research-writer directly)
- When repo management (branch norm, Bun migration, CI) is the goal
- When reports are current and no web research is needed

## Goal

Produce accurate, web-backed RESEARCH_REPORT.md files for all target
projects. Every claim traces to a real web_search result. Reports are
1KB-5KB, follow the standard template, and have symmetric cross-references.

## Critical Rules

1. NO FABRICATION — Every finding must trace to a real web_search result.
   Write "No new findings" rather than inventing content.
2. VERIFY BEFORE CLAIMING — Never report a count without running the
   terminal command. Never embed a URL without web_extract confirming it loads.
3. SCOPE GUARD — This skill covers research and reporting only. Do not start
   branch normalization, migration, or CI work.
4. SIZE GATE — Reports 1KB-5KB. Trim over 5KB. Expand under 1KB.
5. SYMMETRIC CROSS-REFS — If report A references project B, report B must
   reference project A.

## Workflow

### Phase 1: Inventory

Establish ground truth before any research begins.

```bash
find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | sort
find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' | wc -l
pwd
```

- Categorize each project: UPDATE (report exists) or CREATE (missing).
- Load docs/per-project-research-queries.md if it exists (reuse prior queries).

### Phase 2: Per-Project Discovery

For each project, read README.md (or package.json) and AGENTS.md to extract
the tech stack and generate 3-5 targeted search queries:

- "<framework> best practices 2026"
- "<framework> similar open source projects github"
- "<framework> performance optimization cheatsheet"
- "<framework> common pitfalls security hardening"
- "<project-type> architecture guide patterns 2026"

Write docs/per-project-research-queries.md with the full query matrix.

### Phase 3: Parallel Web Research

Dispatch 3-4 projects concurrently via dispatching-parallel-agents.
Each subagent receives: project name, tech stack, query list, target report
path, and reference to Prompts/templates/RESEARCH_REPORT.template.md.

Use context7 for library-specific API docs.
Use web_search for guides, similar projects, cheatsheets.
Do not substitute one for the other.

### Phase 4: Report Writing

For each project after research completes:

1. UPDATE path: read existing report, merge new findings, remove stale links.
2. CREATE path: write fresh report from template.
3. Spot-check 2-3 key URLs with web_extract before embedding.
4. Enforce size gate: trim > 5KB, expand < 1KB.

Template location: Prompts/templates/RESEARCH_REPORT.template.md

### Phase 5: Index and Cross-Reference

```bash
find projects/ -maxdepth 2 -name 'RESEARCH_REPORT.md' -exec ls -lh {} \;
```

- Rewrite projects/RESEARCH_INDEX.md — one row per project with file size
  and last-updated date.
- Verify each report's Related Projects section lists all workspace projects
  sharing its tech stack.
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

| Gate | Condition |
|------|-----------|
| Count | equals target N |
| Sections | >= 9 per report |
| Size min | >= 1KB per report |
| Size max | <= 5KB per report |
| URL checks | 2 per report via web_extract — non-404 |
| Index current | RESEARCH_INDEX.md has N rows with size and date |
| Cross-refs | symmetric in both directions |

## Pitfalls

- **Fabricated counts** — A prior run reported 13 reports written but only 1
  survived on disk. Always run find | wc -l to confirm. Never trust an agent
  self-report without terminal verification.
- **Stale URLs** — Web docs move. Always web_extract before embedding a URL.
- **Scope creep** — Branch normalization, Bun migration, and CI setup belong
  in repo-management.prompts.md. Do not start them during research phases.
- **context7 vs web_search swap** — context7 for library API docs; web_search
  for broader guides, similar projects, cheatsheets. Swapping returns outdated
  Stack Overflow noise instead of authoritative docs.
- **Asymmetric cross-refs** — If Banking references xamehi but xamehi does
  not reference Banking, the cross-reference graph is broken. Check both directions.
- **Report bloat** — Keep under 5KB. Cut anything not immediately actionable
  for this specific project's stack.

## Report Template Sections (Required Order)

1. Project header — type, tech stack, status
2. Similar Projects — table
3. Key Findings — subsections per technology
4. Cheatsheets and Quick Reference — table
5. Best Practices — numbered list of 5
6. Common Pitfalls — table
7. Performance — top 3-5 optimizations
8. Security — top 3-5 considerations
9. Related Projects (in workspace) — cross-refs
10. Resources — table

Full template: Prompts/templates/RESEARCH_REPORT.template.md

## Tools

| Tool | Phase | Purpose |
|------|-------|---------|
| web_search | 3 | Guides, similar projects, cheatsheets |
| web_extract | 3, 4 | Extract content; verify URLs |
| read_file | 1, 2, 4 | Read project files and existing reports |
| write_file | 4, 5 | Write/update reports and index |
| terminal | 1, 6 | Count reports, check sizes, verify sections |
| search_files | 4 | Verify section headers in reports |
| delegate_task | 3 | Parallel per-project research subagents |

## Related Skills

- dispatching-parallel-agents — Spawn parallel subagents for concurrent research
- content-research-writer — Research synthesis per project
- writing-skills — Crisp, compact markdown writing
- systematic-debugging — Find missing or stale reports
- simplify — Strip bloat from over-verbose reports
- context7 — Library API docs and patterns
- acpx-executor — Delegate research to ACPX agents

## Verification Checklist

- [ ] All N reports exist on disk (find | wc -l = N)
- [ ] Every report has >= 9 sections
- [ ] All reports 1KB-5KB
- [ ] 2 URL spot-checks per report pass via web_extract
- [ ] RESEARCH_INDEX.md has N rows with size and date
- [ ] Every Related Projects cross-reference is symmetric
- [ ] No fabricated findings — every fact traces to web_search
- [ ] Scope respected — no branch or migration work started
