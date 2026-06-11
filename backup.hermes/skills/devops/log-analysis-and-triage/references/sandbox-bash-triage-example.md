# Triage Example: SandBox/Bash Logs (2026-05-27)

## Scenario
User workspace at `C:\Users\Alexa\Desktop\SandBox\Bash\logs/` accumulates 32 mixed log files over ~4 hours (21:32–22:42 UTC).
Task: Identify what matters, what to delete, what issues are real vs. false positives.

## Enumeration & Categorization

```
32 files, 6.5 KB total

By type:
  • errors-*.json (10 files) — mostly empty (~75 bytes) except latest (343 bytes)
  • metrics-*.json (10 files) — redundant snapshots (~102 bytes each)
  • analysis-*.log (3 files) — incomplete scans (~512 bytes each)
  • upgrade-2026-*.log (7 files) — stale ISO logs (~131 bytes each)
  • upgrade_native-*.log (2 files) — native upgrade failures (~1.1 KB each)
```

## Sampling

### Latest Error (errors-20260527-223913.json)
```json
{
  "Errors": [{
    "Script": "test-all.sh",
    "Error": "Syntax error: <3>WSL (2661 - Relay) ERROR: CreateProcessCommon:818: execvpe(/bin/bash) failed: No such file or directory",
    "ExitCode": 1,
    "Timestamp": "2026-05-27T22:42:38.4459252+01:00"
  }],
  "StartTime": "2026-05-27T22:39:13.5743567+01:00"
}
```

**Triage:** "execvpe(/bin/bash) failed" → Appears to be bash missing. **BUT:**
- `/bin/bash` exists and is executable (`ls -la /bin/bash` returns 2.5M file)
- Bash works: `bash --version` returns 5.2.37
- Direct spawn works: `bash -c "echo OK"` succeeds
- **Root cause:** PowerShell → WSL interop failure, not bash unavailability
- **Classification:** FALSE POSITIVE (Detection/Interop failure)

### Latest Native Upgrade Log (upgrade_native_20260527_223310.log)
```
Winget command found but not properly configured
Winget is not installed
Skipping winget update - not available
Chocolatey command found but not properly configured
Chocolatey is not installed
...
All package manager operations failed
```

**Triage:** Reports both Winget and Chocolatey missing. **BUT:**
- `winget --version` returns v1.28.240
- `choco --version` returns v2.5.0
- Both work: `winget list` and `choco list` succeed
- **Root cause:** PowerShell upgrade script has incorrect detection logic (likely PATH or subprocess environment issue)
- **Classification:** FALSE POSITIVE (Detection failure, tools work fine)

### Analysis Logs (3 identical, incomplete)
```
[2026-05-27 22:32:10] [SECTION] === Analysis started ===
[2026-05-27 22:32:10] [SECTION] Scanning path(s) for 92 target types...
...
[2026-05-27 22:32:12] [SECTION] === Found 119 dependency folders ===
[2026-05-27 22:32:12] [SECTION] Calculating folder sizes...
[END OF LOG — NO EXIT MARKER]
```

**Triage:** Size calculation stalled/hung. **Classification:** INCOMPLETE (low priority, no real failure indicated, just stalled process)

### Metrics Files
All ~102 bytes, contain only timestamp + minimal stats.

**Triage:** Redundant snapshots, no actionable data. **Classification:** STALE/REDUNDANT

### ISO Upgrade Logs (7 files)
All ~131 bytes, from 21:32–21:39 (old, ~1 hour before latest).

**Triage:** Stale attempts. **Classification:** STALE/REDUNDANT

---

## Triage Assessment

| Type | Count | Verdict | Action |
|------|-------|---------|--------|
| errors-*.json | 10 | Mostly empty stubs; 1 real error (bash spawn FALSE POSITIVE) | Keep latest 1, delete 9 |
| metrics-*.json | 10 | Redundant snapshots | Delete all |
| analysis-*.log | 3 | Stalled/incomplete, no failure | Keep latest 1, delete 2 |
| upgrade-2026-*.log | 7 | Stale, no content | Delete all |
| upgrade_native-*.log | 2 | Both show FALSE POSITIVES (tools exist but script can't detect) | Keep 1 for record, delete 1 |

---

## Cleanup Decision

**Before:** 32 files, 6.5 KB  
**After:** 4 files, 2.8 KB  
**Deleted:** 28 files  
**Space saved:** 3.6 KB (91% reduction)

**Kept for diagnostics:**
- `analysis-20260527-220517.log` — latest scan (119 folders found, incomplete but useful reference)
- `errors-20260527-223913.json` — latest error (bash spawn, documented as false positive)
- `upgrade_native_20260527_223242.log` — native upgrade attempt (false positive, documented)
- `upgrade_native_20260527_223310.log` — same script, same failure, redundant

---

## Verification

After cleanup, verified all "missing" tools work:

```bash
✓ /usr/bin/bash: GNU bash 5.2.37 (MSYS2)
✓ /bin/bash: exists, executable
✓ test-all.sh: direct run succeeds, 15/15 tests PASS

✓ winget v1.28.240: lists 50+ packages
✓ choco v2.5.0: lists 100+ packages
```

---

## Key Learnings

1. **Detection failure ≠ Tool failure.** Always verify tool directly before concluding it's missing.
2. **Interop errors are real but blame the wrapper, not the tool.** PowerShell→Bash errors don't mean bash is broken.
3. **Incomplete logs ≠ failures.** Stalled/hung processes are low priority unless they block critical work.
4. **Metrics snapshots clutter without value.** Delete aggressively.
5. **Keep latest of each type.** Even false positives are useful diagnostics if they recur.
