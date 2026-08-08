---
status: completed
---

# Repair Plan: `.github/prompts/*.prompt.md`

Sources of truth per prompt:

- Existing prompt files: `C:\Users\Alexa\Desktop\SandBox\.github/prompts/*.prompt.md`
- Template files: `C:\Users\Alexa\Desktop\SandBox\.github/prompts/templates/<prompt-name>/*.md`

## Phases

### Phase 1: Audit existing prompt files

- Run `find /c/Users/Alexa/Desktop/SandBox/.github/prompts -maxdepth 2 -type f -name "*.prompt.md"` to enumerate prompt files.
- Read each prompt file and parse frontmatter plus canonical content.
- Detect broken/missing references to template paths below `.github/prompts/templates/`.
- Detect via sibling template directories when a matching `.github/prompts/templates/<prompt-name>/` exists.

### Phase 2: Define repair set

- Report exact targets with source-of-truth mapping.
- Group by:
  - existing prompt needs update against its template directory
  - existing prompt needs template directory created/repaired
  - prompt/template pair exists but contents diverge
- Do not write changes until review confirms the repair set.

### Phase 3: Create/update prompt and template files

- For each target, derive the corresponding template root: `.github/prompts/templates/<prompt-name>/`
- Create missing supporting files under that template directory:
  - `phases.md`, `README.md`, `steps.md`, `inputs.md`, `output_format.md`, etc.
  - Use the existing prompt body as source of truth if no template files exist.
- Update the prompt file frontmatter/body to point to the local template files with relative paths.

### Phase 4: Validate all prompts

- Parse frontmatter for all `.github/prompts/*.prompt.md`.
- For each prompt, verify at least one source-of-truth file exists under its template directory.
- Confirm internal references exist and are non-stub.
- Record any remaining invalid files.

### Phase 5: Verify final set

- Re-list `.github/prompts/*.prompt.md` and template directories.
- Output summary table with status, prompt path, template path, and missing files.
