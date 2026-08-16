# Repo Narrative Docs — Templates & Recipe

Deliverable pair (e.g. `/repo-story-time`): for each repo write `REPOSITORY_SUMMARY.md` (factual) and `THE_STORY_OF_THIS_REPO.md` (narrative retelling of git history).

## Git evidence commands (run per repo, in bash/MSYS)

```sh
git rev-list --count HEAD                                  # total commits
git shortlog -sn                                           # contributor stats
git log --pretty=format:"%ad|%s" --date=short             # date + subject per commit
git log --pretty=format:"%an <%ae>" | sort | uniq -c      # author tally
```

## REPOSITORY_SUMMARY.md — sections

1. **Overview** — what it is, status + license from README
2. **Architecture** — stack bullets, layer/diagram map
3. **Key Components** — paths/files of interest
4. **Technologies** — from `technology-stack.md`
5. **Data Flow**
6. **Team** — `git shortlog -sn` contributor stats (be honest if 1 author)
7. **Evidence Appendix (git)** — commit count, date range, authors

## THE_STORY_OF_THIS_REPO.md — sections

- **Year-in-Numbers** table (commits, contributors, first/latest date, span)
- **Contributors** (shortlog)
- **Seasonal Patterns** (commit dates in order)
- **Themes** (recurring words in subjects)
- **Plot Twists** (notable commits / surprises)
- **Current Chapter** (latest 3 commits + reading of present)

## CRITICAL: synthetic git history (the honest caveat)

Local submodules often show ONE author, all commits within a few weeks, subjects like `initial local project setup` / `vscode config audit` / `update RESEARCH_REPORT.md ... trim to size gate`. This is workspace maintenance, NOT real upstream history.

- Derive product facts from `README`/`ARCHITECTURE`/`AGENTS`, not the git log.
- In `THE_STORY`, state explicitly that the git log is local-submodule-only and does not capture upstream lineage.
- Flag repos carrying large upstream artifacts (`CHANGELOG.md`, `CONTRIBUTORS.md`) inside a tiny-commit repo — that is the real lineage.
- Never fabricate commit narratives.
