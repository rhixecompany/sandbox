# Fetching the awesome-copilot Skills Catalog

## Endpoint
```
GET https://api.github.com/repos/github/awesome-copilot/contents/skills?ref=main
```
Returns a JSON array of directory entries; each has `"name": "<skill-name>"`
and `"type": "dir"`.

## Why not web_extract on the URL?
`web_extract` truncates the response at ~15k chars head + 5k tail, dropping the
middle of the ~310 KB JSON. You get a partial skill list and a wrong count.
Always use the API + regex.

## Extraction regex (Python)
```python
import re, json, urllib.request

url = "https://api.github.com/repos/github/awesome-copilot/contents/skills?ref=main"
req = urllib.request.Request(url, headers={"User-Agent": "hermes"})
with urllib.request.urlopen(req, timeout=30) as r:
    data = json.load(r)

names = sorted({e["name"] for e in data if e.get("type") == "dir"})
print(len(names), "skills")
```
If parsing a `web_extract` cache file instead, use:
```python
names = sorted(set(re.findall(r'"name":\s*"([^"]+)"', txt)))
```
(ignore `\_url` escaped fields — they don't carry `name`).

## Notes
- Catalog size ≈ 371 skills (2026-07). Re-fetch for current count.
- For per-skill front matter compare: raw URL pattern
  `https://raw.githubusercontent.com/github/awesome-copilot/main/skills/<skill>/SKILL.md`
- This repo (SandBox) has NO `.github/skills/` — local-skill side of any
  suggest-* comparison is empty by design.
