---
author: Alexa
description: Use when working with PDF files — reading, extracting text/tables, combining,
  splitting, rotating, watermarking, filling forms, encrypting, or OCR.
license: MIT
name: pdf
tags:
- imported
title: Pdf
version: 1.0.0

---
## Description

Work with PDF files including reading, extracting text/tables, combining, splitting, rotating pages, adding watermarks, filling forms, encrypting/decrypting, and OCR.


## Skills Required

| Skill | Purpose |
|-------|---------|
| `terminal` | CLI commands execution |
| `file` | Read/write files |

## When to Use

- Reading or extracting text from PDFs
- Combining or merging multiple PDFs
- Splitting PDFs into separate files
- Rotating or rearranging pages
- Adding watermarks or annotations
- Filling PDF forms
- Encrypting or decrypting PDFs
- OCR on scanned PDFs

## When NOT to Use

- Word documents (use docx skill)
- Spreadsheets (use xlsx skill)
- Image files
- Real-time PDF editing

## Workflow

### Phase 1: Identify Task

- Determine PDF operation needed
- Gather source files
- Plan output format

### Phase 2: Process PDF

- Load PDF file
- Apply transformations
- Extract or modify content
- Handle errors

### Phase 3: Generate Output

- Create new PDF or modify existing
- Verify output quality
- Check file size

### Phase 4: Verify & Save

- Review results
- Save to appropriate location
- Archive originals if needed

## Tools & References

- **Related Skills**: docx, xlsx
- **Libraries**: PyPDF2, pdfplumber, reportlab
- **OCR**: Tesseract, pytesseract
- **Encryption**: PDF encryption standards

## Best Practices

- Keep original PDFs as backup
- Test on sample files first
- Verify extracted content
- Use appropriate compression
- Document transformations
- Handle large files efficiently
- Maintain file metadata

## Recently Absorbed Skills
- `nano-pdf` (2026-06-25) — PDF text editing via nano-pdf CLI (NL prompts)

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

