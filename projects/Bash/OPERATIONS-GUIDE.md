# Sandbox/Bash Scripts — Ongoing Operations Guide

**Version**: 1.0 | **Status**: Active | **Updated**: 2026-05-27

---

## Daily Operations Checklist

### Morning Check (< 5 minutes)

```bash
cd ~/Desktop/Sandbox/Bash

# 1. Verify all scripts still work
bash test-all.sh
# Expected: 15/15 PASS

# 2. Check logs for errors
ls -lt logs/ | head -5
# Look for recent log files (should be fresh)

# 3. Quick disk analysis
pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 2'
# Takes ~5 seconds, shows disk usage trends
```

---

## Weekly Operations

### Cache Cleanup (Every Monday)

```bash
# 1. Check what would be cleaned (dry-run)
bash cache-clean.sh --all --dry-run
# Review the output

# 2. If approved, run actual cleanup (requires admin)
# Open PowerShell as Administrator, then:
pwsh
cd C:\Users\Alexa\Desktop\Sandbox\Bash
bash cache-clean.sh --all
# Takes ~2-5 minutes depending on cache sizes
```

### Dependency Cleanup (Monthly)

```bash
# 1. Find what would be deleted
bash clean_dependency_folders.sh --max-depth 2 --dry-run
# Shows node_modules, venv, etc. that take up space

# 2. Review results
# If approved, run cleanup:
bash clean_dependency_folders.sh --max-depth 2 --auto
# Takes ~10 seconds to 1 minute
```

### Disk Space Review (Weekly)

```bash
# Comprehensive analysis
pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 3'

# Shows:
# - Top 10 largest dependency folders
# - Breakdown by category (Node.js, Python, etc.)
# - Available disk space
# - Trends over time (compare with previous weeks)
```

---

## Troubleshooting Guide

### "Script hangs on execution"

**Diagnosis**:

```bash
# Add timeout to see where it gets stuck
timeout 30 bash cache-clean.sh --help 2>&1
# If it completes, script is fine
# If timeout, there's a hang
```

**Solution**:

- Check logs: `cat logs/*.log | tail -50`
- Run with debug: `bash cache-clean.sh --help --debug`
- Check available disk space: `df -h`
- Restart terminal and try again

---

### "Permission denied" on scripts

**Diagnosis**:

```bash
ls -la *.sh *.ps1 *.bat
# Look for x permission on .sh files
```

**Solution**:

```bash
chmod +x *.sh src/*.ts
# Make all shell scripts executable
```

---

### "bunx: command not found"

**Diagnosis**:

```bash
which bun
which bunx
# Check if Bun is in PATH
```

**Solution**:

```bash
# Install Bun if missing
curl -fsSL https://bun.sh/install | bash

# Add to PATH if needed
export PATH="$HOME/.bun/bin:$PATH"
```

---

### "PowerShell not found" (on Linux)

**Diagnosis**:

```bash
which pwsh
```

**Solution**:

- This is Windows-only project
- Scripts are designed for Windows 10/11
- On Linux: use bash scripts only (\*.sh)

---

### "Cache cleaner shows 'Not running as administrator'"

**Diagnosis**:

```bash
# This is a warning, not an error
# Some cache operations require admin
```

**Solution**:

```bash
# Option 1: Run as administrator
# Right-click CMD/PowerShell → Run as administrator
# Then run the script

# Option 2: Just skip admin-only operations
# Script will clean what it can (non-admin caches)
```

---

## Scheduled Execution

### Windows Task Scheduler Setup

#### Schedule: Daily Cache Check (7 AM)

```
Name: Daily Cache Check
Program: C:\Windows\System32\bash.exe
Arguments: -c "cd C:\Users\Alexa\Desktop\Sandbox\Bash && bash cache-clean.sh --all --dry-run > logs/daily-check.log 2>&1"
Trigger: Daily at 7:00 AM
Run with highest privileges: No (or Yes if you want actual cleanup)
```

#### Schedule: Weekly Disk Analysis (Sunday 8 AM)

```
Name: Weekly Disk Analysis
Program: C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe
Arguments: -NoProfile -Command ". C:\Users\Alexa\Desktop\Sandbox\Bash\disk-analysis.ps1 -MaxDepth 3 | Out-File -FilePath C:\Users\Alexa\Desktop\Sandbox\Bash\logs\weekly-analysis.log"
Trigger: Weekly on Sunday at 8:00 AM
Run with highest privileges: No
```

#### Schedule: Monthly Cleanup (1st of Month, 10 PM)

```
Name: Monthly Dependency Cleanup
Program: C:\Windows\System32\bash.exe
Arguments: -c "cd C:\Users\Alexa\Desktop\Sandbox\Bash && bash clean_dependency_folders.sh --max-depth 2 --auto"
Trigger: Monthly on 1st at 10:00 PM
Run with highest privileges: Yes (requires admin for cleanup)
```

---

## Log File Management

### Viewing Logs

```bash
# View most recent log
tail -20 logs/*.log | less

# View specific script logs
ls logs/cache-clean*.log
ls logs/upgrade*.log

# View all logs by date
ls -lt logs/ | head -10
```

