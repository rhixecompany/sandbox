# Hook Commands Reference

## Built-in Hooks Configuration
```yaml
hooks:
  session-logger:
    enabled: true
    events: [sessionStart, sessionEnd, userPromptSubmitted]
    script: "~/.hermes/hooks/session-logger/hook.sh"
  
  session-auto-commit:
    enabled: true
    events: [sessionEnd]
    script: "~/.hermes/hooks/session-auto-commit/hook.sh"
  
  governance-audit:
    enabled: true
    events: [sessionStart, sessionEnd, userPromptSubmitted]
    script: "~/.hermes/hooks/governance-audit/hook.sh"
```

## Hook Management
```bash
# Create hook directory
mkdir -p ~/.hermes/hooks/my-hook

# Write hook.sh and make executable
chmod +x ~/.hermes/hooks/my-hook/hook.sh

# Test locally
echo '{"event":"sessionStart","session_id":"test","profile":"default","timestamp":"2026-01-15T10:30:00Z","cwd":"/home/user/project"}' | ~/.hermes/hooks/my-hook/hook.sh

# View hook logs
cat ~/.hermes/logs/hermes/my-hook.log
```

## Skip Flags
```bash
SKIP_LOGGING=true
SKIP_AUTO_COMMIT=true
SKIP_GOVERNANCE_AUDIT=true
```

## Hook Script Rules
1. Use `jq -c` for compact JSON output
2. Use `awk "BEGIN {exit !($a > $b)}"` for float comparison
3. Always support SKIP flag
4. Use absolute paths
5. Log to `logs/hermes/`