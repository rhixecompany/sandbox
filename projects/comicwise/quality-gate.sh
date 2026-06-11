#!/usr/bin/env bash
# ComicWise Quality Gate Runner (Bash)
# Runs lint:strict, triage, type-check, test, build — each logged to a report file.
# Usage: bash quality-gate.sh [--skip-type-check] [--skip-lint] [--skip-triage] [--skip-tests] [--skip-build] [--continue-on-error] [--json]
# Reports: lint-strict.txt, triage-report.txt, type-check.txt, test-report.txt, build-report.txt
# JSON:    quality-gate.json (with --json flag)

set -o pipefail

# ── Args ────────────────────────────────────────────────────────────────────
SKIP_TYPE_CHECK=false
SKIP_LINT=false
SKIP_TRIAGE=false
SKIP_TESTS=false
SKIP_BUILD=false
JSON_OUTPUT=false
CONTINUE_ON_ERROR=false
for arg in "$@"; do
  case "$arg" in
    --skip-type-check) SKIP_TYPE_CHECK=true ;;
    --skip-lint)       SKIP_LINT=true ;;
    --skip-triage)     SKIP_TRIAGE=true ;;
    --skip-tests)      SKIP_TESTS=true ;;
    --skip-build)      SKIP_BUILD=true ;;
    --json)            JSON_OUTPUT=true ;;
    --continue-on-error) CONTINUE_ON_ERROR=true ;;
  esac
done

# ── Colors ──────────────────────────────────────────────────────────────────
GREEN="\033[32m"
YELLOW="\033[33m"
RED="\033[31m"
BLUE="\033[34m"
GRAY="\033[90m"
BOLD="\033[1m"
RESET="\033[0m"

step()  { echo -e "\n${BOLD}${BLUE}[$1]${RESET} ${BOLD}$2${RESET}\n${GRAY}$(printf '%0.s-' {1..60})${RESET}"; }
ok()    { echo -e "  ${GREEN}✓${RESET} $1"; }
fail()  { echo -e "  ${RED}✗${RESET} $1"; }
warn()  { echo -e "  ${YELLOW}⚠${RESET} $1"; }
info()  { echo -e "  ${GRAY}$1${RESET}"; }

# Track results: "step|exit|errors|warnings|time|file"
RESULTS=()
GATE_START=$(date +%s)

run_gate() {
  local step_num="$1" label="$2" cmd="$3" outfile="$4"
  step "$step_num" "$label"
  info "→ $cmd"
  info "→ logging to $outfile (streaming with tee)"

  local start_ts
  start_ts=$(date +%s)

  # Create report header
  {
    echo "=== ComicWise Quality Gate: $label ==="
    echo "Date   : $(date '+%Y-%m-%d %H:%M:%S')"
    echo "Command: $cmd"
    printf '=%.0s' {1..60}; echo
    echo ""
  } | tee "$outfile" > /dev/null

  # Run the actual command through tee
  eval "$cmd" 2>&1 | tee -a "$outfile"
  local exit_code=${PIPESTATUS[0]}

  local end_ts
  end_ts=$(date +%s)
  local elapsed=$(( end_ts - start_ts ))
  local elapsed_fmt
  elapsed_fmt=$(printf "%02d:%02d" $((elapsed / 60)) $((elapsed % 60)))

  # Append timing info
  {
    echo ""
    printf '=%.0s' {1..60}; echo
    echo "Exit   : $exit_code"
    echo "Time   : $elapsed_fmt"
  } | tee -a "$outfile" > /dev/null

  # Count errors/warnings from output file
  local error_count warning_count
  error_count=$(grep -ioP '\berror\b' "$outfile" 2>/dev/null | wc -l)
  warning_count=$(grep -ioP '\bwarning\b' "$outfile" 2>/dev/null | wc -l)

  if [ "$exit_code" -eq 0 ]; then
    ok "$label passed (${elapsed_fmt})"
  else
    fail "$label failed (exit $exit_code) (${elapsed_fmt})"
  fi

  [ "$error_count" -gt 0 ]   && fail "$error_count error(s) detected"
  [ "$warning_count" -gt 0 ] && warn "$warning_count warning(s) detected"

  RESULTS+=("$label|$exit_code|$error_count|$warning_count|$elapsed_fmt|$outfile")
}

