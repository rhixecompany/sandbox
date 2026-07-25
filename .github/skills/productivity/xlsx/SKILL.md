---
author: Alexa
description: Use when working with spreadsheet files (.xlsx/.xlsm/.csv/.tsv) — reading,
  editing, creating, formatting, charting, or converting tabular data.
license: MIT
name: xlsx
tags:
- imported
title: Xlsx
version: 1.0.0

---
## Description

Use for spreadsheet files as primary input or output. Open, read, edit, fix existing .xlsx/.xlsm/.csv/.tsv files, create new spreadsheets, or convert between tabular formats.


## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## When to Use

- Opening or reading spreadsheet files
- Editing or fixing existing spreadsheets
- Creating new spreadsheets from scratch
- Adding columns or computing formulas
- Formatting or charting data
- Cleaning messy tabular data
- Converting between spreadsheet formats

## When NOT to Use

- Word documents (use docx skill)
- PDF files (use pdf skill)
- Google Sheets API integration
- Database pipelines
- Non-tabular data

## Workflow

### Phase 1: Identify Task

- Determine spreadsheet operation
- Gather source files
- Plan output format
- Review data structure

### Phase 2: Process Spreadsheet

- Open file
- Analyze data
- Apply transformations
- Add formulas or formatting

### Phase 3: Validate & Clean

- Verify data accuracy
- Fix formatting issues
- Remove duplicates
- Validate formulas

### Phase 4: Export & Archive

- Save to appropriate format
- Verify output
- Archive originals
- Document changes

## Tools & References

- **Related Skills**: docx, pdf
- **File Formats**: .xlsx, .xlsm, .csv, .tsv
- **Libraries**: openpyxl, pandas, xlrd
- **Operations**: Read, write, format, chart

## Best Practices

- Keep original files as backup
- Use consistent formatting
- Document formulas
- Validate data before processing
- Test on sample files first
- Use meaningful column names
- Archive important spreadsheets



## Pitfalls

- **Stale cache:** Always re-read files from disk after editing; don't rely on cached context
- **Context limits:** Process in batches; write results after each batch
## Verification Checklist

- [ ] Frontmatter complete (name, title, description, version, author, license, tags)
- [ ] Skills Required table present
- [ ] Workflow has ≥3 phases
- [ ] Pitfalls section present
- [ ] All references cited in SKILL.md body
- [ ] SKILL.md is under 250 lines
- [ ] No placeholder text

