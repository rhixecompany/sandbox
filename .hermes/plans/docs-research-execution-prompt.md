---
name: docs-research-execution-prompt
title: "Execute Docs & Research Consolidation"
description: "Execute the remaining phases of the docs/research consolidation plan. Skills created, scripts verified, deletions done. Run verification and final reporting."
---

# Execute: Docs & Research Consolidation — Final Steps

## Context
Phases 0-4 complete: 459 auto-generated files deleted (1.1MB reclaimed), 3 reference skills created, docs-inventory-report.py script created. Remaining: verification and cleanup.

## Required Skills
- `/executing-plans` — batch execution framework
- `/verification-before-completion` — cross-reference verification

## Tasks

### Task 1: Verify Deletions
Count files per subdirectory in docs/ and research/ and compare to expected values:
- docs/skills-reports/: 0 files (was 284) — empty directory
- docs/skills-audit/: 1 file (index.md only) — was 177
- Total docs subdir files: ~133 (was 593)
- Total research files: 25 (unchanged)

### Task 2: Run Inventory Report
```bash
python3 ~/AppData/Local/hermes/scripts/docs-inventory-report.py
```
Report writes to `.hermes/plans/inventory/docs-inventory-report.md`

### Task 3: Verify New Skills
```bash
ls ~/AppData/Local/hermes/skills/reference/mcp-server-catalog/SKILL.md
ls ~/AppData/Local/hermes/skills/reference/api-tutorial-catalog/SKILL.md  
ls ~/AppData/Local/hermes/skills/reference/project-architecture-index/SKILL.md
```
All 3 should exist and be non-empty.

### Task 4: Git Commit (Optional)
```bash
cd ~/Desktop/SandBox
git add -A
git commit -m "docs: consolidate docs/research — delete 459 auto-generated files, create 3 ref skills, add inventory script"
```

### Task 5: Update SESSION_REPORT.md
Append consolidation results to session report.

## Completion Criteria
- [ ] docs/skills-reports/ empty
- [ ] docs/skills-audit/ has only index.md
- [ ] 3 reference skills exist
- [ ] docs-inventory-report.py runs without errors
- [ ] Session report updated
