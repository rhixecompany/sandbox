# Prompt File Extension Normalization

> Pattern for normalizing non-standard `.prompts.md` extensions to `.prompt.md` and updating cross-references.

## When to Use

- A prompt directory has mixed extensions (`.prompt.md` and `.prompts.md`)
- Files use the plural `.prompts.md` extension inconsistently
- After renaming, you need to update internal cross-references in other files

## Discovery

Find non-standard extensions:

```bash
cd .github/prompts
ls *.prompts.md 2>/dev/null | wc -l   # count non-standard files
```

Expected: **0**. If >0, proceed with normalization.

## Rename Pattern

```bash
for f in *.prompts.md; do
  new=$(echo "$f" | sed 's/.prompts.md$/.prompt.md/')
  git mv "$f" "$new" 2>/dev/null || mv "$f" "$new"
done
```

Also rename corresponding template directories:

```bash
for d in templates/*.prompts/; do
  new=$(echo "$d" | sed 's/.prompts$/.prompt/')
  mv "$d" "$new" 2>/dev/null
done
```

## Update Cross-References

After renaming, all files that reference the old `.prompts.md` names must be updated:

```bash
# Find files with stale references
grep -rn "\.prompts\.md" --include="*.md" . | grep -v node_modules | grep -v .git

# Fix each reference
sed -i 's/\.prompts\.md/\.prompt\.md/g' <file>
```

### Files to Check

1. **Other prompt files** — any prompt that references a renamed prompt in its `Related Prompts` section
2. **Documentation files** — docs/ and reports/ that mention prompt filenames
3. **Template directories** — README.md files in templates/ that reference the old name

### Pattern Examples

```bash
# Update prompt cross-references
sed -i 's/repo\.prompts\.md/repo.prompt.md/g' repo.prompt.md
sed -i 's/bash-scripts-fix\.prompts\.md/bash-scripts-fix.prompt.md/g' workspace-consolidate.prompt.md
```

## Verification

```bash
# 1. No .prompts.md files remain
ls *.prompts.md 2>/dev/null | wc -l    # must be 0

# 2. No stale references in prompt files
grep -rn "\.prompts\.md" *.prompt.md   # must be 0

# 3. Template dirs match new names
ls -d templates/*.prompt/ 2>/dev/null | wc -l   # should match renamed count
```

## Pitfalls

- **Code blocks**: Some files reference `.prompts.md` inside markdown code blocks as examples. These are instructional and should NOT be updated — they show the old naming as a historical example.
- **External URLs**: References to external repos or GitHub docs that use `.prompts.md` should be left as-is.
- **Case sensitivity**: Template directories use the exact prompt name. If the prompt uses hyphens, the template dir uses hyphens. If underscores, underscores. Match exactly.
- **git mv vs mv**: Prefer `git mv` when in a git repo — it stages the rename and preserves history. Fall back to `mv` when the directory is not tracked.
