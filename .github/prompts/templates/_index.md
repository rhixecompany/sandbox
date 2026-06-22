# Prompt Templates Index

> Generated: 2026-06-22  
> Location: `.github/prompts/templates/`

This directory contains extracted template files for each prompt in `.github/prompts/`. Each subdirectory follows the prompt name (stem of `.prompt.md`).

## Structure

```
templates/
├── _shared/                    # Shared/reusable templates
│   ├── frontmatter.md          # YAML frontmatter patterns
│   ├── skill-refs.md           # Common skill references
│   └── verification-checklist.md  # Standard verification gates
├── _index.md                   # This file
├── <prompt-name>/              # Per-prompt template folder
│   ├── README.md               # Section inventory + usage notes
│   ├── <extracted-section>.md  # Extracted long sections
│   └── ...
└── ...
```

## Shared Templates

| Template | Purpose |
|----------|---------|
| `_shared/frontmatter.md` | Reusable YAML frontmatter patterns (Hermes + Copilot styles) |
| `_shared/skill-refs.md` | Standard Hermes skill reference table |
| `_shared/verification-checklist.md` | Common verification gate patterns |

## Per-Prompt Templates

Each template folder contains:
1. `README.md` — Section inventory, size, frontmatter type, usage notes
2. Extracted long sections (when applicable, sections >40 lines)
3. Additional reference templates (when applicable)

## DRY Principles

- Shared patterns live in `_shared/` — referenced by multiple prompts
- Per-prompt templates contain *only* content specific to that prompt
- Prompts should cross-reference templates instead of duplicating content
- Long sections (>40 lines) should be extracted to template files
