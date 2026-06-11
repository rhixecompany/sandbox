#!/usr/bin/env bash
git checkout -b skills-migration/batch-21
git add \
  "141|.opencode/skills/pdf/forms.md" \
  "142|.opencode/skills/pdf/reference.md" \
  "143|.opencode/skills/pdf/SKILL.md" \
  "144|.opencode/skills/plans-and-specs/SKILL.md" \
  "145|.opencode/skills/pptx/editing.md" \
  "146|.opencode/skills/pptx/pptxgenjs.md" \
  "147|.opencode/skills/pptx/SKILL.md" \

git commit -m "chore(skills): migrate batch 21 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-21  # commented out — requires approval