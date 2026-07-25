#!/usr/bin/env python3
"""Batch delete all non-default Hermes profiles with auto-confirmation.

Usage:
    python batch-profile-operations.py           # Delete all listed profiles
    python batch-profile-operations.py --list    # Only list, don't delete

Requires: hermes CLI in PATH

Technique: pipes profile name as stdin to satisfy `hermes profile delete` 
interactive confirmation prompt. The CLI reads confirmation from stdin
(input()), so echo+pipe or subprocess input= works.
"""

import subprocess
import shutil
import sys

PROFILES = [
    # --- Configured profiles ---
    "alexa", "code-architect", "creative-director",
    "exec-assistant", "patient-tutor", "research-analyst",
    # --- Unconfigured shells ---
    "arch", "architect", "debugger", "devops-expert",
    "github-actions-expert", "hermes", "implementation-plan",
    "mentor", "planner", "power-bi-data-modeling-expert",
    "prd", "prompt-engineer", "qa-subagent", "reviewer",
    "specification", "tanstack-start-shadcn-tailwind", "terraform",
]


def get_hermes():
    """Find hermes CLI in PATH or common locations."""
    hermes = shutil.which("hermes")
    if hermes:
        return hermes
    # Common install paths
    candidates = [
        r"C:\Users\Alexa\AppData\Local\hermes\hermes-agent\venv\Scripts\hermes.exe",
        r"C:\Users\Alexa\AppData\Local\hermes\.venv\Scripts\hermes.exe",
    ]
    for c in candidates:
        if shutil.which(c) or __import__("os").path.exists(c):
            return c
    return None


def delete_profile(hermes, name):
    """Delete a single profile, piping name as confirmation."""
    print(f"\n--- Deleting {name} ---")
    try:
        result = subprocess.run(
            [hermes, "profile", "delete", name],
            input=f"{name}\n",
            text=True,
            capture_output=True,
            timeout=30,
        )
        output = result.stdout.strip()
        if "deleted" in output.lower():
            print(f"✅ Deleted: {name}")
        elif "does not exist" in output.lower():
            print(f"⏭️  Does not exist: {name}")
        elif "reserved" in output.lower():
            print(f"⛔ Reserved name: {name}")
        elif "Could not remove" in output:
            # Gateway lock blocking (Windows)
            print(f"❌ Lock blocked: {name} — kill gateway process first")
            print(f"   {output[-200:]}")
        else:
            print(output[-300:])
        if result.stderr:
            err = result.stderr.strip()
            if err:
                print(f"   STDERR: {err[-200:]}")
        return result.returncode
    except subprocess.TimeoutExpired:
        print(f"⏰ Timeout: {name}")
        return -1
    except Exception as e:
        print(f"💥 Error: {e}")
        return -2


def main():
    hermes = get_hermes()
    if not hermes:
        print("ERROR: hermes CLI not found")
        sys.exit(1)

    print(f"Using hermes: {hermes}")

    if "--list" in sys.argv:
        print(f"Profiles that would be deleted ({len(PROFILES)}):")
        for p in PROFILES:
            print(f"  - {p}")
        return

    results = {}
    for name in PROFILES:
        rc = delete_profile(hermes, name)
        results[name] = rc

    print("\n" + "=" * 50)
    print("SUMMARY")
    print("=" * 50)
    deleted = [n for n, rc in results.items() if rc == 0]
    failed = [n for n, rc in results.items() if rc != 0]
    if deleted:
        print(f"✅ Deleted ({len(deleted)}): {', '.join(deleted)}")
    if failed:
        print(f"❌ Failed ({len(failed)}): {', '.join(failed)}")

    print("\nRemaining profiles:")
    subprocess.run([hermes, "profile", "list"])


if __name__ == "__main__":
    main()
