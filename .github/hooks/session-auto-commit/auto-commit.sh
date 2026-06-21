#!/usr/bin/env bash
set -euo pipefail

# Legacy entry point - delegates to hook.sh
exec "$(dirname "$0")/hook.sh" "$@"