# ── Main ────────────────────────────────────────────────────────────────────
echo ""
echo -e "${BOLD}${BLUE}╔══════════════════════════════════════════════╗${RESET}"
echo -e "${BOLD}${BLUE}║       ComicWise Quality Gate Runner         ║${RESET}"
echo -e "${BOLD}${BLUE}╚══════════════════════════════════════════════╝${RESET}"
echo -e "${GRAY}Started: $(date '+%Y-%m-%d %H:%M:%S')${RESET}"

# Step 1: Lint Strict
if [ "$SKIP_LINT" = true ]; then
  step "1/5" "ESLint Strict (no auto-fix)"
  warn "Skipped (--skip-lint)"
  RESULTS+=("ESLint Strict|0|0|0|00:00|lint-strict.txt")
else
  run_gate "1/5" "ESLint Strict (no auto-fix)" "pnpm lint:strict" "lint-strict.txt"
  IFS='|' read -r label exit_code errors warnings elapsed file <<< "${RESULTS[-1]}"
  if [ "$exit_code" -ne 0 ] && [ "$CONTINUE_ON_ERROR" = false ]; then
    echo ""
    echo -e "${BOLD}${RED}✗ ESLint Strict failed — stopping here.${RESET}"
    echo -e "${YELLOW}  Review lint-strict.txt for details.${RESET}"
    echo ""
    exit 1
  fi
fi

# Step 2: Triage
if [ "$SKIP_TRIAGE" = true ]; then
  step "2/5" "Quality Gate Triage"
  warn "Skipped (--skip-triage)"
  RESULTS+=("Triage|0|0|0|00:00|triage-report.txt")
else
  run_gate "2/5" "Quality Gate Triage" "pnpm triage" "triage-report.txt"
  IFS='|' read -r label exit_code errors warnings elapsed file <<< "${RESULTS[-1]}"
  if [ "$exit_code" -ne 0 ] && [ "$CONTINUE_ON_ERROR" = false ]; then
    echo ""
    echo -e "${BOLD}${RED}✗ Triage failed — stopping here.${RESET}"
    echo -e "${YELLOW}  Review triage-report.txt for details.${RESET}"
    echo ""
    exit 1
  fi
fi

# Step 3: Type Check
if [ "$SKIP_TYPE_CHECK" = true ]; then
  step "3/5" "TypeScript Type Check"
  warn "Skipped (--skip-type-check)"
  RESULTS+=("TypeScript Type Check|0|0|0|00:00|type-check.txt")
else
  run_gate "3/5" "TypeScript Type Check" "pnpm type-check" "type-check.txt"
  IFS='|' read -r label exit_code errors warnings elapsed file <<< "${RESULTS[-1]}"
  if [ "$exit_code" -ne 0 ] && [ "$CONTINUE_ON_ERROR" = false ]; then
    echo ""
    echo -e "${BOLD}${RED}✗ Type Check failed — stopping here.${RESET}"
    echo -e "${YELLOW}  Review type-check.txt for details.${RESET}"
    echo ""
    exit 1
  fi
fi

# Step 4: Tests
if [ "$SKIP_TESTS" = true ]; then
  step "4/5" "Unit Tests"
  warn "Skipped (--skip-tests)"
  RESULTS+=("Unit Tests|0|0|0|00:00|test-report.txt")
else
  run_gate "4/5" "Vitest Unit Tests" "pnpm test --run" "test-report.txt"
  IFS='|' read -r label exit_code errors warnings elapsed file <<< "${RESULTS[-1]}"
  if [ "$exit_code" -ne 0 ] && [ "$CONTINUE_ON_ERROR" = false ]; then
    echo ""
    echo -e "${BOLD}${RED}✗ Tests failed — stopping here.${RESET}"
    echo -e "${YELLOW}  Review test-report.txt for details.${RESET}"
    echo ""
    exit 1
  fi
fi

# Step 5: Build
if [ "$SKIP_BUILD" = true ]; then
  step "5/5" "Production Build"
  warn "Skipped (--skip-build)"
  RESULTS+=("Build (debug)|0|0|0|00:00|build-report.txt")
else
  run_gate "5/5" "Production Build (debug)" "pnpm build:debug" "build-report.txt"
  IFS='|' read -r label exit_code errors warnings elapsed file <<< "${RESULTS[-1]}"
  if [ "$exit_code" -ne 0 ] && [ "$CONTINUE_ON_ERROR" = false ]; then
    echo ""
    echo -e "${BOLD}${RED}✗ Build failed — stopping here.${RESET}"
    echo -e "${YELLOW}  Review build-report.txt for details.${RESET}"
    echo ""
    exit 1
  fi
