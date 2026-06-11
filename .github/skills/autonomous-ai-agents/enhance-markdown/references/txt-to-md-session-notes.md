# TXT → Markdown Session Notes

This reference captures the practical lessons learned while converting `Prompts/*.txt` prompts into structured `.md` docs.

## Durable workflow notes

- Back up existing target `.md` files before overwriting them during batch conversions.
- Use a timestamped backup path such as `docs/prompt-backups/<YYYYMMDD-HHMMSSZ>/Prompts/`.
- Leave the `.txt` source files untouched; treat them as read-only references.
- When the prompt family includes command-style docs, keep the generated `.md` aligned to the required structural sections and preserve the source intent rather than inventing new behavior.
- After writing, do a quick section-presence verification against the required headings to catch omissions early.

## Common pitfall

- The source `.txt` prompts may be terse or inconsistent, so the conversion step should normalize structure while keeping the original task flow and file references intact.
