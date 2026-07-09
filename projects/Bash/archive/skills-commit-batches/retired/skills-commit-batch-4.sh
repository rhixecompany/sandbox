#!/usr/bin/env bash
git checkout -b skills-migration/batch-4
git add \
  "22|.opencode/skills/claude-api/java/managed-agents/README.md" \
  "23|.opencode/skills/claude-api/php/claude-api.md" \
  "24|.opencode/skills/claude-api/php/managed-agents/README.md" \
  "25|.opencode/skills/claude-api/python/claude-api/batches.md" \
  "26|.opencode/skills/claude-api/python/claude-api/files-api.md" \
  "27|.opencode/skills/claude-api/python/claude-api/README.md" \
  "28|.opencode/skills/claude-api/python/claude-api/streaming.md" \

git commit -m "chore(skills): migrate batch 4 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-4  # commented out — requires approval