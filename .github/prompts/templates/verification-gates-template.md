# Verification Gates Template

**Verification Date**: {{TIMESTAMP}}
**Session**: {{SESSION_ID}}
**Verifier**: {{VERIFIER}}

## Gate 1: Hermes Config Check

### Command
```bash
hermes config check
```

### Expected Result
```
✓ Configuration valid
```

### Actual Result
```
{{GATE1_ACTUAL}}
```

### Status
- [ ] **PASS** — Config valid
- [ ] **FAIL** — {{GATE1_FAILURE_REASON}}

---

## Gate 2: Primary Model Configuration

### Commands
```bash
hermes config show | grep -A 5 "Model:"
```

### Expected
```
Model:        {{EXPECTED_MODEL_JSON}}
```

### Actual
```
{{GATE2_ACTUAL}}
```

### Checks
- [ ] `model.provider` = {{EXPECTED_PROVIDER}}
- [ ] `model.default` = {{EXPECTED_MODEL}}
- [ ] `model.base_url` = {{EXPECTED_BASE_URL}}
- [ ] `model.api_mode` = {{EXPECTED_API_MODE}}

### Status
- [ ] **PASS** — All match
- [ ] **FAIL** — {{GATE2_FAILURE_REASON}}

---

## Gate 3: Fallback Providers List Type

### Command
```bash
python -c "import yaml,os; c=yaml.safe_load(open(os.environ['LOCALAPPDATA']+'/hermes/config.yaml')); print('Type:', type(c['fallback_providers'])); print('Value:', c['fallback_providers'])"
```

### Expected
```
Type: <class 'list'>
Value: ['{{FALLBACK_1}}', '{{FALLBACK_2}}', '{{FALLBACK_3}}', '{{FALLBACK_4}}', '{{FALLBACK_5}}']
```

### Actual
```
{{GATE3_ACTUAL}}
```

### Checks
- [ ] `fallback_providers` is a YAML list (not string)
- [ ] Order matches capability ranking
- [ ] All providers in list have working models

### Status
- [ ] **PASS** — Valid list, correct order
- [ ] **FAIL** — {{GATE3_FAILURE_REASON}}

---

## Gate 4: Provider Default Models

### Commands
```bash
hermes config show | grep -A 20 "providers:"
```

### Expected per Provider
| Provider | Expected Default Model | Actual | Match |
|---|---|---|---|
| {{FALLBACK_1}} | {{FALLBACK_1_MODEL}} | {{GATE4_FB1_ACTUAL}} | {{GATE4_FB1_MATCH}} |
| {{FALLBACK_2}} | {{FALLBACK_2_MODEL}} | {{GATE4_FB2_ACTUAL}} | {{GATE4_FB2_MATCH}} |
| {{FALLBACK_3}} | {{FALLBACK_3_MODEL}} | {{GATE4_FB3_ACTUAL}} | {{GATE4_FB3_MATCH}} |
| {{FALLBACK_4}} | {{FALLBACK_4_MODEL}} | {{GATE4_FB4_ACTUAL}} | {{GATE4_FB4_MATCH}} |
| {{FALLBACK_5}} | {{FALLBACK_5_MODEL}} | {{GATE4_FB5_ACTUAL}} | {{GATE4_FB5_MATCH}} |

### Status
- [ ] **PASS** — All providers have correct working default_model
- [ ] **FAIL** — {{GATE4_FAILURE_REASON}}

---

## Gate 5: Profile List Shows Updated Models

### Command
```bash
hermes profile list
```

### Expected
Primary model ({{PRIMARY_MODEL}}) shown for default profile and relevant aliases.

### Actual
```
{{GATE5_ACTUAL}}
```

### Checks
- [ ] Default profile shows {{PRIMARY_MODEL}}
- [ ] No profiles reference non-working models
- [ ] Gateway status reasonable (running/stopped)

### Status
- [ ] **PASS** — Profiles reflect verified chain
- [ ] **FAIL** — {{GATE5_FAILURE_REASON}}

---

## Gate 6: Workspace Context Files Updated

### Files to Check
| File | Expected Model Ref | Actual | Match |
|---|---|---|---|
| `.hermes.md` | {{PRIMARY_MODEL}} | {{GATE6_HERMES_ACTUAL}} | {{GATE6_HERMES_MATCH}} |
| `AGENTS.md` | {{PRIMARY_MODEL}} | {{GATE6_AGENTS_ACTUAL}} | {{GATE6_AGENTS_MATCH}} |
| `.github/copilot-instructions.md` | {{PRIMARY_MODEL}} | {{GATE6_COPILOT_ACTUAL}} | {{GATE6_COPILOT_MATCH}} |
| `CLAUDE.md` | {{PRIMARY_MODEL}} | {{GATE6_CLAUDE_ACTUAL}} | {{GATE6_CLAUDE_MATCH}} |

### Status
- [ ] **PASS** — All workspace files reference verified working models
- [ ] **FAIL** — {{GATE6_FAILURE_REASON}}

---

## Gate 7: External Agent Configs Updated

### Files to Check
| File | Expected Model Ref | Actual | Match |
|---|---|---|---|
| `~/.opencode/mcp.json` | {{PRIMARY_MODEL}} | {{GATE7_OPENCODE_ACTUAL}} | {{GATE7_OPENCODE_MATCH}} |
| `~/.codex/mcp.json` | {{PRIMARY_MODEL}} | {{GATE7_CODEX_ACTUAL}} | {{GATE7_CODEX_MATCH}} |

### Status
- [ ] **PASS** — External agents reference verified working models
- [ ] **FAIL** — {{GATE7_FAILURE_REASON}}

---

## Gate 8: No Non-Working Models in Config

