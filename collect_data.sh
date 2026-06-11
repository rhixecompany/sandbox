#!/bin/bash
set -e

BASE_DIR="$(pwd)"
PROJECTS_DIR="$BASE_DIR/projects"
OUTPUT_DIR="$BASE_DIR/docs"
OUTPUT_FILE="$OUTPUT_DIR/repo-inventory-context.md"

# Ensure output directory exists
mkdir -p "$OUTPUT_DIR"

# List of projects (exclude research files and rhixecompany-comics? Actually we want all projects under projects/ that are directories and not files)
# We'll take all directories in projects/ that are not the research files (which are files, not directories) and not the consolidation target? 
# But the consolidation target rhixecompany-comics is a directory and should be included in the list? 
# According to the prompt, we scan all 13 projects (excluding the consolidation target). 
# However, for the inventory, we might want to include all projects including the target? 
# The inventory we are making is for all projects under projects/ (including rhixecompany-comics) because we want to document everything.
# Let's include all directories under projects/.
mapfile -t PROJECTS < <(find "$PROJECTS_DIR" -mindepth 1 -maxdepth 1 -type d -not -path '*/\.*' | sort)

# Write header
> "$OUTPUT_FILE"
echo "# Repository Inventory Context" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "Generated from AGENTS.md files in each project." >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"
echo "| Project | Tech Stack | Setup Commands | Testing | Code Style | Source Branch | Consolidation Candidate |" >> "$OUTPUT_FILE"
echo "|---------|------------|----------------|---------|------------|---------------|-------------------------|" >> "$OUTPUT_FILE"

# Function to extract section from AGENTS.md
extract_section() {
    local file="$1"
    local section_start="$2"
    local section_end="$3"  # optional; if empty, extract until empty line or next header
    if [ ! -f "$file" ]; then
        echo "Unknown"
        return
    fi
    # If section_end is provided, we extract between section_start and section_end
    if [ -n "$section_end" ]; then
        awk -v start="$section_start" -v end="$section_end" '
            $0 == start { found=1; next }
            found && $0 == end { exit }
            found { print }
        ' "$file"
    else
        # Extract until empty line or next header (line starting with ##)
        awk -v start="$section_start" '
            $0 == start { found=1; next }
            found && /^## / { exit }
            found && /^$/ { exit }
            found { print }
        ' "$file"
    fi
}

# Process each project
for proj_dir in "${PROJECTS[@]}"; do
    proj=$(basename "$proj_dir")
    echo "Processing $proj..."
    
    # Initialize variables
    tech_stack="Unknown"
    setup_commands="Unknown"
    testing="Unknown"
    code_style="Unknown"
    source_branch="unknown"
    consolidation_candidate="no"
    
    # Extract from AGENTS.md if exists
    if [ -f "$proj_dir/AGENTS.md" ]; then
        # Tech Stack: look for **Tech Stack:** section
        tech_stack=$(extract_section "$proj_dir/AGENTS.md" "**Tech Shell:**" "" 2>/dev/null | sed -z 's/\n/<br>/g;s/<br>$//')
        # If the above didn't work, try alternative pattern
        if [ -z "$tech_stack" ]; then
            tech_stack=$(extract_section "$proj_dir/AGENTS.md" "\*\*Tech Stack:\*\*" "" 2>/dev/null | sed -z 's/\n/<br>/g;s/<br>$//')
        fi
        # Setup Commands
        setup_commands=$(extract_section "$proj_dir/AGENTS.md" "## Setup Commands" "```" 2>/dev/null | sed -z 's/\n/<br>/g;s/<br>$//')
        # Testing Instructions
        testing=$(extract_section "$proj_dir/AGENTS.md" "## Testing Instructions" "```" 2>/dev/null | sed -z 's/\n/<br>/g;s/<br>$//')
        # Code Style
        code_style=$(extract_section "$proj_dir/AGENTS.md" "## Code Style" "##" 2>/dev/null | sed -z 's/\n/<br>/g;s/<br>$//')
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
    
    # Clean up multi-line: replace newlines with <br> and ensure no trailing <br>
    tech_stack=$(echo "$tech_stack" | sed -z 's/\n/<br>/g;s/<br>$//')
    setup_commands=$(echo "$setup_commands" | sed -z 's/\n/<br>/g;s/<br>$//')
    testing=$(echo "$testing" | sed -z 's/\n/<br>/g;s/<br>$//')
    code_style=$(echo "$code_style" | sed -z 's/\n/<br>/g;s/<br>$//')
    
    # Escape pipes in content? Not needed if we don't have pipes in the extracted text.
    # Write row
    echo "| $proj | $tech_stack | $setup_commands | $testing | $code_style | $source_branch | $consolidation_candidate |" >> "$OUTPUT_FILE"
done

echo "Inventory written to $OUTPUT_FILE"
