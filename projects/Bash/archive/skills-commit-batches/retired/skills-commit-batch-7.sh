#!/usr/bin/env bash
git checkout -b skills-migration/batch-7
git add \
  "43|.opencode/skills/claude-api/shared/managed-agents-onboarding.md" \
  "44|.opencode/skills/claude-api/shared/managed-agents-outcomes.md" \
  "45|.opencode/skills/claude-api/shared/managed-agents-overview.md" \
  "46|.opencode/skills/claude-api/shared/managed-agents-tools.md" \
  "47|.opencode/skills/claude-api/shared/managed-agents-webhooks.md" \
  "48|.opencode/skills/claude-api/shared/model-migration.md" \
  "49|.opencode/skills/claude-api/shared/models.md" \

git commit -m "chore(skills): migrate batch 7 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-7  # commented out — requires approval