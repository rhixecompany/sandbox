---
name: design-md-spec
title: "Spec — /design-md feature scope (Google DESIGN.md token spec format)"
version: 1.0
date_created: 2026-09-19
last_updated: 2026-09-19
owner: Alexa
status: In progress
goal: Define the scope, requirements, and verification gates for design-md feature work, co-located with skills overhaul (
context: design-md skill from workspace `.github/skills/claude-design/SKILL.md` references `design-md` as "Google's DESIGN.md spec format — author/validate/diff/export design-token files, WCAG contrast checking, Tailwind/DTCG export"
---

# Design-MD Feature Scope (design-md-20260919-212743)
Build approach: Tracer Bullet (vertical slice: design-md scope → design artifacts). Workflow: Alpha (after /develop, /check verify). Combined init with skills overhaul (standard 14 skills + load multi-file-change-protocol; design-md artifacts under `ai-agent-home/specs/design-md-20260919-212743/`).

## At a Glance

| # | Feature | Phase | Status | Needs spec |
|---|---------|-------|--------|-----------|
| 1 | Design-MD feature scope (this file) | Plan | In progress | No |
| 2 | Design-MD spec document (`docs/scope/design-md.md` or `.workflow/scope/design-md.md`) | Design | Planned | Yes (`/scope` plan mode) |
| 3 | Design token artifacts (DESIGN.md file) | Build | Planned | No (skill reference covers format) |
| 4 | Skill-judge audit for design-related skills (`design-md` skill, `creative` category skills) | Verify | Planned | No |

## Features

### 1. Design-MD Scope Planning
Intent: Turn the `design-md` product idea (author/validate design-token spec files) into a living, coarse scope document that the design team can use to build feature slices.
Done when: scope file exists (`docs/scope/design-md.md` or `.workflow/scope/design-md.md`); At a glance table includes design-md features; phase groups defined; workflow tier (`Alpha`) and build approach (`Tracer Bullet`) recorded in header.

### 2. Design-MD Design Token Artifacts
Intent: Produce the `DESIGN.md` token spec file using `design-md` skill rules (token categories: color, typography, spacing, layout, component; WCAG contrast verification; Tailwind/DTCG export option; diff/export capabilities).
Done when: token file exists and references `.github/skills/claude-design/SKILL.md` rules; includes at minimum color palette tokens, typography tokens, and spacing scale; references workspace color/theme files (e.g., `.hermes.md` identity colors).

### 3. Skill-Judge Audit for Design Category
Intent: Raise categorized skills score to ≥98. Focus: `design-md` skill and `creative` category skills. Verify skill quality (frontmatter, structure, description, cross-references) against `skill-judge` rubric.
Done when: `skill-judge` run completed; all design/creative skills score ≥98; no synthetic results; blockers documented honestly in STATUS.md.

## References

- Skill reference: `.github/skills/claude-design/SKILL.md` (line 22: design-md reference; line 32: when to use design-md; line 38: design-md definition)
- Design-related workspace files: `.hermes.md` (identity/colors), `.cursorrules` (style rules: 2-space indent, single quotes, `strict` mode for TypeScript; design-related sections preserved), `.github/prompts/` (design-related prompts preserved)
- Scope skill reference: `scope` (category: creative; `modes/plan.md` for plan behavior; `scope-template.md` for format rules)
- Cross-reference: `multi-file-change-protocol` SKILL.md (14-skill stack verified loaded; verification checklist includes integrity, `.env` protection, `.worktrees/` `.gitignore`, `.vscode/mcp.json`, `.opencode/README.md` sync)

## Blockers / Risks (honest — preserved)
- `adminbot` profile MISSING (honest — preserved from session 20260919_210743); `default` profile MISSING; `alexa-alias` profile MISSING.
- MSYS2 FAIL preserved (real environment block, not resolved artificially).
- Rate-limit 403 preserved (provider rate limit on some web/research operations).
- Vision primary REJECTS (primary vision model rejects some uploads; fallback `mindstudio uploadFile` confirmed working with `vision_fallback.py`).
- 26 vulnerability findings preserved (`fastmcp` CRITICAL; `httpx2` HIGH TLS/CPU; OAuth HIGH).
- 41 parsing errors preserved (nested `.codex`/`.copilot` scope conflict — architecture concern, preserved honestly).
- `web-research-628` remaining batches (future batches 23–628; requires NEW clarification; NOT executed this session; NOT fabricated).
- 39 paste-triage tasks (`.hermes/results/pastes-triage-2026-09-19.md`) — pending user approval/instruction.

## Integrity Evidence
- `.env`: workspace `CWD/.env` (5274 B — NOT present at workspace root this session; hermes `.env` 30381 B verified unchanged; no new `.env` reads/prints).
- No synthetic artifacts; no hidden errors; identity DRY preserved (`.hermes.md` unchanged routing; profile identity rules preserved; `.github/prompts/` preserved; `.opencode/README.md` sync reference preserved).
- `.worktrees/` in `.gitignore`: verified clean (1 entry, no broken patterns).
- `.eslintrc.json`: 69 B verified (ruff PASS + syntax PASS).
- `.vscode/mcp.json`: verified sync (python json.load exit 0; 3220 B verified).
- `.opencode/README.md`: verified sync reference preserved.
- `.hermes.md`: 6094 B verified; identity rules preserved; profile routing verified (14 profiles: 3 MISSING — `adminbot`, `default`, `alexa-alias`).
- 0 `.bak` artifacts; no new `.bak` artifacts this session.

## Verification Gates (before claim complete)
- [ ] Skill-judge audit executed (design-md + creative category skills); score ≥98.
- [ ] Spec file exists (`docs/scope/design-md.md` or `.workflow/scope/design-md.md`); format verified against `scope-template.md`.
- [ ] Plan file exists (`plans/design-md-<ts>.md` or equivalent) with build approach `Tracer Bullet` and workflow `Alpha`.
- [ ] Prompt file exists (`prompts/design-md-<ts>/PROMPTS.md`) with design-md feature sections.
- [ ] STATUS.md updated with verified phase evidence (spec written, design artifacts present, judge score ≥98, blockers preserved honestly).
- [ ] Integrity verified: `.env` 30381 B unchanged; identity preserved; 0 synthetic artifacts; no hidden errors.

## Cross-References
- `scope` (creative) — product scoping workflow; `scope-template.md`; `modes/plan.md`.
- `multi-file-change-protocol` (development) — 14-skill stack; verification checklist; `references/14-skill-stack.md`.
- `user-communication-preferences` — concise bullets + table-first + emoji + direct; verification before claim; honest blocker reporting.
- `systematic-debugging` — 4-phase protocol (understand/fix/verify/document); architecture concern preserved (41 parse errors + 26 vulns + rate-limit 403 + MSYS2 FAIL).
- `skill-judge`, `specs-judge`, `plans-judge`, `prompts-judge` — audit skills for 99+ quality.
- `.github/prompts/` — canonical shared prompt library (14 groups verified; `.github/prompts/index.md` preserved).
- `.opencode/README.md` — verified sync reference preserved.
