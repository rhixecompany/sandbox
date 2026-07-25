# Bash Heredoc Quoting Pitfalls

## Problem: Variable Expansion Inside Heredocs

When creating bash scripts inline via `cat > file << 'EOF'`, unquoted heredocs expand `$variables` and `$(commands)` immediately in the *parent* shell, not in the created file.

Failure modes:
1. `$(...)` executes in parent shell, output gets baked in as literal text
2. `$variables` expand to empty if unset in parent scope

## The Fix

```bash
# WRONG
cat > script.sh << EOF
name=$(basename "$dir")
EOF

# CORRECT — single-quoted delimiter prevents ALL expansion
cat > script.sh << 'EOF'
name=$(basename "$dir")
EOF
```

Note: `<< "EOF"` does NOT prevent expansion. Only `<< 'EOF'` works.

## Prefer write_file for Complex Scripts

When a script has dynamic content, avoid heredocs entirely:

```python
write_file(path="script.sh", content="""#!/bin/bash
for dir in projects/*/; do
  name=$(basename "$dir")
  echo "$name"
done
""")
```

Benefits: no quoting issues, exact content control, cross-platform, Python f-strings for dynamic values.

## MSYS/Git-Bash Specific Issues

1. `$(...)` in loop bodies execute in parent shell before the loop starts (if heredoc unquoted)
2. Nested heredocs: avoid entirely, use write_file
3. Always use `/` paths in bash heredocs, even on Windows

## Debugging

Symptoms of premature expansion: empty loop variables, wrong find results, unexpected wc counts.
Fix: ensure heredoc delimiter is single-quoted: `<< 'EOF'`
