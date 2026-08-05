#!/usr/bin/env python3
"""
Cross-platform sync verification script for Hermes, Codex, and OpenCode.
Run with: MSYS_NO_PATHCONV=1 python3 verify_sync.py
"""

import os
import json
import yaml
import tomllib
import sys

def check(ok, msg):
    """Record check result"""
    if ok:
        PASSES.append(msg)
    else:
        ERRORS.append(msg)

PASSES = []
ERRORS = []

def expand(path):
    return os.path.expanduser(path)

# ===== VERIFICATION CHECKS =====

# 1. All platform roots exist
print("Checking platform roots...")
roots = {
    "Hermes": expand("~/AppData/Local/hermes/"),
    "Codex": expand("~/.codex/"),
    "OpenCode": expand("~/.opencode/"),
}
for name, path in roots.items():
    check(os.path.exists(path), f"{name} root exists: {path}")

# 2. Skills count match (name-based, after dedup)
def get_skill_names(root):
    names = set()
    for dirpath, dirnames, filenames in os.walk(expand(root)):
        if 'SKILL.md' in filenames:
            rel = os.path.relpath(dirpath, expand(root))
            if rel == '.':
                continue
            names.add(os.path.basename(dirpath))
    return names

hermes_skills = get_skill_names("~/AppData/Local/hermes/skills")
codex_skills = get_skill_names("~/.codex/skills/hermes-auto")
opencode_skills = get_skill_names("~/.opencode/skills/hermes-auto")

check(len(hermes_skills) == len(codex_skills) == len(opencode_skills),
      f"Skill counts match: Hermes={len(hermes_skills)}, Codex={len(codex_skills)}, OpenCode={len(opencode_skills)}")

check(hermes_skills == codex_skills, "Hermes skills == Codex skills (by name)")
check(hermes_skills == opencode_skills, "Hermes skills == OpenCode skills (by name)")

# 3. No flat duplicates in target platforms
def has_flat_duplicates(root):
    flat = set()
    cat = set()
    for dirpath, dirnames, filenames in os.walk(expand(root)):
        if 'SKILL.md' in filenames:
            rel = os.path.relpath(dirpath, expand(root))
            if rel == '.':
                continue
            name = os.path.basename(dirpath)
            if os.sep not in rel:
                flat.add(name)
            else:
                cat.add(name)
    return flat & cat

codex_dups = has_flat_duplicates("~/.codex/skills/hermes-auto")
opencode_dups = has_flat_duplicates("~/.opencode/skills/hermes-auto")

check(len(codex_dups) == 0, f"Codex has no flat duplicates: {codex_dups}")
check(len(opencode_dups) == 0, f"OpenCode has no flat duplicates: {opencode_dups}")

# 4. Hooks synced to workspace
workspace_hooks = expand("~/Desktop/SandBox/.github/hooks")
for hook in ["session-logger", "session-auto-commit", "governance-audit"]:
    check(os.path.exists(os.path.join(workspace_hooks, hook)),
          f"Workspace hook exists: {hook}")

# 5. Hermes profiles exist
hermes_profiles = expand("~/AppData/Local/hermes/profiles")
profile_dirs = [d for d in os.listdir(hermes_profiles) if os.path.isdir(os.path.join(hermes_profiles, d))]
check(len(profile_dirs) >= 13, f"Hermes has >=13 profiles: {len(profile_dirs)}")

# 6. Codex agents exist
codex_agents = expand("~/.codex/agents")
agent_files = [f for f in os.listdir(codex_agents) if f.endswith('.toml')]
check(len(agent_files) >= 140, f"Codex has >=140 agents: {len(agent_files)}")

# 7. Config files exist
check(os.path.exists(expand("~/AppData/Local/hermes/config.yaml")), "Hermes config.yaml exists")
check(os.path.exists(expand("~/.codex/config.toml")), "Codex config.toml exists")
check(os.path.exists(expand("~/Desktop/SandBox/opencode.json")), "OpenCode workspace config exists")

# 8. Cross-platform inventory document exists
check(os.path.exists(expand("~/Desktop/SandBox/docs/cross-platform-inventory.md")),
      "Cross-platform inventory document exists")

# 9. Verify config consistency - models
with open(expand("~/AppData/Local/hermes/config.yaml")) as f:
    hermes_config = yaml.safe_load(f)
hermes_model = hermes_config.get('model', {}).get('default', '')

with open(expand("~/.codex/config.toml"), 'rb') as f:
    codex_config = tomllib.load(f)
codex_model = codex_config.get('model', '')

with open(expand("~/Desktop/SandBox/opencode.json")) as f:
    opencode_config = json.load(f)
opencode_model = opencode_config.get('model', '')

# Models should be platform-optimized, not identical
check(hermes_model == 'gpt-5.4-mini', f"Hermes model: {hermes_model}")
check(codex_model == 'gpt-5.4-mini', f"Codex model: {codex_model}")
check(opencode_model == 'opencode/deepseek-v4-flash-free', f"OpenCode model: {opencode_model}")

# 10. OpenCode CLI works
import subprocess
result = subprocess.run(["C:\\nvm4w\\nodejs\\opencode.cmd", "--version"], capture_output=True, text=True)
check(result.returncode == 0, f"OpenCode CLI works: {result.stdout.strip()}")

result = subprocess.run(["C:\\nvm4w\\nodejs\\opencode.cmd", "auth", "list"], capture_output=True, text=True)
check(result.returncode == 0 and "credentials" in result.stdout.lower(),
      "OpenCode auth list shows credentials")

# ===== REPORT =====
print(f"\n=== VERIFICATION REPORT ===")
print(f"Passes: {len(PASSES)}")
print(f"Errors: {len(ERRORS)}")

if ERRORS:
    print("\nERRORS:")
    for e in ERRORS:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("\nAll checks passed! ✓")
    sys.exit(0)
