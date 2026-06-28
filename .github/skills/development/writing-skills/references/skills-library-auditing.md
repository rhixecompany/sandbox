# Skills Library Auditing Reference

> Commands, patterns, and procedures for systematic skills library maintenance.
> Companion to Phase 5 of `writing-skills`.

## Quick Scan Commands

```bash
# Full inventory
hermes skills list

# Find SKILL.md files count
find /c/Users/Alexa/AppData/Local/hermes/skills -name "SKILL.md" | wc -l

# Root-level (uncategorized) skills
ls -d /c/Users/Alexa/AppData/Local/hermes/skills/*/SKILL.md

# Categorized skills count by category
ls -d /c/Users/Alexa/AppData/Local/hermes/skills/*/*/SKILL.md | cut -d/ -f9 | sort | uniq -c | sort -rn
```

## Duplicate Detection

Skills can exist in both root-level and categorized directories after migration:

```bash
# Find all skill names, check for duplicates
find skills -name "SKILL.md" -exec grep -h "^name:" {} \; | sort | uniq -d
```

**Root-level duplicates already deleted** (as of 2026-05-25):
- ~~`skills/systematic-debugging/`~~ → `skills/software-development/systematic-debugging/` ✓ deleted
- ~~`skills/subagent-driven-development/`~~ → `skills/software-development/subagent-driven-development/` ✓ deleted
- ~~`skills/test-driven-development/`~~ → `skills/software-development/test-driven-development/` ✓ deleted
- ~~`skills/writing-plans/`~~ → `skills/software-development/writing-plans/` ✓ deleted

**Double-nested orphan already deleted**:
- ~~`skills/software-development/requesting-code-review/requesting-code-review/SKILL.md`~~ ✓ deleted

## Frontmatter Corruption Detection

### Pattern: Embedded Line-Numbered Content

The content body contains a line-numbered copy of its own frontmatter:

```markdown
---
name: some-skill
...
---

# Some Skill

     1|---
     2|name: some-skill
     3|description: "..."
     4|---
```

**Detect it:**
```bash
grep -l "1|---" */SKILL.md */*/SKILL.md 2>/dev/null
```

**Fix:** Remove the entire `     1|---` through `     6|## <skill-name>` block. The real frontmatter above `# Heading` is the correct one.

### Pattern: Placeholder Content

Content left as "To be filled." from initial scaffolding.

**Detect it:**
```bash
find . -name "SKILL.md" -exec grep -l "To be filled" {} \;
```

**Fix:** Either remove the empty sections, or fill them with meaningful content.

## Category Consistency Check

Every local skill should live under `skills/<category>/<skill-name>/SKILL.md`.

**Root-level stragglers to recategorize:**
- `agent-browser/` → agentic/
- `algorithmic-art/` → creative/
- `asdf/` → devops/
- `banking/` → (keep? standalone domain)
- `brainstorming/` → planning/
- `brand-guidelines/` → creative/
- `canvas-design/` → creative/
- `humanizer/` → creative/
- `subagent-driven-development/` → autonomous-ai-agents/ (already duplicated there)
- `systematic-debugging/` → software-development/ (already duplicated there)
- `test-driven-development/` → software-development/ (already duplicated there)
- `writing-plans/` → software-development/ (already duplicated there)

> Note: Moving skills requires `hermes` CLI support or manual directory moves + curator state updates. Do not attempt by hand — confirm with the developer toolchain.

## Size Distribution Baseline

Use to identify skills that may be skeletal (too small) or bloated (too large):

```bash
find . -name "SKILL.md" -exec sh -c 'echo "$(wc -c < "$1") $1"' _ {} \; | sort -rn | head -10
```

Typical ranges:
- `< 2KB` — Minimal/imported skills, likely need expansion
- `2-5KB` — Standard skills with basic workflow
- `5-10KB` — Well-developed skills with examples
- `10KB+` — Reference-heavy skills with embedded docs

## Quality Checklist

- [ ] `name:` matches the directory name
- [ ] `version:` is present and incremented
- [ ] `author:` is set appropriately
- [ ] `related_skills:` populated (not empty array)
- [ ] No embedded line-numbered frontmatter in content body
- [ ] No `(To be filled.)` placeholders
- [ ] Heading hierarchy starts at `# Title` not `## Title`
- [ ] Code blocks have language specifiers
- [ ] Skill lives under a category directory
- [ ] No duplicate entries in `hermes skills list`
