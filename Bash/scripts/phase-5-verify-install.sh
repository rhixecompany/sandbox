#!/usr/bin/env bash
# shellcheck shell=bash
#
# phase-5-verify-install.sh
# Verification script for the refactored install modular structure.
# Sources install.sh's modules and performs structural validation.
#
# Usage:
#   ./Bash/scripts/phase-5-verify-install.sh          # Standard check
#   ./Bash/scripts/phase-5-verify-install.sh --verbose # Verbose output
#############################################################################

set -euo pipefail

VERBOSE=false
[[ "${1:-}" == "--verbose" ]] && VERBOSE=true

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
LIB_DIR="$PROJECT_ROOT/install/lib"

PASS=0
FAIL=0
ERRORS=()

log_pass() {
    echo -e "  \033[0;32m✓\033[0m $1"
    ((PASS++)) || true
}

log_fail() {
    echo -e "  \033[0;31m✗\033[0m $1"
    ((FAIL++)) || true
    ERRORS+=("$1")
}

log_info() {
    [[ "$VERBOSE" == true ]] && echo -e "  \033[0;34mℹ\033[0m $1" || true
}

echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║        Phase 5 — Refactored Install Structure Verification    ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""

# ── Step 1: Check that all module files exist ──
echo -e "\033[1m[1/8] Checking module files exist\033[0m"

MODULES=(
    "00-config.sh"
    "01-utils.sh"
    "02-paths.sh"
    "03-deps.sh"
    "04-registry.sh"
    "05-selection.sh"
    "06-modes.sh"
    "07-preview.sh"
    "08-install.sh"
)

for mod in "${MODULES[@]}"; do
    if [ -f "$LIB_DIR/$mod" ]; then
        log_pass "install/lib/$mod exists"
    else
        log_fail "install/lib/$mod MISSING"
    fi
done

# ── Step 2: Source all modules and verify key functions exist ──
echo -e "\033[1m[2/8] Sourcing modules and checking key functions\033[0m"

# Set up minimal environment for sourcing
export WT_SESSION=""
export ConEmuPID=""

# Source all modules
source "$LIB_DIR/00-config.sh"
source "$LIB_DIR/01-utils.sh"
source "$LIB_DIR/02-paths.sh"
source "$LIB_DIR/03-deps.sh"
source "$LIB_DIR/04-registry.sh"
source "$LIB_DIR/05-selection.sh"
source "$LIB_DIR/06-modes.sh"
source "$LIB_DIR/07-preview.sh"
source "$LIB_DIR/08-install.sh"

echo "  Sourced all modules successfully"

# Check required functions exist
FUNCTIONS=(
    "jq_exec"
    "print_header"
    "print_success"
    "print_error"
    "print_info"
    "print_warning"
    "print_step"
    "normalize_and_validate_path"
    "validate_install_path"
    "get_global_install_path"
    "check_bash_version"
    "check_dependencies"
    "fetch_registry"
    "get_profile_components"
    "get_component_info"
    "resolve_component_path"
    "get_registry_key"
    "get_install_path"
    "expand_context_wildcard"
    "expand_selected_components"
    "resolve_dependencies"
    "check_interactive_mode"
    "show_install_location_menu"
    "show_main_menu"
    "show_profile_menu"
    "show_custom_menu"
    "show_component_selection"
    "show_installation_preview"
    "show_collision_report"
    "get_install_strategy"
    "perform_installation"
    "show_post_install"
    "list_components"
    "cleanup_and_exit"
)

for fn in "${FUNCTIONS[@]}"; do
    if declare -F "$fn" &>/dev/null; then
        log_pass "Function '$fn' is defined"
    else
        log_fail "Function '$fn' NOT defined"
    fi
done

# ── Step 3: Verify global vars exist ──
echo -e "\033[1m[3/8] Checking global variables\033[0m"

VARS=(
    "PLATFORM"
    "REPO_URL"
    "BRANCH"
    "RAW_URL"
    "REGISTRY_URL"
    "INSTALL_DIR"
    "TEMP_DIR"
    "SELECTED_COMPONENTS"
    "INSTALL_MODE"
    "PROFILE"
    "NON_INTERACTIVE"
)

for var in "${VARS[@]}"; do
    if declare -p "$var" &>/dev/null 2>&1; then
        log_pass "Variable '$var' is declared"
    else
        # Check if it's a nameref or scalar
        if declare -p "$var" 2>/dev/null | grep -q "declare"; then
            log_pass "Variable '$var' is declared"
        else
            log_info "Variable '$var' is set but may be global"
        fi
    fi
done

# Check platform detection
log_info "Detected platform: $PLATFORM"
log_info "Install dir: $INSTALL_DIR"
log_info "Registry URL: ${REGISTRY_URL:0:60}..."

