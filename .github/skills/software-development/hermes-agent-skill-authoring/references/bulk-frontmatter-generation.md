# Bulk Frontmatter Generation — Programmatic Approach

This reference documents the technique used during the 2026-05-24 session to normalize YAML frontmatter across 151 reference files (spanning 64 skill directories) in 26 batches of 7. It complements the batch audit approach in `skills-audit-and-fix.md`.

## When to Use This

- You have **dozens to hundreds** of markdown files across multiple directories that need consistent YAML frontmatter
- Most files are **reference/supporting files** (not the primary SKILL.md), each with its own `# Heading`
- You want a **single-shot automated approach** rather than per-file manual editing

**Don't use this for:** a handful of files (patch individually), files without clear headings (use placeholders), or files that need unique domain-specific frontmatter fields (manual review first).

## Technique Overview

```
Inventory → Generate Frontmatter + Diffs → Apply in Batches (≤7) → Mirror to Target → Verify All
```

The core idea: use `execute_code` with `search_files` + `read_file` + `write_file` (from `hermes_tools`) to programmatically scan files, generate frontmatter from file content, and write it — all without V4A patches or sed/awk.

## Step-by-Step

### 1. Inventory

Use search_files or terminal `find` to get the canonical file list. Sort it deterministically so batches are reproducible.

```python
from hermes_tools import search_files, terminal, write_file, read_file, patch

# Get canonical list
result = terminal("find .opencode/skills -type f -name '*.md' | sort > /tmp/skills_list.txt")
result = terminal("wc -l /tmp/skills_list.txt")
```

### 2. Backup (always first)

```python
import subprocess, datetime
ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
terminal(f"mkdir -p docs/skills-backups/{ts}")
terminal(f"cp -r .opencode/skills docs/skills-backups/{ts}/")
terminal(f"echo Files backed up: $(find docs/skills-backups/{ts} -type f | wc -l)")
```

### 3. Scan and Generate Frontmatter (the core pattern)

Read the file, extract the first `# Heading`, and skip files that already have frontmatter:

```python
import yaml, re

def needs_frontmatter(content):
    """Check if file is missing YAML frontmatter."""
    # Already has frontmatter
    if content.startswith('---'):
        m = re.search(r'\n---\s*\n', content[3:])
        if m:
            return False, None
    return True, None

def derive_name(filepath, skill_dir):
    """Generate name from parent directory + filename without extension."""
    # filepath: .opencode/skills/claude-api/references/shared-models.md
    rel = filepath.split('skills/', 1)[1] if 'skills/' in filepath else filepath
    parts = rel.replace('\\', '/').split('/')
    # Get the skill directory name (2nd level): claude-api
    parent = parts[0] if len(parts) > 0 else ''
    # Get the stem: shared-models
    stem = re.sub(r'\.md$', '', parts[-1])
    return f"{parent}-{stem}"

def derive_description(content):
    """Extract the first # Heading for the description."""
    # Look for first # heading after frontmatter (if any)
    body = content
    if content.startswith('---'):
        m = re.search(r'\n---\s*\n', content[3:])
        if m:
            body = content[m.end()+3:]
    lines = body.split('\n')
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('# ') and not stripped.startswith('##'):
            return stripped[2:].strip()
    return "Use when (auto-detected heading missing)"
```

### 4. Batch Execution

Read N files (default 7), generate frontmatter, write back in sequence:

```python
BATCH_SIZE = 7

def apply_frontmatter_batch(files, batch_num):
    """Apply frontmatter to a batch of files."""
    results = []
    for filepath in files:
        content = read_file(filepath)["content"]
        needs, _ = needs_frontmatter(content)
        if not needs:
            results.append((filepath, "SKIP (already has frontmatter)"))
            continue

        name = derive_name(filepath, None)
        desc = derive_description(content)

        frontmatter = f"""---
name: {name}
description: "{desc}"
version: 1.0.0
author: Alexa
---
"""
        new_content = frontmatter + content
        write_file(filepath, new_content)
        results.append((filepath, "APPLIED"))

    return results
```