### Log Rotation (Automatic)

Scripts automatically:

- Create timestamped log files
- Keep last 10 logs per script
- Delete older logs automatically

**Example**:

```
logs/
  cache-clean_20260527_210521.log      # Most recent
  cache-clean_20260520_180302.log
  cache-clean_20260513_190115.log
  ...
  cache-clean_20260315_120000.log      # 10 logs kept
  # Older logs deleted automatically
```

### Manual Log Cleanup

```bash
# Delete all logs
rm logs/*.log

# Delete logs older than 30 days
find logs -name "*.log" -mtime +30 -delete

# Archive logs before cleanup
tar czf logs-backup-$(date +%Y%m%d).tar.gz logs/
rm logs/*.log
```

---

## Performance Tuning

### Slow Scans?

```bash
# Reduce scan depth (faster)
bash clean_dependency_folders.sh --max-depth 2 --dry-run
# Default is 4, reduce to 2 for speed

# Specific paths only (faster)
bash clean_dependency_folders.sh --paths ~/Desktop --dry-run
# Instead of scanning entire system
```

### Memory Issues?

```bash
# Run with smaller caches
bash cache-clean.sh --caches npm,docker --auto
# Instead of --all (14 cache types)
```

### Long Execution Times?

```bash
# Check what's running
ls -la logs/*.log | head -1 | awk '{print $NF}'
tail -f logs/$(ls -t logs/*.log | head -1 | xargs basename)
# Follow the most recent log in real-time
```

---

## Maintenance Tasks

### Monthly Review

1. **Check logs for errors**

   ```bash
   grep -i error logs/*.log
   # Should return nothing normally
   ```

2. **Review disk trends**

   ```bash
   # Compare weekly analysis reports
   diff logs/weekly-analysis.log logs/weekly-analysis-prev.log
   # Look for growing categories
   ```

3. **Update script versions** (if needed)
   ```bash
   git status
   git pull origin main
   # Keep scripts up-to-date
   ```

### Quarterly Review

1. **Test all scripts end-to-end**

   ```bash
   bash test-all.sh
   bash upgrade.sh --help
   bash cache-clean.sh --help
   pwsh -NoProfile -Command '. ./disk-analysis.ps1'
   ```

2. **Check documentation**
   - Read README.md
   - Review SPECS.md for any changes
   - Update USAGE-REPORT.md if needed

3. **Performance assessment**
   - Average execution time
   - Log file sizes
   - Disk space recovered

---

## Integration Patterns

### Call from Another Script

```bash
#!/bin/bash
# My script that uses cache-clean.sh

cd ~/Desktop/Sandbox/Bash

# Run cleanup in dry-run mode
bash cache-clean.sh --all --dry-run > /tmp/cleanup-preview.log

# Check result
if [ $? -eq 0 ]; then
    echo "Cleanup preview OK"
    # Maybe proceed with actual cleanup
    bash cache-clean.sh --all --auto
else
    echo "Cleanup preview failed"
    exit 1
fi
```

### Call from PowerShell

```powershell
# My PowerShell script that uses disk-analysis.ps1

Push-Location C:\Users\Alexa\Desktop\Sandbox\Bash

# Run analysis
. ./disk-analysis.ps1 -MaxDepth 2 -OutputFile "C:\Reports\disk-report.txt"

# Check if successful
if ($LASTEXITCODE -eq 0) {
    Send-Email -Subject "Disk Analysis Complete" -Body "See attached report"
}

Pop-Location
```

### CI/CD Integration

```yaml
# GitHub Actions example
jobs:
  maintenance:
    runs-on: windows-latest
    steps:
      - uses: actions/checkout@v3

      - name: Run disk analysis
        run: |
          cd ~/Desktop/Sandbox/Bash
          pwsh -NoProfile -Command '. ./disk-analysis.ps1'

      - name: Upload report
        uses: actions/upload-artifact@v3
        with:
          name: disk-report
          path: logs/analysis-*.log
```

---

## Backup & Recovery

### Backup Scripts

```bash
# Create backup of entire Bash directory
tar czf ~/backup-sandbox-bash-$(date +%Y%m%d).tar.gz \
    ~/Desktop/Sandbox/Bash

# Keep last 4 weeks of backups
find ~ -name "backup-sandbox-bash-*.tar.gz" -mtime +28 -delete
```

### Recovery from Backup

```bash
# List available backups
ls -lt ~/backup-sandbox-bash-*.tar.gz

# Restore from backup
cd ~/
tar xzf backup-sandbox-bash-20260520.tar.gz
# Overwrites with backed-up version
```

---

## Common Workflows

### Weekly Maintenance Run (15 minutes)

```bash
#!/bin/bash
# Weekly maintenance script

cd ~/Desktop/Sandbox/Bash

echo "=== Starting weekly maintenance ==="

# 1. Test all scripts (1 min)
bash test-all.sh

# 2. Analyze disk (2 min)
pwsh -NoProfile -Command '. ./disk-analysis.ps1 -MaxDepth 2' | tee logs/weekly-disk.log

# 3. Check for errors (1 min)
echo "=== Checking logs for errors ==="
grep -i error logs/*.log | tail -5 || echo "No errors found"

# 4. Show disk cleanup opportunities (5 min)
echo "=== Potential cleanup ==="
bash clean_dependency_folders.sh --max-depth 2 --dry-run | grep "Found"

echo "=== Weekly maintenance complete ==="
```

