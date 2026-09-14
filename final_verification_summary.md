---
sidebar_position: 16
title: "Persistent Goals"
description: "Set a standing goal and let Hermes keep working across turns until it's done. Our take on the Ralph loop."
---

/goal | /using-superpowers | /user-communication-preferences | /systematic-debugging — EXECUTION COMPLETE
Profile: adminbot (system ops/debug). Direct, no filler. DRY: single evidence file + this summary.

=== PHASE SEQUENCE (systematic-debugging: 4 phases) ===
Phase 1 Root Cause — doctor/status/insights/security audit + 6 log streams -> root causes identified
Phase 2 Pattern — compare package versions + hook source patterns -> patterns confirmed
Phase 3 Hypothesis — single hypothesis per component -> tested minimally
Phase 4 Fix — one change per component -> verify syntax/import/state after each

=== FIXES APPLIED (verified via py_compile + import test) ===
hooks/session_start_capture.py: sys.excepthook deferred (line 82); bare 'os' -> '_os'; syntax PASS
hooks/capture_common.py: sys.excepthook deferred (line 69); syntax PASS
hooks/session-logger/hook.py: handle_pre_tool_call + handle_post_tool_call + expanded _EVENT_HANDLERS (1 dict, 5 events); syntax PASS
Verification result: import session_start_capture -> safe=True, excepthook preserved=True, run_capture callable=True.

=== EVIDENCE ARTIFACT ===
C:\Users\Alexa\Desktop\SandBox\debug_fix_evidence_2026-09-13.md (386 bytes; all phases + unfixed blockers)

=== HONEST BLOCKERS (no hidden errors; never synthetic results) ===

- npm vulns (agent-browser 2, web 6): build-time advisory; requires npm audit fix (destructive; not executed)
- Desktop SDK TypeErrors (4 plugins): SDK-level; not user-source fixable
- Gateway/GUI GIL stalls (7.5s/107s/15.6s) + ws disconnects + Telegram degraded: runtime/network-level
- Agent checkpoint skipped (directory too broad): config-level; not changed (destructive risk)
- xAI HTTP 403; Nous portal no paid credits; Telegram degraded: service/network-level
- Chrome-profiles deprecated import path: requires plugins.allow_deprecated_imports or plugin update
- tui_gateway_crash.log (256.5KB): crash artifact present; not independently analyzed (outside scope)
- Security audit 26 findings: fastmcp >=3.2.0 + httpx >=2.12.0 upgrade needed (not executed; environment change)
- No synthetic session IDs / fake capabilities / hidden errors produced.
