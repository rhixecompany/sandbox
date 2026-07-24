---
name: suggest-awesome-github-copilot-skills
description: Find GitHub Copilot skills from the awesome-copilot catalog that add coverage the repo lacks, and flag local duplicates or outdated copies.
---

# Suggest Awesome GitHub Copilot Skills

Suggest GitHub Copilot skills that add coverage the repo lacks, and flag local
duplicates or outdated copies.

## When to use

- Auditing or extending the repo's Copilot skills library.
- Onboarding a project that may benefit from community (`awesome-copilot`) skills.
- Before adding a new skill, to avoid duplicating an existing local skill.

## Process

1. **Fetch available skills** from the `github/awesome-copilot` catalog:
   - Enumerate `https://github.com/github/awesome-copilot/tree/main/skills`.
   - For each skill, read its `SKILL.md` (`description` + bundled assets).
2. **Scan local skills** in `.github/prompts/skills/` (or the repo's skill location):
   - For each folder, read `SKILL.md` front matter (`name`, `description`).
   - List any bundled assets inside the folder.
   - Build a local inventory to avoid suggesting duplicates.
3. **Detect outdated copies**: for each local skill, fetch the remote
   `SKILL.md` from
   `https://raw.githubusercontent.com/github/awesome-copilot/main/skills/<skill-name>/SKILL.md`
   and diff it against the local file (front matter, instructions, assets).
4. **Analyze repo context**: languages (.cs/.js/.py/.ts), frameworks
   (ASP.NET, React, Next.js…), project types, workflow needs (testing, CI/CD,
   deployment), and cloud providers (Azure/AWS/GCP).
5. **Produce the comparison table** below.

## Output Format

| Awesome-Copilot Skill | Description | Bundled Assets | Already Installed | Similar Local Skill | Suggestion Rationale |
| --- | --- | --- | --- | --- | --- |
| [gh-cli](https://github.com/github/awesome-copilot/tree/main/skills/gh-cli) | GitHub CLI skill for managing repositories and workflows | None | ❌ No | None | Would enhance GitHub workflow automation capabilities |
| [aspire](https://github.com/github/awesome-copilot/tree/main/skills/aspire) | Aspire skill for distributed application development | 9 reference files | ✅ Yes | aspire | Already covered by existing Aspire skill |
| [terraform-azurerm-set-diff-analyzer](https://github.com/github/awesome-copilot/tree/main/skills/terraform-azurerm-set-diff-analyzer) | Analyze Terraform AzureRM provider changes | Reference files | ⚠️ Outdated | terraform-azurerm-set-diff-analyzer | Instructions updated with new validation patterns - Update recommended |

## Icons

- ✅ Already installed and up-to-date
- ⚠️ Installed but outdated (update available)
- ❌ Not installed in repo

## Local Skills Discovery

1. List all folders in `.github/prompts/skills/`.
2. For each folder, read `SKILL.md` front matter for `name` and `description`.
3. List bundled assets in each folder.
4. Build the inventory; use it to avoid duplicate suggestions.

## Version Comparison

1. For each local skill, build the raw URL
   `https://raw.githubusercontent.com/github/awesome-copilot/main/skills/<skill-name>/SKILL.md`.
2. Fetch it and compare the entire file (front matter, instructions, assets).
3. Document specific differences for outdated skills.

## Update Handling

When an outdated skill is identified:

1. Include it in the table with ⚠️ status.
2. Document the specific differences in the rationale column.
3. Recommend the update with key changes noted.
4. If the user requests the update, replace the entire local skill folder with
   the remote version, preserving its location in `.github/prompts/skills/`.
5. Download all bundled assets alongside the updated `SKILL.md`.

## Notes

- awesome-copilot `SKILL.md` front matter format:

  ```markdown
  ---
  name: "skill-name"
  description: "Brief description of what this skill provides and when to use it"
  ---
  ```

- Each skill is a folder: `SKILL.md` + optional bundled assets; folder name
  lowercase-hyphenated and must match the `name` field.
- Output only the table and the analysis — no extra commentary.
