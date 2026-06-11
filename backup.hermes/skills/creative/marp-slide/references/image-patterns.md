---
name: marp-slide-image-patterns
description: "Marp Image Syntax Reference"
version: 1.0.0
author: Alexa
---
     1|# Marp Image Syntax Reference
     2|
     3|Image placement and styling methods based on official Marpit image syntax.
     4|
     5|Official documentation: https://marpit.marp.app/image-syntax
     6|
     7|## Basic Image Insertion
     8|
     9|### Regular Images
    10|
    11|```markdown
    12|![](image.png) ![alt text](image.png)
    13|```
    14|
    15|Images are displayed as content.
    16|
    17|### Size Specification
    18|
    19|Marp allows adding size keywords to images:
    20|
    21|```markdown
    22|![width:600px](image.png) ![height:400px](image.png) ![w:600px h:400px](image.png)
    23|```
    24|
    25|**Supported units**:
    26|
    27|- `px` - Pixels
    28|- `%` - Percent
    29|- `em`, `rem`, `cm`, `mm`, `in`, `pt`, `pc`
    30|
    31|**Abbreviations**:
    32|
    33|- `w:` = `width:`
    34|- `h:` = `height:`
    35|
    36|## Background Images (`bg` keyword)
    37|
    38|### Basic Background Image
    39|
    40|```markdown
    41|![bg](image.png)
    42|```
    43|
    44|Places the image as a slide background. It doesn't overlap with text content and is positioned in the background.
    45|
    46|### Background Size Keywords
    47|
    48|```markdown
    49|![bg fit](image.png) ![bg cover](image.png) ![bg contain](image.png) ![bg auto](image.png)
    50|```
    51|
    52|| Keyword | Behavior | CSS Equivalent |
    53|| --- | --- | --- |
    54|| `fit` | Preserve aspect ratio, fit within slide | `background-size: contain` |
    55|| `cover` | Preserve aspect ratio, cover entire slide | `background-size: cover` |
    56|| `contain` | Same as `fit` | `background-size: contain` |
    57|| `auto` | Original size | `background-size: auto` |
    58|
    59|### Background Size (Numeric Values)
    60|
    61|```markdown
    62|![bg 80%](image.png) ![bg 1280px](image.png) ![bg 50% 80%](image.png)
    63|```
    64|
    65|Supports the same syntax as CSS `background-size` property.
    66|
    67|## Split Backgrounds
    68|
    69|You can split the screen using multiple background images.
    70|
    71|### Basic Split
    72|
    73|```markdown
    74|![bg](image1.png) ![bg](image2.png)
    75|```
    76|
    77|Two images are displayed split left and right.
    78|
    79|### Three or More Splits
    80|
    81|```markdown
    82|![bg](image1.png) ![bg](image2.png) ![bg](image3.png)
    83|```
    84|
    85|Three or more images are divided equally.
    86|
    87|### Specifying Split Direction
    88|
    89|Default is horizontal split, but vertical split is also possible:
    90|
    91|```markdown
    92|![bg vertical](image1.png) ![bg](image2.png)
    93|```
    94|
    95|Use `vertical` keyword to change to vertical split.
    96|
    97|### Left/Right Alignment
    98|
    99|```markdown
   100|![bg left](image.png)
   101|```
   102|
   103|Places image on the left, reserving text space on the right.
   104|
   105|```markdown
   106|![bg right](image.png)
   107|```
   108|
   109|Places image on the right, reserving text space on the left.
   110|
   111|### Size Ratio Specification
   112|
   113|```markdown
   114|![bg left:33%](image.png)
   115|```
   116|
   117|33% image on left, 67% text space on right.
   118|
   119|```markdown
   120|![bg right:60%](image.png)
   121|```
   122|
   123|60% image on right, 40% text space on left.
   124|
   125|## Filter Effects
   126|
   127|### Brightness Adjustment
   128|
   129|```markdown
   130|![brightness:0.5](image.png) ![brightness:1.5](image.png)
   131|```
   132|
   133|Value range: 0 (completely black) ~ 1 (normal) ~ 2+ (brighter)
   134|
   135|### Contrast
   136|
   137|```markdown
   138|![contrast:0.8](image.png) ![contrast:1.5](image.png)
   139|```
   140|
   141|### Blur
   142|
   143|```markdown
   144|![blur:10px](image.png)
   145|```
   146|
   147|### Grayscale
   148|
   149|```markdown
   150|![grayscale](image.png) ![grayscale:1](image.png)
   151|```
   152|
   153|Value range: 0 (color) ~ 1 (full grayscale)
   154|
   155|### Sepia
   156|
   157|```markdown
   158|![sepia](image.png) ![sepia:0.8](image.png)
   159|```
   160|
   161|### Hue Rotation
   162|
   163|```markdown
   164|![hue-rotate:180deg](image.png)
   165|```
   166|
   167|### Invert
   168|
   169|```markdown
   170|![invert](image.png) ![invert:0.8](image.png)
   171|```
   172|
   173|### Opacity
   174|
   175|```markdown
   176|![opacity:0.5](image.png)
   177|```
   178|
   179|### Saturation
   180|
   181|```markdown
   182|![saturate:2](image.png)
   183|```
   184|
   185|### Multiple Filters
   186|
   187|```markdown
   188|![brightness:1.2 contrast:1.1 saturate:1.3](image.png)
   189|```
   190|
   191|## Practical Pattern Examples
   192|
   193|### Pattern 1: Text on Left, Image on Right
   194|
   195|```markdown
   196|## Product Introduction
   197|
   198|![bg right:40%](product.png)
   199|
   200|- Feature 1
   201|- Feature 2
   202|- Feature 3
   203|```
   204|
   205|### Pattern 2: Background Image + Overlay Text
   206|
   207|```markdown
   208|![bg brightness:0.5](hero.png)
   209|
   210|# Catchphrase
   211|
   212|Subtext
   213|```
   214|
   215|White text placed on darkened background.
   216|
   217|### Pattern 3: Multiple Image Comparison
   218|
   219|```markdown
   220|![bg left:50%](before.png) ![bg right:50%](after.png)
   221|```
   222|
   223|Place Before/After side by side.
   224|
   225|### Pattern 4: Vertical Comparison
   226|
   227|```markdown
   228|![bg vertical](image1.png) ![bg](image2.png)
   229|```
   230|
   231|Place images top and bottom.
   232|
   233|### Pattern 5: Sized Regular Image
   234|
   235|```markdown
   236|## Diagram
   237|
   238|![w:600px](diagram.png)
   239|
   240|The above diagram shows...
   241|```
   242|
   243|### Pattern 6: 3-Split Layout
   244|
   245|```markdown
   246|![bg](image1.png) ![bg](image2.png) ![bg](image3.png)
   247|```
   248|
   249|### Pattern 7: Background with Filter Effects
   250|
   251|```markdown
   252|![bg blur:5px brightness:0.7](background.png)
   253|
   254|# Easy-to-Read Text
   255|
   256|Subdued background with blur and darkness
   257|```
   258|
   259|## Important Notes
   260|
   261|1. **Background Images and Text**: `![bg]` images are placed on the background layer and do not overlap with text
   262|2. **Multiple Background Order**: They are placed from left to right (or top to bottom) in the order written
   263|3. **Filter Support**: Not all filters work in all environments
   264|4. **Relative Paths**: Image paths are specified relative to the Markdown file
   265|
   266|## Official Reference
   267|
   268|For details, refer to official documentation:
   269|
   270|- **Image syntax**: https://marpit.marp.app/image-syntax
   271|