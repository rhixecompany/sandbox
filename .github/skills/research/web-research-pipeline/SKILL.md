---
author: Alexa
description: 'Web search → extract links → scrape full content → save as formatted
  markdown. Use when researching a topic, gathering sources, or building a knowledge
  base from web content. Triggers: research, gather info, web scraping, content collection.'
license: MIT
name: web-research-pipeline
tags:
- research
- web
- scraping
- content
- markdown
title: Web Research Pipeline
version: 1.0.0

---
# Web Research Pipeline

Search the web, extract full content from discovered pages, and save crisply formatted markdown files — one per source — using page titles for filenames.

## When to Use

- Researching a topic from multiple web sources
- Building a knowledge base / reference collection
- Gathering documentation / tutorial content
- Competitive/market research from published content
- Any task that needs "search the web and save everything"

## When NOT to Use

- Single-page extraction (use `web_extract` directly)
- Real-time/live data (use `web_search` directly)
- Internal/private URLs (use `browser` tool)
- Content behind login walls or heavy JS (use `browser` tool)

## Workflow

### Phase 1: Search

Run a targeted `web_search` with a precise query.

```python
from hermes_tools import web_search, web_extract

results = web_search(query="<topic>", limit=10)
```

Rules:
- Use specific, bounded queries ("Python asyncio tutorial site:realpython.com")
- Default limit=10; bump to 20+ for broad topics
- Keep `query` under 120 characters — long queries reduce result quality
- Accept the `web_search` return shape: `{data: {web: [{url, title, description}, ...]}}`

### Phase 2: Extract Content

Collect all discovered URLs from search results, then batch-extract with `web_extract`.

```python
urls = [r['url'] for r in results['data']['web']]
pages = web_extract(urls=urls)
```

Rules:
- `web_extract` accepts max 5 URLs per call — batch in groups of 5
- Handle failures gracefully: check `pages['results']` for `{url, title, content, error}`
- Skip failed URLs silently (log to stderr), continue with successful extractions
- Content is returned as markdown already — do NOT reformat unless broken

### Phase 3: Save as Markdown

Write one `.md` per source page under a topic-named directory.

**Directory naming:**
```
C:\Users\Alexa\Desktop\Sandbox\research\<topic-slug>\
```
- Slug = lowercase, spaces→hyphens, strip special chars
- Create the directory if it doesn't exist (`mcp_filesystem_create_directory` or terminal `mkdir -p`)

**File naming:**
```
<title-slug>.md
```
- Derive slug from the page's `<title>` or `og:title`
- Lowercase, max 60 chars, spaces→hyphens, strip `|:*?"<>`
- If title is missing or generic ("Untitled", "Home", "404"), use the URL domain + path slug
- If slug collision (two pages same title), append `-2`, `-3`, etc.

**File structure per markdown file:**
```markdown
# <Page Title>

> **Source:** <URL>
> **Retrieved:** <ISO-8601 timestamp>

---

<extracted content, unchanged>

---

*Extracted by web-research-pipeline v1.0.0*
```

Rules:
- Preserve extracted content as-is; do not summarize or truncate
- Insert a `---` horizontal rule between metadata and content
- If `web_extract` returned truncated/summarized content (large pages), note it:
  ```markdown
  > ⚠️ Content truncated — original page exceeds extraction limits.
  ```

### Phase 4: Report Summary

After all files are saved, print a summary:

```
## Web Research Pipeline — Summary

**Topic:** <query>
**Sources found:** N
**Successfully extracted:** N
**Failed:** N

### Saved Files
| # | Title | Filename | Size |
|---|-------|----------|------|
| 1 | Real Python asyncio guide | real-python-asyncio-guide.md | 12.4 KB |
| 2 | Python docs asyncio | python-docs-asyncio.md | 8.1 KB |

### Failed URLs (if any)
- https://example.com/blocked (403 Forbidden)

**Output directory:** `research/<topic-slug>/`
```

## Execution Pattern (execute_code)

For an end-to-end run inside `execute_code`, use:

