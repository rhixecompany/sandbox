# Prompts Context Catalog

## Scope
- Target: prompts/*.prompt.md
- Total files: 250
- All YAML valid: Yes (250/250)

## Format
All files use YAML frontmatter with `.prompt.md` extension.
Required fields: name, title, description, tags, version, author, license.

## Dependency Map
- Many prompts reference skills via `skills:` frontmatter field
- Some prompts reference other prompts via `dependencies:` field
- Common `/command` triggers map to filename stems

## Prior Work
- Phase 1 (YAML tags fix): 97 broken `tags: []` patterns fixed
- Phase 2 (Colon/bleed fixes): 6 files with structural YAML issues fixed
