#!/usr/bin/env bash
git checkout -b skills-migration/batch-13
git add \
  "85|.opencode/skills/docx/SKILL.md" \
  "86|.opencode/skills/executing-plans/SKILL.md" \
  "87|.opencode/skills/file-organizer/SKILL.md" \
  "88|.opencode/skills/finishing-a-development-branch/SKILL.md" \
  "89|.opencode/skills/frontend-design/SKILL.md" \
  "90|.opencode/skills/git-helper/SKILL.md" \
  "91|.opencode/skills/glab/references/commands-detailed.md" \

git commit -m "chore(skills): migrate batch 13 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-13  # commented out — requires approval