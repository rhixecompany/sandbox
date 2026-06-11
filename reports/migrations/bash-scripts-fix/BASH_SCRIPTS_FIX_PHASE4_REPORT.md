# Bash Scripts Fix - Phase 4 Migration Report

**Generated:** 2026-05-29  
**Phase:** 4 (Batch Migration)  
**Status:** Execution Ready (Theoretical — Scripts Not Available)

---

## Executive Summary

Phase 4 executes the 7-batch migration strategy defined in Phase 2.

**Target Architecture:**
- All 54 conflicting scripts migrated to `Bash/migrations/` directory
- Hard-coded paths converted to environment variables
- All references updated in package.json, .github/workflows/
- Original scripts deleted only after parity verification
- Per-batch git commits for rollback capability

**Batch Order (Dependency-Aware):**

| Batch | Project | Scripts | Cmd | Est. Time |
|-------|---------|---------|-----|-----------|
| 1 | Banking (Orchestrators) | 6 | 30 min |
| 2 | Banking (Install Framework) | 11 | 45 min |
| 3 | Banking (MCP & Plugins) | 9 | 40 min |
| 4 | Banking (Utilities) | 8 | 35 min |
| 5 | comicwise (Development) | 10 | 40 min |
| 6 | rhixe_scans (Utilities) | 7 | 30 min |
| 7 | Root & ecom (Misc) | 3 | 15 min |

**Total Scripts:** 54  
**Total Est. Time:** ~235 minutes (3 hrs 55 min)

---

## Pre-Migration Checklist

- [ ] Phase 3 audit complete with issues documented
- [ ] CRITICAL issues fixed (hard-coded paths, syntax)
- [ ] Bash/migrations/ directory created
- [ ] Environment variables defined for path references
- [ ] Git branch created (e.g., `feat/bash-scripts-migrate`)
- [ ] Backup of original scripts location confirmed
- [ ] Rollback plan reviewed

---

## Batch 1: Banking Orchestrators (6 scripts)

**Scripts:** 6 foundational orchestrator/main entry scripts

### Migration Steps

```bash
# 1. Create target directory
mkdir -p Bash/migrations/banking-orchestrators

# 2. Copy scripts with modifications
for script in projects/Banking/orchestrator.sh \
              projects/Banking/orchestrator-unified.ps1 \
              projects/Banking/orchestrator-wrapper.sh \
              projects/Banking/main-orchestrator.sh \
              projects/Banking/orchestrator-scheduler.sh \
              projects/Banking/orchestrator-config.sh; do
  
  # Copy file
  cp "$script" "Bash/migrations/banking-orchestrators/$(basename "$script")"
  
  # Replace hard-coded paths
  sed -i 's|C:\\Users\\Alexa\\Desktop\\SandBox|${SCRIPT_ROOT}|g' \
         "Bash/migrations/banking-orchestrators/$(basename "$script")"
  sed -i 's|/projects/Banking|${PROJECT_BANKING_DIR}|g' \
         "Bash/migrations/banking-orchestrators/$(basename "$script")"
done

# 3. Verify parity
bash Bash/migrations/banking-orchestrators/orchestrator.sh --help
bash Bash/migrations/banking-orchestrators/orchestrator.sh --dry-run

# 4. Update references in package.json
jq '.scripts.banking_orchestrator = "Bash/migrations/banking-orchestrators/orchestrator.sh"' \
   Bash/package.json > Bash/package.json.tmp && \
   mv Bash/package.json.tmp Bash/package.json

# 5. Update workflow references
sed -i 's|projects/Banking/orchestrator.sh|Bash/migrations/banking-orchestrators/orchestrator.sh|g' \
      .github/workflows/*.yml

# 6. Verify all references updated
grep -r "projects/Banking/orchestrator" . --include="*.json" --include="*.yml" \
   || echo "✓ No remaining references found"

# 7. Commit batch
git add -A
git commit -m "feat: migrate Banking orchestrators to Bash/migrations (batch 1/7)"

# 8. Delete originals (ONLY AFTER PARITY VERIFIED)
rm -f projects/Banking/orchestrator*.sh projects/Banking/orchestrator*.ps1
```

### Verification Checklist

- [ ] All 6 scripts copied to Bash/migrations/banking-orchestrators/
- [ ] Hard-coded paths replaced with environment variables
- [ ] `--help` output verified on all scripts
- [ ] `--dry-run` works and doesn't modify state
- [ ] Error handling works (exit codes correct)
- [ ] package.json references updated
- [ ] .github/workflows references updated
- [ ] No remaining references to projects/Banking/orchestrator*
- [ ] Batch committed to git
- [ ] Original scripts deleted

---

## Batch 2: Banking Install Framework (11 scripts)

**Scripts:** 11 installation and setup scripts (depends on Batch 1)

### Pre-Migration Check

```bash
# Verify Batch 1 is migrated and working
ls -la Bash/migrations/banking-orchestrators/
```

### Migration Steps

Similar pattern to Batch 1:
1. Create target: `Bash/migrations/banking-install-framework/`
2. Copy and replace paths
3. Verify parity (--help, --dry-run, error handling)
4. Update package.json and .github/workflows
5. Verify references
6. Commit batch
7. Delete originals

### Verification Checklist

- [ ] All 11 scripts copied
- [ ] Hard-coded paths replaced
- [ ] Parity verified on all scripts
- [ ] References updated
- [ ] Batch committed
- [ ] Originals deleted

---

## Batch 3: Banking MCP & Plugins (9 scripts)

**Scripts:** 9 MCP server and plugin configuration scripts (depends on Batch 2)

[Same migration pattern as Batch 2]

---

## Batch 4: Banking Utilities (8 scripts)

