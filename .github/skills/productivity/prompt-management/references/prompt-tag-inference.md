# Prompt Tag Inference

> Supplementary to Phase 4 (Batch Audit & Enhance) of `prompt-management`. Used when fixing `tags: []` prompts to infer meaningful tags from content rather than leaving them empty.

## When to Use

- A prompt has `tags: []` and you need to fill it with content-derived tags
- Batch-processing 50+ prompts where manual tagging is impractical
- Standardizing tag vocabulary across a prompt library

## Approach

Infer tags from three signals in each prompt file, in priority order:

### 1. Title & Name (highest signal)
The frontmatter `title:` and `name:` fields often contain domain keywords directly:
- `title: "Playwright Typescript"` → tags: `[playwright, typescript]`
- `name: "azure-resource-health-diagnose"` → tags: `[azure, debugging]`

### 2. Description & First 500 chars of body
The `description:` field and early body text contain the prompt's domain language:
- `description: "PostgreSQL Code Review Assistant"` → tags: `[postgresql, code-review, database]`
- Body mentions "Docker containerization" → tags: `[docker]`

### 3. Filename patterns
Certain filename patterns reliably indicate the prompt's domain:
- `plan-*`, `execute-*` → `planning`
- `create-*` → `generator`
- `*-mcp-server-generator` → `mcp`
- `*-blueprint-generator` → `architecture`
- `*-review`, `*-audit` → `audit`

## Keyword-to-Tag Mapping Table

Build a mapping of regex patterns to tag arrays. Test patterns against the concatenation of title + name + description + first 500 body chars:

| Pattern | Tags |
|---------|------|
| `python` | `[python]` |
| `typescript\|next\\.?js` | `[typescript, nextjs]` |
| `react` | `[react]` |
| `csharp\|#\|dotnet\|asp\.net\|ef core` | `[csharp, dotnet]` |
| `java\|springboot\|junit\|javadoc` | `[java]` |
| `sql\|postgres\|database\|query\|bigquery` | `[database, sql]` |
| `docker\|container` | `[docker]` |
| `azure\|bicep\|terraform` | `[azure]` |
| `github\|actions\|ci.?cd\|pipeline` | `[github, ci-cd]` |
| `playwright` | `[playwright]` |
| `jest\|testing\|pytest\|xunit` | `[testing]` |
| `mcp.?server` | `[mcp]` |
| `documentation\|doc\|readme\|mkdocs` | `[documentation]` |
| `security\|bias\|injection` | `[security]` |
| `performance\|optimize` | `[performance]` |
| `api\|openapi\|rest\|graphql` | `[api]` |
| `debug\|triage\|diagnos` | `[debugging]` |
| `specification\|feature\|requirement` | `[planning, specification]` |
| `architect\|blueprint\|design` | `[architecture]` |
| `migrate\|upgrade` | `[migration]` |
| `agent\|acp\|acpx` | `[agents]` |
| `linux\|centos\|debian\|fedora\|arch` | `[linux]` |
| `power.?bi\|dax` | `[powerbi]` |
| `vue\|angular\|svelte` | `[frontend]` |
| `django\|flask\|fastapi` | `[python, backend]` |

## Applying the Inference

```python
def infer_tags(filepath: str) -> list[str]:
    content = open(filepath).read()
    fm = yaml.safe_load(re.match(r'^---\n(.*?)\n---', content, re.DOTALL).group(1))
    
    # Build source text
    source = f"{fm.get('title','')} {fm.get('name','')} {fm.get('description','')}"
    body_start = content[content.index('---', content.index('---')+3)+3:][:500].lower()
    source = (source + " " + body_start).lower()
    
    tags = set()
    for pattern, tag_list in KEYWORD_TAGS.items():
        if re.search(pattern, source, re.IGNORECASE):
            tags.update(tag_list)
    
    return sorted(tags)
```

## Pitfalls

- **Over-tagging**: A prompt that mentions "docker" once in a reference section doesn't need `[docker]`. Restrict body scanning to the first 500 chars (goal/description sections).
- **Undertagging**: Prompts that are very generic ("Task1", "Development") may produce few tags. That's fine — generic prompts get generic tags.
- **False positives**: A prompt titled "Refactoring Java Methods" may match both `java` and `refactoring` patterns. Verify that each inferred tag is genuinely about the prompt's domain, not a tangential mention.
- **Existing tags**: Skip any prompt that already has a non-empty `tags:` YAML list — don't overwrite manually curated tags.
- **Tag deduplication**: After inference, run `sort -u` across all tags to catch synonyms (e.g., both `security` and `authentication` from the same prompt). Merge if appropriate.
