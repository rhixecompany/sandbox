# Web Research Pipeline Reference

## Architecture
```
User Query → Web Search → Content Extraction → Synthesis → Report
    1. web_search(query) → URLs
    2. web_extract(urls) → markdown
    3. Filter/rank results
    4. Synthesize findings
    5. Generate structured report
```

## Search Strategies
| Strategy | When | Query Tips |
|----------|------|------------|
| Broad | Exploratory research | Use minimal keywords, no operators |
| Targeted | Specific facts | site:domain, "exact phrase", filetype:pdf |
| Comparative | Multiple sources | Use OR, different phrasings |
| Temporal | Current events | Add date filter: after:2025-01-01 |

## Extraction Options
- **web_extract(urls)** — Clean markdown from URLs, preferred for docs/blogs
- **browser_navigate** + **browser_snapshot** — For JS-heavy pages
- **mcp_fetch_get_markdown** — MCP-first alternative for URL fetch

## Common Filters
```python
def deduplicate(results, key="url"):
    seen = set()
    return [r for r in results if not (r[key] in seen or seen.add(r[key]))]

def score_relevance(results, keywords):
    for r in results:
        r["relevance"] = sum(
            kw.lower() in (r.get("content", "") + r.get("title", "")).lower()
            for kw in keywords
        )
    return sorted(results, key=lambda x: x["relevance"], reverse=True)
```

## Pipeline Patterns

### Rapid Overview (3-5 URLs)
1. Web search → pick top 3-5 results
2. Extract all in parallel
3. Synthesize key points into paragraph

### Deep Dive (10-20 URLs)  
1. Web search → extract links
2. Extract each page
3. Categorize findings by theme
4. Write structured report with sections

### Comparative (2+ products/technologies)
1. Search each topic separately
2. Extract feature lists
3. Build comparison table
4. Pros/cons analysis