### 5. Immediate Mirroring

After each batch is written, copy to the target directory:

```python
def mirror_to_target(source_dir, target_dir):
    """Copy changed files to target location."""
    terminal(f"cp -r {source_dir}/* {target_dir}/")
```

Or more selectively:
```python
def mirror_files(files, source_root, target_root):
    """Mirror specific files to target, preserving relative paths."""
    for f in files:
        rel = f.replace(source_root, '').lstrip('/\\')
        terminal(f"cp '{f}' '{target_root}/{rel}'")
```

### 6. Verification (three-pass)

```python
# Pass 1: Coverage — every file has frontmatter
result = terminal("""
  cd .opencode/skills
  for f in $(find . -name '*.md' | sort); do
    head -1 "$f" | grep -q '^---$' || echo "MISSING: $f"
  done
""")
print(f"Files missing frontmatter: {result['output'].count('MISSING:')}")

# Pass 2: YAML Parseability
result = terminal("""
  cd .opencode/skills
  python3 -c "
import yaml, re, sys, pathlib
files = sorted(pathlib.Path('.').rglob('*.md'))
bad = []
for f in files:
    c = f.read_text()
    if not c.startswith('---'):
        bad.append(f'{f}: no frontmatter')
        continue
    m = re.search(r'\\n---\\s*\\n', c[3:])
    if not m:
        bad.append(f'{f}: unclosed frontmatter')
        continue
    try:
        fm = yaml.safe_load(c[3:m.start()+3])
        if 'name' not in fm:
            bad.append(f'{f}: missing name')
    except Exception as e:
        bad.append(f'{f}: {e}')
print(f'Bad files: {len(bad)}')
for b in bad[:20]:
    print(b)
  "
""")

# Pass 3: Source vs Target diff check (sample)
result = terminal("diff -rq .opencode/skills/hermes-agent-skill-authoring .../hermes/skills/...")
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| `{parent-skill-dir}-{filename}` naming | Preserves context for reference files; avoids collisions across skill dirs |
| Description from first `# Heading` | Content-aware; avoids stale placeholders; consistent with file purpose |
| Batch size 7 | Keeps each write-and-mirror cycle under 60s; produces reviewable diffs |
| Immediate mirror per batch | No accumulated drift; each batch is a self-contained sync unit |
| 3-pass verification | Coverage (did we miss any?) → correctness (valid YAML?) → fidelity (mirror matches source?) |

## Common Pitfalls

1. **File discovery mismatch.** `search_files` may return incomplete results. Fall back to `find . -type f -name '*.md' | sort` via terminal to get the canonical list.

2. **Backslash vs forward slash on Windows.** When constructing relative paths for mirroring, normalize with `.replace('\\', '/')`.

3. **Description too long (>1024 chars).** The validator enforces this. When extracting from a long `# Heading` line, truncate:
   ```python
   desc = heading.strip()[:1020]  # room for quotes etc.
   ```

4. **Frontmatter injection corrupts existing content.** If the file already has frontmatter, skip it (don't double-wrap). If the file starts with content rather than `---`, prepend frontmatter.

5. **Malformed YAML from special characters.** Descriptions containing `"` or `:` need quoting or escaping. Use double-quoted YAML strings (`"..."`) with inner quotes escaped:
   ```python
   desc = desc.replace('"', '\\"')
   frontmatter = f'---\\nname: {name}\\ndescription: "{desc}"\\n...'
   ```

## Verification Checklist

- [ ] Canonical file list sorted and recorded (e.g., `/tmp/skills_list.txt`)
- [ ] Backup written before any modifications
- [ ] Batch size ≤ 7 per cycle
- [ ] Every file in batch: frontmatter written and immediately mirrored
- [ ] Coverage: 100% of files have frontmatter (0 missing)
- [ ] YAML parseability: all frontmatter parses cleanly
- [ ] Fidelity: source ↔ target diff is empty for migrated files
- [ ] Verification artifact saved (e.g., `docs/skills-merge-verify.md`)
