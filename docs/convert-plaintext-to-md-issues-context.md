# convert-plaintext-to-md — Issues Catalog

Generated: 2026-05-25 Audit Phase: 1 (Comprehensive Audit with Issue Detection)

Source file: `.github/prompts/convert-plaintext-to-md.prompt.md`

## Summary

| Category | Count |
| -------- | ----- |
| **Total Issues** | 5 |
| Critical | 1 |
| Major | 3 |
| Minor | 1 |
| **Formatting** | 1 |
| **Content** | 3 |
| **Structural** | 1 |
| **Cross-file** | 0 |

## Issues by Severity

### 🔴 CRITICAL (Breaks Documented Behavior)

#### Issue CNT-001: Parameter Documentation Mismatch (Inputs vs Parameters Table)

**File:** `.github/prompts/convert-plaintext-to-md.prompt.md`

**Lines:** 24, 92-101

**Severity:** Critical

**Category:** Content

**Description:**

The Inputs section (line 24) lists: "Optional parameters (finalize, guide, instructions, platform, pattern, stop)"

However, the Parameters table (lines 92-101) documents 9 parameters:
1. `#file:{{file}}`
2. `finalize`
3. `guide #file:{{reference-file}}`
4. `instructions`
5. `platform={{name}}`
6. `--header [1-4]` ← **MISSING from Inputs list**
7. `-p, --pattern`
8. `-s, --stop <line|eof>`

**Impact:** Users reading the Inputs section will not know about the `--header` parameter, but the Parameters table documents it. This causes documentation inconsistency.

**Evidence:**
```
Inputs section states:
- Optional parameters (finalize, guide, instructions, platform, pattern, stop)

Parameters table includes:
| `--header [1-4]` | No | Add markdown header tags at specified level |
```

**Resolution:** Add `--header` to the Inputs section parameter list on line 24, or remove it from the Parameters table if it's not supported.

---

#### Issue STR-001: Phase 2 Step 3 Incomplete Parameter List

**File:** `.github/prompts/convert-plaintext-to-md.prompt.md`

**Lines:** 69

**Severity:** Critical

**Category:** Structural

**Description:**

Phase 2, Step 3 says: "Apply any passed parameters (finalize, platform, pattern, stop)"

But it is missing:
- `guide` (documented, used in Phase 2 context)
- `instructions` (documented, mentioned in Phase 2 step 4 context)
- `--header` (documented in Parameters table)

**Impact:** Users executing Phase 2 will not know which parameters to apply, as the instruction is incomplete. This breaks the intended execution flow.

**Evidence:**
```
Line 69: 3. Apply any passed parameters (finalize, platform, pattern, stop)
(missing: guide, instructions, --header)
```

**Resolution:** Update line 69 to include all 8 optional parameters:
```
3. Apply any passed parameters (finalize, guide, instructions, platform, --header, pattern, stop)
```

---

### 🟠 MAJOR (Inconsistent or Unclear)

#### Issue CNT-002: Shell Command Syntax Ambiguity in Phase 2 Step 1

**File:** `.github/prompts/convert-plaintext-to-md.prompt.md`

**Lines:** 67

**Severity:** Major

**Category:** Content

**Description:**

Phase 2, Step 1 reads: "If no `{{file}}.md` exists: copy plaintext file to `copy {{file}} {{file}}.md`"

The phrase "copy plaintext file to `copy {{file}} {{file}}.md`" has redundant wording. The word "copy" appears both as the narrative verb ("copy ... to") and within the code snippet. This creates ambiguity:
- Does the user copy the file using the command `cp {{file}} {{file}}.md` or the command `copy {{file}} {{file}}.md`?
- Is "copy" a shell command, Windows command, or pseudocode?

**Impact:** Implementers (both AI and humans) may be confused about the exact operation intended or the syntax to use.

**Evidence:**
```
Line 67: "If no `{{file}}.md` exists: copy plaintext file to `copy {{file}} {{file}}.md`"
                                      ^^^^                    ^^^^
                                    same word repeated — ambiguous
```

**Resolution:** Clarify the intent. Either:
- Option A: "If no `{{file}}.md` exists, create a copy: `cp {{file}} {{file}}.md` (or `copy {{file}} {{file}}.md` on Windows)"
- Option B: "If no `{{file}}.md` exists, duplicate the plaintext file as `{{file}}.md`"

---

#### Issue CNT-003: Rules Section Line 42 vs Phase 2 Step 1 Contradiction

**File:** `.github/prompts/convert-plaintext-to-md.prompt.md`

**Lines:** 42, 67

**Severity:** Major

**Category:** Content

**Description:**

**Rule (line 42):**
"If a corresponding `{{file}}.md` already EXISTS, treat existing content as the plaintext data to be converted"

**Phase 2, Step 1 (line 67):**
"If no `{{file}}.md` exists: copy plaintext file to `copy {{file}} {{file}}.md`"

These two statements together create a logical conflict:
1. Phase 2 Step 1 creates `{{file}}.md` only if it does NOT exist.
2. Rule on line 42 says if `{{file}}.md` DOES exist, treat it as the plaintext source.
3. This implies: if you run the prompt twice on the same file, the behavior changes (first run treats original file as source, second run treats `.md` file as source).

**Question:** Is this intentional or a bug? The current wording suggests the intent is to support idempotent re-runs, but it's not clearly documented that the file can be re-run with different behavior based on whether `.md` exists.

