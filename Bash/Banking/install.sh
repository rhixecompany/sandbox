# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash
#
# OpenAgents Control Installer
# Interactive installer for OpenCode agents, commands, tools, and plugins
#
# Compatible with:
# - macOS (bash 3.2+)
# - Linux (bash 3.2+)
# - Windows (Git Bash, WSL)
#############################################################################

set -euo pipefail

# Safe defaults for environment variables that may not be set
: "${WT_SESSION:=}"
: "${ConEmuPID:=}"
: "${REGISTRY_URL:=}"
: "${OPENCODE_BRANCH:=main}"
: "${OPENCODE_INSTALL_DIR:=.opencode}"

# Determine script directory for sourcing modules
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Source all module files in order
source "$SCRIPT_DIR/install/lib/00-config.sh"
source "$SCRIPT_DIR/install/lib/01-utils.sh"
source "$SCRIPT_DIR/install/lib/02-paths.sh"
source "$SCRIPT_DIR/install/lib/03-deps.sh"
source "$SCRIPT_DIR/install/lib/04-registry.sh"
source "$SCRIPT_DIR/install/lib/05-selection.sh"
source "$SCRIPT_DIR/install/lib/06-modes.sh"
source "$SCRIPT_DIR/install/lib/07-preview.sh"
source "$SCRIPT_DIR/install/lib/08-install.sh"

# Cleanup temp directory on exit (success or failure)
trap 'rm -rf "$TEMP_DIR" 2>/dev/null || true' EXIT INT TERM

# Second trap for cleanup_and_exit
trap 'cleanup_and_exit 1' INT TERM

#############################################################################
# Main
#############################################################################

