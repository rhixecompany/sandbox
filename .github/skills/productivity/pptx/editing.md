---
name: pptx-editing
description: "Editing Presentations"
version: 1.0.0
author: Alexa
---
     1|# Editing Presentations
     2|
     3|## Template-Based Workflow
     4|
     5|When using an existing presentation as a template:
     6|
     7|1. **Analyze existing slides**:
     8|
     9|   ```bash
    10|   python scripts/thumbnail.py template.pptx
    11|   python -m markitdown template.pptx
    12|   ```
    13|
    14|   Review `thumbnails.jpg` to see layouts, and markitdown output to see placeholder text.
    15|
    16|2. **Plan slide mapping**: For each content section, choose a template slide.
    17|
    18|   ⚠️ **USE VARIED LAYOUTS** — monotonous presentations are a common failure mode. Don't default to basic title + bullet slides. Actively seek out:
    19|   - Multi-column layouts (2-column, 3-column)
    20|   - Image + text combinations
    21|   - Full-bleed images with text overlay
    22|   - Quote or callout slides
    23|   - Section dividers
    24|   - Stat/number callouts
    25|   - Icon grids or icon + text rows
    26|
    27|   **Avoid:** Repeating the same text-heavy layout for every slide.
    28|
    29|   Match content type to layout style (e.g., key points → bullet slide, team info → multi-column, testimonials → quote slide).
    30|
    31|3. **Unpack**: `python scripts/office/unpack.py template.pptx unpacked/`
    32|
    33|4. **Build presentation** (do this yourself, not with subagents):
    34|   - Delete unwanted slides (remove from `<p:sldIdLst>`)
    35|   - Duplicate slides you want to reuse (`add_slide.py`)
    36|   - Reorder slides in `<p:sldIdLst>`
    37|   - **Complete all structural changes before step 5**
    38|
    39|5. **Edit content**: Update text in each `slide{N}.xml`. **Use subagents here if available** — slides are separate XML files, so subagents can edit in parallel.
    40|
    41|6. **Clean**: `python scripts/clean.py unpacked/`
    42|
    43|7. **Pack**: `python scripts/office/pack.py unpacked/ output.pptx --original template.pptx`
    44|
    45|---
    46|
    47|## Scripts
    48|
    49|| Script         | Purpose                               |
    50|| -------------- | ------------------------------------- |
    51|| `unpack.py`    | Extract and pretty-print PPTX         |
    52|| `add_slide.py` | Duplicate slide or create from layout |
    53|| `clean.py`     | Remove orphaned files                 |
    54|| `pack.py`      | Repack with validation                |
    55|| `thumbnail.py` | Create visual grid of slides          |
    56|
    57|### unpack.py
    58|
    59|```bash
    60|python scripts/office/unpack.py input.pptx unpacked/
    61|```
    62|
    63|Extracts PPTX, pretty-prints XML, escapes smart quotes.
    64|
    65|### add_slide.py
    66|
    67|```bash
    68|python scripts/add_slide.py unpacked/ slide2.xml      # Duplicate slide
    69|python scripts/add_slide.py unpacked/ slideLayout2.xml # From layout
    70|```
    71|
    72|Prints `<p:sldId>` to add to `<p:sldIdLst>` at desired position.
    73|
    74|### clean.py
    75|
    76|```bash
    77|python scripts/clean.py unpacked/
    78|```
    79|
    80|Removes slides not in `<p:sldIdLst>`, unreferenced media, orphaned rels.
    81|
    82|### pack.py
    83|
    84|```bash
    85|python scripts/office/pack.py unpacked/ output.pptx --original input.pptx
    86|```
    87|
    88|Validates, repairs, condenses XML, re-encodes smart quotes.
    89|
    90|### thumbnail.py
    91|
    92|```bash
    93|python scripts/thumbnail.py input.pptx [output_prefix] [--cols N]
    94|```
    95|
    96|Creates `thumbnails.jpg` with slide filenames as labels. Default 3 columns, max 12 per grid.
    97|
    98|**Use for template analysis only** (choosing layouts). For visual QA, use `soffice` + `pdftoppm` to create full-resolution individual slide images—see SKILL.md.
    99|
   100|---
   101|
   102|## Slide Operations
   103|
   104|Slide order is in `ppt/presentation.xml` → `<p:sldIdLst>`.
   105|
   106|**Reorder**: Rearrange `<p:sldId>` elements.
   107|
   108|**Delete**: Remove `<p:sldId>`, then run `clean.py`.
   109|
   110|**Add**: Use `add_slide.py`. Never manually copy slide files—the script handles notes references, Content_Types.xml, and relationship IDs that manual copying misses.
   111|
   112|---
   113|
   114|## Editing Content
   115|
   116|**Subagents:** If available, use them here (after completing step 4). Each slide is a separate XML file, so subagents can edit in parallel. In your prompt to subagents, include:
   117|
   118|- The slide file path(s) to edit
   119|- **"Use the Edit tool for all changes"**
   120|- The formatting rules and common pitfalls below
   121|
   122|For each slide:
   123|
   124|1. Read the slide's XML
   125|2. Identify ALL placeholder content—text, images, charts, icons, captions
   126|3. Replace each placeholder with final content
   127|
   128|**Use the Edit tool, not sed or Python scripts.** The Edit tool forces specificity about what to replace and where, yielding better reliability.
   129|
   130|### Formatting Rules
   131|
   132|- **Bold all headers, subheadings, and inline labels**: Use `b="1"` on `<a:rPr>`. This includes:
   133|  - Slide titles
   134|  - Section headers within a slide
   135|  - Inline labels like (e.g.: "Status:", "Description:") at the start of a line
   136|- **Never use unicode bullets (•)**: Use proper list formatting with `<a:buChar>` or `<a:buAutoNum>`
   137|- **Bullet consistency**: Let bullets inherit from the layout. Only specify `<a:buChar>` or `<a:buNone>`.
   138|
   139|---
   140|
   141|## Common Pitfalls
   142|
   143|### Template Adaptation
   144|
   145|When source content has fewer items than the template:
   146|
   147|- **Remove excess elements entirely** (images, shapes, text boxes), don't just clear text
   148|- Check for orphaned visuals after clearing text content
   149|- Run visual QA to catch mismatched counts
   150|
   151|When replacing text with different length content:
   152|
   153|- **Shorter replacements**: Usually safe
   154|- **Longer replacements**: May overflow or wrap unexpectedly
   155|- Test with visual QA after text changes
   156|- Consider truncating or splitting content to fit the template's design constraints
   157|
   158|**Template slots ≠ Source items**: If template has 4 team members but source has 3 users, delete the 4th member's entire group (image + text boxes), not just the text.
   159|
   160|### Multi-Item Content
   161|
   162|If source has multiple items (numbered lists, multiple sections), create separate `<a:p>` elements for each — **never concatenate into one string**.
   163|
   164|**❌ WRONG** — all items in one paragraph:
   165|
   166|```xml
   167|<a:p>
   168|  <a:r><a:rPr .../><a:t>Step 1: Do the first thing. Step 2: Do the second thing.</a:t></a:r>
   169|</a:p>
   170|```
   171|
   172|**✅ CORRECT** — separate paragraphs with bold headers:
   173|
   174|```xml
   175|<a:p>
   176|  <a:pPr algn="l"><a:lnSpc><a:spcPts val="3919"/></a:lnSpc></a:pPr>
   177|  <a:r><a:rPr lang="en-US" sz="2799" b="1" .../><a:t>Step 1</a:t></a:r>
   178|</a:p>
   179|<a:p>
   180|  <a:pPr algn="l"><a:lnSpc><a:spcPts val="3919"/></a:lnSpc></a:pPr>
   181|  <a:r><a:rPr lang="en-US" sz="2799" .../><a:t>Do the first thing.</a:t></a:r>
   182|</a:p>
   183|<a:p>
   184|  <a:pPr algn="l"><a:lnSpc><a:spcPts val="3919"/></a:lnSpc></a:pPr>
   185|  <a:r><a:rPr lang="en-US" sz="2799" b="1" .../><a:t>Step 2</a:t></a:r>
   186|</a:p>
   187|<!-- continue pattern -->
   188|```
   189|
   190|Copy `<a:pPr>` from the original paragraph to preserve line spacing. Use `b="1"` on headers.
   191|
   192|### Smart Quotes
   193|
   194|Handled automatically by unpack/pack. But the Edit tool converts smart quotes to ASCII.
   195|
   196|**When adding new text with quotes, use XML entities:**
   197|
   198|```xml
   199|<a:t>the &#x201C;Agreement&#x201D;</a:t>
   200|```
   201|
   202|| Character | Name               | Unicode | XML Entity |
   203|| --------- | ------------------ | ------- | ---------- |
   204|| `“`       | Left double quote  | U+201C  | `&#x201C;` |
   205|| `”`       | Right double quote | U+201D  | `&#x201D;` |
   206|| `‘`       | Left single quote  | U+2018  | `&#x2018;` |
   207|| `’`       | Right single quote | U+2019  | `&#x2019;` |
   208|
   209|### Other
   210|
   211|- **Whitespace**: Use `xml:space="preserve"` on `<a:t>` with leading/trailing spaces
   212|- **XML parsing**: Use `defusedxml.minidom`, not `xml.etree.ElementTree` (corrupts namespaces)
   213|