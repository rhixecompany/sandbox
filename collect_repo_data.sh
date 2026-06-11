#!/bin/bash
# Script to collect per-repo research data for the repo prompt Phase 1a

OUTPUT_FILE="docs/per-repo-research-summary.md"

# Clear the file and write header
> "$OUTPUT_FILE"
echo "# Per-Repo Research Summary" >> "$OUTPUT_FILE"
echo "" >> "$OUTPUT_FILE"

# List of projects (directories in projects/ that are not files)
for dir in projects/*/; do
    # Remove trailing slash and get the directory name
    proj=$(basename "$dir")
    
    echo "Processing $proj..."
    
    # Start a new section for the project
    echo "## $proj" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
    
    # 1. AGENTS.md Summary: We'll take the first few lines after the title until the next header or a blank line?
    # Instead, let's extract the "Project Overview" section if exists, else the first paragraph.
    if [ -f "projects/$proj/AGENTS.md" ]; then
        # Extract the section between "## Project Overview" and the next "##"
        awk '/^## Project Overview$/,/^## / { if (!/^## Project Overview$/ && !/^## /) print }' "projects/$proj/AGENTS.md" >> "$OUTPUT_FILE" 2>/dev/null
        # If that didn't work, try to get the first non-empty lines after the title
        if [ ! -s "$OUTPUT_FILE" ]; then
            # Fallback: get the first 5 lines after the title (skip the title and the next line if it's a separator)
            sed -n '/^# /,/^## /p' "projects/$proj/AGENTS.md" | sed '1d;$d' | head -5 >> "$OUTPUT_FILE" 2>/dev/null
        fi
        echo "" >> "$OUTPUT_FILE"
    else
        echo "AGENTS.md not found." >> "$OUTPUT_FILE"
        echo "" >> "$OUTPUT_FILE"
    fi
    
    # 2. Tech Stack: We'll try to get the Tech Stack section from AGENTS.md
    echo "**Tech Stack**:" >> "$OUTPUT_FILE"
    if [ -f "projects/$proj/AGENTS.md" ]; then
        # Extract the Tech Stack section
        awk '/^\*\*Tech Stack:\*\*$/,/^$/ { if (!/^\*\*Tech Stack:\*\*$/) print }' "projects/$proj/AGENTS.md" >> "$OUTPUT_FILE" 2>/dev/null
        # If that didn't work, try to get the lines after the Tech Stack header until an empty line or next header
        if [ ! -s "$OUTPUT_FILE" ]; then
            # We'll just note that we couldn't extract it automatically
            echo "See AGENTS.md for details." >> "$OUTPUT_FILE"
        fi
    else
        echo "Unknown" >> "$OUTPUT_FILE"
    fi
    echo "" >> "$OUTPUT_FILE"
    
    # 3. Git branch state
    echo "**Git Branch State**:" >> "$OUTPUT_FILE"
    if [ -d "projects/$proj/.git" ]; then
        cd "projects/$proj"
        local_branches=$(git branch | sed 's/^..//' | tr '\n' ' ' | sed 's/ $//')
        remote_branches=$(git branch -r | sed 's/^..//' | grep -v HEAD | tr '\n' ' ' | sed 's/ $//')
        cd ../..
        echo "Local: $local_branches" >> "$OUTPUT_FILE"
        echo "Remote: $remote_branches" >> "$OUTPUT_FILE"
    else
        echo "Not a git repository" >> "$OUTPUT_FILE"
    fi
    echo "" >> "$OUTPUT_FILE"
    
    # 4. GitHub remote URL
    echo "**GitHub Remote URL**:" >> "$OUTPUT_FILE"
    if [ -d "projects/$proj/.git" ]; then
        cd "projects/$proj"
        remote_url=$(git remote get-url origin 2>/dev/null)
        cd ../..
        if [ -n "$remote_url" ]; then
            echo "$remote_url" >> "$OUTPUT_FILE"
        else
            echo "No remote URL found" >> "$OUTPUT_FILE"
        fi
    else
        echo "N/A" >> "$OUTPUT_FILE"
    fi
    echo "" >> "$OUTPUT_FILE"
    
    # 5. .*ignore file inventory
    echo "**.*ignore Files**:" >> "$OUTPUT_FILE"
    if [ -d "projects/$proj" ]; then
        cd "projects/$proj"
        for ignore in .gitignore .dockerignore .prettierignore .eslintignore .npmignore; do
            if [ -f "$ignore" ]; then
                # Get a brief description: first line or a note
                first_line=$(head -1 "$ignore")
                echo "- $ignore: $first_line" >> "$OUTPUT_FILE"
            else
                echo "- $ignore: not present" >> "$OUTPUT_FILE"
            fi
        done
        cd ..
    else
        echo "N/A" >> "$OUTPUT_FILE"
    fi
    echo "" >> "$OUTPUT_FILE"
    
    # 6. RESEARCH_* Files
    echo "**RESEARCH_* Files**:" >> "$OUTPUT_FILE"
    if [ -d "projects/$proj" ]; then
        cd "projects/$proj"
        research_files=$(find . -maxdepth 1 -type f \( -name 'RESEARCH_*.md' -o -name '*_RESEARCH.md' \) 2>/dev/null)
        if [ -n "$research_files" ]; then
            echo "$research_files" >> "$OUTPUT_FILE"
        else
            echo "None" >> "$OUTPUT_FILE"
        fi
        cd ..
    else
        echo "N/A" >> "$OUTPUT_FILE"
    fi
    echo "" >> "$OUTPUT_FILE"
    
    # 7. Consolidation/Cleanup Notes
    echo "**Consolidation/Cleanup Notes**:" >> "$OUTPUT_FILE"
    # We know from the prompt that the consolidation target is rhixecompany-comics (which is the merge of comicwise, Django-Scrapy-Selenium, selenium_webdriver)
    if [ "$proj" = "rhixecompany-comics" ]; then
        echo "Consolidation target: merging comicwise (frontend), Django-Scrapy-Selenium (backend scaffold), and selenium_webdriver (scraper)." >> "$OUTPUT_FILE"
    elif [ "$proj" = "comicwise" ] || [ "$proj" = "Django-Scrapy-Selenium" ] || [ "$proj" = "selenium_webdriver" ]; then
        echo "Part of the consolidation target rhixecompany-comics. Will be merged into the monolith." >> "$OUTPUT_FILE"
    else
        echo "No consolidation planned. Standard cleanup: normalize branches, audit ignore files, optimize dependencies, migrate to bun (if JS/TS), validate CI workflows." >> "$OUTPUT_FILE"
    fi
    echo "" >> "$OUTPUT_FILE"
    echo "--" >> "$OUTPUT_FILE"
    echo "" >> "$OUTPUT_FILE"
done

echo "Per-repo research summary written to $OUTPUT_FILE"
