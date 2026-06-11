#!/usr/bin/env bash
# shellcheck shell=bash
#
# 08-install.sh - Installation execution, post-install, component listing, cleanup
#############################################################################

perform_installation() {
    print_step "Preparing installation..."

    # Create base directory only - subdirectories created on-demand when files are installed
    mkdir -p "$INSTALL_DIR"

    # Check for collisions
    local collisions=()
    for comp in "${SELECTED_COMPONENTS[@]}"; do
        local type="${comp%%:*}"
        local id="${comp##*:}"
        local registry_key
        registry_key=$(get_registry_key "$type")
        local path
        path=$(resolve_component_path "$type" "$id")

        if [ -n "$path" ] && [ "$path" != "null" ]; then
            local install_path
            install_path=$(get_install_path "$path")
            if [ -f "$install_path" ]; then
                collisions+=("$install_path")
            fi
        fi
    done

    # Determine installation strategy
    local install_strategy="fresh"

    if [ ${#collisions[@]} -gt 0 ]; then
        # In non-interactive mode, use default strategy (skip existing files)
        if [ "$NON_INTERACTIVE" = true ]; then
            print_info "Found ${#collisions[@]} existing file(s) - using 'skip' strategy (non-interactive mode)"
            print_info "To overwrite, download script and run interactively, or delete existing files first"
            install_strategy="skip"
        else
            show_collision_report ${#collisions[@]} "${collisions[@]}"
            install_strategy=$(get_install_strategy)

            if [ "$install_strategy" = "cancel" ]; then
                print_info "Installation cancelled by user"
                cleanup_and_exit 0
            fi
        fi

        # Handle backup strategy
        if [ "$install_strategy" = "backup" ]; then
            local backup_dir
            backup_dir="${INSTALL_DIR}.backup.$(date +%Y%m%d-%H%M%S)"
            print_step "Creating backup..."

            # Only backup files that will be overwritten
            local backup_count=0
            for file in "${collisions[@]}"; do
                if [ -f "$file" ]; then
                    local backup_file="${backup_dir}/${file}"
                    mkdir -p "$(dirname "$backup_file")"
                    if cp "$file" "$backup_file" 2>/dev/null; then
                        backup_count=$((backup_count + 1))
                    else
                        print_warning "Failed to backup: $file"
                    fi
                fi
            done

            if [ $backup_count -gt 0 ]; then
                print_success "Backed up ${backup_count} file(s) to $backup_dir"
                install_strategy="overwrite"  # Now we can overwrite
            else
                print_error "Backup failed. Installation cancelled."
                cleanup_and_exit 1
            fi
        fi
    fi

    # Perform installation
    print_step "Installing components..."

    local installed=0
    local skipped=0
    local failed=0

    for comp in "${SELECTED_COMPONENTS[@]}"; do
        local type="${comp%%:*}"
        local id="${comp##*:}"

        # Get the correct registry key (handles singular/plural)
        local registry_key
        registry_key=$(get_registry_key "$type")

        # Get component path
        local path
        path=$(resolve_component_path "$type" "$id")

        if [ -z "$path" ] || [ "$path" = "null" ]; then
            print_warning "Could not find path for ${comp}"
            failed=$((failed + 1))
            continue
        fi

        # Check if component has additional files (for skills)
        local files_array
        files_array=$(jq_exec ".components.${registry_key}[]? | select(.id == \"${id}\") | .files[]?" "$TEMP_DIR/registry.json")

        if [ -n "$files_array" ]; then
            # Component has multiple files - download all of them
            local component_installed=0
            local component_failed=0

            while IFS= read -r file_path; do
                [ -z "$file_path" ] && continue

                local dest
                dest=$(get_install_path "$file_path")

                # Check if file exists and we're in skip mode
                if [ -f "$dest" ] && [ "$install_strategy" = "skip" ]; then
                    continue
                fi

                # Download file
                local url="${RAW_URL}/${file_path}"
                mkdir -p "$(dirname "$dest")"

                if curl -fsSL "$url" -o "$dest"; then
                    # Transform paths for global installation
                    if [[ "$INSTALL_DIR" != ".opencode" ]] && [[ "$INSTALL_DIR" != *"/.opencode" ]]; then
                        local expanded_path="${INSTALL_DIR/#\~/$HOME}"
                        sed -i.bak -e "s|@\\.opencode/context/|@${expanded_path}/context/|g" \
                                   -e "s|\.opencode/context|${expanded_path}/context|g" "$dest" 2>/dev/null || true
                        rm -f "${dest}.bak" 2>/dev/null || true
                    fi
                    component_installed=$((component_installed + 1))
                else
                    component_failed=$((component_failed + 1))
                fi
            done <<< "$files_array"

            if [ $component_failed -eq 0 ]; then
                print_success "Installed ${type}: ${id} (${component_installed} files)"
                installed=$((installed + 1))
            else
                print_error "Failed to install ${type}: ${id} (${component_failed} files failed)"
                failed=$((failed + 1))
            fi
        else
            # Single file component - original logic
            local dest
            dest=$(get_install_path "$path")

            # Check if file exists before we install (for proper messaging)
            local file_existed=false
            if [ -f "$dest" ]; then
                file_existed=true
            fi

            # Check if file exists and we're in skip mode
            if [ "$file_existed" = true ] && [ "$install_strategy" = "skip" ]; then
                print_info "Skipped existing: ${type}:${id}"
                skipped=$((skipped + 1))
                continue
            fi

            # Download component
            local url="${RAW_URL}/${path}"

            # Create parent directory if needed
            mkdir -p "$(dirname "$dest")"

            if curl -fsSL "$url" -o "$dest"; then
                # Transform paths for global installation (any non-local path)
                # Local paths: .opencode or */.opencode
                if [[ "$INSTALL_DIR" != ".opencode" ]] && [[ "$INSTALL_DIR" != *"/.opencode" ]]; then
                    # Expand tilde and get absolute path for transformation
                    local expanded_path="${INSTALL_DIR/#\~/$HOME}"
                    # Transform @.opencode/context/ references to actual install path
                    sed -i.bak -e "s|@\\.opencode/context/|@${expanded_path}/context/|g" \
                               -e "s|\.opencode/context|${expanded_path}/context|g" "$dest" 2>/dev/null || true
                    rm -f "${dest}.bak" 2>/dev/null || true
                fi

                # Show appropriate message based on whether file existed before
                if [ "$file_existed" = true ]; then
                    print_success "Updated ${type}: ${id}"
                else
                    print_success "Installed ${type}: ${id}"
                fi
                installed=$((installed + 1))
            else
                print_error "Failed to install ${type}: ${id}"
                failed=$((failed + 1))
            fi
        fi
    done

    # Handle additional paths for advanced profile
    if [ "$PROFILE" = "advanced" ]; then
        local additional_paths
        additional_paths=$(jq_exec '.profiles.advanced.additionalPaths[]?' "$TEMP_DIR/registry.json")
        if [ -n "$additional_paths" ]; then
            print_step "Installing additional paths..."
            while IFS= read -r path; do
                # For directories, we'd need to recursively download
                # For now, just note them
                print_info "Additional path: $path (manual download required)"
            done <<< "$additional_paths"
        fi
    fi

    echo ""
    print_success "Installation complete!"
    echo -e "  Installed: ${GREEN}${installed}${NC}"
    [ $skipped -gt 0 ] && echo -e "  Skipped: ${CYAN}${skipped}${NC}"
    [ $failed -gt 0 ] && echo -e "  Failed: ${RED}${failed}${NC}"

    show_post_install
}

show_post_install() {
    echo ""
    print_step "Next Steps"

    echo "1. Review the installed components in ${CYAN}${INSTALL_DIR}/${NC}"

    # Check if env.example was installed
    if [ -f "${INSTALL_DIR}/env.example" ] || [ -f "env.example" ]; then
        echo "2. Copy env.example to .env and configure:"
        echo -e "   ${CYAN}cp env.example .env${NC}"
        echo "3. Start using OpenCode agents:"
    else
        echo "2. Start using OpenCode agents:"
    fi
    echo -e "   ${CYAN}opencode${NC}"
    echo ""

    # Show installation location info
    print_info "Installation directory: ${CYAN}${INSTALL_DIR}${NC}"

    # Check for backup directories
    local has_backup=0
    local backup_dir
    local backup_dirs=()

    shopt -s nullglob
    backup_dirs=("${INSTALL_DIR}.backup."*)
    shopt -u nullglob

    for backup_dir in "${backup_dirs[@]}"; do
        if [ -d "$backup_dir" ]; then
            has_backup=1
            break
        fi
    done
    if [ "$has_backup" -eq 1 ]; then
        print_info "Backup created - you can restore files from ${INSTALL_DIR}.backup.* if needed"
    fi

    print_info "Documentation: ${REPO_URL}"
    echo ""

    cleanup_and_exit 0
}

list_components() {
    clear || true
    print_header

    echo -e "${BOLD}Available Components${NC}\n"

    local categories=("agents" "subagents" "commands" "tools" "plugins" "skills" "contexts")

    for category in "${categories[@]}"; do
        local cat_display
        cat_display=$(echo "$category" | awk '{print toupper(substr($0,1,1)) tolower(substr($0,2))}')
        echo -e "${CYAN}${BOLD}${cat_display}:${NC}"

        local components
        components=$(jq_exec ".components.${category}[]? | \"\(.id)|\(.name)|\(.description)\"" "$TEMP_DIR/registry.json")

        while IFS='|' read -r id name desc; do
            echo -e "  ${GREEN}${name}${NC} (${id})"
            echo -e "    ${desc}"
        done <<< "$components"

        echo ""
    done
}

cleanup_and_exit() {
    rm -rf "$TEMP_DIR"
    exit "$1"
}
