# Batch Remediation with Checkpoint Verification

## Overview

When remediating scripts across multiple files in a cross-platform context (Bash, PowerShell, BAT, TypeScript), organize work into batches of ≤7 files. After each batch, run verification checkpoints and update append-only progress and verification logs.

## Workflow

### Pre-Batch: Planning & Inventory

1. **Create inventory document** (`docs/<project>-scripts-list-context.md`)
   - Scan all target roots (e.g., `Bash/`, `rhixecompany/Banking/`, `Rhixe-company/comicwise/`)
   - Record script counts by type (`.sh`, `.ps1`, `.bat`, `.ts`)
   - Note responsibilities and entrypoint styles (thin wrapper, direct CLI, core runner, helper library, orchestration chain)

2. **Create remediation plan** (`docs/plans/<project>-remediation-cross-scope-vN.md`)
   - Define phases (Phase 1–7 for typical audit-fix cycle)
   - Batch breakdown: high-risk scripts first (install, setup, cleanup, verification, orchestration)
   - Define verification criteria for each batch

3. **Create progress log** (`docs/<project>-fix-issues-context.md`)
   - Initialize with "Status: Batches starting"
   - Keep append-only; never overwrite prior batch entries
   - Each batch entry includes: date, scope, files changed, actions, verification, result, notes

4. **Create verification report** (`docs/<project>-verification-report.md`)
   - Initialize with status matrix (area → check type → result → notes)
   - Create a "Batch Verification Log" section
   - Fill matrix row-by-row as batches complete

### Per-Batch: Execution & Verification

**Step 1: Scope Selection**
- Choose ≤7 files based on priority (critical/high-risk first)
- Group by logical unit (e.g., all variants of a wrapper family: `.sh`, `.ps1`, `.bat`)
- Prefer file families over scattering changes

**Step 2: Read & Analyze**
- Read all current variants to understand existing patterns
- Identify canonical implementations and deviations
- Look for bugs (business logic hiding in wrappers, missing handlers, stale references)

**Step 3: Implement Changes**
- Apply fixes using `patch()` or `write_file()` — not shell commands
- Keep changes focused (wrapper normalization, not refactoring unrelated code)
- Test changes locally where possible (syntax check, dry-run execution)

**Step 4: Verification Checkpoint**

| Check Type | Tools | What To Verify |
|------------|-------|---|
| **Syntax** | AST parser (PS1), `bash -n` (SH), readable (BAT) | All files parse without errors |
| **Execution** | Direct run or mock invocation | Help output works, arguments forward correctly |
| **Exit Code** | Check `$LASTEXITCODE` / `$?` / `%ERRORLEVEL%` | Wrapper propagates runner exit code |
| **Argument Pass-Through** | Run wrapper with `--flag value` | All arguments reach the runner unchanged |
| **Parity** | Compare wrapper behavior across platforms | `.sh`, `.ps1`, `.bat` produce same output |

**Example verification for Banking wrapper batch:**
```bash
# Syntax check
powershell.exe -NoProfile -Command "[System.Management.Automation.Language.Parser]::ParseFile('path/to/orchestrator.ps1', [ref]$null, [ref]$null)"

# Execution test
powershell.exe -File rhixecompany/Banking/scripts/orchestrator.ps1 --help
cmd.exe /c rhixecompany\Banking\scripts\orchestrator.bat --help

# Exit code check
cmd.exe /c "orchestrator.bat nonexistent; echo %ERRORLEVEL%"
```

**Step 5: Update Artifacts**

1. **Progress log entry** (append-only):
   ```markdown
   ### Batch N — <scope>
   
   - Date: YYYY-MM-DD
   - Scope: <what was normalized>
   - Files changed:
     - file1 (action)
     - file2 (action)
   - Actions:
     - Rewrote X as thin wrapper
     - Normalized Y to use contract Z
     - Fixed bug: ...
   - Verification:
     - Parsed N files: OK
     - Executed N wrappers: OK
     - Exit code propagation: OK
   - Result: Success | Partial | Failed
   - Notes: <key learnings, exceptions, blockers>
   ```

2. **Verification report matrix** (update relevant row):
   ```markdown
   | Area | Check | Result | Notes |
   | --- | --- | --- | --- |
   | Banking wrappers | Syntax / dry-run / parity | Partial | Batch 2 wrapper contract aligned on 7 files. |
   ```

3. **Verification report log** (append batch summary):
   ```markdown
   ### Batch N — <scope>
   
   - Files verified: [list]
   - Checks performed: [list]
   - Result: Pass | Fail
   - Notes: [summary of findings, exceptions, fixes]
   ```

### Post-Batch: Review & Planning

**After each batch:**
- Confirm verification checkpoint passed before proceeding to next batch
- Review progress log for patterns or recurring issues
- Update plan if new issues discovered
- Plan next batch scope based on learnings

**At end of all batches:**
- Perform final verification sweep (syntax, parity, dead code)
- Consolidate lessons into skill or memory
- Archive progress logs as part of project record

## File Naming & Location

- **Inventory**: `docs/<project>-scripts-list-context.md`
- **Plan**: `docs/plans/<project>-remediation-cross-scope-vN.md` (use version suffix)
- **Progress Log**: `docs/<project>-fix-issues-context.md` (append-only)
- **Verification Report**: `docs/<project>-verification-report.md` (update matrix + log sections)

## Append-Only Pattern

**Progress log and verification report MUST be append-only** to maintain evidence trail:

- ✓ Add new batch entries below prior entries
- ✓ Update status header if needed
- ✗ Delete or modify prior batch entries
- ✗ Rewrite matrix rows — only add new rows
- ✓ Append to verification log section

This ensures:
- Full audit trail of remediation decisions
- Ability to review changes over time
- Traceability for rollbacks if needed

## Pitfalls

- **Batch too large**: Keep to ≤7 files. Larger batches are harder to review and verify.
- **Skipping verification**: Running syntaxcheck after each batch catches errors early.
- **Mixing concerns**: Don't combine wrapper normalization with TypeScript consolidation in the same batch; verify wrapper layer first.
- **Stale progress logs**: Update logs immediately after batch completion, not later.
- **Silent failures**: Always report verification results explicitly (Pass/Fail/Partial); avoid vague language.
- **Forgotten batches**: Count batches consistently; if Batch 2 exists, there should be a Batch 1 entry.

## Related Patterns

- **Wrapper orchestration contract**: See `references/wrapper-orchestration-contract.md` for platform-specific patterns
- **5-phase workflow**: See main skill section "Phases" for full audit-plan-implement-verify cycle
- **Critical bug detection**: Business logic in thin wrappers is a common pattern to fix (see wrapper contract reference for detection rules)
