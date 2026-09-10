#!/usr/bin/env python3
import os, hashlib
base = r"C:\Users\Alexa\Desktop\SandBox"
roots = [".github", ".copilot", ".codex", ".opencode", ".hermes"]
print("=== AGENTS ===")
for r in roots:
    ap = os.path.join(base, r, "agents")
    if os.path.exists(ap):
        items = os.listdir(ap)
        print(f"{r}/agents: {len(items)} files: {sorted(items)[:5]}...")
    else:
        print(f"{r}/agents: MISSING")
print("\n=== HOOKS ===")
for r in roots:
    hp = os.path.join(base, r, "hooks")
    if os.path.exists(hp):
        items = [x for x in os.listdir(hp) if x != '__pycache__']
        print(f"{r}/hooks: {len(items)} files")
    else:
        print(f"{r}/hooks: MISSING")
print("\n=== .github/skills ===")
sp = os.path.join(base, ".github", "skills")
if os.path.exists(sp):
    skills = sorted(os.listdir(sp))
    print(f"count: {len(skills)}")
    for s in skills: print(f"  {s}")
print("\n=== .github/templates ===")
tp = os.path.join(base, ".github", "templates")
if os.path.exists(tp):
    print(sorted(os.listdir(tp)))
print("\n=== .github/instructions ===")
ip = os.path.join(base, ".github", "instructions")
if os.path.exists(ip):
    print(sorted(os.listdir(ip)))
else:
    print("MISSING")
print("\n=== .github/prompts count ===")
pp = os.path.join(base, ".github", "prompts")
if os.path.exists(pp):
    prompts = [x for x in os.listdir(pp) if x.endswith('.prompt.md')]
    print(f"{len(prompts)} .prompt.md files")
print("\n=== MCP configs ===")
for r in [".github", ".copilot", ".codex"]:
    mp = os.path.join(base, r, "mcp.json")
    if os.path.exists(mp):
        print(f"{r}/mcp.json: {os.path.getsize(mp)} bytes")
print("\n=== .hermes/hooks ===")
hp = os.path.join(base, ".hermes", "hooks")
if os.path.exists(hp):
    items = sorted(os.listdir(hp))
    print(f"{len(items)} items: {items}")
else:
    print("MISSING")
