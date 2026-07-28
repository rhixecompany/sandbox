# technology-stack-blueprint-generator Template

Prompt: technology-stack-blueprint-generator.prompt.md
Lines: ~150
Templates: 1

## Templates

- `generated_prompt.md` — Canonical execution instructions and output templates

## Quick Start

```bash
# Run the prompt to generate tech stack docs for all projects
hermes run technology-stack-blueprint-generator
```

## Output Structure

```
SandBox/
├── Technology_Stack_Blueprint.md           # Master workspace blueprint
└── projects/
    ├── Banking/
    │   └── TECHNOLOGY_STACK.md             # Per-project tech stack
    ├── Bash/
    │   └── TECHNOLOGY_STACK.md
    ├── comicwise/
    │   └── TECHNOLOGY_STACK.md
    └── ... (all projects)
```

## Key Features

- **Per-project output**: Each project gets its own TECHNOLOGY_STACK.md in its root directory
- **Master blueprint**: Cross-project analysis at workspace root
- **Version accuracy**: All versions traced to actual config files
- **Multi-language**: Supports 12+ languages/runtimes
- **Idempotent**: Safe to re-run anytime