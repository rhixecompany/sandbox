#!/usr/bin/env python3
"""
Hermes Installation Verification Script
Checks that Hermes is properly installed and configured.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_command(cmd, capture=True):
    """Run a command and return result."""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=capture, text=True)
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)

def check_hermes_cli():
    """Check hermes CLI is available."""
    ok, out, err = run_command("hermes --version")
    if ok:
        print(f"✅ hermes CLI: {out.strip()}")
        return True
    else:
        print(f"❌ hermes CLI not found: {err}")
        return False

def check_config():
    """Check config file exists."""
    config_path = Path.home() / ".hermes" / "config.yaml"
    if config_path.exists():
        print(f"✅ Config: {config_path}")
        return True
    else:
        print(f"❌ Config not found: {config_path}")
        return False

def check_soul():
    """Check SOUL.md exists."""
    soul_path = Path.home() / ".hermes" / "SOUL.md"
    if soul_path.exists():
        print(f"✅ SOUL.md: {soul_path}")
        return True
    else:
        print(f"❌ SOUL.md not found: {soul_path}")
        return False

def check_memories():
    """Check memory files."""
    mem_dir = Path.home() / ".hermes" / "memories"
    user_md = mem_dir / "USER.md"
    memory_md = mem_dir / "MEMORY.md"
    
    ok = True
    if user_md.exists():
        print(f"✅ USER.md: {user_md}")
    else:
        print(f"⚠️  USER.md not found: {user_md}")
    
    if memory_md.exists():
        print(f"✅ MEMORY.md: {memory_md}")
    else:
        print(f"⚠️  MEMORY.md not found: {memory_md}")
    
    return ok

def check_skills_dir():
    """Check skills directory."""
    skills_dir = Path.home() / ".hermes" / "skills"
    if skills_dir.exists():
        skill_count = len(list(skills_dir.rglob("SKILL.md")))
        print(f"✅ Skills dir: {skills_dir} ({skill_count} skills)")
        return True
    else:
        print(f"❌ Skills dir not found: {skills_dir}")
        return False

def check_providers():
    """Check configured providers."""
    ok, out, err = run_command("hermes auth list")
    if ok:
        print(f"✅ Providers configured")
        for line in out.strip().split('\n'):
            if line.strip():
                print(f"   - {line.strip()}")
        return True
    else:
        print(f"⚠️  No providers configured or auth list failed")
        return False

def main():
    print("=" * 50)
    print("Hermes Installation Verification")
    print("=" * 50)
    
    checks = [
        ("CLI", check_hermes_cli),
        ("Config", check_config),
        ("SOUL.md", check_soul),
        ("Memories", check_memories),
        ("Skills", check_skills_dir),
        ("Providers", check_providers),
    ]
    
    results = []
    for name, check_fn in checks:
        print(f"\n🔍 Checking {name}...")
        results.append((name, check_fn()))
    
    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    
    passed = sum(1 for _, ok in results if ok)
    total = len(results)
    
    for name, ok in results:
        status = "PASS" if ok else "FAIL"
        print(f"  {status}: {name}")
    
    print(f"\nResult: {passed}/{total} checks passed")
    
    if passed == total:
        print("🎉 All checks passed!")
        return 0
    else:
        print("⚠️  Some checks failed. Run with --help for guidance.")
        return 1

if __name__ == "__main__":
    sys.exit(main())