#!/usr/bin/env bash
git checkout -b skills-migration/batch-2
git add \
  "8|.opencode/skills/banking/reference/validations.md" \
  "9|.opencode/skills/banking/SKILL.md" \
  "10|.opencode/skills/brainstorming/SKILL.md" \
  "11|.opencode/skills/brainstorming/spec-document-reviewer-prompt.md" \
  "12|.opencode/skills/brainstorming/visual-companion.md" \
  "13|.opencode/skills/brand-guidelines/SKILL.md" \
  "14|.opencode/skills/canvas-design/SKILL.md" \

git commit -m "chore(skills): migrate batch 2 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-2  # commented out — requires approval