# Frontmatter Corruption Repair

> Detection and repair patterns for garbled/malformed skill frontmatter that can result from batch migration operations.

## Common Corruption Patterns

### Pattern A: Double/Triple Frontmatter (SKILL.md files)
A garbled dummy frontmatter block (`name: skill`, `description: "1|---"`) was prepended *on top of* the already-correct frontmatter, creating stacked frontmatter blocks.

**Detection:**
```bash
# In .opencode/skills or Hermes skills path
rg '^name: skill$' --glob '**/SKILL.md' -l
```

**Characteristic output:**
```
---
name: skill
description: "1|---"
version: 1.0.0
author: Alexa
license: MIT
metadata:
  hermes:
    tags: []
    related_skills: []
---
     1|---
     2|name: real-skill-name
     3|description: "Real description..."
     4|---
```

**Fix:** Restore from a clean backup (pre-migration copy). The backup directory at `docs/skills-backups/YYYYMMDD-HHMMSS/skills/<name>/SKILL.md` usually contains the clean version.

### Pattern B: `1|#` Prefix in Descriptions (Reference .md files)
Reference files received frontmatter where the `description` field contains a literal `1|#` prefix copied from `read_file` output.

**Detection:**
```bash
rg 'description: "1\\|#' --glob '*.md' -l
```

**Characteristic output:**
```yaml
---
name: some-file
description: "1|# Actual Heading Text"
---
```

**Fix:** Patch the description to remove the `1|` prefix. The correct description is the actual heading text.

```yaml
# Before
description: "1|# Actual Heading Text"
# After
description: "# Actual Heading Text"
```

### Pattern D: Line-Numbered Content Embedding (Hermes skills)

The content body contains a verbatim copy of rendered text with embedded line numbers like `    11|`, `    12|` etc. This happens when `skill_view()` output (which displays content with line numbers) is written back directly as file content.

**Detection:**
```bash
grep -rl "     1|---" --include="SKILL.md" /c/Users/Alexa/AppData/Local/hermes/skills/
```

**Characteristic output:**
```markdown
---
name: some-skill
...
---

# Some Skill

## Description

Some description text.
    11|
    12|## When to Use
    13|
    14|- Item one
    15|- Item two
```

Every content line after the heading has `    XX|` prefix. The real frontmatter and first few lines of clean content are OK.

**Fix:** Rewrite the entire file, stripping all `    XX|` prefixes from the content body. The clean content exists, it's just prefixed with line numbers:

```python
# Python fix pattern
import re
with open("SKILL.md", "r") as f:
    content = f.read()

# Split into frontmatter + body
parts = content.split("---\n", 2)
frontmatter = "---\n" + parts[1] + "---\n"
body = parts[2]

# Remove line-number prefixes from every content line
body = re.sub(r"^\s+\d+\|", "", body, flags=re.MULTILINE)
# Clean up extra blank lines
body = re.sub(r"\n{3,}", "\n\n", body)

with open("SKILL.md", "w") as f:
    f.write(frontmatter + "\n" + body.lstrip("\n"))
```

**Alternative (bash):**
```bash
sed -i '/^      [0-9]|/d' SKILL.md
```

**Note:** Also check for `(To be filled.)` placeholders at the end — these were common in the same batch of corrupted files and should be replaced with real content.
The garbled frontmatter block contains `description: "1|---"` — this is Pattern A's dummy block.

**Detection:**
```bash
rg 'description: "1\\|---' --glob '*.md' -l
```

**Fix:** Same as Pattern A — restore SKILL.md from backup.

## Mirrored Fixes

Both `.opencode/skills/` and `C:\Users\Alexa\AppData\Local\hermes\skills\` must be fixed. After fixing `.opencode/skills/`, mirror by copying:

```bash
cp .opencode/skills/<relative-path> "$HERMES_SKILLS/<relative-path>"
```

## Verification

After fixing, re-run detection queries to confirm zero remaining occurrences. Spot-check first 4 lines of each fixed file:

```bash
head -4 <file>
# Should show:
# ---
# name: <correct-name>
# description: "<correct description>"
# ---
```
