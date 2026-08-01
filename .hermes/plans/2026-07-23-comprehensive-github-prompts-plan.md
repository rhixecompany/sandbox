# 2026-07-23 Comprehensive Plan: Normalize `.github` Prompt Assets and Cross-References

> Status: approved for execution
> Approver: Alexa
> Date: 2026-07-23

> Goal: migrate all Hermes prompt and instruction assets under `.github/prompts`, read/maintain/debug/fix/enhance/upgrade them, remove legacy duplicates, patch cross-references, and verify only canonical paths remain.

## Objectives

- Canonical prompt root is `.github/prompts`.
- Exact-duplicate prompt/instruction bodies are deduped; only one copy remains.
- All active `.github` docs, workflows, and instructions reference canonical paths only.
- Changes are auditable via `git` and verification report.

## Scope

In:

- `.github/prompts/**`
- Active repo metadata/docs: `.github/copilot-instructions.md`, `.github/workflows/*`, `.github/instructions/*`, `README.md`, `AGENTS.md`, `SESSION_REPORT.md`, `.hermes/plans/*`
- Hermes hooks and scripts used by prompt-management workflows in this repo

Out:

- External or vendored skill files under `node_modules`, `myvenv`, other project-private `.claude/.cursor` trees unless owned by this repo root

## Principles

- Canonical over copy-paste: prefer updating canonical files.
- Exact-body dedupe only; no semantic merging without user decision.
- Context-budget awareness: avoid pasting entire prompts; use file references and diff targets.
- Invariants: `.github/agents`, `.github/instructions`, `.github/skills` removed only after references are migrated and verified.

## Phases

### Phase 1: Baseline Audit

- Enumerate canonical prompt inventory and counts by category.
- Scan for exact-duplicate bodies across `.github/prompts`.
- Find all stale references to legacy prompt roots outside archived historical text.

Acceptance:

- Audit JSON/JSONL written `.hermes/audits/2026-07-23-github-prompts-baseline.json`.
- Duplicate count confirmed.

### Phase 2: Canonical Path Normalization

- Update every active reference from legacy `.github/agents|instructions|skills/` to `.github/prompts/agents|instructions|skills/`.
- Update stale `prompts/**` workflow filters to `.github/prompts/**` where intended.
- Patch `agent-skills`, `agents`, and agent prompts that still point to legacy roots.

Acceptance:

- Zero active stale references outside archived/history text.
- Retention: archived history preserved as historical docs; active instructions normalized.

### Phase 3: Dedupe and Prune

- Consolidate exact-duplicate bodies:
  - within `agents/` and `instructions/`
  - across `skills/**/SKILL.md` only if exact bodies match
- Keep canonical path, archive extras under `.github/prompts/archived/dup-<name>/`, update references if needed.

Acceptance:

- Duplicate report shows 0 remaining exact duplicates in active set.

### Phase 4: Directory Hygiene

- Confirm `.github/prompts/` has only canonical subdirectories.
- Confirm no leftover legacy root dirs remain.
- Ensure all needed skills, scripts, or README snippets exist on disk.

Acceptance:

- `find .github -maxdepth 2 -type d` shows only active canonical dirs plus workflows.

### Phase 5: Verification and Reporting

- Re-run counts, duplicate scan, stale-reference scan.
- Generate migration diff/artifacts summary and save to docs.
- Update `SESSION_REPORT.md` with final state and verification evidence.

Acceptance:

- Verification script exits clean, reports zero new issues, writes `.hermes/audits/...`.

## Success Criteria

- `.github/prompts/` exists with canonical `agents/`, `instructions/`, `skills/`, `archived/`.
- Legacy prompt roots either removed or empty and documented as removed.
- No exact-duplicate bodies remain in active prompt set.
- Zero active stale canonical-path references remain.
- Verification report saved to `.hermes/audits/`.

## Risks and Mitigations

- File-count mismatch due to former legacy dirs still present in `git status`: run `git status --short` and diff stat for exact artifact report.
- Archived history mentions old paths: preserve as historical text; do not alter archival provenance unless creating a note.
- Context budget: avoid full-file dumps. Summarize via counts, file lists, and issue counts.

## Tasks and Owners

- Phase 1 audit: terminal/read-only
- Phase 2 normalization: patch/read across active docs/canonical copies
- Phase 3 dedupe: terminal scan + patch/move/archive duplicates
- Phase 4 hygiene: directory/file manipulation
- Phase 5 verification: terminal + write report files
