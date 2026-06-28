# Batch Prompt Template Extraction

> Pattern for consolidating markdown prompt files: extract long sections into per-prompt template directories, trim inline content, follow DRY. Covers both extraction AND balanced trimming.

## When to Use

- A folder has 50+ `.prompt.md` files that need consolidation
- Prompts have long sections (>30 lines) that should be extracted as templates
- You need to apply DRY across many prompt files with shared patterns
- Previously extracted templates need trimming (inline content → template references)

## Workflow

### Phase 1: Create Infrastructure

```bash
# Create per-prompt template directories
cd .github/prompts
for f in *.prompt.md *.prompts.md 2>/dev/null; do  # catch both extensions
  name="${f%.prompt.md}"
  name="${name%.prompts}"
  mkdir -p "templates/$name"
done

# Create shared templates directory
mkdir -p templates/_shared
```

### Phase 2: Extract Long Sections

For each prompt with sections >30 lines under `##` headings:

1. Read the prompt file
2. Parse `## ` headings and calculate section lengths
3. For each section >30 lines, write to `templates/<name>/<slug>.md`
4. Skip if template file already exists (idempotent)

```python
# Key extraction logic:
headings = [(i, line) for i, line in enumerate(lines) if re.match(r'^## [^#]', line.strip())]
for idx in range(len(headings)-1, -1, -1):
    start, title = headings[idx]
    end = headings[idx+1][0] if idx+1 < len(headings) else total
    length = end - start
    if length > 30:
        # Write section to template file
        safe = re.sub(r'[^a-zA-Z0-9_ -]', '', title.strip("# ").strip())[:35].strip().lower()
        safe = safe.replace(" ", "_")[:30]
        with open(f"templates/{name}/{safe}.md", "w") as tf:
            tf.write("\n".join(section_lines))
```

### Phase 3: Create README per Prompt

Each template directory gets a README.md with:
- Prompt name and file size
- Line count and section count
- List of extracted template files

### Phase 4: Add Template References to Prompts

Append a `## Template References` section to each prompt that has extracted templates:

```markdown
## Template References

Detailed templates in `templates/<name>/`:
- `<template-1>.md` — Description
- `<template-2>.md` — Description
```

Check for existing references first — never duplicate.

### Phase 5: Balanced Trimming (CRITICAL)

After extracting sections into templates, **trim the prompt** by replacing long inline sections with concise references. BUT use the **balanced pattern**:

**DO NOT** do this (aggressive — user will reject):
```markdown
## Phases

> ### Phase 1: Do Thing
> **Full content:** `templates/name/phases.md`
```
This removes ALL inline detail. The prompt is no longer self-contained.

**DO this instead** (balanced):
```markdown
## Phases

### Phase 1: Do Thing

**Goal:** One-line description of what this phase accomplishes.

| Step | Action | Output |
| --- | --- | --- |
| 1.1 | Run `command` | Expected output |
| 1.2 | Run `command` | Expected output |

> **Detailed breakdown:** `templates/name/phases.md`
```

**Balanced trim rules:**
1. Keep the **heading** and **goal** inline — always
2. Keep a **step table** (3-5 rows max) — the user needs to see the flow without opening the template
3. Keep **critical rules** inline (the first 15% rule, safety constraints)
4. Move **verbose explanations**, **long examples**, **exhaustive task lists** to templates
5. The template reference should be in a `>` blockquote — noticeable but not the primary content
6. Verify the prompt is still **actionable** without opening any template file

### Phase 6: Section Threshold Strategy

Different prompts need different section-length thresholds for extraction:

| Prompt Size | Threshold | Rationale |
|-------------|-----------|-----------|
| >300 lines | 30 lines | Large prompts, extract only substantial sections |
| 100-300 lines | 15 lines | Medium prompts, extract moderately long sections |
| 30-100 lines | 5 lines | Small prompts, extract any meaningful section |
| <30 lines | — | Too small to extract; create README only |

For mixed-scale batches (215 prompts ranging 1-3119 lines), sort by descending size and apply tiered thresholds.

### Phase 7: Shared Templates

Create `templates/_shared/` with reusable templates:
- `frontmatter.md` — YAML frontmatter patterns (Hermes + Copilot styles)
- `skill-refs.md` — Common Hermes skill reference table (16 core skills)
- `verification-checklist.md` — Standard verification gates + safety pattern
- `best-practices.md` — Prompt engineering best practices (structure, safety, DRY)

### Phase 8: Index

Create `templates/_index.md` documenting:
- Directory structure
- Shared template descriptions
- DRY principles
- Per-prompt template conventions

## YAML Frontmatter Fixes

When processing prompts, watch for this common issue:

**Merged closing `---`**: Copilot-style prompts often have the closing `---` merged with the next heading:

```markdown
|---## Goal
```

or (no pipe):

```markdown
---## Goal
```

Fix: Split into separate lines:

```markdown
---

## Goal
```

