# Hermes Hooks + Plugins Repair, Verification, and Maintenance Plan
**Workspace:** `C:\Users\Alexa\Desktop\SandBox` (git repo)  
**Hermes profile:** default  
**Live hooks dir:** `C:\Users\Alexa\AppData\Local\hermes\hooks\`  
**Config:** `C:\Users\Alexa\AppData\Local\hermes\config.yaml`  
**Hook scripts:** `C:\Users\Alexa\AppData\Local\hermes\scripts\`  
**Plugins dir:** `C:\Users\Alexa\AppData\Local\hermes\plugins\`  
**Environment:** Windows 11, MSYS bash available, model `stepfun/step-3.7-flash:free` (nous)  

## Approval Gate Policy
- **No commits** without explicit user approval.
- `session-auto-commit` requires **follow-up approval** before any enable/re-enable.
- All **destructive git actions** must be explicitly approved before execution.
- Commands marked `[APPROVAL REQUIRED]` require verbal/text approval before running.
- PHASE 4+ changes require **gate acknowledgement** before proceeding.

---

## Out of Scope for This Plan
- Safe read-only discovery, drafting, and verification commands may run without gate.
- Anything outside these paths is out of scope unless explicitly approved.

---

## PHASE 0 — Discovery & Baseline Verification
**Approval:** None required for read-only commands.

### 0.1 Inspect live hook source-of-truth
```bash
ls -la /c/Users/Alexa/AppData/Local/hermes/hooks
find /c/Users/Alexa/AppData/Local/hermes/hooks -maxdepth 2 -type f | sort
```

### 0.2 Inspect live hook scripts
```bash
ls -la /c/Users/Alexa/AppData/Local/hermes/scripts
cat /c/Users/Alexa/AppData/Local/hermes/scripts/session-logger
cat /c/Users/Alexa/AppData/Local/hermes/scripts/session-auto-commit
cat /c/Users/Alexa/AppData/Local/hermes/scripts/governance-audit
```

### 0.3 Inspect hook config registration
```bash
sed -n '591,601p' "/c/Users/Alexa/AppData/Local/hermes/config.yaml"
```

### 0.4 Inspect plugins directory
```bash
find /c/Users/Alexa/AppData/Local/hermes/plugins -maxdepth 2 -type f | sort
```

### 0.5 Inspect latest hook/governance logs
```bash
ls -lt /c/Users/Alexa/AppData/Local/hermes/logs/sessions | head -20
ls -lt /c/Users/Alexa/AppData/Local/hermes/logs/hermes/governance | head -20
tail -n 20 /c/Users/Alexa/AppData/Local/hermes/logs/governance/audit.log 2>/dev/null || true
tail -n 20 /c/Users/Alexa/AppData/Local/hermes/logs/errors.log 2>/dev/null || true
tail -n 20 /c/Users/Alexa/AppData/Local/hermes/logs/desktop.log 2>/dev/null || true
```

### 0.6 Verify dump file integrity in SandBox
```bash
cd /c/Users/Alexa/Desktop/SandBox && git status --short
python -c "import json,sys; [json.load(open(p)) for p in ['analysis_slice1.json','benchmark_results.json','_audit_prompts.json','_pending_skills_report.json','skill_name_to_path.json']]" && echo JSON_OK
```

### 0.7 Baseline git state
```bash
cd /c/Users/Alexa/Desktop/SandBox && git status -sb && git rev-parse HEAD
```

**Verification gate:** Document current branching state, dirty files, and hook registration before any edits. If hooks run already without creating mission-critical output, note that as stable.

---

## PHASE 1 — Repair Hook Contracts & Log Artifacts
**Approval:** None required for non-destructive repair scripts; required for deleting/moving legacy artifacts in `hooks/` directories.

### 1.1 Validate canonical event names in `hooks.json`
```bash
for f in $(find /c/Users/Alexa/AppData/Local/hermes/hooks -name hooks.json); do
  echo "=== $f ==="; cat "$f"
