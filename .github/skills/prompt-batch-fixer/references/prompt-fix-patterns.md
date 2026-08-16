# Prompt Fix Patterns

A catalog of known YAML frontmatter and body markdown issues found in prompt files,
with detection commands and fix strategies. Each pattern has a before/after example.

## Pattern 1: Inline YAML List Syntax

**Symptom:** `audit flags → yaml_error:expected <block end>`

**Detection:**
```bash
grep -rn '^  [a-z_]*: - ' *.prompt.md | head -10
```

**Before:**
```yaml
toolsets: - terminal
tags: - python
scripts: - build.sh
```

**After:**
```yaml
toolsets:
  - terminal
tags:
  - python
scripts:
  - build.sh
```

**Fix:** A Python regex replaces `key: - value` with `key:\n  - value` for known list keys (toolsets, tags, scripts, skills, formatter, plan, dependencies).

## Pattern 2: `metadata: hermes:` Inline Mapping (Wrong Nesting)

**Symptom:** `audit flags → yaml_error:mapping values are not allowed here`

**Detection:**
```bash
grep -rl "metadata:" *.prompt.md | xargs grep -l "hermes:" | xargs grep -l "related_skills:"
```

**Before:**
```yaml
metadata:
  hermes:
  related_skills:
  - foo
  - bar
```

In this invalid structure, `hermes:` is null and `related_skills:` is a sibling key under `metadata`. If `hermes:` has no value and `related_skills:` is at the same indent, it creates a YAML ambiguity.

**After:**
```yaml
metadata:
  hermes:
    related_skills:
      - foo
      - bar
```

**Fix:** A Python regex changes `  hermes:\n  related_skills:` to `  hermes:\n    related_skills:` and re-indents the list items.

## Pattern 3: Multi-Line Single-Quoted YAML Descriptions

**Symptom:** `yaml.safe_load()` raises `while parsing a block mapping` even though the file looks correct.

**Before:**
```yaml
description: 'Inventory providers, discover models, benchmark accessible free models, '
  'compare providers, analyze rate limits/fallbacks, and create/update automation scripts.'
```

PyYAML cannot parse single-quoted strings that span multiple lines with continuation quotes.

**After:**
```yaml
description: "Inventory providers, discover models, benchmark accessible free models, compare providers, analyze rate limits/fallbacks, and create/update automation scripts."
```

**Fix:** A Python regex captures `description: '...\n  '...'` patterns, joins the content, and writes as a double-quoted single-line string.

## Pattern 4: Orphaned List Items After Tag Replacement

**Symptom:** Stale `- foo` lines remaining in frontmatter after a tag block was replaced.

**Before (after a tags block replacement):**
```yaml
tags:
  - agents
  - system-prompt
- agents
- system-prompt
```

The unindented `- agents` lines are orphans from the old tag format.

**After:**
```yaml
tags:
  - agents
  - system-prompt
```

**Fix:** Detect root-level (no leading whitespace) lines starting with `- ` that have no colon (are not continuation items under a known key). Remove them.

## Pattern 5: Copilot `...` Doc Separators

**Symptom:** Files use `...` instead of `---` as YAML document separators.

**Detection:**
```bash
grep -l "^\.\.\.$" *.prompt.md
```

**Before:**
```
...
name: foo
version: 1.0.0
...
```

**After:**
```
---
name: foo
version: 1.0.0
---
```

**Fix:** Simple regex replace: s/^\.\.\.$/---/g

## Pattern 6: Merged Body Markdown (`---##`)

**Symptom:** `audit flags → merged_yaml_close` — the audit script finds `---##` within 600 chars of the frontmatter close.

**Before:**
```
---## GoalResearch the project...
---## ContextWorkspace: is here...
```

**After:**
```
---

## Goal

Research the project...

---

## Context

Workspace: is here...
```

**Fix:** `re.sub(r'---##', '---\n\n##', body)` and `re.sub(r'---###', '---\n\n###', body)` to separate the horizontal rule from the heading.

## Pattern 7: CRLF → LF Line Endings

**Symptom:** `file *.prompt.md` shows CRLF terminators. Some YAML parsers generate spurious errors.

**Fix:**
```bash
sed -i 's/\r$//' *.prompt.md
```
or in Python:
```python
content = open(f, 'r', encoding='utf-8').read()
open(f, 'w', encoding='utf-8', newline='\n').write(content)
```

## Pattern 8: Double-Quoted YAML With Escaped Newlines

**Symptom:** Description is hard to read in source:
```yaml
description: "line one\
  \ line two\
  \ line three.\nAlso includes section B."
```

**After:**
```yaml
description: "line one line two line three. Also includes section B."
```

**Note:** The `\n` in the original creates a real newline in the rendered value. Only simplify if the line breaks aren't needed. For single-line descriptions, prefer unquoted or single-quoted YAML to avoid escaping issues.

## Multi-Pass Fix Strategy

When fixing 100+ prompt files with multiple issue types, **never write one monolithic fix script**. Instead:

| Pass | Focus | Rollback Risk |
|------|-------|---------------|
| 1 | Structural: `...`→`---`, CRLF→LF, missing fields | Low (idempotent) |
| 2 | List format: inline→block, metadata nesting | Medium (YAML structure) |
| 3 | Body: `---##`→`---\n\n##`, heading spacing | Medium (markdown) |
| 4 | Content: orphaned items, ML descriptions | High (data loss risk) |

Use separate scripts per pass. If pass 4 corrupts data (e.g. a bug in body join), you can `git checkout` the affected files and re-run passes 1-3 without redoing the entire batch.
