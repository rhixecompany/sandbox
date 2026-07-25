# Generic Boilerplate Markers

Detect injected generic sections after a bulk fix pass. These five patterns
cover every generic section the automated fixer may inject.

## Checklist

```
- [ ] Prerequisites are verified and available
- [ ] .*operations completed without errors
- [ ] Output verified against expected requirements
- [ ] Configuration changes documented if applicable
- [ ] Final result is ready for use or delivery
```

## Workflow

```
## Workflow

### Phase 1: Setup

Verify prerequisites are in place and configure the environment.
```

## Overview

```
.*skill provides tools and workflows for managing .*operations efficiently.
```

## When to Use

```
- When working with .*tools or services
- When automating or managing .*tasks
- \*\*Triggers\*\*: ".*"
```

## Placeholder H2

Lines matching `^## [a-z][-a-z0-9]+$` that appear immediately before a
generic checklist — these are auto-injected skill-name-as-H2 placeholders.

## Sweep Command

```bash
cd skills
for marker in \
  'Prerequisites are verified' \
  'operations completed without errors' \
  'Document outcomes and store any configuration' \
  'skill provides tools and workflows for managing' \
  'Triggers: "'; do
  count=$(find . -name 'SKILL.md' -exec grep -l "$marker" {} \; | wc -l)
  echo "$marker: $count hits"
done
```

Zero hits across all five markers = clean.
