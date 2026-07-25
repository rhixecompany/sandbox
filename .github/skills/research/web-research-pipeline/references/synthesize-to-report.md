# Synthesizing a RESEARCH_REPORT from Existing Research

## When This Applies

A project already has a curated web-research document (`web-research-<project>.md`). The task is to synthesize it into the standardized report template. This is common when research and reporting run as separate passes.

## Workflow

### 1. Find the research artifact

Search for `web-research*` under the project directory. If not found at the expected path, broaden the search across all projects.

### 2. Read the research artifact

Files can exceed 400 lines. Page through in 200-line segments using offset. If the dedup system says "unchanged" for a file you haven't seen, force with `offset=1`.

### 3. Gather local project documents

Open the project's architecture overview, readme, package manifest, status summary, and specs. These are authoritative for project specifics — prefer them over web data when they conflict.

### 4. Write from template

Standard sections: project header, similar projects, key findings, cheatsheets, best practices, common pitfalls, performance, security, related projects, resources. Use ONLY real data. Drop any section that lacks data.

### 5. Size compliance

Verify with byte count. Target: 1024-5120 bytes (1KB-5KB). Over 5KB: trim systematically using the hierarchy below. Under 1KB: expand with more references.

**Systematic trimming hierarchy (most to least aggressive):**

| Priority | Technique | Typical savings |
|----------|-----------|----------------|
| 1 | Shorten table cell descriptions (remove adverbs, articles, clauses) | 30-80 bytes per cell |
| 2 | Condense bullet points (keep one fact per bullet, drop examples) | 20-50 bytes per bullet |
| 3 | Merge related items into semicolon-separated lines | 15-40 bytes per merge |
| 4 | Remove redundancy (shorten Best Practices if same in Key Findings) | 30-80 bytes per item |
| 5 | Shorten inline formatting (drop version tags, shorten paths) | 5-20 bytes |

**What NOT to cut:** Never drop a `##` section (9 minimum). Never remove tech stack, verifiable source URLs, or findings traceable to research.

Check size after each round: `wc -c < "projects/<name>/RESEARCH_REPORT.md"`. If still over, repeat hierarchy. If under 1KB, you trimmed too much — restore wording in priorities 1-2.

### 6. Cross-reference symmetry

If project A references project B in related projects, check that B's report also references A.

## Real Example: Bash Project

- Research file: `projects/Bash/web-research-bash.md` (481 lines, 18.7KB)
- Local docs read: architecture overview, readme, package manifest, status summary, specs, real-world examples (6 files)
- Output: 4,828 bytes, 125 lines, 10 sections
- Size fix: first draft 7,694 bytes (over 5KB) — trimmed tables and condensed prose

## Pitfalls

- **Dedup on first read**: If a file was never read but `read_file` says "unchanged", use `offset=1` to force re-read
- **First draft too large**: Drafts commonly exceed 5KB — use the systematic trimming hierarchy in step 5; avoid dropping whole sections or essential source URLs
- **Over-trimming into <1KB**: If after trimming you're under 1KB, you removed too much — restore full descriptions in table cells and bullet points rather than adding fabricated content
- **Missing local file**: Skip that section rather than fabricate data
- **Asymmetric cross-refs**: Always check both directions of related projects
