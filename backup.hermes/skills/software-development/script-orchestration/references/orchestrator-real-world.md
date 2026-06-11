# Real-World Implementation: Sandbox/Bash Orchestrator

## Project Context

**Date:** 2026-05-27  
**Goal:** Consolidate 180 scripts (177 original + 3 orchestrator wrappers) across 11 directories into unified management system  
**Constraint:** Auto-run by default; interactive discovery; error recovery; structured logging  

## Script Inventory

```
Total: 180 scripts

Core Production (64 scripts)
├─ src/ (15 TypeScript)
│  • upgrade.ts, cache-clean.ts, clean-dep.ts, git-commit-batches.ts
│  • dry-run.ts, ast-transformer.ts, behavior-test.ts, script-runner.ts
│  • 7 library modules (cli, colors, errors, logging)
│
├─ scripts/ (27 PowerShell orchestration)
│  • 9 phase-based orchestration scripts (discovery, clone, triage, debug, remediation, cross-ref)
│  • 9 shared libraries (git-ops, clone-utils, dependency-scanner, package-managers, etc.)
│  • 9 utility scripts
│
└─ root/ (22 production wrappers + utilities)
   • disk-analysis.ps1, cache-clean.ps1, clean-dependency-folders.ps1, upgrade.ps1
   • 18 supporting utilities

Domain-Specific (95 scripts)
├─ Banking/ (34 scripts)
│  • Installation framework (11 + libs)
│  • Operational scripts: verification, diagnostics, MCP integration
│
├─ archive/skills-commit-batches/ (51 scripts)
│  • 26 numbered pairs: skills-commit-batch-1.ps1 + .sh through batch-26
│
├─ comicwise/ (10 scripts)
│  • setup-dev, dev, cleanup, install-vscode-extensions, quality-gate
│
├─ Bash/ (7 scripts)
│  • Migration utilities: migrate-script.sh, mark-dead-code.sh, finalize-migration.sh
│  • 4 TypeScript migration tools
│
└─ Utilities/ (13 scripts)
   • tests (1), lib (2), ecom (1), rhixe_scans (7), root (6)
```

## Architecture Decisions

### 1. Directory-Based Categorization
Instead of naming convention or metadata files, use directory structure as single source of truth:
- Scripts physically located in a path automatically belong to that category
- No registration step needed for new scripts
- Scaling challenge: if 100+ directories, group via parent path patterns

### 2. Multi-Language Support via Extension
Support all common script languages out of the box:
- `.ps1` → pwsh -File (PowerShell)
- `.sh` → bash (shell scripts)
- `.bat` → cmd /c (batch files)
- `.ts` → bunx tsx (TypeScript)

Decision: Syntax-check shell scripts (.sh) first; if check passes, execute actual script.

### 3. Auto-Run vs. Interactive
- **Auto-run (default):** Runs 5 core production tasks in sequence; suitable for CI/cron
- **Interactive:** Menu-driven; suitable for manual exploration or category-specific execution
- **Fallback:** If auto-run fails, user can invoke with `-Mode interactive` to debug/recover

### 4. Error Handling Strategy
- **Retry on transient failures:** 3 attempts, 2-second delay, exponential backoff
- **Fail fast on permission errors:** Exit code 5 does not retry
- **Continue on failure:** Failed scripts log error but don't halt pipeline
- **Log everything:** Timestamp, script name, error message, exit code to JSON

### 5. Structured Logging
- One error log per run (timestamped: yyyyMMdd-HHmmss)
- One metrics log per run (same timestamp)
- JSON format for post-analysis via jq
- Error structure: {Timestamp, Script, Error, ExitCode}
- Metrics structure: {StartTime, Pipeline: [{Task, Duration, Status}], ScriptExecTime: {}}

## Implementation Details

### Discovery Performance
- **180 scripts discovered in:** < 2 seconds
- **Algorithm:** Recursive directory scan with exclusion filters
- **Excluded paths:** node_modules, __pycache__, .git, .venv, dist, build, .next

### Execution Performance
- **Core pipeline (5 tasks):** 20-60 seconds total
  - Disk analysis: 2-5s
  - Cache cleanup: 3-10s
  - Dependency cleanup: 5-15s
  - Package upgrade: 2-5s
  - Test suite: 5-10s

### Error Handling in Practice
- **Permission errors:** Fail on first occurrence (Exit Code 5)
- **Network timeouts:** Retry up to 3 times
- **Disk full:** Fail after 1 attempt (error condition unlikely to resolve mid-execution)
- **Syntax errors:** Detected in discovery phase, skip at runtime