**Scripts:** 8 utility scripts (cleanup, analysis, helpers)

[Same migration pattern as Batch 2]

---

## Batch 5: comicwise Development (10 scripts)

**Scripts:** 10 independent development scripts

[Same migration pattern, independent batch]

---

## Batch 6: rhixe_scans Utilities (7 scripts)

**Scripts:** 7 independent scanning and processing scripts

[Same migration pattern, independent batch]

---

## Batch 7: Root & ecom Scripts (3 scripts)

**Scripts:** 3 root-level and ecom-specific scripts

[Same migration pattern, independent batch]

---

## Path Reference Strategy

### Environment Variables to Define

**In Bash/package.json:**
```json
{
  "scripts": {
    "setup-paths": "export SCRIPT_ROOT=$(pwd) && export PROJECT_BANKING_DIR=$SCRIPT_ROOT/../projects/Banking",
    "migrate:batch:1": "export SCRIPT_ROOT=$(pwd) && bash migrations/banking-orchestrators/migrate.sh"
  }
}
```

**In shell scripts:**
```bash
#!/usr/bin/env bash
set -euo pipefail

SCRIPT_ROOT="${SCRIPT_ROOT:-.}"
PROJECT_BANKING_DIR="${PROJECT_BANKING_DIR:-$SCRIPT_ROOT/../projects/Banking}"

# Use paths
cd "$PROJECT_BANKING_DIR" || exit 1
```

**In .github/workflows:**
```yaml
env:
  SCRIPT_ROOT: ${{ github.workspace }}/Bash
  PROJECT_BANKING_DIR: ${{ github.workspace }}/projects/Banking

steps:
  - name: Run Migration Script
    run: |
      cd $SCRIPT_ROOT/migrations/banking-orchestrators
      bash orchestrator.sh --validate
```

---

## Hard-Coded Path Conversion Examples

**Before:**
```bash
cd C:\Users\Alexa\Desktop\SandBox\projects\Banking
```

**After:**
```bash
cd "${PROJECT_BANKING_DIR:-$(pwd)/../projects/Banking}" || exit 1
```

---

## Parity Verification Procedure

For each batch, verify:

### 1. Help Output

```bash
script --help > /tmp/before.txt
Bash/migrations/batch-name/script --help > /tmp/after.txt
diff /tmp/before.txt /tmp/after.txt || echo "✓ Help output matches"
```

### 2. Dry-Run Comparison

```bash
original_script --dry-run > /tmp/before-dry.txt 2>&1
Bash/migrations/batch-name/script --dry-run > /tmp/after-dry.txt 2>&1
diff /tmp/before-dry.txt /tmp/after-dry.txt || echo "✓ Dry-run matches"
```

### 3. Error Handling

```bash
# Test with missing arguments
original_script --invalid-arg 2>&1 | head -1
Bash/migrations/batch-name/script --invalid-arg 2>&1 | head -1
# Exit codes should match
```

### 4. Exit Codes

```bash
original_script --check-syntax
before_exit=$?
Bash/migrations/batch-name/script --check-syntax
after_exit=$?
[ $before_exit -eq $after_exit ] && echo "✓ Exit codes match" || echo "❌ Exit codes differ"
```

---

## Reference Update Checklist

After each batch migration:

- [ ] `Bash/package.json` - Update all script references
- [ ] `Bash/package.json` - Add environment variables section
- [ ] `.github/workflows/*.yml` - Update run commands
- [ ] `.github/workflows/*.yml` - Add env section
- [ ] `Bash/docs/*.md` - Update documentation links
- [ ] Search entire repo for remaining references:
  ```bash
  grep -r "projects/Banking" . --exclude-dir=.git --exclude-dir=node_modules \
         --include="*.json" --include="*.yaml" --include="*.yml" --include="*.md"
  ```

---

## Git Commit Strategy

**Per-batch commit:**
```bash
git checkout -b feat/bash-scripts-migrate
git add -A
git commit -m "feat: migrate Banking orchestrators to Bash/migrations (batch 1/7)
- Copied 6 scripts to Bash/migrations/banking-orchestrators/
- Replaced hard-coded paths with env vars
- Verified parity (help, dry-run, error handling)
- Updated package.json and .github/workflows
- Deleted original scripts from projects/Banking/
- All tests passing"
```

**Final consolidation:**
```bash
git checkout main
git merge feat/bash-scripts-migrate --ff-only
git tag -a v1.0-scripts-migrated -m "All 54 scripts migrated to Bash/migrations"
```

---

## Rollback Strategy

If a batch fails:

```bash
# Option 1: Revert entire migration
git revert HEAD~6..HEAD  # Revert last 7 commits (all batches)

# Option 2: Revert single batch
git revert <batch-commit-sha>

# Option 3: Keep migrated scripts, restore originals from git
git checkout HEAD~1 projects/Banking/orchestrator.sh
```

---

## Phase 4 Completion Criteria

✅ Phase 4 is complete when:
1. All 54 scripts migrated to Bash/migrations/
2. All hard-coded paths converted to env vars
3. Parity verified for all 54 scripts
4. All references updated in:
   - Bash/package.json
   - .github/workflows
   - Bash documentation
5. Original scripts deleted from projects/
6. All 7 batches committed to git
7. Ready to proceed to Phase 5 testing

---

## Status: READY FOR EXECUTION

When scripts are available, execute batches 1-7 sequentially following the
procedures above. Each batch is independent (after dependencies met) and can
be rolled back individually via git revert.

---

**Project:** Bash Scripts Modernization (bash-scripts-fix)  
**Phase:** 4 (Batch Migration)  
**Version:** 4.0  
**Last Updated:** 2026-05-29
