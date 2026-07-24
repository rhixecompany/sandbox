---
name: audit-skills-judge-fix
title: Audit Skills Judge Fix
project_path: C:\Users\Alexa\Desktop\SandBox
description: Run local skills audit and collect findings; categorize skill health, duplicates, and dead entries; run judge scoring; remediate fixable issues; consolidate mappings; verify with tooling; write audit reports.
version: 1.0.0
license: MIT
author: Hermes Agent
toolsets: - file - terminal - browser - skills
scripts: []
skills: - using-superpowers - user-communication-preferences - plans-and-specs - executing-plans - verification-before-completion - subagent-driven-development
formatter: default
plan: |
  ### Phase 1: Skills Audit Collection
  - Enumerate Hermes skills: `hermes skills` → extract active skills
  - Pull full SKILL.md for each skill: verify frontmatter completeness
  - Collect metrics: skill_dir, name, title, version, author
  
  ### Phase 2: Health Categorization
  - Calculate health score: (defined_fields_present / total_fields) * 100
  - Define categories: healthy (>90), needs_attention (70-89), critical (<70)
  - Generate summary: total skills, healthy, needs_attention, critical
  
  ### Phase 3: Judge Scoring
  - Score each skill by: completeness, formatting, metadata consistency
  - Risk factors: missing fields, outdated versions, unclear purpose
  - Output: health report + prioritized action list

  ### Phase 4: Remediation Planning
  - For each critical skill: create remediation plan
  - Staging steps: patch missing fields in SKILL.md
  - Document changes: log in `docs/audit/skills-audit-restoration-log.md`

  ### Phase 5: Verification & Reporting
  - Re-run audit after remediation: confirm health improvement
  - Generate final report: `docs/audit/skills-audit-final-report.md`
  - Archive: compress audit logs

dependencies: - skill:using-superpowers - skill:user-communication-preferences - skill:plans-and-specs - skill:executing-plans - skill:verification-before-completion - skill:subagent-driven-development
tags: - audit - execution - fix - ml - prompts - skills - workflow
trigger: /audit-skills-judge-fix
metadata:
  related_skills: [using-superpowers, user-communication-preferences, plans-and-specs, executing-plans, verification-before-completion, subagent-driven-development]
  workspace_path: C:\Users\Alexa\Desktop\SandBox
  audit_output_dir: C:\Users\Alexa\Desktop\SandBox\docs\audit
---

# Audit Skills Judge Fix

## Overview

Audit Hermes skills in the SandBox workspace, categorize health, run judge scoring, plan remediations, and verify improvements.

## Phase 1: Skills Audit Collection

1. **Enumerate active skills**
   - Run: `hermes skills` → output to `docs/audit/skills-list.txt`
   - Extract skill names for processing

2. **Collect skill metadata**
   - For each skill, read SKILL.md: `C:\Users\Alexa\Desktop\SandBox\hermes\skills\<skill_name>\SKILL.md`
   - Gather: name, title, description, version, author, linked_files count
   - Store in structured audit data: `docs/audit/skills-audit-data.json`

## Phase 2: Health Categorization

Categorize each skill based on completeness:

- **Healthy (>90%)**: All required fields present, complete frontmatter, well-structured
- **Needs Attention (70-89%)**: Minor gaps, one or two missing fields
- **Critical (<70%)**: Major gaps, incomplete frontmatter, structural issues

Health score calculation:
```yaml
health_score: (defined_fields / total_required_fields) * 100
total_required_fields: 12 (name, title, description, version, license, author, toolsets, scripts, skills, formatter, plan, tags)
```

## Phase 3: Judge Scoring

Score skills by:

- **Completeness**: Frontmatter completeness
- **Formatting**: YAML syntax, markdown structure
- **Metadata**: Consistent and clear metadata
- **Risk Assessment**: Missing critical fields, outdated versions
- **Overall Quality**: Documentation quality, consistency

Output: `docs/audit/skills-judge-scores.json` with per-skill scores and recommendations.

## Phase 4: Remediation Planning

For **Critical** skills (score < 70%):

1. **Analyze gaps**
   - Read current SKILL.md
   - Identify missing required fields
   - List structural issues

2. **Create remediation steps**
   - For each missing field, draft corrective content
   - Plan specific `patch` actions with exact old_string and new_string

3. **Execute in staging**
   - Apply patches to skill SKILL.md files
   - Log all changes: `docs/audit/skills-audit-restoration-log.md`

4. **Verify remediation**
   - Re-run health assessment
   - Confirm skills moved to Healthy or Needs Attention category

## Phase 5: Verification & Reporting

1. **Health verification**
   - Run complete re-audit: `hermes skills` + analysis
   - Compare before/after metrics
   - Confirm improvements quantified

2. **Generate final report**
   - `docs/audit/skills-audit-final-report.md` includes:
     - Executive summary of improvements
     - Skill health trends over time
     - Remaining action items
     - Recommendations for ongoing maintenance

3. **Archive and cleanup**
   - Compress audit logs: `docs/audit/skills-audit-logs.tar.gz`
   - Clean temporary files in `docs/audit/`

## Exit Condition

Audit complete when:

- All skills assessed and categorized
- Critical skills remediated to Healthy/Needs Attention
- Verification report generated
- Final metrics logged in progress tracker
- Audit artifacts archived

## Notes

- This audit focuses on **compact, declarative skill quality**
- Use `skill_manage` for actual skill patches, but document all planned changes
- Maintain deterministic audit trail for reproducibility
- Skip destructive deletions; focus on structural corrections and metadata enrichment
