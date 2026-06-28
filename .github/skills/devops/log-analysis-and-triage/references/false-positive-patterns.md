# False Positive Detection Patterns

## Pattern: "Tool Not Found" But Tool Exists

### Red Flags for False Positive
- Script reports "X not found" or "X not installed"
- But `which X` succeeds or direct invocation works
- Tool works in one context but not another (PowerShell vs. bash, WSL vs. native, subprocess vs. parent)

### Causes
1. **Subprocess environment isolation:** Tool is in parent's PATH but not subprocess's
   - PowerShell calls bash, which inherits limited PATH
   - Script runs in isolated environment (venv, container, WSL)
2. **Permission issue:** Tool exists but subprocess can't execute
3. **Script PATH logic error:** Script checks `if command -v X`, but environment differs at execution time

### Verification Checklist
```bash
# In parent shell
which <tool>
<tool> --version
<tool> <basic_operation>

# In subprocess (if applicable)
bash -c "which <tool>"
pwsh -c "Get-Command <tool>"

# Direct execution in parent
<tool> --help
```

If tool works in parent but script says it's missing → **environment or subprocess isolation issue**

---

## Pattern: Spawn/Interop Errors

### Red Flags for False Positive
- Error mentions `execvpe()`, `CreateProcessCommon`, `WSL`, `relay`, or `fork()`
- Error happens when one runtime calls another (PowerShell→Bash, WSL→Windows, subprocess spawning)
- Tool being invoked exists and works in its native context

### Causes
1. **WSL/MSYS2 interop:** PowerShell on Windows 10/11 with WSL or MSYS2
   - Windows process tries to execute `/bin/bash` but WSL environment not fully initialized
   - PATH confusion between native Windows and MSYS2 paths
2. **Subprocess environment:** Child process inherits different environment than parent
3. **Path escaping:** Shell quoting/escaping issues in nested calls

### Verification Checklist
```bash
# Test tool directly in current shell
bash --version
bash -c "echo OK"

# Test tool in parent context (e.g., from PowerShell)
# If this fails but direct shell call works → interop issue

# Check for path/symlink mismatches
ls -la /bin/bash
which bash
```

If tool works directly but fails when called from wrapper → **interop or environment issue**

---

## Pattern: Incomplete / Stalled Logs

### Red Flags for False Positive
- Log ends abruptly mid-operation (e.g., "Calculating folder sizes..." then EOF)
- No exit code or error marker at end of file
- Process metadata (start time) present but no end time
- Same script run multiple times with identical partial output

### Causes
1. **Process hung:** Script stalled, consumed excessive resources, got stuck in loop
2. **Timeout:** Process exceeded time limit and was killed
3. **Log truncation:** File was truncated (rare, but check `wc -l`)

### Verification Checklist
```bash
# Check for exit marker
tail -5 <log_file>

# Compare file size with others
ls -lS <logs_dir>

# Check if process still running (unlikely if log is old)
ps aux | grep <script_name>

# Re-run script to see if it completes
bash <script_name>
```

If script completes successfully when re-run → **stalled process, low priority**

---

## Pattern: Redundant Metrics / Snapshots

### Red Flags for Deletion Candidate
- Multiple files with identical structure (~102 bytes each)
- Content is only timestamp + 2–3 fields
- No unique information (same metrics across all files)
- Created in rapid succession (same script re-run)

### Example
```json
// metrics-20260527-222611.json
{
  "timestamp": "2026-05-27T22:26:11Z",
  "snapshot": "..."
}

// metrics-20260527-223107.json — identical structure, same fields
{
  "timestamp": "2026-05-27T22:31:07Z",
  "snapshot": "..."
}
```

### Verification
- Open 2–3 files
- Compare structure and field names
- If identical, delete all but latest (if any)

---

## Decision Tree: Real Failure vs. False Positive

```
┌─ Error log reports tool missing
├─ Does `which <tool>` succeed?
│  ├─ YES → FALSE POSITIVE (detection/environment issue)
│  │         Keep for record; debug caller
│  └─ NO → Could be real
│      ├─ Is tool really needed for this task?
│      │  ├─ YES → REAL FAILURE (install tool)
│      │  └─ NO → Low priority
│
├─ Error mentions spawn/interop (execvpe, CreateProcessCommon, WSL)
│  ├─ Does tool work directly?
│  │  ├─ YES → FALSE POSITIVE (wrapper issue)
│  │  │         Keep for interop diagnostics; fix caller
│  │  └─ NO → REAL FAILURE (tool missing or broken)
│
├─ Log incomplete (no exit marker)
│  ├─ Is process still running?
│  │  ├─ YES → Process hung (investigate)
│  │  └─ NO → Killed/timed out (low priority unless critical)
│
└─ Metrics/snapshots repeated
   ├─ Keep latest 1 if any
   └─ Delete rest (no unique value)
```

---

## Common False Positives in the Wild

| Error | Root Cause | Fix |
|-------|-----------|-----|
| `Winget is not installed` | PowerShell PATH isolation | Run `winget` directly; check subprocess ENV |
| `execvpe(/bin/bash) failed` | WSL interop, not bash missing | Verify `/bin/bash` exists; test bash directly |
| `npm ERR! not found: "git"` | Git not in subprocess PATH | Ensure git in parent PATH; check env inheritance |
| `python: command not found` | Venv not activated in subprocess | Activate venv in parent; check subprocess isolation |
| `docker: command not found` | Docker daemon not running or PATH issue | Check `docker ps`; verify Docker installation |

---

## Lessons Learned

1. **Always verify directly before concluding a tool is missing.**
   - Use `which`, `--version`, and a basic operation
   - Test in both parent and subprocess contexts

2. **Interop errors are real problems, but blame the wrapper, not the tool.**
   - PowerShell→Bash errors don't mean bash is broken
   - WSL errors don't mean the tool is missing
   - Fix the caller's environment or subprocess isolation

3. **Incomplete logs are usually low priority unless they block critical work.**
   - Stalled/hung processes are diagnostic issues, not functional failures
   - Keep for troubleshooting, but don't let them block progress

4. **Metrics snapshots clutter without value. Delete aggressively.**
   - Keep latest only if needed for trend analysis
   - Most cases: keep none

5. **Keep latest of each error type for 24–48 hours.**
   - Even false positives are useful if they recur
   - Helps detect patterns (e.g., "Winget detection fails every morning")

6. **Governance audit false positives in temp dirs are expected.**
   - Test sessions in `hermes-hook-test` trigger `sudo`/`chmod` threat detection
   - No action needed — the hook is working correctly
   - Verify by checking session cwd in audit log

7. **Memory tool drift (issue #26045) is a known hermes bug.**
   - When `patch` modifies MEMORY.md, memory tool internal state desyncs
   - Symptom: `.bak.*` files appear, all memory() calls fail
   - Fix: delete .bak files, skip memory update, resyncs next session
   - Do NOT retry memory() — it won't resolve until file is re-read

8. **Provider 402/429 errors are self-healing.**
   - Hermes marks provider unhealthy and retries automatically
   - Check current state with `hermes chat` before concluding it's broken
   - Persistent 402 = add credits; persistent 429 = wait for weekly reset
