# Disk Cleanup — Implementation Plan

**Date:** 2026-08-16  
**Type:** disk-cleanup / disk-space-cleanup / cleanup-disk  
**Status:** pending  

---

## Goal

Free disk space on C: drive (currently 100% full, 1.3GB free) by running comprehensive cleanup across workspace and Hermes root.

## Architecture

Two-phase approach: (1) Run cleanup_disk.py script for workspace + subrepos, (2) Enable and use disk-cleanup Hermes plugin for agent artifacts. Measure before/after.

## Tech Stack

- cleanup_disk.py (Python script at ~/AppData/Local/hermes/scripts/cleanup_disk.py)
- Hermes disk-cleanup plugin (bundled, opt-in)
- df -h / du -sh for measurement

---

## Tasks

### Task 1: Measure Current Disk State

**Objective:** Record before-state free space.

**Step 1: Check C: drive free space**
```bash
df -h /c
```

**Step 2: Find largest directories**
```bash
C:/Program\ Files/Git/usr/bin/bash.exe -c 'du -sh ~/AppData/Local/hermes/{skills,plugins,hooks,profiles,caches,.cache,.venv,node_modules} 2>/dev/null | sort -rh | head -10'
```

**Step 3: Document** → `.hermes/plans/results/disk-cleanup-before.txt`

---

### Task 2: Run cleanup_disk.py Dry-Run

**Objective:** Preview what would be deleted without actually deleting.

**Step 1: Run dry-run on SandBox**
```bash
cd ~/Desktop/SandBox && python3.11 scripts/cleanup_disk.py --verify --min-size 5 .
```
Note: Use python3.11 (not python3.13 which is pip-less). MSYS_NO_PATHCONV=1 for Windows paths.

**Step 2: Run dry-run on Hermes root (conservative)**
```bash
cd ~/Desktop/SandBox && python3.11 ~/AppData/Local/hermes/scripts/cleanup_disk.py --verify --cats cache,logs,archive "C:/Users/Alexa/AppData/Local/hermes"
```

**Step 3: Document** → `.hermes/plans/results/disk-cleanup-dryrun.txt`

---

### Task 3: Review and Approve

**Objective:** Review dry-run results and approve destructive apply.

**Step 1: Read dry-run results**
Read `.hermes/plans/results/disk-cleanup-dryrun.txt`

**Step 2: Calculate expected space gain**
Estimate based on dry-run output.

**Step 3: Record approval**
Create `.hermes/approvals/2026-08-16-disk-cleanup-approval.md` with:
- Scope of cleanup
- Expected space gain
- Rollback plan (nothing to rollback — all items are disposable)
- Approval timestamp

**⚠️ This is a destructive operation — requires explicit approval.**

---

### Task 4: Apply Cleanup (SandBox)

**Objective:** Execute cleanup on SandBox workspace.

**Step 1: Run cleanup_disk.py with --apply**
```bash
cd ~/Desktop/SandBox && MSYS_NO_PATHCONV=1 python3.11 scripts/cleanup_disk.py --apply --min-size 5 .
```

**Step 2: Document** → `.hermes/plans/results/disk-cleanup-apply-sandbox.txt`

---

### Task 5: Apply Cleanup (Hermes Root — Conservative)

**Objective:** Clean Hermes root caches/logs only (never deps).

**Step 1: Run cleanup_disk.py on Hermes root**
```bash
cd ~/Desktop/SandBox && MSYS_NO_PATHCONV=1 python3.11 ~/AppData/Local/hermes/scripts/cleanup_disk.py --apply --cats cache,logs,archive "C:/Users/Alexa/AppData/Local/hermes"
```

**Step 2: Document** → `.hermes/plans/results/disk-cleanup-apply-hermes.txt`

---

### Task 6: Enable disk-cleanup Plugin

**Objective:** Enable the Hermes bundled disk-cleanup plugin for ongoing maintenance.

**Step 1: Enable plugin**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes plugins enable disk-cleanup 2>&1'
```

**Step 2: Run disk-cleanup status**
```bash
cd ~/Desktop/SandBox && C:/Program\ Files/Git/usr/bin/bash.exe -c 'hermes disk-cleanup status 2>&1'
```

**Step 3: Document** → `.hermes/plans/results/disk-cleanup-plugin.txt`

---

### Task 7: Measure After State

**Objective:** Record after-state free space and calculate gain.

**Step 1: Check C: drive free space**
```bash
df -h /c
```

**Step 2: Calculate delta**
Compare with before-state from Task 1.

**Step 3: Document** → `.hermes/plans/results/disk-cleanup-after.txt`

---

### Task 8: Compile Cleanup Report

**Objective:** Produce complete disk cleanup report.

**Step 1: Aggregate all results**
Read all `.hermes/plans/results/disk-cleanup-*.txt` files.

**Step 2: Write final report**
Create `.hermes/plans/results/disk-cleanup-report.md` with:
- Before/after space measurements
- Items deleted per category
- Space gained per category
- Any errors or locked files
- Recommendations for ongoing maintenance

---

## Dependencies

- Task 1 → Task 2 → Task 3 (approval gate) → Tasks 4-5 (parallel) → Task 6 → Task 7 → Task 8

## Verification

- [ ] Before/after disk space measured
- [ ] Dry-run reviewed and approved
- [ ] Cleanup applied to SandBox
- [ ] Cleanup applied to Hermes root (conservative)
- [ ] disk-cleanup plugin enabled
- [ ] Final report compiled

## Approval Gate

**DESTRUCTIVE OPERATION.** Task 4 and Task 5 delete files. Review dry-run results (Task 2) and approve explicitly before proceeding.

## Pitfalls

- **argparse abbreviation:** `--roots` partially matches `--roots-file`. Script uses `allow_abbrev=False`.
- **Double-counting:** scanning parent + subroot duplicates entries — dedupe by resolved path.
- **Windows native Python:** can't resolve MSYS `/c/...` paths; use `C:/...` and `MSYS_NO_PATHCONV=1`.
- **Temp rmtree:** fails on in-use files; use age-based cleanup.
- **Hermes root:** never delete runtime deps (node_modules/venv needed by agent).
- **Active log files:** may be locked → script logs error and continues (expected).
- **npm quirk:** `npm config get omit` = dev globally → npm install/ci silently SKIP devDependencies.
