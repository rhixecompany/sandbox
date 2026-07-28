#!/usr/bin/env python3
"""
Repair unparseable YAML frontmatter in prompt files.
Handles: unquoted description/title containing ': ' (colon-space) etc.
"""
import re, yaml
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")

def repair_frontmatter(text):
    """Try to fix common YAML frontmatter issues and re-parse."""
    # Find frontmatter boundaries
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not m:
        return text  # Can't find frontmatter at all
    
    raw_fm = m.group(1)
    
    # Try parsing
    try:
        yaml.safe_load(raw_fm)
        return text  # Already valid
    except yaml.YAMLError:
        pass
    
    # Fix 1: Quote description values that contain ': '
    # Pattern: description: (unquoted text with : in it) followed by newline+key or ---
    lines = raw_fm.split('\n')
    fixed_lines = []
    in_multiline = False
    current_value = []
    
    for line in lines:
        if in_multiline:
            if line.strip() and line[0] == ' ':
                current_value.append(line)
                continue
            else:
                # End of multi-line value — join and check
                in_multiline = False
        
        # Check if this line starts a YAML key
        if ':' in line and not line.startswith(' ') and not line.startswith('- '):
            key, _, value = line.partition(':')
            key = key.strip()
            value = value.strip()
            
            if value and not value.startswith(("'", '"', '[', '{', '>', '|')):
                # Check if value needs quoting (contains ': ', '#', etc.)
                if ': ' in value or value.startswith('*'):
                    # Quote it
                    fixed_lines.append(f"{key}: \"{value}\"")
                    continue
                elif value in ('',):
                    # Empty -> preserve
                    fixed_lines.append(f"{key}: {value}")
                    continue
        
        fixed_lines.append(line)
    
    repaired = '\n'.join(fixed_lines)
    
    # Verify
    try:
        yaml.safe_load(repaired)
        # Build final text with repaired frontmatter
        return f"---\n{repaired}\n---{text[m.end():]}"
    except yaml.YAMLError as e:
        print(f"Still broken after simple fix: {e}")
        return text

def main():
    prompt_files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
    fixed = 0
    for pf in prompt_files:
        original = pf.read_text(encoding="utf-8")
        repaired = repair_frontmatter(original)
        if repaired != original:
            pf.write_text(repaired, encoding="utf-8")
            print(f"Fixed: {pf.name}")
            fixed += 1
    
    print(f"\nFixed {fixed} files")

if __name__ == "__main__":
    main()