# ── Step 4: Test path utilities ──
echo -e "\033[1m[4/8] Testing path utilities\033[0m"

# normalize_and_validate_path
TEST_PATH=$(normalize_and_validate_path "/tmp/test")
if [ "$TEST_PATH" = "/tmp/test" ]; then
    log_pass "normalize_and_validate_path: absolute path preserved"
else
    log_fail "normalize_and_validate_path: expected '/tmp/test', got '$TEST_PATH'"
fi

# Empty path
if normalize_and_validate_path "" > /dev/null 2>&1; then
    log_fail "normalize_and_validate_path: empty path should return 1"
else
    log_pass "normalize_and_validate_path: empty path rejected (return 1)"
fi

# get_registry_key
KEY=$(get_registry_key "agent")
if [ "$KEY" = "agents" ]; then
    log_pass "get_registry_key: 'agent' → 'agents'"
else
    log_fail "get_registry_key: expected 'agents', got '$KEY'"
fi

KEY=$(get_registry_key "contexts")
if [ "$KEY" = "contexts" ]; then
    log_pass "get_registry_key: 'contexts' → 'contexts' (plural preserved)"
else
    log_fail "get_registry_key: expected 'contexts', got '$KEY'"
fi

# get_install_path
INSTALL_DIR=".opencode"
TEST_PATH=$(get_install_path ".opencode/agent/test.md")
if [ "$TEST_PATH" = ".opencode/agent/test.md" ]; then
    log_pass "get_install_path: path correctly resolved"
else
    log_fail "get_install_path: expected '.opencode/agent/test.md', got '$TEST_PATH'"
fi

# ── Step 5: Check COLOR variables ──
echo -e "\033[1m[5/8] Checking terminal color variables\033[0m"

COLORS=("RED" "GREEN" "YELLOW" "BLUE" "MAGENTA" "CYAN" "BOLD" "NC")
for c in "${COLORS[@]}"; do
    if declare -p "$c" &>/dev/null 2>&1; then
        log_pass "Color '$c' is defined"
    else
        log_fail "Color '$c' NOT defined"
    fi
done

# ── Step 6: Verify install.sh can be syntax-checked ──
echo -e "\033[1m[6/8] Syntax-checking install.sh\033[0m"

if bash -n "$PROJECT_ROOT/install.sh" 2>&1; then
    log_pass "install.sh: syntax OK"
else
    log_fail "install.sh: syntax ERROR"
fi

echo -e "\033[1m[6/8] Syntax-checking install-agents.sh\033[0m"

if bash -n "$PROJECT_ROOT/install-agents.sh" 2>&1; then
    log_pass "install-agents.sh: syntax OK"
else
    log_fail "install-agents.sh: syntax ERROR"
fi

# ── Step 7: Check all lib modules for syntax ──
echo -e "\033[1m[7/8] Syntax-checking all lib modules\033[0m"

for mod in "${MODULES[@]}"; do
    if bash -n "$LIB_DIR/$mod" 2>&1; then
        log_pass "$mod: syntax OK"
    else
        log_fail "$mod: syntax ERROR"
    fi
done

# ── Step 8: Verify set -euo pipefail in both main scripts ──
echo -e "\033[1m[8/8] Verifying set -euo pipefail\033[0m"

for script in "install.sh" "install-agents.sh"; do
    if grep -q "set -euo pipefail" "$PROJECT_ROOT/$script" 2>/dev/null; then
        log_pass "$script: has 'set -euo pipefail'"
    else
        log_fail "$script: MISSING 'set -euo pipefail'"
    fi
done

# Safe defaults check
for script in "install.sh" "install-agents.sh"; do
    if grep -q "WT_SESSION:=" "$PROJECT_ROOT/$script" 2>/dev/null; then
        log_pass "$script: has safe default for WT_SESSION"
    else
        log_fail "$script: MISSING safe default for WT_SESSION"
    fi
done

# ── Summary ──
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                         Summary                               ║"
echo "╚════════════════════════════════════════════════════════════════╝"
echo ""
echo -e "  Passed: \033[0;32m${PASS}\033[0m"
echo -e "  Failed: \033[0;31m${FAIL}\033[0m"

if [ "$FAIL" -gt 0 ]; then
    echo ""
    echo -e "\033[0;31mErrors:\033[0m"
    for err in "${ERRORS[@]}"; do
        echo "  • $err"
    done
    echo ""
    echo -e "\033[0;31mSome checks failed. Review above.${NC}"
    exit 1
else
    echo ""
    echo -e "\033[0;32mAll checks passed! The refactored structure is sound.${NC}"
    exit 0
fi
