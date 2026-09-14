---
name: prompt-library-de-dup-and-backup-archive.prompt
title: Implementation Prompt — Prompt Library De-Dup and Backup Archive
version: 1.0.0
date: 2026-09-13
subgoal: prompt-library-de-dup-and-backup-archive
destructive: true
protocol: multi-file-change-protocol
---

# Implementation Prompt — prompt-library-de-dup-and-backup-archive

## Execution Commands (sequential audit-first; destructive only after audit gate)

```bash
# Phase 1 — Audit (verify both directories exist)
ls -la .github/prompts .github/prompts_backup 2>/dev/null || echo "One dir missing — audit blocked"

# Phase 1b — Run Python audit (produces ./specs/*.md + *.json)
python3 -c "import os, hashlib, json ..."  # or use scripts/prompt-library-de-dup-audit.sh

# Phase 2 — Verify audit artifacts before destructive action
cat ./specs/prompt-library-de-dup-audit.md
cat ./specs/prompt-library-de-dup-audit-data.json | head -n 30

# Phase 3 — Apply destructive actions (only after audit verification)
bash scripts/prompt-library-de-dup-audit.sh  # executes delete/update/migrate + log creation

# Phase 4 — Final gate verification
ls .github/prompts_backup 2>/dev/null || echo "BACKUP REMOVED — PASS"
cat ./specs/prompt-library-de-dup-action-log.md | tail -n 5
```

## Artifact Checklist (post-execution verification)
- [ ] `.github/prompts_backup` deleted
- [ ] `./plans/prompt-library-de-dup-and-backup-archive-plan.md` exists
- [ ] `./specs/prompt-library-de-dup-and-backup-archive-spec.md` exists
- [ ] `scripts/prompt-library-de-dup-audit.sh` exists
- [ ] `skills/prompt-library-de-dup-and-backup-archive/SKILL.md` exists
- [ ] `./prompts/prompt-library-de-dup-and-backup-archive.prompt.md` exists (this file)
- [ ] `./specs/prompt-library-de-dup-action-log.md` exists and lists each destructive action
- [ ] No placeholder text in artifacts; SKILL.md ≤250 lines (verified: 55 lines)

## Related
- Skill: `skills/prompt-library-de-dup-and-backup-archive/`
- Plan: `./plans/prompt-library-de-dup-and-backup-archive-plan.md`
- Spec: `./specs/prompt-library-de-dup-and-backup-archive-spec.md`
- Script: `scripts/prompt-library-de-dup-audit.sh`
- Audit: `./specs/prompt-library-de-dup-audit.md` + `.json`
- Log: `./specs/prompt-library-de-dup-action-log.md`
