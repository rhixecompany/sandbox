# Copilot → Hermes Prompt Frontmatter Migration

## Field Mapping

| Copilot Field | Hermes Equivalent | Action |
|---|---|---|
| `agent:` | none | **Remove** — Copilot-specific execution agent |
| `model:` | none | **Remove** — model pinning is per-profile, not per-prompt |
| `tools:` | `toolsets:` | **Rename** — same value, different key. **Watch for multi-line format!** |
| `trigger:` | keep | Both use it (optional) |
| `name:`, `title:`, `description:`, `version:`, `author:`, `license:` | same | Keep as-is |

## Multi-Line `tools:` Detection

Copilot prompts often write tools as a multi-line flow sequence:

```yaml
tools:
  [
    "edit/editFiles",
    "web/fetch",
    "search/codebase"
  ]
```

The naive `get_field('tools')` returns `""` because the value is on subsequent lines. After conversion, the frontmatter becomes:

```yaml
toolsets:
  [
    "edit/editFiles",      # <-- orphaned! Not attached to any field
    "web/fetch",
    "search/codebase"
  ]
```

### Detection command
```bash
# Files with orphaned [ block in frontmatter
awk '/^---/{c++;next} c==1 && /^\s*\[/{print FILENAME;exit}' *.prompt.md

# Files where tools: is followed by [ on next line
for f in *.prompt.md; do
  fl=$(grep -n '^tools:' "$f" | head -1 | cut -d: -f1)
  [ -n "$fl" ] && { nl=$((fl+1)); sed -n "${nl}p" "$f" | grep -q '^\s*\[' && echo "$f: multi-line tools"; }
done
```

### Fix: extract bracket items and write YAML block list
1. Find the `tools:` line
2. Read lines until `]` is found (collecting items)
3. Remove all those lines from frontmatter
4. Write `toolsets:` with `  - item` for each extracted item

### Post-fix verification
```bash
# No orphaned brackets
awk '/^---/{c++;next} c==1 && /^\s*\[/{print FILENAME;exit}' *.prompt.md | wc -l
# Should print 0
```

## Multi-Line `tags:` Format

Some prompts use:

```yaml
tags: []
  [
    hermes,
    copilot,
    opencode
  ]
```

This is invalid YAML in strict mode — `tags: []` declares an empty flow sequence, but the `[` on the next line is orphaned. The intended value is `[hermes, copilot, opencode]`.

### Fix
1. Detect: `tags:` line is `tags: []` and next line starts with `[`
2. Read items from the bracket block
3. Replace with:
   ```yaml
   tags:
     - hermes
     - copilot
     - opencode
   ```

### False positives to watch for
- `tags: []` followed by `  - hermes` — this is already valid YAML (block items after empty flow sequence are treated as list items by most parsers). Leave it alone.
- `tags: [hermes, copilot]` inline — already valid, no change needed.

## Inline `tools:` Format

The simple case — a single line:

```yaml
tools: ["edit/editFiles", "web/fetch"]
```

This converts directly to:

```yaml
toolsets: ["edit/editFiles", "web/fetch"]
```

The inline value is captured correctly by `get_field()` → `["edit/editFiles", "web/fetch"]` → `update_field('toolsets', value)` writes `toolsets: ["edit/editFiles", "web/fetch"]`.

## Pitfalls

| Pitfall | Detection |
|---|---|
| Orphaned `[` block | `awk '/^---/{c++;next} c==1 && /^\s*\[/'` after conversion |
| Empty `toolsets:` after migration | `grep '^toolsets:\s*$'` then check next line for `-` or `[` |
| `tags:` in body, not frontmatter | `grep -n '^tags:'` and verify inside `---` delimiters |
| Field reordering changes semantics | `awk '/^---/{c++;next} c==1 && /^name:/{print NR}'` — capture original line position |
