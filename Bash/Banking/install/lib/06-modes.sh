#!/usr/bin/env bash
# shellcheck shell=bash
#
# 06-modes.sh - Interactive mode selection and menus
#############################################################################

check_interactive_mode() {
    # Check if stdin is a terminal (not piped from curl)
    if [ ! -t 0 ]; then
        print_header
        print_error "Interactive mode requires a terminal"
        echo ""
        echo "You're running this script in a pipe (e.g., curl | bash)"
        echo "For interactive mode, download the script first:"
        echo ""
        echo -e "${CYAN}# Download the script${NC}"
        echo "curl -fsSL https://raw.githubusercontent.com/darrenhinde/OpenAgentsControl/main/install.sh -o install.sh"
        echo ""
        echo -e "${CYAN}# Run interactively${NC}"
        echo "bash install.sh"
        echo ""
        echo "Or use a profile directly:"
        echo ""
        echo -e "${CYAN}# Quick install with profile${NC}"
        echo "curl -fsSL https://raw.githubusercontent.com/darrenhinde/OpenAgentsControl/main/install.sh | bash -s essential"
        echo ""
        echo "Available profiles: essential, developer, business, full, advanced"
        echo ""
        cleanup_and_exit 1
    fi
}

show_install_location_menu() {
    check_interactive_mode

    clear
    print_header

    local global_path
    global_path=$(get_global_install_path)

    echo -e "${BOLD}Choose installation location:${NC}\n"
    echo -e "  ${GREEN}1) Local${NC} - Install to ${CYAN}.opencode/${NC} in current directory"
    echo "     (Best for project-specific agents)"
    echo ""
    echo -e "  ${BLUE}2) Global${NC} - Install to ${CYAN}${global_path}${NC}"
    echo "     (Best for user-wide agents available everywhere)"
    echo ""
    echo -e "  ${MAGENTA}3) Custom${NC} - Enter exact path"
    echo "     Examples:"
    case "$PLATFORM" in
        Windows)
            echo -e "       ${CYAN}C:/Users/username/my-agents${NC} or ${CYAN}~/my-agents${NC}"
            ;;
        *)
            echo -e "       ${CYAN}/home/username/my-agents${NC} or ${CYAN}~/my-agents${NC}"
            ;;
    esac
    echo ""
    echo "  4) Back / Exit"
    echo ""
    read -r -p "Enter your choice [1-4]: " location_choice

    case $location_choice in
        1)
            INSTALL_DIR=".opencode"
            print_success "Installing to local directory: .opencode/"
            sleep 1
            ;;
        2)
            INSTALL_DIR="$global_path"
            print_success "Installing to global directory: $global_path"
            sleep 1
            ;;
        3)
            echo ""
            read -r -p "Enter installation path: " custom_path

            if [ -z "$custom_path" ]; then
                print_error "No path entered"
                sleep 2
                show_install_location_menu
                return
            fi

            local normalized_path
            normalized_path=$(normalize_and_validate_path "$custom_path")

            if ! normalize_and_validate_path "$custom_path" > /dev/null; then
                print_error "Invalid path"
                sleep 2
                show_install_location_menu
                return
            fi

            if ! validate_install_path "$normalized_path"; then
                echo ""
                read -r -p "Continue anyway? [y/N]: " continue_choice
                if [[ ! $continue_choice =~ ^[Yy] ]]; then
                    show_install_location_menu
                    return
                fi
            fi

            INSTALL_DIR="$normalized_path"
            print_success "Installing to custom directory: $INSTALL_DIR"
            sleep 1
            ;;
        4)
            cleanup_and_exit 0
            ;;
        *)
            print_error "Invalid choice"
            sleep 2
            show_install_location_menu
            return
            ;;
    esac
}

