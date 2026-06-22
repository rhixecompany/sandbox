# Phases

> Extracted from `convert-plaintext-to-md.prompt.md`.

## Phases

### Phase 1: Intake

**Goal:** Read the request and identify the exact scope.

**Steps:**
1. Read the request and identify the exact scope
2. Locate the relevant files, diffs, or references
3. Run `/context-map` for the target source file and markdown output path
4. Determine which conversion method applies (explicit instructions, documented options, or reference file)

### Phase 2: Execute

**Goal:** Perform the conversion with the smallest safe change set.

**Steps:**
1. Determine source text and initialize output target:
   - If `{{file}}.md` exists, use its current content as source text
   - Otherwise, read source from `#file:{{file}}` and create `{{file}}.md` from that plaintext as the initial target
2. Apply markdown formatting: headers, lists, code blocks, tables
3. Apply each passed parameter per the Parameters table
4. Apply any predefined instructions (`pre=<name>`) if applicable

### Phase 3: Verify

**Goal:** Check the result against the goal, rules, and inputs.

**Steps:**
1. Verify headers are correctly structured
2. Verify code blocks have language annotations where applicable
3. Verify lists and tables are properly formatted
4. Confirm the output is usable and complete

### Phase 4: Hand off

**Goal:** Return the final artifact or findings clearly.

**Steps:**
1. Return the final markdown file path
2. Stop once the requested result is delivered
