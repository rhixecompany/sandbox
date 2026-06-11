#!/usr/bin/env bash
# shellcheck shell=bash
#
# 00-config.sh - Platform detection, colors, configuration, and global vars
# Part of the OpenAgents Control Installer
#############################################################################

# Safe defaults for set -u (environment variables that may not be set)
: "${WT_SESSION:=}"
: "${ConEmuPID:=}"
: "${REGISTRY_URL:=}"

# Detect platform
PLATFORM="$(uname -s)"
case "$PLATFORM" in
    Linux*)     PLATFORM="Linux";;
    Darwin*)    PLATFORM="macOS";;
    CYGWIN*|MINGW*|MSYS*) PLATFORM="Windows";;
    *)          PLATFORM="Unknown";;
esac

# Colors for output (disable on Windows if not supported)
if [ "$PLATFORM" = "Windows" ] && [ -z "$WT_SESSION" ] && [ -z "$ConEmuPID" ]; then
    # Basic Windows terminal without color support
    RED=''
    GREEN=''
    YELLOW=''
    BLUE=''
    MAGENTA=''
    CYAN=''
    BOLD=''
    NC=''
else
    RED='\033[0;31m'
    GREEN='\033[0;32m'
    YELLOW='\033[1;33m'
    BLUE='\033[0;34m'
    MAGENTA='\033[0;35m'
    CYAN='\033[0;36m'
    BOLD='\033[1m'
    NC='\033[0m' # No Color
fi

# Configuration
REPO_URL="https://github.com/darrenhinde/OpenAgentsControl"
BRANCH="${OPENCODE_BRANCH:-main}"  # Allow override via environment variable
RAW_URL="https://raw.githubusercontent.com/darrenhinde/OpenAgentsControl/${BRANCH}"

# Registry URL - supports local fallback for development
# Priority: 1) REGISTRY_URL env var, 2) Local registry.json, 3) Remote GitHub
if [ -n "$REGISTRY_URL" ]; then
    # Use explicitly set REGISTRY_URL (for testing)
    :
elif [ -f "./registry.json" ]; then
    # Use local registry.json if it exists (for development)
    REGISTRY_URL="file://$(pwd)/registry.json"
else
    # Default to remote GitHub registry
    REGISTRY_URL="${RAW_URL}/registry.json"
fi

INSTALL_DIR="${OPENCODE_INSTALL_DIR:-.opencode}"  # Allow override via environment variable
TEMP_DIR="/tmp/opencode-installer-$$"

# Global variables
SELECTED_COMPONENTS=()
INSTALL_MODE=""
PROFILE=""
NON_INTERACTIVE=false
CUSTOM_INSTALL_DIR=""  # Set via --install-dir argument