show_main_menu() {
    check_interactive_mode

    clear
    print_header

    echo -e "${BOLD}Choose installation mode:${NC}\n"
    echo "  1) Quick Install (Choose a profile)"
    echo "  2) Custom Install (Pick individual components)"
    echo "  3) List Available Components"
    echo "  4) Exit"
    echo ""
    read -r -p "Enter your choice [1-4]: " choice

    case $choice in
        1) INSTALL_MODE="profile" ;;
        2) INSTALL_MODE="custom" ;;
        3) list_components; read -r -p "Press Enter to continue..."; show_main_menu ;;
        4) cleanup_and_exit 0 ;;
        *) print_error "Invalid choice"; sleep 2; show_main_menu ;;
    esac
}

show_profile_menu() {
    clear
    print_header

    echo -e "${BOLD}Available Installation Profiles:${NC}\n"

    # Essential profile
    local essential_name
    essential_name=$(jq_exec '.profiles.essential.name' "$TEMP_DIR/registry.json")
    local essential_desc
    essential_desc=$(jq_exec '.profiles.essential.description' "$TEMP_DIR/registry.json")
    local essential_count
    essential_count=$(jq_exec '.profiles.essential.components | length' "$TEMP_DIR/registry.json")
    echo -e "  ${GREEN}1) ${essential_name}${NC}"
    echo -e "     ${essential_desc}"
    echo -e "     Components: ${essential_count}\n"

    # Developer profile
    local dev_desc
    dev_desc=$(jq_exec '.profiles.developer.description' "$TEMP_DIR/registry.json")
    local dev_count
    dev_count=$(jq_exec '.profiles.developer.components | length' "$TEMP_DIR/registry.json")
    local dev_badge
    dev_badge=$(jq_exec '.profiles.developer.badge // ""' "$TEMP_DIR/registry.json")
    if [ -n "$dev_badge" ]; then
        echo -e "  ${BLUE}2) Developer ${GREEN}[${dev_badge}]${NC}"
    else
        echo -e "  ${BLUE}2) Developer${NC}"
    fi
    echo -e "     ${dev_desc}"
    echo -e "     Components: ${dev_count}\n"

    # Business profile
    local business_name
    business_name=$(jq_exec '.profiles.business.name' "$TEMP_DIR/registry.json")
    local business_desc
    business_desc=$(jq_exec '.profiles.business.description' "$TEMP_DIR/registry.json")
    local business_count
    business_count=$(jq_exec '.profiles.business.components | length' "$TEMP_DIR/registry.json")
    echo -e "  ${CYAN}3) ${business_name}${NC}"
    echo -e "     ${business_desc}"
    echo -e "     Components: ${business_count}\n"

    # Full profile
    local full_name
    full_name=$(jq_exec '.profiles.full.name' "$TEMP_DIR/registry.json")
    local full_desc
    full_desc=$(jq_exec '.profiles.full.description' "$TEMP_DIR/registry.json")
    local full_count
    full_count=$(jq_exec '.profiles.full.components | length' "$TEMP_DIR/registry.json")
    echo -e "  ${MAGENTA}4) ${full_name}${NC}"
    echo -e "     ${full_desc}"
    echo -e "     Components: ${full_count}\n"

    # Advanced profile
    local adv_name
    adv_name=$(jq_exec '.profiles.advanced.name' "$TEMP_DIR/registry.json")
    local adv_desc
    adv_desc=$(jq_exec '.profiles.advanced.description' "$TEMP_DIR/registry.json")
    local adv_count
    adv_count=$(jq_exec '.profiles.advanced.components | length' "$TEMP_DIR/registry.json")
    echo -e "  ${YELLOW}5) ${adv_name}${NC}"
    echo -e "     ${adv_desc}"
    echo -e "     Components: ${adv_count}\n"

    echo "  6) Back to main menu"
    echo ""
    read -r -p "Enter your choice [1-6]: " choice

    case $choice in
        1) PROFILE="essential" ;;
        2) PROFILE="developer" ;;
        3) PROFILE="business" ;;
        4) PROFILE="full" ;;
        5) PROFILE="advanced" ;;
        6) show_main_menu; return ;;
        *) print_error "Invalid choice"; sleep 2; show_profile_menu; return ;;
    esac

    # Load profile components (compatible with bash 3.2+)
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
}

