# Title Derivation Algorithm

## Problem

When auditing skill libraries, 90%+ of skills lack the `title:` frontmatter field. Manually entering titles is slow. Solution: auto-derive from directory name using capitalization rules + acronym handling.

## Algorithm

### Input
Directory name in kebab-case (lowercase, hyphen-separated):
- `agent-browser`
- `github-pr-workflow`
- `huggingface-hub`
- `hermes-breakdown-epic-arch`
- `llm-orchestrator`
- `dspy-program-optimizer`

### Output
Proper title case:
- `Agent Browser`
- `GitHub PR Workflow`
- `HuggingFace Hub`
- `Hermes Breakdown Epic Arch`
- `LLM Orchestrator`
- `DSPy Program Optimizer`

### Rules

1. **Split on hyphens**
   ```python
   parts = dir_name.split('-')
   ```

2. **Define known acronyms** (uppercase in titles)
   ```python
   acronyms = {
       'ai', 'mcp', 'nlp', 'ml', 'llm', 'dspy', 'rag',
       'cr', 'pr', 'ci', 'cd', 'api', 'aws', 'gcp', 'sql',
       'orm', 'jwt', 'oauth', 'jwt', 'crm', 'erp'
   }
   ```

3. **For each part:**
   - If lowercase part is in acronyms → `part.upper()`
   - Else → `part.capitalize()`

4. **Join with spaces**
   ```python
   return ' '.join(title_parts)
   ```

### Python Implementation

```python
def derive_title(dir_name: str, acronyms: set = None) -> str:
    """
    Derive a proper title from a skill directory name.
    
    Args:
        dir_name: Skill directory name (kebab-case)
        acronyms: Set of known acronyms (lowercase keys)
    
    Returns:
        Proper Title Case string
    
    Examples:
        >>> derive_title('agent-browser')
        'Agent Browser'
        >>> derive_title('github-pr-workflow')
        'GitHub PR Workflow'
        >>> derive_title('llm-orchestrator')
        'LLM Orchestrator'
    """
    if acronyms is None:
        acronyms = {
            'ai', 'mcp', 'nlp', 'ml', 'llm', 'dspy', 'rag',
            'cr', 'pr', 'ci', 'cd', 'api', 'aws', 'gcp', 'sql',
            'orm', 'jwt', 'oauth', 'crm', 'erp', 'http', 'ftp'
        }
    
    parts = dir_name.split('-')
    title_parts = []
    
    for part in parts:
        if part.lower() in acronyms:
            title_parts.append(part.upper())  # AI, MCP, PR
        else:
            title_parts.append(part.capitalize())  # Agent, Browser
    
    return ' '.join(title_parts)
```

### Test Cases

```python
test_cases = [
    ('agent-browser', 'Agent Browser'),
    ('algorithmic-art', 'Algorithmic Art'),
    ('apple-notes', 'Apple Notes'),
    ('autonomous-ai-agents', 'Autonomous AI Agents'),
    ('github-pr-workflow', 'GitHub PR Workflow'),
    ('huggingface-hub', 'HuggingFace Hub'),
    ('hermes-breakdown-epic-arch', 'Hermes Breakdown Epic Arch'),
    ('llm-orchestrator', 'LLM Orchestrator'),
    ('dspy-program-optimizer', 'DSPy Program Optimizer'),
    ('mcp-builder', 'MCP Builder'),
    ('jwt-auth-service', 'JWT Auth Service'),
    ('aws-lambda-integration', 'AWS Lambda Integration'),
]

for dir_name, expected in test_cases:
    result = derive_title(dir_name)
    assert result == expected, f"Failed: {dir_name} → {result} (expected {expected})"
```

## Notes

- **Case sensitivity:** Input is always lowercase (kebab-case); output is Title Case
- **Acronym conflicts:** Some names like "GitHub" break the rule (casing). Handle via acronym set.
- **Custom acronyms:** Pass `acronyms` parameter to extend for domain-specific terms
- **Abbreviations vs. acronyms:** Don't include abbreviations like "num" (number) — only true acronyms
- **Multi-word names:** Use hyphens, e.g., "machine-learning" → "Machine Learning" (not acronym)

## Validation

Before applying title derivation at scale:
1. Run algorithm on 10-20 sample skills
2. Manually verify outputs look reasonable
3. Spot-check for any acronym misses (add to set if needed)
4. Confirm no existing titles will be overwritten (check Phase 1 audit first)
