# DRY_RUN_SUPPORT=true
#!/usr/bin/env bash
# shellcheck shell=bash

set -euo pipefail

# Script to analyze all bash, PowerShell, bat, and TypeScript scripts
# Target directories as per Phase 1 requirements

OUTPUT_FILE="/c/Users/Alexa/Desktop/Sandbox/docs/bash-scripts-list-context.md"
TEMP_DIR="/c/Users/Alexa/Desktop/Sandbox/.temp-analysis"

# Create output directory
mkdir -p "$(dirname "$OUTPUT_FILE")"
mkdir -p "$TEMP_DIR"

# Define target directories
TARGET_DIRS=(
    "/c/Users/Alexa/Desktop/Sandbox/Bash/scripts"
    "/c/Users/Alexa/Desktop/Sandbox/Bash"
    "/c/Users/Alexa/Desktop/Sandbox/projects/Banking/scripts"
    "/c/Users/Alexa/Desktop/Sandbox/projects/Banking"
    "/c/Users/Alexa/Desktop/Sandbox/projects/comicwise/scripts"
    "/c/Users/Alexa/Desktop/Sandbox/projects/comicwise"
)

# Initialize output file with header
cat > "$OUTPUT_FILE" <<'HEADER'
# Bash Scripts Inventory and Risk Assessment
## Phase 1: Complete Script Catalog

**Generated:** $(date)
**Analysis Scope:** Bash scripts (.sh), PowerShell scripts (.ps1), Batch files (.bat), TypeScript scripts (.ts)
**Target Directories:**
- Bash/scripts/**, Bash/**
- projects/Banking/scripts/**, projects/Banking/**
- projects/comicwise/scripts/**, projects/comicwise/**

---

## Executive Summary

This document provides a comprehensive inventory of all scripts across target directories with metadata, dependency analysis, and risk assessments.

### Risk Level Classification:
- **CRITICAL**: Hardcoded credentials, rm -rf patterns, eval/exec usage, no validation
- **HIGH**: Elevated privileges, destructive operations, external command injection potential
- **MEDIUM**: Complex logic, multiple external dependencies, minimal error handling
- **LOW**: Simple operations, well-validated, good error handling

---

## Script Inventory

| File Path | Type | Size | LOC | Last Modified | Purpose | Dependencies | Risk Level | Notes |
|-----------|------|------|-----|---------------|---------|--------------|------------|-------|
HEADER

# Function to count lines of code (excluding blanks and comments)
count_loc() {
    local file="$1"
    local ext="${file##*.}"
    
    case "$ext" in
        sh)
            grep -v '^\s*#' "$file" | grep -v '^\s*$' | wc -l 2>/dev/null || echo "0"
            ;;
        ps1)
            grep -v '^\s*#' "$file" | grep -v '^\s*$' | wc -l 2>/dev/null || echo "0"
            ;;
        bat)
            grep -v '^\s*REM' "$file" | grep -v '^\s*::' | grep -v '^\s*$' | wc -l 2>/dev/null || echo "0"
            ;;
        ts)
            grep -v '^\s*//' "$file" | grep -v '^\s*\*' "$file" | grep -v '^\s*$' | wc -l 2>/dev/null || echo "0"
            ;;
        *)
            wc -l < "$file" 2>/dev/null || echo "0"
            ;;
    esac
}

# Function to analyze script purpose from header comments
analyze_purpose() {
    local file="$1"
    head -20 "$file" | grep -E "^#|^REM|^::" | grep -iE "purpose|description|summary" | head -1 | sed 's/^[#:REM ]*//' | tr '\n' ' ' || echo "No description"
}

# Function to extract dependencies
extract_dependencies() {
    local file="$1"
    local deps=""
    
    # Look for common patterns: source, require, import, external commands
    local pattern="(source|require|import|from|using) +['\"]?[^'\"[:space:]]+"
    deps=$(grep -oE "$pattern" "$file" 2>/dev/null | awk '{print $2}' | tr -d "'\"" | sort -u | tr '\n' ', ' | sed 's/,$//')

    # Also check for external command calls
    local ext_pattern="(git|npm|node|bun|curl|wget|docker|kubectl) "
    local external=$(grep -oE "$ext_pattern" "$file" 2>/dev/null | sort -u | tr '\n' ', ' | sed 's/,$//')
    
    if [ -n "$external" ]; then
        if [ -n "$deps" ]; then
            deps="$deps, $external"
        else
            deps="$external"
        fi
    fi
    
    [ -z "$deps" ] && deps="None detected"
    echo "$deps"
}

