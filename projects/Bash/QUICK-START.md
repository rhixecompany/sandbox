# Quick Start Guide — Unified Orchestrator

## 30-Second Startup

### Default Auto-Run (Recommended)

```bash
# PowerShell
.\orchestrator-unified.ps1

# or Shell
./orchestrator-unified.sh

# or Batch
orchestrator-unified.bat
```

**What happens:**

- Discovers all 177 scripts
- Runs 5 core production tasks in sequence:
  1. Disk analysis
  2. Cache cleanup
  3. Dependency cleanup
  4. Package upgrade
  5. Test suite
- Generates JSON logs with metrics and errors
- Reports success/failure for each task

**Total time:** 20-60 seconds depending on system

---

## Interactive Mode (Manual Selection)

```bash
.\orchestrator-unified.ps1 -Mode interactive
```

**Menu flow:**

```
🎯 SELECT CATEGORY:
  1) Core: 64 scripts
  2) Banking: 34 scripts
  3) Archive: 51 scripts
  ...
  0) Exit

→ Choose category → Choose script → Execute → Continue or Exit
```

---

## Dry-Run Mode (Preview)

```bash
.\orchestrator-unified.ps1 -DryRun
```

**Shows what would run without actually executing.**

Useful for:

- Testing orchestrator logic
- Verifying script paths
- Checking permissions

---

## Filter by Category

Run only Banking scripts:

```bash
.\orchestrator-unified.ps1 -Category Banking -Mode interactive
```

Available categories:

- `Core` — Production pipeline
- `Banking` — Banking domain
- `Archive` — Git commit batches
- `Comicwise` — Media project
- `Bash` — Migration utilities
- `Utilities` — Tests, libs, misc

---

## View All Scripts

List all 177 scripts:

```bash
.\orchestrator-unified.ps1 -Mode discover
```

Exits after showing discovery summary.

---

## Validate Scripts

Syntax-check all shell scripts:

```bash
.\orchestrator-unified.ps1 -Mode validate
```

Reports syntax errors only (doesn't execute).

---

## Check Logs

After execution, inspect JSON logs:

```bash
# View error log
cat logs/errors-*.json | jq '.'

# View metrics log
cat logs/metrics-*.json | jq '.'

# Count errors
cat logs/errors-*.json | jq '.Errors | length'

# See execution times
cat logs/metrics-*.json | jq '.ScriptExecTime'
```

---

## Example Output

```
╔══════════════════════════════════════════════════════════════════════════════╗
║ 🎼 UNIFIED SCRIPT ORCHESTRATOR - Sandbox/Bash (177 Scripts)                 ║
╚══════════════════════════════════════════════════════════════════════════════╝

🔍 Discovering scripts...

📊 Discovery Summary:
  • Core: 64 scripts
  • Banking: 34 scripts
  • Archive: 51 scripts
  • Comicwise: 10 scripts
  • Bash: 7 scripts
  • Utilities: 18 scripts
  ─────────────────────
  TOTAL: 177 scripts

📋 Mode: auto
🔧 DryRun: False

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

════════════════════════════════════════════════════════════════════════════════
📊 EXECUTION REPORT
════════════════════════════════════════════════════════════════════════════════

📈 Statistics:
  Total Scripts Found: 177
  Scripts Executed:    5
  Successful:          5
  Failed:              0
  Skipped:             0

⏱️  Timing:
  Total Duration:      24.53s
  Average Per Script:  4.91s

📁 Log Files:
  Errors:  errors-20260527-143022.json
  Metrics: metrics-20260527-143022.json
════════════════════════════════════════════════════════════════════════════════
```

---

## Troubleshooting

### "PowerShell not found"

Install or update PowerShell 7+:

```bash
# Windows (via Chocolatey)
choco install powershell-core

# Or download from https://github.com/PowerShell/PowerShell/releases
```

### "Bash not found (for .sh scripts)"

Install Git Bash or use WSL.

### Scripts don't execute

Check execution policy:

```powershell
Get-ExecutionPolicy
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope CurrentUser
```

### Permission denied

Make shell scripts executable:

```bash
chmod +x orchestrator-unified.sh *.sh
```

---

## Common Tasks

### Cleanup disk (cache + dependencies)

```bash
.\orchestrator-unified.ps1 -Mode auto
```

### Run all Banking scripts

```bash
.\orchestrator-unified.ps1 -Category Banking -Mode interactive
```

### Check disk usage

```bash
.\orchestrator-unified.ps1 -Category Core -ScriptFilter disk-analysis
```

### Run tests only

```bash
.\orchestrator-unified.ps1 -Category Utilities
```

### Schedule daily auto-run (Windows Task Scheduler)

```batch
REM Create task
schtasks /create /tn "Daily Orchestrator" /tr "pwsh -File C:\path\to\orchestrator-unified.ps1" /sc daily /st 02:00
```

### Schedule daily auto-run (Linux Cron)

```bash
0 2 * * * /path/to/orchestrator-unified.sh -m auto >> /var/log/orchestrator.log 2>&1
```

---

## Features at a Glance

| Feature | Command |
| --- | --- |
| **Auto-run core pipeline** | `.\orchestrator-unified.ps1` |
| **Interactive menu** | `.\orchestrator-unified.ps1 -Mode interactive` |
| **Filter by category** | `.\orchestrator-unified.ps1 -Category Banking` |
| **Dry-run preview** | `.\orchestrator-unified.ps1 -DryRun` |
| **List all scripts** | `.\orchestrator-unified.ps1 -Mode discover` |
| **Validate syntax** | `.\orchestrator-unified.ps1 -Mode validate` |
| **Custom log path** | `.\orchestrator-unified.ps1 -LogPath C:\logs` |
| **Shell wrapper** | `./orchestrator-unified.sh -m auto` |
| **Batch wrapper** | `orchestrator-unified.bat -m auto` |

---

## Performance Baseline

Typical execution times (auto-run):

- **Disk Analysis**: 2-5 seconds
- **Cache Cleanup**: 3-10 seconds
- **Dependency Cleanup**: 5-15 seconds
- **Package Upgrade**: 2-5 seconds
- **Test Suite**: 5-10 seconds
- **Total**: 20-60 seconds

---

## Next Steps

1. **Run it:** `.\orchestrator-unified.ps1`
2. **Check logs:** `cat logs/*.json`
3. **Try interactive:** `.\orchestrator-unified.ps1 -Mode interactive`
4. **Read full docs:** See `ORCHESTRATOR-README.md`

---

**Status:** ✓ Production Ready  
**Scripts:** 177 total (64 Core + 95 Domain + 18 Utilities)  
**Last Updated:** 2026-05-27
