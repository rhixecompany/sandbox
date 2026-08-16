# Parallel CLI for Web Research

## Installation
```bash
npm install -g @anthropic-ai/claude-code
# or use npx
npx @anthropic-ai/claude-code
```

## Basic Web Research Commands
```bash
# Search and summarize
claude "Search for latest AI research papers and summarize top 3"

# Multi-source analysis
claude "Compare Python, JS, and Rust for web scraping. Give pros/cons"

# Extract and format
claude "Go to example.com/docs, extract all API endpoints, format as table"
```

## Parallel Execution Patterns
| Pattern | Command | Best For |
|---------|---------|----------|
| Sequential | One task at a time | Simple Q&A |
| Chain | Pipe output to next task | Extract → Summarize |
| Fan-out | Multiple independent queries | Comparative research |
| Gather | Single query across sources | Consensus finding |

## Result Processing
```python
def parse_claude_output(text):
    """Extract structured data from Claude responses."""
    sections = re.split(r'\n#{2,3}\s+', text)
    return {s.split('\n')[0].strip(): s for s in sections if s.strip()}
```

## Research Workflow Template
1. Define research question with clear scope
2. Choose execution pattern (fan-out for comparisons)
3. Run Claude queries with context
4. Parse and deduplicate results
5. Synthesize into final report
