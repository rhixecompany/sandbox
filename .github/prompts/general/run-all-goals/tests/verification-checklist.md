---
name: verification-checklist
description: "Verified gate checklist — tree-primary with cleanup-first phases."
---

- [PASS] tree.prompt.txt verified as PRIMARY source
- [PASS] Input files verified (tree.prompt.txt: 3,020 B; run-all-goals.prompt.md: 10,383 B)
- [PASS] Skills verified (brainstorming SKILL.md confirmed present)
- [PASS] Workspace audit verified (85 skills; 27 SKILL.md)
- [PASS] Cleanup phases verified (Phase 1-2: .enhance/.goals deleted, *.json/*.log/*.txt cleaned)
- [PASS] Config phases verified (Phase 3-4: .editorconfig, package.json, etc.)
- [PASS] mjs->mts conversion verified (Phase 5)
- [PASS] Model tests verified (3 session IDs)
- [PASS] Config/fallback verified
- [PASS] Fix verified (AST PASS)
- [PASS] No secrets; DRY; no `.bak`; profile verified (adminbot + patient-tutor)
- [PASS] tree.prompt.txt referenced as PRIMARY in all artifacts
- [PASS] Agent sync: 5 AI agents identical configs
- [PASS] Cleanup: .enhance, .goals, .hermes_diagnostics removed
- [PASS] Config: package.json, pyrightconfig.json, tsconfig.json, requirements.txt updated
- [PASS] mjs to mts conversion complete
- [PASS] DRI: rules reference shared templates
