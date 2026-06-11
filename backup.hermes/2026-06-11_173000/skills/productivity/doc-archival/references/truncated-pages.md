# Doc Archival: Handling Truncated Pages

## Problem

`web_extract()` truncates large pages with LLM summarization. The returned content includes markers like:
```
[... summary truncated for context management ...]
[Content truncated — showing first 5,000 of 7,330 chars. LLM summarization timed out.]
```

## Solution: Browser Fallback

For any page that comes back truncated, use the browser to get the full content:

```python
# Step 1: Navigate to the page
browser_navigate(url="https://example.com/docs/page")

# Step 2: Extract full article text
browser_console(expression="document.querySelector('article').innerText")
```

This returns the complete page content as plain text, which you can then format into markdown.

## When to Use Browser vs web_extract

| Page Size | Method |
|-----------|--------|
| < 5,000 chars | `web_extract` — fast, no browser needed |
| 5,000-15,000 chars | `web_extract` first, check for truncation, fall back to browser if needed |
| > 15,000 chars | Use browser directly — will definitely be truncated by web_extract |

## Docusaurus / VuePress / MkDocs Pattern

Most modern documentation sites (including hermes-agent.nousresearch.com) use a framework where the main content is in an `<article>` tag:

```javascript
document.querySelector('article').innerText
```

If that doesn't work, try:
```javascript
document.querySelector('[class*="article"]').innerText
document.querySelector('main').innerText
document.querySelector('.markdown').innerText
```

## Batch Fetch Strategy

When fetching multiple pages:

1. **First pass:** Use `web_extract(urls=[...])` with up to 5 URLs per call
2. **Check results:** Look for truncation markers in each result
3. **Second pass:** For truncated pages, use `browser_navigate` + `browser_console` one at a time
4. **Write files:** Once all content is captured, write all markdown files
5. **Verify:** Run the verification script to ensure completeness
