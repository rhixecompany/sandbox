---
name: dependency-ecosystem-audit
description: Execute the SandBox monorepo dependency ecosystem audit — technology stacks, node-dependency.md, python-packages.md, per-package research cheat-sheets, audit skills/scripts/hooks, requirements.txt reconciliation. Use when the user asks to inventory/audit dependencies, generate dependency reports, research every package, or reconcile requirements.txt.
author: Hermes Agent
version: 1.0.0
tags: [development, research, audit, dependencies]
---

# Dependency Ecosystem Audit Prompt

## Role

You are executing a pre-approved, fully specified audit of the SandBox monorepo
at `C:/Users/Alexa/Desktop/SandBox`. Follow the plan and spec exactly. Auto-advance
between phases; only pause on critical failure. All destructive operations are
pre-approved; keep git traceability.

## Inputs (read first)

- Plan: `.hermes/plans/2026-09-11_004316-dependency-ecosystem-audit.md`
- Spec: `.hermes/specs/dependency-ecosystem-audit-spec.md`
- Skills: `executing-plans`, `subagent-driven-development`, `web-research-pipeline`, `node-dep-audit`, `python-dep-audit`, `research-doc-verify`

## Repos in scope (26)

1. Root `SandBox` (package.json: 1 dep + 30 devDeps; pyproject.toml (no deps); requirements.txt: 210 pinned; bun.lock; uv.lock)
2. `packages/openrouter-client` (TS client: @openrouter/sdk + @types/bun + typescript)
3. `packages/openrouter-client-py` (pyproject: openrouter + pytest extra)
4–26. `projects/*` (23 repos): Banking, Bash, comicwise, cookiecutter-django-tailwind, Django-Scrapy-Selenium, ecom, mcp-server-typescript, profile, Python-projects, Resume_maker, rhixe_scans, selenium_webdriver, university-libary-jsm, xamehi, xamehi.tv, youtube-downloader, + others present on disk. Enumerate live with `find projects -maxdepth 2 -name package.json -o -name pyproject.toml -o -name requirements.txt`.

## Workflow

### Phase 1–3 — Inventory & reports (controller, verified data)

1. Enumerate manifests: `find . -maxdepth 3 -name package.json -not -path '*/node_modules/*' -not -path '*/.git/*'`; same for `pyproject.toml`, `requirements*.txt`, `uv.lock` (exclude venvs).
2. Parse every package.json (dependencies + devDependencies), every pyproject.toml `[project.dependencies]` + `[project.optional-dependencies]`, every requirements*.txt.
3. Write `technology-stacks.md` (26 repo sections), `node-dependency.md` (per-repo + unique index), `python-packages.md` (per-repo + unique index; must include all 210 root entries).
4. Use `execute_code` for parsing/dedup so counts are verified; write files with `write_file`.

### Phase 4 — Research cheat-sheets (~245 docs)

1. Generate package lists: node list (~34), python list (~210) from the indexes.
2. Dispatch 6 parallel subagents (2 node batches or 1 node + 5 python batches of ≤50 each). Each subagent:
   - Uses web-research-pipeline pattern: web_search / tavily / fetch → extract → write markdown cheat-sheet.
   - Writes to `research/packages/node/<slug>.md` or `research/packages/python/<slug>.md`.
   - Template: `# <Package> Cheat-Sheet`, metadata block (source/timestamp/backend), `## Overview`, `## Install`, `## Core API / Usage`, `## Links` (≥2 authoritative).
   - Batches ≥10 packages with progress JSON in `results/research-batch-<id>.json`.
3. After all subagents: `python scripts/research-doc-verify.py` → re-dispatch for missing/stub docs.

### Phase 5 — Skills/scripts/hooks (DRY, consolidated)

1. `skill_manage` create: `node-dep-audit`, `python-dep-audit`, `research-doc-verify` (frontmatter + body ≥10 lines, trigger descriptions).
2. Write `scripts/node-dep-audit.py`, `scripts/python-dep-audit.py`, `scripts/research-doc-verify.py` (stdlib only; exit 0/1; human-readable report output).
3. Write `hooks/node-dep-audit.sh`, `hooks/python-dep-audit.sh`, `hooks/research-doc-verify.sh` — same checks, non-destructive, summary output.

### Phase 6 — requirements.txt reconciliation

1. `~/myvenv/Scripts/python.exe -m pip freeze` + compare with `uv.lock`/manifests.
2. Classify entries: Direct (in python-packages.md manifests), Dev (pytest/ruff/type tooling), Transitive.
3. Rewrite `requirements.txt`: `# Direct` / `# Dev` / `# Transitive` sections, keep `==` pins, ensure every python-packages.md entry present.
4. Report MISSING (in file not installed) and EXTRA (installed not in file) explicitly.

### Phase 7 — Verification & commit

1. Run the three audit scripts — all exit 0.
2. `bun run check`, `pytest -q` — pass, no regressions.
3. Update plan status → Completed; `git add -A && git commit -m "feat: dependency ecosystem audit (reports, research, tooling)"`.

## Output conventions

- Concise bullets/tables; lead with results; no fluff.
- Report doc counts and verification outputs as evidence.
- Flag blockers honestly with exact commands/paths.