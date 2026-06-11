---
name: validate-memories
title: Validate Memories
category: devops
description: "Validate that USER.md and MEMORY.md exist and meet simple schema checks in the Hermes install folder. Useful as a local guard and CI job."
---

# validate-memories skill

This skill provides a small validator script and CI workflow to ensure the Hermes memory files are present and conform to a minimal schema. Use when you want automatic drift detection of the agent's local memory artifacts.

Files included:

- scripts/validate_memories.py - the validator
- scripts/ci_validate_memories.sh - a small wrapper to run the validator in CI
- .github/workflows/validate_memories.yml - GitHub Actions workflow to run validation on changes

Usage:

1. Edit the paths in scripts/validate_memories.py if your Hermes home is in a different location. Default path used: C:\\Users\\Alexa\\AppData\\Local\\hermes
2. Run the validator locally: python scripts/validate_memories.py
3. The workflow runs automatically on pushes and PRs touching the memories or scripts paths.

Pitfalls:
- This is intentionally lightweight; adapt rules for stricter checks if needed.

User preferences encoded:
- Do NOT create backup files (.bak) when editing existing files. Validator and automation scripts SHOULD honor the local policy file at C:\\Users\\Alexa\\AppData\\Local\\hermes\\.hermes_policies (key: [backup].enabled = false) and overwrite in-place unless explicitly asked to preserve backups.
- The validator is a quick smoke test. For stricter enforcement, add schema checks in the script under scripts/validate_memories.py and register them with this skill's templates/


## When to Use


- you want automatic drift detection of the agent's local memory artifacts
- **Triggers**: "validate memories" required for a project


