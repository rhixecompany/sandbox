# DRY Template Convention (prompts/templates/_index.md)

Source of truth for how `prompts/` files reference extracted template content.

## Structure
```
templates/
├── _shared/                    # Shared/reusable templates
│   ├── frontmatter.md
│   ├── skill-refs.md
│   └── verification-checklist.md
├── _index.md                   # This file
├── <prompt-name>/              # Per-prompt template folder (stem of .prompt.md)
│   ├── README.md               # Section inventory + usage notes
│   ├── <extracted-section>.md  # Extracted long sections
│   └── ...
└── ...
```

## Rules
- Shared patterns live in `_shared/` — referenced by multiple prompts.
- Per-prompt templates contain *only* content specific to that prompt.
- Prompts should cross-reference templates instead of duplicating content.
- Long sections (>40 lines) should be extracted to template files.

## Per-prompt folder contents
1. `README.md` — Section inventory, size, frontmatter type, usage notes.
2. Extracted long sections (sections >40 lines).
3. Additional reference templates when applicable.

## Applied during repair
When a `.prompt.md`'s "Template References" lists `templates/<name>/<file>.md`
that is missing, create `<file>.md` with the extracted section body, and add a
`README.md` inventory mapping each file to its source section + line range.
