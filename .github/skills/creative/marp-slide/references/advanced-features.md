---
name: marp-slide-advanced-features
description: "Marp Advanced Features Reference"
version: 1.0.0
author: Alexa
---
     1|# Marp Advanced Features Reference
     2|
     3|Advanced features of Marp Core and Marpit.
     4|
     5|## Fragmented List (Progressive Display)
     6|
     7|Feature to display list items progressively (animation effect).
     8|
     9|Official documentation: https://github.com/marp-team/marpit/tree/main/docs/fragmented-list
    10|
    11|### Basic Usage
    12|
    13|```markdown
    14|- Item 1
    15|- Item 2
    16|- Item 3
    17|```
    18|
    19|Normally, all items are displayed at once.
    20|
    21|### Using Asterisks (\*)
    22|
    23|```markdown
    24|- Item 1
    25|- Item 2
    26|- Item 3
    27|```
    28|
    29|When using `--html` option with Marp CLI, each item displays sequentially.
    30|
    31|### Important Notes
    32|
    33|- **Only effective in HTML output**: No effect in PDF/PPTX/images
    34|- **Presentation mode**: Works during browser presentations
    35|- **Marp for VS Code**: May not work in preview
    36|
    37|## Math Notation (Marp Core Extension)
    38|
    39|Supports Pandoc-style math formulas. Rendered using KaTeX.
    40|
    41|Official: https://github.com/marp-team/marp-core#math-typesetting
    42|
    43|### Inline Math
    44|
    45|```markdown
    46|Insert $E = mc^2$ in text
    47|```
    48|
    49|### Block Math
    50|
    51|```markdown
    52|$$
    53|\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}
    54|$$
    55|```
    56|
    57|### Multi-line Math
    58|
    59|```markdown
    60|$$
    61|\begin{aligned}
    62|  f(x) &= x^2 + 2x + 1 \\
    63|  &= (x + 1)^2
    64|\end{aligned}
    65|$$
    66|```
    67|
    68|### Math Examples
    69|
    70|```markdown
    71|## Quadratic Formula
    72|
    73|$$
    74|x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
    75|$$
    76|
    77|## Euler's Identity
    78|
    79|$$
    80|e^{i\pi} + 1 = 0
    81|$$
    82|```
    83|
    84|### Important Notes
    85|
    86|- **KaTeX notation**: Subset of LaTeX syntax
    87|- **Unsupported notation**: Some LaTeX features not supported
    88|- **KaTeX official**: https://katex.org/docs/supported.html
    89|
    90|## Emoji (Marp Core Extension)
    91|
    92|Supports GitHub Emoji notation.
    93|
    94|Official: https://github.com/marp-team/marp-core#emoji
    95|
    96|### Usage
    97|
    98|```markdown
    99|:smile: :heart: :+1: :sparkles:
   100|```
   101|
   102|Rendered result: 😄 ❤️ 👍 ✨
   103|
   104|### Common Emoji
   105|
   106|```markdown
   107|:arrow_right: → :check: ✓ :x: ✗ :bulb: 💡 :warning: ⚠️ :rocket: 🚀 :tada: 🎉
   108|```
   109|
   110|### Emoji List
   111|
   112|Complete list: https://github.com/ikatyang/emoji-cheat-sheet
   113|
   114|## Auto-scaling
   115|
   116|Automatically adjusts font size when there's too much text.
   117|
   118|### Disable
   119|
   120|```markdown
   121|---
   122|marp: true
   123|---
   124|
   125|<!-- _class: no-scaling -->
   126|
   127|# No auto-scaling
   128|```
   129|
   130|Control with custom CSS:
   131|
   132|```css
   133|section.no-scaling {
   134|  --marpit-auto-scaling: off;
   135|}
   136|```
   137|
   138|## Using HTML Tags
   139|
   140|You can write HTML directly in Markdown.
   141|
   142|### Alignment Control
   143|
   144|```markdown
   145|<div style="text-align: center;">
   146|Centered text
   147|</div>
   148|```
   149|
   150|### Two-Column Layout
   151|
   152|```markdown
   153|<div style="display: flex;">
   154|<div style="flex: 1;">
   155|
   156|## Left Side
   157|
   158|- Point 1
   159|- Point 2
   160|
   161|</div>
   162|<div style="flex: 1;">
   163|
   164|## Right Side
   165|
   166|- Point 3
   167|- Point 4
   168|
   169|</div>
   170|</div>
   171|```
   172|
   173|### Styled Box
   174|
   175|```markdown
   176|<div style="background-color: #e3f2fd; padding: 20px; border-radius: 8px;">
   177|
   178|**Important Point**
   179|
   180|Important content goes here
   181|
   182|</div>
   183|```
   184|
   185|## Marp CLI Detailed Options
   186|
   187|Official: https://github.com/marp-team/marp-cli
   188|
   189|### Basic Commands
   190|
   191|```bash
   192|# Convert to HTML
   193|marp slide.md
   194|
   195|# Convert to PDF
   196|marp slide.md --pdf
   197|
   198|# Convert to PowerPoint
   199|marp slide.md --pptx
   200|
   201|# Convert to image
   202|marp slide.md --images png
   203|```
   204|
   205|### Watch Mode
   206|
   207|```bash
   208|# Watch file and auto-convert
   209|marp -w slide.md
   210|
   211|# Watch in server mode
   212|marp -s -w slide.md
   213|```
   214|
   215|### Specify Theme
   216|
   217|```bash
   218|# Use custom theme
   219|marp slide.md --theme custom-theme.css
   220|
   221|# Specify theme directory
   222|marp slide.md --theme-set themes/
   223|```
   224|
   225|### Batch Convert Multiple Files
   226|
   227|```bash
   228|# Convert all Markdown in directory
   229|marp slides/*.md
   230|
   231|# Specify output directory
   232|marp slides/*.md -o output/
   233|```
   234|
   235|### HTML Output Options
   236|
   237|```bash
   238|# HTML output (single file)
   239|marp slide.md -o output.html
   240|
   241|# Standalone HTML (using CDN)
   242|marp slide.md --html
   243|```
   244|
   245|### PDF Output Options
   246|
   247|```bash
   248|# PDF output
   249|marp slide.md --pdf --allow-local-files
   250|
   251|# PDF without page numbers
   252|marp slide.md --pdf --pdf-notes
   253|```
   254|
   255|### Image Output
   256|
   257|```bash
   258|# Output as PNG images
   259|marp slide.md --images png
   260|
   261|# Output as JPEG images
   262|marp slide.md --images jpeg
   263|
   264|# Specify resolution
   265|marp slide.md --images png --image-scale 2
   266|```
   267|
   268|## Marp for VS Code
   269|
   270|Official: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode
   271|
   272|### Enable
   273|
   274|Write in Markdown file front matter:
   275|
   276|```markdown
   277|---
   278|marp: true
   279|---
   280|```
   281|
   282|### Preview
   283|
   284|- `Ctrl+Shift+V` (Win/Linux)
   285|- `Cmd+Shift+V` (Mac)
   286|
   287|### Export
   288|
   289|1. Command Palette (`Ctrl+Shift+P`)
   290|2. Select "Marp: Export slide deck..."
   291|3. Choose format (HTML/PDF/PPTX/PNG/JPEG)
   292|
   293|### Settings
   294|
   295|Customizable in VS Code settings:
   296|
   297|```json
   298|{
   299|  "markdown.marp.enableHtml": true,
   300|  "markdown.marp.themes": ["./themes/custom-theme.css"]
   301|}
   302|```
   303|
   304|## Automated Build with GitHub Actions
   305|
   306|Official: https://github.com/marketplace/actions/marp-action
   307|
   308|### Basic Workflow
   309|
   310|```yaml
   311|name: Marp Build
   312|
   313|on:
   314|  push:
   315|    branches: [main]
   316|
   317|jobs:
   318|  build:
   319|    runs-on: ubuntu-latest
   320|    steps:
   321|      - uses: actions/checkout@v3
   322|
   323|      - name: Marp Build
   324|        uses: docker://marpteam/marp-cli:latest
   325|        with:
   326|          args: slides.md --pdf --allow-local-files
   327|
   328|      - name: Upload PDF
   329|        uses: actions/upload-artifact@v3
   330|        with:
   331|          name: slides
   332|          path: slides.pdf
   333|```
   334|
   335|### Publish to GitHub Pages
   336|
   337|```yaml
   338|- name: Marp to Pages
   339|  uses: docker://marpteam/marp-cli:latest
   340|  with:
   341|    args: slides.md -o index.html
   342|
   343|- name: Deploy to Pages
   344|  uses: peaceiris/actions-gh-pages@v3
   345|  with:
   346|    github_token: ${{ secrets.GITHUB_TOKEN }}
   347|    publish_dir: ./
   348|```
   349|
   350|## Tips & Tricks
   351|
   352|### 1. Customize Slide Numbers
   353|
   354|```css
   355|section::after {
   356|  content: "Page " attr(data-marpit-pagination);
   357|}
   358|```
   359|
   360|### 2. Gradient Background
   361|
   362|```markdown
   363|---
   364|backgroundImage: linear-gradient(135deg, #667eea 0%, #764ba2 100%)
   365|color: white
   366|---
   367|```
   368|
   369|### 3. Two-Column Layout
   370|
   371|```markdown
   372|<div class="columns">
   373|<div>
   374|
   375|Left side content
   376|
   377|</div>
   378|<div>
   379|
   380|Right side content
   381|
   382|</div>
   383|</div>
   384|
   385|<style>
   386|.columns {
   387|  display: grid;
   388|  grid-template-columns: 1fr 1fr;
   389|  gap: 2rem;
   390|}
   391|</style>
   392|```
   393|
   394|### 4. Progress Bar
   395|
   396|```css
   397|section::before {
   398|  content: "";
   399|  position: absolute;
   400|  top: 0;
   401|  left: 0;
   402|  width: calc(var(--paginate) / var(--paginate-total) * 100%);
   403|  height: 5px;
   404|  background-color: #3b82f6;
   405|}
   406|```
   407|
   408|## Troubleshooting
   409|
   410|### PDF Not Generated
   411|
   412|- Check if Chrome or Edge is installed
   413|- Add `--allow-local-files` option
   414|
   415|### Fonts Not Displaying
   416|
   417|- Load Google Fonts with `@import`
   418|- Specify local fonts with absolute path
   419|
   420|### Images Not Displaying
   421|
   422|- Check image relative paths
   423|- May need `--allow-local-files`
   424|
   425|## Official References
   426|
   427|- **Marp Official Site**: https://marp.app/
   428|- **Marpit Directives**: https://marpit.marp.app/directives
   429|- **Image Syntax**: https://marpit.marp.app/image-syntax
   430|- **Theme CSS**: https://marpit.marp.app/theme-css
   431|- **Marp Core**: https://github.com/marp-team/marp-core
   432|- **Marp CLI**: https://github.com/marp-team/marp-cli
   433|- **VS Code Extension**: https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode
   434|