---
name: suggest-awesome-github-copilot-skills-templates
title: Suggest Awesome Copilot Skills — Template Folder
description: Extracted long sections for suggest-awesome-github-copilot-skills.prompt.md
version: 1.0.0
tags: [template, suggest-awesome-github-copilot-skills]
---

# suggest-awesome-github-copilot-skills — Template Folder

Extracted sections referenced by `prompts/suggest-awesome-github-copilot-skills.prompt.md`.
Kept here per the DRY convention in `prompts/templates/_index.md` (long sections >40 lines
are extracted to per-prompt template files; prompts cross-reference instead of duplicating).

## Section Inventory

| File                              | Source Section                 | Lines (approx) |
| --------------------------------- | ------------------------------ | -------------- |
| `rules.md`                        | Rules                          | 55–62          |
| `phases.md`                       | Phases                         | 64–84          |
| `process.md`                      | Process                        | 86–91          |
| `inputs.md`                       | Inputs                         | 44–48          |
| `context_analysis_criteria.md`    | Context Analysis Criteria      | 93–109         |
| `output_format.md`                | Output Format                  | 111–119        |
| `local_skills_discovery_pr.md`    | Local Skills Discovery Process | 121–127        |
| `version_comparison_process.md`   | Version Comparison Process     | 129–140        |
| `skill_structure_requirements.md` | Skill Structure Requirements   | 142–149        |
| `front_matter_structure.md`       | Front Matter Structure         | 151–160        |
| `requirements.md`                 | Requirements                   | 162–176        |
| `icons_reference.md`              | Icons Reference                | 178–182        |
| `update_handling.md`              | Update Handling                | 184–194        |

## Usage Notes

- The main `.prompt.md` inlines a summary of each section; this folder holds the
  canonical, full versions.
- Filenames were corrected from the original manifest typos:
  `skill_structure_requireme.md` → `skill_structure_requirements.md`,
  `version_comparison_proces.md` → `version_comparison_process.md`.
