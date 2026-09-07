---
name: disk-cleanup-workflow
title: Disk Cleanup Workflow Specification
status: in_progress
owner: Alexa
version: 1.0.0
---

## Goal

Disk cleanup workflow specification covering dependency cleaning, archive removal, cache clearing, and hermes root cleanup with safe destructive operations.

## Requirements

### Dependencies & Scope
- [ ] Disk (C:) status documented: total, used, free space
- [ ] SandBox git status documented (modified, untracked files)
- [ ] Identify all cleanup categories: deps, archive, cache, logs, hermes root, temp

### Cleanup Categories
- [ ] **deps**: node_modules, venv, .venv, __pycache__, dist, build in SandBox and subrepos
- [ ] **archive**: .archive, backup, *.bak, *.orig, *.rej, *~
- [ ] **cache**: .cache, npm-cache in workspace
- [ ] **logs**: *.log, *.tmp in workspace
- [ ] **hermes root**: cache, logs, archive ONLY (never deps)
- [ ] **temp**: C:\Users\Alexa\AppData\Local\Temp — age-based (>3 days)

### Safety Requirements
- [ ] Destructive operations require explicit approval before --apply
- [ ] Dry-run mode available for all cleanup operations
- [ ] Backup strategy before cleanup (git commits, file copies)
- [ ] Cleanup script (cleanup_disk.py) available and tested

### Execution Plan
- [ ] Phase 1: Dry-run and report what will be deleted
- [ ] Phase 2: Get explicit approval for --apply
- [ ] Phase 3: Execute cleanup with --apply
- [ ] Phase 4: Verify disk space recovered
- [ ] Phase 5: Commit results

## Acceptance Criteria

| Check | Command | Expected |
|-------|---------|----------|
| Dry-run reports | `python cleanup_disk.py --dry-run` | Lists all files to be cleaned |
| Disk before | `df -h /c` | Free space recorded |
| Cleanup applied | `python cleanup_disk.py --apply` | Files deleted per categories |
| Disk after | `df -h /c` | Free space increased |
| Git clean | `git status --short` | No unexpected deletions |
| No deps deleted | Verify hermes root | Only cache/logs/archive removed |

## Non-Functional Requirements

Dry-run completes within 30 seconds. Cleanup --apply completes within 5 minutes. No more than 10% of total files deleted. Disk space recovery measurable in GB. Destructive operations require explicit --apply flag.

## Verification

```bash
# 1. Dry-run to see what will be cleaned
python cleanup_disk.py --dry-run

# 2. Record disk space before
# Windows: wmic logicaldisk get size,freespace,caption

# 3. Apply cleanup (requires explicit approval)
python cleanup_disk.py --apply

# 4. Verify disk space recovered
# Compare before/after free space

# 5. Verify no deps deleted in hermes root
ls ~/AppData/Local/hermes/node_modules 2>/dev/null || echo "No node_modules in hermes root (correct)"

# 6. Git status check
git status --short
```

## Linked Specs
- disk-cleanup-workflow-spec.md

## Linked Plan
- ../provider-workflow-master-plan.md