show_custom_menu() {
    clear
    print_header

    echo -e "${BOLD}Select component categories to install:${NC}\n"
    echo "Use space to toggle, Enter to continue"
    echo ""

    local categories=("agents" "subagents" "commands" "tools" "plugins" "skills" "contexts" "config")
    local selected_categories=()

    # Simple selection (for now, we'll make it interactive later)
    echo "Available categories:"
    for i in "${!categories[@]}"; do
        local cat="${categories[$i]}"
        local count
        count=$(jq_exec ".components.${cat} | length" "$TEMP_DIR/registry.json")
        local cat_display
        cat_display=$(echo "$cat" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}')
        echo "  $((i+1))) ${cat_display} (${count} available)"
    done
    echo "  $((${#categories[@]}+1))) Select All"
    echo "  $((${#categories[@]}+2))) Continue to component selection"
    echo "  $((${#categories[@]}+3))) Back to main menu"
    echo ""

    read -r -p "Enter category numbers (space-separated) or option: " -a selections

    for sel in "${selections[@]}"; do
        if [ "$sel" -eq $((${#categories[@]}+1)) ]; then
            selected_categories=("${categories[@]}")
            break
        elif [ "$sel" -eq $((${#categories[@]}+2)) ]; then
            break
        elif [ "$sel" -eq $((${#categories[@]}+3)) ]; then
            show_main_menu
            return
        elif [ "$sel" -ge 1 ] && [ "$sel" -le ${#categories[@]} ]; then
            selected_categories+=("${categories[$((sel-1))]}")
        fi
    done

    if [ ${#selected_categories[@]} -eq 0 ]; then
        print_warning "No categories selected"
        sleep 2
        show_custom_menu
        return
    fi

    show_component_selection "${selected_categories[@]}"
}

show_component_selection() {
    local categories=("$@")
    clear
    print_header

    echo -e "${BOLD}Select components to install:${NC}\n"

    local all_components=()
    local component_details=()

    for category in "${categories[@]}"; do
        local cat_display
        cat_display=$(echo "$category" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}')
        echo -e "${CYAN}${BOLD}${cat_display}:${NC}"

        local components
        components=$(jq_exec ".components.${category}[]? | .id" "$TEMP_DIR/registry.json")

        local idx=1
        while IFS= read -r comp_id; do
            local comp_name
            comp_name=$(jq_exec ".components.${category}[]? | select(.id == \"${comp_id}\") | .name" "$TEMP_DIR/registry.json")
            local comp_desc
            comp_desc=$(jq_exec ".components.${category}[]? | select(.id == \"${comp_id}\") | .description" "$TEMP_DIR/registry.json")

            echo "  ${idx}) ${comp_name}"
            echo "     ${comp_desc}"

            all_components+=("${category}:${comp_id}")
            component_details+=("${comp_name}|${comp_desc}")

            idx=$((idx+1))
        done <<< "$components"

        echo ""
    done

    echo "Enter component numbers (space-separated), 'all' for all, or 'done' to continue:"
    read -r -a selections

    for sel in "${selections[@]}"; do
        if [ "$sel" = "all" ]; then
            SELECTED_COMPONENTS=("${all_components[@]}")
            break
        elif [ "$sel" = "done" ]; then
            break
        elif [ "$sel" -ge 1 ] && [ "$sel" -le ${#all_components[@]} ]; then
            SELECTED_COMPONENTS+=("${all_components[$((sel-1))]}")
        fi
    done

    if [ ${#SELECTED_COMPONENTS[@]} -eq 0 ]; then
        print_warning "No components selected"
        sleep 2
        show_custom_menu
        return
    fi

    # Resolve dependencies
    print_step "Resolving dependencies..."
    local original_count=${#SELECTED_COMPONENTS[@]}
    for comp in "${SELECTED_COMPONENTS[@]}"; do
        resolve_dependencies "$comp"
    done

    if [ ${#SELECTED_COMPONENTS[@]} -gt "$original_count" ]; then
        print_info "Added $((${#SELECTED_COMPONENTS[@]} - original_count)) dependencies"
    fi

    show_installation_preview
}
