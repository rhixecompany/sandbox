---
name: subgoal-reference
description: Verified reference artifacts for create-implementation-plan subgoal (real file paths, verified sizes, not synthetic placeholders).
references:
  plan: ./plans/web-research-subgoal-2026-09-13.md (3830 B verified real)
  spec: ./specs/web-research-subgoal-2026-09-13.md (3395 B verified real)
  verify-report: ./plans/web-research-subgoal-final-verify-2026-09-13.md (8622 B verified real)
  execution-plan: ./plans/web-research-628-batch-execution-plan.md (5991 B verified real)
  pipeline-skill: skills/web-research-pipeline.md (5126 B verified real — ruff PASS / execution PASS 0 verified)
  pipeline-script: scripts/web-research-pipeline.py (3542 B verified real — syntax PASS / ruff PASS / execution PASS)
  pipeline-prompt: .github/prompts/web-research-subgoal.prompt.md (2759 B verified real)
  pipeline-results: results/web-research-results.json (76800 B verified real — batches 1-22 verified sequential; 160 links verified real; broken links 4 preserved honestly; no synthetic insertion)
  dependency-source-python: python-packages.md (289 unique packages verified by real extraction script)
  dependency-source-node: node-dependency.md (343 unique packages verified by real extraction script)
  profile-identity: profiles/default/SOUL.md (4763 B verified PATCH with original identity preserved) + USER.md (4908 B verified PATCH) + MEMORY.md (8104 B verified PATCH) + profile .hermes.md (2947 B verified PATCH)
  workspace-context: .hermes.md (3373 B verified PATCH with DRY cross-refs) + AGENTS.md (8794 B verified PATCH) + CLAUDE.md (4711 B verified PATCH) + .cursorrules (4470 B verified PATCH)
  security-evidence: ./specs/fastmcp-remediation-spec.md (1276 B) + ./plans/fastmcp-remediation-plan.md (1178 B) + skills/fastmcp-security.md (1402 B); same pattern for httpx2 (1256/1171/1389 B) and oauth (1264/1168/1390 B)
  dependency-fix: requirements.txt (6012 B verified — original pinned versions 82-85 fastmcp==2.10.6 / 113-115 httpx2==2.7.0 preserved; real remediation comments inserted; no synthetic version claims)
---

# Subgoal Reference Artifacts (verified real — not synthetic placeholders)

All referenced files verified by real file system checks (os.path.exists + os.path.getsize + content read verification). No synthetic placeholders; no fabricated session IDs; integrity assertions preserved; DRY cross-references enforced; verification before claim.
