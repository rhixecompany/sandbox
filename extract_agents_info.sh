#!/bin/bash
set -e

BASE_DIR="$(pwd)"
PROJECTS_DIR="$BASE_DIR/projects"
OUTPUT_DIR="$BASE_DIR/docs"
OUTPUT_FILE="$OUTPUT_DIR/repo-inventory-context.md"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# Function to extract a section from a file
# $1: file
# $2: start marker (regex)
# $3: end marker (regex, optional). If not provided, stop at empty line or next header (line starting with ##)
extract_section() {
    local file="$1"
    local start_marker="$2"
    local end_marker="$3"
    if [ ! -f "$file" ]; then
        echo "Unknown"
        return
    fi
    if [ -z "$end_marker" ]; then
        # Stop at empty line or next header
        awk -v start="$start_marker" '
            $0 == start { found=1; next }
            found && /^## / { exit }
            found && /^$/ { exit }
            found { print }
        ' "$file"
    else
        awk -v start="$start_marker" -v end="$end_marker" '
            $0 == start { found=1; next }
            found && $0 == end { exit }
            found { print }
        ' "$file"
    fi
}

# List of projects (directories in projects/)
mapfile -t PROJECTS < <(find "$PROJECTS_DIR" -mindepth 1 -maxdepth 1 -type d -not -path '*/\.*' | sort)

# Write header
> "$OUTPUT_FILE"
echo "# Repository Inventory Context" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Generated from AGENTS.md files in each project." >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "| Project | Tech Stack | Setup Commands | Testing | Code Style | Source Branch | Consolidation Candidate |" >> "$OUTPUT_FILE"
echo "|---------|------------|----------------|---------|------------|---------------|-------------------------|" >> "$OUTPUT_FILE"

# Process each project
for proj_dir in "${PROJECTS[@]}"; do
    proj=$(basename "$proj_dir")
    # echo "Processing $proj..." >&2
    
    # Initialize variables
    tech_stack="Unknown"
    setup_commands="Unknown"
    testing="Unknown"
    code_style="Unknown"
    source_branch="unknown"
    consolidation_candidate="no"
    
    # Extract from AGENTS.md if exists
    if [ -f "$proj_dir/AGENTS.md" ]; then
        # Tech Stack: look for **Tech Stack:** section, if not found, use Project Overview
        tech_stack_raw=$(extract_section "$proj_dir/AGENTS.md" "\*\*Tech Stack:\*\*" "" 2>/dev/null)
        if [ -z "$tech_stack_raw" ]; then
            # Fallback to Project Overview
            tech_stack_raw=$(extract_section "$proj_dir/AGENTS.md" "## Project Overview" "##" 2>/dev/null)
        fi
        # Clean up: remove the marker line if it's included (our extract_section doesn't include the start marker)
        # But we might have empty lines at the start/end, we'll trim.
        tech_stack=$(echo "$tech_stack_raw" | sed -z 's/\n/<br>/g;s/<br>$//' | sed 's/^<br>//')
        
        # Setup Commands
        setup_commands_raw=$(extract_section "$proj_dir/AGENTS.md" "## Setup Commands" "```" 2>/dev/null)
        setup_commands=$(echo "$setup_commands_raw" | sed -z 's/\n/<br>/g;s/<br>$//' | sed 's/^<br>//')
        
        # Testing Instructions
        testing_raw=$(extract_section "$proj_dir/AGENTS.md" "## Testing Instructions" "```" 2>/dev/null)
        testing=$(echo "$testing_raw" | sed -z 's/\n/<br>/g;s/<br>$//' | sed 's/^<br>//')
        
        # Code Style
        code_style_raw=$(extract_section "$proj_dir/AGENTS.md" "## Code Style" "##" 2>/dev/null)
        code_style=$(echo "$code_style_raw" | sed -z 's/\n/<br>/g;s/<br>$//' | sed 's/^<br>//')
    fi
    
    # Determine source branch from git
    if [ -d "$proj_dir/.git" ]; then
        cd "$proj_dir"
        if git show-ref --verify --quiet refs/heads/main; then
            source_branch="main"
        elif git show-ref --verify --quiet refs/heads/master; then
            source_branch="master"
        else
            source_branch="unknown"
        fi
        cd "$BASE_DIR"
    fi
    
    # Determine consolidation candidate: yes if project is comicwise, Django-Scrapy-Selenium, or selenium_webdriver
    if [[ "$proj" == "comicwise" || "$proj" == "Django-Scrapy-Selenium" || "$proj" == "selenium_webdriver" ]]; then
        consolidation_candidate="yes"
    fi
    
    # Write row
    echo "| $proj | $tech_stack | $setup_commands | $testing | $code_style | $source_branch | $consolidation_candidate |" >> "$OUTPUT_FILE"
done

echo "Inventory written to $OUTPUT_FILE"
