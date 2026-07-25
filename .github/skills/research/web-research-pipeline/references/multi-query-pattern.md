# Multi-Query Research Pattern

When research queries are sourced from a structured document (e.g., `per-project-research-queries.md` with numbered sections), use this pattern:

## Workflow

```python
# 1. Parse queries from source document
queries = extract_queries("docs/per-project-research-queries.md", project="ecom")

# 2. For each query, run search + extract
all_findings = []
for q in queries:
    urls = web_search(query=q, limit=8)['data']['web']
    # Prioritize: official docs > tutorials > recent articles > forums
    urls = rank_urls(urls, prefer_domains=["docs.", "developer.", "github.com", "readthedocs.io"])
    content = web_extract(urls=urls[:5], char_limit=15000)
    all_findings.append({"query": q, "sources": content})

# 3. Synthesize into existing report (UPDATE mode)
report = read_file("projects/ecom/RESEARCH_REPORT.md")
updated = merge_findings(report, all_findings, mode="UPDATE")
write_file("projects/ecom/RESEARCH_REPORT.md", updated)
```

## Query Extraction Helper

```python
def extract_queries(path, project):
    """Parse per-project-research-queries.md, return list for given project."""
    import re
    content = read_file(path)
    # Find section for project (## N. project-name)
    pattern = rf"## \d+\.\s*{project}\n\*\*Tech Stack:\*\*.*?\n\*\*Queries:\*\*\n((?:- .+\n)*)"
    match = re.search(pattern, content, re.DOTALL | re.IGNORECASE)
    if not match:
        return []
    query_lines = match.group(1).strip().split('\n')
    return [line[2:].strip() for line in query_lines if line.startswith('- ')]
```

## URL Ranking Heuristic

```python
PREFERRED_DOMAINS = [
    "docs.", "developer.", "readthedocs.io", "github.com",
    "django-rest-framework.org", "redux-toolkit.js.org",
    "paypal.com", "developer.paypal.com",
    "vite.dev", "django-rest-framework-simplejwt.readthedocs.io",
]

def rank_urls(urls, prefer_domains=PREFERRED_DOMAINS):
    def score(url):
        from urllib.parse import urlparse
        host = urlparse(url).netloc.lower()
        for i, pref in enumerate(prefer_domains):
            if pref in host:
                return 100 - i
        # Penalize: youtube, reddit, facebook, stackoverflow (unless code)
        for bad in ["youtube.com", "facebook.com", "reddit.com"]:
            if bad in host:
                return -10
        return 0
    return sorted(urls, key=score, reverse=True)
```

## UPDATE Mode Merge Strategy

| Existing Section | Action |
|------------------|--------|
| Key Findings | Append new subsections; deduplicate by topic |
| Cheatsheets | Add new rows; keep alphabetical |
| Best Practices | Append numbered items; renumber |
| Common Pitfalls | Add new rows; avoid duplicates |
| Performance | Append new techniques |
| Security | Append new measures |
| Resources | Add new links; dedupe by URL |
| **New Findings (date)** | Always append timestamped section at end |

## Template: New Findings Section

```markdown
---

## New Findings (YYYY-MM-DD Update)

### [Topic from Query N]

- Finding 1 with [source](url)
- Finding 2 with [source](url)

### [Topic from Query N+1]

...
```