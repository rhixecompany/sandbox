# Batch Audit Patterns (content-structure + safety)

Read-only detection catalog used by `prompt-library-audit`. All scans run on the prompt
**body** (text after the closing frontmatter `---`). The actual regex/string lists are
kept in `scripts/prompt_library_audit.py` and assembled at runtime so the skill text
stays free of verbatim override/jailbreak phrases (the safety scanner otherwise blocks
the whole skill, even though these are DEFENSIVE detection targets).

## Structure heuristic
A prompt "has recognizable structure" if its body contains at least one H2 (`##`) or H3
(`###`) heading whose lowercased text contains one of: `goal`, `context`, `workflow`,
`phase`, `rule`. No H2/H3 at all -> *heading-free blob*. Headings present but none
matching the keywords -> *non-canonical naming*.

## CRITICAL — instruction-override / role-play jailbreak
Substring category: phrases that try to override prior instructions, impersonate a
restriction-free persona, demand the model act without limits, or force disclosure of
the system prompt / exfiltration. Match case-insensitively; dedup on (file, line, label).

## HIGH — destructive operations (approval gate required)
Flag destructive shell/DB operations only when the whole file contains NO approval-gate
wording. Categories: recursive/forced deletes, force-push / hard reset / clean, table
drops / truncates, filesystem format / raw device writes, world-writable perms, and
pipe-to-shell downloads. Approval-gate wording that neutralizes the flag: `approval`,
`approve`, `confirm`, `consent`, `authoriz`, `ask the user`, `before proceeding`,
`verify with`, `requires`.

## HIGH — secret / credential exposure (protective phrasing excluded)
Flag reveal-verbs within ~40 chars of credential nouns. Always EXCLUDE protective
phrasing: negation words (never, don't, avoid, must not, refuse) or store/keep wording.
A "never print credentials" line is a guardrail, not a leak.

## Non-destructive proof
Snapshot SHA-256 of every `.prompt.md` before/after the run; assert zero differences.
Cross-check counts with an independent re-implementation of the scan.