**Impact:** Users expect deterministic behavior but will experience different behavior depending on prior execution state.

**Evidence:**
```
Line 42 (Rule): If .md exists → treat .md as source
Line 67 (Phase 2 Step 1): If .md does NOT exist → create it

Logic flow:
- 1st run: .md doesn't exist → create from plaintext → convert
- 2nd run: .md exists → treat .md as source → convert

This is either intentional idempotency or a bug.
```

**Resolution:** Clarify intent in the Rules section or add a note in Phase 2 explaining this behavior, e.g.:
- "If re-running this prompt: the existing `{{file}}.md` becomes the new source. To re-convert from the original plaintext, delete `{{file}}.md` and re-run."

---

#### Issue FMT-001: Table Alignment & Markdown Syntax in Parameters Table

**File:** `.github/prompts/convert-plaintext-to-md.prompt.md`

**Lines:** 92-101

**Severity:** Minor

**Category:** Formatting

**Description:**

In the Parameters table, several parameter names use shell-style syntax with dashes and pipes, e.g., `-s, --stop <line\|eof>`. The backslash before the pipe (`\|`) is a markdown escape, which is correct, but can reduce readability.

Example:
```
| `-s, --stop <line\|eof>` | No | Line number to stop conversion, or `eof` |
```

The backslash is necessary in markdown to escape the pipe, but it makes the parameter less readable in raw markdown. Consider:
- Keeping it as-is (correct, but less readable in raw form)
- Using a different representation (e.g., `line or eof`)

**Impact:** Minor — markdown rendering is correct, but raw markdown source is slightly harder to read.

**Evidence:**
```
Line 101: | `-s, --stop <line\|eof>` | No | Line number to stop conversion, or `eof` |
```

**Resolution:** No action required (markdown is correct). If improving readability is desired, consider rewording parameter examples to use prose instead of shell syntax (e.g., "Line number or 'eof'").

---

## Issues by File

### `.github/prompts/convert-plaintext-to-md.prompt.md`

| Issue ID | Severity | Category | Description | Line(s) |
| -------- | -------- | -------- | ----------- | ------- |
| CNT-001 | 🔴 Critical | Content | Parameter mismatch: `--header` missing from Inputs section | 24, 99 |
| STR-001 | 🔴 Critical | Structural | Phase 2 Step 3: Incomplete parameter list (missing 3 parameters) | 69 |
| CNT-002 | 🟠 Major | Content | Shell command syntax ambiguity in Phase 2 Step 1 | 67 |
| CNT-003 | 🟠 Major | Content | Logical conflict: Rule 42 vs Phase 2 Step 1 about .md existence | 42, 67 |
| FMT-001 | 🟡 Minor | Formatting | Table syntax readability (backslash escapes in parameters) | 101 |

---

## Formatting Audit Results

✅ **Heading Hierarchy:** Correct (H1 → H2 → H3)

✅ **List Styles:** Consistent (bullet `-` and numbered `1.`)

✅ **Code Fences:** Not used (appropriate for this prompt type)

✅ **Tables:** Proper markdown syntax, 3 tables, all aligned

✅ **Indentation:** Consistent throughout

✅ **Links:** External URLs properly formatted with markdown syntax

✅ **Frontmatter:** YAML format correct with trigger/description/tags

⚠️ **Raw markdown readability:** One parameter uses escaped pipe (`\|`) which is correct but slightly harder to read in raw form.

---

## Content Audit Results

✅ **Clarity:** Generally clear, well-structured

⚠️ **Completeness:** Parameter lists are incomplete in some sections (see CNT-001)

⚠️ **Consistency:** Parameter documentation inconsistent across Inputs section vs Parameters table

⚠️ **Logic:** Potential contradiction between Rule 42 and Phase 2 Step 1 (see CNT-003)

---

## Structural Audit Results

✅ **Organization:** Goal → Context → Inputs → Outputs → Rules → Phases → Parameters → Reference (logical flow)

✅ **Phases:** 4 phases clearly defined with Goal and Steps for each

⚠️ **Phase-to-Parameters alignment:** Phase 2 Step 3 doesn't match Parameters table completely

✅ **Cross-section references:** Generally consistent (e.g., {{file}} used throughout)

---

## Recommendations

### Immediate (Before Using Prompt)

1. **Resolve CNT-001:** Add `--header` to line 24 Inputs list
2. **Resolve STR-001:** Update line 69 Phase 2 Step 3 with all 8 parameters
3. **Resolve CNT-003:** Add clarifying note about idempotent behavior with .md files

### Optional Improvements

4. **Resolve CNT-002:** Clarify shell command syntax in Phase 2 Step 1
5. **Resolve FMT-001:** Consider rewording parameters to use prose format for better readability

---

## Cross-File References Check

✅ All external URLs are live and relevant:
- GitHub markdown docs (primary target audience)
- MarkdownGuide.org (industry standard reference)
- Azure DevOps guidance (platform-specific guidance)

✅ Skills referenced exist:
- `.opencode/skills/writing-plans/`
- `.opencode/skills/simplify/`

✅ No broken internal file references found.

---

**Audit Date:** 2026-05-25
**Audit Tool:** Systematic content analysis with formatting/structural/logic validation
**Status:** ⚠️ 5 issues identified (1 critical, 3 major, 1 minor) — Recommend review before using prompt in production
