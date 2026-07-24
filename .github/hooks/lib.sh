#!/usr/bin/env bash
# Shared library for Hermes hooks

# Colors for logging
readonly RED='\033[0;31m'
readonly GREEN='\033[0;32m'
readonly YELLOW='\033[1;33m'
readonly BLUE='\033[0;34m'
readonly NC='\033[0m' # No Color

log_debug() {
    echo -e "${BLUE}[DEBUG]${NC} $*" >&2
}

log_info() {
    echo -e "${GREEN}[INFO]${NC} $*" >&2
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $*" >&2
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $*" >&2
}

# Read JSON value safely
json_get() {
    local json="$1"
    local key="$2"
    local default="${3:-}"
    
    echo "$json" | jq -r "${key} // \"${default}\"" 2>/dev/null || echo "${default}"
}

# Ensure directory exists
ensure_dir() {
    mkdir -p "$1"
}

# Write JSONL line to file
write_jsonl() {
    local file="$1"
    local json="$2"
    
    ensure_dir "$(dirname "$file")"
    echo "$json" >> "$file"
}