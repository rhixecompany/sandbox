#!/usr/bin/env bash
git checkout -b skills-migration/batch-11
git add \
  "71|.opencode/skills/content-research-writer/references/decision-trees.md" \
  "72|.opencode/skills/content-research-writer/references/examples.md" \
  "73|.opencode/skills/content-research-writer/references/philosophy.md" \
  "74|.opencode/skills/content-research-writer/references/workflows/blog-post.md" \
  "75|.opencode/skills/content-research-writer/SKILL.md" \
  "76|.opencode/skills/context7/library-registry.md" \
  "77|.opencode/skills/context7/navigation.md" \

git commit -m "chore(skills): migrate batch 11 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-11  # commented out — requires approval