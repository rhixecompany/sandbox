# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash
# Log rotation utility — call after writing logs
# Usage: rotate_logs <log_dir> [max_logs=10]
rotate_logs() {
    local log_dir="$1" max_logs="${2:-10}"
    if [[ -d "$log_dir" ]]; then
        while [[ $(find "$log_dir" -name '*.log' 2>/dev/null | wc -l) -gt $max_logs ]]; do
            find "$log_dir" -name '*.log' -printf '%T@ %p\n' 2>/dev/null | sort -n | head -1 | cut -d' ' -f2- | xargs rm -f 2>/dev/null || true
        done
    fi
}
