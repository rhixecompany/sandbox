# Wiki Schema Template

```markdown
# Wiki Schema

## Domain
[What this wiki covers e.g. "AI/ML research"]

## Conventions
- File names: lowercase, hyphens, no spaces
- Every wiki page starts with YAML frontmatter
- Use [[wikilinks]] to link between pages
- When updating a page bump the updated date
- Every new page must be added to index.md
- Every action must be appended to log.md

## Frontmatter
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: entity | concept | comparison | query | summary
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low
contested: true
contradictions: [other-page-slug]
---
```

## Page Thresholds
- Create a page when an entity appears in 2+ sources
- Add to existing when a source mentions something already covered
- Split a page when it exceeds ~200 lines
- Archive when fully superseded
```
