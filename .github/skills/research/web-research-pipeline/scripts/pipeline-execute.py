#!/usr/bin/env python3
"""Web Research Pipeline — automated execution script."""
from hermes_tools import web_search, web_extract, terminal, tool_call
from datetime import datetime
import os, re
from urllib.parse import urlparse

def slugify(text, max_len=60):
    text = text.lower().strip()
    text = re.sub(r'[|:*?"<>]', '', text)
    text = re.sub(r'\s+', '-', text)
    text = re.sub(r'[^a-z0-9\-]', '', text)
    text = re.sub(r'-+', '-', text)
    return text[:max_len].strip('-')

def url_slug(url):
    p = urlparse(url)
    host = p.netloc.replace('www.', '')
    path = p.path.strip('/').replace('/', '-')
    slug = f"{host}-{path}" if path else host
    return slugify(slug, 80)

# Phase 1: Preflight
try:
    terminal("hermes mcp status --json 2>&1", timeout=15)
except:
    pass

# Phase 2: Search
query = "your search query"
try:
    results = tool_call(name="firecrawl_search", arguments={"query": query, "limit": 10})
    urls = [r['url'] for r in results.get('data', {}).get('results', results.get('results', []))]
except Exception:
    results = web_search(query=query, limit=10)
    urls = [r['url'] for r in results['data']['web']]

if not urls:
    print(f"No results for: {query}")
    exit(0)

# Phase 3: Extract
all_pages = []
failed = {}
for url in urls:
    content = None; backend = None
    for attempt_name, attempt_fn in [("mcp-fetch", lambda u=url: tool_call(name="mcp_fetch_get_markdown", arguments={"url": u})),
                                      ("web_extract", lambda u=url: web_extract(urls=[u], char_limit=15000))]:
        try:
            r = attempt_fn()
            if isinstance(r, dict):
                c = r.get('content', r.get('markdown', ''))
                if not c and 'results' in r:
                    c = r['results'][0].get('content', '')
            else:
                c = ''
            if len(c) > 100:
                content = c; backend = attempt_name; break
        except:
            continue
    if not content:
        failed[url] = "All backends exhausted"
        continue
    title = ""
    for line in content.split('\n'):
        if line.startswith('# '):
            title = line.replace('# ', '').strip(); break
    title = title or urlparse(url).netloc
    all_pages.append({'url': url, 'content': content, 'title': title, 'backend': backend})

# Phase 4: Save
out_dir = os.path.join(os.path.expanduser("~/Desktop/SandBox/research"), slugify(query))
os.makedirs(out_dir, exist_ok=True)
saved = []
existing = {}
for page in all_pages:
    base = slugify(page['title']) if page['title'] and page['title'] not in ('untitled','home','404') else url_slug(page['url'])
    existing[base] = existing.get(base, 0) + 1
    fs = f"{base}-{existing[base]}.md" if existing[base] > 1 else f"{base}.md"
    md = f"# {page['title']}\n\n> **Source:** {page['url']}\n> **Retrieved:** {datetime.now():%Y-%m-%dT%H:%M:%S}\n> **Backend:** {page['backend']}\n\n---\n\n{page['content']}\n\n---\n"
    with open(os.path.join(out_dir, fs), 'w', encoding='utf-8') as f:
        f.write(md)
    saved.append(fs)

# Summary
backends = sorted(set(p['backend'] for p in all_pages))
print(f"Topic: {query}\nSources: {len(urls)}\nSaved: {len(saved)}\nFailed: {len(failed)}\nBackends: {', '.join(backends)}\nDir: {out_dir}")
