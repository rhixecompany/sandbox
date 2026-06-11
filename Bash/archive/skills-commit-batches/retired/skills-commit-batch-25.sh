#!/usr/bin/env bash
git checkout -b skills-migration/batch-25
git add \
  "169|.opencode/skills/simplify/SKILL.md" \
  "170|.opencode/skills/skill-creator/agents/analyzer.md" \
  "171|.opencode/skills/skill-creator/agents/comparator.md" \
  "172|.opencode/skills/skill-creator/agents/grader.md" \
  "173|.opencode/skills/skill-creator/references/schemas.md" \
  "174|.opencode/skills/skill-creator/SKILL.md" \
  "175|.opencode/skills/skill-judge/SKILL.md" \

git commit -m "chore(skills): migrate batch 25 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-25  # commented out — requires approval