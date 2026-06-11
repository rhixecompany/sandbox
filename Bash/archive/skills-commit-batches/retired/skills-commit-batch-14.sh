#!/usr/bin/env bash
git checkout -b skills-migration/batch-14
git add \
  "92|.opencode/skills/glab/references/quick-reference.md" \
  "93|.opencode/skills/glab/references/troubleshooting.md" \
  "94|.opencode/skills/glab/SKILL.md" \
  "95|.opencode/skills/httpie/SKILL.md" \
  "96|.opencode/skills/humanizer/references/anti-patterns.md" \
  "97|.opencode/skills/humanizer/references/patterns-reference.md" \
  "98|.opencode/skills/humanizer/SKILL.md" \

git commit -m "chore(skills): migrate batch 14 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-14  # commented out — requires approval