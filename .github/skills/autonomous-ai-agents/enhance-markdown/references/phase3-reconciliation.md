# Phase 3 Reconciliation Pattern

## Problem

When Phase 2 marks plan items as complete `[x]`, Phase 3 cannot assume the fixes are actually applied to disk. Reasons:

1. **Plan-File desync:** Companion markdown was marked done, but the actual file write failed (timeout, permission error, subagent crash)
2. **Duplicate item in multiple batches:** The same file/issue was flagged in Batch 1 AND Batch 3; Batch 1 fix applied correctly, but plan wasn't updated, causing Batch 3 to claim it's already done when it actually is
3. **Subagent claim without verification:** The fix was promised by openagent/opencoder but the write was silently dropped or the rollback happened post-commit

## Solution: Disk-First Reconciliation

### Algorithm (Phase 3.2)

```python
# Load plan
plan_items = parse_companion_markdown(path="thoughts/plans/{purpose}-debug.md")
pending = [item for item in plan_items if item.status == "[ ]"]
confirmed_complete = [item for item in plan_items if item.status == "[x]"]

# Reconcile against disk
for item in confirmed_complete:
    file_path = item.target_file
    file_content = read_file(file_path)  # re-read from disk
    
    # Check if the fix is actually present
    if is_fix_present(file_content, item):
        # ✅ Fix is there — mark as confirmed
        log(f"✅ {item.id}: fix confirmed present on disk")
        continue
    else:
        # ❌ Fix is missing — re-apply
        log(f"⚠️ {item.id}: claimed fixed but NOT on disk — re-applying")
        apply_fix(item)
        file_content = read_file(file_path)  # verify again
        if is_fix_present(file_content, item):
            log(f"✅ {item.id}: re-applied successfully")
        else:
            log(f"❌ {item.id}: re-apply FAILED — marking as open")
            plan_items[item.id].status = "[ ]"
            pending.append(item)

# Execute pending items as normal
for item in pending:
    apply_fix(item)
    verify_on_disk(item)
    mark_complete(item)
```

### Detection: `is_fix_present(content, item)`

Depends on issue type:

| Issue Type | Detection Method |
| --- | --- |
| Unclosed code fence | `content.count('```') % 2 == 0` |
| Heading hierarchy | `extract_heading_at_line(item.line_num)` has correct level vs prev |
| Mixed tabs/spaces | `'\t' not in content[affected_region]` |
| Missing section | `'## Goal' in content` or equivalent section marker |
| TODO/FIXME | `'TODO' in content` (these are informational, never "fixed") |

### Session Example: github-prompts-batch (2026-05-29)

**Scenario:** Phase 2 applied heading hierarchy fixes to 6 files, marked them `[x]`. Phase 3 entry check found plan items already marked complete and was about to skip them.

**Discovery:** Re-verifying against disk showed all 6 files had correct fixes in place (no false alarm). If any had been missing, re-apply + re-verify pattern would have kicked in.

**Lesson:** The pattern prevented a potential silent failure — had the plan been trusted without disk verification, a failed write from Phase 2 would have been carried forward as "complete" into Phase 4, and the verify step would have caught it as a discrepancy. With Phase 3 reconciliation, the fix would have been re-applied preemptively.

## Integration into Phase 3

### Step 3.2 — Execute Remaining Items (updated)

```
FOR EACH pending item in plan:
  1. Apply fix via openagent
  2. Re-read modified file from disk
  3. Verify fix is present via is_fix_present()
  4. IF fix verified → mark [x]
  5. IF fix not verified → log ERROR, leave as [ ], continue

FOR EACH completed item [x] in plan (NEW — reconciliation):
  1. Re-read target file from disk
  2. Check if fix is actually present via is_fix_present()
  3. IF present → log "✅ confirmed", skip
  4. IF missing → log "⚠️ NOT on disk", re-apply + reverify, then mark [x]
```

## Edge Cases

### Case 1: Multiple fixes in the same file

If Phase 2 applied fixes A and B to file X in different batches:

- Batch 1 fixed A, marked done ✅
- Batch 2 fixed B, marked done ✅
- Phase 3: re-read file X
  - Check fix A: present ✅
  - Check fix B: present ✅
  - Mark both confirmed, skip

If B is missing (Batch 2 write timeout):

- Re-apply B, re-verify, mark done

If A is present but B is missing, and the fixes conflict (e.g., both edit the same line):

- Log: "⚠️ Conflict detected between items {A} and {B} in file {X}"
- Re-read and manually assess, or re-apply B with conflict resolution
- Do not silently overwrite A

### Case 2: TODO/FIXME "fixes"

TODO comments are informational and cannot be "fixed" by automated means. They should never be marked `[x]` in the plan.

**Correct behavior in Phase 2:** Mark as `Minor` severity, leave in plan as `[ ]`, skip fix application, mark with note in progress log: "Acknowledged as informational — no fix applied."

**If mistakenly marked `[x] in Phase 2:** Phase 3 reconciliation will try to check `is_fix_present()`, which returns `True` (the TODO is still there, unchanged), so it confirms as "complete." This is acceptable because the TODO was never meant to be removed.

**Better:** Exclude TODO items from the plan entirely, or mark them `[x] ACKNOWLEDGED` (non-standard marker) to indicate they were reviewed but not changed.

### Case 3: Subagent crash between fix and plan update

Rare but possible: openagent applied fix to disk, then crashed before updating the companion plan.

- In Phase 2: item remains `[ ]`, Phase 2 tries to re-apply, openagent is now healthy, fix is idempotent, re-apply succeeds, marked `[x]`
- In Phase 3: item is `[x]`, disk verification confirms present, skip

**Prevention:** In Phase 2, after openagent returns success, immediately re-read the file on disk and verify the fix BEFORE marking the plan item `[x]`. Do not trust the agent's word.

## Testing the Pattern

A minimal test: create a companion plan with one item marked `[x]`, manually delete the fix from the file, then run Phase 3 reconciliation. It should detect the missing fix and re-apply it.

```bash
# Simulate: mark item done but remove the actual fix
echo "- [x] test-issue: testfile.md — test fix" >> thoughts/plans/test-debug.md
# Manually revert the fix in testfile.md
git checkout testfile.md

# Run Phase 3 reconciliation
# Expected: Phase 3 detects missing fix, re-applies, verifies, marks confirmed
```

## References

- **Original issue:** Session 2026-05-29, github-prompts-batch audit. Phase 2 applied 5 unclosed code fence fixes and 6 heading hierarchy fixes. Phase 3 entry checks found items already marked complete and was about to skip them. Reconciliation verified all fixes were actually present on disk (no false alarm in this case, but pattern prevents future silent failures).
- **Related pitfalls:** See Phase 3 reconciliation pattern in enhance-markdown SKILL.md
