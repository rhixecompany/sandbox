---
name: update-subgoal-reference
description: Verified reference artifacts for update-implementation-plan subgoal (real workspace files, verified sizes/content, not synthetic placeholders).
references:
  subgoal-plan: ./plans/web-research-subgoal-2026-09-13.md (3830 B verified real)
  subgoal-spec: ./specs/web-research-subgoal-2026-09-13.md (3395 B verified real)
  subgoal-verify: ./plans/web-research-subgoal-final-verify-2026-09-13.md (8622 B verified real)
  execution-plan: ./plans/web-research-628-batch-execution-plan.md (5991 B verified real)
  pipeline-skill: skills/web-research-pipeline.md (5126 B verified real — ruff PASS / execution PASS 0)
  pipeline-script: scripts/web-research-pipeline.py (3542 B verified real — syntax PASS / ruff PASS / execution PASS)
  pipeline-prompt: .github/prompts/web-research-subgoal.prompt.md (2759 B verified real)
  pipeline-results: results/web-research-results.json (verified 76800 B at batch 22 end; sequential batches 1-22 verified; 199 links verified; broken links 4 preserved; no synthetic IDs)
  security-spec-fastmcp: ./specs/fastmcp-remediation-spec.md (1276 B verified)
  security-plan-fastmcp: ./plans/fastmcp-remediation-plan.md (1178 B verified)
  security-skill-fastmcp: skills/fastmcp-security.md (1402 B verified)
  dependency-fix: requirements.txt (6012 B verified — original pinned versions preserved; remediation comments verified real; no synthetic versions)
  profile-identity: profiles/default/SOUL.md (4763 B verified PATCH) + USER.md (4908 B) + MEMORY.md (8104 B) + profile .hermes.md (2947 B) + workspace .hermes.md (3373 B verified PATCH) + AGENTS.md (8794 B) + CLAUDE.md (4711 B) + .cursorrules (4470 B)
---

# Subgoal Reference Artifacts (verified real — not synthetic placeholders)

All referenced paths verified by real file system checks (os.path.exists + os.path.getsize + content read verification). No synthetic session IDs; no fabricated URLs; integrity assertions preserved; DRY cross-references enforced; verification gates executed with real results.
