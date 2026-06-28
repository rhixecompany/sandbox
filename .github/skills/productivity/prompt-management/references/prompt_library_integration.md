# Prompt Library Integration Guide

## Purpose
Enable reuse of existing prompts from internal or external libraries without duplicating logic.

---

## Discovery
### Local Prompts
```bash
# Find all .md files in prompts/ directory
search_files pattern="prompts/.*\\.md$" target=files
```

### External Libraries
- **Hermes Community Prompts** – `https://github.com/hermes-ai/prompt-library`
- **GitHub Prompts** – `https://github.com/<org>/<repo>/prompts`
- **Custom Registry** – Configured via `prompt_libraries` in `~/.hermes/config.yaml`

---

## Import Workflow
1. **Search** – Use `search_files` or `web_search` to locate candidate prompts.
2. **Fetch** – `web_extract` or `read_file` to retrieve the full prompt markdown.
3. **Analyze** – Parse front‑matter and sections; map to our template fields.
4. **Adapt** – Create a new prompt under `prompts/<name>.md` using `prompt_template.md` as base.
   - Copy compatible sections (Plans‑and‑Specs, Scripts, etc.).
   - Replace or merge profile/persona/toolset declarations.
5. **Validate** – Run the Verification Checklist from the skill.
6. **Commit** – `git add` the new prompt; optionally tag with source.

---

## Sub‑agent Import
For large libraries, delegate the import to a sub‑agent:

```json
{
  "goal": "Import all prompts from <library-url> into prompts/ directory, adapting each to our template.",
  "context": "Target template: templates/prompt_template.md. Use search_files to list candidates.",
  "toolsets": ["web", "file", "terminal"]
}
```

---

## Version Tracking
Store library source metadata in the imported prompt’s front‑matter:

```yaml
source:
  library: "hermes-community"
  url: "https://github.com/hermes-ai/prompt-library/blob/main/prompts/data-ingest.md"
  version: "v1.2.0"
  imported_at: "2026-06-24"
```

---

## Updating Imported Prompts
1. Check upstream for changes (`git fetch` or revisit URL).
2. Diff the upstream version against local copy.
3. Apply updates via the **Update Prompt** workflow (Phase 2).
4. Bump `version` in front‑matter and record changelog.

---

## CI Integration
See `.github/workflows/prompt-library-sync.yml` for automated nightly sync (optional).