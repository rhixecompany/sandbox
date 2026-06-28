---
name: marp-slide-best-practices
description: "Marp Slide Creation Best Practices"
version: 1.0.0
author: Alexa
---
     1|# Marp Slide Creation Best Practices
     2|
     3|Guidelines for creating "cool" high-quality slides.
     4|
     5|## Slide Titles (h2)
     6|
     7|### ✅ Good Examples
     8|
     9|- **Concise**: About 5-7 characters
    10|- **Clear**: Content is immediately understandable
    11|- **Consistent**: Use the same style at the same hierarchy level
    12|
    13|```markdown
    14|## Introduction
    15|
    16|## Problem
    17|
    18|## Solution
    19|
    20|## Results
    21|```
    22|
    23|### ❌ Bad Examples
    24|
    25|```markdown
    26|## In this section we will explain the introduction
    27|
    28|## What are the challenges we are facing
    29|```
    30|
    31|## Bullet Points
    32|
    33|### ✅ Good Examples
    34|
    35|- **3-5 items**: Not too many
    36|- **Concise**: About 15-25 characters per line
    37|- **Parallel**: Same grammatical structure at the same level
    38|
    39|```markdown
    40|- Simple and easy to understand
    41|- Unified design
    42|- Effective information delivery
    43|```
    44|
    45|### ❌ Bad Examples
    46|
    47|```markdown
    48|- This is a very long explanation that doesn't fit on one line and becomes difficult to read
    49|- Short
    50|- The next item is in sentence format. This lack of uniformity makes it hard to read.
    51|```
    52|
    53|## Slide Structure
    54|
    55|### Basic Structure
    56|
    57|1. **Title Slide** (`<!-- _class: lead -->`)
    58|   - Title
    59|   - Presenter name
    60|   - Date
    61|
    62|2. **Agenda Slide**
    63|   - Show overall flow
    64|   - About 3-5 items
    65|
    66|3. **Content Slides**
    67|   - 1 slide = 1 message
    68|   - Title summarizes content
    69|
    70|4. **Summary Slide**
    71|   - Reconfirm key points
    72|   - Words of thanks
    73|
    74|### Recommended Slide Count
    75|
    76|- 5-minute presentation: 5-8 slides
    77|- 10-minute presentation: 10-15 slides
    78|- 20-minute presentation: 15-25 slides
    79|
    80|## Text Amount
    81|
    82|### ✅ Good Balance
    83|
    84|```markdown
    85|## Product Features
    86|
    87|- High-speed processing
    88|- Intuitive UI
    89|- Highly extensible design
    90|```
    91|
    92|### ❌ Too Crowded
    93|
    94|```markdown
    95|## About the Product
    96|
    97|This product was developed using the latest technology. The main features include the following 7 points:
    98|
    99|- Feature 1: Detailed explanation continues at length...
   100|- Feature 2: Even more detailed explanation... (Continued)
   101|```
   102|
   103|## Using Whitespace
   104|
   105|- **Adequate whitespace**: Don't cram too much information
   106|- **Visual guidance**: Layout that naturally draws eyes to important information
   107|- **Breathing room**: Appropriate "pauses" between slides
   108|
   109|## Using Colors
   110|
   111|Leverage colors defined in the theme:
   112|
   113|- **Background color**: `#f8f8f4` (light beige)
   114|- **Text color**: `#3a3b5a` (dark navy)
   115|- **Heading color**: `#4f86c6` (blue)
   116|- **Accent color**: `#000000` (black)
   117|
   118|### When Using Additional Colors
   119|
   120|```markdown
   121|<span style="color: #c62828;">Important point</span>
   122|```
   123|
   124|Use sparingly and avoid excessive decoration.
   125|
   126|## Using Images
   127|
   128|### Effective Usage
   129|
   130|- **Clear purpose**: To aid understanding, not just decoration
   131|- **High quality**: Use high-resolution images
   132|- **Appropriate size**: Neither too large nor too small
   133|
   134|### Layout Tips
   135|
   136|```markdown
   137|# Text on left, image on right
   138|
   139|![bg right:40%](image.png)
   140|
   141|- Point 1
   142|- Point 2
   143|```
   144|
   145|## Font Size Guidelines
   146|
   147|Defined in the theme:
   148|
   149|- h1: 56px (title slide only)
   150|- h2: 40px (regular slide titles)
   151|- h3: 28px (subheadings)
   152|- Body text: 22px
   153|
   154|## Animations and Transitions
   155|
   156|Marp does not support animations by default. Focus on simple slide transitions.
   157|
   158|## Checklist
   159|
   160|After completing slides, verify:
   161|
   162|- [ ] Are titles concise (5-7 characters)?
   163|- [ ] Are bullet points 3-5 items?
   164|- [ ] Is it 1 slide = 1 message?
   165|- [ ] Is the text amount appropriate?
   166|- [ ] Is there sufficient whitespace?
   167|- [ ] Are images used effectively?
   168|- [ ] Is there overall consistency?
   169|- [ ] Is the slide count appropriate?
   170|