Detection (two patterns):
```bash
grep -l "^---|---" *.prompt.md    # piped variant
grep -l "^---[^|]" *.prompt.md    # direct variant (--- followed by non-pipe non-newline)
```

### Python Fix Script

```python
import os

for fname in os.listdir("."):
    if not fname.endswith(".prompt.md"):
        continue
    with open(fname, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    changed = False
    new_lines = []
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("---") and len(stripped) > 3 and not stripped.startswith("---|"):
            after = stripped[3:].strip()
            new_lines.append("---")
            new_lines.append("")
            new_lines.append(after)
            changed = True
        else:
            new_lines.append(line)
    
    if changed:
        with open(fname, "w") as fh:
            fh.write("\n".join(new_lines))
```

## File Extension Normalization

See `references/prompt-file-extension-normalization.md` for the pattern on renaming `.prompts.md` (plural) to `.prompt.md` (singular) and updating cross-references in other prompt files.

## Python Batch Processing Pattern

For 100+ prompts, use `python3 << 'PYEOF' ... PYEOF` heredocs via `terminal`:

```bash
cd ~/Desktop/SandBox/.github/prompts && python3 << 'PYEOF'
import os, re

prompts = [(f, os.path.getsize(f)) for f in os.listdir(".") if f.endswith(".prompt.md")]
prompts.sort(key=lambda x: -x[1])

for fname, _ in prompts:
    name = fname.replace(".prompt.md", "")
    tdir = f"templates/{name}"
    os.makedirs(tdir, exist_ok=True)
    
    with open(fname, "r") as fh:
        content = fh.read()
    lines = content.split("\n")
    
    # Extract sections...
PYEOF
```

## Large-Scale Operation (200+ prompts)

When processing 200+ prompts, use this strategy:

1. **Sort by descending size** — process largest first (most impact per prompt)
2. **Batch by 10** — process in batches of 10 prompts, report after each batch
3. **Template count target** — aim for 3+ template files per large prompt, 1+ per medium prompt
4. **Trim after extraction** — run a separate pass to replace inline content with template refs (Phase 5)
5. **Validate incrementally** — after each batch, check: template refs resolve, YAML is valid, no duplicate refs
6. **Handle tiny prompts (<30 lines)** — ~9 out of 215 will have nothing extractable. Skip them with README only
7. **Track savings** — report KB saved by trimming (expect ~900KB for 200 prompts with large sections)

## Verification

| Gate | Check | Expected |
|------|-------|----------|
| Count | `find templates -name "*.md" ! -name "README.md" ! -path "*/_shared/*" \| wc -l` | 300-500 for 200 prompts |
| Coverage | `grep -l "Template References" *.prompt.md \| wc -l` | >95% of prompts |
| Index | `ls templates/_shared/*.md \| wc -l` | ≥4 files |
| README | `ls templates/*/README.md \| wc -l` | Matches prompt count |
| Resolve refs | Check each `templates/<name>/<file>.md` exists for every `template references:` mention | 100% |
| Balanced trim | Sample-check 5 prompts: each has inline goal + step table + template ref, not just `> Full content:` | All actionable |
| YAML closing | `grep -c "^---[^|]" *.prompt.md` | 0 (all fixed) |
| Extension norm | `ls *.prompts.md 2>/dev/null ; wc -l` | 0 non-standard extensions |

## Pitfalls

- **Don't overwrite existing templates** — check `os.path.exists()` before writing
- **Don't duplicate template refs** — check `"Template References" not in content` before appending
- **Shell escaping** — Use Python heredocs (`<< 'PYEOF'`) not shell string interpolation for file writes
- **Batch size** — Process 10 prompts per batch for manageability; 100+ per script for efficiency
- **read_file dedup** — After 3-4 reads of the same path, `read_file` blocks. Use `terminal` + `head/tail/wc` for repeated checks
- **YAML vs no-YAML** — Only ~20% of prompts have proper YAML frontmatter. Don't add frontmatter to prompts that don't have it unless specifically asked
- **Merged `|---`** — Only fix the closing `---` merge issue. The table-formatting `|---` in markdown tables is correct
- **Over-trimming** — The most common mistake. Always keep enough inline content that the prompt is actionable without opening template files. If the template reference is the ONLY content under a heading, you trimmed too far.
- **DRY Skills Required tables** — Many prompts have a redundant `## Skills Required` table that duplicates the YAML `skills:` field. Remove these during trimming — the frontmatter is the source of truth.
- **Trigger mismatch** — Some prompts have `trigger:` that differs from the filename stem. Only flag as warning; changing triggers can break existing workflows.
- **Cross-reference staleness after rename** — After renaming files, ALL files that reference the old name must be updated. Use `grep -rn "oldname"` across the entire workspace, not just the prompt directory. Documentation files (`docs/`, `reports/`) are especially prone to stale references.
- **Extension pattern in discovery** — When using `--pattern`, include both `.prompt.md` and `.prompts.md` if the directory might have mixed extensions. Use `--pattern "*.prompt*.md"` to catch both.
