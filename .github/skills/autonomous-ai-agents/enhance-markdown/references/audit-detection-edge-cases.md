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

---

## Additional Edge Cases (Session: 2026-06-20)

### 1. Frontmatter Fence Count False Positive

**Trigger:** Audit rule "double frontmatter fences" counting `---` occurrences in first N lines.

**False Positive Pattern:** Markdown table separator rows (`--- | --- | ---`) inside the first 60 lines are counted as additional frontmatter fences.

**Example:**
```markdown
---          # Line 1: frontmatter open
skills:
  - foo
---          # Line 5: frontmatter close (actual count = 2)

## Skills Required

| Skill | Purpose |
|---|---|        # Line 10: table header
| --- | --- |   # Line 11: table separator - FALSE POSITIVE
```

**Audit Result:** Reports 4 fences in first 60 lines (2 real + 2 table separators)

**Fix:** Distinguish frontmatter fences (standalone `---` on line) from table separators (`--- | ---` or `| --- |` pattern). Only count lines matching `^---$` exactly.

```python
# Correct: count only standalone fences
fm_fences = sum(1 for line in lines[:60] if line.strip() == '---')
```

---

### 2. Cross-Table Regex Contamination

**Trigger:** Regex `\|\s*\`([^`]+)\`\s+\|` for extracting skills from tables.

**False Positive Pattern:** Regex matches backtick-wrapped identifiers in ANY table, not just the "Skills Required" table.

**Example:**
```markdown
## Skills Required           # Correct table (3 skills)
| Skill | Purpose |
| `using-superpowers` | ... |

## Free Models Identified    # Different table (7 models)
| Provider | Model | Context Window |
| OpenRouter | `openrouter/elephant-alpha` | 128K |
```

**Audit Result:** Reports 10 skills (3 real + 7 model names from free models table)

**Fix:** Scope regex to the specific table section. Use heading-anchored extraction:

