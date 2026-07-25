# Class Pattern Reference — plans-and-specs

## Prompt File Conversion (Class Pattern)

For projects that maintain `.prompt.md` files (Copilot/Hermes/OpenCode prompts) and need to convert plaintext `.txt` drafts into properly formatted prompt files.

### 4-Phase Conversion Model

1. **INVENTORY** — Catalog all `.txt` sources and existing `.prompt.md` targets; identify which are plaintext vs. already formatted
2. **STRUCTURE** — For each plaintext source, produce a formatted `.prompt.md` with:
   - YAML frontmatter (`title`, `trigger`, `tags`)
   - `## Skills Required` table (skill name + purpose)
   - Phased workflow (`Phase 1..N` with steps and verification)
   - `## Description` / `## Goal` / `## Overview` narrative sections
3. **FORMAT & CONSISTENCY** — Apply uniform header levels, list style, code-block annotations, and verification checklists across all files in the batch
4. **VERIFY** — Confirm frontmatter validity, section completeness, and cross-reference consistency

### File Convention

```
target-path/
├── my-prompt.prompts.txt         # Plaintext source (short-form)
├── my-prompt.prompts.md          # Formatted output (frontmatter + phases)
└── .github/prompts/task.prompt.md  # Production prompt (full .prompt.md spec)
```

### Key Patterns

- **Frontmatter first**: Every `.prompt.md` must open with `---` delimited YAML (title, trigger, tags)
- **Trigger match**: The `trigger: /name` in frontmatter should match the filename stem
- **Skills Required**: Always present as a markdown table with Skill and Purpose columns
- **Phased structure**: Use `Phase N: Title` with numbered steps or sub-tables
- **Verification checklist**: Close every prompt file with a bullet checklist of acceptance criteria

See `templates/prompt-file-conventions.md` for the frontmatter template, section templates, and real file-name conventions used in the SandBox repo.
