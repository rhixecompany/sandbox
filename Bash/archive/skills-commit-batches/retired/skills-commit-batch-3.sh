#!/usr/bin/env bash
git checkout -b skills-migration/batch-3
git add \
  "15|.opencode/skills/caveman-unified/SKILL.md" \
  "16|.opencode/skills/claude-api/csharp/claude-api.md" \
  "17|.opencode/skills/claude-api/curl/examples.md" \
  "18|.opencode/skills/claude-api/curl/managed-agents.md" \
  "19|.opencode/skills/claude-api/go/claude-api.md" \
  "20|.opencode/skills/claude-api/go/managed-agents/README.md" \
  "21|.opencode/skills/claude-api/java/claude-api.md" \

git commit -m "chore(skills): migrate batch 3 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-3  # commented out — requires approval