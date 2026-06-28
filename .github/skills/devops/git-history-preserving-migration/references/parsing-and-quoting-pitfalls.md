# Parsing and quoting pitfalls

Lessons from migrating the Rhixe-company sandbox:

1. read_file returns an object; always check for 'content'. If missing, re-run with a larger limit or fail gracefully.

2. When extracting a JSON fenced block from markdown, prefer this flow:
   - Search for a regex matching ```json\n(.*?)\n``` with re.S (dot matches newline).
   - Trim whitespace. If json.loads fails with "Extra data", try to detect multiple objects and load the first array or use a tolerant parser.
   - Fallback to parsing a comma-separated summary line if the fenced block is not present.

3. Avoid embedding unescaped triple backticks in Python f-strings. Use triple-quoted raw strings for write_file content or build content as a list of lines then join.

4. Windows paths contain backslashes; when matching with regex, prefer matching inside quotes and use non-greedy patterns: '([^']+)'.

5. When generating PowerShell commands, prefer Copy-Item for non-destructive defaults; include Move-Item as an explicit alternative.
