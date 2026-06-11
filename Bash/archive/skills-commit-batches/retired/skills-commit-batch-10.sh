#!/usr/bin/env bash
git checkout -b skills-migration/batch-10
git add \
  "64|.opencode/skills/code-docs/references/terraform_style.md" \
  "65|.opencode/skills/code-docs/SKILL.md" \
  "66|.opencode/skills/codemap/codemap.md" \
  "67|.opencode/skills/codemap/README.md" \
  "68|.opencode/skills/codemap/SKILL.md" \
  "69|.opencode/skills/content-research-writer/references/anti-patterns.md" \
  "70|.opencode/skills/content-research-writer/references/collaboration-framework.md" \

git commit -m "chore(skills): migrate batch 10 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-10  # commented out — requires approval