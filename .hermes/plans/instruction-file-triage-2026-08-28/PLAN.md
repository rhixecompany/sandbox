---
title: Instruction File Triage & Repair (Goal 1)
slug: instruction-file-triage-2026-08-28
status: in_progress
created: 2026-08-28T18:30+00:00
profile: adminbot
model: minimax/minimax-m3:free (openrouter)
goal: 1 of 2 (Goal 2 multi-agent-fanout already complete per SESSION_REPORT 18:00)
---

# Goal 1 — Instruction File Triage, Repair, Enhancement

## Context

The user (Alexa) requested comprehensive triage of all instruction-style files across
the workspace. Goal 2 (multi-agent provider fanout) was completed in the prior session
and verified intact (17/17 artifacts present). Goal 1 has not been executed end-to-end.

Discovery (Phase 0) found **251 real instruction files** (after excluding vendor dirs,
caches, spawn-trees, backups, node_modules, hermes-agent source) across:

| File type     | Pattern                          | Count (approx) |
| ------------- | -------------------------------- | -------------- |
| Persona       | `SOUL.md`                        | 30+            |
| User profile  | `USER.md`                        | 25+            |
| Agent memory  | `MEMORY.md`                      | 30+            |
| Agent rules   | `AGENTS.md`                      | 50+            |
| Agent rules   | `CLAUDE.md`                      | 40+            |
| Hermes root   | `.hermes.md`                     | 20+            |
| Cursor rules  | `.cursorrules`                   | 40+            |
| Copilot rules | `copilot-instructions.md` + `.github/copilot-instructions.md` | 80+ |

Common pathologies observed in inventory (sample read):
- **Bloat**: SOUL.md 200+ lines, >10 KB → violates the 250-line cap rule
- **Duplication**: Same rule in 3-5 files (e.g., MCP-first rule appears in SOUL.md, USER.md, AGENTS.md, .hermes.md)
- **Stale content**: References to "minimax/minimax-m3:free" when it was the old default; now `nvidia/nemotron-3-ultra-550b-a55b:free`
- **Embedded paths**: Old `Bash/` paths not yet migrated to `projects/Bash/`
- **Conflicting rules**: Some files require hook approval, others say skip

## Goal

1. **Triage** all 251 instruction files → classify into: canonical, duplicate, bloat, stale, conflicting
2. **Repair** pathologies with minimum invasive patches
3. **Enhance** with DRY cross-references and best-practice structure
4. **Verify** with deterministic gates: file count, line cap, rule-dedup count

## Hard Constraints

- **No destructive operations** without an approval gate per skill rule.
- **DRY principle** — when fixing, link to canonical source rather than copy-paste.
- **250-line SKILL.md cap** — enhancements go to `references/`.
- **MCP-first tool precedence** — prefer filesystem / ast-grep / memory MCP over native.
- **SandBox `core.autocrlf=true`** — write LF only.
- **No backup files** — use git for rollback.

## Output Artifacts

| Path | Purpose |
| ---- | ------- |
| `scripts/instruction_audit.py` | Triage script (stdlib only) — scans, classifies, reports |
| `scripts/instruction_fix.py` | Auto-fix script with --dry-run default (whitelist only) |
| `.hermes/plans/instruction-file-triage-2026-08-28/SPEC.md` | Full design |
| `.hermes/plans/instruction-file-triage-2026-08-28/PLAN.md` | This file |
| `.hermes/plans/instruction-file-triage-2026-08-28/implementation-plan.md` | Step-by-step |
| `.hermes/plans/instruction-file-triage-2026-08-28/audit-report.json` | Machine-readable |
| `.hermes/plans/instruction-file-triage-2026-08-28/audit-report.md` | Human-readable |
| `~/AppData/Local/hermes/skills/agent-core-architecture/instruction-triage/SKILL.md` | Umbrella skill |
| `~/AppData/Local/hermes/skills/agent-core-architecture/instruction-triage/references/...` | Detail files |
| `~/AppData/Local/hermes/skills/agent-core-architecture/instruction-triage/scripts/...` | Copy of audit/fix scripts |
| `~/AppData/Local/hermes/skills/agent-core-architecture/instruction-triage/templates/...` | Skeletons |
| `.github/prompts/instruction-triage.prompt.md` | Reusable prompt |
| `SESSION_REPORT.md` | Updated to record Goal 1 work |

## Strict-Sequential Phases

| Phase | Description | Gate |
| ----- | ----------- | ---- |
| P1    | SPEC.md — design output schema, classification rules, thresholds | SPEC complete |
| P2    | `instruction_audit.py` (read-only triage) | Script runs, report produced |
| P3    | Run audit, capture results, write audit-report.{json,md} | Report present, counts match |
| P4    | Triage findings → pick canonical sources, design DRY strategy | Strategy doc |
| P5    | `instruction_fix.py` (whitelist-only auto-fixer, --dry-run default) | Script runs dry-run cleanly |
| P6    | Skill `instruction-triage` (SKILL.md ≤250 lines + 3 refs + 3 scripts + 2 templates) | Skill published, hermes sees it |
| P7    | Prompt `.github/prompts/instruction-triage.prompt.md` | File exists, well-formed |
| P8    | Verification gates (V1-V6) — file count, line cap, dedup count, no backup files, bun lint clean | All 6 PASS |
| P9    | Update SESSION_REPORT.md with Goal 1 entry | Report updated |

## Verification Gates

| Gate | Check | Tool |
| ---- | ----- | ---- |
| V1 | `python scripts/instruction_audit.py` exits 0, 251 files scanned | terminal |
| V2 | `audit-report.json` valid JSON, has all classification fields | python json.load |
| V3 | `instruction_fix.py --dry-run` exits 0, zero files changed (idempotent) | terminal |
| V4 | Skill `instruction-triage` appears in `hermes skills list` | hermes |
| V5 | SKILL.md ≤250 lines | python wc -l |
| V6 | No `.bak`, `.backup`, `.old` files created | find |

## Risk

- **R1**: Auto-fix may corrupt frontmatter or duplicate sections.
  Mitigation: whitelist-only (line cap reduction, dead-link removal); never merge blocks.
- **R2**: 251 files is a large sweep. Batch to ≤7 files/run.
- **R3**: User may not want wholesale edits; restrict to read-only triage unless explicit "fix" requested. The user did request "fix, enhance" — proceed with whitelist fixes.

## Approval Gate

Destructive edits (file truncation, block removal) require explicit `--apply` flag with summary of
affected files. Default = `--dry-run`. No silent mutations.

## Open Questions

- None blocking. Will surface in audit report for user triage.

## Open Items (post-Goal-1)

- Per-project canonical SOUL/USER/MEMORY audit
- Cross-profile config sync
- Re-run after each new instruction file is added
