# Skill Structure Requirements

> Extracted from `suggest-awesome-github-copilot-skills.prompt.md`.

## Skill Structure Requirements

Based on the Agent Skills specification, each skill is a folder containing:

- **`SKILL.md`**: Main instruction file with front matter (`name`, `description`) and detailed instructions
- **Optional bundled assets**: Scripts, templates, reference data, and other files referenced from `SKILL.md`
- **Folder naming**: Lowercase with hyphens (e.g., `azure-deployment-preflight`)
- **Name matching**: The `name` field in `SKILL.md` front matter must match the folder name
