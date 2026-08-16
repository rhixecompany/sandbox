#!/usr/bin/env python3
"""
Patch ~/AppData/Local/hermes/scripts/fix_prompts.py to add
deduplication of duplicate `tags:` lines after fix_tags_format().

Usage:
    python scripts/patch_fix_prompts_dedup_tags.py

This adds a _dedup_tags() function and calls it after fix_tags_format().
"""
import sys

TARGET = r"~/AppData/Local/hermes/scripts/fix_prompts.py"

# The _dedup_tags function to insert
DEDUP_FUNC = """
def _dedup_tags(fm_lines, filepath):
    \"\"\"Remove duplicate `tags:` lines in frontmatter, keeping the last occurrence.\"\"\"
    tags_indices = [i for i, l in enumerate(fm_lines) if l.startswith('tags:')]
    if len(tags_indices) > 1:
        # Keep only the last tags: line
        for idx in reversed(tags_indices[:-1]):
            del fm_lines[idx]
        print(f\"  deduped tags: in {filepath}\")
    return fm_lines
"""

# The call to insert after fix_tags_format returns
HOOK = "        fm_lines = _dedup_tags(fm_lines, filepath)"

def main():
    with open(TARGET) as f:
        content = f.read()
    
    # Insert dedup function before main() or the last function
    if "_dedup_tags" in content:
        print("Already patched.")
        return
    
    # Insert the function
    content = content.replace(
        "def main():", 
        DEDUP_FUNC + "\n\ndef main():"
    )
    
    # Insert the call after fix_tags_format completes
    content = content.replace(
        "fm_lines = fix_tags_format(fm_lines, filepath)",
        "fm_lines = fix_tags_format(fm_lines, filepath)\n        fm_lines = _dedup_tags(fm_lines, filepath)"
    )
    
    with open(TARGET, 'w') as f:
        f.write(content)
    
    print(f"Patched {TARGET} with _dedup_tags()")

if __name__ == "__main__":
    main()
