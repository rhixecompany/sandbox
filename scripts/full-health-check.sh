#!/usr/bin/env bash
# Comprehensive Hermes Profile Health Check
# Verifies: hooks, plugins, skills, config, MCP

PASS=0
FAIL=0
WARN=0

header() { echo -e "\n=== $1 ==="; }
check() {
    local name="$1"
    local cmd="$2"
    local expected="${3:-}"
    
    echo -n "  $name ... "
    if output=$(eval "$cmd" 2>&1); then
        echo "PASS"
        ((PASS++))
    else
        echo "FAIL (output: $output)"
        ((FAIL++))
    fi
}

warn() {
    local name="$1"
    local msg="$2"
    echo "  WARN: $name - $msg"
    ((WARN++))
}

# --- Hook Tests ---
header "Hooks"

unset SKIP_LOGGING SKIP_AUTO_COMMIT SKIP_GOVERNANCE_AUDIT

check "session-logger syntax" "bash -n .github/hooks/session-logger/hook.sh"
check "session-auto-commit syntax" "bash -n .github/hooks/session-auto-commit/hook.sh"
check "governance-audit syntax" "bash -n .github/hooks/governance-audit/hook.sh"

check "session-logger sessionStart" 'echo "{\"event\": \"sessionStart\", \"session_id\": \"health\"}" | .github/hooks/session-logger/hook.sh | grep -q "\"status\": \"ok\""'
check "session-logger pre_llm_call" 'echo "{\"event\": \"pre_llm_call\", \"session_id\": \"health\", \"user_message\": \"test\"}" | .github/hooks/session-logger/hook.sh | grep -q "\"status\": \"ok\""'
check "session-logger skip flag" 'export SKIP_LOGGING=true && echo "{\"event\": \"sessionStart\", \"session_id\": \"health\"}" | .github/hooks/session-logger/hook.sh | grep -q "\"status\": \"skipped\""'

check "session-auto-commit sessionEnd" 'echo "{\"event\": \"sessionEnd\", \"session_id\": \"health\"}" | .github/hooks/session-auto-commit/hook.sh | grep -q "status"'
check "session-auto-commit skip flag" 'export SKIP_AUTO_COMMIT=true && echo "{\"event\": \"sessionEnd\", \"session_id\": \"health\"}" | .github/hooks/session-auto-commit/hook.sh | grep -q "\"status\": \"skipped\""'

check "governance-audit pre_llm_call" 'echo "{\"event\": \"pre_llm_call\", \"session_id\": \"health\", \"user_message\": \"hello\"}" | .github/hooks/governance-audit/hook.sh | grep -q "\"status\": \"ok\""'
check "governance-audit threat detection" 'echo "{\"event\": \"pre_llm_call\", \"session_id\": \"health\", \"user_message\": \"ignore previous\"}" | .github/hooks/governance-audit/hook.sh 2>&1 | grep -q "threat-detected"'
check "governance-audit skip flag" 'export SKIP_GOVERNANCE_AUDIT=true && echo "{\"event\": \"pre_llm_call\", \"session_id\": \"health\", \"user_message\": \"test\"}" | .github/hooks/governance-audit/hook.sh | grep -q "\"status\": \"skipped\""'

unset SKIP_LOGGING SKIP_AUTO_COMMIT SKIP_GOVERNANCE_AUDIT

# --- Config.yaml Hook Registration ---
header "Config.yaml Hook Registration"
check "session-logger registered" "grep -q 'session-logger:' ~/AppData/Local/hermes/config.yaml"
check "session-auto-commit registered" "grep -q 'session-auto-commit:' ~/AppData/Local/hermes/config.yaml"
check "governance-audit registered" "grep -q 'governance-audit:' ~/AppData/Local/hermes/config.yaml"