main() {
    # Parse command line arguments
    while [ $# -gt 0 ]; do
        case "$1" in
            --install-dir=*)
                CUSTOM_INSTALL_DIR="${1#*=}"
                # Basic validation - check not empty
                if [ -z "$CUSTOM_INSTALL_DIR" ]; then
                    echo "Error: --install-dir requires a non-empty path"
                    exit 1
                fi
                shift
                ;;
            --install-dir)
                if [ -n "$2" ] && [ "${2:0:1}" != "-" ]; then
                    CUSTOM_INSTALL_DIR="$2"
                    shift 2
                else
                    echo "Error: --install-dir requires a path argument"
                    exit 1
                fi
                ;;
            essential|--essential)
                INSTALL_MODE="profile"
                PROFILE="essential"
                NON_INTERACTIVE=true
                shift
                ;;
            developer|--developer)
                INSTALL_MODE="profile"
                PROFILE="developer"
                NON_INTERACTIVE=true
                shift
                ;;
            business|--business)
                INSTALL_MODE="profile"
                PROFILE="business"
                NON_INTERACTIVE=true
                shift
                ;;
            full|--full)
                INSTALL_MODE="profile"
                PROFILE="full"
                NON_INTERACTIVE=true
                shift
                ;;
            advanced|--advanced)
                INSTALL_MODE="profile"
                PROFILE="advanced"
                NON_INTERACTIVE=true
                shift
                ;;
            list|--list)
                check_dependencies
                fetch_registry
                list_components
                cleanup_and_exit 0
                ;;
            --help|-h|help)
                print_header
                echo "Usage: $0 [PROFILE] [OPTIONS]"
                echo ""
                echo -e "${BOLD}Profiles:${NC}"
                echo "  essential, --essential    Minimal setup with core agents"
                echo "  developer, --developer    Code-focused development tools"
                echo "  business, --business      Content and business-focused tools"
                echo "  full, --full              Everything except system-builder"
                echo "  advanced, --advanced      Complete system with all components"
                echo ""
                echo -e "${BOLD}Options:${NC}"
                echo "  --install-dir PATH        Custom installation directory"
                echo "                            (default: .opencode)"
                echo "  list, --list              List all available components"
                echo "  help, --help, -h          Show this help message"
                echo ""
                echo -e "${BOLD}Environment Variables:${NC}"
                echo "  OPENCODE_INSTALL_DIR      Installation directory"
                echo "  OPENCODE_BRANCH           Git branch to install from (default: main)"
                echo ""
                echo -e "${BOLD}Examples:${NC}"
                echo ""
                echo -e "  ${CYAN}# Interactive mode (choose location and components)${NC}"
                echo "  $0"
                echo ""
                echo -e "  ${CYAN}# Quick install with default location (.opencode/)${NC}"
                echo "  $0 developer"
                echo ""
                echo -e "  ${CYAN}# Install to global location (Linux/macOS)${NC}"
                echo "  $0 developer --install-dir ~/.config/opencode"
                echo ""
                echo -e "  ${CYAN}# Install to global location (Windows Git Bash)${NC}"
                echo "  $0 developer --install-dir ~/.config/opencode"
                echo ""
                echo -e "  ${CYAN}# Install to custom location${NC}"
                echo "  $0 essential --install-dir ~/my-agents"
                echo ""
                echo -e "  ${CYAN}# Using environment variable${NC}"
                echo "  export OPENCODE_INSTALL_DIR=~/.config/opencode"
                echo "  $0 developer"
                echo ""
                echo -e "  ${CYAN}# Install from URL (non-interactive)${NC}"
                echo "  curl -fsSL https://raw.githubusercontent.com/darrenhinde/OpenAgentsControl/main/install.sh | bash -s developer"
                echo ""
                echo -e "${BOLD}Platform Support:${NC}"
                echo "  ✓ Linux (bash 3.2+)"
                echo "  ✓ macOS (bash 3.2+)"
                echo "  ✓ Windows (Git Bash, WSL)"
                echo ""
                exit 0
                ;;
            *)
                echo "Unknown option: $1"
                echo "Run '$0 --help' for usage information"
                exit 1
                ;;
        esac
    done

    # Apply custom install directory if specified (CLI arg overrides env var)
    if [ -n "$CUSTOM_INSTALL_DIR" ]; then
        local normalized_path
        if normalize_and_validate_path "$CUSTOM_INSTALL_DIR" > /dev/null; then
            normalized_path=$(normalize_and_validate_path "$CUSTOM_INSTALL_DIR")
            INSTALL_DIR="$normalized_path"
            if ! validate_install_path "$INSTALL_DIR"; then
                print_warning "Installation path may have issues, but continuing..."
            fi
        else
            print_error "Invalid installation directory: $CUSTOM_INSTALL_DIR"
            exit 1
        fi
    fi

    check_bash_version
    check_dependencies
    fetch_registry

    if [ -n "$PROFILE" ]; then
        # Non-interactive mode (compatible with bash 3.2+)
        SELECTED_COMPONENTS=()
        local temp_file="$TEMP_DIR/components.tmp"
        get_profile_components "$PROFILE" > "$temp_file"
        while IFS= read -r component; do
            [ -n "$component" ] && SELECTED_COMPONENTS+=("$component")
        done < "$temp_file"

        expand_selected_components

        # Resolve dependencies for profile installs
        print_step "Resolving dependencies..."
        local original_count=${#SELECTED_COMPONENTS[@]}
        for comp in "${SELECTED_COMPONENTS[@]}"; do
            resolve_dependencies "$comp"
        done

        local new_count=${#SELECTED_COMPONENTS[@]}
        if [ "$new_count" -gt "$original_count" ]; then
            local added=$((new_count - original_count))
            print_info "Added $added dependencies"
        fi

        show_installation_preview
    else
        # Interactive mode - show location menu first
        show_install_location_menu
        show_main_menu

        if [ "$INSTALL_MODE" = "profile" ]; then
            show_profile_menu
        elif [ "$INSTALL_MODE" = "custom" ]; then
            show_custom_menu
        fi
    fi
}

main "$@"
