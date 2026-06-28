# Batch Frontmatter Analysis for Prompt Files

> Pattern for scanning 100+ `.prompt.md` files, extracting frontmatter, identifying YAML issues, and extracting skill/dependency references.

## Discovery Steps

### 1. Inventory

```bash
ls .github/prompts/*.prompt.md | wc -l
```

### 2. Scan Frontmatter in Batches

Use `execute_code` with `terminal` calls to read `head -30` of each file, then parse:

```python
from hermes_tools import terminal
import re

r = terminal("ls /path/*.prompt.md 2>/dev/null")
files = [f.strip() for f in r["output"].strip().split("\n") if f.strip()]

for f in files[:50]:  # batch of 50
    r2 = terminal(f'head -30 "{f}"')
    lines = r2.get("output", "").split("\n")
    
    # Check for YAML opening
    if lines and lines[0].strip() == "---":
        # Find closing ---
        end_idx = -1
        for j in range(1, len(lines)):
            if lines[j].strip() == "---":
                end_idx = j
                break
        # Extract sections
```

### 3. Detect YAML Issues

| Issue | Detection | Fix |
|-------|-----------|-----|
| Missing closing `---` | `lines[j].strip() == "---"` not found in first 30 lines | Add standalone `---` line |
| Merged `|---##Content` | `"|---" in line and len(line.strip()) > 3` | Split into `---` + newline + `## Content` |
| No frontmatter at all | First line is not `---` | No action (community prompt without YAML) |

### 4. Extract Skill References

Two field formats:
- `dependencies:` with `- skill:name` items
- `skills:` with `- name` items (may include descriptions after ` — `)

Handle both:

```python
in_deps = False
for line in frontmatter_lines:
    if line.strip().startswith("dependencies:"):
        in_deps = True; continue
    elif line.strip().startswith("skills:"):
        in_skills = True; in_deps = False; continue
    elif line.strip().startswith(("tags:", "trigger:", "description:")):
        in_deps = False; in_skills = False
    
    if in_deps and "- skill:" in line:
        skill = line.split("skill:")[1].strip()
    elif in_skills and line.strip().startswith("- "):
        skill = line.strip()[2:].split(" — ")[0].strip()
```

### 5. Verify Skill Existence

Use `find` on the skills directory — skills live in category subdirectories:

```bash
find ~/AppData/Local/hermes/skills -name "SKILL.md" -path "*/$skill_name/*"
```

### 6. Template Extraction

For long sections (>40 lines), extract into the prompt's template directory:

```python
safe_title = re.sub(r'[^a-zA-Z0-9_-]', '_', heading[:30]).lower()
tpl_path = f"templates/{prompt_name}/{safe_title}.md"
# Write template, then trim original prompt section
```

## Pitfalls

- `read_file` blocks repeated reads of unchanged files — use `terminal(f'head -N "{f}"')` for batch scanning
- YAML frontmatter timing: scanning only `head -30` may miss frontmatter in larger files
- Skill names with hyphens vs underscores — always check actual on-disk directory names
- Copilot-style frontmatter (`agent:`, `tools:`, `model:`) uses different field names than Hermes (`trigger:`, `dependencies:`)
