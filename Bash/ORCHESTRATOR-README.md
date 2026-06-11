# Unified Script Orchestrator

Consolidates all 177 Sandbox/Bash scripts into a single, intelligent orchestrator with auto-run capability, interactive selection, error handling, and structured logging.

## Overview

```
UNIFIED ORCHESTRATOR (orchestrator-unified.ps1)
├─ Core (64 scripts) — Production pipeline
│  ├─ src/ (15 TS implementations)
│  ├─ scripts/ (27 orchestration + 9 libraries)
│  └─ root/ (22 production wrappers + utilities)
│
├─ Banking (34 scripts) — Domain-specific
├─ Archive (51 scripts) — Git commit batches
├─ Comicwise (10 scripts) — Media project
├─ Bash (7 scripts) — Migration utilities
└─ Utilities (18 scripts) — Tests, libs, misc
```

## Features

✓ **Auto-Run Pipeline** — Default mode runs core production tasks in sequence  
✓ **Interactive Mode** — Menu-driven category and script selection  
✓ **Error Handling** — Retry logic, timeout protection, comprehensive error logging  
✓ **Structured Logging** — JSON error logs + execution metrics  
✓ **Dry-Run Mode** — Preview operations before execution  
✓ **Real-Time Progress** — Visual indicators, timing, metrics collection  
✓ **Multi-Language Support** — PowerShell, Shell, Batch, TypeScript  
✓ **Metrics Collection** — Execution times, success rates, performance data

## Usage

### Quick Start (Auto-Run)

```bash
# PowerShell
.\orchestrator-unified.ps1

# Shell
./orchestrator-unified.sh

# Batch
orchestrator-unified.bat
```

Runs default core production pipeline:

1. Disk Analysis
2. Cache Cleanup
3. Dependency Cleanup
4. Package Upgrade
5. Test Suite

### Interactive Mode

```bash
.\orchestrator-unified.ps1 -Mode interactive
```

Menu-driven interface:

- Select category (Core, Banking, Comicwise, etc.)
- Select individual script
- Execute with feedback
- Loop or exit

### Dry-Run (Preview)

```bash
.\orchestrator-unified.ps1 -DryRun
```

Preview operations without actual execution.

### Specific Category

```bash
.\orchestrator-unified.ps1 -Category Banking
```

Run all scripts in a specific category.

### Discover Mode

```bash
.\orchestrator-unified.ps1 -Mode discover
```

List all 177 scripts organized by category and exit.

### Validate Mode

```bash
.\orchestrator-unified.ps1 -Mode validate
```

Syntax-check all shell scripts.

## Command-Line Reference

### PowerShell

```powershell
.\orchestrator-unified.ps1 [options]

OPTIONS:
  -Mode <string>              auto | interactive | discover | validate (default: auto)
  -Category <string>          Filter to specific category
  -ScriptFilter <string>      Pattern to match scripts (e.g., 'cache-clean')
  -DryRun                     Preview without execution
  -LogPath <string>           Custom log directory (default: ./logs)
  -Verbose                    Show verbose output
```

### Shell

```bash
./orchestrator-unified.sh [options]

OPTIONS:
  -m, --mode MODE             auto | interactive | discover | validate
  -c, --category CATEGORY     Category filter
  -d, --dry-run              Preview without execution
  -l, --log-path PATH         Custom log directory
  --help                     Show help
```

### Batch

```cmd
orchestrator-unified.bat [options]

OPTIONS:
  -m, --mode MODE             auto | interactive | discover | validate
  -c, --category CATEGORY     Category filter
  -d, --dry-run              Preview without execution
  -l, --log-path PATH         Custom log directory
  --help                     Show help
```

## Examples

### Auto-Run Production Pipeline

```bash
# Run default core scripts
.\orchestrator-unified.ps1
```

Output:

