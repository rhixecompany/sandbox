#!/usr/bin/env python3
"""Batch delete all non-default Hermes profiles."""
import asyncio
import subprocess, sys, os

profiles = [
    "alexa", "code-architect", "creative-director", "debugger",
    "devops-expert", "exec-assistant", "github-actions-expert", "hermes",
    "implementation-plan", "mentor", "patient-tutor", "planner",
    "power-bi-data-modeling-expert", "prd", "prompt-engineer", "qa-subagent",
    "research-analyst", "reviewer", "specification",
    "tanstack-start-shadcn-tailwind", "terraform", "arch", "architect"
]

hermes_py = r"C:\Users\Alexa\AppData\Local\hermes\.venv\Scripts\hermes.exe"
# Fallback: find hermes in PATH
import shutil
hermes = shutil.which("hermes") or hermes_py

async def main():
    print(f"Using hermes: {hermes}")
    print()

    for p in profiles:
        print(f"--- Deleting {p} ---")
        try:
            result = await asyncio.to_thread(
                subprocess.run,
                [hermes, "profile", "delete", p],
                input=f"{p}\n",
                text=True,
                capture_output=True,
                timeout=30
            )
            print(result.stdout[-500:] if result.stdout else "")
            if result.stderr:
                print(f"STDERR: {result.stderr[-300:]}")
            print(f"Exit code: {result.returncode}")
        except subprocess.TimeoutExpired:
            print(f"TIMEOUT deleting {p}")
        except Exception as e:
            print(f"ERROR: {e}")
        print()

    print("DONE")

if __name__ == "__main__":
    asyncio.run(main())
