#!/usr/bin/env bash
git checkout -b skills-migration/batch-12
git add \
  "78|.opencode/skills/context7/README.md" \
  "79|.opencode/skills/context7/SKILL.md" \
  "80|.opencode/skills/customize-opencode/SKILL.md" \
  "81|.opencode/skills/datadog/reference/installation.md" \
  "82|.opencode/skills/datadog/SKILL.md" \
  "83|.opencode/skills/dispatching-parallel-agents/SKILL.md" \
  "84|.opencode/skills/doc-coauthoring/SKILL.md" \

git commit -m "chore(skills): migrate batch 12 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-12  # commented out — requires approval