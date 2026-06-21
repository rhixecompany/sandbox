#!/usr/bin/env bash
set -euo pipefail

# Session Auto-Commit Hook - Regenerates SESSION_REPORT.md on session end
# Reads from session_logs/sessions.log, writes rolling 41-session summary
# Optionally git commits the report

# Source shared library
source "$(dirname "$0")/../lib.sh"

REPORT_PATH="${1:-${HOME}/Desktop/SandBox/SESSION_REPORT.md}"
LOG_DIR="${HOME}/AppData/Local/hermes/logs/sessions"
SESSION_LOG="${LOG_DIR}/sessions.log"
ensure_log_dir "$LOG_DIR"

# Build rolling summary (last 41 sessions) using portable reverse_lines
if [ -f "$SESSION_LOG" ]; then
    tail -n 500 "$SESSION_LOG" | reverse_lines | head -n 41 > /tmp/last_sessions.txt
else
    echo "No sessions logged yet" > /tmp/last_sessions.txt
fi

# Write concise report
{
    echo "# SESSION_REPORT"
    echo
    echo "Rolling 41-session summary (most recent first)."
    echo
    awk -F ' \\| ' '{print $1 " " $2 " | " $3 " | " $4 " | " $5}' /tmp/last_sessions.txt
} > "$REPORT_PATH"

# Write session_meta_latest.json for audit/verification
if [ -f "${LOG_DIR}/session_meta.json" ]; then
    cp "${LOG_DIR}/session_meta.json" "${LOG_DIR}/session_meta_latest.json"
fi

# Optionally git add/commit if in a repo and file changed
git_commit_if_changed "${HOME}/Desktop/SandBox" "SESSION_REPORT.md" "chore(session-report): update rolling 41-session summary"

exit 0