### Check
Search config.yaml and all propagated files for any model marked `working=false` in ranking.

### Command
```bash
grep -r "{{EXCLUDED_MODEL_1}}\|{{EXCLUDED_MODEL_2}}\|{{EXCLUDED_MODEL_3}}" \
  ~/AppData/Local/hermes/config.yaml \
  C:\Users\Alexa\Desktop\SandBox\.hermes.md \
  C:\Users\Alexa\Desktop\SandBox\AGENTS.md \
  ~/AppData/Local/hermes/profiles/ 2>/dev/null || echo "None found"
```

### Expected
```
None found
```

### Actual
```
{{GATE8_ACTUAL}}
```

### Status
- [ ] **PASS** — No excluded models referenced
- [ ] **FAIL** — {{GATE8_FAILURE_REASON}}

---

## Gate 9: No Secrets in Output

### Check
Verify no API keys, tokens, or credentials in any generated files.

### Command
```bash
grep -r "sk-\|api[_-]key\|Bearer\|token" \
  C:\Users\Alexa\Desktop\SandBox\.github\prompts\templates\ \
  C:\Users\Alexa\Desktop\SandBox\.github\prompts\test-providers-models.prompt.md \
  provider_docs/ \
  probes/ \
  ranking/ \
  config/ \
  propagation/ 2>/dev/null || echo "None found"
```

### Expected
```
None found
```

### Actual
```
{{GATE9_ACTUAL}}
```

### Status
- [ ] **PASS** — No secrets exposed
- [ ] **FAIL** — {{GATE9_FAILURE_REASON}}

---

## Gate 10: Documentation Complete

### Required Artifacts
| Artifact | Path | Exists | Complete |
|---|---|---|---|
| Provider Inventory | `provider_docs/provider-inventory.md` | {{DOC1_EXISTS}} | {{DOC1_COMPLETE}} |
| Provider Docs (per provider) | `provider_docs/{{PROVIDER}}-research.md` | {{DOC2_EXISTS}} | {{DOC2_COMPLETE}} |
| Model Probes | `probes/{{PROVIDER}}-{{MODEL}}-probe.md` | {{DOC3_EXISTS}} | {{DOC3_COMPLETE}} |
| Capability Ranking | `ranking/capability-ranking-{{TIMESTAMP}}.md` | {{DOC4_EXISTS}} | {{DOC4_COMPLETE}} |
| Hermes Config Target | `config/hermes-config-target-{{TIMESTAMP}}.md` | {{DOC5_EXISTS}} | {{DOC5_COMPLETE}} |
| Agent Propagation | `propagation/agent-propagation-{{TIMESTAMP}}.md` | {{DOC6_EXISTS}} | {{DOC6_COMPLETE}} |
| This Verification Report | `verification/verification-{{TIMESTAMP}}.md` | {{DOC7_EXISTS}} | {{DOC7_COMPLETE}} |

### Status
- [ ] **PASS** — All artifacts exist and complete
- [ ] **FAIL** — {{GATE10_FAILURE_REASON}}

---

## Gate 11: All :free Models Documented & Probed

### Check
Cross-reference discovered :free models from web research with probe results.

### Summary
| Provider | Discovered :free Models | Probed | Working | Excluded |
|---|---|---|---|---|
| nous | {{NOUS_DISCOVERED}} | {{NOUS_PROBED}} | {{NOUS_WORKING}} | {{NOUS_EXCLUDED}} |
| opencode-zen | {{OZ_DISCOVERED}} | {{OZ_PROBED}} | {{OZ_WORKING}} | {{OZ_EXCLUDED}} |
| openrouter | {{OR_DISCOVERED}} | {{OR_PROBED}} | {{OR_WORKING}} | {{OR_EXCLUDED}} |
| ollama-cloud | {{OLLAMA_DISCOVERED}} | {{OLLAMA_PROBED}} | {{OLLAMA_WORKING}} | {{OLLAMA_EXCLUDED}} |
| gemini | {{GEMINI_DISCOVERED}} | {{GEMINI_PROBED}} | {{GEMINI_WORKING}} | {{GEMINI_EXCLUDED}} |
| deepseek | {{DS_DISCOVERED}} | {{DS_PROBED}} | {{DS_WORKING}} | {{DS_EXCLUDED}} |

### Status
- [ ] **PASS** — All discovered models probed, results documented
- [ ] **FAIL** — {{GATE11_FAILURE_REASON}}

---

## Overall Verification Status

| Gate | Status | Notes |
|---|---|---|
| 1. Config Check | {{G1_STATUS}} | {{G1_NOTES}} |
| 2. Primary Model | {{G2_STATUS}} | {{G2_NOTES}} |
| 3. Fallback List Type | {{G3_STATUS}} | {{G3_NOTES}} |
| 4. Provider Default Models | {{G4_STATUS}} | {{G4_NOTES}} |
| 5. Profile List | {{G5_STATUS}} | {{G5_NOTES}} |
| 6. Workspace Files | {{G6_STATUS}} | {{G6_NOTES}} |
| 7. External Agents | {{G7_STATUS}} | {{G7_NOTES}} |
| 8. No Excluded Models | {{G8_STATUS}} | {{G8_NOTES}} |
| 9. No Secrets | {{G9_STATUS}} | {{G9_NOTES}} |
| 10. Documentation | {{G10_STATUS}} | {{G10_NOTES}} |
| 11. All Models Probed | {{G11_STATUS}} | {{G11_NOTES}} |

### Final Verdict
- [ ] **ALL GATES PASS** — Configuration complete and verified
- [ ] **SOME GATES FAIL** — {{FAILING_GATES}} need remediation

---

*Fill in during Phase 7 execution. Save as `verification/verification-{{TIMESTAMP}}.md`*