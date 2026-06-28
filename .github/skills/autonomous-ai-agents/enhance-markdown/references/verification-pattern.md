# Independent Verification Pattern for enhance-markdown

**Source:** Session 2026-06-14 — enhance-markdown on sample.prompt.md + sample.prompt.txt
**Updated:** 2026-06-21 — Added file-type-aware field checks, YAML-comment H1 edge case, pipe-balance check

## Pattern: execute_code with YAML + Regex Verification

Use `execute_code` with a Python script to independently verify Phase 4 gates without relying on the agent's own editing accuracy.

### Template

```python
import yaml
import re

def verify_file(path, purpose):
    with open(path, 'r') as f:
        content = f.read()
        lines = content.split('\n')

    results = {"passed": [], "failed": [], "warnings": []}
    is_prompt = path.endswith('.prompt.md')
    is_skill = path.endswith('SKILL.md')

    # 1. Frontmatter parses as single YAML document
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if fm_match:
        try:
            fm = yaml.safe_load(fm_match.group(1))
            results["passed"].append("Frontmatter parses as single YAML document")
        except yaml.YAMLError as e:
            results["failed"].append(f"Frontmatter YAML parse error: {e}")
            fm = {}
    else:
        results["failed"].append("No frontmatter found")
        fm = {}

    # --- Field checks are file-type-aware ---
    # SKILL.md required: name, title, description, tags, version, author, license
    # .prompt.md required: trigger, description, tags, skills (name, title, version recommended)
    if is_prompt:
        required = ['trigger', 'description', 'tags', 'skills']
        recommended = ['name', 'title', 'version', 'metadata']
    else:
        required = ['name', 'title', 'description', 'tags', 'version', 'author', 'license']
        recommended = ['metadata']

    # 2. Required fields
    for r in required:
        if r in fm:
            results["passed"].append(f"Required field '{r}' present")
        else:
            results["failed"].append(f"Missing required field '{r}'")

    # 3. Recommended fields
    for r in recommended:
        if r in fm:
            results["passed"].append(f"Recommended field '{r}' present")
        else:
            results["warnings"].append(f"Missing recommended field '{r}'")

    # 4. metadata.hermes.related_skills (optional but valuable for both)
    if 'metadata' in fm and 'hermes' in fm['metadata'] and 'related_skills' in fm['metadata']['hermes']:
        rs = fm['metadata']['hermes']['related_skills']
        results["passed"].append(f"metadata.hermes.related_skills: {rs}")
        # Cross-check: if both skills: and metadata.hermes.related_skills exist, they must match
        if 'skills' in fm:
            fm_skills = set(fm['skills'])
            md_skills = set(rs)
            if fm_skills == md_skills:
                results["passed"].append(f"skills and metadata.hermes.related_skills match")
            else:
                results["failed"].append(f"skills mismatch: fm={fm_skills} vs md={md_skills}")
    else:
        results["warnings"].append("metadata.hermes.related_skills missing")

    # 5. No 'mode' field (anti-pattern for both file types)
    if 'mode' in fm:
        results["failed"].append(f"Non-standard 'mode' field present: {fm['mode']}")
    else:
        results["passed"].append("No 'mode' field in frontmatter")

    # 6. Double-fence check (first 60 lines)
    first_60 = lines[:60]
    fence_count = sum(1 for line in first_60 if line.strip() == '---')
    if fence_count == 2:
        results["passed"].append(f"Frontmatter fences in first 60 lines: {fence_count} (expected 2)")
    else:
        results["failed"].append(f"Frontmatter fences in first 60 lines: {fence_count} (expected 2)")

    # 7. Skills list cleanliness (context-aware)
    if 'skills' in fm:
        skills_val = fm['skills']
        if isinstance(skills_val, list):
            for s in skills_val:
                if isinstance(s, str) and (' ' in s or ':' in s):
                    results["failed"].append(f"skills list contains prose/deps: '{s}'")
            # For SKILL.md: warn if skills: is present (should use metadata.hermes.related_skills)
            if is_skill:
                results["warnings"].append(
                    "skills: field in SKILL.md frontmatter — use metadata.hermes.related_skills instead"
                )
        else:
            results["failed"].append(f"skills: is {type(skills_val).__name__}, not a list")
    elif is_prompt:
        results["failed"].append("Missing 'skills' field for .prompt.md file")
    else:
        results["passed"].append("No skills: field (expected for SKILL.md — uses metadata.hermes.related_skills)")

    # 8. Single H1 check (with YAML comment edge case)
    h1_matches = [(i+1, l) for i, l in enumerate(lines) if re.match(r'^# ', l)]
    # Filter out YAML comments (inside frontmatter between --- fences)
    real_h1 = [(ln, text) for ln, text in h1_matches
               if not (1 <= ln <= 30 and text.strip().startswith('# '))]
    # Also check: is a YAML comment masquerading as H1?
    yaml_h1 = [ln for ln, text in h1_matches if text.strip().startswith('# ')
               and 1 <= ln <= 30]
    if yaml_h1:
        results["warnings"].append(
            f"YAML comment at column 0 parsed as H1 on line(s) {yaml_h1} — indent comments"
        )
    if len(real_h1) == 0:
        results["failed"].append("No real H1 heading found")
    elif len(real_h1) == 1:
        results["passed"].append("Single H1 heading")
    else:
        results["warnings"].append(f"{len(real_h1)} H1 headings found: {[text for _, text in real_h1]}")

    # 9. Phase headings (H2 for phases)
    phase_h2 = re.findall(r'^(## Phase \d+:.*?)$', content, re.MULTILINE)
    phase_h3 = re.findall(r'^(### Phase \d+:.*?)$', content, re.MULTILINE)
    if phase_h2 and not phase_h3:
        results["passed"].append(f"Phase headings use H2: {len(phase_h2)} phases")
    elif phase_h3:
        results["warnings"].append(f"Phase headings use H3 (should be H2): {len(phase_h3)}")
    else:
        results["warnings"].append("No Phase headings found (optional)")

    # 10. Checkbox task items
    checkboxes = re.findall(r'- \[ \] .*', content)
    results["passed"].append(f"Checkbox task items: {len(checkboxes)}")

    # 11. Verification checklist section
    if '## Verification Checklist' in content:
        results["passed"].append("Verification checklist section present")
    else:
        results["warnings"].append("Verification checklist section missing")

    # 12. File extension
    if path.endswith('.prompt.md'):
        results["passed"].append("File extension: .prompt.md")
    elif path.endswith('.txt'):
        results["failed"].append("File extension: .txt — must be .prompt.md or SKILL.md")
    elif path.endswith('SKILL.md'):
        results["passed"].append("File extension: SKILL.md")
    else:
        results["warnings"].append(f"File extension: .{path.split('.')[-1]} (unexpected)")

    # 13. Trigger matches filename stem (prompt.md only)
    if is_prompt and 'name' in fm and 'trigger' in fm:
        expected_trigger = '/' + fm['name']
        if fm['trigger'] == expected_trigger:
            results["passed"].append(
                f"Trigger matches filename stem: {fm['trigger']} -> {fm['name']}.prompt.md"
            )
        else:
            results["failed"].append(
                f"Trigger '{fm['trigger']}' != expected '{expected_trigger}' from name"
            )

    # 14. Table pipe-balance check (handles 2+ column tables)
    in_code = False
    for i, line in enumerate(lines):
        s = line.strip()
        if s.startswith('```'):
            in_code = not in_code
        elif not in_code and s.startswith('|') and '---' not in s:
            pipes = s.count('|')
            if pipes % 2 == 0:
                results["warnings"].append(
                    f"Line {i+1}: even pipe count ({pipes}) — may be missing trailing pipe"
                )

    return results

