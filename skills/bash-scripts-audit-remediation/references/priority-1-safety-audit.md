# Priority 1 Safety Audit — Context-Dependent Risk Assessment

**Created:** 2026-05-27  
**Use case:** When auditing scripts with "CRITICAL" patterns that are actually safe in context

**SAFETY NOTE:** This file documents DANGEROUS patterns for educational purposes. These are examples of what NOT to do, not executable code.

## Context

During a multi-repo script audit (11K+ scripts), automated pattern matching flagged 3 scripts as CRITICAL based on destructive patterns:
- `rm -rf $TEMP_DIR` (install.sh)
- `rm -f $LOCK_PATH` (diagnose-and-fix-git.sh)
- `git branch -D` (delete-gone-branches.sh)

Manual review revealed all were **safe in context** — the patterns were legitimate, not bugs.

## Risk Assessment Pattern

When automation flags scripts as CRITICAL, perform context-dependent analysis:

### Safe Patterns (Not Actually Dangerous)

| Pattern | Why It's Safe | Example |
|---------|---------------|---------|
| `rm -rf $TEMP_DIR` in trap | Cleanup handler for temporary directory | `trap 'rm -rf "$TEMP_DIR" 2>/dev/null \|\| true' EXIT` |
| `rm -f $LOCK_PATH` | Removes git lock file only | `rm -f .git/index.lock` |
| `git branch -D` with dry-run | Has explicit `--apply` flag required | `git branch -D "$branch"` only runs with `--apply` |
| Temp file cleanup in exit handler | Standard cleanup pattern | `trap 'rm -f /tmp/myapp.$$' EXIT INT TERM` |

### Actually Dangerous Patterns (NEVER USE THESE)

**WARNING:** The following patterns are DANGEROUS and should never be used. They are documented here as examples to AVOID.

| Pattern | Why It's Dangerous | Fix |
|---------|-------------------|------|
| Recursive root deletion | Destroys entire filesystem | Validate paths, require confirmation |
| Code injection via eval | Arbitrary code execution | Use bash -c with sanitized args |
| Force push without dry-run | Overwrites remote history | Require --force-with-lease or explicit confirmation |
| Privileged deletion with unbound var | Deletes from root if variable empty | Add set -u, validate variable not empty |

## Audit Workflow

1. **Pattern match** — Flag scripts with known-dangerous patterns
2. **Read context** — Examine surrounding code (5-10 lines before/after)
3. **Classify** — Determine if pattern is safe/dangerous in context
4. **Verdict** — Mark as SAFE or BLOCKED with rationale

### Example: install.sh

**Pattern:** `rm -rf $TEMP_DIR`  
**Context (Line 37):**
```bash
trap 'rm -rf "$TEMP_DIR" 2>/dev/null || true' EXIT INT TERM
```
**Analysis:**
- `$TEMP_DIR` set earlier to `mktemp -d`
- Quoted variable prevents word splitting
- Only runs in trap handler (cleanup on exit)
- `|| true` prevents trap failure from killing script

**Verdict:** ✅ SAFE — Standard trap cleanup pattern

### Example: diagnose-and-fix-git.sh

**Pattern:** `rm -f $LOCK_PATH`  
**Context (Line 26):**
```bash
LOCK_PATH=".git/index.lock"
if rm -f "$LOCK_PATH"; then
```
**Analysis:**
- `$LOCK_PATH` hardcoded to `.git/index.lock`
- Git lock files are safe to delete when git process is stuck
- `-f` flag makes it idempotent (no error if missing)

**Verdict:** ✅ SAFE — Lock file removal only

### Example: delete-gone-branches.sh

**Pattern:** `git branch -D`  
**Context (Lines 12, 75):**
```bash
--apply    Actually delete the branches with `git branch -D`
...
if [[ "$APPLY" == "true" ]]; then
  git branch -D "$branch"
```
**Analysis:**
- Dry-run by default (prints branches, doesn't delete)
- Requires explicit `--apply` flag to delete
- User must consciously opt-in to destructive behavior

**Verdict:** ✅ SAFE — Dry-run default with explicit opt-in

## Scale-Aware Triage

When auditing 1K+ scripts, use **risk-based prioritization**:

### Triage Levels

| Priority | Script Count | Action |
|----------|--------------|--------|
| Priority 1 (CRITICAL patterns) | 4-5 | Manual audit (read full file) |
| Priority 2 (HIGH patterns) | 10-20 | Manual audit (targeted review) |
| Priority 3 (MEDIUM patterns) | 50-100 | Automated fix + spot check |
| Priority 4 (LOW patterns) | 100-500 | Automated fix, no review needed |
| Archive candidates | 1K-10K | Tag for deletion, defer audit |

### Example Triage Output

```
Total scripts: 11,152
- Archived dead code: ~9,400 (exclude from audit)
- Already TypeScript: ~1,204 (exclude from migration)
- Migration candidates: 15-20 (Priority 1-3 audit)
- Auto-fixable: ~500 (Priority 4, batch process)
```

## Automation Rules

1. **Never auto-delete** scripts flagged as CRITICAL — always require manual review
2. **Preserve context** in reports — show 5-10 lines before/after match
3. **Generate audit checklist** for Priority 1 scripts
4. **Document verdicts** in audit report with rationale
5. **Lock scope** before Phase 2 — get explicit approval on what to migrate

## Integration with Phase 1

Add Priority 1 audit to Phase 1 workflow:

```markdown
### Phase 1 Extended: Inventory + Risk Triage

1. Catalog all scripts (counts, types, LOC)
2. Flag CRITICAL/HIGH patterns via regex
3. **Priority 1 audit** — Manual review of CRITICAL scripts
4. Generate triage report with verdicts
5. Lock migration scope (exclude safe scripts, archive dead code)
```

## Verification Checklist

After Priority 1 audit:
- [ ] All CRITICAL scripts have explicit SAFE/BLOCKED verdict
- [ ] Verdicts include rationale (not just pattern match)
- [ ] Safe patterns documented with explanation
- [ ] Migration scope locked (count of scripts approved for Phase 2)
- [ ] Audit results embedded in Phase 1 report

## Related References

- `bash-common-pitfall-fixes.md` — Fix patterns for actual bugs
- `wrapper-orchestration-contract.md` — Wrapper-specific safety rules
- Phase 2 inputs — Use audit verdicts to filter migration candidates
