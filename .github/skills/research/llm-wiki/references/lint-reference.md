# Wiki Lint Checklist

## Orphan Pages
Find pages with no inbound [[wikilinks]]:
- Scan all .md files in entities/, concepts/, comparisons/, queries/
- Extract all [[wikilinks]] and build inbound link map
- Pages with zero inbound links are orphans

## Full Lint Checklist
1. Broken wikilinks - links to nonexistent pages
2. Index completeness - every page in index.md
3. Frontmatter validation - required fields, tags in taxonomy
4. Stale content - updated >90 days behind sources
5. Contradictions - contested pages or conflicting claims
6. Quality signals - low confidence or single-source pages
7. Source drift - sha256 mismatches on raw/ files
8. Page size - flag pages over 200 lines
9. Tag audit - tags not in SCHEMA.md taxonomy
10. Log rotation - rotate log.md if >500 entries