done
```
- Expected canonical events: `on_session_start`, `on_session_end`, `pre_llm_call`.
- If legacy alias is still used as primary, flag for gate.

### 1.2 Validate each `hook.py` imports canonical `lib.py`
```bash
grep -R "lib.py\|read_payload\|write_jsonl\|skip_context\|is_skipped" /c/Users/Alexa/AppData/Local/hermes/hooks -n
```

### 1.3 Remediation: non-destructive
```bash
# Example: if a hook lacks lib.py imports, patch it
python - <<'PY'
from pathlib import Path
p = Path('/c/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.py')
text = p.read_text()
if 'C:/Users/Alexa/AppData/Local/hermes/hooks/lib.py' not in text:
    # !! This is illustrative; actual manual review is required
    pass
PY
```

**Approval Gate 1:** "Proceed with correcting `hooks.json`/`hook.py` events/imports as identified?"

---

## PHASE 2 — Repair Plugin & Script Artifacts
**Approval:** Required for any workspace-side edits or deletions.

### 2.1 Audit plugin manifest / activity
```bash
find /c/Users/Alexa/AppData/Local/hermes/plugins -maxdepth 2 -type f \( -name README.md -o -name package.json -o -name install.sh -o -name install.ps1 \) -print | xargs -I{} sh -c 'echo === {} ===; stat -c "%y %n" {} 2>/dev/null || stat {}'
```

### 2.2 Repair broken readable manifests in SandBox
- Identify plugin/workspace JSON/YAML files that are malformed.
- Repair in place using `patch` after review.

### 2.3 Move/copy non-repo artifacts out of workspace hooks folder
- SandBox contains a `.github/scripts/` mirror of Hermes helper scripts. If these conflict with the live `C:/Users/Alexa/AppData/Local/hermes/scripts/`, separate them.

**Approval Gate 2:** "Approve moving/renaming workspace files as listed?"

---

## PHASE 3 — Verify Live Hook Execution
**Approval:** None for non-destructive tests; required before mutating any git state or repo state.

### 3.1 Smoke test each canonical event
```bash
echo '{}' | bash /c/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh
echo '{"event":"on_session_end","session_id":"test-end"}' | bash /c/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/hook.sh
echo '{}' | bash /c/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh
```

### 3.2 Verify log entries created
```bash
tail -n 20 /c/Users/Alexa/AppData/Local/hermes/logs/sessions/sessions.log 2>/dev/null || true
tail -n 20 /c/Users/Alexa/AppData/Local/hermes/logs/hermes/governance/audit.log 2>/dev/null || true
find /c/Users/Alexa/AppData/Local/hermes/logs/hermes -maxdepth 2 -type f -newer /c/Users/Alexa/AppData/Local/hermes/logs/hermes/session_meta.json
```

### 3.3 Verify SKIP flags work
```bash
SKIP_session_logger=true echo '{}' | bash /c/Users/Alexa/AppData/Local/hermes/hooks/session-logger/hook.sh
SKIP_SESSION_AUTO_COMMIT=true echo '{"event":"on_session_end","session_id":"test-end"}' | bash /c/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/hook.sh
SKIP_GOVERNANCE_AUDIT=true echo '{}' | bash /c/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/hook.sh
```
- After each, confirm no new JSONL record was appended.

### 3.4 Legacy alias regression test
```bash
echo '{}' | bash /c/Users/Alexa/AppData/Local/hermes/hooks/session-logger/log-session-start.sh
echo '{"event":"on_session_end","session_id":"test-end"}' | bash /c/Users/Alexa/AppData/Local/hermes/hooks/session-auto-commit/auto-commit.sh
echo '{}' | bash /c/Users/Alexa/AppData/Local/hermes/hooks/governance-audit/audit-prompt.sh
```
- Confirm JSONL in canonical log dirs only.

### 3.5 Windows consent / allowlist validation
- If hook commands fail with consent/permission errors, note exact string for `config.yaml` allowlist update.

**Approval Gate 3:** "Profiles and permissions verified; proceed to config mutations?"

---

## PHASE 4 — Repair Config Registration & Repo Artifacts
**Approval:** Required for any edit to `config.yaml` and any state-changing repo modification.

### 4.1 Diff of `config.yaml` from backup
```bash
diff -u /c/Users/Alexa/AppData/Local/hermes/config.yaml.bak.20260710_145115 /c/Users/Alexa/AppData/Local/hermes/config.yaml
```

### 4.2 Patch `config.yaml` if needed
- Ensure `hooks:` entries use canonical bash scripts.
- Ensure `on_session_end` ordering is: session-logger → session-auto-commit → governance-audit.
- Ensure `hooks_auto_accept: false` remains.

**Approval Gate 4:** "Approve proposed config.yaml edits?"

### 4.3 SandBox workspace health
```bash
cd /c/Users/Alexa/Desktop/SandBox && git status -sb
# list broken symlinks or missing tracks
find . -xtype l 2>/dev/null
```

### 4.4 Validate repo JSON/YAML docs integrity
```bash
python - <<'PY'
import json, pathlib
cands = [
 pathlib.Path('/c/Users/Alexa/Desktop/SandBox/analysis_slice1.json'),
 pathlib.Path('/c/Users/Alexa/Desktop/SandBox/benchmark_results.json'),
 pathlib.Path('/c/Users/Alexa/Desktop/SandBox/_audit_prompts.json'),
 pathlib.Path('/c/Users/Alexa/Desktop/SandBox/_pending_skills_report.json'),
 pathlib.Path('/c/Users/Alexa/Desktop/SandBox/skill_name_to_path.json'),
]
for p in cands:
    json.load(open(p, 'rb'))
    print('OK', p)
