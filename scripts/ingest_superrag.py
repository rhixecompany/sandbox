#!/usr/bin/env python3
"""ingest_superrag.py - Ingest a directory of reference files into Supermemory
as superrag (chunk/embed only) documents.

Idempotent: files already ingested (stable sha1-based customId) are skipped,
so re-running is safe and free. Polls each document until status == "done".

Usage:
    SUPERMEMORY_API_KEY=sm_... python ingest_superrag.py --dir ../docs --tag sandbox_docs
    python ingest_superrag.py --dir ../docs --tag sandbox_docs --dry-run
    python ingest_superrag.py --dir ../docs --tag sandbox_docs --limit 3

Container tag rules: singular containerTag, format ^[a-zA-Z0-9_:-]+$, one tag
per project, no cross-tag queries.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

API_BASE = os.environ.get("SUPERMEMORY_API_BASE", "https://api.supermemory.ai")
TAG_RE = re.compile(r"^[a-zA-Z0-9_:-]+$")
MAX_BYTES = 100_000
EXTS = {".md", ".txt", ".json"}


def _headers(key: str) -> dict:
    return {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}",
    }


def _post(key: str, path: str, body: dict) -> dict:
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        data=json.dumps(body).encode("utf-8"),
        headers=_headers(key),
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def _get(key: str, path: str) -> dict:
    req = urllib.request.Request(f"{API_BASE}{path}", headers=_headers(key), method="GET")
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def tag_ok(tag: str) -> bool:
    return bool(TAG_RE.match(tag)) and len(tag) <= 100


def list_existing_ids(key: str, tag: str) -> set:
    """Existing customIds for a tag (POST /v3/documents/list)."""
    try:
        data = _post(key, "/v3/documents/list", {"containerTag": tag})
    except urllib.error.HTTPError:
        return set()
    ids = set()
    for doc in data.get("memories", []) or []:
        cid = doc.get("customId")
        if cid:
            ids.add(cid)
    return ids


def ingest_one(key: str, tag: str, relpath: str, text: str, custom_id: str) -> str:
    """POST one document, poll until done. Returns status string."""
    doc = _post(
        key,
        "/v3/documents",
        {
            "content": text[:MAX_BYTES],
            "containerTag": tag,
            "taskType": "superrag",
            "customId": custom_id,
            "metadata": {"source_file": relpath, "ingestor": "ingest_superrag.py"},
        },
    )
    doc_id = doc.get("id", "")
    deadline = time.time() + 60
    status = doc.get("status", "queued")
    while status == "queued" and time.time() < deadline:
        time.sleep(3)
        status = _get(key, f"/v3/documents/{doc_id}").get("status", status)
    return status


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--dir", required=True, help="Directory of reference files to ingest")
    ap.add_argument("--tag", required=True, help="Singular containerTag (^[a-zA-Z0-9_:-]+$)")
    ap.add_argument("--dry-run", action="store_true", help="Only list what would be ingested")
    ap.add_argument("--limit", type=int, default=0, help="Max NEW documents to ingest (0 = unlimited)")
    ap.add_argument("--max-bytes", type=int, default=MAX_BYTES)
    args = ap.parse_args()

    key = os.environ.get("SUPERMEMORY_API_KEY")
    if not key:
        print("ERROR: SUPERMEMORY_API_KEY not set", file=sys.stderr)
        return 2
    if not tag_ok(args.tag):
        print(f"ERROR: invalid containerTag {args.tag!r} (must match ^[a-zA-Z0-9_:-]+$, <=100 chars)", file=sys.stderr)
        return 2
    if not os.path.isdir(args.dir):
        print(f"ERROR: not a directory: {args.dir}", file=sys.stderr)
        return 2

    existing = set() if args.dry_run else list_existing_ids(key, args.tag)
    candidates: list[tuple[str, str, int]] = []  # (relpath, custom_id, size)
    for root, _dirs, files in os.walk(args.dir):
        _dirs[:] = [d for d in _dirs if not d.startswith((".", "node_modules", "archive"))]
        for name in sorted(files):
            if os.path.splitext(name)[1].lower() not in EXTS:
                continue
            full = os.path.join(root, name)
            rel = os.path.relpath(full, args.dir).replace("\\", "/")
            size = os.path.getsize(full)
            cid = hashlib.sha1(rel.encode("utf-8")).hexdigest()[:24]
            candidates.append((rel, cid, size))

    new, skipped, errors, too_big = [], 0, 0, 0
    for rel, cid, size in candidates:
        if cid in existing:
            skipped += 1
            continue
        if size > args.max_bytes:
            too_big += 1
            print(f"  SKIP (too big {size}B) {rel}")
            continue
        new.append((rel, cid))
        if args.dry_run:
            print(f"  WOULD INGEST {rel}")

    print(
        f"{'[dry-run] ' if args.dry_run else ''}tag={args.tag} dir={args.dir}: "
        f"candidates={len(candidates)} new={len(new)} skipped={skipped} too_big={too_big} errors={errors}"
    )
    if args.dry_run or len(new) == 0:
        return 0

    ingested = 0
    for rel, cid in new:
        if args.limit and ingested >= args.limit:
            break
        full = os.path.join(args.dir, rel)
        with open(full, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        try:
            status = ingest_one(key, args.tag, rel, text, cid)
        except urllib.error.HTTPError as exc:
            errors += 1
            print(f"  FAIL {rel}: HTTP {exc.code}")
            continue
        ingested += 1
        print(f"  {'OK' if status == 'done' else 'STILL ' + status} {rel} -> hyperlink-free")
    print(f"ingested={ingested} errors={errors} (limit={args.limit or 'unlimited'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
