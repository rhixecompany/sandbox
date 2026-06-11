#!/usr/bin/env bash
# shellcheck shell=bash
#
# 05-selection.sh - Component selection, wildcard expansion, dependency resolution
#############################################################################

expand_context_wildcard() {
    local pattern=$1
    local prefix="${pattern%%\**}"

    prefix="${prefix%/}"
    if [ -n "$prefix" ]; then
        prefix="${prefix}/"
    fi

    jq_exec ".components.contexts[]? | select(.path | startswith(\".opencode/context/${prefix}\")) | .path | sub(\"^\\\\.opencode/context/\"; \"\") | sub(\"\\\\.md$\"; \"\")" "$TEMP_DIR/registry.json"
}

expand_selected_components() {
    local expanded=()

    for comp in "${SELECTED_COMPONENTS[@]}"; do
        local type="${comp%%:*}"
        local id="${comp##*:}"

        if [[ "$id" == *"*"* ]]; then
            if [ "$type" != "context" ]; then
                print_warning "Wildcard only supported for context components: ${comp}"
                continue
            fi

            local matches
            matches=$(expand_context_wildcard "$id")

            if [ -z "$matches" ]; then
                print_warning "No contexts matched: ${comp}"
                continue
            fi

            while IFS= read -r match; do
                [ -n "$match" ] && expanded+=("context:${match}")
            done <<< "$matches"
            continue
        fi

        expanded+=("$comp")
    done

    local deduped=()
    for comp in "${expanded[@]}"; do
        local found=0
        for existing in "${deduped[@]}"; do
            if [ "$existing" = "$comp" ]; then
                found=1
                break
            fi
        done
        if [ "$found" -eq 0 ]; then
            deduped+=("$comp")
        fi
    done

    SELECTED_COMPONENTS=("${deduped[@]}")
}

resolve_dependencies() {
    local component=$1
    local type="${component%%:*}"
    local id="${component##*:}"

    # Get the correct registry key (handles singular/plural)
    local registry_key
    registry_key=$(get_registry_key "$type")

    # Get dependencies for this component
    local deps
    deps=$(jq_exec ".components.${registry_key}[] | select(.id == \"${id}\" or (.aliases // [] | index(\"${id}\"))) | .dependencies[]?" "$TEMP_DIR/registry.json" 2>/dev/null || echo "")

    if [ -n "$deps" ]; then
        for dep in $deps; do
            if [[ "$dep" == *"*"* ]]; then
                local dep_type="${dep%%:*}"
                local dep_id="${dep##*:}"

                if [ "$dep_type" = "context" ]; then
                    local matched
                    matched=$(expand_context_wildcard "$dep_id")

                    if [ -z "$matched" ]; then
                        print_warning "No contexts matched dependency: ${dep}"
                        continue
                    fi

                    while IFS= read -r match; do
                        local expanded_dep="context:${match}"
                        local found=0
                        for existing in "${SELECTED_COMPONENTS[@]}"; do
                            if [ "$existing" = "$expanded_dep" ]; then
                                found=1
                                break
                            fi
                        done
                        if [ "$found" -eq 0 ]; then
                            SELECTED_COMPONENTS+=("$expanded_dep")
                            resolve_dependencies "$expanded_dep"
                        fi
                    done <<< "$matched"
                    continue
                fi
            fi

            # Add dependency if not already in list
            local found=0
            for existing in "${SELECTED_COMPONENTS[@]}"; do
                if [ "$existing" = "$dep" ]; then
                    found=1
                    break
                fi
            done
            if [ "$found" -eq 0 ]; then
                SELECTED_COMPONENTS+=("$dep")
                # Recursively resolve dependencies
                resolve_dependencies "$dep"
            fi
        done
    fi
}
