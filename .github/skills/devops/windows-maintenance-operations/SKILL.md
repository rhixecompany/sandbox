---
author: Alexa
description: ''
license: MIT
name: windows-maintenance-operations
tags: null
title: Windows Maintenance Operations
version: 1.0.0

---
# Windows Maintenance Operations

## Trigger Conditions

Use this skill when:
- User asks to clean dependencies (node_modules, venv, etc.)
- User asks to clear system caches (NPM, Docker, VS Code, WinGet, Bun, PNPM, etc.)
- User asks to free disk space or perform maintenance
- User asks to run cleanup scripts or operations marked as destructive
- System is at critical disk capacity (0 bytes free, 100% full)
- Any operation requires `--dry-run` before real execution

## Workflow: Discovery → Preview → Execute → Validate

### Phase 1: Discovery & Metrics (Safe, Read-Only)

**ALWAYS start with metrics collection** before any deletion:

```bash
# 1. Capture BEFORE state
pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 2' > before.txt

# 2. Scan what would be deleted
bash clean_dependency_folders.sh --dry-run
bash cache-clean.sh --all --dry-run
```

**What to capture:**
- Total disk free space
- Largest folders by category
- Dependency count and types
- Cache types available
- Estimated reclaim potential

**Document the BEFORE metrics** in a report before proceeding.

---

### Phase 2: Preview & Approval (Safe, Non-Destructive)

**Run all operations in dry-run mode first:**

```bash
# Dependency cleanup (preview)
bash clean_dependency_folders.sh --dry-run

# Cache cleanup (preview)
bash cache-clean.sh --all --dry-run

# Git operations (if applicable)
bash git-commit-batches.sh --list
```

**Expected output:**
- "Found X folder(s), YYY MB" (what would be deleted)
- "[dry-run] would clean..." (cache operations)
- No actual changes made

**Always show results to user** before executing real operations.

**Require explicit approval** before moving to Phase 3 (execution is irreversible).

---

### Phase 3: Real Execution (Destructive)

**Only after explicit approval**, execute with `--auto` flag:

```bash
# Dependency cleanup (REAL)
bash clean_dependency_folders.sh --max-depth 2 --auto

# Cache cleanup (REAL)
bash cache-clean.sh --all --auto
```

**Execution notes:**
- Operations typically complete in <1 minute
- Use `--auto` flag to skip interactive confirmation
- Caches: Some require admin (flag with warning if not running as admin)
- Dependencies: Irreversible without `npm install` / `pip install` / etc.

**Capture logs:**
- Cache cleanup logs: `logs/cache-clean-*.log`
- Dependency logs: Tool-specific logs in `logs/`

---

### Phase 4: Validation & AFTER Metrics (Safe, Read-Only)

**Immediately after cleanup**, capture AFTER state:

```bash
# Capture AFTER state
pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 2' > after.txt

# Compare and report
echo "BEFORE: $BEFORE_FREE_MB MB free"
echo "AFTER: $AFTER_FREE_MB MB free"
echo "RECLAIMED: $(( AFTER_FREE_MB - BEFORE_FREE_MB )) MB"
```

**Success criteria:**
- ✓ BEFORE free space < AFTER free space
- ✓ Dependency folders reduced
- ✓ No errors in logs
- ✓ All cache types succeeded

---

### Phase 5: Recovery Documentation

**Always document recovery procedures** for reversible/restorable operations:

```markdown
## Recovery Procedures

### Restore npm Dependencies
  cd ~/path/to/project && npm install

### Restore Python venv
  cd ~/path/to/project && python -m venv venv

### Regenerate Caches
  • NPM: npm cache clean --force
  • Docker: docker system prune -a
  • Bun: bun pm cache rm
  • VS Code: Restart and let it rebuild
```

---
metadata:
  hermes:
    tags: []


## Safety Guardrails

### Critical: 0 Bytes Free Detection

When system is at 0 bytes (100% capacity):
- ✓ **DO execute immediately** after user approval
- ✓ **Skip the interactive confirmation** (use `--auto`)
- ✓ **Dependency cleanup first** (fastest, highest gain)
- ✓ **Then cache cleanup** (fills in remaining space)
- ⚠️ **Caches may require admin** — expected; document it

Example: At 0 bytes free, if you have 301 MB dependencies + 418 MB caches:
```
Before: 0 bytes free (100% full)
Action: Delete dependencies (301 MB)
Result: 301 MB free, system now operational
Then: Clean caches (~418 MB additional)
Final: ~719 MB free, disk operational
```

### Irreversible Operations

