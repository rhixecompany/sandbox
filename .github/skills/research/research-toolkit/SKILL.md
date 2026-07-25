---
name: research-toolkit
title: Research Toolkit (find, monitor, write)
description: Scholarly research workflow — search/fetch arXiv papers, monitor blogs & RSS via blogwatcher, and write ML conference papers (NeurIPS/ICML/ICLR).
license: MIT
author: Hermes Agent
version: 1.0.0
tags: [research, arxiv, blogwatcher, rss, literature-review, paper-writing]
metadata:
  hermes:
    tags: [research, arxiv, blogwatcher, paper-writing]
---
# Research Toolkit

Class-level umbrella for the research workflow: **find** papers, **monitor** sources, and **write**
papers. Subsections map to the three stages; detailed command references live under `references/`.

- **Find papers** → arXiv search/fetch + Semantic Scholar citations. See `references/arxiv.md`.
- **Monitor sources** → Blogwatcher (RSS/Atom feeds, Docker, scanning). See `references/blogwatcher.md`.
- **Write papers** → Full NeurIPS/ICML/ICLR pipeline (literature review → experiments → writing). See `references/research-paper-writing.md`.

## When to Use

- "Search arXiv for papers on X" / "get the BibTeX / citations for this paper"
- "Monitor these blogs/RSS feeds and alert me on new posts"
- "Help me write a conference paper" / "structure the experiments and related work"

## 1. arXiv — quick orientation

```bash
# Latest 10 papers in cs.AI
curl -s "http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=10&sortBy=submittedDate"

# By ID
curl -s "http://export.arxiv.org/api/query?id_list=2401.00001"

# BibTeX
curl -s "http://export.arxiv.org/api/query?id_list=2401.00001" | python -c "import sys,xmltodict,json; ..."
```

Boolean query syntax, sort/pagination, full-paper fetch (PDF→markdown), BibTeX generation, and
Semantic Scholar citation lookups are in `references/arxiv.md`.

## 2. Blogwatcher — quick orientation

```bash
# Docker with persistent storage
docker run -d -v blogwatcher-data:/data -p 8080:8080 blogwatcher/blogwatcher
# Add a blog, then scan
blogwatcher add <url>
blogwatcher scan
```

Installation (Docker/named volume/bind mount), managing blogs, scanning/reading, env vars, and
example output are in `references/blogwatcher.md`.

## 3. Research Paper Writing — quick orientation

Phased pipeline: Phase 0 project setup → Phase 1 literature review (seed papers, related work,
verify every citation) → Phase 2 experiment design → Phase 3 execution & monitoring → Phase 4
result analysis → writing. The full 2000+ line playbook (with TODO patterns, cost tracker, multi-author
coordination, cron monitoring) is in `references/research-paper-writing.md`.

## Related Skills

- `research-toolkit` subsumes the former `arxiv`, `blogwatcher`, and `research-paper-writing` skills.
- For web research beyond arXiv, see `web-research-pipeline`, `repo-research-pipeline`, `domain-intel`.
- For turning a codebase into docs, see `code-wiki`, `documentation-extraction-and-indexing`.

## Reference Library

| File | Contents |
|------|----------|
| `references/arxiv.md` | Search syntax, fetch by ID, BibTeX, full-paper extract, Semantic Scholar citations |
| `references/blogwatcher.md` | Docker install, blog management, scanning, env vars, output |
| `references/research-paper-writing.md` | Full paper-writing pipeline: setup, lit review, experiments, writing |

## Skills Required

| Skill | Purpose |
|-------|---------|
| `hermes-agent` | Core Hermes functionality |
| `skill-judge` | Evaluate skill quality |

## Pitfalls

- **Thin content**: Add concrete code examples and real-world use cases where applicable.
- **Missing error handling**: Include error-handling patterns in workflow phases.
- **No resumability**: Add entry/exit checks at each phase for long-running workflows.

## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has >=3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md under 250 lines
- [ ] No placeholder text
