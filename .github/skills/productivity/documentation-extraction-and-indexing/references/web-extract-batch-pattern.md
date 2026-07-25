# web_extract Batch Extraction Pattern

## Template for Extracting Multiple URLs in Batches

```python
from hermes_tools import web_extract, write_file
import os, re

def extract_urls_to_markdown(urls, output_dir, batch_size=5):
    """Extract URLs via web_extract in batches, save as Markdown with source headers."""
    os.makedirs(output_dir, exist_ok=True)
    
    batches = [urls[i:i+batch_size] for i in range(0, len(urls), batch_size)]
    all_results = []
    
    for i, batch in enumerate(batches):
        print(f"Processing batch {i+1}/{len(batches)}: {len(batch)} URLs")
        res = web_extract(batch)
        all_results.extend(res['results'])
    
    written = []
    for r in all_results:
        url = r.get('url', '')
        content = r.get('content', '')
        error = r.get('error')
        
        # Sanitize filename
        fname = re.sub(r'[^A-Za-z0-9._-]+', '_', url)
        path = os.path.join(output_dir, f"{fname}.md")
        
        header = f"# Source: {url}\n\n"
        if error:
            body = f"**ERROR:** {error}\n\n---\n*Extraction failed*"
        else:
            body = content
        
        write_file(path=path, content=header + body)
        written.append({'path': path, 'url': url, 'len': len(content), 'error': error})
    
    return written

# Usage
urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    # ...
]
results = extract_urls_to_markdown(urls, "docs/example-source/")

# Verification
for r in results:
    status = f"ERROR: {r['error']}" if r['error'] else f"OK ({r['len']} chars)"
    print(f"{r['path']} | {status}")
```