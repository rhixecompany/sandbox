# Tag Inference for Prompts

> Technique for adding meaningful tags to prompts with empty `tags: []` based on content signals.

## When to Use

When batch-processing 100+ prompts that have `tags: []` (empty) and need meaningful categorisation from their existing content rather than hand-curating each one.

## Approach

1. **Extract frontmatter** — Read each `.prompt.md` file, parse YAML frontmatter for `name`, `title`, `description`
2. **Build keyword→tag map** — Map regex patterns to tag names. Group by domain (languages, frameworks, tools, concerns)
3. **Match against source text** — Concatenate `title + name + description + first 500 chars of body` and test each regex
4. **Apply name-pattern heuristics** — File naming conventions add extra signal:
   - `plan-*` / `execute-*` → `planning`
   - `create-*` → `generator`
   - `*-mcp-server-*` → `mcp`
   - `*-blueprint-*` → `architecture`
   - `*-review` / `*-audit` → `audit`
5. **Write back** — Replace `tags: []` with `tags: [tag1, tag2, ...]`

## Keyword→Tag Map (reference)

| Domain | Patterns | Tags |
|--------|----------|------|
| Languages | `python` `javascript\|node` `csharp\|dotnet` `java\|spring` `ruby` `rust` | respective language tag |
| Frameworks | `react` `next\.?js` `django` `express` `springboot` | respective framework tag |
| Databases | `sql\|postgres\|database\|query` `drizzle\|orm` `cosmos\|bigquery` | `database`, `sql`, etc. |
| DevOps | `docker\|container` `kubernetes\|k8s` `azure\|bicep` `ci.?cd` `terraform` | respective devops tag |
| Cloud | `aws` `gcp\|google-cloud` `azure` | respective cloud tag |
| Tools | `mcp` `playwright` `jest\|pytest` `eslint` | respective tool tag |
| Concerns | `security\|safety\|injection\|bias` `performance\|optimize` `debug\|triage` `refactor` `migrate\|upgrade` | respective concern tag |
| Documentation | `documentation\|doc\|readme\|mkdocs` `markdown\|md\|tldr` | `documentation` |
| Architecture | `architect\|blueprint\|design\|adr` `specification\|spec\|feature` | `architecture`, `planning` |
| Agents | `agent\|acp\|acpx` `copilot\|hermes\|opencode` | `agents`, `ai-assistant` |

## Pitfalls

- **Don't overwrite existing tags** — only fill `tags: []` (empty). Check `isinstance(tags, list) and len(tags) > 0` first.
- **Don't add bare-string tags** — YAML array format only (`tags: [a, b]` or `tags:\n  - a\n  - b`)
- **Don't infer from file path alone** — the content (frontmatter + body) is the source of truth; file naming is supplemental.
- **De-duplicate** — the same tag shouldn't appear twice in one prompt.
- **Order doesn't matter** — tags are a set, not a ranked list.

## Script Template

```python
import os, re, yaml
from pathlib import Path

# 1. Define keyword→tag mapping
KEYWORD_TAGS = {
    r'python': ['python'],
    r'typescript|next\.?js': ['typescript', 'nextjs'],
    r'sql|postgres|database': ['database', 'sql'],
    # ... extend per project domain
}

# 2. Infer function
def infer_tags(filepath: Path) -> list:
    content = filepath.read_text(encoding='utf-8')
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        return []
    fm = yaml.safe_load(fm_match.group(1))
    if not fm:
        return []
    source = f"{fm.get('title','')} {fm.get('name','')} {fm.get('description','')}\n"
    source += content[fm_match.end():fm_match.end()+500].lower()
    tags = set()
    for pattern, tag_list in KEYWORD_TAGS.items():
        if re.search(pattern, source, re.IGNORECASE):
            tags.update(tag_list)
    return sorted(tags)

# 3. Apply
prompts_dir = Path("prompts")
for pf in prompts_dir.glob("*.prompt.md"):
    content = pf.read_text(encoding='utf-8')
    if 'tags: []' not in content:
        continue
    inferred = infer_tags(pf)
    if inferred:
        pf.write_text(content.replace('tags: []', f'tags: [{", ".join(inferred)}]'), encoding='utf-8')
```