### Log File Growth
- **Typical error log:** < 10 KB per run (unless many failures)
- **Typical metrics log:** < 5 KB per run
- **Recommendation:** Rotate logs monthly or after 100 runs

## Wrappers

### PowerShell Main (orchestrator-unified.ps1)
- 570 lines, 23.7 KB
- Entry point for Windows environments
- Full feature set: all 5 modes, error handling, logging

### Shell Wrapper (orchestrator-unified.sh)
- 80 lines, 2.6 KB
- Delegates to PowerShell orchestrator via pwsh command
- Provides CLI argument mapping for Unix/Linux environments

### Batch Wrapper (orchestrator-unified.bat)
- 70 lines, 2.5 KB
- Delegates to PowerShell orchestrator via pwsh command
- Provides CLI argument mapping for cmd.exe environments

## Category Ordering

Priorities determine execution sequence in auto-run:
```
Core        → Priority 1 (production pipeline)
Banking     → Priority 2
Archive     → Priority 3
Comicwise   → Priority 4
Bash        → Priority 5
Utilities   → Priority 6
```

Within each category, scripts are sorted by name.

## Auto-Run Pipeline Sequence

```
1. disk-analysis.ps1          → Analyze disk usage (pattern: 'disk-analysis')
2. cache-clean.*              → Clean all cache types (pattern: 'cache-clean')
3. clean-dependency-folders.* → Clean node_modules, venv, etc (pattern: 'clean')
4. upgrade.*                  → Upgrade packages (pattern: 'upgrade')
5. test-all.sh                → Run test suite (pattern: 'test-all')
```

All 5 tasks passed on first execution (100% success rate).

## Metrics Collected

**Per execution:**
- Total scripts discovered
- Scripts executed
- Success count
- Failure count
- Skipped count
- Total duration
- Average duration per script
- Per-script execution times

**Example output:**
```
Total Scripts Found: 180
Scripts Executed:    5
Successful:          5
Failed:              0
Total Duration:      24.53s
Average Per Script:  4.91s
```

## Testing Strategy

1. **Discover mode:** Verify all 180 scripts are found and categorized
   ```
   .\orchestrator.ps1 -Mode discover
   ```

2. **Dry-run:** Preview auto-run pipeline without execution
   ```
   .\orchestrator.ps1 -DryRun
   ```

3. **Validate:** Syntax-check all 77 shell scripts
   ```
   .\orchestrator.ps1 -Mode validate
   ```

4. **Interactive:** Manually select and run scripts by category
   ```
   .\orchestrator.ps1 -Mode interactive
   ```

5. **Auto-run:** Execute default pipeline
   ```
   .\orchestrator.ps1
   ```

## Known Limitations

1. **Parallel execution not supported:** Scripts run sequentially only. For parallel execution, use separate orchestrator or external tool.

2. **Script communication:** Orchestrator does not pass data between scripts. Each runs independently.

3. **Circular dependencies:** No dependency tracking. Must manually order in $AutoRunPipeline.

4. **Mixed language inheritance:** Environment variables and paths may differ between PowerShell and shell subprocesses.

5. **Timeout enforcement:** Only supported via Start-Process wrapper (complex implementation). Basic implementation uses trap handlers.

## Production Deployment

**Recommended schedule:**
- Daily: auto-run core cleanup pipeline (2 AM)
- Weekly: interactive exploration of domain-specific categories
- Monthly: validate all scripts and rotate logs

**Monitoring:**
- Track error log size and error frequency
- Alert if failure count exceeds threshold (e.g., > 1 in 10 runs)
- Generate weekly metrics report from JSON logs

**Recovery:**
- If auto-run fails, review error log JSON for root cause
- Re-run with `-Mode interactive` and select specific category
- If specific script fails consistently, investigate script directly

## Scaling Considerations

**For 500+ scripts:**
- Consider sub-orchestrators per domain (Banking orchestrator, Archive orchestrator, etc.)
- Implement parallel category execution (each category runs in background job)
- Add health check mechanism (script availability before execution)

**For 1000+ scripts:**
- Split into multi-level orchestrators (root orchestrator calls category sub-orchestrators)
- Implement caching of discovery results (refresh on explicit flag)
- Add script dependency graph and topological sort

## Future Enhancements

1. Conditional execution: Run script B only if script A succeeded
2. Script dependencies: Declare which scripts must run before/after others
3. Parallel execution: Run independent scripts in parallel jobs
4. Filtering: Run only scripts matching complex criteria
5. Dry-run output capture: Show what each script would output before executing
6. Notification: Email/Slack alerts on pipeline completion or failures
