#!/usr/bin/env python3
"""search_superrag.py - Semantic search over an ingested Supermemory container
(documents mode = raw chunk retrieval for RAG grounding).

Usage:
    SUPERMEMORY_API_KEY=sm_... python search_superrag.py --tag sandbox_docs --query "mcp security audit"
    python search_superrag.py --tag sandbox_docs --query "..." --limit 10

Container tag rules: singular containerTag, format ^[a-zA-Z0-9_:-]+$, one tag
per project, no cross-tag queries.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.request

API_BASE = os.environ.get("SUPERMEMORY_API_BASE", "https://api.supermemory.ai")
TAG_RE = re.compile(r"^[a-zA-Z0-9_:-]+$")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tag", required=True, help="Singular containerTag to search")
    ap.add_argument("--query", required=True, help="Search query")
    ap.add_argument("--limit", type=int, default=5)
    ap.add_argument("--mode", choices=["documents", "memories", "hybrid"], default="documents")
    args = ap.parse_args()

    key = os.environ.get("SUPERMEMORY_API_KEY")
    if not key:
        print("ERROR: SUPERMEMORY_API_KEY not set", file=sys.stderr)
        return 2
    if not TAG_RE.match(args.tag) or len(args.tag) > 100:
        print(f"ERROR: invalid containerTag {args.tag!r}", file=sys.stderr)
        return 2

    body = json.dumps(
        {"q": args.query, "containerTag": args.tag, "searchMode": args.mode, "limit": args.limit}
    ).encode("utf-8")
    req = urllib.request.Request(
        f"{API_BASE}/v4/search",
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=40) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        print(f"ERROR: HTTP {exc.code}", file=sys.stderr)
        return 1

    results = data.get("results", []) or []
    print(f"{len(results)} result(s) for tag={args.tag} mode={args.mode}")
    for r in results:
        text = r.get("chunk") or r.get("memory") or r.get("content") or ""
        score = r.get("similarity") or r.get("score") or 0.0
        title = ""
        for doc in r.get("documents", []) or []:
            if doc.get("metadata", {}).get("source_file"):
                title = f" [{doc['metadata']['source_file']}]"
                break
        print(f"  [{score:.3f}]{title} {str(text)[:160].replace(chr(10), ' ')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
