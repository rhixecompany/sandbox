# Folder Structure and Output

> Extracted from `mkdocs-translations.prompt.md`.

## Folder Structure and Output

Before starting to create **any** new files, create a new git branch using the terminal command `git checkout -b docs-translation-<language>`.

- Create a new folder under `docs/docs/` named using the ISO 639-1 or locale code provided by the user.  
  Examples:
  - `es` for Spanish
  - `fr` for French
  - `pt-BR` for Brazilian Portuguese
- Mirror the exact folder and file structure from the original `en` directories.
- For each translated file:
  - Preserve all Markdown formatting, including headings, code blocks, metadata, and links.
  - Maintain the original filename.
  - Do **not** wrap the translated content in Markdown code blocks.
  - Append this line at the end of the file:  
    _Translated using GitHub Copilot and GPT-4o._
  - Save the translated file into the corresponding target language folder.

---
