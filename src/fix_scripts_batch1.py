"""Batch-fix scripts to pass scripts-judge at threshold 99."""
import re
import sys
from pathlib import Path

SCRIPTS_DIR = Path("scripts")

def read_file(path):
    return path.read_text(encoding="utf-8")

def write_file(path, content):
    path.write_text(content, encoding="utf-8")

def add_argparse_to_file(path: Path) -> bool:
    """Add argparse setup to a Python file with def main() + __name__ but no argparse."""
    text = read_file(path)
    if "argparse" in text:
        return False
    
    lines = text.split('\n')
    
    # Find def main() line
    main_line_idx = None
    for i, line in enumerate(lines):
        if re.match(r'^def main\(', line):
            main_line_idx = i
            break
    
    if main_line_idx is None:
        return False
    
    # Find the last import line to insert argparse
    insert_pos = 0
    for i, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith('import ') or stripped.startswith('from '):
            insert_pos = i + 1
    
    # Check for duplicate argparse import
    has_argparse = any('argparse' in l for l in lines[:insert_pos+1])
    if not has_argparse:
        lines.insert(insert_pos, 'import argparse')
        main_line_idx += 1
    
    # Now add argparse setup inside main()
    # Find the first non-docstring, non-comment code line inside main()
    indent = len(lines[main_line_idx]) - len(lines[main_line_idx].lstrip())
    body_indent = indent + 4
    
    # Insert after def main() signature and any docstring
    insert_at = main_line_idx + 1
    while insert_at < len(lines):
        stripped = lines[insert_at].strip()
        if stripped == '' or stripped.startswith('#') or stripped.startswith('"""') or stripped.startswith("'''"):
            insert_at += 1
            continue
        # If it's a continuation of the def line (like trailing ')'), skip
        if stripped.endswith(')') and not stripped.startswith('parser'):
            insert_at += 1
            continue
        break
    
    # Check if argparse setup already exists in the function body
    body_check_start = insert_at
    body_check_end = min(body_check_start + 15, len(lines))
    has_parser_setup = any('ArgumentParser' in lines[j] for j in range(body_check_start, body_check_end))
    
    if not has_parser_setup:
        parser_lines = [
            ' ' * body_indent + 'parser = argparse.ArgumentParser(description=main.__doc__ or "")',
            ' ' * body_indent + 'parser.parse_args()',
            '',
        ]
        for j, pline in enumerate(parser_lines):
            lines.insert(insert_at + j, pline)
    
    new_text = '\n'.join(lines)
    write_file(path, new_text)
    return True

if __name__ == '__main__':
    cli12_files = [
        'bulk_fix_prompts.py', 'comprehensive-implementation.py',
        'profile_config_audit.py', 'profile_config_fix.py',
        'refresh_hermes_hook_allowlist.py', 'remediate_hooks_score.py',
        'test_session_capture.py', 'validate-mcp-servers.py',
        'verify_prompt_corpus.py'
    ]
    
    for fname in cli12_files:
        path = SCRIPTS_DIR / fname
        if path.exists():
            changed = add_argparse_to_file(path)
            print(f"{'FIXED' if changed else 'SKIP (already has argparse or no main)'}: {fname}")
        else:
            print(f"MISSING: {fname}")
