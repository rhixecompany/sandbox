#!/usr/bin/env python3
"""
Repair stubborn YAML frontmatter: 
- Unescaped internal double quotes in double-quoted values
- Unquoted values containing ': ' (mapping indicators)
"""
import re, yaml
from pathlib import Path

PROMPTS_DIR = Path(r"C:\Users\Alexa\Desktop\SandBox\.github\prompts")

def repair_frontmatter_text(raw_fm):
    """Apply multiple fix strategies to repair YAML frontmatter."""
    
    # Strategy 1: Handle double-quoted values with unescaped internal quotes
    # Pattern: key: "text with "internal" quotes" more text"
    # Fix: replace with single-quoted or escaped version
    lines = raw_fm.split('\n')
    fixed_lines = []
    
    for line in lines:
        # Skip indented list items and dicts
        if line.startswith(' ') or line.startswith('- '):
            fixed_lines.append(line)
            continue
        
        # Check for key: "value" pattern
        m = re.match(r'^(\w[\w_-]*):\s*(")(.*)', line)
        if m:
            key = m.group(1)
            rest = m.group(3)
            
            # Find the closing quote that properly ends the YAML string
            # (i.e., last double quote in the line, unless followed by more content)
            # Or if the value itself contains internal quotes, we need to escape them
            
            # Check if value ends with a lone closing quote
            if rest.endswith('"') and rest.count('"') % 2 == 1:
                # Properly quoted — check for internal issues
                inner = rest[:-1]  # Remove closing quote
                # Check for unescaped internal quotes
                if '"' in inner:
                    # Need to: change to block scalar or escape internal quotes
                    # Use single quotes if no single quotes inside
                    if "'" not in inner:
                        fixed_lines.append(f"{key}: '{inner}'")
                    else:
                        # Escape the internal double quotes
                        escaped = inner.replace('"', '\\"')
                        fixed_lines.append(f'{key}: "{escaped}"')
                    continue
                else:
                    fixed_lines.append(line)
                    continue
            else:
                # Could be a longer value spanning multiple lines or ending at ---
                pass
        
        # Strategy 2: Unquoted values containing ': ' (mapping indicator)
        m2 = re.match(r'^(\w[\w_-]*):\s+(.*)', line)
        if m2:
            key = m2.group(1)
            value = m2.group(2)
            if value and not value.startswith(("'", '"', '[', '{', '>', '|', '- ')):
                if ': ' in value:
                    # Need quoting
                    if "'" not in value:
                        fixed_lines.append(f"{key}: '{value}'")
                    else:
                        fixed_lines.append(f'{key}: "{value}"')
                    continue
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines)


def repair_file(path, dry_run=False):
    """Repair YAML frontmatter in a file."""
    original = path.read_text(encoding="utf-8")
    text = original
    
    # Extract frontmatter
    m = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not m:
        # Try with ... closer
        m = re.match(r'^---\s*\n(.*?)\n\.\.\.', text, re.DOTALL)
    if not m:
        return False
    
    raw_fm = m.group(1)
    
    # Try parsing
    try:
        yaml.safe_load(raw_fm)
        return False  # Already valid
    except yaml.YAMLError:
        pass
    
    # Apply repairs
    repaired = repair_frontmatter_text(raw_fm)
    
    # Verify
    try:
        yaml.safe_load(repaired)
    except yaml.YAMLError as e:
        print(f"  Still broken after fix for {path.name}: {e}")
        print(f"  Repaired (first 300): {repaired[:300]}")
        return False
    
    if not dry_run:
        # Replace frontmatter in file
        new_text = f"---\n{repaired}\n---{text[m.end():]}"
        path.write_text(new_text, encoding="utf-8")
        print(f"  Fixed: {path.name}")
    else:
        print(f"  Would fix: {path.name}")
    
    return True


def main():
    import sys
    dry_run = "--dry-run" in sys.argv
    
    prompt_files = sorted(PROMPTS_DIR.glob("*.prompt.md"))
    fixed = 0
    still_broken = []
    
    for pf in prompt_files:
        if repair_file(pf, dry_run):
            fixed += 1
    
    # Final check
    broken = []
    for pf in prompt_files:
        m = re.match(r'^---\s*\n(.*?)\n---', pf.read_text(encoding="utf-8"), re.DOTALL)
        if m:
            try:
                yaml.safe_load(m.group(1))
            except yaml.YAMLError:
                broken.append(pf.name)
    
    print(f"\nFixed: {fixed} files")
    if broken:
        print(f"Still broken: {broken}")
    else:
        print("All files now have valid YAML frontmatter!")

if __name__ == "__main__":
    main()