fi

# ── Summary ─────────────────────────────────────────────────────────────────
GATE_END=$(date +%s)
TOTAL_ELAPSED=$(( GATE_END - GATE_START ))
TOTAL_FMT=$(printf "%02d:%02d" $((TOTAL_ELAPSED / 60)) $((TOTAL_ELAPSED % 60)))

FAIL_COUNT=0
TOTAL_ERRORS=0
TOTAL_WARNINGS=0
FAILED_GATES=()
echo ""
echo -e "${BOLD}${BLUE}═══ Summary ═══════════════════════════════════${RESET}"
for entry in "${RESULTS[@]}"; do
  IFS='|' read -r label exit_code errors warnings elapsed file <<< "$entry"
  TOTAL_ERRORS=$((TOTAL_ERRORS + errors))
  TOTAL_WARNINGS=$((TOTAL_WARNINGS + warnings))
  if [ "$exit_code" -eq 0 ]; then
    icon="${GREEN}✓"
  else
    icon="${RED}✗"
    FAIL_COUNT=$((FAIL_COUNT + 1))
    FAILED_GATES+=("$label")
  fi
  # Compute timing percentage
  # Parse elapsed MM:SS into seconds
  elapsed_min=${elapsed%%:*}
  elapsed_sec=${elapsed##*:}
  gate_secs=$(( 10#$elapsed_min * 60 + 10#$elapsed_sec ))
  if [ "$TOTAL_ELAPSED" -gt 0 ]; then
    pct=$(( gate_secs * 100 / TOTAL_ELAPSED ))
  else
    pct=0
  fi
  printf "  %b %b %-20s %b%s (%2d%%)  → %s%b\n" "$icon" "$RESET" "$label" "$GRAY" "$elapsed" "$pct" "$file" "$RESET"
done
echo ""
echo -e "  ${GRAY}Total: $TOTAL_FMT | Errors: $TOTAL_ERRORS | Warnings: $TOTAL_WARNINGS${RESET}"
echo ""

# ── JSON Output ─────────────────────────────────────────────────────────────
if [ "$JSON_OUTPUT" = true ]; then
  JSON_FILE="quality-gate.json"
  PASSED=true
  [ "$FAIL_COUNT" -gt 0 ] && PASSED=false
  # Build failedGates JSON array
  FAILED_JSON="["
  for i in "${!FAILED_GATES[@]}"; do
    [ "$i" -gt 0 ] && FAILED_JSON+=", "
    FAILED_JSON+="\"${FAILED_GATES[$i]}\""
  done
  FAILED_JSON+="]"
  {
    echo '{'
    echo "  \"timestamp\": \"$(date '+%Y-%m-%dT%H:%M:%S')\","
    echo "  \"duration\": \"$TOTAL_FMT\","
    echo "  \"passed\": $PASSED,"
    echo "  \"totalErrors\": $TOTAL_ERRORS,"
    echo "  \"totalWarnings\": $TOTAL_WARNINGS,"
    echo "  \"failedGates\": $FAILED_JSON,"
    echo '  "gates": {'
    idx=0
    total=${#RESULTS[@]}
    for entry in "${RESULTS[@]}"; do
      IFS='|' read -r label exit_code errors warnings elapsed file <<< "$entry"
      idx=$((idx + 1))
      key=$(echo "$label" | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g')
      comma=","
      [ "$idx" -eq "$total" ] && comma=""
      echo "    \"$key\": { \"exitCode\": $exit_code, \"errors\": $errors, \"warnings\": $warnings, \"time\": \"$elapsed\", \"file\": \"$file\" }$comma"
    done
    echo '  }'
    echo '}'
  } > "$JSON_FILE"
  info "→ JSON written to $JSON_FILE"
fi

if [ "$FAIL_COUNT" -eq 0 ]; then
  echo -e "${BOLD}${GREEN}✓ All quality gates passed${RESET} ${GRAY}(total: $TOTAL_FMT)${RESET}"
  echo ""
  exit 0
else
  echo -e "${BOLD}${RED}✗ $FAIL_COUNT gate(s) failed${RESET} ${GRAY}(total: $TOTAL_FMT)${RESET}"
  echo -e "${YELLOW}  Review the .txt report files for details.${RESET}"
  echo ""
  exit 1
fi
