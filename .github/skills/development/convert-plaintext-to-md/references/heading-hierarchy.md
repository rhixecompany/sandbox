# Heading Hierarchy Validation

## Rules

1. **Single H1** — Exactly one `# ` at document start (or after frontmatter)
2. **No skipped levels** — H1 → H2 → H3 only, never H1 → H3
3. **Consistent depth** — Max 4 levels (H1–H4) for readability
4. **Logical grouping** — Sibling headings at same level represent peer sections

## Validation Algorithm

```
current_level = 0
for each heading in document:
    if heading.level > current_level + 1:
        ERROR: "Skipped heading level: H{current_level} → H{heading.level}"
    if heading.level == 1 and not first_heading:
        ERROR: "Multiple H1 headings"
    current_level = heading.level
```

## Common Violations & Fixes

| Violation | Example | Fix |
|-----------|---------|-----|
| Skip H2 | `# Title` → `### Section` | Insert `## Missing Section` or demote to `##` |
| Multiple H1 | `# Title` ... `# Another` | Demote subsequent to `##` |
| Too deep | `#### Deep` | Flatten: merge with parent or promote siblings |
| promote siblings |

## Auto-Fix Strategies

1. **Demote all by 1** if first heading is H2+ (common in extracted content)
2. **Insert synthetic H2** when H1→H3 gap detected
3. **Collapse H4+H5** into H3 with bold sub-items
4. **Report only** — flag for manual review when structure ambiguous

## Pre-Conversion Analysis

Before converting plaintext:
1. Scan for ALL CAPS lines → candidate H2
2. Scan for Setext underlines (`===`, `---`) → confirm H2/H3
3. Count heading candidates → estimate max depth
4. If max depth > 4, plan flattening strategy

## Integration with Conversion

Phase 2 (Convert Structure) should:
1. Assign provisional levels during first pass
2. Run hierarchy validation
3. Apply fixes before writing output
4. Re-validate after fixes