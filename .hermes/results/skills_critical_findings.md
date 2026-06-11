# Critical Findings — Skills Audit
Date: 2026-06-11

This document lists CRITICAL findings from the hermes skills audit, grouped by skill. Each entry shows file:line, a snippet, and remediation.

Top offenders:
- unsloth: 27
- lambda-labs: 12
- web-pentest: 9
- here-now: 6
- openclaw-migration: 6
- cli: 5
- fitness-nutrition: 4
- grok: 4
- oss-forensics: 4
- qmd: 4
- canvas: 3
- darwinian-evolver: 3
- fastmcp: 3
- osint-investigation: 3
- stocks: 2
- agentmail: 1
- antigravity-cli: 1
- axolotl: 1
- docker-management: 1
- gitnexus-explorer: 1
- honcho: 1
- modal: 1
- parallel-cli: 1
- pinggy-tunnel: 1
- siyuan: 1
- watchers: 1

## agentmail — 1 critical findings
- Line: 16, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.

## antigravity-cli — 1 critical findings
- Line: 26, File: references\cli-docs.md:9, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.

## axolotl — 1 critical findings
- Line: 33, File: references\other.md:310, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.

## canvas — 3 critical findings
- Line: 85, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 87, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 89, File: scripts\canvas_api.py:19, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).

## darwinian-evolver — 3 critical findings
- Line: 150, File: None, Category: injection
  - Snippet: 
  - Remediation: Review and sanitize; convert to read-only examples or add explicit warnings and approval steps.
- Line: 152, File: scripts\parrot_openrouter.py:39 "key =, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 154, File: templates\custom_problem_template.py:47 "key =, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).

## docker-management — 1 critical findings
- Line: 204, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).

## fastmcp — 3 critical findings
- Line: 267, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 269, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 271, File: templates\api_wrapper.py:13, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).

## fitness-nutrition — 4 critical findings
- Line: 298, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 300, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 302, File: scripts\nutrition_search.py:20 "API_KEY =, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 304, File: scripts\nutrition_search.py:8, Category: obfuscation
  - Snippet: 
  - Remediation: Review and sanitize; convert to read-only examples or add explicit warnings and approval steps.

## gitnexus-explorer — 1 critical findings
- Line: 314, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.

## grok — 4 critical findings
- Line: 348, File: None, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 350, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 352, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 354, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.

## here-now — 6 critical findings
- Line: 376, File: scripts\publish.sh:95, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 384, File: None, Category: privilege_escalation
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 386, File: None, Category: privilege_escalation
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 388, File: None, Category: privilege_escalation
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 390, File: None, Category: privilege_escalation
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 392, File: None, Category: privilege_escalation
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.

## honcho — 1 critical findings
- Line: 403, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.

## cli — 5 critical findings
- Line: 486, File: None, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 488, File: references\authentication.md:6 "curl -fsSL, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 490, File: references\authentication.md:44 "curl -fsSL, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 492, File: references\cli-reference.md:78 "infsh completion bash, Category: destructive
  - Snippet: 
  - Remediation: Review and sanitize; convert to read-only examples or add explicit warnings and approval steps.
- Line: 494, File: references\cli-reference.md:6, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.

## lambda-labs — 12 critical findings
- Line: 530, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 532, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 534, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 536, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 538, File: references\advanced-usage.md:578 "# Update, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 540, File: references\advanced-usage.md:579 "ssh ubuntu@<IP>, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 542, File: references\troubleshooting.md:12 "curl -u, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 544, File: references\troubleshooting.md:50 "curl -u, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 546, File: references\troubleshooting.md:82 "curl -u, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 548, File: references\troubleshooting.md:479 "curl -u, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 550, File: references\troubleshooting.md:102 "# Check, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 552, File: references\troubleshooting.md:103 "cat, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.

## modal — 1 critical findings
- Line: 682, File: references\troubleshooting.md:371 "value =, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).

