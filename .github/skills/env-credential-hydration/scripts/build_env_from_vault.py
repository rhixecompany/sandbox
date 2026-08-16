"""Generic .env hydration from a plaintext credential vault.

Reads raw credential files at runtime so secret values never pass through
tool-call payloads or transcripts. Prints only variable names + masked values.

Usage:
    1. Edit VAULT / OUT paths and the MAP below (filename -> [(env_var, selector)]).
    2. Run:  python build_env_from_vault.py
    3. Verify: git check-ignore .env ; grep the printed masked output.

Selectors:
    None                    -> whole file (first non-empty line)
    "line:N"                -> Nth non-empty line (blank lines skipped)
    "prefix:<token>"        -> first line starting with <token>
    "label:<prefix>"        -> value after first line whose label matches <prefix>
                               (case-insensitive; split on FIRST colon only)
"""
from pathlib import Path

VAULT = Path(r"C:\Users\Alexa\Desktop\Github")   # <- edit: credential vault dir
OUT = Path(r"C:\Users\Alexa\Desktop\SandBox\.env")  # <- edit: output .env path

# (filename, [(env_var, selector)])
MAP = {
    # "access_token.txt": [("GITHUB_ACCESS_TOKEN", None)],
    # "tailgate-api-key.txt": [
    #     ("TAILSCALE_API_KEY", "prefix:tskey-api-"),
    #     ("TAILSCALE_AUTH_KEY", "prefix:tskey-auth-"),
    # ],
    # "openai-api-key.txt": [
    #     ("OPENAI_API_KEY", "label:NEW:"),
    #     ("OPENAI_API_KEY_OLD", "label:OLD:"),
    # ],
}

# Group ordering for the output file: ("Provider", [env_var, ...])
GROUPS = [
    ("OpenAI", ["OPENAI_API_KEY", "OPENAI_API_KEY_OLD"]),
    ("GitHub", ["GITHUB_ACCESS_TOKEN"]),
    ("LLM / AI Providers", []),
    ("Cloud / Infra", []),
    ("Tooling / Misc", []),
]


def read_lines(path: Path) -> list[str]:
    return [ln.strip() for ln in path.read_text(encoding="utf-8", errors="replace").splitlines()]


def extract(lines: list[str], selector) -> str | None:
    if selector is None:
        return next((ln for ln in lines if ln.strip()), None)
    if selector.startswith("line:"):
        idx = int(selector.split(":")[1])
        non_empty = [ln for ln in lines if ln.strip()]
        return non_empty[idx] if idx < len(non_empty) else None
    if selector.startswith("prefix:"):
        pref = selector.split(":", 1)[1]
        return next((ln for ln in lines if ln.startswith(pref)), None)
    if selector.startswith("label:"):
        label = selector.split(":", 1)[1]
        for ln in lines:
            if ln.lower().startswith(label.lower()):
                return ln.split(":", 1)[1].strip() or None
        return None
    raise ValueError(f"unknown selector: {selector}")


def mask(v: str) -> str:
    if len(v) <= 8:
        return "***"
    return v[:6] + "…" + v[-4:]


def main() -> None:
    resolved: dict[str, str] = {}
    missing: list[str] = []

    for fname, specs in MAP.items():
        fpath = VAULT / fname
        if not fpath.exists():
            missing.append(f"{fname} (file missing)")
            continue
        lines = read_lines(fpath)
        for var, sel in specs:
            val = extract(lines, sel)
            if val:
                resolved[var] = val
            else:
                missing.append(f"{var} (not found in {fname})")

    sections = ["# .env — generated from credential vault (edit header)", ""]
    for group_name, vars_ in GROUPS:
        entries = [v for v in vars_ if v in resolved]
        if entries:
            sections.append(f"# --- {group_name} ---")
            sections.extend(f"{v}={resolved[v]}" for v in entries)
            sections.append("")
    OUT.write_text("\n".join(sections), encoding="utf-8")

    print("=== RESOLVED ===")
    for v in sorted(resolved):
        print(f"  {v} = {mask(resolved[v])}")
    print(f"\n=== MISSING ({len(missing)}) ===")
    for m in missing:
        print(f"  {m}")
    print(f"\nWrote {OUT} ({len(resolved)} variables)")


if __name__ == "__main__":
    main()
