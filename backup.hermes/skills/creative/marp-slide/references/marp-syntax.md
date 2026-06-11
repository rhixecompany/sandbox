---
name: marp-slide-marp-syntax
description: "Marp Basic Syntax Reference"
version: 1.0.0
author: Alexa
---
     1|# Marp Basic Syntax Reference
     2|
     3|Basic Marp syntax based on official documentation.
     4|
     5|## Front Matter (Directives)
     6|
     7|### Basic Structure
     8|
     9|```markdown
    10|---
    11|marp: true
    12|theme: default
    13|paginate: true
    14|---
    15|```
    16|
    17|### Main Global Directives
    18|
    19|| Directive | Description | Example Values |
    20|| --- | --- | --- |
    21|| `marp` | Enable Marp functionality | `true` |
    22|| `theme` | Specify theme | `default`, `gaia`, `uncover` |
    23|| `size` | Slide size (Marp Core extension) | `16:9`, `4:3`, `A4` |
    24|| `paginate` | Show page numbers | `true`, `false` |
    25|| `header` | Header for all slides | Any text |
    26|| `footer` | Footer for all slides | Any text |
    27|| `backgroundColor` | Background color | `#fff`, `white` |
    28|| `backgroundImage` | Background image | `url('image.png')` |
    29|| `color` | Text color | `#000`, `black` |
    30|| `class` | Apply CSS class | `lead`, `invert` |
    31|
    32|### Size Directive (Marp Core)
    33|
    34|```markdown
    35|---
    36|size: 16:9
    37|---
    38|```
    39|
    40|Available sizes:
    41|
    42|- `16:9` (1280x720, default)
    43|- `4:3` (960x720)
    44|- `A4` (210mm x 297mm)
    45|
    46|### Page-Specific Directives
    47|
    48|To change settings per slide, use `<!-- directive_name: value -->` format:
    49|
    50|```markdown
    51|<!-- _class: lead -->
    52|<!-- _backgroundColor: black -->
    53|<!-- _color: white -->
    54|
    55|# Apply only to this slide
    56|```
    57|
    58|**Meaning of underscore `_`**:
    59|
    60|- Without `_`: Apply to all following slides
    61|- With `_`: Apply to current slide only
    62|
    63|## Slide Breaks
    64|
    65|```markdown
    66|---
    67|# First Slide
    68|---
    69|
    70|# Next Slide
    71|
    72|---
    73|```
    74|
    75|`---` (horizontal rule) switches to a new slide.
    76|
    77|## Headers and Footers
    78|
    79|### Global Settings
    80|
    81|```markdown
    82|---
    83|header: "Lecture Name"
    84|footer: "October 2024"
    85|---
    86|```
    87|
    88|### Per-Slide Settings
    89|
    90|```markdown
    91|<!-- header: 'Section 1' -->
    92|<!-- footer: 'Page number display' -->
    93|```
    94|
    95|### Disable
    96|
    97|```markdown
    98|<!-- header: '' -->
    99|<!-- footer: '' -->
   100|```
   101|
   102|## Pagination (Page Numbers)
   103|
   104|```markdown
   105|---
   106|paginate: true
   107|---
   108|```
   109|
   110|Display position and style vary by theme.
   111|
   112|Hide on specific slide:
   113|
   114|```markdown
   115|<!-- paginate: false -->
   116|```
   117|
   118|Or:
   119|
   120|```markdown
   121|<!-- _paginate: false -->
   122|```
   123|
   124|## Inline Styles
   125|
   126|### Style Specification in Markdown
   127|
   128|```markdown
   129|---
   130|marp: true
   131|---
   132|
   133|<style>
   134|section {
   135|  background-color: #f0f0f0;
   136|}
   137|
   138|h1 {
   139|  color: #333;
   140|}
   141|</style>
   142|
   143|# Slide
   144|```
   145|
   146|### Scoped Style
   147|
   148|Apply style to specific slide only:
   149|
   150|```markdown
   151|<style scoped>
   152|h1 {
   153|  color: red;
   154|}
   155|</style>
   156|
   157|# Red heading on this slide only
   158|```
   159|
   160|## Math Formulas (Marp Core Extension)
   161|
   162|Supports Pandoc-style math formulas:
   163|
   164|### Inline Math
   165|
   166|```markdown
   167|$E = mc^2$
   168|```
   169|
   170|### Block Math
   171|
   172|```markdown
   173|$$
   174|\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
   175|$$
   176|```
   177|
   178|## Emoji (Marp Core Extension)
   179|
   180|```markdown
   181|:smile: :+1: :sparkles:
   182|```
   183|
   184|Supports GitHub Emoji notation.
   185|
   186|## Comments
   187|
   188|HTML comments are not rendered:
   189|
   190|```markdown
   191|<!-- This is a comment -->
   192|```
   193|
   194|Directives are also written in comment format:
   195|
   196|```markdown
   197|<!-- _class: lead -->
   198|```
   199|
   200|## Official Reference Links
   201|
   202|For details, refer to official documentation:
   203|
   204|- **Directives List**: https://marpit.marp.app/directives
   205|- **Marp Core Features**: https://github.com/marp-team/marp-core
   206|- **Theme CSS Specification**: https://marpit.marp.app/theme-css
   207|- **Official Site**: https://marp.app/
   208|
   209|## Common Configuration Examples
   210|
   211|### Basic Setup
   212|
   213|```markdown
   214|---
   215|marp: true
   216|theme: default
   217|size: 16:9
   218|paginate: true
   219|---
   220|```
   221|
   222|### Title Slide
   223|
   224|```markdown
   225|---
   226|marp: true
   227|theme: default
   228|---
   229|
   230|<!-- _class: lead -->
   231|<!-- _paginate: false -->
   232|
   233|# Presentation Title
   234|
   235|Presenter Name
   236|```
   237|
   238|### Section Breaks
   239|
   240|```markdown
   241|<!-- _class: lead -->
   242|
   243|# Chapter 2
   244|
   245|New Section
   246|
   247|---
   248|
   249|## Regular Slide
   250|```
   251|
   252|### Custom Background Color
   253|
   254|```markdown
   255|<!-- _backgroundColor: #e3f2fd -->
   256|
   257|# Slide with Light Blue Background
   258|```
   259|