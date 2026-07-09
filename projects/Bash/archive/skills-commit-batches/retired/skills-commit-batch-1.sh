#!/usr/bin/env bash
# DRY_RUN_SUPPORT=true
DRY_RUN=${DRY_RUN:-false}
for arg in "$@"; do
  if [ "$arg" = "--dry-run" ] || [ "$arg" = "-n" ]; then DRY_RUN=true; fi
done
if [ "$DRY_RUN" = "true" ]; then
  echo "DRY-RUN: $(basename "$0") would prepare git commit batch 1 (no side effects)."
  exit 0
fi

git checkout -b skills-migration/batch-1
git add \
  ".opencode/skills/agent-browser/SKILL.md" \
  ".opencode/skills/algorithmic-art/SKILL.md" \
  ".opencode/skills/asdf/references/plugin-install.md" \
  ".opencode/skills/asdf/SKILL.md" \
  ".opencode/skills/banking/reference/dal-patterns.md" \
  ".opencode/skills/banking/reference/idempotency-key-pattern.md" \
  ".opencode/skills/banking/reference/testing.md" \

git commit -m "chore(skills): migrate batch 1 — normalize frontmatter and fix formatting (author: Alexa)"
# git push origin skills-migration/batch-1  # commented out — requires approval
