#!/usr/bin/env bash
# shellcheck shell=bash
#
# 02-paths.sh - Cross-platform path handling functions
#############################################################################

normalize_and_validate_path() {
    local input_path="$1"
    local normalized_path

    # Handle empty path
    if [ -z "$input_path" ]; then
        echo ""
        return 1
    fi

    # Expand tilde to $HOME (works on Linux, macOS, Windows Git Bash)
    if [[ $input_path == ~* ]]; then
        normalized_path="${HOME}${input_path:1}"
    else
        normalized_path="$input_path"
    fi

    # Convert backslashes to forward slashes (Windows compatibility)
    normalized_path="${normalized_path//\\//}"

    # Remove trailing slashes
    normalized_path="${normalized_path%/}"

    # If path is relative, make it absolute based on current directory
    if [[ ! "$normalized_path" = /* ]] && [[ ! "$normalized_path" =~ ^[A-Za-z]: ]]; then
        normalized_path="$(pwd)/${normalized_path}"
    fi

    echo "$normalized_path"
    return 0
}

validate_install_path() {
    local path="$1"
    local parent_dir

    # Get parent directory
    parent_dir="$(dirname "$path")"

    # Check if parent directory exists
    if [ ! -d "$parent_dir" ]; then
        print_error "Parent directory does not exist: $parent_dir"
        return 1
    fi

    # Check if parent directory is writable
    if [ ! -w "$parent_dir" ]; then
        print_error "No write permission for directory: $parent_dir"
        return 1
    fi

    # If target directory exists, check if it's writable
    if [ -d "$path" ] && [ ! -w "$path" ]; then
        print_error "No write permission for directory: $path"
        return 1
    fi

    return 0
}

get_global_install_path() {
    # Return platform-appropriate global installation path
    case "$PLATFORM" in
        macOS|Linux|Windows)
            echo "${HOME}/.config/opencode"
            ;;
        *)
            echo "${HOME}/.config/opencode"
            ;;
    esac
}
