#!/usr/bin/env python3
"""
Create missing memories/ directories and USER.md/MEMORY.md for all profiles
"""
import os
from pathlib import Path

HERMES_ROOT = Path("C:/Users/Alexa/AppData/Local/hermes")
PROFILES_DIR = HERMES_ROOT / "profiles"

# Profile configurations with their models
PROFILE_CONFIGS = {
    "arch": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "architect": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "debugger": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "devops-expert": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "github-actions-expert": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "hermes": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "implementation-plan": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "mentor": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "planner": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "power-bi-data-modeling-expert": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "prd": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "prompt-engineer": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "qa-subagent": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "reviewer": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "specification": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "tanstack-start-shadcn-tailwind": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
    "terraform": {"model": "—", "provider": "—", "purpose": "Unconfigured profile"},
}

def create_user_md(profile_name, config):
    """Generate USER.md content for a profile"""
    return f"""# USER.md — {profile_name} Profile

## Identity
- **Name:** Alexa
- **OS:** Windows 11
- **Shell:** POSIX (git-bash/MSYS)

## Active Model & Providers
- **Profile Model:** {config['model']}
- **Providers:** {config['provider']}

## Execution Preferences
- Conservative non-destructive config edits
- Explicit confirmation before destructive actions
- Read-first operations; verify with import+log grep
- Purpose: {config['purpose']}

## Standards
See SOUL.md for code quality, commit style, response style, security, file operations.
"""

def create_memory_md(profile_name):
    """Generate MEMORY.md content for a profile"""
    return f"""# MEMORY.md — {profile_name} Profile

<!-- Add durable facts specific to this profile here -->
<!-- Format: fact: description (YYYY-MM-DD) -->
"""

for profile_name, config in PROFILE_CONFIGS.items():
    profile_dir = PROFILES_DIR / profile_name
    memories_dir = profile_dir / "memories"
    
    # Create memories directory
    memories_dir.mkdir(exist_ok=True)
    
    # Create USER.md
    user_md = memories_dir / "USER.md"
    if not user_md.exists():
        user_md.write_text(create_user_md(profile_name, config))
        print(f"Created: {user_md}")
    else:
        print(f"Exists: {user_md}")
    
    # Create MEMORY.md
    memory_md = memories_dir / "MEMORY.md"
    if not memory_md.exists():
        memory_md.write_text(create_memory_md(profile_name))
        print(f"Created: {memory_md}")
    else:
        print(f"Exists: {memory_md}")

print("Done!")