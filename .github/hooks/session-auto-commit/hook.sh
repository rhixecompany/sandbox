#!/usr/bin/env bash
# session-auto-commit hook — thin wrapper, delegates to async Python.
set -euo pipefail
# Resolve hook directory — handle MSYS2/Windows path translation
HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd )"
if command -v cygpath &>/dev/null; then
    HOOK_DIR=$(cygpath -w "$HOOK_DIR" 2>/dev/null || echo "$HOOK_DIR")
elif command -v pwd && pwd -W &>/dev/null; then
    HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd -W )"
fi
HOOK_DIR=${HOOK_DIR//\\//}
if command -v python3 &>/dev/null; then
    exec python3 "$HOOK_DIR/hook.py"
elif command -v python &>/dev/null; then
    exec python "$HOOK_DIR/hook.py"
else
    echo "[ERROR] session-auto-commit: python3/python not found on PATH" >&2
    exit 1
fi