PY
```

### 4.5 Repair aligned script docs
- Update `README.md` files in each hook directory to reflect canonical events and log paths.

---

## PHASE 5 — Maintain: Drift Prevention & Health Checks
**Approval:** None for read-only checks; required for automation/cron additions.

### 5.1 Establish periodic hook verification command
```bash
/c/Users/Alexa/AppData/Local/hermes/scripts/hook-health-check.sh 2>/dev/null || \
/c/Users/Alexa/Desktop/SandBox/.github/scripts/hook-health-check.sh 2>/dev/null || echo 'NO_HEALTH_SCRIPT'
```

### 5.2 Establish periodic JSONL log rotation / health check
```bash
python - <<'PY'
from pathlib import Path
for p in [
 Path('/c/Users/Alexa/AppData/Local/hermes/logs/sessions'),
 Path('/c/Users/Alexa/AppData/Local/hermes/logs/hermes/governance'),
 Path('/c/Users/Alexa/AppData/Local/hermes/logs/audit'),
]:
    print(p, sum(1 for _ in p.glob('*.jsonl')))
PY
```

### 5.3 Cron/hook allowlist maintenance
- If new hooks are added or event names change, update `config.yaml` allowlist accordingly.

### 5.4 Git hygiene for SandBox artifacts
```bash
cd /c/Users/Alexa/Desktop/SandBox \
  && git add -A \
  && git status -sb
```

**Approval Gate 5:** "Contents to stage look correct — proceed with commit?"  
- Only run `git commit` after explicit approval.

---

## Destructive & Git Command Approval Matrix
| Command / Action | Requires Explicit Approval |
|---|---|
| `git commit` | Always |
| `git push` | Always |
| `git rm` / deleting workspace files | Always |
| Enabling `session-auto-commit` in `config.yaml` | Follow-up approval required |
| Any write to `config.yaml` | Gate 4 |
| Any hook `.py` / `.sh` edit | Gate 1 + Gate 4 if config changes |
| `git stash --include-untracked` | Recommended approval |
| `git clean -fdx` | Never run without explicit text approval |

---

## Recommended Execution Order
1. Run **PHASE 0** immediately; deliver findings + diff reports.
2. Request **Gate 1** only if repairs are needed in `C:/Users/Alexa/AppData/Local/hermes/hooks/`.
3. After repair, run **PHASE 3** tests.
4. Request **Gate 4** only before `config.yaml` changes.
5. Run **PHASE 5** automation setup.

---

## Success Criteria
- All three hooks fire for `on_session_start`, `on_session_end`, `pre_llm_call`.
- Skip flags suppress hook output exactly.
- Legacy aliases produce canonical JSONL only.
- `config.yaml` registration matches live scripts.
- SandBox repo JSON docs pass validation.
- No unapproved git commits or destructive actions performed.