These cannot be undone without reinstall/rebuild:
- **node_modules** — Restore: `npm install`
- **Python venv** — Restore: `python -m venv venv`
- **.NET bin/obj** — Restore: dotnet rebuild
- **Java target/** — Restore: maven/gradle rebuild

⚠️ **Always warn user before deleting** dependency folders.

### Reversible Operations

These regenerate automatically:
- **NPM cache** — Regenerates on next `npm install`
- **Docker cache** — Regenerates on next build
- **Temp files** — Regenerates on next tool use
- **Thumbnails** — Windows regenerates on next file browse

---

## Common Cleanup Targets & Space Freed (Typical Windows Dev Machine)

| Target | Avg Space | Command | Reversible |
|--------|-----------|---------|-----------|
| node_modules (typical) | 100-500 MB | `clean_dependency_folders.sh` | No |
| Python venv | 50-200 MB | `clean_dependency_folders.sh` | No |
| Docker buildkit | 20-100 MB | `cache-clean.sh` | Yes |
| NPM cache | 50-200 MB | `cache-clean.sh` | Yes |
| Temp folder | 100-1000 MB | `cache-clean.sh` | Yes |
| Windows Update cache | 50-500 MB | `cache-clean.sh` | Yes |
| VS Code cache | 100-500 MB | `cache-clean.sh` | Yes |
| **TOTAL TYPICAL** | **300-1000 MB** | Combined ops | Mixed |

---

## Pitfalls

### ❌ Pitfall 1: Running Without Before Metrics
**Problem**: User can't verify if cleanup actually worked.  
**Fix**: Always capture disk state BEFORE and AFTER. Show the delta.

### ❌ Pitfall 2: No Approval on Destructive Ops
**Problem**: User doesn't know what's being deleted.  
**Fix**: Always show dry-run output and require explicit approval before `--auto`.

### ❌ Pitfall 3: Forgetting Recovery Procedures
**Problem**: User deletes node_modules, then can't restore.  
**Fix**: Document recovery steps for every destructive operation.

### ❌ Pitfall 4: Running As Non-Admin
**Problem**: Some caches (Windows Update, System Temp) require elevation.  
**Fix**: Check early, warn if not admin, skip admin-only operations gracefully.

### ❌ Pitfall 5: Deleting Code Dependencies Carelessly
**Problem**: Delete node_modules from an active project → breaks build.  
**Fix**: Verify project is not currently in use; document npm install step.

### ❌ Pitfall 6: Not Logging Operations
**Problem**: No audit trail if something goes wrong.  
**Fix**: Capture all logs, including timestamps and file deletions.

---

## Quick Reference

### One-Liner Safety Pattern

```bash
# SAFE: Dry-run only
bash clean_dependency_folders.sh --dry-run && bash cache-clean.sh --all --dry-run

# REAL: After user approval
bash clean_dependency_folders.sh --max-depth 2 --auto && bash cache-clean.sh --all --auto
```

### Check Disk BEFORE and AFTER

```bash
# BEFORE
pwsh -NoProfile -Command 'Get-Volume C | Select-Object SizeRemaining, Size'

# (do cleanup)

# AFTER
pwsh -NoProfile -Command 'Get-Volume C | Select-Object SizeRemaining, Size'
```

### Common Flags

| Flag | Meaning |
|------|---------|
| `--dry-run` | Preview only, no changes |
| `--auto` | Skip interactive prompts, execute |
| `--max-depth N` | Scan up to N directory levels |
| `--all` | Target all cache/dependency types |
| `--debug` | Show debug output |

---

## References

- Cache types: NPM, Docker, WinGet, Bun, PNPM, Git LFS, VS Code, Temp, Windows Update, DNS, Thumbnails, WER
- Recovery: `npm install`, `python -m venv venv`, `dotnet restore`, `mvn clean install`
- Tools: disk-analysis.ps1, cache-clean.sh, clean_dependency_folders.sh

## Verification Checklist

- [ ] Prerequisites verified and available
- [ ] Windows Maintenance Operations operations completed successfully
- [ ] Configuration or output verified against requirements
- [ ] No errors or warnings during execution
- [ ] Changes documented and committed if applicable

## Overview

Windows Maintenance Operations is a skill for handling windows maintenance operations tasks and automation workflows. Use this skill when you need to perform windows maintenance operations operations efficiently.

## When to Use


- When you need to perform Windows Maintenance Operations operations or tasks
- When managing Windows Maintenance Operations infrastructure or configurations
- When automating or debugging Windows Maintenance Operations workflows
- **Triggers**: "windows maintenance operations" required for a project

