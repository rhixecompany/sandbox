#!/usr/bin/env bash
# shellcheck shell=bash
#
# 01-utils.sh - Utility functions for the OpenAgents Control Installer
#############################################################################

# jq_exec wrapper - use jq, or fall back to node/python for JSON parsing
jq_exec() {
    local output
    output=$(jq -r "$@")
    local ret=$?
    printf "%s\n" "$output" | tr -d '\r'
    return $ret
}

print_header() {
    echo -e "${CYAN}${BOLD}"
    echo "╔════════════════════════════════════════════════════════════════╗"
    echo "║                                                                ║"
    echo "║           OpenAgents Control Installer v1.0.0                 ║"
    echo "║                                                                ║"
    echo "╚════════════════════════════════════════════════════════════════╝"
    echo -e "${NC}"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1"
}

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

print_step() {
    echo -e "\n${MAGENTA}${BOLD}▶${NC} $1\n"
}
