# Browser Fallback for Truncated Pages

## When web_extract Returns Summaries

`web_extract` caps large pages at ~5000 chars and returns LLM summaries. For full content, use browser automation:

```python
from hermes_tools import browser_navigate, browser_console, write_file
import os, re

def extract_full_page(url, output_dir):
    """Navigate to URL and extract full article text via browser console."""
    os.makedirs(output_dir, exist_ok=True)
    
    # Navigate (returns snapshot)
    browser_navigate(url)
    
    # Extract full article text
    result = browser_console(
        expression="document.querySelector('article')?.innerText || document.body.innerText"
    )
    content = result.get('result', '')
    
    if not content or len(content) < 500:
        # Try alternative selectors
        selectors = [
            'main',
            '[role="main"]',
            '.content',
            '.documentation',
            '#content'
        ]
        for sel in selectors:
            result = browser_console(
                expression=f"document.querySelector('{sel}')?.innerText"
            )
            if result.get('result') and len(result['result']) > 500:
                content = result['result']
                break
    
    # Save
    fname = re.sub(r'[^A-Za-z0-9._-]+', '_', url)
    path = os.path.join(output_dir, f"{fname}.md")
    header = f"# Source: {url}\n\n"
    write_file(path=path, content=header + content)
    
    return path, len(content)

# Usage for known-truncated URLs
truncated_urls = [
    "https://hermes-agent.nousresearch.com/docs/user-guide/features/hooks",
    "https://hermes-agent.nousresearch.com/docs/user-guide/features/plugins",
]
for url in truncated_urls:
    path, length = extract_full_page(url, "docs/hermes/")
    print(f"Saved {path}: {length} chars")
```

## Selector Priority for Documentation Sites

| Selector | Use Case |
|----------|----------|
| `article` | Most doc sites (Docusaurus, VitePress, GitBook) |
| `main` | Fallback for semantic HTML |
| `[role="main"]` | Accessibility-compliant sites |
| `.content` / `.documentation` | Custom class-based layouts |
| `#content` | ID-based content areas |
| `document.body.innerText` | Last resort (includes nav/footer) |

## Verification

After extraction, check:
```bash
# Should be > 10KB for full doc pages
wc -c docs/hermes/*.md
# No "truncated" or "summary" markers
grep -i "truncat\|summary" docs/hermes/*.md
```