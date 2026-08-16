#!/usr/bin/env python3
"""
Kit Verification Script
Validates completeness of an actionable research kit.

Usage: python verify_kit.py <kit_directory>
"""

import os
import sys
import csv
import re
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import time

REQUIRED_ROOT = ["README.md", "_MASTER.md"]
REQUIRED_DIRS = ["templates", "trackers", "references"]
TEMPLATE_MIN_FILES = 3
TRACKER_MIN_FILES = 2
REFERENCE_MIN_FILES = 3

def check_file_exists(path: Path, name: str) -> tuple[bool, str]:
    matches = list(path.glob(name))
    if matches:
        return True, f"✅ {name}"
    return False, f"❌ Missing: {name}"

def check_dir_min_files(path: Path, dirname: str, min_files: int) -> tuple[bool, str]:
    dir_path = path / dirname
    if not dir_path.exists():
        return False, f"❌ Missing directory: {dirname}/"
    files = [f for f in dir_path.iterdir() if f.is_file()]
    if len(files) >= min_files:
        return True, f"✅ {dirname}/ has {len(files)} files (≥{min_files})"
    return False, f"⚠️ {dirname}/ has only {len(files)} files (need ≥{min_files})"

def validate_csv(path: Path) -> tuple[bool, str]:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            headers = next(reader, None)
            if not headers:
                return False, f"❌ {path.name}: empty CSV"
            # Check for trailing commas (common issue)
            for i, row in enumerate(reader, 2):
                if len(row) != len(headers):
                    return False, f"❌ {path.name}: line {i} has {len(row)} cols, expected {len(headers)}"
        return True, f"✅ {path.name}: valid CSV ({len(headers)} columns)"
    except Exception as e:
        return False, f"❌ {path.name}: {e}"

def extract_urls_from_md(path: Path) -> list[str]:
    urls = []
    pattern = re.compile(r'https?://[^\s\)\]\}]+')
    try:
        content = path.read_text(encoding='utf-8')
        urls = pattern.findall(content)
    except:
        pass
    return urls

def check_url(url: str, timeout: int = 10) -> tuple[bool, str]:
    try:
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Kit Verifier)'})
        with urlopen(req, timeout=timeout) as resp:
            if 200 <= resp.status < 400:
                return True, f"✅ {url}"
            return False, f"⚠️ {url}: HTTP {resp.status}"
    except HTTPError as e:
        return False, f"❌ {url}: HTTP {e.code}"
    except URLError as e:
        return False, f"❌ {url}: {e.reason}"
    except Exception as e:
        return False, f"❌ {url}: {e}"

def main():
    if len(sys.argv) < 2:
        print("Usage: python verify_kit.py <kit_directory>")
        sys.exit(1)

    kit_path = Path(sys.argv[1])
    if not kit_path.exists():
        print(f"❌ Kit directory not found: {kit_path}")
        sys.exit(1)

    print(f"\n🔍 Verifying kit: {kit_path.name}\n")

    all_ok = True

    # 1. Root files
    print("📁 Root files:")
    for pattern in REQUIRED_ROOT:
        ok, msg = check_file_exists(kit_path, pattern)
        print(f"  {msg}")
        if not ok:
            all_ok = False

    # 2. Required directories with minimum files
    print("\n📂 Required directories:")
    for dirname, min_files in [("templates", TEMPLATE_MIN_FILES), ("trackers", TRACKER_MIN_FILES), ("references", REFERENCE_MIN_FILES)]:
        ok, msg = check_dir_min_files(kit_path, dirname, min_files)
        print(f"  {msg}")
        if not ok:
            all_ok = False

    # 3. Validate CSV files
    print("\n📊 CSV validation:")
    csv_files = list((kit_path / "templates").glob("*.csv")) + list((kit_path / "trackers").glob("*.csv"))
    for csv_file in csv_files:
        ok, msg = validate_csv(csv_file)
        print(f"  {msg}")
        if not ok:
            all_ok = False

    # 4. Check platform_links.md has URLs
    print("\n🔗 Platform links validation:")
    links_file = kit_path / "references" / "platform_links.md"
    if links_file.exists():
        urls = extract_urls_from_md(links_file)
        print(f"  Found {len(urls)} URLs in platform_links.md")
        # Check first 10 to avoid rate limiting
        for url in urls[:10]:
            ok, msg = check_url(url)
            print(f"    {msg}")
            if not ok and "HTTP 403" not in msg and "HTTP 429" not in msg:
                all_ok = False
            time.sleep(0.3)  # Be polite
        if len(urls) > 10:
            print(f"    ... and {len(urls) - 10} more (not checked to avoid rate limits)")
    else:
        print("  ❌ platform_links.md not found")
        all_ok = False

    # 5. Check for tax guidance matching jurisdiction
    print("\n📋 Tax guidance:")
    tax_files = list((kit_path / "references").glob("tax*.md")) + list((kit_path / "references").glob("*tax*.md"))
    if tax_files:
        print(f"  ✅ Found tax guidance: {tax_files[0].name}")
    else:
        print("  ⚠️ No tax guidance file found (tax*.md)")
        all_ok = False

    # 6. Check scam warnings
    print("\n⚠️ Scam warnings:")
    scam_files = list((kit_path / "references").glob("scam*.md")) + list((kit_path / "references").glob("*warn*.md"))
    if scam_files:
        print(f"  ✅ Found scam warnings: {scam_files[0].name}")
    else:
        print("  ⚠️ No scam warnings file found")
        all_ok = False

    # 7. Quick README check
    print("\n📖 README:")
    readme = kit_path / "README.md"
    if readme.exists():
        content = readme.read_text(encoding='utf-8')
        if "quick start" in content.lower() or "5-min" in content.lower():
            print("  ✅ Has quick start section")
        else:
            print("  ⚠️ No quick start section found")
    else:
        print("  ❌ README.md missing")
        all_ok = False

    print("\n" + "="*50)
    if all_ok:
        print("✅ KIT VERIFICATION PASSED")
        sys.exit(0)
    else:
        print("❌ KIT VERIFICATION FAILED — fix issues above")
        sys.exit(1)

if __name__ == "__main__":
    main()