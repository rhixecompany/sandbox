#!/usr/bin/env bash
git checkout -b skills-migration/batch-5
git add \
  "29|.opencode/skills/claude-api/python/claude-api/tool-use.md" \
  "30|.opencode/skills/claude-api/python/managed-agents/README.md" \
  "31|.opencode/skills/claude-api/ruby/claude-api.md" \
  "32|.opencode/skills/claude-api/ruby/managed-agents/README.md" \
  "33|.opencode/skills/claude-api/shared/agent-design.md" \
  "34|.opencode/skills/claude-api/shared/error-codes.md" \
  "35|.opencode/skills/claude-api/shared/live-sources.md" \

git commit -m "chore(skills): migrate batch 5 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-5  # commented out — requires approval