#!/usr/bin/env python3
"""Create/repair memory files (USER.md, MEMORY.md) for the 7 stub Hermes
profiles that are missing them, and fix the stub SOUL.md header line to match
the profile tagline. Idempotent: re-running produces no changes if already done.

Root canonical sources (read-only here):
  - MEMORY.md  -> copied verbatim to every profile
  - USER.md    -> per-profile authored from root + profile tagline/role

Stub profiles (no memories/ dir, 513B default SOUL.md):
  cto, designer, dev, ops, pm, qa, security

Safe by design:
  - Never touches config.yaml / .env / auth.json (sensitive, guarded).
  - Only WRITES non-default profile memories + edits the stub SOUL.md header.
  - MEMORY.md is identical across all profiles (universal agent notes).
"""
import os
import sys

HERMES = os.environ.get("HERMES_HOME", r"C:/Users/Alexa/AppData/Local/hermes")
ROOT_MEM = os.path.join(HERMES, "memories", "MEMORY.md")

# Profile -> (tagline, role). Used for SOUL header + USER Identity/Model lines.
PROFILES = {
    "cto": ("OWL: Chief technology officer. Strategic tech direction, architecture oversight, pragmatic calls.", "CTO"),
    "designer": ("OWL: Product designer. UX clarity, visual polish, accessible interfaces.", "Designer"),
    "dev": ("OWL: Software developer. Build features cleanly, test, ship.", "Developer"),
    "ops": ("OWL: Operations engineer. Reliability, automation, incident response.", "Operations"),
    "pm": ("OWL: Product manager. Prioritization, scope, stakeholder alignment.", "Product manager"),
    "qa": ("OWL: Quality engineer. Test coverage, regression hunts, release gates.", "QA engineer"),
    "security": ("OWL: Security engineer. Threat modeling, hardening, vuln triage.", "Security engineer"),
}

MODEL = "deepseek-v4-flash-free (opencode-zen)"


def read_text(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write_text(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"  wrote {path} ({len(content)}B)")


def make_user(profile, tagline, role):
    # Schema: frontmatter + Identity + Model + Execution Preferences (lowercase match
    # in validator). Non-default requires only a "model" keyword somewhere.
    return f"""---
user: Alexa
---
# USER.md — {profile} profile

Pointer file. Canonical durable rules in MEMORY.md.

## Identity
- Name: Alexa | Workspace: ~/Desktop/SandBox | Profile: {profile} | Role: {role}
- Persona: {tagline}

## Environment Stack
- OS: Windows 11 (MSYS2/git-bash)
- Runtimes: Bun, Python 3.11/3.13 (uv), TypeScript strict
- Tooling: Ruff, Pyright, ESLint, Prettier, Markdownlint

## Model
- {MODEL}

## Execution Preferences
- **Communication**: concise bullets, lead with result, skip fluff
- **Code**: TypeScript strict, JSDoc/docstring *why* not *what*
- **Skills**: structured SKILL.md (YAML frontmatter + md body)
- **Hooks**: ruff format+check --fix pre-commit
- **Execution**: read→patch→verify, MCP-first, no backup files
- **Profile routing**: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→alexa

## Standing Goal
Maintain/enhance all prompts at .github/prompts/ with DRY, structural sections. Uses stacked skill bundles (using-superpowers, subagent-driven-development, brainstorming) for prompt work.

## Honcho Memory
Active (hybrid mode). Use honcho_profile/context/reasoning/search as needed.
"""


def fix_soul_header(soul_path, profile, tagline):
    text = read_text(soul_path)
    # Stub SOUL is a single default paragraph; replace with a minimal profile header +
    # the original default body so it still loads and reflects the profile.
    default_body = (
        "You are Hermes Agent, an intelligent AI assistant created by Nous Research. "
        "You are helpful, knowledgeable, and direct. You assist users with a wide range of "
        "tasks including answering questions, writing and editing code, analyzing information, "
        "creative work, and executing actions via your tools. You communicate clearly, admit "
        "uncertainty when appropriate, and prioritize being genuinely useful over being verbose "
        "unless otherwise directed below. Be targeted and efficient in your exploration and "
        "investigations."
    )
    new_header = (
        f"# SOUL.md — Core Operating Principles\n\n"
        f"**Profile:** {profile} | **Model:** {MODEL} | **Owner:** Alexa | "
        f"**Host:** Windows 11 (MSYS2/git-bash) | **Shell:** bash (Hermes terminal tool) | "
        f"**Default CWD:** ~/Desktop/SandBox\n\n"
        f"**Identity:** {tagline}\n\n---\n\n"
    )
    # If the file already starts with our header marker, skip (idempotent).
    if text.startswith("# SOUL.md — Core Operating Principles"):
        print(f"  skip SOUL header (already profile-formatted): {soul_path}")
        return
    write_text(soul_path, new_header + default_body + "\n")


def main():
    root_mem = read_text(ROOT_MEM)
    if len(root_mem) > 6000:
        print(f"WARN: root MEMORY.md is {len(root_mem)} chars (>6000); not copying as-is", file=sys.stderr)
        return 1
    # root USER.md validated as the canonical source for full profiles; stub profiles
    # get an authored per-profile USER.md (see make_user) so they pass schema checks.

    for profile, (tagline, role) in PROFILES.items():
        pdir = os.path.join(HERMES, "profiles", profile)
        mdir = os.path.join(pdir, "memories")
        print(f"[profile {profile}]")
        # MEMORY.md verbatim
        write_text(os.path.join(mdir, "MEMORY.md"), root_mem)
        # USER.md authored
        write_text(os.path.join(mdir, "USER.md"), make_user(profile, tagline, role))
        # SOUL.md header fix
        fix_soul_header(os.path.join(pdir, "SOUL.md"), profile, tagline)
    print("DONE. Run validate_memories.py to confirm.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
