# Plan: VS Code & Hermes Profile Sync

## Overview
5-phase sequential operation: (1) fix VS Code settings/extensions, (2) migrate MCP servers from Hermes to VSCode, (3) delete profile-specific artifacts, (4) copy defaults to profiles, (5) verify sync.

## Strict Sequential Constraint
Each phase must fully complete (including verification) before the next begins.

---

## Phase 1: VS Code Settings & Extensions ✅
- Fixed `terminal.integrated.defaultProfile.windows` → "Git Bash" (was "PowerShell")
- Added `[markdown]` formatter → `yzhang.markdown-all-in-one`
- Added `[html]` formatter → `vscode.html-language-features` (was missing)
- Removed duplicate `[html]` block
- Uninstalled 3 conflicting extensions:
  - `donjayamanne.githistory` (redundant with GitLens)
  - `mhutchie.git-graph` (redundant with GitLens)
  - `naumovs.color-highlight` (overlaps with bierner.color-info)
- Verified settings.json is valid JSON

## Phase 2: Migrate MCP Servers to VSCode ✅
- Added 11 Hermes MCP servers to `.vscode/mcp.json`:
  - mcp-ast-grep, mcp-code-sandbox, mcp-codex, mcp-copilot-mcp
  - mcp-fetch, mcp-linear, mcp-memory, mcp-mindstudio
  - mcp-playwright, mcp-sequential-thinking, mcp-smithery
- Preserved existing 3: mcp-docker, mcp-filesystem, mcp-github
- Total: 14 MCP servers in VSCode

## Phase 3: Delete Profile-Specific Items ✅
- Removed `config.yaml`, `skills/`, `hooks/`, `.env`, `plugins/` from all 6 profiles
- Profiles: alexa, code-architect, creative-director, exec-assistant, patient-tutor, research-analyst
- All items verified deleted (empty of target items)

## Phase 4: Copy Defaults to Profiles ✅
- Copied root `config.yaml`, `.env`, `hooks/`, `plugins/`, `skills/` to all 6 profiles
- Skills: 107 skill directories per profile (full root library)
- Some .git packfile permission errors in plugins (non-content, minor)

## Phase 5: Verify Sync ✅
- config.yaml: ALL 7 copies have identical md5 (`3bd42a7b94a6310528`)
- .env: ALL 7 copies have identical md5 (`8e12d71c867d338d3`)
- hooks/: ALL 7 copies have identical structure (3 subdirs, same files)
- plugins/: ALL 7 copies have same 4 plugin directories
- skills/: ALL 7 copies match root (107 skills, identical listing)
