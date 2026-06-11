# Manual Review Queue

Date: 2026-05-30 Status: open Purpose: duplicate families intentionally left in
place after conservative cleanup

## Review Principles

These items were not auto-deleted because they belong to project-local vendor,
static, template, or generated-report trees where duplication alone is not a
sufficient delete signal.

## Queue

### 1. Project Vendor And Static Text Duplicates

Reason: exact duplicates are present across multiple projects, but they are
owned by separate project trees and may be required for packaging, attribution,
or framework integrity.

Examples:

- `projects/profile/base/static/admin/fonts/README.txt`
- `projects/profile/static/admin/fonts/README.txt`
- `projects/xamehi.tv/static/admin/fonts/README.txt`
- `projects/profile/base/static/ckeditor/ckeditor/LICENSE.md`
- `projects/profile/static/ckeditor/ckeditor/LICENSE.md`
- `projects/profile/base/static/admin/js/vendor/jquery/LICENSE.txt`
- `projects/profile/static/admin/js/vendor/jquery/LICENSE.txt`
- multiple `OFL.txt`, `README.txt`, and `LICENSE*.md` files across `comicwise`,
  `rhixecompany-comics`, `Django-Scrapy-Selenium`, and other project asset trees

Recommended action:

- Review per project before removing any file.
- Deduplicate only if build/runtime/attribution requirements are proven
  unchanged.

### 2. Generated Project-Docs Placeholder Changelogs

Reason: several `docs/project-docs/*/CHANGELOG.md` files are byte-identical.
They look templated, but they may still be intentionally scoped to each
project-docs directory.

Examples:

- `docs/project-docs/ecom/CHANGELOG.md`
- `docs/project-docs/my-opencode-config/CHANGELOG.md`
- `docs/project-docs/profile/CHANGELOG.md`
- `docs/project-docs/Python-projects/CHANGELOG.md`
- `docs/project-docs/rhixe_scans/CHANGELOG.md`
- `docs/project-docs/selenium_webdriver/CHANGELOG.md`
- `docs/project-docs/university-libary-jsm/CHANGELOG.md`

Recommended action:

- Decide whether these should remain per-project placeholders or be replaced by
  a shared template policy.
- If removed, update any project-doc generator assumptions first.

### 3. Hermes Completion Report Family

Reason: these files overlap by subject but are not exact duplicates. They appear
to represent different reporting layers within the Hermes setup work.

Files:

- `docs/COMPLETION_REPORT.md`
- `docs/HERMES_MIGRATION_COMPLETION_REPORT.md`
- `docs/HERMES_COMPLETE_VERIFICATION.md`
- `docs/HERMES_CONFIGURATION_STATUS.md`

Recommended action:

- Keep for now.
- Consider a future merge into one status page, one verification page, and one
  archival completion report.

### 4. Workspace Consolidation Summary Family

Reason: both files are active summary-style docs with related but not identical
scope.

Files:

- `docs/workspace-consolidation-summary.md`
- `docs/workspace-consolidation-final-summary.md`

Recommended action:

- Review whether the final summary should be archived and the regular summary
  kept as the living document.

### 5. Update-Implementation-Plan Report Family

Reason: this set is clearly one workflow family, but it is still used as a
traceable audit trail and should not be compressed without verifying who links
into it.

Files:

- `docs/TASK_COMPLETION_SUMMARY.md`
- `docs/UPDATE_IMPLEMENTATION_PLAN_INDEX.md`
- `docs/update-implementation-plan-context.md`
- `docs/update-implementation-plan-issues-context.md`
- `docs/update-implementation-plan-fix-issues-context.md`
- `docs/update-implementation-plan-phase4-verification.md`

Recommended action:

- Keep the audit trail intact for now.
- If reduced later, preserve one executive summary, one index, and one final
  verification record.

## Completed In This Wave

- `projects/comicwise/docs/TRIAGE_REPORT.md` archived and deleted
- `projects/comicwise/docs/triage-report.md` kept as canonical
- docs index family consolidated to one canonical hub plus compatibility pages
