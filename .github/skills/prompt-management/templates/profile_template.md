---
name: profile_template
description: Skeleton for defining a Hermes profile configuration used in prompts.
---

# Profile Template

## Name
<!-- Profile name, e.g., `default`, `code-architect`, `research-analyst` -->

## Model & Provider
```yaml
model: qwen/qwen3-coder:free
provider: openrouter
```

## Toolsets
```yaml
toolsets:
  - terminal
  - file
  - web
  - skills
  - memory
```

## Personality
<!-- Personality preset, e.g., `professional`, `concise`, `caveman` -->

## Environment Variables
```yaml
env:
  OPENAI_API_KEY: ${OPENAI_API_KEY}
  OPENROUTER_API_KEY: ${OPENROUTER_API_KEY}
```

## Notes
<!-- Any additional configuration or constraints. -->