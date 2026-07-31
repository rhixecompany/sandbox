"""Build root .env from ../Github credential vault.

Reads raw credential files at runtime so secret values never pass through
tool-call payloads or transcripts. Prints only variable names + masked values.
"""
from pathlib import Path

VAULT = Path(r"C:\Users\Alexa\Desktop\Github")
OUT = Path(r"C:\Users\Alexa\Desktop\SandBox\.env")

# (filename, [(env_var, selector)]) — selector: None = whole file (first non-empty line),
# "label:<prefix>" = value after the first line starting with <prefix>
MAP = {
    "access_token.txt": [("GITHUB_ACCESS_TOKEN", None)],
    "ace-data-cloud-api-key.txt": [("ACE_DATA_CLOUD_API_KEY", None)],
    "alexandereiseghohi_github_accesstoken.txt": [("GITHUB_TOKEN_ALEXANDER", None)],
    "alibaba-access-key.txt": [
        ("ALIBABA_ACCESS_KEY_ID", "line:0"),
        ("ALIBABA_ACCESS_KEY_SECRET", "line:1"),
    ],
    "context7_api_token.txt": [("CONTEXT7_API_TOKEN", None)],
    "groq-cloud-api-key.txt": [("GROQ_API_KEY", None)],
    "hostinger-api-token.txt": [("HOSTINGER_API_TOKEN", None)],
    "huggingface-api-key.txt": [("HUGGINGFACE_API_KEY", None)],
    "huncho-api-key.txt": [("HONCHO_API_KEY", None)],
    "neon-api-key.txt": [("NEON_API_KEY", None)],
    "olama-cloud-api-key.txt": [("OLLAMA_CLOUD_API_KEY", None)],
    "opencode-zen-api-key.txt": [("OPENCODE_ZEN_API_KEY", None)],
    "openrouter_api_key.txt": [("OPENROUTER_API_KEY", None)],
    "sentry_token.txt": [("SENTRY_AUTH_TOKEN", None)],
    "sithery-api-key.txt": [("SMITHERY_API_KEY", None)],
    "tailgate-api-key.txt": [
        ("TAILSCALE_API_KEY", "prefix:tskey-api-"),
        ("TAILSCALE_AUTH_KEY", "prefix:tskey-auth-"),
    ],
    "travely-api-key.txt": [("TAVILY_API_KEY", None)],
    "xgrok-api-key.txt": [("XAI_API_KEY", None)],
    "openai-api-key.txt": [
        ("OPENAI_API_KEY", "label:NEW:"),
        ("OPENAI_API_KEY_OLD", "label:OLD:"),
        ("OPENAI_API_KEY_NEW3", "label:new3:"),
    ],
    "openai-test-api-key.txt": [("OPENAI_TEST_API_KEY", None)],
    "rhixecompany@gmail.com-openai-key.txt": [("OPENAI_API_KEY_RHIXECOMPANY", None)],
    "rhixecompany_github_access_token.txt": [
        ("GITHUB_TOKEN_RHIXECOMPANY", "label:new:"),
        ("GITHUB_TOKEN_RHIXECOMPANY_OLD", "label:old:"),
        ("GITHUB_TOKEN_RHIXECOMPANY_PAT", "label:personal_access_token:"),
    ],
    "rhixecompany-openai-cloud-api-key.txt": [
        ("OPENAI_CLOUD_API_KEY_RHIXECOMPANY", "line:0"),
        ("OPENAI_CLOUD_API_KEY_RHIXECOMPANY_2", "line:1"),
    ],
}

# Group ordering for the output file
GROUPS = [
    ("OpenAI", ["OPENAI_API_KEY", "OPENAI_API_KEY_OLD", "OPENAI_API_KEY_NEW3",
                "OPENAI_TEST_API_KEY", "OPENAI_API_KEY_RHIXECOMPANY",
                "OPENAI_CLOUD_API_KEY_RHIXECOMPANY", "OPENAI_CLOUD_API_KEY_RHIXECOMPANY_2"]),
    ("GitHub", ["GITHUB_ACCESS_TOKEN", "GITHUB_TOKEN_ALEXANDER",
                "GITHUB_TOKEN_RHIXECOMPANY", "GITHUB_TOKEN_RHIXECOMPANY_OLD",
                "GITHUB_TOKEN_RHIXECOMPANY_PAT"]),
    ("Cloud / Infra", ["ALIBABA_ACCESS_KEY_ID", "ALIBABA_ACCESS_KEY_SECRET",
                       "HOSTINGER_API_TOKEN", "NEON_API_KEY",
                       "OLLAMA_CLOUD_API_KEY", "ACE_DATA_CLOUD_API_KEY"]),
    ("LLM / AI Providers", ["GROQ_API_KEY", "HUGGINGFACE_API_KEY", "OPENROUTER_API_KEY",
                            "OPENCODE_ZEN_API_KEY", "XAI_API_KEY", "HONCHO_API_KEY"]),
    ("Tooling / Misc", ["CONTEXT7_API_TOKEN", "SMITHERY_API_KEY", "TAVILY_API_KEY",
                        "SENTRY_AUTH_TOKEN", "TAILSCALE_API_KEY", "TAILSCALE_AUTH_KEY"]),
]


def read_lines(path: Path) -> list[str]:
    return [ln.strip() for ln in path.read_text(encoding="utf-8", errors="replace").splitlines()]


def extract(lines: list[str], selector) -> str | None:
    if selector is None:
        return next((ln for ln in lines if ln.strip()), None)
    if selector.startswith("line:"):
        # nth non-empty line (blank/whitespace-only lines don't count)
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
    raise ValueError(selector)


def mask(v: str) -> str:
    if len(v) <= 8:
        return "***"
    return v[:6] + "…" + v[-4:]


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

# Write .env grouped
sections: list[str] = ["# SandBox root .env — generated from ../Github vault (2026-07-28)",
                       "# WARNING: contains live secrets. Never commit. github-billing-info.txt (PII/PCI) intentionally excluded."]
for group_name, vars_ in GROUPS:
    entries = [v for v in vars_ if v in resolved]
    if entries:
        sections.append("")
        sections.append(f"# --- {group_name} ---")
        for v in entries:
            sections.append(f"{v}={resolved[v]}")
sections.append("")
OUT.write_text("\n".join(sections), encoding="utf-8")

print("=== RESOLVED ===")
for v in sorted(resolved):
    print(f"  {v} = {mask(resolved[v])}")
print(f"\n=== MISSING ({len(missing)}) ===")
for m in missing:
    print(f"  {m}")
print(f"\nWrote {OUT} ({len(resolved)} variables, {len(sections)} lines)")
