# Web Extract Fallback Pattern

## Problem

`web_extract` truncates large pages with "LLM summarization timed out" — content beyond ~5,000 chars gets cut.

## Solution

Use `browser_navigate` + `browser_console` to get full page content:

1. Navigate to the page:
   ```
   browser_navigate(url="https://example.com/docs/page")
   ```

2. Extract full article text:
   ```
   browser_console(expression="document.querySelector('article').innerText")
   ```

3. For pages without `<article>` tags, try:
   ```
   browser_console(expression="document.querySelector('main').innerText")
   browser_console(expression="document.body.innerText")
   ```

## When to Use

- `web_extract` returns truncated content (look for `[... summary truncated ...]` in output)
- Pages with code blocks, tables, or long lists that exceed the summarization limit
- When you need the *complete* page content, not a summary

## Tips

- Always try `web_extract` first — it's faster and cheaper for small pages
- Use the browser fallback only when truncation is detected
- The browser approach works for any docs site, not just Hermes
- On Docusaurus/MkDocs sites, `article` or `main` selectors usually capture the content
