#!/usr/bin/env bash
# shellcheck shell=bash
#
# 07-preview.sh - Installation preview, collision report, and strategy selection
#############################################################################

show_installation_preview() {
    # Only clear screen in interactive mode
    if [ "$NON_INTERACTIVE" != true ]; then
        clear
    fi
    print_header

    echo -e "${BOLD}Installation Preview${NC}\n"

    if [ -n "$PROFILE" ]; then
        echo -e "Profile: ${GREEN}${PROFILE}${NC}"
    else
        echo -e "Mode: ${GREEN}Custom${NC}"
    fi

    echo -e "Installation directory: ${CYAN}${INSTALL_DIR}${NC}"

    echo -e "\nComponents to install (${#SELECTED_COMPONENTS[@]} total):\n"

    # Group by type
    local agents=()
    local subagents=()
    local commands=()
    local tools=()
    local plugins=()
    local skills=()
    local contexts=()
    local configs=()

    for comp in "${SELECTED_COMPONENTS[@]}"; do
        local type="${comp%%:*}"
        case $type in
            agent) agents+=("$comp") ;;
            subagent) subagents+=("$comp") ;;
            command) commands+=("$comp") ;;
            tool) tools+=("$comp") ;;
            plugin) plugins+=("$comp") ;;
            skill) skills+=("$comp") ;;
            context) contexts+=("$comp") ;;
            config) configs+=("$comp") ;;
        esac
    done

    [ ${#agents[@]} -gt 0 ] && echo -e "${CYAN}Agents (${#agents[@]}):${NC} ${agents[*]##*:}"
    [ ${#subagents[@]} -gt 0 ] && echo -e "${CYAN}Subagents (${#subagents[@]}):${NC} ${subagents[*]##*:}"
    [ ${#commands[@]} -gt 0 ] && echo -e "${CYAN}Commands (${#commands[@]}):${NC} ${commands[*]##*:}"
    [ ${#tools[@]} -gt 0 ] && echo -e "${CYAN}Tools (${#tools[@]}):${NC} ${tools[*]##*:}"
    [ ${#plugins[@]} -gt 0 ] && echo -e "${CYAN}Plugins (${#plugins[@]}):${NC} ${plugins[*]##*:}"
    [ ${#skills[@]} -gt 0 ] && echo -e "${CYAN}Skills (${#skills[@]}):${NC} ${skills[*]##*:}"
    [ ${#contexts[@]} -gt 0 ] && echo -e "${CYAN}Contexts (${#contexts[@]}):${NC} ${contexts[*]##*:}"
    [ ${#configs[@]} -gt 0 ] && echo -e "${CYAN}Config (${#configs[@]}):${NC} ${configs[*]##*:}"

    echo ""

    # Skip confirmation if profile was provided via command line
    if [ "$NON_INTERACTIVE" = true ]; then
        print_info "Installing automatically (profile specified)..."
        perform_installation
    else
        read -r -p "Proceed with installation? [Y/n]: " confirm

        if [[ $confirm =~ ^[Nn] ]]; then
            print_info "Installation cancelled"
            cleanup_and_exit 0
        fi

        perform_installation
    fi
}

show_collision_report() {
    local collision_count=$1
    shift
    local collisions=("$@")

    echo ""
    print_warning "Found ${collision_count} file collision(s):"
    echo ""

    # Group by type
    local agents=()
    local subagents=()
    local commands=()
    local tools=()
    local plugins=()
    local skills=()
    local contexts=()
    local configs=()

    for file in "${collisions[@]}"; do
        # Skip empty entries
        [ -z "$file" ] && continue

        if [[ $file == *"/agent/subagents/"* ]]; then
            subagents+=("$file")
        elif [[ $file == *"/agent/"* ]]; then
            agents+=("$file")
        elif [[ $file == *"/command/"* ]]; then
            commands+=("$file")
        elif [[ $file == *"/tool/"* ]]; then
            tools+=("$file")
        elif [[ $file == *"/plugin/"* ]]; then
            plugins+=("$file")
        elif [[ $file == *"/skills/"* ]]; then
            skills+=("$file")
        elif [[ $file == *"/context/"* ]]; then
            contexts+=("$file")
        else
            configs+=("$file")
        fi
    done

    # Display grouped collisions
    [ ${#agents[@]} -gt 0 ] && echo -e "${YELLOW}  Agents (${#agents[@]}):${NC}" && printf '    %s\n' "${agents[@]}"
    [ ${#subagents[@]} -gt 0 ] && echo -e "${YELLOW}  Subagents (${#subagents[@]}):${NC}" && printf '    %s\n' "${subagents[@]}"
    [ ${#commands[@]} -gt 0 ] && echo -e "${YELLOW}  Commands (${#commands[@]}):${NC}" && printf '    %s\n' "${commands[@]}"
    [ ${#tools[@]} -gt 0 ] && echo -e "${YELLOW}  Tools (${#tools[@]}):${NC}" && printf '    %s\n' "${tools[@]}"
    [ ${#plugins[@]} -gt 0 ] && echo -e "${YELLOW}  Plugins (${#plugins[@]}):${NC}" && printf '    %s\n' "${plugins[@]}"
    [ ${#skills[@]} -gt 0 ] && echo -e "${YELLOW}  Skills (${#skills[@]}):${NC}" && printf '    %s\n' "${skills[@]}"
    [ ${#contexts[@]} -gt 0 ] && echo -e "${YELLOW}  Context (${#contexts[@]}):${NC}" && printf '    %s\n' "${contexts[@]}"
    [ ${#configs[@]} -gt 0 ] && echo -e "${YELLOW}  Config (${#configs[@]}):${NC}" && printf '    %s\n' "${configs[@]}"

    echo ""
}

get_install_strategy() {
    echo -e "${BOLD}How would you like to proceed?${NC}\n" >&2
    echo "  1) ${GREEN}Skip existing${NC} - Only install new files, keep all existing files unchanged" >&2
    echo "  2) ${YELLOW}Overwrite all${NC} - Replace existing files with new versions (your changes will be lost)" >&2
    echo "  3) ${CYAN}Backup & overwrite${NC} - Backup existing files, then install new versions" >&2
    echo "  4) ${RED}Cancel${NC} - Exit without making changes" >&2
    echo "" >&2
    read -r -p "Enter your choice [1-4]: " strategy_choice

    case $strategy_choice in
        1) echo "skip" ;;
        2)
            echo "" >&2
            print_warning "This will overwrite existing files. Your changes will be lost!"
            read -r -p "Are you sure? Type 'yes' to confirm: " confirm
            if [ "$confirm" = "yes" ]; then
                echo "overwrite"
            else
                echo "cancel"
            fi
            ;;
        3) echo "backup" ;;
        4) echo "cancel" ;;
        *) echo "cancel" ;;
    esac
}
