#!/usr/bin/env bash
# shellcheck shell=bash
# ==============================================================================
# Cross-Reference Check — Parallel Script Drift Detection
# Version: 1.0.0
# Description: Compares parallel script implementations (sh/ps1/bat) for drift.
#
# Usage:
#   ./phase-6-cross-ref.sh              Report only
#   ./phase-6-cross-ref.sh --fix        Auto-align version strings
#   ./phase-6-cross-ref.sh --json       JSON output for CI
# ==============================================================================
set -euo pipefail

FIX=0
JSON=0
EXIT=0

for a in "$@"; do case "$a" in --fix) FIX=1;; --json) JSON=1;; esac; done

GREEN='\033[0;32m'; YELLOW='\033[1;33m'; NC='\033[0m'

ok()   { [ $JSON -eq 0 ] && printf "  ${GREEN}OK${NC}   %s\n" "$1"; }
warn() { [ $JSON -eq 0 ] && printf "  ${YELLOW}WARN${NC} %s\n" "$1"; }

# ── Script Pairs ────────────────────────────────────────────────────────────
PAIRS=(
  "Bash/clean_dependency_folders.sh Bash/clean-dependency-folders.ps1 Bash/clean-dependency-folders.bat"
  "Bash/cache-clean.sh Bash/cache-clean.ps1 Bash/cache-clean.bat"
  "Bash/git-commit-batches.sh Bash/git-commit-batches.ps1"
  "Bash/upgrade.sh Bash/upgrade.ps1 Bash/upgrade.bat"
  "Bash/scripts/phase-2-light-inventory.sh Bash/scripts/phase-2-light-inventory.ps1"
  "Rhixe-company/comicwise/quality-gate.sh Rhixe-company/comicwise/quality-gate.ps1"
)

# ── Check functions ──────────────────────────────────────────────────────────

shebang_ok() {
  local f=$1 ext=${1##*.}
  [ "$ext" = "bat" ] && return 0
  local want; [ "$ext" = "sh" ] && want="#!/usr/bin/env bash" || want="#!/usr/bin/env pwsh"
  [ "$(head -1 "$f" 2>/dev/null)" = "$want" ]
}

flags_ok() {
  local f=$1 ext=${1##*.}
  [ "$ext" = "bat" ] && return 0
  [ "$ext" = "sh" ]  && grep -q 'set -euo pipefail' "$f" 2>/dev/null && return 0
  [ "$ext" = "ps1" ] && grep -qi 'ErrorActionPreference.*Stop' "$f" 2>/dev/null && return 0
  return 1
}

shellcheck_ok() {
  [ "${1##*.}" != "sh" ] && return 0
  grep -q 'shellcheck shell=bash' "$1" 2>/dev/null
}

getver() { grep -oP 'Version:\s*\K[\d]+\.[\d]+\.[\d]+' "$1" 2>/dev/null | head -1; }

# ── Analyze one pair (space-separated file paths) ──────────────────────────

analyze() {
  local pair="$1" issues="" versions=""

  for f in $pair; do
    [ ! -f "$f" ] && { issues="$issues|missing:$(basename $f)"; continue; }
    shebang_ok "$f"    || issues="$issues|wrong_shebang:$(basename $f)"
    flags_ok "$f"      || issues="$issues|missing_flags:$(basename $f)"
    shellcheck_ok "$f" || issues="$issues|no_shellcheck:$(basename $f)"
    local v=$(getver "$f")
    versions="$versions $f=$v"
  done

  # Check version drift
  local unique=$(for x in $versions; do echo "${x#*=}"; done | grep -v '^$' | sort -u | wc -l)
  if [ "$unique" -gt 1 ]; then
    issues="$issues|version_drift: $versions"
    [ "$FIX" = "1" ] && align_versions "$pair" "$versions"
  fi

  [ -z "$issues" ] && ok "$(echo "$pair" | tr ' ' ' ↔ ')" && return

  EXIT=1
  local disp; disp=$(echo "$pair" | tr ' ' ' ↔ ')
  if [ "$JSON" = "1" ]; then
    echo '{"pair":"'"$disp"'","issues":"'"$(echo "$issues" | sed 's/^|//')"'"}'
  else
    warn "$disp"
    IFS='|' read -ra il <<< "$issues"
    for i in "${il[@]}"; do [ -n "$i" ] && warn "  └─ $i"; done
  fi
}

align_versions() {
  local pair="$1" versions="$2" max=""
  for x in $versions; do
    local v="${x#*=}"; [ -z "$v" ] && continue
    if [ -z "$max" ] || [ "$(printf '%s\n' "$v" "$max" | sort -V | tail -1)" != "$max" ]; then
      max="$v"
    fi
  done
  [ -z "$max" ] && return
  for f in $pair; do
    [ ! -f "$f" ] && continue
    sed -i "s/Version: [0-9]\+\.[0-9]\+\.[0-9]\+/Version: $max/g" "$f"
    ok "Aligned $(basename $f) version -> $max"
  done
}

# ── Batch pairs ─────────────────────────────────────────────────────────────
for n in $(seq 1 26); do
  s="Bash/scripts/skills-commit-batch-${n}.sh"
  p="Bash/scripts/skills-commit-batch-${n}.ps1"
  [ -f "$s" ] && [ -f "$p" ] && PAIRS+=("$s $p")
done

# ── Main ─────────────────────────────────────────────────────────────────────
[ "$JSON" = "1" ] && echo '{ "drifted_pairs": ['

first=1
for chk in "${PAIRS[@]}"; do
  analyze "$chk"
done

[ "$JSON" = "1" ] && echo '], "exit_code": '$EXIT' }'

if [ $EXIT -eq 0 ]; then
  [ "$JSON" = "0" ] && printf "\n${GREEN}All parallel scripts are in sync.${NC}\n"
else
  [ "$JSON" = "0" ] && printf "\n${YELLOW}Drift detected. Run --fix to auto-align versions.${NC}\n"
fi

exit $EXIT
