---
name: marp-slide-official-themes
description: "Marp Official Themes Reference"
version: 1.0.0
author: Alexa
---
     1|# Marp Official Themes Reference
     2|
     3|Explanation of the 3 official themes included in Marp Core.
     4|
     5|Official implementation: https://github.com/marp-team/marp-core/tree/main/themes
     6|
     7|## Official Theme List
     8|
     9|1. **default** - Simple and versatile theme
    10|2. **gaia** - Modern and colorful theme
    11|3. **uncover** - Minimal and elegant theme
    12|
    13|## Default Theme
    14|
    15|### Features
    16|
    17|- **Colors**: White background, black text, blue accent
    18|- **Font**: Simple sans-serif
    19|- **Use for**: General presentations
    20|- **Style**: Clean, readable
    21|
    22|### Usage
    23|
    24|```markdown
    25|---
    26|marp: true
    27|theme: default
    28|---
    29|
    30|# Title
    31|
    32|Content
    33|```
    34|
    35|### Available Classes
    36|
    37|#### lead (Title Slide)
    38|
    39|```markdown
    40|<!-- _class: lead -->
    41|
    42|# Presentation
    43|
    44|Subtitle or description
    45|```
    46|
    47|Centered, large text.
    48|
    49|#### invert (Inverted Colors)
    50|
    51|```markdown
    52|<!-- _class: invert -->
    53|
    54|# Black Background · White Text
    55|```
    56|
    57|Background becomes black, text becomes white.
    58|
    59|#### Combined
    60|
    61|```markdown
    62|<!-- _class: lead invert -->
    63|
    64|# Inverted Title Slide
    65|```
    66|
    67|Multiple classes can be applied simultaneously.
    68|
    69|### Customization Example
    70|
    71|```markdown
    72|---
    73|theme: default
    74|---
    75|
    76|<style>
    77|section {
    78|  background-color: #f5f5f5;
    79|}
    80|
    81|h1 {
    82|  color: #1e40af;
    83|}
    84|</style>
    85|```
    86|
    87|## Gaia Theme
    88|
    89|### Features
    90|
    91|- **Colors**: Colorful, vibrant accent colors
    92|- **Font**: Modern sans-serif
    93|- **Use for**: Creative presentations, design showcases
    94|- **Style**: Energetic, visually appealing
    95|
    96|### Usage
    97|
    98|```markdown
    99|---
   100|marp: true
   101|theme: gaia
   102|---
   103|
   104|# Title
   105|```
   106|
   107|### Color Variations
   108|
   109|The Gaia theme has multiple color schemes:
   110|
   111|```markdown
   112|<!-- _class: lead -->
   113|
   114|# Default Colors
   115|
   116|---
   117|
   118|<!-- _class: lead invert -->
   119|
   120|# Inverted Colors
   121|
   122|---
   123|
   124|<!-- _class: lead gaia -->
   125|
   126|# Gaia Colors
   127|```
   128|
   129|### Distinctive Styles
   130|
   131|- **Gradient backgrounds**: Used in title slides
   132|- **Colorful accents**: Headings and links
   133|- **Large typography**: Impactful headings
   134|
   135|### Customization Example
   136|
   137|```markdown
   138|---
   139|theme: gaia
   140|---
   141|
   142|<style>
   143|section {
   144|  --color-background: #fff;
   145|  --color-foreground: #333;
   146|  --color-highlight: #e91e63;
   147|}
   148|</style>
   149|```
   150|
   151|## Uncover Theme
   152|
   153|### Features
   154|
   155|- **Colors**: Minimal, white or black base
   156|- **Font**: Elegant serif font
   157|- **Use for**: Formal presentations, academic talks
   158|- **Style**: Refined, simple, elegant
   159|
   160|### Usage
   161|
   162|```markdown
   163|---
   164|marp: true
   165|theme: uncover
   166|---
   167|
   168|# Title
   169|```
   170|
   171|### Available Classes
   172|
   173|#### lead (Title Slide)
   174|
   175|```markdown
   176|<!-- _class: lead -->
   177|
   178|# Presentation
   179|```
   180|
   181|Centered, large serif font.
   182|
   183|#### invert (Inverted Colors)
   184|
   185|```markdown
   186|<!-- _class: invert -->
   187|
   188|# Black Background Slide
   189|```
   190|
   191|Black background, white text.
   192|
   193|### Distinctive Styles
   194|
   195|- **Serif font**: Used for headings
   196|- **Wide margins**: Minimal layout
   197|- **Center alignment**: Content tends to be centered
   198|
   199|### Customization Example
   200|
   201|```markdown
   202|---
   203|theme: uncover
   204|---
   205|
   206|<style>
   207|section {
   208|  font-family: 'Georgia', serif;
   209|  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
   210|  color: white;
   211|}
   212|</style>
   213|```
   214|
   215|## Theme Comparison Table
   216|
   217|| Feature        | default    | gaia       | uncover     |
   218|| -------------- | ---------- | ---------- | ----------- |
   219|| **Background** | White      | Colorful   | White/Black |
   220|| **Font**       | Sans-serif | Sans-serif | Serif       |
   221|| **Colors**     | Simple     | Vibrant    | Minimal     |
   222|| **Use Case**   | General    | Creative   | Formal      |
   223|| **Style**      | Clean      | Energetic  | Elegant     |
   224|
   225|## Common Class Specifications
   226|
   227|Available in all official themes:
   228|
   229|### lead
   230|
   231|```markdown
   232|<!-- _class: lead -->
   233|```
   234|
   235|- For title slides
   236|- Centered
   237|- Large text
   238|- Hides footer/page numbers
   239|
   240|### invert
   241|
   242|```markdown
   243|<!-- _class: invert -->
   244|```
   245|
   246|- Inverts colors
   247|- Swaps background and text colors
   248|- Dark mode style
   249|
   250|## Theme Selection Guidelines
   251|
   252|### When to Choose default
   253|
   254|- General presentations
   255|- Business use
   256|- Need simple, readable design
   257|- As a base for customization
   258|
   259|### When to Choose gaia
   260|
   261|- Creative presentations
   262|- Design-related talks
   263|- Youth-oriented audiences
   264|- Need visual impact
   265|
   266|### When to Choose uncover
   267|
   268|- Formal presentations
   269|- Academic talks
   270|- Minimal design preference
   271|- Want elegant impression
   272|
   273|## Combining with Custom Themes
   274|
   275|### Extending Official Themes
   276|
   277|```css
   278|/* @theme my-custom-default */
   279|
   280|@import-theme 'default';
   281|
   282|section {
   283|  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
   284|}
   285|
   286|h1 {
   287|  color: #1e3a8a;
   288|}
   289|```
   290|
   291|### Switching Between Multiple Themes
   292|
   293|```markdown
   294|---
   295|marp: true
   296|theme: default
   297|---
   298|
   299|# Section 1 (default theme)
   300|
   301|---
   302|
   303|<!-- theme: gaia -->
   304|
   305|# Section 2 (gaia theme)
   306|
   307|---
   308|
   309|<!-- theme: uncover -->
   310|
   311|# Section 3 (uncover theme)
   312|```
   313|
   314|Note: Theme switching within the same file has limited support.
   315|
   316|## Practical Examples
   317|
   318|### Using default Theme
   319|
   320|```markdown
   321|---
   322|marp: true
   323|theme: default
   324|paginate: true
   325|---
   326|
   327|<!-- _class: lead -->
   328|
   329|# Project Report
   330|
   331|October 2024
   332|
   333|---
   334|
   335|## Agenda
   336|
   337|1. Progress Status
   338|2. Challenges and Solutions
   339|3. Future Plans
   340|
   341|---
   342|
   343|## Progress Status
   344|
   345|- Task A: Completed
   346|- Task B: In Progress
   347|- Task C: On Schedule
   348|```
   349|
   350|### Using gaia Theme
   351|
   352|```markdown
   353|---
   354|marp: true
   355|theme: gaia
   356|---
   357|
   358|<!-- _class: lead -->
   359|
   360|# New Product Launch
   361|
   362|Innovative Design
   363|
   364|---
   365|
   366|## Concept
   367|
   368|**Three Pillars**
   369|
   370|1. 🎨 Beauty
   371|2. 🚀 Speed
   372|3. 💡 Usability
   373|```
   374|
   375|### Using uncover Theme
   376|
   377|```markdown
   378|---
   379|marp: true
   380|theme: uncover
   381|---
   382|
   383|<!-- _class: lead -->
   384|
   385|# Research Presentation
   386|
   387|Deep Learning Applications
   388|
   389|---
   390|
   391|## Research Background
   392|
   393|Recent technological advances...
   394|
   395|---
   396|
   397|<!-- _class: invert -->
   398|
   399|## Experimental Results
   400|
   401|Accuracy: 95.3%
   402|```
   403|
   404|## Official References
   405|
   406|- **Official Theme Implementation**: https://github.com/marp-team/marp-core/tree/main/themes
   407|- **Marp Core README**: https://github.com/marp-team/marp-core
   408|- **Theme CSS Specification**: https://marpit.marp.app/theme-css
   409|