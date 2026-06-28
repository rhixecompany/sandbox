#!/usr/bin/env bash
# Cross-platform hook runner for Hermes
# Polyglot: works as bash script; Windows users should use run-hook.cmd instead
# Usage: run-hook.sh <hook-name> <event> [args...]

set -euo pipefail

HOOK_DIR="$(cd "$(dirname "$0")" && pwd)"
HOOK_NAME="${1:-}"
EVENT="${2:-}"

if [ -z "$HOOK_NAME" ] || [ -z "$EVENT" ]; then
    echo "Usage: $0 <hook-name> <event> [args...]" >&2
    echo "Available hooks: governance-audit, session-logger, session-auto-commit" >&2
    exit 1
fi

HOOK_SCRIPT="${HOOK_DIR}/${HOOK_NAME}/hook.sh"

if [ ! -x "$HOOK_SCRIPT" ]; then
    echo "Hook not found or not executable: $HOOK_SCRIPT" >&2
    exit 1
fi

# Read stdin and pass to hook with event as first argument
exec "$HOOK_SCRIPT" "$EVENT"