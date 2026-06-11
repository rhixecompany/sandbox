#!/usr/bin/env bash
git checkout -b skills-migration/batch-8
git add \
  "50|.opencode/skills/claude-api/shared/prompt-caching.md" \
  "51|.opencode/skills/claude-api/shared/tool-use-concepts.md" \
  "52|.opencode/skills/claude-api/SKILL.md" \
  "53|.opencode/skills/claude-api/typescript/claude-api/batches.md" \
  "54|.opencode/skills/claude-api/typescript/claude-api/files-api.md" \
  "55|.opencode/skills/claude-api/typescript/claude-api/README.md" \
  "56|.opencode/skills/claude-api/typescript/claude-api/streaming.md" \

git commit -m "chore(skills): migrate batch 8 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-8  # commented out — requires approval