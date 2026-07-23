import asyncio
import os, re, glob, json

ROOT = os.path.join(os.environ["LOCALAPPDATA"], "hermes", "skills")
# also scan references under skills
TARGETS = []
for base in [ROOT]:
    for md in glob.glob(os.path.join(base, "**", "*.md"), recursive=True):
        TARGETS.append(md)

PATH_RE = re.compile(r'C:/Users/Alexa/AppData/Local/hermes|C:\\Users\\Alexa\\AppData\\Local\\hermes|~/AppData/Local/hermes|\$HOME/AppData/Local/hermes')

fence_re = re.compile(r'^```(\w*)')
def split_blocks(lines):
    blocks = []  # (lang, start, end, list_of_lines)
    i = 0
    cur = None
    for idx, ln in enumerate(lines):
        m = fence_re.match(ln.strip())
        if m and cur is None:
            cur = {"lang": m.group(1).lower(), "start": idx, "lines": []}
        elif m and cur is not None:
            cur["end"] = idx
            blocks.append(cur)
            cur = None
        elif cur is not None:
            cur["lines"].append(ln)
    return blocks

async def main():
    loop = asyncio.get_running_loop()
    stats = {"in_code": 0, "in_prose": 0, "by_lang": {}, "files_with_code_matches": 0,
             "python_code_matches": 0, "powershell_code_matches": 0}
    file_report = []
    for md in TARGETS:
        text = await loop.run_in_executor(None, _read_file, md)
        if text is None:
            continue
        if not PATH_RE.search(text):
            continue
        lines = text.splitlines()
        blocks = split_blocks(lines)
        in_code = 0
        in_prose = 0
        for b in blocks:
            lang = b["lang"]
            for ln in b["lines"]:
                if PATH_RE.search(ln):
                    in_code += 1
                    stats["by_lang"][lang] = stats["by_lang"].get(lang, 0) + 1
                    if lang in ("python", "py"):
                        stats["python_code_matches"] += 1
                    if lang in ("powershell", "pwsh"):
                        stats["powershell_code_matches"] += 1
        # prose = total matches - in_code
        total = len(PATH_RE.findall(text))
        in_prose = total - in_code
        if in_code > 0:
            stats["files_with_code_matches"] += 1
        stats["in_code"] += in_code
        stats["in_prose"] += in_prose
        if in_code > 0:
            file_report.append((md.replace(ROOT, "<skills>"), in_code, in_prose,
                                {b["lang"]: sum(1 for l in b["lines"] if PATH_RE.search(l)) for b in blocks if any(PATH_RE.search(l) for l in b["lines"])}))

    print(f"Scanned {len(TARGETS)} md files under skills/")
    print(f"Matches INSIDE code blocks (in-scope): {stats['in_code']}")
    print(f"Matches in PROSE (out-of-scope):       {stats['in_prose']}")
    print(f"Files with in-code matches:            {stats['files_with_code_matches']}")
    print(f"By code-block language: {stats['by_lang']}")
    print(f"python code matches: {stats['python_code_matches']} | powershell: {stats['powershell_code_matches']}")
    print("\n=== Files with in-code matches (lang:count) ===")
    for fr in sorted(file_report, key=lambda x: -x[1]):
        print(f"  {fr[0]}: code={fr[1]} prose={fr[2]} langs={fr[3]}")

def _read_file(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except Exception:
        return None

if __name__ == "__main__":
    asyncio.run(main())
