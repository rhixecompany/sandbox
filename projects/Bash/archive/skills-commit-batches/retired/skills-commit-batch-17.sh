#!/usr/bin/env bash
git checkout -b skills-migration/batch-17
git add \
  "113|.opencode/skills/marp-slide/assets/template-tech.md" \
  "114|.opencode/skills/marp-slide/references/advanced-features.md" \
  "115|.opencode/skills/marp-slide/references/best-practices.md" \
  "116|.opencode/skills/marp-slide/references/image-patterns.md" \
  "117|.opencode/skills/marp-slide/references/marp-syntax.md" \
  "118|.opencode/skills/marp-slide/references/official-themes.md" \
  "119|.opencode/skills/marp-slide/references/theme-css-guide.md" \

git commit -m "chore(skills): migrate batch 17 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-17  # commented out — requires approval