```
▶️  AUTO-RUN PIPELINE
Running core production scripts in sequence...

── Analyze disk usage ──
  [1/5] Running: disk-analysis.ps1
    ✓ Success

── Clean caches ──
  [2/5] Running: cache-clean.sh
    ✓ Success

── Clean dependencies ──
  [3/5] Running: clean_dependency_folders.sh
    ✓ Success

── Upgrade packages ──
  [4/5] Running: upgrade.ps1
    ✓ Success

── Run test suite ──
  [5/5] Running: test-all.sh
    ✓ Success

📊 EXECUTION REPORT
═══════════════════════════════════════════════════════════════════════════════
📈 Statistics:
  Total Scripts Found:  177
  Scripts Executed:     5
  Successful:           5
  Failed:               0
  Skipped:              0

⏱️  Timing:
  Total Duration:       24.53s
  Average Per Script:   4.91s

📁 Log Files:
  Errors:  errors-20260527-143022.json
  Metrics: metrics-20260527-143022.json
═══════════════════════════════════════════════════════════════════════════════
```

### Interactive Category Selection

```bash
.\orchestrator-unified.ps1 -Mode interactive
```

Output:

```
🎯 SELECT CATEGORY:
  1) Core: 64 scripts
  2) Banking: 34 scripts
  3) Archive: 51 scripts
  4) Comicwise: 10 scripts
  5) Bash: 7 scripts
  6) Utilities: 18 scripts
  7) All
  0) Exit

Enter choice: 2

🎯 SELECT SCRIPT from Banking:
  1) install.sh
  2) install-agents.sh
  3) aggressive-capture.ps1
  4) verify-agents.ps1
  ...
  0) Back

Enter choice: 3
```

### Dry-Run Mode

```bash
.\orchestrator-unified.ps1 -Mode auto -DryRun
```

Output:

```
▶️  AUTO-RUN PIPELINE
Running core production scripts in sequence...

── Analyze disk usage ──
  [1/5] Running: disk-analysis.ps1
    [DRY-RUN] Would execute: C:\...\disk-analysis.ps1

── Clean caches ──
  [2/5] Running: cache-clean.sh
    [DRY-RUN] Would execute: C:\...\cache-clean.sh

... (continues with all tasks)
```

### Banking Category Only

```bash
.\orchestrator-unified.ps1 -Category Banking
```

Discover and run all 34 Banking scripts (interactive selection).

### Validation Check

```bash
.\orchestrator-unified.ps1 -Mode validate
```

Syntax-checks all 77 shell scripts and reports errors.

## Logging

### Directory Structure

```
logs/
├─ errors-20260527-143022.json          # Error log with details
└─ metrics-20260527-143022.json         # Execution metrics
```

### Error Log Format

```json
{
  "Errors": [
    {
      "Timestamp": "2026-05-27T14:30:35.5678901Z",
      "Script": "cache-clean.sh",
      "Error": "Command execution failed: disk full",
      "ExitCode": 1
    }
  ],
  "StartTime": "2026-05-27T14:30:22.1234567Z"
}
```

### Metrics Log Format

```json
{
  "Pipeline": [
    {
      "Task": "disk-analysis",
      "Duration": 2.35,
      "Status": "success"
    },
    {
      "Task": "cache-clean",
      "Duration": 5.12,
      "Status": "success"
    }
  ],
  "ScriptExecTime": {
    "disk-analysis.ps1": 2.35,
    "cache-clean.sh": 5.12,
    "clean-dep.ts": 3.78
  },
  "StartTime": "2026-05-27T14:30:22.1234567Z"
}
```

## Category Details

### Core (64 scripts) — Production Pipeline

