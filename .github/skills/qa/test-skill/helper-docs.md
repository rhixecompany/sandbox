---
name: test-skill-helper-docs
description: "Helper Documentation"
version: 1.0.0
author: Alexa
---
     1|# Helper Documentation
     2|
     3|This file tests the `read_skill_file` tool with markdown content.
     4|
     5|## Purpose
     6|
     7|When you load this file using `read_skill_file`, it should:
     8|
     9|1. Be injected into context via `noReply` + `synthetic: true`
    10|2. Be wrapped in `<skill-file>` XML tags
    11|3. Include metadata about the skill directory
    12|
    13|## Sample Content
    14|
    15|Here's some sample content to verify the file loaded correctly:
    16|
    17|- Item 1: Testing list rendering
    18|- Item 2: More list items
    19|- Item 3: Even more items
    20|
    21|### Code Example
    22|
    23|```python
    24|def hello():
    25|    print("Hello from helper-docs.md!")
    26|```
    27|
    28|## Verification
    29|
    30|If you can see this content, `read_skill_file` is working correctly!
    31|