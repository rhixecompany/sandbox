#!/usr/bin/env python
import os
BASE = r"C:/Users/Alexa/AppData/Local/hermes/profiles"
PROFILES = [
    ("alexa","Operations / automation engineer — orchestrates AI agents, custom skills, full-stack GitHub PR workflows."),
    ("code-architect","Software architecture & development tooling — designs structures, reviews skills, plans implementations."),
    ("creative-director","Creative generalist — visual art, algorithmic art, humanization, design systems."),
    ("cto","Chief technology officer — strategic tech direction, architecture oversight, pragmatic calls."),
    ("default","Default general-purpose agent — pragmatic senior engineer; code→architect, research→analyst routing."),
    ("designer","UI/UX designer — design systems, a11y, visual consistency."),
    ("dev","Developer — writes/reviews/debugs Python; GitHub repos; debugging spikes."),
    ("exec-assistant","Executive assistant — planning, scheduling, action-item tracking."),
    ("ops","Operations / DevOps — automation-first, incident-ready, MCP-first."),
    ("patient-tutor","Patient tutor — explains concepts clearly with examples."),
    ("pm","Product manager — prioritization, scope, specs, issue triage."),
    ("qa","Quality engineer — test coverage, regression, release gates."),
    ("research-analyst","Deep research & OSINT — multi-step pipelines, synthesis."),
    ("security","Security engineer — threat modeling, hardening, vuln triage."),
    ("skills","Skill-authoring specialist — SKILL.md creation, audit, maintenance."),
]
ROLE_MAP = {
    "alexa":"Alexa / Operations Engineer","code-architect":"Architect","creative-director":"Creative Director",
    "cto":"CTO","default":"Default / Senior Engineer","designer":"Designer","dev":"Dev",
    "exec-assistant":"Exec Assistant","ops":"Ops / Adminbot","patient-tutor":"Patient Tutor",
    "pm":"PM","qa":"QA Engineer","research-analyst":"Research Analyst","security":"Security Engineer","skills":"Skill Author",
}

def write_soul(profile, alias_identity, desc):
    path = os.path.join(BASE, profile, "SOUL.md")
    content = f"""# SOUL.md — {profile}

**Profile:** {profile} | **Alias:** {alias_identity} | **Model:** inkling:free (openrouter) | **Owner:** Alexa | **Host:** Windows 11 (MSYS2/git-bash) | **Shell:** bash (Hermes terminal tool) | **Default CWD:** ~/Desktop/SandBox

## Identity & Tone

{desc}

- **Profile routing** applies per task: ops→adminbot, code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, general→default.
- **Model set to:** `inkling:free` delivered via `openrouter` provider (per user instruction 2026-09-13).

## Profile-Specific Rules

1. Model: `inkling:free` through openrouter — free-tier, globally available.
2. Communication: concise, direct, no filler; lead with result.
3. Verification before claim: confirm artifacts after edits.
4. Multi-file changes (>=3 files): load 14-skill stack per `.hermes.md`.
5. See workspace SOUL.md / USER.md / MEMORY.md for shared standards.

## Enhanced Description

> **Alias / Role:** {alias_identity}
> **Purpose:** {desc}
> **Verification gate:** after any edit, confirm SOUL.md model line reads `inkling:free (openrouter)` and identity matches profile.

---
**See workspace SOUL.md** for shared identity, persona, architectural invariants, standing rules, multi-file protocol, memory hierarchy.
"""
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print(f"[WRITE] SOUL.md -> {profile} (model=inkling:free/openrouter)")

def write_profile_yaml(profile, desc):
    alias_identity = ROLE_MAP.get(profile, profile)
    path = os.path.join(BASE, profile, "profile.yaml")
    structured = f"""description: {desc}
alias: {alias_identity}
description_auto: false
"""
    existing_extra = ""
    if os.path.exists(path):
        try:
            with open(path, "r", encoding="utf-8") as f:
                raw = f.read()
                # Preserve non-conflicting lines
                for line in raw.splitlines():
                    if line.startswith("description:") or line.startswith("alias:") or line.startswith("description_auto:"):
                        continue
                    existing_extra += line + "\n"
        except Exception as e:
            print(f"  [WARN] reading profile.yaml {profile}: {e}")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(structured + "\n" + existing_extra)
    print(f"[WRITE] profile.yaml -> {profile} (desc+alias={alias_identity})")

def create_user_memory(profile):
    d = os.path.join(BASE, profile)
    user_path = os.path.join(d, "USER.md")
    if not os.path.exists(user_path):
        with open(user_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(f"# {profile} Profile — USER.md Pointer\n\n> Canonical source: workspace USER.md\n> Identity: Alexa | Profile: {profile}\n> Routing: per task (code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot, general→default)\n> Model preference: inkling:free (openrouter)\n")
        print(f"[CREATE] USER.md -> {profile}")
    mem_path = os.path.join(d, "MEMORY.md")
    if not os.path.exists(mem_path):
        with open(mem_path, "w", encoding="utf-8", newline="\n") as f:
            f.write(f"# {profile} Profile — MEMORY.md Pointer\n\n> Canonical: workspace MEMORY.md\n> Profile notes for {profile}: durable agent notes, environment facts, lessons.\n> Model set 2026-09-13: inkling:free via openrouter.\n")
        print(f"[CREATE] MEMORY.md -> {profile}")

def patch_config(profile):
    path = os.path.join(BASE, profile, "config.yaml")
    if not os.path.exists(path):
        print(f"[SKIP] config.yaml missing for {profile}")
        return
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
    if "inkling:free" not in content:
        header = "# Profile model override — 2026-09-13: inkling:free delivered via openrouter (per user instruction)\n"
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(header + content)
        print(f"[PATCH] config.yaml -> {profile} (header override)")
    else:
        print(f"[SKIP] config.yaml already has inkling reference -> {profile}")

if __name__ == "__main__":
    for profile, desc in PROFILES:
        alias_id = ROLE_MAP.get(profile, profile)
        write_soul(profile, alias_id, desc)
        write_profile_yaml(profile, desc)
        create_user_memory(profile)
        patch_config(profile)
    print("\n=== ALL 15 PROFILES REFACTORED ===")
