#!/usr/bin/env bash
git checkout -b skills-migration/batch-16
git add \
  "106|.opencode/skills/jira/SKILL.md" \
  "107|.opencode/skills/marp-slide/assets/template-basic.md" \
  "108|.opencode/skills/marp-slide/assets/template-business.md" \
  "109|.opencode/skills/marp-slide/assets/template-colorful.md" \
  "110|.opencode/skills/marp-slide/assets/template-dark.md" \
  "111|.opencode/skills/marp-slide/assets/template-gradient.md" \
  "112|.opencode/skills/marp-slide/assets/template-minimal.md" \

git commit -m "chore(skills): migrate batch 16 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-16  # commented out — requires approval