# Verification Patterns for Plaintext→Markdown Conversion

## Automated Checks (run after conversion)

### 1. Content Preservation
```python
def verify_content_preserved(source: str, output: str) -> bool:
    # Strip markdown formatting, compare word sets
    source_words = set(re.findall(r'\b\w+\b', source.lower()))
    output_words = set(re.findall(r'\b\w+\b', strip_markdown(output).lower()))
    # Allow 5% variance for formatting tokens
    return len(source_words - output_words) / len(source_words) < 0.05
```

### 2. Heading Hierarchy
```python
def verify_headings(output: str) -> list[str]:
    headings = re.findall(r'^(#{1,6})\s+(.+)$', output, re.MULTILINE)
    errors = []
    prev_level = 0
    h1_count = 0
    for level_md, text in headings:
        level = len(level_md)
        if level == 1:
            h1_count += 1
        if level > prev_level + 1:
            errors.append(f"Skipped level: H{prev_level} → H{level} ({text})")
        prev_level = level
    if h1_count != 1:
        errors.append(f"Expected 1 H1, found {h1_count}")
    return errors
```

### 3. Code Block Language Tags
```python
def verify_code_blocks(output: str) -> list[str]:
    errors = []
    for match in re.finditer(r'^```(\w*)\n', output, re.MULTILINE):
        if not match.group(1):
            errors.append("Code block missing language tag")
    return errors
```

### 4. Link Format
```python
def verify_links(output: str) -> list[str]:
    errors = []
    # Bare URLs not in links
    bare_urls = re.findall(r'(?<!\]\()https?://\S+', output)
    for url in bare_urls:
        errors.append(f"Bare URL not linked: {url}")
    # Broken reference links
    refs = re.findall(r'\[([^\]]+)\]\(([^)]*)\)', output)
    for text, url in refs:
        if not url:
            errors.append(f"Empty link URL: [{text}]")
    return errors
```

### 5. Frontmatter (if present)
```python
def verify_frontmatter(output: str) -> list[str]:
    if not output.startswith('---'):
        return ["Missing frontmatter fence"]
    try:
        fm_end = output.index('\n---', 3)
        fm = yaml.safe_load(output[3:fm_end])
        required = ['title', 'description', 'date']
        return [f"Missing frontmatter field: {f}" for f in required if f not in fm]
    except (ValueError, yaml.YAMLError) as e:
        return [f"Frontmatter parse error: {e}"]
```

## Manual Spot-Checks

| Check | Method |
|-------|--------|
| Tables render correctly | View in Markdown preview |
| Lists nest properly | Check indentation in source |
| Special chars escaped | Search for `&`, `<`, `>` not in code |
| Images have alt text | `![]()` → `![alt]()` |

## Integration

Run all checks in Phase 4 (Verify Output). Fail conversion if:
- Any content preservation error
- Heading hierarchy errors
- Missing code block languages
- Frontmatter parse errors