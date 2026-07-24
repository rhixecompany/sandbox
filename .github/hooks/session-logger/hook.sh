#!/usr/bin/env bash
# session-logger hook — thin wrapper, delegates to async Python.
set -euo pipefail
HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd -W )"
HOOK_DIR=${HOOK_DIR//\\//}
if command -v python3 &>/dev/null; then
    exec python3 "$HOOK_DIR/hook.py"
elif command -v python &>/dev/null; then
    exec python "$HOOK_DIR/hook.py"
else
    echo "[ERROR] session-logger: python3/python not found on PATH" >&2
    exit 1
fi