```python
# Find Skills Required table only
skills_section = re.search(r'## Skills Required\n\n((?:\|.*\|\n)+)', content)
if skills_section:
    table_skills = re.findall(r'\|\s*`([^`]+)`\s+\|', skills_section.group(1))
```

---

### 3. Windows Path Detection in Cross-Platform Prompts

**Trigger:** Audit flagging hardcoded Windows paths (`C:\Users\...`).

**Context:** Legitimate in Windows-specific docs, but problematic in cross-platform prompt files meant to run on any OS.

**Mitigation:** Normalize to `~/AppData/Local/...` or `$HERMES_HOME/...` in prompt files. Flag only if path is in a prompt file (`.prompt.md`, `.prompt.txt`), not in OS-specific documentation.

---

### 4. YAML Comment Indentation (False H1 Heading)

**Session:** 2026-06-21 | **Case:** enhance-markdown on sync-hermes-copilot-codex.prompt.md

**Trigger:** Regex `^# ` (H1 heading detection) counting YAML comments at column 0 as markdown H1 headings.

**False Positive Pattern:** A YAML comment (`# comment`) placed at column 0 inside the YAML frontmatter block is matched by `re.findall(r'^# ', content, re.MULTILINE)` as an H1 heading. This is valid YAML but creates a false positive in heading hierarchy checks.

**Example:**
```yaml
---
tags:
  - foo
  - bar
# Copilot-format deps      # <-- line 7: "Copilot-format deps" counted as H1
dependencies:
  - skill:baz
---
```

**Audit Result:** Reports 2 H1 headings (1 real title + 1 YAML comment)

**Fix:** Either:
- Indent YAML comments to match their block level (`  # comment` instead of `# comment`)
- Or use trailing inline comments (`  - foo  # comment`)
- In verification scripts, filter out lines 1-30 (frontmatter zone) from H1 counting

**Detection in verification:**
```python
h1_matches = [(i+1, l) for i, l in enumerate(lines) if re.match(r'^# ', l)]
# Filter out lines inside frontmatter (first 30 lines should cover YAML)
real_h1 = [(ln, text) for ln, text in h1_matches
           if not (1 <= ln <= 30 and text.strip().startswith('# '))]
yaml_h1 = [ln for ln, text in h1_matches if text.strip().startswith('# ')
           and 1 <= ln <= 30]
```

---

### 5. Flow-Sequence YAML Tags (Valid but Inconsistent)

---

### 6. Merged YAML Closing Fence (`|---` Followed by Content)

**Session:** 2026-06-22 | **Case:** enhance-markdown --folder .github/prompts/

**Issue:** Audit scanning for frontmatter boundaries checks for standalone `---` delimiters. Some prompt files have the closing `---` merged with the following content on the same line (e.g., `|---## Goal` instead of `---\\n\\n## Goal`).

**Pattern:**
```yaml
---
name: "example"
description: "Some description"
|---## Goal          # <-- closing --- merged with content
Use when "Some description" to accomplish the associated tasks and objectives.
```

**Detection:** The merged `---` is not detected as a frontmatter boundary by `line.strip() == "---"` checks. The YAML parser (`yaml.safe_load`) may also fail or silently truncate depending on the parser.

**Prevalence (this session):** 3 out of 215 prompts had this pattern (code-review.prompt.md, testing.prompt.md, documentation.prompt.md).

**Mitigation:**

**For Phase 1 audit:** After detecting an opening `---`, scan for BOTH:
- Standalone `---` (line.strip() == "---")
- Merged `---` pattern: a line containing `|` followed by `---` then non-whitespace content

```python
# Detect both standalone and merged closing fences
def find_closing_fence(lines, start=1):
    for i in range(start, len(lines)):
        stripped = lines[i].strip()
        if stripped == "---":
            return i, "standalone"
        # Also catch "|---some heading" pattern
        if "|--" in stripped and stripped.count("---") == 1:
            idx = stripped.find("---")
            after = stripped[idx+3:].strip()
            if after and not after.startswith(" "):
                return i, "merged"
    return None, None
```

**Fix:** Split the merged line:
1. Insert `---` at the merge point
2. Add a blank line
3. Put the remaining content on its own line

```patch
- |---## Goal
+ ---
+
+ ## Goal
```

**Verification:** After fixing, `yaml.safe_load` should parse the frontmatter as a single document with valid YAML. The file should have exactly 2 standalone `---` fences in the first N lines.

---

### 7. Table Separator Confused with Frontmatter Fence (Reinforcement)

Already covered in Section 1 (Frontmatter Fence Count False Positive). The fix there — only count lines matching `^---$` exactly — also catches merged-closing fences, but only if they've already been separated. For raw detection, add the merged-pattern check above before applying the `^---$` filter.

---

### 8. Non-YAML Prompt Files in Batch Audits

**Session:** 2026-06-22 | **Case:** enhance-markdown --folder .github/prompts/

**Context:** Out of 215 prompt files scanned, 170 (79%) lacked YAML frontmatter. These are community/Copilot-format prompts that start directly with markdown content, not `---`.

**Audit behavior:** These files are skipped by Phase 1's YAML-frontmatter-dependent checks but should not be flagged as errors — they're a valid format variant.

**Mitigation:**
- In audit reports, separate counts into "with YAML" vs "without YAML"
- Do not flag missing frontmatter as an error for `.prompt.md` files (some ecosystems don't use it)
- When extracting skills/dependencies, only check files that have YAML frontmatter

**Session:** 2026-06-21 | **Case:** enhance-markdown on sync-hermes-copilot-codex.prompt.md

**Trigger:** Audit flagging unconventional YAML formatting in frontmatter.

**False Positive Pattern:** YAML flow sequences (`[...]`) are valid YAML but visually inconsistent when mixed with block-style lists (`- item`) in the same frontmatter block. Not a functional error but a style concern.

**Example:**
```yaml
tags:
  [
    hermes,
    copilot,
    opencode,
  ]
skills:
  - using-superpowers         # block-style list — inconsistent
  - user-communication-preferences
```

**Why it's valid:** YAML allows flow sequences in block mapping context. A `[` starts the flow sequence, each item on its own line (or same line), and `]` closes it. This is NOT a YAML error.

**Recommendation:** This is a style preference, not a bug. Flag as Info/Low only when:
1. The tags list has 5+ items (flow sequence becomes unwieldy)
2. Other lists in frontmatter use block style (inconsistency)
3. The file is meant for cross-system use (some parsers handle block style more reliably)

**Fix:** Convert to block-style for consistency:
```yaml
tags:
  - hermes
  - copilot
  - opencode
```