# Function to assess risk level
assess_risk() {
    local file="$1"
    local risk="LOW"
    local notes=""
    
    # Check for CRITICAL patterns
    local critical_pattern="(password|secret|token|api_key|credential).*="
    if grep -qE "$critical_pattern" "$file" 2>/dev/null; then
        risk="CRITICAL"
        notes="${notes}Hardcoded credentials found; "
    fi

    local rm_pattern="rm +(-rf|-fr|-r -f|-f -r)"
    if grep -qE "$rm_pattern" "$file" 2>/dev/null; then
        risk="CRITICAL"
        notes="${notes}Destructive rm -rf pattern; "
    fi

    if grep -qE "eval|exec" "$file" 2>/dev/null; then
        risk="CRITICAL"
        notes="${notes}eval/exec usage detected; "
    fi
    
    # Check for HIGH risk patterns
    if [ "$risk" != "CRITICAL" ]; then
        if grep -qE "sudo|runas|elevate" "$file" 2>/dev/null; then
            risk="HIGH"
            notes="${notes}Elevated privileges; "
        fi
        
        if grep -qE "DROP|DELETE|TRUNCATE" "$file" 2>/dev/null; then
            risk="HIGH"
            notes="${notes}Database destructive ops; "
        fi
    fi
    
    # Check for MEDIUM risk patterns
    if [ "$risk" = "LOW" ]; then
        local complexity=$(grep -cE "if|while|for|case" "$file" 2>/dev/null)
        if [ "$complexity" -gt 10 ]; then
            risk="MEDIUM"
            notes="${notes}High cyclomatic complexity; "
        fi
    fi
    
    # Check for dead code indicators (last modified >6 months and low git activity)
    local mod_time=$(stat -c %Y "$file" 2>/dev/null || stat -f %m "$file" 2>/dev/null || echo "0")
    local current_time=$(date +%s)
    local age_days=$(( (current_time - mod_time) / 86400 ))
    
    if [ "$age_days" -gt 180 ]; then
        notes="${notes}Not modified >6mo; "
    fi
    
    # Remove trailing semicolon and space
    notes=$(echo "$notes" | sed 's/; $//')
    [ -z "$notes" ] && notes="Standard script"
    
    echo "$risk|$notes"
}

# Main analysis loop
echo "" >> "$OUTPUT_FILE"

for dir in "${TARGET_DIRS[@]}"; do
    if [ ! -d "$dir" ]; then
        continue
    fi
    
    # Find all script files
    find "$dir" -type f \( -name "*.sh" -o -name "*.ps1" -o -name "*.bat" -o -name "*.ts" \) 2>/dev/null | while read -r script; do
        # Skip node_modules and .git directories
        if echo "$script" | grep -qE "node_modules|\.git/|archive/skills-commit-batches"; then
            continue
        fi
        
        # Get file metadata
        file_path="$script"
        file_type="${script##*.}"
        file_size=$(stat -c %s "$script" 2>/dev/null || stat -f %z "$script" 2>/dev/null || echo "0")
        file_size_kb=$(( file_size / 1024 ))
        [ "$file_size_kb" -eq 0 ] && file_size_kb="<1"
        
        last_modified=$(stat -c %y "$script" 2>/dev/null | cut -d' ' -f1 || stat -f %Sm -t "%Y-%m-%d" "$script" 2>/dev/null || echo "Unknown")
        
        loc=$(count_loc "$script")
        purpose=$(analyze_purpose "$script" | sed 's/|/-/g' | tr '\n' ' ' | cut -c1-80)
        dependencies=$(extract_dependencies "$script" | sed 's/|/-/g' | cut -c1-60)
        
        risk_data=$(assess_risk "$script")
        risk_level=$(echo "$risk_data" | cut -d'|' -f1)
        risk_notes=$(echo "$risk_data" | cut -d'|' -f2 | sed 's/|/-/g')
        
        # Write to output file
        echo "| $file_path | $file_type | ${file_size_kb}KB | $loc | $last_modified | $purpose | $dependencies | **$risk_level** | $risk_notes |" >> "$OUTPUT_FILE"
    done
done

# Add summary statistics
echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "## Summary Statistics" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# Count by type
echo "### Scripts by Type" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
grep "| .* |" "$OUTPUT_FILE" | grep -v "File Path" | awk -F'|' '{print $3}' | sort | uniq -c | while read count type; do
    echo "- **$type**: $count scripts" >> "$OUTPUT_FILE"
done

echo "" >> "$OUTPUT_FILE"
echo "### Scripts by Risk Level" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
grep "| .* |" "$OUTPUT_FILE" | grep -oE "\*\*[A-Z]+\*\*" | sort | uniq -c | while read count risk; do
    risk_clean=$(echo "$risk" | tr -d '*')
    echo "- **$risk_clean**: $count scripts" >> "$OUTPUT_FILE"
done

echo "" >> "$OUTPUT_FILE"
echo "---" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "## Detailed Risk Findings" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "### Critical Risk Scripts" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

grep "| .* |" "$OUTPUT_FILE" | grep "\*\*CRITICAL\*\*" | awk -F'|' '{print "- " $2 " - " $9}' >> "$OUTPUT_FILE"

echo "" >> "$OUTPUT_FILE"
echo "### High Risk Scripts" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

grep "| .* |" "$OUTPUT_FILE" | grep "\*\*HIGH\*\*" | awk -F'|' '{print "- " $2 " - " $9}' >> "$OUTPUT_FILE"

# Cleanup
rm -rf "$TEMP_DIR"

echo ""
echo "Analysis complete! Output written to: $OUTPUT_FILE"
echo ""
