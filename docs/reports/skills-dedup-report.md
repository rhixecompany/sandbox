# Deduplication Report — audit-skills-judge-fix

## Summary

- Total duplicate pairs found: 67
- Identical root-level copies removed: 14
- Different pairs (need manual review): 1 (claude-code)
- Already deduped or path issues: 52

## Removed (14)

1password, 3-statement-model, accelerate, canvas, chroma, cli, clip,
cloudflare-temporary-deploy, code-wiki, creative-ideation, darwinian-evolver,
dcf-model, drug-discovery, duckduckgo-search

## Different — Manual Review Needed

| Skill | Root size | Category size | Root path | Category path |
|-------|-----------|---------------|-----------|---------------|
| claude-code | 36329 | 34288 | skills/claude-code/ | skills/autonomous-ai-agents/claude-code/ |

## Resolution

- Identical root copies removed (category-level is canonical)
- Different pair flagged — likely the root copy has extra content from a different version
- 52 entries were not duplicated in practice (path parsing gap or already cleaned)
