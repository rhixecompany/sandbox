# Copilot-Style Frontmatter Merge Pattern

> Reference for handling mixed-format prompt libraries (Hermes + Copilot imports).

## Problem

Prompt files imported from GitHub Copilot or other platforms often have:
- CRLF line endings (`\r\n`)
- Non-standard frontmatter starting with `toolsets:` instead of `name:`
- VS Code extension-style tool identifiers (`github.vscode-pull-request-github/issue_fetch`)
- No `name:`, `version:`, `author:`, or `license:` fields

Running a standard Hermes fix script on these files causes:
1. **Duplicate frontmatter blocks** — CRLF `---\r\n` isn't recognized as valid frontmatter, so a second `---` block is prepended
2. **Missing required fields** — Copilot files lack `name:`, `version:`, etc.
3. **Large frontmatter gap** — 60+ lines of `toolsets:` entries between `---` delimiters

## The 3-Script Cascade Pattern

### Script 1: Comprehensive Fix (`fix_prompts_comprehensive.py`)
- Handles: Python-list tags → YAML, empty tags → inference, missing fields, dep standardization
- **Must** check `content.startswith('---\n') or content.startswith('---\r\n')` in `has_yaml_frontmatter()`
- **Must** open files in binary mode (`'rb'`) and normalize CRLF→LF before parsing
- Output: All files get proper Hermes frontmatter, but CRLF files may get duplicate blocks

### Script 2: Duplicate Frontmatter Cleanup (`fix_crlf_frontmatter.py`)
- Detects files with multiple `---` blocks where gap < 60 lines
- Removes the second (duplicate) block, keeps the first
- Adds missing `name:`/`version:` to the surviving block
- **Limitation**: Fails on Copilot files where gap > 60 lines (large `toolsets:` lists)

### Script 3: Copilot Frontmatter Merge (`fix_copilot_frontmatter.py`)
- Targets specific files that still have issues after Script 2
- Finds the LAST `---` block (the one with `name:` added by Script 1)
- Merges non-standard fields from the first block (e.g. `toolsets:`) into the clean block
- Produces a single unified frontmatter with LF line endings

## Detection Heuristic

```python
def needs_copilot_fix(filepath):
    with open(filepath, 'rb') as f:
        raw = f.read()
    content = raw.replace(b'\r\n', b'\n').decode('utf-8')
    lines = content.split('\n')
    dashes = [i for i, line in enumerate(lines[:200]) if line.strip() == '---']
    return len(dashes) >= 2
```

## Key Edge Cases

1. **Multi-line `tools:` format** — Copilot prompts write `tools:\n  [\n    "item1",\n  ]`. The fix script's `get_field()` only reads the first line (returns `""`), leaving an orphaned `[` block.
2. **Duplicate `toolsets:` entries** — `github/*` often appears twice in Copilot tool lists
3. **Body content after second `---`** — When removing duplicate blocks, ensure body text after the second `---` is preserved, not the body after the first
4. **Horizontal rules in body** — `---` in body text (markdown HR) can be mistaken for frontmatter delimiters. Only treat as frontmatter if within first 200 lines AND followed by YAML-like key-value pairs.

## Post-Fix Verification

```python
import glob
missing = {'name': 0, 'version': 0, 'author': 0, 'license': 0, 'tags': 0}
for f in glob.glob('*.prompt.md'):
    with open(f, 'r') as fh:
        content = fh.read()
    assert content.startswith('---'), f"Missing frontmatter: {f}"
    end = content.find('---', 3)
    fm = content[3:end]
    for field in missing:
        assert f'{field}:' in fm, f"Missing {field}: {f}"
```
