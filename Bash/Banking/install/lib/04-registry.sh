#!/usr/bin/env bash
# shellcheck shell=bash
#
# 04-registry.sh - Registry fetch and query functions
#############################################################################

fetch_registry() {
    print_step "Fetching component registry..."

    mkdir -p "$TEMP_DIR"

    # Handle local file:// URLs
    if [[ "$REGISTRY_URL" == file://* ]]; then
        local local_path="${REGISTRY_URL#file://}"
        if [ -f "$local_path" ]; then
            cp "$local_path" "$TEMP_DIR/registry.json"
            print_success "Using local registry: $local_path"
        else
            print_error "Local registry not found: $local_path"
            exit 1
        fi
    else
        # Fetch from remote URL
        if ! curl -fsSL "$REGISTRY_URL" -o "$TEMP_DIR/registry.json"; then
            print_error "Failed to fetch registry from $REGISTRY_URL"
            exit 1
        fi
        print_success "Registry fetched successfully"
    fi
}

get_profile_components() {
    local profile=$1
    jq_exec ".profiles.${profile}.components[]?" "$TEMP_DIR/registry.json"
}

get_component_info() {
    local component_id=$1
    local component_type=$2

    if [ "$component_type" = "context" ] && [[ "$component_id" == */* ]]; then
        jq_exec "first(.components.contexts[]? | select(.path == \".opencode/context/${component_id}.md\"))" "$TEMP_DIR/registry.json"
        return
    fi

    jq_exec ".components.${component_type}[]? | select(.id == \"${component_id}\" or (.aliases // [] | index(\"${component_id}\")))" "$TEMP_DIR/registry.json"
}

resolve_component_path() {
    local component_type=$1
    local component_id=$2
    local registry_key
    registry_key=$(get_registry_key "$component_type")

    if [ "$component_type" = "context" ] && [[ "$component_id" == */* ]]; then
        # Try .md extension first (most context files), then fall back to the
        # path as-is for non-markdown files (e.g. paths.json). Fixes #251.
        local result
        result=$(jq_exec "first(.components.contexts[]? | select(.path == \".opencode/context/${component_id}.md\") | .path)" "$TEMP_DIR/registry.json")
        if [ -z "$result" ] || [ "$result" = "null" ]; then
            result=$(jq_exec "first(.components.contexts[]? | select(.path == \".opencode/context/${component_id}\") | .path)" "$TEMP_DIR/registry.json")
        fi
        echo "$result"
        return
    fi

    jq_exec ".components.${registry_key}[]? | select(.id == \"${component_id}\" or (.aliases // [] | index(\"${component_id}\"))) | .path" "$TEMP_DIR/registry.json"
}

# Helper function to get the correct registry key for a component type
get_registry_key() {
    local type=$1
    # Handle both singular and plural forms
    # Registry uses plural keys: agents, contexts, skills
    case "$type" in
        config) echo "config" ;;
        # Already plural forms - use as-is
        agents|contexts|skills) echo "$type" ;;
        # Singular forms - pluralize them
        agent) echo "agents" ;;
        context) echo "contexts" ;;
        skill) echo "skills" ;;
        # Fallback: if already ends with 's', assume plural
        *s) echo "$type" ;;
        # Default: add 's' to make plural
        *) echo "${type}s" ;;
    esac
}

# Helper function to convert registry path to installation path
# Registry paths are like ".opencode/agent/foo.md"
# We need to replace ".opencode" with the actual INSTALL_DIR
get_install_path() {
    local registry_path=$1
    # Strip leading .opencode/ if present
    local relative_path="${registry_path#.opencode/}"
    # Return INSTALL_DIR + relative path
    echo "${INSTALL_DIR}/${relative_path}"
}
