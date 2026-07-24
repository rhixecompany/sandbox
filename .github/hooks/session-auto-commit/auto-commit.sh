#!/usr/bin/env bash
# session-auto-commit: auto-commit.sh
# Legacy script mapped to canonical on_session_end event.
set -euo pipefail

HOOK_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &>/dev/null && pwd -W )"
HOOK_DIR="${HOOK_DIR//\\//}"
readonly LIB_DIR="${HOOK_DIR}/../lib.sh"
source "${LIB_DIR}"

payload=$(cat)
session_id=$(echo "$payload" | jq -r '.session_id // "unknown"')
working_dir=$(echo "$payload" | jq -r '.working_dir // ""')

if [[ -n "${working_dir}" ]]; then
    repo_root="${working_dir}"
elif [[ -d "C:/Users/Alexa/Desktop/SandBox/.git" ]]; then
    repo_root="C:/Users/Alexa/Desktop/SandBox"
elif [[ -d "${HOME}/.hermes/.git" ]]; then
    repo_root="${HOME}/.hermes"
else
    log_info "No git repository found for auto-commit; skipping"
    exit 0
fi

cd "${repo_root}"
if git diff --quiet && git diff --cached --quiet && [[ $(git status --porcelain | grep '^??' | wc -l) -eq 0 ]]; then
    log_info "No changes to commit for session ${session_id}"
    exit 0
fi

git add -A
timestamp=$(date -u +"%Y-%m-%dT%H:%M:%SZ")
commit_msg="chore(session): auto-commit session ${session_id} at ${timestamp}"
git commit -m "${commit_msg}" || {
    log_error "Auto-commit failed for session ${session_id}"
    exit 1
}
log_info "Auto-committed session ${session_id}: ${commit_msg}"