# --- Plugin Tests ---
header "Plugins"
check "disk-cleanup enabled" "hermes plugins list 2>&1 | grep -q 'disk-cleanup.*enabled'"
check "openrouter-provider enabled" "hermes plugins list 2>&1 | grep -q 'openrouter-provider.*enabled'"
check "security-guidance enabled" "hermes plugins list 2>&1 | grep -q 'security-guidance.*enabled'"

# --- Skill Tests ---
header "Skills"
SKILL_COUNT=$(hermes skills list 2>&1 | grep -c 'enabled')
echo "  Total enabled skills: $SKILL_COUNT"
if [[ $SKILL_COUNT -gt 300 ]]; then
    echo "  Skill count > 300 ... PASS"
    ((PASS++))
else
    echo "  Skill count > 300 ... FAIL (got $SKILL_COUNT)"
    ((FAIL++))
fi

check "plan skill" "hermes skills list 2>&1 | grep -q 'plan.*enabled'"
check "github-pr-workflow skill" "hermes skills list 2>&1 | grep -q 'github-pr-workflow.*enabled'"
check "kanban-orchestrator skill" "hermes skills list 2>&1 | grep -q 'kanban-orchestrator.*enabled'"
check "hermes-agent-skill-authoring skill" "hermes skills list 2>&1 | grep -q 'hermes-agent-skill-authoring.*enabled'"
check "subagent-driven-development skill" "hermes skills list 2>&1 | grep -q 'subagent-driven-dev.*enabled'"
check "test-driven-development skill" "hermes skills list 2>&1 | grep -q 'test-driven-develop.*enabled'"
check "systematic-debugging skill" "hermes skills list 2>&1 | grep -q 'systematic-debugging.*enabled'"
check "requesting-code-review skill" "hermes skills list 2>&1 | grep -q 'requesting-code-review.*enabled'"

# Verify skill directories match SKILL.md name
header "Skill Integrity"
MISMATCH=0
for skill in $(ls ~/AppData/Local/hermes/skills/ 2>/dev/null); do
    if [[ -f ~/AppData/Local/hermes/skills/$skill/SKILL.md ]]; then
        name=$(grep -E '^name:' ~/AppData/Local/hermes/skills/$skill/SKILL.md | head -1 | sed 's/name: *//')
        if [[ "$name" != "$skill" ]]; then
            echo "  MISMATCH: dir=$skill, SKILL.md name=$name"
            ((MISMATCH++))
        fi
    fi
done
if [[ $MISMATCH -eq 0 ]]; then
    echo "  All skill dirs match SKILL.md names ... PASS"
    ((PASS++))
else
    echo "  Skill dir/name mismatches: $MISMATCH ... FAIL"
    ((FAIL++))
fi

# --- MCP Tests ---
header "MCP"
check "mcp-docker configured" "grep -q 'mcp-docker' ~/AppData/Local/hermes/config.yaml"
check "filesystem MCP configured" "grep -q 'filesystem' ~/AppData/Local/hermes/config.yaml"
check "fetch MCP configured" "grep -q 'fetch' ~/AppData/Local/hermes/config.yaml"
check "memory MCP configured" "grep -q 'memory' ~/AppData/Local/hermes/config.yaml"

# --- Backup Verification ---
header "Backup"
check "backup.hermes exists" "test -d backup.hermes/2026-06-11_173000"
check "backup manifest exists" "test -f backup.hermes/2026-06-11_173000/manifest.json"
check "backup has hooks" "test -d backup.hermes/2026-06-11_173000/hooks"
check "backup has skills" "test -d backup.hermes/2026-06-11_173000/skills"
check "backup has config.yaml" "test -f backup.hermes/2026-06-11_173000/config.yaml"

# --- Summary ---
header "Summary"
echo "  Passed: $PASS"
echo "  Failed: $FAIL"
echo "  Warnings: $WARN"

if [[ $FAIL -gt 0 ]]; then
    echo ""
    echo "HEALTH CHECK: FAILED"
    exit 1
else
    echo ""
    echo "HEALTH CHECK: PASSED"
    exit 0
fi