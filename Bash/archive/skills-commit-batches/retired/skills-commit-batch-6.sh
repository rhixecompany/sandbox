#!/usr/bin/env bash
git checkout -b skills-migration/batch-6
git add \
  "36|.opencode/skills/claude-api/shared/managed-agents-api-reference.md" \
  "37|.opencode/skills/claude-api/shared/managed-agents-client-patterns.md" \
  "38|.opencode/skills/claude-api/shared/managed-agents-core.md" \
  "39|.opencode/skills/claude-api/shared/managed-agents-environments.md" \
  "40|.opencode/skills/claude-api/shared/managed-agents-events.md" \
  "41|.opencode/skills/claude-api/shared/managed-agents-memory.md" \
  "42|.opencode/skills/claude-api/shared/managed-agents-multiagent.md" \

git commit -m "chore(skills): migrate batch 6 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-6  # commented out — requires approval