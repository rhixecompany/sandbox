# Disk Cleanup Workflow — Brainstorming

**Date:** 2026-08-16  
**Type:** disk-cleanup / disk-space-cleanup / cleanup-disk  
**Status:** draft  

---

## Problem Statement

C: drive is at 100% capacity (1.3GB free of 237GB). This is a critical blocker for any operations that need disk space. The Hermes skills directory alone is 18.3 MB across 2803 files. The .env file is 28KB. The SandBox has 32 modified files.

---

## Available Tools

| Tool | Type | Description |
|------|------|-------------|
| `cleanup_disk.py` | Python script | Full-sweep cleanup: deps, archive, cache, logs. Dry-run-first, safe hermes-root filtering. Located at `~/AppData/Local/hermes/scripts/cleanup_disk.py` |
| `disk-cleanup` plugin | Hermes bundled plugin | `/disk-cleanup status`, `/disk-cleanup dry-run`, `/disk-cleanup quick`, `/disk-cleanup deep`. Opt-in, never auto-enabled. |
| `disk-space-cleanup` skill | Skill | Full-sweep workflow: measure, dry-run, apply, verify. Uses cleanup_disk.py as canonical script. |
| `cleanup-disk` skill | Skill | Wrapper for cleanup_disk.py script. |

---

## SCAMPER Analysis

### Substitute
- cleanup_disk.py (canonical script) vs disk-cleanup plugin (narrower scope) — use both for different purposes
- Manual `du -sh` + `df -h` vs automated script — script is more thorough

### Combine
- cleanup_disk.py (workspace + subrepos) + disk-cleanup plugin (Hermes artifacts) = comprehensive cleanup
- Measure → dry-run → approve → apply → verify = complete workflow

### Adapt
- Adapt the OpenRouter workflow template to disk cleanup: 8-step verification pattern

### Modify
- Hermes root: ONLY cache, logs, archive — NEVER deps (runtime node_modules/venv needed by agent)
- Temp folder: age-based cleanup (>3 days), not wholesale rmtree (files in use)

### Eliminate
- Eliminate bloated .git objects via `git gc --prune=now` (safe, non-history-rewriting)
- Eliminate app unused via `winget list` → `winget uninstall --id <id> --silent` (only after approval)

### Reverse
- Instead of cleaning everything, clean only the biggest space-wasters first

---

## Cleanup Categories (from cleanup_disk.py)

| Category | Targets | Scope |
|----------|---------|-------|
| deps | node_modules, venv, .venv, myvenv, __pycache__, dist, build, .next, .tox | SandBox + subrepos |
| archive | .archive, backup, *.bak, *.orig, *.rej, *~ | SandBox + subrepos |
| cache | .cache, npm-cache | SandBox + subrepos |
| logs | *.log, *.tmp | SandBox + subrepos |
| hermes root | cache, logs, archive ONLY | ~/AppData/Local/hermes |
| temp | Age-based (>3 days) + empty dirs | C:\Users\Alexa\AppData\Local\Temp |

---

## Key Decisions Needed

1. Which categories to run? (all? deps only? hermes root separate?)
2. Min-size threshold? (default: 5MB — skip smaller items)
3. Include OS caches? (pip/npm/bun/Temp)
4. App uninstall inventory needed?

---

## Implementation Artifacts Needed

- `.hermes/plans/disk-cleanup-implementation-plan.md`
- Execution results in `.hermes/plans/results/disk-cleanup-*.txt`