```python
from hermes_tools import web_search, web_extract, terminal
from datetime import datetime
import re, os, json

def slugify(text, max_len=60):
    text = text.lower().strip()
    text = re.sub(r'[|:*?"<>]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'[^a-z0-9\-]', '', text)
    text = re.sub(r'-+', '-', text)
    return text[:max_len].strip('-')

def url_slug(url):
    from urllib.parse import urlparse
    p = urlparse(url)
    host = p.netloc.replace('www.', '')
    path = p.path.strip('/').replace('/', '-')
    slug = f"{host}-{path}" if path else host
    return slugify(slug, 80)

query = "target query here"
output_base = r"C:\Users\Alexa\Desktop\Sandbox\research"

# Phase 1
results = web_search(query=query, limit=10)
urls = [r['url'] for r in results['data']['web']]

# Phase 2 — batch in 5s
all_pages = []
for i in range(0, len(urls), 5):
    batch = urls[i:i+5]
    extracted = web_extract(urls=batch)
    all_pages.extend(extracted['results'])

# Phase 3
slug = slugify(query)
out_dir = os.path.join(output_base, slug)
os.makedirs(out_dir, exist_ok=True)

saved = []
failed = []
existing_slugs = {}

for page in all_pages:
    if page.get('error'):
        failed.append({'url': page['url'], 'error': page['error']})
        continue

    title = page.get('title', '').strip()
    content = page.get('content', '')
    source_url = page['url']

    if not title or title.lower() in ('untitled', 'home', '404', ''):
        title = source_url
        file_slug = url_slug(source_url)
    else:
        file_slug = slugify(title)

    # Deduplicate slugs
    if file_slug in existing_slugs:
        existing_slugs[file_slug] += 1
        file_slug = f"{file_slug}-{existing_slugs[file_slug]}"
    else:
        existing_slugs[file_slug] = 1

    filepath = os.path.join(out_dir, f"{file_slug}.md")
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')

    md = f"# {title}\n\n"
    md += f"> **Source:** {source_url}\n"
    md += f"> **Retrieved:** {now}\n\n"
    md += "---\n\n"
    md += content + "\n\n"
    md += "---\n\n"
    md += "*Extracted by web-research-pipeline v1.0.0*\n"

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(md)

    saved.append({'title': title, 'file': f"{file_slug}.md", 'size': f"{len(md)/1024:.1f} KB", 'url': source_url})

# Phase 4
print(f"\n## Web Research Pipeline — Summary\n")
print(f"**Topic:** {query}")
print(f"**Sources found:** {len(urls)}")
print(f"**Successfully extracted:** {len(saved)}")
print(f"**Failed:** {len(failed)}")
print(f"\n### Saved Files")
print("| # | Title | Filename | Size | URL |")
print("|---|-------|----------|------|-----|")
for i, s in enumerate(saved, 1):
    print(f"| {i} | {s['title'][:50]} | {s['file']} | {s['size']} | {s['url'][:60]}... |")
if failed:
    print(f"\n### Failed URLs")
    for f in failed:
        print(f"- {f['url']} ({f['error']})")
print(f"\n**Output directory:** `{out_dir}`")
```

## Edge Cases & Pitfalls

### Duplicate page titles
Two different pages with the same `<title>` will collide. The slug-dedup logic appends `-2`, `-3`, etc. Always check `existing_slugs` before writing.

### Empty or very short content
Some pages return < 200 chars (paywalls, login walls, JS-rendered apps). Save them anyway but add a warning header:
```markdown
> ⚠️ Minimal content — page may require JavaScript or authentication.
```

### Rate limiting on web_search
`web_search` can return `{error: ...}` at the tool level. If the search itself fails, abort and report — don't proceed with stale/empty URL lists.

### Filename length
Windows paths cap at 260 chars. Keep slugs under 80 chars. If the full path exceeds 240 chars, truncate the slug further.

### Content already in markdown
`web_extract` returns markdown. Do NOT wrap it in code blocks or escape it. Write it as-is after the metadata header.

### Title contains pipe characters
The pipe `|` breaks markdown table rendering in the summary report. Strip `|` from titles when displaying in tables.


## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Skill has clear description with trigger keywords
- [ ] Workflow has 4 numbered phases (Search → Extract → Save → Report)
- [ ] Filename convention documented (title-based slugging)
- [ ] File structure template shown (metadata header + content + footer)
- [ ] Edge cases section covers: duplicates, empty content, rate limits, path length
- [ ] End-to-end execute_code snippet provided and runnable
- [ ] `web_extract` batching (max 5 URLs) handled correctly
- [ ] Summary report format documented
