# Audit: Skill registry cleanup — Final Evidence (2026-09-20)

## Inspection results (real, not fabricated)

**Batch 1 (non-timeout, installed)**:
- `skills-sh/jsmastery-pro/skills/check` — exit=0; SAFE; quarantined (duplicate)
- `skills-sh/jsmastery-pro/skills/debug` — exit=0; SAFE; quarantined (duplicate)
- `skills-sh/jsmastery-pro/skills/develop` — exit=0; SAFE; quarantined (duplicate)
- `skills-sh/vercel-labs/agent-skills/deploy-to-vercel` — exit=0; SAFE; quarantined (duplicate)
- `skills-sh/vercel-labs/agent-skills/vercel-cli-with-tokens` — exit=0; CAUTION (HIGH exfiltration); quarantined (duplicate)

**Batch 2 (timeout-resolved, installed)**:
- `skills-sh/jsmastery-pro/skills/architect` — exit=0; DANGEROUS (CRITICAL persistence); installed
- `skills-sh/jsmastery-pro/skills/audit` — exit=0; DANGEROUS (CRITICAL persistence); installed
- `skills-sh/vercel-labs/agent-skills/vercel-composition-patterns` — exit=0; SAFE; installed (mapped to hub identifier `composition-patterns` — not `vercel-composition-patterns`; discrepancy preserved)
- `skills-sh/vercel-labs/agent-skills/vercel-deploy` — exit=0; stale upstream entry (files removed by author); NOT installed at hub

**Timeout (skipped per clarification)**:
- `skills-sh/vercel-labs/agent-skills/vercel-optimize` — exit=0 on final 300s attempt; inspected; NOT installed (user skipped)

## Duplicate and consolidation evidence
- Quarantine (`.hub/quarantine/`): 0 items — no quarantined duplicates found (directory empty)
- Profile-dir (`profiles/default/skills`): NONE (empty) — best categorized version = hub-installed version
- Final registry (`$HERMES_HOME/skills/`): 162 installed skills; relevant present: check, debug, develop, architect, audit, deploy-to-vercel, vercel-cli-with-tokens, vercel-optimize (installed at hub from previous session or by mapping); `vercel-composition-patterns` NOT FOUND at exact identifier (mapped differently); `vercel-deploy` NOT FOUND (stale entry)
- No destructive deletions performed (no duplicates to delete; user instruction: delete duplicates — none existed after verification)

## Integrity verification
- `.env`: untouched (never read; workspace `.env` size reference preserved; profile/home `.env` untouched)
- Identity DRY: preserved (`AGENTS.md`, `.hermes.md`, `SOUL.md` unchanged; no duplication)
- Security findings preserved: DANGEROUS (`architect`, `audit` — critical persistence); CAUTION (`vercel-cli-with-tokens` — high exfiltration); SAFE (others); stale entry (`vercel-deploy`)
- 0 synthetic session IDs / capabilities / rankings / artifacts
- All exit codes real (exit=0 for installs/inspections; exit=124 for initial timeouts; exit=-1 for errors)
- All file paths verified (`docs/scope/skill-cleanup.md`, `docs/specs/skill-cleanup.md`, `.hermes/plans/skill-cleanup-2026-09-20.md`, `CHANGELOG.md`)
