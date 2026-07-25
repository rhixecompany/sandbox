# Skills Extraction from Prompt Files

> Pattern for extracting all referenced skills from a batch of `.prompt.md` files during `enhance-markdown --batch`.

## Problem

When auditing batch `.prompt.md` files, each prompt references skills via `skills:`, `dependencies:`, or `metadata.hermes.related_skills:` fields. These need to be extracted, deduplicated, and audited (via `skill-judge`) to ensure all dependencies are healthy before executing the prompts.

## Discovery Steps

1. **Read all prompt files** — Use `search_files("*.prompt.md")` or direct reads of the batch target files
2. **Extract `skills:` lists** — From each prompt's YAML frontmatter, grab the `skills:` array
3. **Deduplicate** — Combine across all files into a unique set
4. **Classify** — Split into core skills (used in `skills:` section) vs referenced skills (mentioned in `dependencies:` or `metadata.hermes.related_skills:`)

## Output

Write a batch context file (e.g., `.hermes/plans/batch-context.md`) with:

```markdown
# Batch Context — All Prompts

## Targets
| # | File | Skills Used |
|---|------|-------------|
| 1 | `prompt-a.md` | skill-1, skill-2, skill-3 |
| 2 | `prompt-b.md` | skill-2, skill-4 |

## All Unique Skills
1. skill-1
2. skill-2
3. ...
```

## Integration with skill-judge

After extracting the unique skill list, pipe to `skill-judge --batch` for evaluation:

```
extracted skills → skill-judge --batch skill1 skill2 ...
                 → score report
                 → fix any below-threshold skills
                 → verify all ≥ 80
```

## Pitfalls

- **YAML `skills:` syntax varies** — Some prompts use `- skill-name` (list), some use inline arrays `[skill-1, skill-2]`. Handle both in extraction.
- **Dependencies section** — `dependencies:` often duplicates `skills:` but may include additional items (e.g., `- provider:hermes-auth`). Filter out non-skill deps.
- **Related skills metadata** — Check `metadata.hermes.related_skills` for additional skill references not in the `skills:` field.
- **gh-cli** type references — External CLI tools listed in skills/deps are NOT skill-judge targets. Filter by checking existence: if `skill_view(name)` fails, it's not a Hermes skill.
