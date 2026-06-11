# Audit Detection Edge Cases

**Session:** 2026-05-29 | **Case:** prompts-batch audit over 8 prompt markdown files

## Issue

Phase 1 audit rule **"Check for unbalanced table pipes"** flagged false positives in files where `|` appears in non-table contexts:

- Shell code blocks: `| grep`, `| head`, pipes in bash commands
- YAML frontmatter: `status: draft | review | final` (pipe as separator in YAML value)
- Code examples: `error | fix | next-step` in inline code or comments

**Example false positive:**
```
Line 183:    for script in $(find Bash/ -name '*.sh' -type f | sort); do
Line 196:    | Issue | Action |
Line 197:    |-------|--------|
```

Line 183 has 1 pipe (shell sort), lines 196–197 are actual markdown table lines with balanced pipes. Simple regex `line.count('|') % 2` catches all three.

## Root Cause

Audit phase counts pipes on ANY line containing `|`, without filtering:
1. Code fences (```...```)
2. YAML frontmatter (---)
3. Lines with leading spaces (indented code)

## Mitigation

**For Phase 1 audit (detection):**

Before checking pipe balance, skip:
1. Lines inside ` ``` ` code fences (track state)
2. Lines inside `---` YAML blocks (track state)
3. Lines starting with spaces followed by `|` (likely code indentation, not markdown)

**For Phase 4 verification (false positive resolution):**

When verifying "unbalanced table pipe" issues:
1. First check: does the file contain any valid markdown table separators (`| --- |` or `|-----|`)?
2. If yes: assume the table is valid, mark as ✅ Fixed (issue was likely a false positive from audit)
3. If no: check the specific line number and verify it's actually a table before claiming it's broken

## Recommendation

Update Phase 1.3 (Batch-Reading) audit logic to implement state tracking for code/YAML blocks. This prevents re-flagging the same false positives across future runs.

**Code pattern:**

```python
in_code_fence = False
in_yaml = False
for i, line in enumerate(lines):
    if line.strip().startswith('```'):
        in_code_fence = not in_code_fence
    elif line.strip().startswith('---'):
        in_yaml = not in_yaml
    elif (not in_code_fence and not in_yaml and 
          line.strip().startswith('|') and 
          line.count('|') % 2 != 0):
        # Real unbalanced table pipe detected
```

## Impact

Reduces false positives in Phase 1 audits of markdown files with code blocks. Verification phase (Phase 4) already handles false positives gracefully, so this is a quality-of-life improvement, not a blocking issue.
