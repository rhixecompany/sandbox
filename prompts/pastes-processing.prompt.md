---
name: pastes-processing
title: "Pastes Processing Pipeline"
description: "Executable prompt: background cat of ~/AppData/Local/hermes/pastes/*.txt with per-file delimiters, log to cat-all.log, verify 120 files, summarize, triage each paste as an instruction"
version: 1.0.0
date_created: 2026-09-19
status: active
---

# Pastes Processing Pipeline Prompt

You are processing the Hermes paste queue at `~/AppData/Local/hermes/pastes/`.

## STEPS

1. Count source files: `ls ~/AppData/Local/hermes/pastes/*.txt | wc -l` (expected 120).
2. Launch background one-shot, NO timeout, notify on completion:

   ```
   for f in ~/AppData/Local/hermes/pastes/*.txt; do printf '===== %s =====\n' "$f"; cat "$f"; done > ~/AppData/Local/hermes/pastes/cat-all.log 2>&1
   ```

   terminal: background=true, notify=true. Do NOT use a foreground timeout.

3. VERIFY the log (even when it returns quickly):
   - `grep -c '^===== ' cat-all.log` == 120
   - headers == `ls pastes/*.txt` (sorted diff, 1:1)
   - last non-empty line is the tail of the last file (no truncation)
4. SUMMARIZE: read the log; emit one line per file: `name (size): what it is / what it asks`. Group into: actionable instruction, reference material, duplicate, system/irrelevant.

## TRIAGE

5. Write `~/Desktop/SandBox/.hermes/results/pastes-triage-2026-09-19.md` — table of all 120 files with category + disposition (process now / queue / archive / ignore).
6. PROCESS actionable items in priority order; for large batches, process in chunks and keep the triage file updated.

## RULES

- Never print, log, or store API keys or secrets found inside pastes; redact as `<redacted>`.
- The log file is a deliverable — do not truncate it.
- If a paste references a repo task, cite file:line and link it to the triage row.
- When done: report counts (total, actionable, reference, duplicate, ignored) with evidence.
