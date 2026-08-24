# Implementation Plan: Next Steps Execution

**Created:** 2026-08-25T00:02:46.462520
**Goal:** Execute remaining Next Steps per specs in `.hermes/plans/next-steps-specs.md`

---

## Phase 1: GitHub Authentication Setup (SPEC-001) — P0

### Tasks:
1. **Check current Git remote URL and auth method**
   - Command: `git remote -v`
   - Verify HTTPS vs SSH

2. **Generate SSH key (if not exists)**
   - Command: `ls -la ~/.ssh/id_ed25519*`
   - If missing: `ssh-keygen -t ed25519 -C "alexa@rhixecompany.com"`

3. **Add SSH key to ssh-agent**
   - Command: `eval $(ssh-agent -s) && ssh-add ~/.ssh/id_ed25519`

4. **Add SSH public key to GitHub**
   - Command: `cat ~/.ssh/id_ed25519.pub`
   - Manual step: Add to GitHub Settings → SSH and GPG keys

5. **Verify SSH connection**
   - Command: `ssh -T git@github.com`

6. **Change remote to SSH**
   - Command: `git remote set-url origin git@github.com:rhixecompany/sandbox.git`

7. **Push commits and tags**
   - Command: `git push origin clean-development`
   - Command: `git push origin --tags`

### Verification:
- [ ] `git push origin clean-development` succeeds
- [ ] `git push origin --tags` succeeds  
- [ ] Tag `profile-sync-2026-08-24` visible on GitHub

---

## Phase 2: Multi-Agent Sync Parity Verification (SPEC-002) — P1

### Tasks:
1. **Locate verify_sync.py**
   - Check: `~/Desktop/SandBox/hermes-profiles/verify_sync.py`
   - If missing, check Hermes profiles directory

2. **Run verification**
   - Command: `cd ~/Desktop/SandBox/hermes-profiles && python verify_sync.py`
   - Or: `hermes skills run multi-agent-sync` if available

3. **Analyze results**
   - Check all 65 checks pass
   - Document any failures

### Verification:
- [ ] 65 checks pass
- [ ] No parity failures between Hermes, Codex, OpenCode

---

## Phase 3: Test Providers Models Live Probe (SPEC-003) — P0

### Tasks:
1. **Execute test-providers-models prompt**
   - Command: `hermes chat --prompt test-providers-models`
   - Or run via prompt trigger: `/test-providers-models`

2. **Monitor subagent delegation**
   - Subagent A: opencode-zen, openrouter, deepseek
   - Subagent B: gemini, ollama-cloud, nous, huggingface
   - Subagent C: openai-codex, copilot, xai-oauth, xai

3. **Verify probe results**
   - Check structured capability output
   - Confirm working models only in fallback chain

4. **Update Hermes config**
   - Primary model = highest-ranked verified working model
   - Fallback chain ordered by capability
   - Each provider's default_model set

5. **Propagate to agents**
   - Update profile SOUL.md/USER.md/MEMORY.md
   - Update workspace context files
   - Update OpenCode/Codex/VS Code configs

### Verification:
- [ ] All authorized providers probed
- [ ] Only verified working models in fallback chain
- [ ] Hermes config updated
- [ ] Agent configs propagated

---

## Execution Order

1. Phase 1 (GitHub Auth) — Blocks push of completed work
2. Phase 3 (Live Probe) — Updates model configs  
3. Phase 2 (Sync Verify) — Validates parity after config updates

---

## Resource Allocation

| Resource | Phase 1 | Phase 2 | Phase 3 |
|----------|---------|---------|---------|
| Primary Agent | ✅ | ✅ | ✅ |
| Subagents | — | — | 3 parallel |
| Human (Alexa) | SSH key approval | Review results | Review probe results |

---

## Success Criteria

- [ ] GitHub push succeeds (no 403)
- [ ] 65/65 multi-agent sync checks pass
- [ ] Live probe produces verified fallback chain
- [ ] All agents use verified working models only
- [ ] No secrets/tokens in any output
