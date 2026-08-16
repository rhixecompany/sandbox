---
author: Hermes Agent
description: Audit all active Hermes sessions for resource usage, stale sessions, and cleanup opportunities. Supports automated cleanup with safety checks.
category: qa
license: MIT
metadata:
  hermes:
    related_skills:
    - hermes-system-maintenance
    - session-audit-report
    - validate-memories
    tags:
    - sessions
    - audit
    - cleanup
    - maintenance
    - resource-management
name: session-audit
tags:
- sessions
- audit
- cleanup
- maintenance
- resource-management
- hermes
title: Session Audit
version: 1.0.0
---
# Session Audit

## Overview

Audit all active and recent Hermes sessions for resource usage (memory, CPU, disk), stale/abandoned sessions, and cleanup opportunities. Generates report with safety-checked cleanup recommendations.

## When to Use

- Periodic system maintenance
- Before major upgrades
- Resource pressure investigation
- Session hygiene

## Workflow

### Phase 1: Audit

```bash
# Skill-local script (self-contained). Fall back to the canonical copy at
# ~/AppData/Local/hermes/scripts/session_audit.py if the skill copy is absent.
SKILL_AUDIT="$LOCALAPPDATA/hermes/skills/qa/session-audit/scripts/session_audit.py"
python "$SKILL_AUDIT" --output docs/session-audit-report.md
```

### Phase 2: Cleanup

```bash
# Dry run
python "$SKILL_AUDIT" --cleanup --dry-run

# Apply (with safety)
python "$SKILL_AUDIT" --cleanup --max-age 7
```

## Script Reference

**Locations (byte-identical):**
- Skill-local: `~/AppData/Local/hermes/skills/qa/session-audit/scripts/session_audit.py`
- Canonical: `~/AppData/Local/hermes/scripts/session_audit.py`

**Options:**
| Flag | Description |
|------|-------------|
| `--output` | Report output path |
| `--cleanup` | Enable cleanup mode |
| `--dry-run` | Show what would be cleaned |
| `--max-age` | Max session age (default: 7d) |
| `--force` | Bypass safety checks |

## Safety

- Never cleans active sessions
- Preserves sessions with uncommitted work
- Backups before removal
- Configurable age threshold


## Pitfalls

- **None identified yet** — Review edge cases and failure modes for this skill's domain.
- **Assumptions** — Verify platform compatibility (Windows/Mac/Linux) before relying on default paths.
- **State management** — Terminal state persists across calls; exported vars and working directory carry forward.
- **Error handling** — Always validate tool output before proceeding to the next step.

## Related Skills

- `hermes-system-maintenance` — Full system maintenance
- `session-audit-report` — Session reporting
- `validate-memories` — Memory validation

## Verification Checklist

- [ ] Prerequisites and environment are properly configured
- [ ] Session Audit operations completed successfully
- [ ] Output meets expected quality and requirements
- [ ] Any errors during execution were resolved
- [ ] Changes are documented and committed if applicable

## Best Practices

1. **Prepare before executing**: Ensure all prerequisites and dependencies are in place
2. **Validate inputs**: Check configuration, parameters, and environment before running
3. **Handle errors gracefully**: Implement proper error handling and recovery
4. **Document results**: Keep records of what was done, what worked, and what didn't
5. **Clean up**: Remove temporary files, release resources after completion
