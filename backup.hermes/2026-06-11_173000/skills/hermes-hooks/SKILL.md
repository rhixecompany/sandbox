---
name: hermes-hooks
description: Hook creation, events, built-in hooks, and common automation patterns
version: 1.0.0
platforms: [macos, linux, windows]
metadata:
  hermes:
    tags: [hermes, hooks, automation]
    category: hooks
    requires_toolsets: [terminal, file, skills]
    config:
      - key: hermes.skill.hooks.enabled
        description: "Enable hooks skill"
        default: "true"
---

# Hermes Hooks Skill

## When to Use
- Creating custom event-driven automation
- Understanding built-in hooks (session-logger, session-auto-commit, governance-audit)
- Implementing audit trails, cost tracking, security scanning

## Procedure
1. **Built-in Hooks** (config.yaml):
   ```yaml
   hooks:
     session-logger:
       enabled: true
       events: [sessionStart, sessionEnd, userPromptSubmitted]
       script: "C:\\Users\\Alexa\\AppData\\Local\\hermes\\hooks\\session-logger\\hook.sh"
     
     session-auto-commit:
       enabled: true
       events: [sessionEnd]
       script: "C:\\Users\\Alexa\\AppData\\Local\\hermes\\hooks\\session-auto-commit\\hook.sh"
     
     governance-audit:
       enabled: true
       events: [sessionStart, sessionEnd, userPromptSubmitted]
       script: "C:\\Users\\Alexa\\AppData\\Local\\hermes\\hooks\\governance-audit\\hook.sh"
   ```

2. **Hook Script Rules**:
   - Always use `jq -c` for compact JSON output
   - Use `awk "BEGIN {exit !($a > $b)}"` for float comparison (never `bc` + `(( ))`)
   - Always support a SKIP flag (e.g., `SKIP_LOGGING=true`)
   - Use absolute paths in `hooks.json`
   - Log to `logs/hermes/`, never `logs/copilot/`

3. **Event Payloads**:
   ```json
   // sessionStart
   {"event": "sessionStart", "session_id": "abc123", "profile": "default", "timestamp": "2026-01-15T10:30:00Z", "cwd": "/home/user/project"}
   
   // sessionEnd
   {"event": "sessionEnd", "session_id": "abc123", "profile": "default", "timestamp": "2026-01-15T11:45:00Z", "duration_seconds": 4500, "message_count": 42, "tool_calls": 18}
   
   // userPromptSubmitted
   {"event": "userPromptSubmitted", "session_id": "abc123", "profile": "default", "timestamp": "2026-01-15T10:35:00Z", "prompt": "Help me debug", "toolsets": ["web", "terminal", "file"]}
   ```

4. **Create Custom Hook**:
   ```bash
   mkdir -p ~/.hermes/hooks/my-hook
   # Write hook.sh (see template below)
   chmod +x ~/.hermes/hooks/my-hook/hook.sh
   # Register in config.yaml
   ```

5. **Hook Template**:
   ```bash
   #!/usr/bin/env bash
   set -euo pipefail
   input=$(cat)
   skip_var="SKIP_MY_HOOK"
   [[ "${!skip_var:-}" == "true" ]] && echo '{"status": "skipped"}' && exit 0
   event=$(echo "$input" | jq -r '.event')
   case "$event" in
     sessionStart) echo '{"status": "ok"}' ;;
     userPromptSubmitted) prompt=$(echo "$input" | jq -r '.prompt'); echo '{"status": "ok"}' ;;
     *) echo '{"status": "ignored"}' ;;
   esac
   ```

## Common Patterns
1. **Audit Trail** — Log all prompts/responses for compliance
2. **Auto-Formatting** — Run formatters on file changes at session end
3. **Cost Tracking** — Accumulate token usage per session/project
4. **Security Scanning** — Inspect prompts for secrets, PII, injection attempts
5. **Notification Bridge** — Send session summaries to Slack, Discord, email

## Pitfalls
- **Hook not firing** → Check `config.yaml` events list; verify script path
- **Script fails silently** → Check `~/.hermes/logs/hermes/` for stderr
- **JSON parse error** → Ensure script outputs valid JSON; use `jq -c`
- **Skip flag not working** → Verify env var name matches `SKIP_<HOOK_NAME>` pattern
- **Permission denied** → `chmod +x ~/.hermes/hooks/<name>/hook.sh`

## Verification
- Start session, send prompt, end session
- Check `~/.hermes/logs/hermes/session-*.log`
- Verify auto-commit creates git commits on session end
- Verify governance audit detects threat patterns

## References
- `references/commands.md` — CLI commands
- `references/hook-template.md` — Complete hook.sh template
- `references/event-payloads.md` — All event JSON schemas