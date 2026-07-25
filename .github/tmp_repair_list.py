import json
import re
from pathlib import Path

ROOT = Path("C:/Users/Alexa/Desktop/SandBox/.github/prompts")
TEMPLATES = ROOT / "templates"
REPORT_OUT = ROOT.parent / "docs" / "prompt-repair-list.json"

link_ref = re.compile(r"\[`[^`]*`\]\((?:\\.?/)?templates/[^\)]*\)")
bt_ref = re.compile(r"`(?:\\.?/)?templates/[^`]*`")
link_url = re.compile(r"\]\((?:\\.?/)?templates([^\)]*)\)")
GLOB_CHARS = "*?"
PLACEHOLDER_RE = re.compile(r"<[^>]+>")


def normalize(path: str) -> str:
    path = path.strip()
    path = re.sub(r"^\[(?:`)?[^`]*?(?:`)?\]\((?:\\.?/)?", "", path)
    path = re.sub(r"\)$", "", path)
    path = path.strip("`")
    path = re.sub(r"^\\./+", "", path)
    path = re.sub(r"^templates/+", "", path)
    return path.strip("/").strip()


def is_placeholder(path: str) -> bool:
    if not path:
        return True
    if any(c in path for c in GLOB_CHARS):
        return True
    return bool(PLACEHOLDER_RE.search(path))


repair_list = []
for pf in sorted(ROOT.glob("*.prompt.md")):
    text = pf.read_text(encoding="utf-8", errors="ignore")
    raw_links = link_ref.findall(text)
    raw_bts = bt_ref.findall(text)
    raw_bts = [b for b in raw_bts if b not in " ".join(raw_links)]
    missing_files = set()
    missing_dirs = set()
    for link in raw_links:
        m = link_url.search(link)
        if not m:
            continue
        path = normalize(m.group(1))
        if not path or is_placeholder(path):
            continue
        if path.endswith("/"):
            if not (TEMPLATES / path).exists():
                missing_dirs.add(path)
            continue
        resolved = TEMPLATES / path
        if not resolved.exists():
            if resolved.is_dir() or (not resolved.suffix and (TEMPLATES / (path + "/")).exists()):
                missing_dirs.add(path + "/")
            else:
                missing_files.add(path)
    for b in raw_bts:
        path = normalize(b)
        if not path or is_placeholder(path):
            continue
        resolved = TEMPLATES / path
        if not resolved.exists():
            if not path.endswith("/") and resolved.is_dir():
                missing_dirs.add(path + "/")
                continue
            if path.endswith("/") or resolved.is_dir():
                if not (TEMPLATES / path).exists():
                    missing_dirs.add(path)
                continue
            missing_files.add(path)
    if missing_files or missing_dirs:
        repair_list.append(
            {
                "prompt": pf.name,
                "missing_files": sorted(missing_files),
                "missing_dirs": sorted(missing_dirs),
            }
        )

REPORT_OUT.write_text(json.dumps(repair_list, indent=2), encoding="utf-8")
print("repair_list_written:", REPORT_OUT)
print("prompts_with_missing_files:", sum(1 for r in repair_list if r["missing_files"]))
print("prompts_with_missing_dirs:", sum(1 for r in repair_list if r["missing_dirs"]))
print("\nSample missing files:")
for r in repair_list[:20]:
    if r["missing_files"]:
        print(r["prompt"], "->", r["missing_files"][:5])
