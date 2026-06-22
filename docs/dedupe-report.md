# Deduplication Report
**Total unique skill names:** 352
**Skills with duplicate paths:** 9
**Potential overlaps (similar names):** 0

## Duplicate Paths (Same Name, Multiple Locations)
| Skill | Paths | Lines | Canonical? |
|-------|-------|-------|------------|
| baoyu-article-illustrator | baoyu-article-illustrator | 207 | ❌ |
| baoyu-article-illustrator | creative\baoyu-article-illustrator | 227 | ✅ |
| baoyu-comic | baoyu-comic | 248 | ❌ |
| baoyu-comic | creative\baoyu-comic | 181 | ✅ |
| chainlink | blockchain\chainlink | 76 | ✅ |
| chainlink | chainlink | 75 | ❌ |
| creative-ideation | creative\creative-ideation | 152 | ✅ |
| creative-ideation | creative-ideation | 177 | ❌ |
| peft | mlops\peft | 436 | ✅ |
| peft | peft | 435 | ❌ |
| pixel-art | creative\pixel-art | 246 | ✅ |
| pixel-art | pixel-art | 218 | ❌ |
| simpo | mlops\simpo | 224 | ✅ |
| simpo | simpo | 223 | ❌ |
| subagent-driven-development | software-development\subagent-driven-development | 272 | ✅ |
| subagent-driven-development | subagent-driven-development | 352 | ❌ |
| watchers | devops\watchers | 113 | ✅ |
| watchers | watchers | 112 | ❌ |

## Potential Overlaps (Similar Names)
| Base Name | Variants | Action |
|-----------|----------|--------|

## Recommended Actions
1. For duplicate paths: Keep the version in the category subdirectory (✅)
2. For overlaps: Merge thin skills into the fuller version
3. Use `skill_manage(action='delete', absorbed_into='<umbrella>')` for merges
4. Use `rm -rf` for true duplicates with identical content
