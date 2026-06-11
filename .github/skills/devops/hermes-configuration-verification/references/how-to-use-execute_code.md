How to use execute_code instead of delegate_task

Purpose: reduce toolset loading and avoid hitting the soft tool-count limit when analyzing multiple files or performing multi-step operations.

Pattern:

1. Use execute_code when you need to run 3+ tool calls with logic between them (filter, aggregate, loop, retries).
2. Execute code runs in Python with hermes_tools pre-imported. Use web_search, web_extract, read_file, write_file, terminal, patch, and other helpers directly.

Example replaceable script:

```python
from hermes_tools import read_file, search_files, write_file, terminal

# Find all README.md files under project
matches = search_files(pattern='**/README.md', path='.', target='files')

for p in matches['matches']:
    content = read_file(p)['content']
    # simple check
    if 'TODO' in content:
        print(f"Found TODO in {p}")

# Run a shell command and capture output
res = terminal('git status --porcelain', timeout=30)
print(res['output'])

# Write a brief report
write_file('tmp/execute_code_report.md', '# Execute Code Report\n\nFound X files with TODOs')
```

Best practices:
- Limit execute_code scripts to 50 tool calls.
- Keep scripts idempotent and safe for dry-run.
- Prefer terminal() for commands and read_file()/write_file() for file ops — they are reliable and tracked.
- When needing parallel subagents for independent heavy tasks, use delegate_task, but be aware of the tool-count implications.

Save this file under the skill as a reference for future sessions.