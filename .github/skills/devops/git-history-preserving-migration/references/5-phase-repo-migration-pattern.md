# 5-Phase Repository Migration Pattern

**Session:** 2026-05-27  
**Context:** Multi-repository consolidation with patch application and documentation generation  
**Outcome:** ✅ Success - 11 projects preserved, 4 patches processed, zero data loss

## Pattern Overview

A comprehensive 5-phase workflow for repository migration that prioritizes **documentation-first orchestration** and **safe patch handling** over immediate code changes.

## When to Use

- Migrating/consolidating 10+ repositories
- Applying patches of unknown compatibility
- Need comprehensive documentation before making changes
- Uncertainty about project states (empty dirs, stale patches, etc.)
- Safety-first requirement (no data loss acceptable)

## Phase Structure

### Phase 1: Inventory and Triage (READ-ONLY)
**Goal:** Understand what you have before changing anything

**Tasks:**
1. List all projects in target directory
2. Inventory all patch files (*.patch)
3. Analyze each project:
   - File count (detect empty directories early)
   - Git status and remote
   - Tech stack (package.json, requirements.txt)
   - Latest commit info
4. For each patch:
   - Map to target project (filename heuristics)
   - Run `git apply --check` (dry-run)
   - Document conflicts/compatibility
5. Generate comprehensive inventory report

**Output:** `docs/<workspace>-projects-list-context.md`

**Pitfall Avoided:** Phase 1's initial file count using `find ... | wc -l` in execute_code returned 0 for 7 projects due to bash command issues. The counts were corrected in Phase 4 before cleanup. **Lesson:** When file counts are suspiciously low (0) for known-active projects, re-verify with direct terminal calls before destructive operations.

---

### Phase 2: Documentation-First Orchestration (GENERATE)
**Goal:** Document current state BEFORE making changes

**Rationale:** If patches fail or migration introduces issues, you need baseline documentation to understand what changed.

**Tasks:**
1. For each active project (file_count > 0), generate:
   - `manifest.json` (metadata)
   - `summary.md` (executive summary)
   - `validation.md` (health check)
   - `cross-links.md` (dependency mapping)
2. Create project-specific documentation directories
3. Run validation checks (git status, file integrity)

**Output:** `docs/project-docs/<project>/*` (4 files per project)

**Technique:** Use `execute_code` with Python loops to generate documentation in parallel across all projects. This is faster than delegate_task for mechanical file generation.

**User Preference:** Direct execution with execute_code is preferred over delegation for multi-phase workflows with clear steps. Reserve delegation for tasks requiring deep reasoning or specialized expertise.

---

### Phase 3: Create Consolidation and Patch Plan (DESIGN)
**Goal:** Design the execution strategy without touching code

**Tasks:**
1. Categorize each patch:
   - **ARCHIVE** (too large, memory issues)
   - **SKIP** (obsolete, already applied)
   - **MANUAL_REVIEW** (minor conflicts)
   - **INVESTIGATE** (no target found)
   - **REGENERATE** (structural issues)
2. Identify deduplication opportunities
3. Design execution order (dependencies, risk level)
4. Define rollback procedures for each action
5. Create patch execution table (structured data)

**Outputs:**
- `docs/<workspace>-merge-plan.md` (human-readable)
- `docs/patch-execution-table.json` (machine-readable)

**Key Decision:** Patches showing "already exists" conflicts are likely **full repository snapshots** (not incremental changes). Mark as SKIP/obsolete instead of forcing application.

---

### Phase 4: Execute Migration and Apply Patches (APPLY)
**Goal:** Implement the plan with safety checks at each step

**Execution Order:**
1. **ARCHIVE** problematic patches (memory overflow, too large)
   - Move to `patches/archive/<patch>.YYYYMMDD`
   - Create README explaining why archived
2. **SKIP** obsolete patches
   - Move to `patches/obsolete/`
   - Document as "already applied"
3. **MANUAL REVIEW** patches with minor conflicts
   - Dry-run check: `git apply --check`
   - If clean, ready for apply
   - If conflicts, document for user review
4. **INVESTIGATE** patches with no target
   - Search workspace for potential targets
   - Document findings
5. **REGENERATE** patches with structural issues
   - Identify projects needing new patches
   - Note generation method (git format-patch)
6. **CLEANUP** empty directories
   - **CRITICAL:** Re-verify file counts before removing
   - Move to `projects/archive/empty-stubs/` (not delete)

**Output:** `docs/<workspace>-patch-application-report.md`

**Safety Protocol:**
- Archive before delete (never rm -rf directly)
- Move to archive/ directories (reversible)
- Create READMEs documenting all moves
- Log every action with timestamp

