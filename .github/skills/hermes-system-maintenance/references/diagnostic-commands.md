# Diagnostic Commands Quick Reference

Copy-paste commands for rapid troubleshooting. All paths use MSYS `/c/Users/Alexa` syntax.

## Memory & Disk

```bash
# Check all memory stores
wc -c $LOCALAPPDATA/hermes/memories/{MEMORY.md,USER.md}

# Check disk utilization
df -h /c/Users/Alexa

# Largest Hermes folders (watch for timeout on slow disks)
du -sh $LOCALAPPDATA/hermes/*

# Individual log sizes
ls -lhS $LOCALAPPDATA/hermes/logs/*.log | grep -v ".log\."
```

## MCP & Provider Status

```bash
# List enabled MCP servers
grep -E "^\s+[a-z-]+:\s*$" $LOCALAPPDATA/hermes/config.yaml | head -10

# Check primary model and provider
grep -E "^model:|^fallback" $LOCALAPPDATA/hermes/config.yaml | head -3

# Count recent errors in logs (last 50 lines)
tail -50 $LOCALAPPDATA/hermes/logs/errors.log | grep -E "(429|402|401|connection|failed)" | wc -l

# Stream errors in real-time
tail -f $LOCALAPPDATA/hermes/logs/errors.log | grep -E "ERROR|connection|unhealthy"
```

## Cleanup (User Approval Required)

```bash
# List files to delete (do NOT run; just inspect)
find $LOCALAPPDATA/hermes/logs -name "*.log.*" -type f

# List temp folder size
du -sh /c/Users/Alexa/AppData/Local/Temp

# After cleanup, verify
wc -c $LOCALAPPDATA/hermes/memories/MEMORY.md
df -h /c/Users/Alexa
```

## Git Checkpoint State

```bash
# Check checkpoint repo integrity
git -C $LOCALAPPDATA/hermes/checkpoints log --oneline | head -5

# If corrupted, report error details
git -C $LOCALAPPDATA/hermes/checkpoints gc --aggressive 2>&1 | tail -10
```

## Configuration Validation

```bash
# Verify config syntax (YAML)
python3 -c "import yaml; yaml.safe_load(open('$LOCALAPPDATA/hermes/config.yaml'))" && echo "✓ Valid"

# Check for common issues
grep -E "^\s+#|TODO|XXX|FIXME" $LOCALAPPDATA/hermes/config.yaml
grep "password\|secret\|token" $LOCALAPPDATA/hermes/config.yaml | wc -l
# (Should be 0 — no raw secrets in config)
```

## Session-Specific Diagnostic Log

To enable persistent diagnostic logging (runs every 5 min):

```bash
cat > $LOCALAPPDATA/hermes/scripts/health-check.sh << 'EOF'
#!/bin/bash
echo "=== Hermes Health Check: $(date) ===" >> $LOCALAPPDATA/hermes/logs/health.log
wc -c $LOCALAPPDATA/hermes/memories/MEMORY.md >> $LOCALAPPDATA/hermes/logs/health.log
df -h /c/Users/Alexa | tail -1 >> $LOCALAPPDATA/hermes/logs/health.log
tail -1 $LOCALAPPDATA/hermes/logs/errors.log >> $LOCALAPPDATA/hermes/logs/health.log
echo "" >> $LOCALAPPDATA/hermes/logs/health.log
EOF
chmod +x $LOCALAPPDATA/hermes/scripts/health-check.sh
```

Then schedule via cron: `hermes cron create "*/5 * * * *" $HOME/AppData/Local/hermes/scripts/health-check.sh`