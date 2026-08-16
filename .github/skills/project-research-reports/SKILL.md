---
name: project-research-reports
title: "Project Research Reports"
description: "Maintain RESEARCH_REPORT.md files — 10 sections, size-gated."
version: 1.0.0
author: "Hermes Agent"
license: MIT
tags: [research, reports, documentation, project-docs]
---

# Project Research Reports

Create and maintain structured `RESEARCH_REPORT.md` files for workspace projects, conducting web research, updating against a hard template contract, and verifying all gates.

## When to Use

- Updating one or more project `RESEARCH_REPORT.md` files with the latest technology findings
- Creating a new research report from scratch for a workspace project
- Batch-maintaining multiple project reports to ensure consistency

## When NOT to Use

- Creating a full documentation kit (use `research-actionable-kit`)
- Pure research synthesis without a report deliverable
- Inline doc changes without structured sections

## Workflow

### Phase 1: Discover & Read

1. List projects under `projects/` — identify which carry a `RESEARCH_REPORT.md`
2. Read each existing report and the project's `README.md` to understand the stack
3. Note the current section structure, size, and last-verified date

### Phase 2: Batch Research

Run **8–10 parallel Tavily MCP searches** covering every unique tech-stack component across all projects:

- One search per major framework/library (Next.js, Drizzle, Prisma, Stripe, Auth.js, Neon, Plaid, Celery, etc.)
- Use `search_depth='advanced'` + `time_range='year'`
- Each returns 5 results with snippets — enough for 3–5 bullets per component

Topic-specific query patterns (customize per project):
```
"Next.js 16 best practices 2026 production deployment Turbopack"
"Drizzle ORM 2026 best practices production tips serverless edge"
"NextAuth v5 Auth.js 2026 production patterns Drizzle adapter"
"Stripe subscriptions Next.js 2026 App Router webhooks best practices"
"Prisma 6 ORM 2026 performance connection pooling best practices"
"Neon serverless PostgreSQL 2026 Drizzle ORM connection pooling"
"Next.js 15 16 security best practices 2026 CSP rate limiting"
"Plaid Dwolla fintech integration 2026 best practices webhooks"
```

### Phase 3: Write Reports

For each project, structure the report with exactly these 10 `##` sections:

1. **Project** — One-liner type, full tech stack, status
2. **Similar Projects** — Table mapping peer projects with relevance notes
3. **Key Findings** — 2-4 subsections each with 3-5 bullet findings from research
4. **Cheatsheets & Quick Reference** — Table of resources per topic
5. **Best Practices** — Numbered list of production best practices
6. **Common Pitfalls** — Table: Pitfall | Impact | Avoidance
7. **Performance** — Numbered optimization tips
8. **Security** — Numbered security measures
9. **Related Projects (in workspace)** — Bullet list with nature of shared patterns
10. **Resources** — Table: external URLs for each technology

End with a `### Research Methodology` note: source type + last-verified date.

### Phase 4: Verify Gates

#### Section-count gate
```bash
grep -c '^## ' "$f/RESEARCH_REPORT.md"
```
Must equal exactly **10**. If less, add the missing canonical section.

#### Size gate
```bash
wc -c "$f/RESEARCH_REPORT.md"
```
Must be **1024–5120 bytes**. If over, trim:
1. Normalize CRLF→LF: `sed -i 's/\r$//' "$f"` (CRLF inflates `wc -c` by ~1 byte/line)
2. Remove redundant `### Research Methodology` block
3. Cut Resource tables to 4–6 rows
4. Shorten Technology Stack line (e.g. `TypeScript` → `TS`)
5. Merge Security/Practices items into fewer lines
6. Tighten Key Findings bullets (drop parentheticals)

#### Cross-reference symmetry gate
Every pair of projects must have **bidirectional references** in the Related Projects section. If project A mentions project B, project B must also mention project A. Non-overlapping stacks (e.g. pure Django vs pure Next.js) may legitimately omit each other.

#### Full verification command
```bash
for f in project1 project2 project3; do
  bytes=$(wc -c < "$f/RESEARCH_REPORT.md")
  secs=$(grep -c '^## ' "$f/RESEARCH_REPORT.md")
  printf "%-30s %5s bytes | %d sections\n" "$f" "$bytes" "$secs"
done
```

## Support Files

- `references/2026-framework-facts.md` — Condensed bank of verified 2026 framework facts (Next.js 16, Drizzle ORM, Auth.js, Stripe, Prisma, Neon, Plaid, Celery). Reuse across reports instead of re-searching every component.

## Pitfalls

| Pitfall | Prevention |
|---------|------------|
| **CRLF inflates byte count** | `sed -i 's/\r$//' file.md` before final measurement; `wc -c` counts CRLF as 2 bytes/line |
| **Sibling-writer overwrite** | When subagents split work, verify final on-disk content after writing; prefer single-writer |
| **Fabricating findings** | Only cite sources actually retrieved; never invent data |
| **Missing section count** | Always run `grep -c '^## '` before declaring done |
| **Asymmetric references** | Check every pair of related projects in both directions |
| **Stale facts** | Always search for the current year (2026+); framework patterns change quarterly |

## Verification Checklist

- [ ] All projects have exactly 10 `##` sections
- [ ] All reports are 1024–5120 bytes on disk (LF-normalized)
- [ ] Every Related Projects reference is bidirectional
- [ ] Last-verified date is current
- [ ] No fabricated findings — only content retrieved from actual searches
- [ ] CRLF normalized before final measurement

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
