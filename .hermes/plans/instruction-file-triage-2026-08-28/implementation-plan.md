---
title: Implementation Plan — Instruction Triage (Step-by-step)
slug: instruction-triage-impl-2026-08-28
---

# Implementation Plan — Step-by-step

## Step 1: Audit script (no execution yet)

File: `scripts/instruction_audit.py`
- 200-300 lines, stdlib only
- Function: `audit(root_paths, skip_patterns) -> AuditReport`
- Walks, classifies per SPEC §3, emits JSON per SPEC §4
- Test with `python scripts/instruction_audit.py` (writes `scripts/.runtime/instruction-audit.json`)

## Step 2: Run audit, copy to plan dir

```bash
python scripts/instruction_audit.py
cp scripts/.runtime/instruction-audit.json .hermes/plans/instruction-file-triage-2026-08-28/audit-report.json
```

## Step 3: Generate human-readable report

`scripts/render_audit_report.py` (or inline python): JSON → markdown
- Table per file with: path, type, size, lines, class, issues
- Summary section: counts, top 10 bloat files, top 10 duplicates

## Step 4: Fix script (whitelist only)

File: `scripts/instruction_fix.py`
- 150-200 lines
- Loads `templates/whitelist-fixes.json`
- For each file in scope, applies each rule
- `--dry-run` (default) prints diffs, no writes
- `--apply` writes changes, prints per-file diff

## Step 5: Run fix --dry-run

```bash
python scripts/instruction_fix.py --dry-run
# Expected: exit 0, "0 files would change" (first run on clean files)
```

## Step 6: Publish skill

`~/AppData/Local/hermes/skills/agent-core-architecture/instruction-triage/`
- `SKILL.md` (≤250 lines)
- `references/classification-rules.md`
- `references/whitelist-fixes.md`
- `references/output-schema.md`
- `scripts/audit.sh` (bash wrapper)
- `scripts/fix.sh` (bash wrapper)
- `templates/audit-report.json` (skeleton)
- `templates/whitelist-fixes.json` (add new rules here)

## Step 7: Publish prompt

`.github/prompts/instruction-triage.prompt.md` — 60-80 lines, 5-phase workflow

## Step 8: Verification gates V1-V6

```bash
# V1
python scripts/instruction_audit.py && echo "V1 PASS"

# V2
python -c "import json; d=json.load(open('.hermes/plans/instruction-file-triage-2026-08-28/audit-report.json')); assert 'totals' in d; assert 'files' in d" && echo "V2 PASS"

# V3
python scripts/instruction_fix.py --dry-run | grep -q "0 files would change" && echo "V3 PASS"

# V4
hermes skills list | grep -q "instruction-triage" && echo "V4 PASS"

# V5
wc -l ~/AppData/Local/hermes/skills/agent-core-architecture/instruction-triage/SKILL.md | awk '{ if ($1<=250) print "V5 PASS" }'

# V6
find C:/Users/Alexa/Desktop/SandBox C:/Users/Alexa/AppData/Local/hermes -name "*.bak" -o -name "*.backup" -o -name "*.old" 2>/dev/null | wc -l
# Expected: 0
```

## Step 9: Update SESSION_REPORT.md

Append Goal 1 section with: artifacts created, V1-V6 results, top-10 findings, open items.

## Step 10: Commit

Only if all gates pass. Per user-communication-preferences: never commit without explicit ask.
Skip auto-commit; let user decide.