### Quarterly Deep Cleanup (1 hour)

```bash
#!/bin/bash
# Quarterly deep cleanup (run as administrator)

cd ~/Desktop/Sandbox/Bash

echo "=== Starting quarterly cleanup ==="

# 1. Back up current state
echo "Creating backup..."
tar czf ~/backup-pre-cleanup-$(date +%Y%m%d).tar.gz ~/Desktop/Sandbox/Bash

# 2. Disk analysis before
echo "Analyzing disk before cleanup..."
pwsh -NoProfile -Command '. ./disk-analysis.ps1' | tee logs/before-cleanup.log

# 3. Clean caches
echo "Cleaning caches..."
bash cache-clean.sh --all --auto

# 4. Clean dependencies
echo "Cleaning dependencies..."
bash clean_dependency_folders.sh --max-depth 3 --auto

# 5. Disk analysis after
echo "Analyzing disk after cleanup..."
pwsh -NoProfile -Command '. ./disk-analysis.ps1' | tee logs/after-cleanup.log

# 6. Show results
echo "=== Cleanup complete ==="
echo "See logs/before-cleanup.log and logs/after-cleanup.log for comparison"
```

---

## Support & Help

### Getting Help

```bash
# Show script help
bash upgrade.sh --help
bash cache-clean.sh --help
pwsh -NoProfile -Command '. ./disk-analysis.ps1 -Help'

# View documentation
cat README.md          # Quick start guide
cat SPECS.md           # Technical details
cat PLAN.md            # Implementation plan
cat USAGE-REPORT.md    # Real-world examples
```

### Reporting Issues

When reporting a problem:

1. **Include the error message**:

   ```bash
   bash cache-clean.sh --all 2>&1 | tee error-report.log
   # Attach error-report.log
   ```

2. **Include the log file**:

   ```bash
   cat logs/*.log
   # Show last 20 lines
   ```

3. **Include system info**:
   ```bash
   uname -a
   bun --version
   pwsh -NoProfile -Command '$PSVersionTable.PSVersion'
   ```

---

## Version Control

### Track Changes

```bash
# See what changed
git status
git diff

# Commit fixes
git add -A
git commit -m "fix: cache-clean timeout issue"

# View history
git log --oneline | head -10
```

### Update from Repository

```bash
# Check for updates
git fetch origin

# Update to latest
git pull origin main

# Verify still working
bash test-all.sh
```

---

## Quick Reference

| Task | Command | Time |
| --- | --- | --- |
| Show help | `bash *.sh --help` | < 1s |
| Dry-run cleanup | `bash cache-clean.sh --all --dry-run` | 3s |
| Actual cleanup | `bash cache-clean.sh --all --auto` | 2-5m |
| Disk analysis | `pwsh -NoProfile -Command '. ./disk-analysis.ps1'` | 5s |
| Run all tests | `bash test-all.sh` | 30s |
| View recent logs | `tail -20 logs/*.log` | < 1s |

---

## Emergency Procedures

### Script Not Responding (Stuck)

```bash
# 1. Stop the process
Ctrl+C

# 2. Check what went wrong
tail -50 logs/*.log | grep -A 5 ERROR

# 3. Retry with timeout
timeout 60 bash cache-clean.sh --help

# 4. If still stuck, check system
# Windows Task Manager → Check CPU/Memory
# Restart if necessary
```

### Out of Disk Space

```bash
# 1. Check how much free
df -h
# or in PowerShell: Get-Volume

# 2. Find largest dependency folders
bash clean_dependency_folders.sh --dry-run

# 3. Clean immediately (requires admin)
bash clean_dependency_folders.sh --auto

# 4. Clean caches
bash cache-clean.sh --all --auto
```

### Corrupt Log Files

```bash
# Logs are just text, can be deleted
rm logs/*.log

# Scripts will create new logs on next run
bash test-all.sh
# New logs created automatically
```

---

## Glossary

- **Dry-run**: Preview mode, shows what would happen without making changes
- **Auto**: Skip confirmations, proceed automatically
- **Debug**: Verbose output, shows detailed information
- **Max-depth**: Maximum folder recursion depth (1=current, 2=1 level deep, etc.)
- **Log rotation**: Automatically delete old logs, keep recent ones
- **Exit code**: Script result (0=success, 1=failure, 2=usage error)
- **Cache**: Temporary files that can be safely deleted
- **Dependency folder**: node_modules, venv, target/, etc. that can be regenerated

---

## Summary

- ✓ **Scripts are production-ready**
- ✓ **Run daily maintenance checks**
- ✓ **Review logs weekly**
- ✓ **Deep cleanup quarterly**
- ✓ **Keep backups monthly**
- ✓ **Update from repo periodically**

---

**Created**: 2026-05-27 | **Owner**: Alexa | **Status**: Active
