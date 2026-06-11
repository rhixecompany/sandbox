# Project Consolidation Execution Prompt

**Status**: Ready to Execute Phase 3 & 4  
**Approval Required**: Yes - destructive operations

---

## Quick Start

Execute all phases in sequence:

```
1. Create backups
2. Consolidate duplicates (keep target, delete source)
3. Copy source-only projects to target
4. Verify all projects
5. Archive source directory
6. Document consolidation
```

---

## Execution Checklist

### BACKUPS (CRITICAL - Do First)

- [ ] Create backup of C:\Users\Alexa\Desktop\SandBox\Rhixe-company (source)
- [ ] Create backup of C:\Users\Alexa\Desktop\SandBox\rhixecompany (target)
- [ ] Store backups safely with timestamp
- [ ] Verify backup integrity

### PHASE 3: CONSOLIDATION

#### 3.1 Handle Duplicates (10 projects)

**HIGH-PRIORITY (Delete from source, keep target)**
- [ ] cookiecutter-django-tailwind - DELETE source copy
- [ ] Django-Scrapy-Selenium - DELETE source copy
- [ ] selenium_webdriver - DELETE source copy
- [ ] youtube-downloader - DELETE source copy

**MEDIUM-PRIORITY (Compare, then keep best version)**
- [ ] ecom - COMPARE & MERGE
- [ ] Python-projects - COMPARE & MERGE
- [ ] rhixe_scans - COMPARE & MERGE
- [ ] university-libary-jsm - COMPARE & MERGE

**REQUIRES INVESTIGATION**
- [ ] rhixecompany - Verify purpose and keep
- [ ] xamehitv - Keep (consolidate xamehi variants into this)

#### 3.2 Copy Source-Only Projects to Target

- [ ] **comicwise** - Copy from source to target
- [ ] **rhixe.company** - Copy from source, rename to rhixe-company in target
- [ ] **xamehi** - Copy from source to target
- [ ] **xamehi.tv** - Copy from source OR merge into xamehitv

#### 3.3 Naming Standardization

- [ ] Ensure rhixe-company (hyphen) is canonical
- [ ] Consolidate xamehi family into single directory structure
- [ ] Update all documentation

### PHASE 4: VERIFICATION

- [ ] All 14+ projects present in target
- [ ] All git repos are valid (git fsck --full)
- [ ] No broken references in imports
- [ ] All project READMEs accessible
- [ ] No uncommitted changes left behind

### PHASE 5: CLEANUP

- [ ] Create CONSOLIDATION.md documenting all changes
- [ ] Archive source Rhixe-company directory
- [ ] Remove or rename source directory
- [ ] Store backups long-term

---

## Commands Reference

### Create Backups (FIRST!)
```bash
mkdir -p C:\Users\Alexa\Desktop\SandBox\Backups\backup_$(date +%Y%m%d_%H%M%S)

# Backup source
xcopy "C:\Users\Alexa\Desktop\SandBox\Rhixe-company" \
      "C:\Users\Alexa\Desktop\SandBox\Backups\Rhixe-company_backup" /E /I /Y

# Backup target
xcopy "C:\Users\Alexa\Desktop\SandBox\rhixecompany" \
      "C:\Users\Alexa\Desktop\SandBox\Backups\rhixecompany_backup" /E /I /Y

echo "Backups created. Verify with: dir C:\Users\Alexa\Desktop\SandBox\Backups"
```

### Copy Single Project
```bash
xcopy "C:\Users\Alexa\Desktop\SandBox\Rhixe-company\[PROJECT]" \
      "C:\Users\Alexa\Desktop\SandBox\rhixecompany\[PROJECT]" /E /I /Y
```

### Copy & Rename Project
```bash
xcopy "C:\Users\Alexa\Desktop\SandBox\Rhixe-company\rhixe.company" \
      "C:\Users\Alexa\Desktop\SandBox\rhixecompany\rhixe-company" /E /I /Y
```

### Delete Project
```bash
rmdir "C:\Users\Alexa\Desktop\SandBox\Rhixe-company\[PROJECT]" /S /Q
```

### Verify Git Integrity
```bash
cd "C:\Users\Alexa\Desktop\SandBox\rhixecompany\[PROJECT]"
git fsck --full
git status
```

### List All Projects
```bash
cd "C:\Users\Alexa\Desktop\SandBox\rhixecompany"
ls -1d */ | sort
```

---

## Decision Points

### Decision 1: xamehi Consolidation
Current state:
- Source has: xamehi, xamehi.tv, xamehitv
- Target has: xamehitv

**Options**:
A) Keep xamehitv as canonical, delete xamehi variants from source
B) Copy xamehi & xamehi.tv to target, keep all three
C) Merge all three into single xamehi directory with subdirectories

**Recommendation**: Option B (keep all three for now, document relationship)

### Decision 2: rhixe-company Precedence
Current state:
- Source has: rhixe.company (with dot)
- Target has: rhixe-company (with hyphen)

**Options**:
A) Keep target's rhixe-company, delete source's rhixe.company
B) Merge both, keeping newer version
C) Keep both with different names (legacy support)

**Recommendation**: Option A (use hyphen naming convention)

---

## Risk Mitigation

**BEFORE executing any destructive operation**:
1. Backups must be verified
2. At least 2 independent copies exist
3. Git repos must pass fsck check
4. Approval explicitly given for each delete

**IF something goes wrong**:
1. STOP immediately
2. Restore from backup
3. Retry with adjusted strategy
4. Document what went wrong

---

## Success Metrics

After consolidation:
- Single source of truth at C:\Users\Alexa\Desktop\SandBox\rhixecompany
- Zero duplicate projects
- All git histories preserved
- All projects functional
- Documentation complete
- Backups archived

---

## Timeline

**Phase 3 (Consolidation)**: 4 hours
- 1 hr: Create/verify backups
- 1 hr: Handle duplicates
- 1 hr: Copy source-only projects
- 1 hr: Rename/standardize

**Phase 4 (Verification)**: 1-2 hours
- Verify all projects
- Fix any broken references
- Update documentation

**Phase 5 (Cleanup)**: 30 min
- Archive source directory
- Document consolidation
- Store backups

**TOTAL**: 5.5-6.5 hours

---

## Approval

- [ ] User approves full end-to-end execution
- [ ] User approves backup strategy
- [ ] User approves deletion of duplicates
- [ ] User approves source directory archive

---

**NEXT**: Await approval, then execute Phase 3
