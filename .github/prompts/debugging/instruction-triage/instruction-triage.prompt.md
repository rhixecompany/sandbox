---
name: instruction-triage
title: Instruction File Triage
description: Audit, fix, and enhance instruction files (SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules, copilot-instructions.md) using the instruction-triage skill.
trigger: /instruction-triage
category: debugging
version: 1.0.0
author: OWL
license: MIT
tags: [instruction-files, audit, prompt]
metadata: 
hermes: 
toolsets: 
skills: 
- skill: using-superpowers
dependencies: []
formatter: markdown
---

# Instruction File Triage

## When to Use

- "Audit all my instruction files"
- "Find DRY violations in agent rules"
- "Detect bloat in SOUL.md / AGENTS.md"
- "Fix stale path references"

## Workflow (5 phases)

### Phase 1: Audit (read-only)

```bash
python scripts/instruction_audit.py --output .hermes/plans/instruction-file-triage/audit-report.json
```

Inspect `audit-report.md` for findings.

### Phase 2: Review

Identify:
- **Bloat** (>250 lines): trim or extract to `references/`
- **Stale**: run whitelist fix
- **DRY violations** (`cross_refs` with count > 3): consolidate to canonical

### Phase 3: Fix (whitelist only, dry-run first)

```bash
python scripts/instruction_fix.py          # dry-run
python scripts/instruction_fix.py --apply  # actually write
```

### Phase 4: Manual Enhancement

For bloat duplicates (e.g. mindstudio-agent CLAUDE.md × 6):
1. Pick canonical: `~/AppData/Local/hermes/plugins/mindstudio-agent/CLAUDE.md`
2. Replace 5 copies with: `<!-- See canonical: <path> -->`
3. Re-run audit; verify classification improves

### Phase 5: Verify

| Gate | Check |
| ---- | ----- |
| V1 | audit.py exits 0 |
| V2 | audit-report.json valid |
| V3 | fix.py dry-run idempotent (0 changes) |
| V4 | `hermes skills list \| grep instruction-triage` |
| V5 | SKILL.md ≤250 lines |
| V6 | no `.bak`/`.backup`/`.old` files |

## Output

- `scripts/.runtime/instruction-audit.json` — machine-readable
- `.hermes/plans/instruction-file-triage/audit-report.md` — human-readable
- Console: classification summary + top findings

## Pitfalls

- Don't auto-merge duplicate blocks — human review required
- Don't rename or delete instruction files — use git for rollback
- `Bash/` → `projects/Bash/` is correct; verify no double-substitution
- Mindstudio-agent CLAUDE.md is 391 lines by design (reference docs) — NOT auto-trim

## Reference

## Goal
Audit, fix, and enhance instruction files (SOUL.md, USER.md, MEMORY.md, .hermes.md, AGENTS.md, CLAUDE.md, .cursorrules, copilot-instructions.md) using the instruction-triage skill.

## Context

## Verification

<content>

<content>

<content>

Skill: `instruction-triage` (auto-loaded)
