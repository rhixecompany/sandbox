# Onboarding Q&A Pattern: Enhancing Prompts with Quick-Answer Sections

## Problem

Complex orchestration prompts (200+ lines, multi-phase workflows) make the agent unusable for simple user questions. A prompt built to research 14 projects fails when someone just asks "summarize this repo" or "check disk usage."

## Solution

Add a lightweight **Onboarding Q&A section** to the existing prompt. Each Q is self-contained, independently runnable, and does not interfere with the main workflow.

## Structure

Each Q&A entry follows this skeleton:

```markdown
### Q<N>: "<User's exact question>"

**Phase: <Topic>**

1. Step one — first action
2. Step two — second action
3. Step three — third action

**Actions:**
```
terminal("command")
read_file("path")
```
```

## When to Apply

| Condition | Apply? |
|-----------|--------|
| Prompt is a complex orchestrator (>200 lines, multi-phase) | ✅ Yes |
| Prompt does NOT handle simple ad-hoc questions | ✅ Yes |
| Prompt is a single-purpose utility (<100 lines) | ❌ No — make a new prompt instead |
| The question is part of the prompt's domain (e.g. disk usage in a repo prompt) | ✅ Yes |
| The question belongs to a different domain | ❌ No — belongs in a different prompt |

## Question Classification

| Class | Example | Placement |
|-------|---------|-----------|
| **Summarize/Intro** | "Summarize this repo in 5 bullets" | Repo prompt |
| **Entrypoint** | "What's the main entrypoint?" | Repo prompt |
| **PR/CI setup** | "Set up a clean GitHub PR workflow" | Repo-management prompt |
| **Disk analysis** | "Show top 5 largest directories" | Repo prompt + management prompt |
| **Directory orientation** | "What's the main project file here?" | Repo prompt |

## Post-Edit Validation Checklist

After writing or editing YAML-frontmatter prompt files, run this checklist before declaring done:

### Frontmatter Integrity
- [ ] File starts with `---` (NOT `|---` — the `|` prefix is a **read_file display artifact**, not actual content)
- [ ] Frontmatter closes with `---` (grep for the second `^---$`)
- [ ] No duplicate fields (grep for `^[a-z_]` keys — `version:`, `name:`, etc. must appear exactly once)
- [ ] `version:` bumped if content changed (minor → 2.0→2.1, patch → 2.0→2.0.1)
- [ ] `trigger:` present for all executable prompts
- [ ] `name:` matches filename stem (e.g. `name: repo` for `repo.prompt.md`)

### Cross-File Consistency (task-related group)
- [ ] Same `version:` across all files in the group
- [ ] Cross-references are symmetric: if A references B's new section, B references A's
- [ ] Description field updated to mention new capabilities

### Content Validation
- [ ] All backticked commands in `**Actions:**` blocks are real, runnable commands
- [ ] `du` flags match the target OS (`--exclude` is GNU coreutils — OK on Git Bash/MSYS)
- [ ] Entrypoint grep patterns cover: Python (`main`, `def main`, `if __name__`), JS/TS (`"main"`, `"start"`), Rust (`fn main`)
- [ ] Headers match the pattern `### Q<N>: "<exact user question>"` for discoverability

### Read File Pipe-Prefix Pitfall

**Critical:** `read_file` displays content as `LINE_NUM|ACTUAL_CONTENT`. When you copy text from read_file output into a `patch` old_string or new_string, the `|` separator between the line number and content MUST NOT be included in the file content. Similarly, `grep -n` displays `LINE_NUM:MATCHED_LINE`, and the colon prefix must NOT be included in patch content.

**Real-world bug from this session:** A section separator `---` was accidentally typed as `|---` because the read_file pipe was copied along with the content. The separator rendered as `|---` in the file, breaking the frontmatter-adjacent layout. Fix: always verify every `---` separator is three bare dashes with no prefix.

### Grep-Based Verification Commands

```bash
# 1. Check version consistency across all files in a group
grep "^version:" prompts/repo*.prompt.md

# 2. Check no duplicate keys in any one file
for f in prompts/repo*.prompt.md; do
  echo "=== $f ==="
  grep -c "^version:" "$f"  # must be 1
  grep -c "^name:" "$f"     # must be 1
  grep -c "^trigger:" "$f"  # must be 1 for executable prompts
done

# 3. Check for spurious pipe-prefix on frontmatter lines
grep -n "^|---" prompts/repo*.prompt.md
# Expected: only legitimate markdown table separators (|----, |-------, etc.)
# NOT: |--- on a line by itself (that's a patch artifact)

# 4. Verify all files' line 1 is ---
head -1 -q prompts/repo*.prompt.md

# 5. Verify target questions present in expected files
grep -c "Summarize this repo\|main entrypoint\|disk usage\|PR workflow" prompts/repo*.prompt.md
```

## Cautions

- **Don't bloat the prompt** — keep each Q&A to 8–15 lines max. The onboarding section as a whole should be ≤80 lines.
- **Duplicate sparingly** — If a question fits into two prompts (e.g. disk usage in both `repo.prompt.md` and `repo-management.prompt.md`), add it to the most natural home and cross-reference from the other.
- **Keep commands real** — Every command in `**Actions:**` must be something the agent can run immediately. No `[placeholder]`, no pseudocode.
- **Use grep for entrypoint detection** — `grep -E '"main"|"start"|main\\.py|def main|if __name__|fn main'` covers Python, JS/TS, and Rust in one pass.
- **Exclude noise in disk scans** — Always exclude `.git`, `node_modules`, `venv`, `__pycache__`, `dist`, `build`, `target`.
