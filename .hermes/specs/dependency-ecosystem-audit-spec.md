---
name: dependency-ecosystem-audit
title: Dependency Ecosystem Audit Spec
description: Spec for the SandBox monorepo dependency audit — tech-stacks, node/python dependency reports, per-package research, audit tooling, requirements.txt reconciliation.
author: Hermes Agent
version: 1.0.0
date: 2026-09-11
status: approved
tags: [audit, dependencies, research, node, python, requirements]
---

# Dependency Ecosystem Audit — Specification

## 1. Purpose

Audit all 26 repos in the SandBox monorepo (root, `packages/` ×2, `projects/` ×23) and produce machine-verifiable dependency documentation, per-package research cheat-sheets, audit tooling (skills/scripts/hooks), and a reconciled `requirements.txt`.

## 2. Scope

| Item | In scope | Out of scope |
|------|----------|--------------|
| Repos | root, packages/*, projects/* (26) | node_modules, .git, venvs, backups |
| Node deps | direct deps + devDeps from package.json (npm/npx/bun/bunx tooling) | transitive from bun.lock |
| Python deps | direct packages from requirements*.txt + pyproject.toml | transitive resolution graph |
| Research | 1 cheat-sheet per direct package (~245) | deep per-API docs |
| Tooling | 3 skills + 3 scripts + 3 hooks (consolidated, DRY) | per-package tooling |
| requirements.txt | live-env reconciliation, organized sections | unrequested dependency upgrades |

## 3. Deliverables & Acceptance Criteria

### 3.1 `technology-stacks.md` (root)
- **AC-1.1**: Contains one section per repo (26), listing language, runtime, package manager, key frameworks/libraries detected from manifests.
- **AC-1.2**: Machine-readable tables; validated by `node-dep-audit.py`.

### 3.2 `node-dependency.md` (root)
- **AC-2.1**: Per-repo table (repo, package, version spec, type dep/devDep).
- **AC-2.2**: Unique package index, deduped by name; each entry lists all repos using it.
- **AC-2.3**: Covers npm, npx, bun, bunx tooling (eslint, prettier, typescript, cspell, etc.).
- **AC-2.4**: Validated by `node-dep-audit.py` — every manifest dependency appears; exit 0.

### 3.3 `python-packages.md` (root)
- **AC-3.1**: Per-repo table for all 10 Python manifest locations.
- **AC-3.2**: Unique package index, deduped case-insensitively; every `requirements.txt`/`pyproject.toml` entry present (root: all 210).
- **AC-3.3**: Validated by `python-dep-audit.py` — exit 0.

### 3.4 Research cheat-sheets (`research/packages/node/`, `research/packages/python/`)
- **AC-4.1**: One file per direct package; filename = kebab-case slug ≤ 80 chars.
- **AC-4.2**: Template: title, metadata block (source, timestamp, backend), sections (Overview, Install, Core API / Usage, Links/Docs).
- **AC-4.3**: Doc count == unique package count (verify programmatically); no empty/stub docs (<200 chars content).
- **AC-4.4**: Each doc links ≥2 authoritative sources (official docs, npm/PyPI, GitHub).

### 3.5 Skills/scripts/hooks
- **AC-5.1**: `node-dep-audit` skill + `scripts/node-dep-audit.py` — parses all package.json, diffs vs `node-dependency.md`, exit 0/1 with report.
- **AC-5.2**: `python-dep-audit` skill + `scripts/python-dep-audit.py` — parses all Python manifests + requirements.txt, diffs vs `python-packages.md`, exit 0/1.
- **AC-5.3**: `research-doc-verify` skill + `scripts/research-doc-verify.py` — checks doc existence, size, required sections vs package lists.
- **AC-5.4**: `hooks/` scripts run the same audits non-destructively, output summary + exit code.

### 3.6 `requirements.txt`
- **AC-6.1**: Sections: `# Direct`, `# Dev`, `# Transitive`; preserves `==` pins.
- **AC-6.2**: Every package in `python-packages.md` present in the file.
- **AC-6.3**: Cross-checked against `~/myvenv` live freeze; differences reported, not silently dropped.

### 3.7 Governance docs
- **AC-7.1**: Plan at `.hermes/plans/2026-09-11_004316-dependency-ecosystem-audit.md` (status updated on completion).
- **AC-7.2**: Prompt at `.github/prompts/development/dependency-ecosystem-audit.prompt.md`.

## 4. Execution Order (fastest/parallel)

1. Phase 1–3 (controller): inventory → reports (single-pass data collection, verified by scripts).
2. Phase 4 (6 parallel subagents): research batches; per-batch workspace JSON for progress.
3. Phase 5 (controller): create 3 skills via skill_manage, 3 scripts, 3 hook scripts.
4. Phase 6 (controller): live-env freeze → classify → rewrite requirements.txt.
5. Phase 7 (controller): run all audits + `bun run check` + `pytest` → fix → commit.

## 5. Constraints

- Direct deps only (user decision). One cheat-sheet per direct package (user decision).
- Consolidated DRY tooling (user decision). Live-env requirements reconciliation (user decision).
- Destructive operations pre-approved; traceability via git commits.
- Windows/MSYS2: POSIX syntax in terminal; `C:/` paths for native tools; LF line endings (`core.autocrlf=true`).
- No secrets in outputs; `.env`/credentials never read or printed.

## 6. Verification Commands

```bash
python scripts/node-dep-audit.py        # exit 0
python scripts/python-dep-audit.py      # exit 0
python scripts/research-doc-verify.py   # exit 0
bun run check                           # pass
pytest -q                               # no regressions
```

## 7. Risks

| Risk | Mitigation |
|------|------------|
| Research backend rate limits/timeouts | Fallback chain fetch→tavily→web_search; retry; per-batch logging |
| Subagent doc drift (stubs, wrong sections) | research-doc-verify gates re-run before completion; re-dispatch fixes |
| myvenv env drift vs requirements.txt pins | Report MISSING/EXTRA explicitly; keep pins from manifests |
| Large batch (210 py) exceeds single session | 5+ parallel batches; workspace files to persist counts |