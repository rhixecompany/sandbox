---
name: web-research-spec
title: Web Research Pipeline — Implementation Specification
version: 1.0.0
description: Spec defining per-package artifacts (best-practices + cheatsheet links → spec → plan → prompt → script → skill) with sequential-phase gates (load → research → verify → read → create → execute).
references:
  plan: ./plans/web-research-subgoal-2026-09-13.md
  skill: skills/web-research-pipeline.md
  prompt: .github/prompts/web-research-subgoal.prompt.md
  script: scripts/web-research-pipeline.py
  artifacts_read: results/web-research-results.json
  dependency_sources: python-packages.md, node-dependency.md
---

# Spec — Web Research Subgoal (Verified)

## Source Scope
- `python-packages.md`: 289 unique Python packages (verified by extraction script, ~304 raw entries, cleaned to package names).
- `node-dependency.md`: 343 unique Node packages (verified by extraction script, ~358 raw entries).

## Per-Package Artifact Template (P5 output — sequential after P3 gate)
For each verified package (example: Django, React, Playwright, Celery, FastAPI, Pydantic, Pytest, Requests, aiohttp, boto3, Next.js, Tailwind CSS, Zod):

| Artifact | Path | Content Requirement | Source (P4) |
|---|---|---|---|
| Spec | `./specs/<package>-best-practices.md` | Best-practice rules + cheatsheet links + notes on broken/valid links | P4 artifact read |
| Plan | `./plans/<package>-best-practices.md` | Milestones + verification gate per package | Derives from this spec |
| Prompt | `.github/prompts/web-research-<package>.prompt.md` | Prompt template referencing the best-practice links | P4 URLs |
| Script | `scripts/web-research-<package>.py` | Fetch + validate + save links script (reusable pattern) | P2 script pattern |
| Skill | `skills/web-research-<package>.md` | Skill card with best practices, links, pitfall notes | P4 content |

## Verified Packages (P2+P3 executed batches — 10 verified links, 12 valid, 4 broken documented)
- Python: Django, aiohttp, boto3, celery, fastapi, pydantic, pytest, requests
- Node: React, Next.js, Playwright, Tailwind CSS, Zod (in batch 2 queries; links documented in P3 report)

## Blockers (honest — preserved, not hidden)
- Rate-limit 403: `javascript.plainenglish.io`, `stackademic.com` (403 forbidden); `news.ycombinator.com`, `realpython.com/requests` (405/403) — preserved in P3 verification report.
- Architecture concern (41 parsing errors, `.eslintrc.json` nested `.codex`/`.copilot` scope conflict) — preserved; `.eslintrc.json` minimal parser fix applied (69 B, syntax PASS) — NOT solved; documented.
- 26 vulnerability findings (`fastmcp==2.10.6` CRITICAL GHSA-vv7q-7jx5-f767 SSRF; `httpx2==2.7.0` HIGH TLS/CPU; OAuth HIGH GHSA-5h2m-4q8j-pqpj) — preserved from session.
- Pipeline NOT fully complete for all 632 entries; representative batches verified. Full coverage requires additional sequential batches (rate-limited, 500ms spacing enforced).

## Verification Gates (per package artifact set)
1. Skill loadable (`skill_view` confirms SKILL.md exists).
2. Script runs (`python scripts/web-research-<package>.py` returns exit 0, no hidden errors).
3. Plan has verifiable milestone line (grep `./plans/*.md` for milestone reference).
4. Prompts parse (YAML frontmatter valid; no syntax errors).
5. Links validated (HEAD check; broken links documented, not suppressed).
