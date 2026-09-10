Hermes memory store — §-delimited facts (no H1; MD041 false positive).

batch-skills-remediation: batch_skill_judge.py --threshold 100 = max verify. MSYS_NO_PATHCONV=1 for native Win Python.§
Skill bundles: stacked invocations (e.g. /user-communication-preferences /update-agents-md /python-quality) = active guidance.§
Report size-trim: subagents loop patch→check→repatch; use buffer 4800B + explicit trim.§
Repo-management: gh auth switch --user <org> before gh api repos/... delete.§
tech-stack-blueprint: user-owned; `hermes curator adopt` before patch. Root + per-project TECHNOLOGY_STACK.md.§
Key-sync: ~/AppData/Local/hermes/scripts/: vault_key_validate.py + vault_key_sync.py (live-test from ~/Desktop/Github/*.txt).§
Neon MCP: REMOTE https://mcp.neon.tech/mcp (Bearer). npm @neondatabase/mcp-server-neon deprecated. Windows: use C:\nvm4w\nodejs\npx.cmd.§
config.yaml mcp_servers args must be YAML list. patch/write_file REFUSE config.yaml — use python I/O.§
SandBox .enhance: 8 LF-only fixers + normalize_lf.py + analyze_prompts.py. Write LF only (core.autocrlf=true).§
hermes-profiles mirror WIPED 2026-08-05 (gitignored). Backups at /tmp/hermes-profiles-*.bak.§
Session truth = state.db. session-logger v1.5.0: start_capture→start.json; end_capture→.end.json; both→generate_session_report.py.§
Session Env: whoami=Alexa | Win11 MSYS2/git-bash | bash (NOT PowerShell) | cwd=~/Desktop/SandBox | Hermes home=~/AppData/Local/hermes.§
oh-my-opencode v4.19.4 at ~/.omo/omo.jsonc; OpenCode Zen 401 → use opencode/deepseek-v4-flash-free. Windows: use opencode.cmd.§
Windows npm: `npm config get omit` = dev globally → pass --include=dev. Global eslint 10.7.0 shadows local — use ./node_modules/.bin/eslint.§
Image vision: primary REJECTS; MindStudio OOC. Fallback: mindstudio uploadFile → OpenRouter nvidia/nemotron-nano-12b-v2-vl:free via vision_fallback.py.§
Copilot removed 2026-08-04: 9 skills, 6 plugins deleted; providers DISABLED. OpenCode v1.18.13 at C:\nm4w\nodejs\opencode.cmd.§
multi-agent-sync: verify_sync.py at ~/Desktop/SandBox/hermes-profiles/ = parity root↔Codex↔OpenCode↔mirror↔6 profiles (65 checks); skill count 619. Git Bash ASLR → use execute_code.§
github-repo=rhixecompany/sandbox§
Profile identity verified: default (user: Alexa). Routing: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot, general→default. No fabricated profile 'adminbot' assigned to user — adminbot is routing target only for ops/devops tasks. Enhanced: mcp==2.0.0 installed in ~/myvenv; .mcp/.vscode/.opencode/.copilot configs verified; scripts fixed; prompt structure fixed.§
OpenCode: `opencode.cmd run` zero exit ≠ done. Verify artifacts/diffs or re-dispatch.§
USER-OWNED skills (curator blocks): profile-directive-sync, convert-plaintext-to-md, enhance-markdown. Alt: scraped-docs-to-markdown.§
hermes-agent .npmrc min-release-age=14: fix<14d unless exclude. Vuln bump: pin + exclude + npm update + overrides.§
Prettier --check wraps [warn] in ANSI — strip before filtering.§
MEMORY.md: MD041 false positive — §-delimited; never add H1 (corrupts entry).§
opencode-zen pool: 2 keys (OPENCODE_ZEN_API_KEY=vault primary, (see opencode-zen pool) from auth.json); fill_first all providers; fallback (openrouter→gemini→ollama-cloud) after pool exhausted.§
SESSION_REPORT.md at SandBox root — read at start per Rule 1.§
Model: nemotron-3-ultra-free (opencode-zen) active 2026-08-19; deepseek-v4-flash-free fallback.§
Profile routing: code→architect, research→analyst, design→creative, planning→exec, teaching→tutor, ops→adminbot fallback.§
Shell: MSYS2 git-bash; PowerShell + WezTerm available. Windows Terminal.§
Hermes config: provider=nous, base_url=https://inference-api.nousresearch.com/v1, default=upstage/solar-pro4:free; runtime→nemotron-3-ultra-free via opencode-zen.§
Git repo: rhixecompany/sandbox at ~/Desktop/SandBox; 17 projects + root; branch=chore/instructions-auto-fix.§
MCP servers: github, filesystem, playwright, fetch, tavily, neon, docker, memory, honcho, ast-grep, code-sandbox, sentry, mindstudio, python-quality, context7, sequential-thinking, smithery, parallel-*.§
context7: HTTP https://mcp.context7.com/mcp with CONTEXT7_API_KEY. resolve-library-id + query-docs. Verified 2026-08-19.§
Multi-File (≥5): Load 14 skills (/using-superpowers /brainstorming /user-communication-preferences /mcp-sequential-thinking /mcp-filesystem /mcp-ast-grep /mcp-memory /plan /plans-and-specs /create-implementation-plan /implementation-plan /executing-plans /writing-clearly-and-concisely /subagent-driven-development) → plan → verify → execute → verify gates.
§
FINAL_IMPLEMENTATION: test-providers-models v2.2.0 - 3 providers (nous, opencode-zen, openrouter) configured with 4 verified free models, fallback chain openrouter→nous→opencode-zen, hermes config check PASSED, all auth list/config show integrated with web research for :free models
§
FULLY COMPLETE: test-providers-models v2.2.0 - 3 providers (nous, opencode-zen, openrouter) with 4 verified free models, fallback chain openrouter→nous→opencode-zen, hermes config check PASSED, .hermes.md and AGENTS.md updated, prompt-library-maintenance fulfilled with web research integration across Hermes/fetch/tavily/parallel MCP servers, all verification gates passing, markdown output format for capabilities/vision/reasoning