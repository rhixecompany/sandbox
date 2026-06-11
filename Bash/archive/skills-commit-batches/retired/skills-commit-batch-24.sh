#!/usr/bin/env bash
git checkout -b skills-migration/batch-24
git add \
  "162|.opencode/skills/shadcn/rules/composition.md" \
  "163|.opencode/skills/shadcn/rules/forms.md" \
  "164|.opencode/skills/shadcn/rules/icons.md" \
  "165|.opencode/skills/shadcn/rules/styling.md" \
  "166|.opencode/skills/shadcn/SKILL.md" \
  "167|.opencode/skills/simplify/codemap.md" \
  "168|.opencode/skills/simplify/README.md" \

git commit -m "chore(skills): migrate batch 24 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-24  # commented out — requires approval