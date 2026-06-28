# Heading Hierarchy Validation Algorithm

## Problem

Simple pattern matching cannot detect heading hierarchy violations. A line like:

```markdown
### Heading
```

Is **correct** after `## Subheading` (level 3 after 2 = +1, valid) but **wrong** after `# Title` (level 3 after 1 = +2, invalid skip).

## Validation Rule

A heading is valid if its level ≤ (previous heading level + 1).

```
previous level = 1 → next level can be 1 or 2 ✅
previous level = 2 → next level can be 1, 2, or 3 ✅
previous level = 3 → next level can be 1, 2, 3, or 4 ✅
previous level = 2 → next level is 4 ❌ (skip of 2)
```

## Algorithm

```python
def validate_heading_hierarchy(content):
    lines = content.split('\n')
    issues = []
    prev_level = 0
    
    for line_num, line in enumerate(lines, start=1):
        # Check if line is a heading
        match = re.match(r'^(#{1,6})\s+', line)
        if not match:
            continue
        
        curr_level = len(match.group(1))
        
        # Check hierarchy
        if curr_level > prev_level + 1:
            issues.append({
                'line': line_num,
                'current_level': curr_level,
                'previous_level': prev_level,
                'message': f'Heading level skip: #{prev_level} → #{curr_level} at line {line_num}'
            })
        
        prev_level = curr_level
    
    return issues
```

## Python Implementation (Hermes/Phase 1 reusable)

```python
import re

def find_heading_hierarchy_issues(filepath):
    """Scan a markdown file for heading hierarchy violations."""
    try:
        content = open(filepath, 'r', encoding='utf-8').read()
    except Exception as e:
        return {'error': str(e), 'issues': []}
    
    lines = content.split('\n')
    issues = []
    prev_level = 0
    
    for line_num, line in enumerate(lines, start=1):
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if not m:
            continue
        
        curr_level = len(m.group(1))
        heading_text = m.group(2)
        
        # Validate: next level should not skip more than 1
        if curr_level > prev_level + 1:
            issues.append({
                'id': f'{filepath.split("/")[-1]}-H{line_num}',
                'line': line_num,
                'heading': heading_text,
                'violation': f'Level {curr_level} after {prev_level} (skip of {curr_level - prev_level})',
                'fix': f'Change {"#" * curr_level} to {"#" * (prev_level + 1)}'
            })
        
        prev_level = curr_level
    
    return {
        'filepath': filepath,
        'total_headings': len([l for l in lines if re.match(r'^#{1,6}\s+', l)]),
        'issues': issues
    }


# Usage in Phase 1
from pathlib import Path

target_files = [...]  # from file inventory
for fpath in target_files:
    result = find_heading_hierarchy_issues(str(fpath))
    if result['issues']:
        print(f"❌ {fpath}: {len(result['issues'])} issue(s)")
        for issue in result['issues']:
            print(f"   Line {issue['line']}: {issue['violation']}")
            print(f"   → {issue['fix']}")
```

## Session Example: github-prompts-batch (2026-05-29)

### Broken Example (before fix)

File: `breakdown-plan.prompt.md`
Line 182:

```markdown
## Overview
...
### Subsection 1
...
#### Deep subsection  ← Current level 4
...
#### Should be level 3 here, not 4
```

**Detection:**
- Previous heading (line ~170): `## Overview` → level 2
- Current heading (line 182): `#### Deep subsection` → level 4
- Violation: 4 > (2 + 1) → **skip of 2, invalid**

**Fix applied:** `#### Deep subsection` → `### Deep subsection`

**Verification:** After fix, level 3 ≤ (2 + 1) → ✅ valid

### Correct Example (after fix)

File: `create-tldr-page.prompt.md`
Line 149:

Before fix:
```markdown
# Main Title
...
### Subsection  ← Level 3 after 1: skip of 2, INVALID
```

After fix (applied by Phase 2):
```markdown
# Main Title
...
## Subsection  ← Level 2 after 1: +1, VALID
```

## Edge Cases

### Case 1: Multiple consecutive deep jumps

```markdown
# Title
## Subheading
#### Too deep
```

Algorithm detects the jump from 2 → 4. Only ONE issue (the jump). No need to report the Title/Subheading as wrong.

### Case 2: Heading after code block

The regex `^#{1,6}\s+` matches only if `#` is at column 0 (start of line). Code blocks with heading-like syntax are not matched:

```markdown
# Title

## Subheading

\`\`\`
# This is not a heading
# This is code
\`\`\`

### Next real heading (level 3 after 2: OK)
```

No false positive on the lines inside the code block.

### Case 3: Setext-style headings (underline style)

```markdown
Title
=====

Subtitle
--------
```

This algorithm only detects ATX-style (`# Title`), not setext-style. Markdown allows both. If the file mixes styles, you'll need a separate regex:

```python
# Setext detection (optional)
setext_h1 = re.match(r'^=+$', line)
setext_h2 = re.match(r'^-+$', line)
```

For consistency in audit, recommend converting all setext to ATX (e.g., `=====` → `#`) in Phase 2 as a bonus cleanup.

## Integration into enhance-markdown Workflow

### Phase 1 — Audit

Use `find_heading_hierarchy_issues()` for every file in the batch. Report all issues with line numbers and violations. Severity: `Major` (or `Minor` if the file is a stub with few headings).

### Phase 2 — Fix

For each issue:

```python
issue = {'line': 182, 'current_level': 4, 'previous_level': 2}
fix = f"Change #### to {'#' * (issue['previous_level'] + 1)}"  # → "Change #### to ###"

# Apply fix via patch
old_line = lines[issue['line'] - 1]  # 1-indexed → 0-indexed
new_line = re.sub(r'^#{2,6}\s+', ('# ' * (issue['previous_level'] + 1)) + ' ', old_line)
# or more robustly:
new_line = '#' * (issue['previous_level'] + 1) + ' ' + re.sub(r'^#{1,6}\s+', '', old_line)
```

### Phase 4 — Verify

Re-run `find_heading_hierarchy_issues()` on the modified file. Assert `issues == []` (no violations).

## Testing

Minimal test case:

```python
test_content = """# Title
## Subheading
#### Invalid (skip of 2)
### Valid
"""

issues = find_heading_hierarchy_issues_from_string(test_content)
assert len(issues) == 1
assert issues[0]['line'] == 3
assert issues[0]['violation'] == 'Level 4 after 2 (skip of 2)'
```

## References

- **Discovered in:** Session 2026-05-29, github-prompts-batch Phase 1 audit. 6 files had heading hierarchy violations (5 with `### → ##` fix, 1 with `#### → ###`). All violations were level skips of 2+ (invalid). Corrected by applying the algorithm above in Phase 3.
- **Related pitfall:** See enhance-markdown SKILL.md, "Pitfall — Heading hierarchy detection requires context"
