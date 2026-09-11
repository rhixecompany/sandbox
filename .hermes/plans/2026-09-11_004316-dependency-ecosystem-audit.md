---
goal: Monorepo Dependency Ecosystem Audit — tech-stacks, node-dependency.md, python-packages.md, per-package research cheat-sheets, audit skills/scripts/hooks, requirements.txt reconciliation
version: 1.0.0
date_created: 2026-09-11
last_updated: 2026-09-11
owner: Alexa (Hermes Agent)
status: In progress
tags: [audit, dependencies, research, node, python, skills, scripts, hooks, requirements]
---

# Introduction

![Status: In progress](https://img.shields.io/badge/status-In%20progress-yellow)

Audit every repository in the SandBox monorepo (root + `packages/` + all 23 `projects/`) and produce: (1) consolidated technology-stack report, (2) `node-dependency.md` for all npm/npx/bun/bunx direct deps + devDeps, (3) `python-packages.md` for every direct Python package, (4) web-researched cheat-sheets for each direct package under `research/packages/`, (5) consolidated per-ecosystem audit skills/scripts/hooks, (6) reconciled `requirements.txt` (direct/dev/transitive, verified against live env). Executed in the fastest parallel order via subagents.

## 1. Requirements & Constraints

- **REQ-001**: Inventory every repo: root `SandBox`, `packages/openrouter-client`, `packages/openrouter-client-py`, all 23 `projects/*` — 26 repos total.
- **REQ-002**: `node-dependency.md` at SandBox root covering ALL npm/npx/bun/bunx dependencies + devDependencies, direct-only (no transitive from `bun.lock`).
- **REQ-003**: `python-packages.md` at SandBox root covering every direct Python package from `requirements.txt`/`pyproject.toml` across all repos (root requirements.txt = 210 pinned).
- **REQ-004**: Web research (web-research-pipeline) produces one cheat-sheet per direct package (~245 docs) into `research/packages/node/` and `research/packages/python/`.
- **REQ-005**: Consolidated per-ecosystem skills + scripts + hooks: `node-dep-audit`, `python-dep-audit`, `research-doc-verify` (DRY; no per-package duplication).
- **REQ-006**: Reconcile `requirements.txt` against live env (`~/myvenv`), organized direct/dev/transitive, every package from `python-packages.md` present.
- **REQ-007**: Deliverables chain: create implementation spec + plan + prompt, then execute, verify, and commit.
- **SEC-001**: No secrets: never read/print `.env`, credentials, or API keys; reports contain package metadata only.
- **SEC-002**: No destructive ops without git-visible traceability; user pre-approved all destructive operations for this goal.
- **CON-001**: Direct dependencies only — no transitive expansion (per user decision).
- **CON-002**: Windows/MSYS2/git-bash; POSIX syntax in terminal; native tools need `C:/` paths.
- **CON-003**: Research docs must be saved as markdown, one file per package, slug ≤ 80 chars.
- **CON-004**: `requirements.txt` currently pip-freeze style; final format organized into sections.
- **GUD-001**: MCP-first tool precedence (filesystem, ast-grep, memory, fetch).
- **GUD-002**: Subagent-driven development with 2-stage review for research batches.
- **GUD-003**: Auto-advance between phases — no checkpoint pauses unless a phase fails critically.
- **PAT-001**: Per-repo manifest parsing → dedupe → master index pattern (machine-parseable tables).
- **PAT-002**: Research doc template from `web-research-pipeline` (title, metadata, content, footer).

## 2. Implementation Steps

### Implementation Phase 1 — Inventory & Technology Stacks

- GOAL-001: Enumerate all 26 repos, parse every manifest, produce consolidated `technology-stacks.md`.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-001 | Enumerate repos + manifests (package.json, pyproject.toml, requirements*.txt, uv.lock) | | |
| TASK-002 | Parse all package.json (18 node repos) for name/version/deps/devDeps | | |
| TASK-003 | Parse all Python manifests (10 locations) for direct packages | | |
| TASK-004 | Write `technology-stacks.md` (per-repo stack summary) at root | | |

### Implementation Phase 2 — node-dependency.md

- GOAL-002: Produce `node-dependency.md` at root with per-repo + consolidated direct dependency index.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-005 | Build master Node direct-dep index (name, version spec, repo(s), dep/devDep, purpose) | | |
| TASK-006 | Write `node-dependency.md` (per-repo tables + unique package index + npm/npx/bun/bunx usage notes) | | |

### Implementation Phase 3 — python-packages.md

- GOAL-003: Produce `python-packages.md` at root with every direct Python package.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-007 | Build master Python direct-package index from all manifests (dedupe by lowercase name) | | |
| TASK-008 | Write `python-packages.md` (per-repo tables + unique package index + install/usage notes) | | |

### Implementation Phase 4 — Web Research Cheat-Sheets (~245 docs)

- GOAL-004: One cheat-sheet per direct package via parallel research subagents.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-009 | Prepare package lists split across 6 parallel subagents (node ~34, python 210 in 5 batches of ~42) | | |
| TASK-010 | Subagent batch A: node cheat-sheets → `research/packages/node/` | | |
| TASK-011 | Subagent batches B–F: python cheat-sheets → `research/packages/python/` | | |
| TASK-012 | Verify doc count == package count; re-dispatch missing docs | | |

### Implementation Phase 5 — Audit Skills, Scripts, Hooks

- GOAL-005: Consolidated DRY skills/scripts/hooks per ecosystem.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-013 | Create skill `node-dep-audit` (validate node-dependency.md vs live manifests) | | |
| TASK-014 | Create skill `python-dep-audit` (validate python-packages.md + requirements.txt sync) | | |
| TASK-015 | Create skill `research-doc-verify` (validate research/packages docs exist + meet template) | | |
| TASK-016 | Write `scripts/node-dep-audit.py`, `scripts/python-dep-audit.py`, `scripts/research-doc-verify.py` | | |
| TASK-017 | Write hook scripts in `hooks/` wiring the three audits (post-write verification) | | |

### Implementation Phase 6 — requirements.txt Reconciliation

- GOAL-006: Reconcile `requirements.txt` with live env, organized and verified.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-018 | Capture live env packages (`~/myvenv` pip freeze + uv) | | |
| TASK-019 | Classify: direct (from manifests) / dev (test tooling) / transitive | | |
| TASK-020 | Rewrite `requirements.txt` sections; verify every python-packages.md entry present | | |

### Implementation Phase 7 — Verification & Commit

- GOAL-007: All gates pass; commit with traceability.

| Task | Description | Completed | Date |
|------|-------------|-----------|------|
| TASK-021 | Run `node-dep-audit.py`, `python-dep-audit.py`, `research-doc-verify.py` — 0 failures | | |
| TASK-022 | Run `bun run check` + `pytest` — no new regressions | | |
| TASK-023 | Update plan status → Completed; git commit all artifacts | | |

## 3. Alternatives

- **ALT-001**: Full transitive tree from `bun.lock` (≈400+ packages) — rejected: user chose direct-only; transitive adds noise without actionable value.
- **ALT-002**: Per-package skills/scripts/hooks (~245 sets) — rejected: violates DRY; consolidated per-ecosystem chosen.
- **ALT-003**: Research only runtime deps (~40 docs) — rejected: user chose full direct coverage (~245 docs).
- **ALT-004**: Keep requirements.txt freeze as-is — rejected: user chose live-env reconciliation with organized sections.

## 4. Dependencies

- **DEP-001**: `web-research-pipeline` skill + firecrawl/tavily/fetch MCP fallback chain.
- **DEP-002**: `~/myvenv` (Python 3.13, mcp 2.0.0, ruff, pyright) for Python audit scripts.
- **DEP-003**: bun/npm/node on PATH for Node manifest parsing (`C:/Users/Alexa/.bun/bin/bun`, `C:/nvm4w/nodejs/`).
- **DEP-004**: Existing reports referenced: root `requirements.txt` (210 pkgs), root `package.json` (31 direct), `packages/*` manifests, `projects/*` manifests.

## 5. Files

- **FILE-001**: `node-dependency.md` (new, root)
- **FILE-002**: `python-packages.md` (new, root)
- **FILE-003**: `technology-stacks.md` (new, root)
- **FILE-004**: `research/packages/node/*.md` (new, ~34 docs)
- **FILE-005**: `research/packages/python/*.md` (new, ~210 docs)
- **FILE-006**: `scripts/node-dep-audit.py` (new)
- **FILE-007**: `scripts/python-dep-audit.py` (new)
- **FILE-008**: `scripts/research-doc-verify.py` (new)
- **FILE-009**: `hooks/node-dep-audit.sh`, `hooks/python-dep-audit.sh`, `hooks/research-doc-verify.sh` (new)
- **FILE-010**: `requirements.txt` (modified — organized sections)
- **FILE-011**: `.hermes/specs/dependency-ecosystem-audit-spec.md` (new)
- **FILE-012**: `.github/prompts/development/dependency-ecosystem-audit.prompt.md` (new)
- **FILE-013**: Skills: `node-dep-audit`, `python-dep-audit`, `research-doc-verify` (new)

## 6. Testing

- **TEST-001**: `node-dep-audit.py` — every manifest dep appears in node-dependency.md; exit 0.
- **TEST-002**: `python-dep-audit.py` — every python-packages.md entry appears in requirements.txt; exit 0.
- **TEST-003**: `research-doc-verify.py` — every direct package has a doc with required sections; exit 0.
- **TEST-004**: `bun run check` passes (lint/format/markdownlint/spellcheck).
- **TEST-005**: `pytest` passes with no regressions.

## 7. Risks & Assumptions

- **RISK-001**: Web research rate limits / flaky backends → fallback chain fetch→tavily→web_search; retry failed URLs; subagents batch with sleeps.
- **RISK-002**: 210 docs at ~500 words each is heavy for one session → 6 parallel subagents, per-batch workspace files, count verification.
- **RISK-003**: Live env drift (myvenv may lack some pinned packages) → report as MISSING vs installed, keep pin from python-packages.md.
- **ASSUMPTION-001**: "Direct" = entries in manifest files, not resolved lockfile graph.
- **ASSUMPTION-002**: Filename `node-dependency.md` (corrected spelling of user's `node-dependecy.md`).
- **ASSUMPTION-003**: Research docs template: title, metadata (source/timestamp/backend), cheat-sheet sections (install, core API, examples, links).

## 8. Related Specifications / Further Reading

- [Spec: dependency-ecosystem-audit-spec.md](../specs/dependency-ecosystem-audit-spec.md)
- [web-research-pipeline skill](../../research/web-research-pipeline/SKILL.md)
- [executing-plans skill](../../software-development/executing-plans/SKILL.md)
- [subagent-driven-development skill](../../software-development/subagent-driven-development/SKILL.md)