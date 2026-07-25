# Near-Duplicate Prompt Consolidation

> Detailed technique reference for prompt-consolidation Phase 2 and Phase 5.

## Jaccard Similarity Implementation

```python
import pathlib, re

def get_body_text(prompt_path):
    """Extract body text (strip frontmatter)."""
    content = prompt_path.read_text(encoding='utf-8')
    parts = content.split('---', 2)
    body = parts[2] if len(parts) > 2 else content
    body = re.sub(r'\s+', ' ', body).strip()
    return body

def jaccard_similarity(text1, text2):
    """Word-overlap similarity: 1.0 = identical, 0.0 = no overlap."""
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())
    if not words1 or not words2:
        return 0.0
    intersection = words1 & words2
    union = words1 | words2
    return len(intersection) / len(union)
```

## Threshold Tuning

| Score | Action | Notes |
|-------|--------|-------|
| 0.9+ | Strong consolidation candidate | Usually same prompt with minor wording changes |
| 0.8–0.89 | Likely consolidation | Review variable sections to confirm |
| 0.6–0.79 | Possibly shared template | Extract common sections, keep separate prompts |
| <0.6 | Distinct prompts | No action needed |

For groups of 3+ prompts, compute a pairwise matrix to find the core cluster.

## Parameterized Mapping Table Pattern

When consolidating N near-duplicates into 1 parameterized prompt, create a `## Parameters` table:

```markdown
| Parameter | type_a | type_b | type_c |
|-----------|--------|--------|--------|
| `local_dir` | path for A | path for B | path for C |
| `file_pattern` | pattern for A | pattern for B | pattern for C |
| `trigger` | `/type-a` | `/type-b` | `/type-c` |
```

Then in the consolidated prompt's Phases, use `{parameter}` placeholders like `{local_dir}` and `{file_pattern}`.

## Real Example: suggest-awesome-* Consolidation

**Before** (4 files):
- `suggest-awesome-github-copilot-agents.prompt.md` (152 lines)
- `suggest-awesome-github-copilot-instructions.prompt.md` (173 lines)
- `suggest-awesome-github-copilot-prompts.prompt.md` (152 lines)
- `suggest-awesome-github-copilot-skills.prompt.md` (181 lines)

**Jaccard similarities** (body-level):
- agents ↔ instructions: 0.91
- agents ↔ prompts: 0.88
- agents ↔ skills: 0.86
- instructions ↔ prompts: 0.90
- instructions ↔ skills: 0.87
- prompts ↔ skills: 0.89

All pairs >0.8 → consolidation justified.

**Variable elements identified** (4 parameters):
1. `awesome_dir` — GitHub directory name
2. `local_dir` — local scan directory
3. `file_pattern` — file extension pattern
4. `discovery` — folder vs file enumeration

**After** (1 file):
- `suggest-awesome-github-copilot.prompt.md` with `## Parameters` table

**Net result**: −3 files, −450+ lines of duplicate boilerplate.

## Cleanup Steps

```bash
# Delete old files
git rm -f prompts/old-name-*.prompt.md

# Archive orphaned template dirs
for d in prompts/templates/old-name-*/; do
  [ -d "$d" ] && git mv "$d" .hermes/archived-prompt-templates/
done

# Verify no stale references
grep -rn "old-name" prompts/ --include="*.prompt.md" -l

# Re-validate
python /path/to/validate_prompt_frontmatter.py
python /path/to/dry_run_prompts.py
```

## Warning Signs to Skip Consolidation

- A prompt is actively imported/referenced by name from another prompt's `dependencies:` field.
- The variable elements constitute >40% of the body content (branching logic overwhelms savings).
- The group has >5 varying parameters (too complex for one parameterized prompt).
- The prompts belong to different functional domains (e.g., cloud ops vs local dev).
