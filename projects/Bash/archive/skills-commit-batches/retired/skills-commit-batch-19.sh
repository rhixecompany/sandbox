#!/usr/bin/env bash
git checkout -b skills-migration/batch-19
git add \
  "127|.opencode/skills/mcp-builder/SKILL.md" \
  "128|.opencode/skills/meeting-insights-analyzer/references/behavioral-patterns.md" \
  "129|.opencode/skills/meeting-insights-analyzer/references/bias-mitigation.md" \
  "130|.opencode/skills/meeting-insights-analyzer/references/edge-cases.md" \
  "131|.opencode/skills/meeting-insights-analyzer/references/frameworks.md" \
  "132|.opencode/skills/meeting-insights-analyzer/SKILL.md" \
  "133|.opencode/skills/mermaid-diagrams/references/advanced-features.md" \

git commit -m "chore(skills): migrate batch 19 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-19  # commented out — requires approval