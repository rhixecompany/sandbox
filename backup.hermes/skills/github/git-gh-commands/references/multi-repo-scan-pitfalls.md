# Multi-Repo Scan Pitfalls

## Reusable lesson

When enumerating files across many repos, do not assume recursive globbing is safe on Windows workspaces with vendored dependencies.

### Observed failure mode

- `pathlib.Path.rglob('*RESEARCH*.md')` can throw `FileNotFoundError` while walking into broken symlinks or transient vendor paths inside `node_modules/.pnpm/...`.
- The failure is not limited to the target pattern; the traversal itself can die before yielding results.

### Safer pattern

Use `os.walk()` with an explicit prune list:

```python
skip = {
    '.git',
    'node_modules',
    '.next',
    '.venv',
    '.mypy_cache',
    '.pytest_cache',
    '__pycache__',
    '.pnpm',
}

for dirpath, dirnames, filenames in os.walk(repo_root):
    dirnames[:] = [d for d in dirnames if d not in skip]
    for name in filenames:
        if 'RESEARCH' in name and name.endswith('.md'):
            yield Path(dirpath) / name
```

### When to use

- Repo inventories
- RESEARCH_* cross-reference scans
- Ignore-file audits
- Any batch filesystem inspection across cloned projects

### Verification

- Confirm the traversal returns results without touching vendored dependency trees.
- Prefer this over `Path.rglob()` when scanning a workspace that contains deep package stores or generated artifacts.
