# Async CLI Script Patterns for Hermes

## Canonical Entrypoint

Every Python CLI script in `~/AppData/Local/hermes/scripts/` should use this pattern:

```python
#!/usr/bin/env python3
import asyncio
import argparse
import sys
from pathlib import Path
from typing import List


async def main() -> None:
    parser = argparse.ArgumentParser(description="...")
    parser.add_argument("--workspace", type=str, default=".")
    # ... more args ...
    args = parser.parse_args()
    # ... async work ...
    sys.exit(0)


if __name__ == "__main__":
    asyncio.run(main())
```

## I/O Offloading Pattern

File operations **must** be offloaded to a thread to avoid blocking the event loop:

```python
# ✅ Correct — async file read/write
content = await asyncio.to_thread(Path(path).read_text, encoding="utf-8")
await asyncio.to_thread(Path(path).write_text, content, encoding="utf-8")

# ❌ Wrong — blocks the event loop
content = Path(path).read_text()
```

## Concurrent Processing Pattern

When processing multiple files, use `asyncio.gather()`:

```python
async def process_one(file_path: Path) -> dict:
    content = await asyncio.to_thread(file_path.read_text, encoding="utf-8")
    # ... CPU-bound processing stays synchronous ...
    return {"file": str(file_path), "result": ...}

files = list(workspace.glob("**/*.md"))
results = await asyncio.gather(*(process_one(f) for f in files))
```

## Network Calls

```python
# ✅ Correct — offload blocking HTTP call
response = await asyncio.to_thread(urllib.request.urlopen, req, timeout=timeout)

# ❌ Wrong — blocks the event loop
response = urllib.request.urlopen(req, timeout=timeout)
```

## CPU-Bound Processing

Keep text processing, regex, JSON parsing, and scoring logic synchronous — these run on the calling thread and don't block the event loop for any meaningful duration:

```python
# ✅ Fine — CPU-bound, fast (<1ms)
def score_frontmatter(text: str) -> int:
    if not text.startswith("---"):
        return 0
    ...

# ✅ Fine — calling it inside async function
result = score_frontmatter(content)
```

## Output Patterns

Each script should support **both** human-readable and JSON output:

```python
if args.json:
    output = json.dumps({"results": results, ...}, indent=2)
    if args.output:
        await asyncio.to_thread(Path(args.output).write_text, output, encoding="utf-8")
    else:
        print(output)
else:
    # Human-readable report
    print(f"Scanned {len(files)} file(s) ...")
    for r in results:
        status = "PASS" if r.get("passed") else "FAIL"
        print(f"  [{status}] {r['file']}")
```

## Syntax Verification

After creating or modifying a Python script, verify syntax:

```bash
python3 -c "import ast; ast.parse(open('FILE').read())"
```

Prefer Hermes' built-in auto-lint (runs on `write_file`), but the ast.parse command works in any environment.

## Key Principles

| Principle | Reason |
|-----------|--------|
| `asyncio.run(main())`, not `main()` | Required for async entrypoint |
| Offload all I/O to `asyncio.to_thread` | Prevents event loop blocking |
| Keep CPU-bound processing synchronous | Text processing is fast enough |
| `asyncio.gather()` for file batches | Process files concurrently |
| argparse CLI, not hardcoded paths | Scripts need to be reusable |
| Support both text and JSON output | Human runs + automated pipeline |
