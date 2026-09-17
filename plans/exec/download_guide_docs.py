#!/usr/bin/env python3
"""Download script — verified working path via session urllib test.
Fetches .md files from NousResearch/hermes-agent website/docs/user-guide
using GitHub Contents API (discovery) + raw.githubusercontent.com (download).
Batch size: 7 per batch (executing-plans Phase 4 rule).
Outputs: docs/user-guide/ + ./specs/download-log.md
"""
import json
import os
import time
import urllib.parse
import urllib.request

WORK = r"C:\Users\Alexa\Desktop\SandBox"
TARGET_DIR = os.path.join(WORK, "docs", "user-guide")
LOG_FILE = os.path.join(WORK, "$HERMES_HOME", "specs", "download-log.md")
BASE_RAW = "https://raw.githubusercontent.com/NousResearch/hermes-agent/main/website/docs/user-guide"
API_ROOT = "https://api.github.com/repos/NousResearch/hermes-agent/contents/website/docs/user-guide"
BATCH_SIZE = 7

os.makedirs(TARGET_DIR, exist_ok=True)
# Create subfolder placeholders as needed (verified by directory creation after list)

# Helper: list directory contents from GitHub API

def api_list(path="website/docs/user-guide"):
    url = f"https://api.github.com/repos/NousResearch/hermes-agent/contents/{path}"
    req = urllib.request.Request(url, headers={"User-Agent":"HermesAgent","Accept":"application/vnd.github.v3+json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read())

def discover_all():
    # Returns list of (relative_path, download_url) for all .md files
    results = []
    def recurse(path, prefix=""):
        try:
            items = api_list(path)
        except Exception:
            # Log failure; don't fabricate paths
            results.append((f"ERROR/api/{path}", None))
            return
        if not isinstance(items, list):
            # If single file returned (e.g., path to file), handle
            if isinstance(items, dict) and items.get("type") == "file":
                name = items.get("name", "")
                rel = f"{prefix}/{name}" if prefix else name
                if name.endswith(".md"):
                    raw_url = items.get("download_url", f"{BASE_RAW}/{urllib.parse.quote(rel)}")
                    results.append((rel, raw_url))
            else:
                results.append((f"ERROR/not-list/{path}", None))
            return
        for item in items:
            name = item.get("name", "")
            item_type = item.get("type")
            rel = f"{prefix}/{name}" if prefix else name
            if item_type == "dir":
                # Recurse
                recurse(f"{path}/{name}", rel)
            elif item_type == "file" and name.endswith(".md"):
                raw_url = item.get("download_url", f"{BASE_RAW}/{urllib.parse.quote(rel)}")
                results.append((rel, raw_url))
            elif item_type == "file":
                # Non-.md files (like _category_.json) intentionally excluded per spec
                pass
    recurse("website/docs/user-guide", "")
    return results

def download_batch(batch_items, batch_idx):
    # batch_items: list of (rel_path, url)
    log_lines = []
    for rel_path, url in batch_items:
        out_path = os.path.join(TARGET_DIR, rel_path)
        out_dir = os.path.dirname(out_path)
        os.makedirs(out_dir, exist_ok=True)
        try:
            req = urllib.request.Request(url, headers={"User-Agent":"HermesAgent"})
            with urllib.request.urlopen(req, timeout=30) as resp:
                data = resp.read()
            if len(data) == 0:
                log_lines.append(f"| {rel_path} | SKIPPED | zero bytes from server | warning | batch {batch_idx} |")
                continue
            with open(out_path, "wb") as f:
                f.write(data)
            # Verify non-empty after write
            size_after = os.path.getsize(out_path)
            status = "OK" if size_after > 0 else "ERROR"
            log_lines.append(f"| {rel_path} | {status} | {size_after} bytes | info | batch {batch_idx} |")
        except Exception as e:
            log_lines.append(f"| {rel_path} | ERROR | download failed: {e} | error | batch {batch_idx} |")
            # Don't propagate exception (executing-plans Phase 4: continue on failure)
    return log_lines

if __name__ == "__main__":
    # Discovery (single API call — not batched; verified working in session)
    print("Discovering .md files via GitHub Contents API...")
    all_items = discover_all()
    # Separate actual .md entries from error markers
    valid_items = [(r,u) for (r,u) in all_items if not r.startswith("ERROR/")]
    error_items = [(r,u) for (r,u) in all_items if r.startswith("ERROR/")]
    print(f"Discovered .md entries: {len(valid_items)}; errors (non-.md or API failures): {len(error_items)}")
    if error_items:
        for r, _ in error_items[:10]:
            print(f"  Discovery note: {r}")

    # Initialize log
    with open(LOG_FILE, "w", encoding="utf-8") as f:
        f.write("# Download Log — Hermes User-Guide .md Files\n")
        f.write("| file_path | status | detail | severity | batch |\n")
        f.write("|---|---|---|---|---|\n")

    # Process in batches of BATCH_SIZE
    batches = [valid_items[i:i+BATCH_SIZE] for i in range(0, len(valid_items), BATCH_SIZE)]
    total_ok = 0
    total_errors = 0
    for idx, batch in enumerate(batches, start=1):
        print(f"Batch {idx}/{len(batches)} ({len(batch)} items)...")
        lines = download_batch(batch, idx)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            for line in lines:
                f.write(line + "\n")
        # Count
        for line in lines:
            if "ERROR" in line.split("|")[1].strip():
                total_errors += 1
            elif "OK" in line.split("|")[1].strip():
                total_ok += 1
        # Small delay to respect rate limits (verified: no rate limit issues in test; defensive)
        time.sleep(0.3)

    # Final verification counts
    downloaded_files = []
    for root, _dirs, files in os.walk(TARGET_DIR):
        for fn in files:
            if fn.endswith(".md"):
                downloaded_files.append(os.path.join(root, fn))

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write("\n--- SUMMARY ---\n")
        f.write(f"Total discovered .md entries: {len(valid_items)}\n")
        f.write(f"Batch groups processed: {len(batches)} (batch size ≤ {BATCH_SIZE})\n")
        f.write(f"Downloaded files on disk: {len(downloaded_files)}\n")
        f.write(f"OK count (from log): {total_ok}\n")
        f.write(f"ERROR count (from log): {total_errors}\n")
        f.write("Download errors are logged above (individual file paths shown). No fabricated content.\n")

    print(f"Batch download complete. Files on disk under {TARGET_DIR}: {len(downloaded_files)}")
    print(f"Log saved: {LOG_FILE}")
