# Diagnostic Commands Quick Reference

Copy-paste commands for rapid troubleshooting. All paths use MSYS `/c/Users/Alexa` syntax.

## Memory & Disk

```bash
# Check all memory stores
wc -c /c/Users/Alexa/AppData/Local/hermes/memories/{MEMORY.md,USER.md}

# Check disk utilization
df -h /c/Users/Alexa

# Largest Hermes folders (watch for timeout on slow disks)
du -sh /c/Users/Alexa/AppData/Local/hermes/*

# Individual log sizes
ls -lhS /c/Users/Alexa/AppData/Local/hermes/logs/*.log | grep -v ".log\."
```

## MCP & Provider Status

```bash
# List enabled MCP servers
grep -E "^\s+[a-z-]+:\s*$" /c/Users/Alexa/AppData/Local/hermes/config.yaml | head -10

# Check primary model and provider
grep -E "^model:|^fallback" /c/Users/Alexa/AppData/Local/hermes/config.yaml | head -3

# Count recent errors in logs (last 50 lines)
tail -50 /c/Users/Alexa/AppData/Local/hermes/logs/errors.log | grep -E "(429|402|401|connection|failed)" | wc -l

# Stream errors in real-time
tail -f /c/Users/Alexa/AppData/Local/hermes/logs/errors.log | grep -E "ERROR|connection|unhealthy"
```

## Cleanup (User Approval Required)

```bash
# List files to delete (do NOT run; just inspect)
find /c/Users/Alexa/AppData/Local/hermes/logs -name "*.log.*" -type f

# List temp folder size
du -sh /c/Users/Alexa/AppData/Local/Temp

# After cleanup, verify
wc -c /c/Users/Alexa/AppData/Local/hermes/memories/MEMORY.md
df -h /c/Users/Alexa
```

## Git Checkpoint State

```bash
# Check checkpoint repo integrity
git -C /c/Users/Alexa/AppData/Local/hermes/checkpoints log --oneline | head -5

# If corrupted, report error details
git -C /c/Users/Alexa/AppData/Local/hermes/checkpoints gc --aggressive 2>&1 | tail -10
```

## Configuration Validation

```bash
# Verify config syntax (YAML)
python3 -c "import yaml; yaml.safe_load(open('/c/Users/Alexa/AppData/Local/hermes/config.yaml'))" && echo "✓ Valid"

# Check for common issues
grep -E "^\s+#|TODO|XXX|FIXME" /c/Users/Alexa/AppData/Local/hermes/config.yaml
grep "password\|secret\|token" /c/Users/Alexa/AppData/Local/hermes/config.yaml | wc -l
# (Should be 0 — no raw secrets in config)
```

## Session-Specific Diagnostic Log

To enable persistent diagnostic logging (runs every 5 min):

```bash
cat > /c/Users/Alexa/AppData/Local/hermes/scripts/health-check.sh << 'EOF'
#!/bin/bash
echo "=== Hermes Health Check: $(date) ===" >> /c/Users/Alexa/AppData/Local/hermes/logs/health.log
wc -c /c/Users/Alexa/AppData/Local/hermes/memories/MEMORY.md >> /c/Users/Alexa/AppData/Local/hermes/logs/health.log
df -h /c/Users/Alexa | tail -1 >> /c/Users/Alexa/AppData/Local/hermes/logs/health.log
tail -1 /c/Users/Alexa/AppData/Local/hermes/logs/errors.log >> /c/Users/Alexa/AppData/Local/hermes/logs/health.log
echo "" >> /c/Users/Alexa/AppData/Local/hermes/logs/health.log
EOF
chmod +x /c/Users/Alexa/AppData/Local/hermes/scripts/health-check.sh
```

Then schedule via cron: `hermes cron create "*/5 * * * *" /c/Users/Alexa/AppData/Local/hermes/scripts/health-check.sh`