- **src/** (15 TypeScript): Upgrade, cache-clean, clean-dep, git-batches, dry-run engine, AST transformers
- **scripts/** (27): Multi-phase orchestration (discovery, cloning, triage, debug, remediation, cross-ref) + 9 shared libraries
- **root/** (22): Production wrappers + disk-analysis + utilities

**Auto-Run Sequence:**

1. Disk Analysis (disk-analysis.ps1)
2. Cache Cleanup (cache-clean.\*)
3. Dependency Cleanup (clean_dependency_folders.\*)
4. Package Upgrade (upgrade.\*)
5. Test Suite (test-all.sh)

### Banking (34 scripts)

- Installation framework (11 scripts + libs)
- Operational scripts: Verification, diagnostics, MCP integration, plugin management
- Orchestration and planning

### Archive (51 scripts)

- Git commit batch operations (25 numbered pairs: skills-commit-batch-1 through 26)
- Each pair: PowerShell implementation + shell wrapper
- Deployable as pre-generated commit operations

### Comicwise (10 scripts)

- Development environment setup (setup-dev)
- Development server (dev)
- Project cleanup
- VS Code extension installation
- Quality gate checks

### Bash (7 scripts)

- Script migration tools (migrate-script.sh, mark-dead-code.sh, finalize-migration.sh)
- TypeScript migration utilities (AST transformer, behavior testing, dry-run engine, script runner)

### Utilities (18 scripts)

- **tests/** (1): verify-dryrun.sh
- **lib/** (2): log-rotate (PS + shell)
- **ecom/** (1): install.sh
- **rhixe_scans/** (7): Infrastructure setup (docker, git, browser installers, prod config)
- **root/** (6): Config files (.prettierrc.ts, .lintstagedrc.ts, types.d.ts), analyzers, runtime commands

## Error Handling

### Retry Logic

- Default: 3 automatic retries on failure
- Configurable: `MaxRetries` in script config
- Exponential backoff: 2-second delay between retries

### Timeout Protection

- Default: 300 seconds per script
- Configurable: `TimeoutSeconds` in script config
- Prevents hanging on long-running operations

### Error Recovery

- Failed scripts don't stop pipeline (continue to next)
- All errors logged with timestamp and details
- Exit code indicates overall success/failure
- Metrics available for post-mortem analysis

## Exit Codes

| Code | Meaning                            |
| ---- | ---------------------------------- |
| 0    | Success — all tasks completed      |
| 1    | Failure — one or more tasks failed |
| 2    | Invalid arguments or configuration |

## Performance Metrics

Collected during execution:

- **Total Scripts Found**: Count of all 177 scripts
- **Scripts Executed**: Number run in this session
- **Success/Failure Counts**: Pass/fail breakdown
- **Execution Times**: Per-script duration
- **Average Duration**: Mean execution time
- **Total Duration**: End-to-end elapsed time

Example:

```
📈 Statistics:
  Total Scripts Found: 177
  Scripts Executed:    5
  Successful:          5
  Failed:              0
  Skipped:             0

⏱️  Timing:
  Total Duration:      24.53s
  Average Per Script:  4.91s
```

## Troubleshooting

### PowerShell Execution Policy

If scripts don't run, enable execution:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
```

### Missing Dependencies

Ensure these are available:

- **PowerShell 7+** (pwsh)
- **Bash** (for shell scripts)
- **Bun/Bunx** (for TypeScript execution)
- **Node.js/npm** (for JavaScript execution)

### Script Failures

Check error logs:

```bash
cat logs/errors-*.json | jq '.Errors[] | {Script, Error}'
```

### Permission Issues

Ensure scripts are executable:

```bash
chmod +x orchestrator-unified.sh
chmod +x *.sh
```

## Integration

### Cron/Scheduled Tasks

Windows Task Scheduler:

```batch
powershell -NoProfile -ExecutionPolicy Bypass -File "C:\path\to\orchestrator-unified.ps1"
```

Linux Cron:

```bash
0 2 * * * /path/to/orchestrator-unified.sh -m auto
```

### CI/CD Pipeline

GitHub Actions:

```yaml
- name: Run Orchestrator
  run: |
    pwsh -NoProfile -ExecutionPolicy Bypass `
      -File orchestrator-unified.ps1 -Mode auto
```

## Development

### Adding New Scripts

1. Place script in appropriate directory
2. Orchestrator auto-discovers on next run
3. Categorization based on directory path

### Extending Categories

Edit `$Script:Categories` in orchestrator-unified.ps1:

```powershell
$Script:Categories['NewCategory'] = @{
    Description = 'Description'
    Paths       = @('path/to/scripts')
    Priority    = 7
    Scripts     = @()
}
```

### Custom Auto-Run Pipeline

Edit `$Script:AutoRunPipeline`:

```powershell
$Script:AutoRunPipeline = @(
    @{ Category = 'Core'; Pattern = 'custom'; Description = 'Custom task' }
)
```

## Status

✓ **Production Ready**

- All 177 scripts integrated
- Error handling implemented
- Logging functional
- Metrics collection active
- Interactive mode tested
- Auto-run pipeline verified

## License

Sandbox/Bash Project

## Contact

Author: Alexa  
Date: 2026-05-27  
Status: Unified Orchestrator Complete