# Run verification
results = verify_file('./target.prompt.md', 'target')
results2 = verify_file('./SKILL.md', 'skill-name')

print("=== target.prompt.md ===")
for r in results["passed"]: print(f"✅ {r}")
for r in results["warnings"]: print(f"⚠️  {r}")
for r in results["failed"]: print(f"❌ {r}")

print("\n=== SKILL.md ===")
for r in results2["passed"]: print(f"✅ {r}")
for r in results2["warnings"]: print(f"⚠️  {r}")
for r in results2["failed"]: print(f"❌ {r}")
```

### Key Principles

1. **Independent** — Runs separately from the edit/apply flow; doesn't trust the agent's own state
2. **Deterministic** — Uses `yaml.safe_load` and regex, not LLM judgment
3. **Comprehensive** — Checks all Phase 4 gates in one pass
4. **Structured output** — Passed/Failed/Warning categories for clear reporting
5. **File-type-aware** — Adapts frontmatter field validation to SKILL.md vs `.prompt.md` conventions

### When to Use

- Phase 4 verification gate
- Post-fix validation before claiming completion
- CI-style checks on prompt files

### Edge Cases Handled

- **YAML comment as false H1:** A `# comment` at column 0 inside YAML frontmatter is regex-matched as markdown H1. Indent comments or use trailing inline comments.
- **Table pipe balance:** A 2-column table has 3 pipes (`| col1 | col2 |`) — correct. An even pipe count signals a missing trailing pipe.
- **File-type awareness:** `.prompt.md` files require `trigger`, `description`, `tags`, `skills`; SKILL.md files require `name`, `title`, `description`, `tags`, `version`, `author`, `license`.
