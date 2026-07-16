# Project Folders Structure Blueprint

Generated from workspace: `C:\Users\Alexa\Desktop\SandBox`

## Workspace Folder Overview
- Root workspace contains shared config files plus a `projects/` collection of subprojects.
- Folder organization is mixed: some projects are app-centric, some are backend/frontend splits, and some are language/tooling examples.

## Top-Level Tree
```text
./
├── .github/
│   ├── agents/
│   ├── instructions/
│   ├── skills/
│   ├── workflows/
│   ├── copilot-instructions.md
│   └── pull_request_template.md
├── .hermes/
│   ├── approvals/
│   ├── archived-plan-templates/
│   ├── archived-prompt-templates/
│   └── plans/
├── Bash/
├── judge_results/
│   ├── all_results.json
│   ├── all_results2.json
│   ├── all_results3.json
│   ├── all_results4.json
│   ├── all_results5.json
│   ├── all_results6.json
│   ├── summary.md
│   ├── summary2.md
│   ├── summary3.md
│   ├── summary4.md
│   ├── summary5.md
│   └── summary6.md
├── projects/
│   ├── Banking/
│   ├── Bash/
│   ├── comicwise/
│   ├── cookiecutter-django-tailwind/
│   ├── Django-Scrapy-Selenium/
│   ├── ecom/
│   ├── mcp-servers/
│   ├── profile/
│   ├── Python-projects/
│   ├── Resume_maker/
│   ├── rhixe_scans/
│   ├── rhixecompany-comics/
│   ├── selenium_webdriver/
│   ├── university-libary-jsm/
│   ├── xamehi/
│   ├── xamehi.tv/
│   ├── youtube-downloader/
│   ├── COMPLETION_REPORT.txt
│   ├── README_RESEARCH.md
│   ├── RESEARCH_CAMPAIGN_SUMMARY.md
│   └── RESEARCH_INDEX.md
├── research/
│   ├── binance-api-tutorial/
│   ├── busha-api-tutorial/
│   ├── cryptocurrency-wallets-api-tutorial/
│   ├── face-mask-video-call-tutorial/
│   ├── flutterwave-tutorial/
│   ├── hermes-agents-tutorial/
│   ├── hermes-memory-files/
│   ├── paypal-tutorial/
│   ├── paystack-tutorial/
│   └── python-asyncio-tutorial/
├── results/
│   ├── _agents_fix_discovery.json
│   ├── agents-fix.output.md
│   └── consolidated-agent-registry.json
├── Resume_maker/
├── templates/
│   └── execute-all-prompts/
├── .editorconfig
├── .git-blame-ignore-revs
├── .gitmodules
├── .hermes.md
├── .markdownlintrc.json
├── 1614584020.txt
├── AGENTS.md
├── analysis_slice1.json
├── analyze_slice1.py
├── analyze_slice3.py
├── audit_prompts.py
├── audit_skills.py
├── build_registry.py
├── build_report.py
├── build_report_slice1.py
├── bun.lock
├── classify.py
├── classify2.py
├── CLEANUP_SUMMARY.md
├── CONTRIBUTING.md
├── index.ts
├── inspect_tags.py
├── llms.txt
├── package.json
├── PRESTATE_SandBox.md
├── README.md
├── requirements.txt
├── score_slice3.py
├── SESSION_REPORT.md
├── slice3.txt
├── tsconfig.json
```

## Naming Conventions
- Preserve existing folder names exactly, including hyphens, underscores, and dots.
- Avoid renaming subprojects unless a collision or portability issue is confirmed.

## File Placement
- Keep workspace-level docs in `docs/`.
- Keep per-project docs under `docs/Project_Architecture/` using the project path as namespace to avoid filename collisions.

## Update Notes
- Refresh after any project move, split, or subproject addition.