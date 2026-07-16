# The Story of This Repo — Resume_maker (Job Docs Generator)

*A narrative built from real git data. **Scope caveat:** `Resume_maker` is a folder inside the `SandBox` monorepo, not its own repo/submodule.*

## Year in Numbers
- **182** total commits in the parent `SandBox` monorepo (all by `rhixecompany`)
- **4** commits that actually touch the `projects/Resume_maker/` path (all dated 2026-07)
- **1** contributor — `rhixecompany <rhixecompany@gmail.com>`
- **~2+** sample people encoded in the repo (`alexander-input.json`, `basil-input.json`)
- **4** document types produced: resume, cover letter, LinkedIn guide, interview prep

## Contributors
| Author | Workspace commits | Commits touching `projects/Resume_maker/` |
| --- | --- | --- |
| rhixecompany | 182 | 4 |

Solo, across the entire workspace.

## Seasonal Patterns
Scoped to the folder: **all 4** Resume_maker-touching commits fall in **2026-07** (Jul 9, 10, 15, 16) — part of the workspace's prompt-enrichment and YAML-repair sprint. The generator source predates these (Jun workspace history) but isn't isolated in Resume_maker-specific commits.

## Themes
- **Personal, pragmatic tooling.** This is the only project in the slice built to produce *documents about a person* — resumes and cover letters — with real sample inputs (`alexander`, `basil`).
- **AI-assisted authoring.** It ships `grok_summary_prompt.md`/`.txt` — the generator is designed to pair with an LLM (Grok) to summarize and shape the resume content.
- **Research era (Jul).** Its 4 folder-commits are workspace updates + the YAML corruption fix — the same reporting wave seen everywhere.

## Plot Twists
1. **A résumé generator that lives inside someone else's résumé of commits.** Like Bash, Resume_maker has no git identity of its own; to find its history you slice the monorepo by path, and what you find is maintenance, not features.
2. **Grok, not GitHub Copilot, is the co-author.** While siblings lean on Copilot instructions, Resume_maker carries explicit Grok prompt files — a different AI workflow for the writing step.
3. **Failure-tolerant by design.** PDF conversion can fail and the Markdown still survives (and vice-versa). The tool assumes the worst and degrades gracefully — a quiet sign of hard-won experience with `markdown-pdf`.

## Current Chapter
Resume_maker is a **stable, personal utility** in light-maintenance mode. Its generator works; recent commits are workspace-level updates. The next chapter is likely incremental prompt tuning (the Grok summary prompts) rather than architectural change.

> Evidence note: path-scoped counts from `git log -- <path>` and `git shortlog`. The 182 figure is the monorepo total, explicitly distinguished from the 4 folder-scoped commits. Scoping ambiguity is disclosed, not hidden.