## openclaw-migration — 6 critical findings
- Line: 737, File: scripts\openclaw_to_hermes.py:1148, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 739, File: scripts\openclaw_to_hermes.py:1335 "# OpenClaw's, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 741, File: scripts\openclaw_to_hermes.py:419, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 743, File: scripts\openclaw_to_hermes.py:420, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 745, File: scripts\openclaw_to_hermes.py:2949 ""- Review, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 747, File: scripts\openclaw_to_hermes.py:3116 "print(", Category: persistence
  - Snippet: print(
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.

## osint-investigation — 3 critical findings
- Line: 784, File: scripts\fetch_courtlistener.py:130, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 786, File: scripts\fetch_opencorporates.py:176, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 788, File: scripts\fetch_senate_ld.py:127, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).

## oss-forensics — 4 critical findings
- Line: 803, File: references\recovery-techniques.md:89 "curl -s, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 805, File: references\recovery-techniques.md:97 "curl -s, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 807, File: references\recovery-techniques.md:130 "curl -s, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 809, File: templates\malicious-package-report.md:17 "-, Category: traversal
  - Snippet: 
  - Remediation: Review and sanitize; convert to read-only examples or add explicit warnings and approval steps.

## parallel-cli — 1 critical findings
- Line: 844, File: None, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.

## pinggy-tunnel — 1 critical findings
- Line: 881, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).

## qmd — 4 critical findings
- Line: 973, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 994, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 996, File: None, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 998, File: None, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.

## siyuan — 1 critical findings
- Line: 1077, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.

## stocks — 2 critical findings
- Line: 1152, File: scripts\stocks_client.py:247, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 1154, File: scripts\stocks_client.py:381, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).

## unsloth — 27 critical findings
- Line: 1189, File: references\llms-full.md:7590, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1191, File: references\llms-full.md:7843, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1193, File: references\llms-full.md:8062, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1195, File: references\llms-full.md:8385, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1197, File: references\llms-full.md:8708, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1199, File: references\llms-full.md:8929, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1201, File: references\llms-full.md:9277, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1204, File: references\llms-full.md:9557, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1206, File: references\llms-full.md:9625, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1208, File: references\llms-full.md:10012, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1210, File: references\llms-full.md:10312, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1212, File: references\llms-full.md:12256, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1214, File: references\llms-full.md:13658, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1216, File: references\llms-full.md:14275, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1218, File: references\llms-full.md:15729, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1220, File: references\llms-txt.md:188, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1222, File: references\llms-txt.md:1263, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1224, File: references\llms-txt.md:3543, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1226, File: references\llms-txt.md:3754, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1228, File: references\llms-txt.md:3975, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1230, File: references\llms-txt.md:4475, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1232, File: references\llms-txt.md:4594, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1234, File: references\llms-txt.md:5291, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1236, File: references\llms-txt.md:5927, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1238, File: references\llms-txt.md:7141, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1240, File: references\llms-txt.md:7814, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.
- Line: 1242, File: references\llms-txt.md:11481, Category: supply_chain
  - Snippet: 
  - Remediation: Remove or gate `curl | sh` install snippets. Prefer pinned artifacts, checksums, or instruct users to review scripts before running. Consider adding a non-executing code block and links to verified package sources.

## watchers — 1 critical findings
- Line: 1978, File: scripts\watch_github.py:118, Category: exfiltration
  - Snippet: 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).

## web-pentest — 9 critical findings
- Line: 1987, File: None, Category: destructive
  - Snippet: 
  - Remediation: Review and sanitize; convert to read-only examples or add explicit warnings and approval steps.
- Line: 1989, File: None, Category: persistence
  - Snippet: 
  - Remediation: Avoid instructions that write SSH keys or modify system configs. Require explicit manual approval and sandbox alternatives; add warnings and non-automated steps.
- Line: 1991, File: references\bypass-techniques.md:44 "- Null byte, Category: traversal
  - Snippet: 
  - Remediation: Review and sanitize; convert to read-only examples or add explicit warnings and approval steps.
- Line: 1993, File: references\bypass-techniques.md:46 "- Absolute path:, Category: traversal
  - Snippet: 
  - Remediation: Review and sanitize; convert to read-only examples or add explicit warnings and approval steps.
- Line: 1995, File: references\bypass-techniques.md:50 "- Try ending the, Category: traversal
  - Snippet: 
  - Remediation: Review and sanitize; convert to read-only examples or add explicit warnings and approval steps.
- Line: 1997, File: references\exploitation-techniques.md:36 "Witness:, Category: traversal
  - Snippet: 
  - Remediation: Review and sanitize; convert to read-only examples or add explicit warnings and approval steps.
- Line: 1999, File: scripts\recon-scan.sh:46, Category: exfiltration
  - Snippet: echo 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 2001, File: scripts\recon-scan.sh:81, Category: exfiltration
  - Snippet: echo 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
- Line: 2003, File: scripts\recon-scan.sh:88, Category: exfiltration
  - Snippet: echo 
  - Remediation: Remove hard-coded secrets and example tokens. Replace with environment variable usage and document secure setup. Mask examples (REDACTED).
