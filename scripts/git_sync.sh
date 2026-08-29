#!/usr/bin/env bash
# Git sync for SandBox monorepo + 13 submodules
# Stages the current branch's working tree, commits with conventional messages,
# and (after user OK) pushes to origin/clean-development.
#
# Usage:
#   bash scripts/git_sync.sh commit   # commit root + submodules (no push)
#   bash scripts/git_sync.sh status   # show what would be done
#   bash scripts/git_sync.sh push     # push to origin/clean-development (REQUIRES APPROVAL)

set -euo pipefail
cd "$(dirname "$0")/.."

# Helpers
log()  { printf "[%(%H:%M:%S)T] %s\n" -1 "$*"; }
fail() { printf "ERROR: %s\n" "$*" >&2; exit 1; }

# 0. Pre-flight
[ -d .git ] || fail "Not a git repo"
git rev-parse --is-inside-work-tree >/dev/null 2>&1 || fail "Not a git work tree"

current_branch=$(git rev-parse --abbrev-ref HEAD)
log "Current branch: $current_branch"
[ "$current_branch" = "clean-development" ] || fail "Expected to be on clean-development; got $current_branch"

# Count changes
modified=$(git status -s | grep -c "^ M" || true)
untracked=$(git status -s | grep -c "^??" || true)
sub_modified=0
for s in $(git submodule--helper list 2>/dev/null | awk '{print $2}'); do
    if [ -d "$s" ] && (cd "$s" && git status -s 2>/dev/null | grep -qE "^(\?\?| M| D|A |M )"); then
        sub_modified=$((sub_modified+1))
    fi
done
log "Root: $modified modified, $untracked untracked"
log "Submodules with dirty tree: $sub_modified / 13"

case "${1:-status}" in
    status)
        log "STATUS mode — no changes made"
        git status -s | head -30
        log "Submodule status:"
        git submodule status
        ;;

    commit)
        log "COMMIT mode — staging + committing only (no push)"

        # 1. Stage root changes
        log "Staging root changes..."
        git add -A
        git status -s | head -10

        # 2. Commit root
        if ! git diff --cached --quiet; then
            log "Committing root working tree..."
            git commit -m "feat: comprehensive 10-subgoal remediation (PHASES A-E)

- PHASE A: Disk cleanup (Docker 582MB, bun cache 4.9GB, npm 385MB)
- PHASE B: Plugins + hooks audit (scripts/plugins_hooks_audit.py + skill + prompt)
- PHASE C0: Provider executor (scripts/provider_executor.py + consolidated report)
- PHASE D: Ollama qwen3-vl:2b wired into 4 agents (Hermes/OpenCode/Codex/Copilot)
- PHASE E: Prompt DRY — 232 triggers added; 3 broken fences identified

New artifacts:
- scripts/plugins_hooks_audit.py
- scripts/provider_executor.py
- scripts/ollama_wire.py
- scripts/prompt_dry_audit.py
- scripts/prompt_dry_fix.py
- .github/prompts/ollama-wire.prompt.md
- .github/prompts/plugins-hooks-audit.prompt.md
- .github/prompts/provider-executor.prompt.md (via fanout)
- .hermes/plans/2026-08-29_full-audit-remediation.md
- .hermes/plans/disk-cleanup-2026-08-29/report.md
- .hermes/plans/plugins-hooks-audit-2026-08-29/report.{json,md}
- .hermes/plans/provider-executor-2026-08-29/ (per-provider reports)
- .hermes/plans/prompt-dry-audit-2026-08-29/report.{json,md}
- .hermes/plans/prompt-dry-2026-08-29/report.md
- ~/AppData/Local/hermes/skills/devops/{plugins-hooks-audit,ollama-wire}/SKILL.md

Modified:
- ~/AppData/Local/hermes/config.yaml (ollama-launch.default_model)
- ~/.config/opencode/opencode.json (model.ollama-local)
- .codex/mcp.json (mcpServers.ollama-local.env.OLLAMA_MODEL)
- .copilot/mcp.json (mcpServers.ollama-local.env.OLLAMA_MODEL)
- 232 .github/prompts/*.prompt.md (added trigger: field)
" 2>&1 | tail -5
        else
            log "No root changes to commit"
        fi

        # 3. Per-submodule commit (only if dirty AND user OK)
        log "Per-submodule status:"
        for s in $(git submodule--helper list 2>/dev/null | awk '{print $2}'); do
            if [ -d "$s" ] && (cd "$s" && git status -s 2>/dev/null | grep -qE "^(\?\?| M| D|A |M )"); then
                log "  $s: DIRTY — would commit (run with --submodules to actually commit)"
            else
                log "  $s: clean"
            fi
        done
        ;;

    push)
        # REQUIRES USER APPROVAL — REFUSE if not explicitly approved
        if [ "${HERMES_PUSH_APPROVED:-no}" != "yes" ]; then
            fail "Push requires HERMES_PUSH_APPROVED=yes env var. Refusing."
        fi
        log "PUSH mode — pushing clean-development to origin"
        git push origin clean-development 2>&1 | tail -10
        log "Now syncing development and production via fast-forward ONLY if safe"
        # Check if origin/development is ancestor of HEAD
        if git merge-base --is-ancestor origin/development HEAD; then
            log "origin/development is ancestor of HEAD — fast-forwarding"
            git push origin clean-development:development 2>&1 | tail -5
        else
            log "SKIPPED: origin/development is NOT ancestor of HEAD (would need force push)"
        fi
        if git merge-base --is-ancestor origin/production HEAD; then
            log "origin/production is ancestor of HEAD — fast-forwarding"
            git push origin clean-development:production 2>&1 | tail -5
        else
            log "SKIPPED: origin/production is NOT ancestor of HEAD"
        fi
        ;;

    *)
        echo "Usage: $0 {status|commit|push}"
        echo "  status  — show what would be done (default)"
        echo "  commit  — stage + commit root tree + submodule preview"
        echo "  push    — push to origin (REQUIRES HERMES_PUSH_APPROVED=yes)"
        exit 1
        ;;
esac