---

### Phase 5: Verification (VALIDATE)
**Goal:** Confirm zero data loss and document final state

**Checks:**
1. **Deliverable verification:** All phase outputs exist
2. **Patch state verification:** Count archived/obsolete/processed
3. **Project integrity:**
   - Directory exists
   - Is git repository
   - File count matches expected
   - No broken refs
4. **Data loss assessment:** Compare before/after states

**Output:** `docs/<workspace>-migration-final-report.md`

**Success Criteria:**
- ✅ All phases complete
- ✅ All validation reports PASS
- ✅ Zero data loss confirmed
- ✅ Rollback capability maintained

---

## Key Techniques

### 1. Execute_code for Parallel Processing
```python
from hermes_tools import terminal, write_file
for project in projects:
    # Analyze, generate docs, verify
    metadata = analyze_project(project)
    write_file(f"docs/project-docs/{project}/manifest.json", json.dumps(metadata))
```

**When:** Mechanical operations (file enumeration, template generation, batch writes)

### 2. Structured Logging
```python
log_entries = []
log_entries.append({
    "timestamp": datetime.now(),
    "action": "ARCHIVE",
    "target": "comicwise.patch",
    "status": "SUCCESS"
})
```

**When:** Tracking multi-step operations for audit trail

### 3. Progressive File Count Verification
```bash
# Initial check (Phase 1)
find projects/project-name -type f | wc -l

# Re-verification (Phase 4, before cleanup)
find projects/project-name -type f | wc -l
```

**When:** Before any destructive operation (delete, move, rm -rf)

### 4. Archive-First Safety
```bash
# NEVER:
rm -rf projects/empty-dir

# ALWAYS:
mkdir -p projects/archive/empty-stubs
mv projects/empty-dir projects/archive/empty-stubs/
echo "Reason: 0 files" > projects/archive/empty-stubs/README.md
```

**When:** Any directory removal or bulk deletion

---

## Pitfalls & Recovery

### Pitfall: Phase 1 File Count Errors
**Problem:** Bash `find | wc -l` returned 0 for active projects  
**Impact:** Nearly deleted 7 active projects (722-183 files each)  
**Recovery:** Re-counted in Phase 4 before cleanup → found files → preserved  
**Lesson:** Always re-verify "empty" directories before cleanup operations

### Pitfall: Large Patch Memory Overflow
**Problem:** 5.1GB comicwise.patch caused "Out of memory, realloc failed"  
**Solution:** Archive instead of apply, document reason  
**Lesson:** Test patch size before `git apply --check`; archive >1GB patches

### Pitfall: Missing Patch Files
**Problem:** profile.patch and run-audit.sh.patch not found  
**Investigation:** May have been applied earlier or never at workspace root  
**Resolution:** Document as SKIPPED with investigation notes  
**Lesson:** Don't fail entire workflow for missing patches; log and continue

---

## Deliverables Structure

```
docs/
├── <workspace>-projects-list-context.md        # Phase 1
├── phase2-documentation-plan.md                # Phase 2
├── project-docs/                               # Phase 2
│   ├── project-1/
│   │   ├── manifest.json
│   │   ├── summary.md
│   │   ├── validation.md
│   │   └── cross-links.md
│   └── [... more projects]
├── <workspace>-merge-plan.md                   # Phase 3
├── patch-execution-table.json                  # Phase 3
├── <workspace>-patch-application-report.md     # Phase 4
└── <workspace>-migration-final-report.md       # Phase 5

patches/
├── archive/
│   ├── <patch>.YYYYMMDD
│   └── README.md
├── obsolete/
│   ├── [patches already applied]
│   └── README.md
└── regenerate/
    └── [empty, ready for new patches]

projects/archive/
└── empty-stubs/
    ├── [moved directories]
    └── README.md
```

---

## Success Metrics (Example Session)

- **Projects analyzed:** 14
- **Active projects preserved:** 11 (35,322 files)
- **Patches processed:** 4 (1 archived, 3 obsolete)
- **Documentation generated:** 36 files
- **Data loss:** NONE
- **Execution time:** ~2 hours (automated)
- **Rollback capability:** ✅ Maintained

---

## When NOT to Use This Pattern

- Single repository migration (too heavyweight)
- No patches to apply (simpler copy/move workflow)
- All patches verified clean (skip Phase 1 dry-run)
- Time-critical migration (this is thorough, not fast)

For simpler migrations, use the standard git-history-preserving workflow in SKILL.md.

---

**Pattern Status:** ✅ VALIDATED (zero data loss, 11 projects preserved)  
**Recommended For:** Enterprise-scale repository consolidations with patch uncertainty
