#!/usr/bin/env bash
git checkout -b skills-migration/batch-26
git add \
  "176|.opencode/skills/slack-gif-creator/SKILL.md" \
  "177|.opencode/skills/subagent-driven-development/code-quality-reviewer-prompt.md" \
  "178|.opencode/skills/subagent-driven-development/implementer-prompt.md" \
  "179|.opencode/skills/subagent-driven-development/SKILL.md" \
  "180|.opencode/skills/subagent-driven-development/spec-reviewer-prompt.md" \
  "181|.opencode/skills/systematic-debugging/condition-based-waiting.md" \
  "182|.opencode/skills/systematic-debugging/CREATION-LOG.md" \

git commit -m "chore(skills): migrate batch 26 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-26  # commented out — requires approval