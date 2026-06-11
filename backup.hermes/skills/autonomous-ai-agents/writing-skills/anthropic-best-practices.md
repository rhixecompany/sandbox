---
name: writing-skills-anthropic-best-practices
description: "Skill authoring best practices"
version: 1.0.0
author: Alexa
---
     1|# Skill authoring best practices
     2|
     3|> Learn how to write effective Skills that Claude can discover and use successfully.
     4|
     5|Good Skills are concise, well-structured, and tested with real usage. This guide provides practical authoring decisions to help you write Skills that Claude can discover and use effectively.
     6|
     7|For conceptual background on how Skills work, see the [Skills overview](/en/docs/agents-and-tools/agent-skills/overview).
     8|
     9|## Core principles
    10|
    11|### Concise is key
    12|
    13|The [context window](https://platform.claude.com/docs/en/build-with-claude/context-windows) is a public good. Your Skill shares the context window with everything else Claude needs to know, including:
    14|
    15|- The system prompt
    16|- Conversation history
    17|- Other Skills' metadata
    18|- Your actual request
    19|
    20|Not every token in your Skill has an immediate cost. At startup, only the metadata (name and description) from all Skills is pre-loaded. Claude reads SKILL.md only when the Skill becomes relevant, and reads additional files only as needed. However, being concise in SKILL.md still matters: once Claude loads it, every token competes with conversation history and other context.
    21|
    22|**Default assumption**: Claude is already very smart
    23|
    24|Only add context Claude doesn't already have. Challenge each piece of information:
    25|
    26|- "Does Claude really need this explanation?"
    27|- "Can I assume Claude knows this?"
    28|- "Does this paragraph justify its token cost?"
    29|
    30|**Good example: Concise** (approximately 50 tokens):
    31|
    32|````markdown theme={null}
    33|## Extract PDF text
    34|
    35|Use pdfplumber for text extraction:
    36|
    37|```python
    38|import pdfplumber
    39|
    40|with pdfplumber.open("file.pdf") as pdf:
    41|    text = pdf.pages[0].extract_text()
    42|```
    43|````
    44|
    45|**Bad example: Too verbose** (approximately 150 tokens):
    46|
    47|```markdown theme={null}
    48|## Extract PDF text
    49|
    50|PDF (Portable Document Format) files are a common file format that contains text, images, and other content. To extract text from a PDF, you'll need to use a library. There are many libraries available for PDF processing, but we recommend pdfplumber because it's easy to use and handles most cases well. First, you'll need to install it using pip. Then you can use the code below...
    51|```
    52|
    53|The concise version assumes Claude knows what PDFs are and how libraries work.
    54|
    55|### Set appropriate degrees of freedom
    56|
    57|Match the level of specificity to the task's fragility and variability.
    58|
    59|**High freedom** (text-based instructions):
    60|
    61|Use when:
    62|
    63|- Multiple approaches are valid
    64|- Decisions depend on context
    65|- Heuristics guide the approach
    66|
    67|Example:
    68|
    69|```markdown theme={null}
    70|## Code review process
    71|
    72|1. Analyze the code structure and organization
    73|2. Check for potential bugs or edge cases
    74|3. Suggest improvements for readability and maintainability
    75|4. Verify adherence to project conventions
    76|```
    77|
    78|**Medium freedom** (pseudocode or scripts with parameters):
    79|
    80|Use when:
    81|
    82|- A preferred pattern exists
    83|- Some variation is acceptable
    84|- Configuration affects behavior
    85|
    86|Example:
    87|
    88|````markdown theme={null}
    89|## Generate report
    90|
    91|Use this template and customize as needed:
    92|
    93|```python
    94|def generate_report(data, format="markdown", include_charts=True):
    95|    # Process data
    96|    # Generate output in specified format
    97|    # Optionally include visualizations
    98|```
    99|````
   100|
   101|**Low freedom** (specific scripts, few or no parameters):
   102|
   103|Use when:
   104|
   105|- Operations are fragile and error-prone
   106|- Consistency is critical
   107|- A specific sequence must be followed
   108|
   109|Example:
   110|
   111|````markdown theme={null}
   112|## Database migration
   113|
   114|Run exactly this script:
   115|
   116|```bash
   117|python scripts/migrate.py --verify --backup
   118|```
   119|
   120|Do not modify the command or add additional flags.
   121|````
   122|
   123|**Analogy**: Think of Claude as a robot exploring a path:
   124|
   125|- **Narrow bridge with cliffs on both sides**: There's only one safe way forward. Provide specific guardrails and exact instructions (low freedom). Example: database migrations that must run in exact sequence.
   126|- **Open field with no hazards**: Many paths lead to success. Give general direction and trust Claude to find the best route (high freedom). Example: code reviews where context determines the best approach.
   127|
   128|### Test with all models you plan to use
   129|
   130|Skills act as additions to models, so effectiveness depends on the underlying model. Test your Skill with all the models you plan to use it with.
   131|
   132|**Testing considerations by model**:
   133|
   134|- **Claude Haiku** (fast, economical): Does the Skill provide enough guidance?
   135|- **Claude Sonnet** (balanced): Is the Skill clear and efficient?
   136|- **Claude Opus** (powerful reasoning): Does the Skill avoid over-explaining?
   137|
   138|What works perfectly for Opus might need more detail for Haiku. If you plan to use your Skill across multiple models, aim for instructions that work well with all of them.
   139|
   140|## Skill structure
   141|
   142|<Note>
   143|  **YAML Frontmatter**: The SKILL.md frontmatter requires two fields:
   144|
   145|- `name` - Human-readable name of the Skill (64 characters maximum)
   146|- `description` - One-line description of what the Skill does and when to use it (1024 characters maximum)
   147|
   148|For complete Skill structure details, see the [Skills overview](/en/docs/agents-and-tools/agent-skills/overview#skill-structure). </Note>
   149|
   150|### Naming conventions
   151|
   152|Use consistent naming patterns to make Skills easier to reference and discuss. We recommend using **gerund form** (verb + -ing) for Skill names, as this clearly describes the activity or capability the Skill provides.
   153|
   154|**Good naming examples (gerund form)**:
   155|
   156|- "Processing PDFs"
   157|- "Analyzing spreadsheets"
   158|- "Managing databases"
   159|- "Testing code"
   160|- "Writing documentation"
   161|
   162|**Acceptable alternatives**:
   163|
   164|- Noun phrases: "PDF Processing", "Spreadsheet Analysis"
   165|- Action-oriented: "Process PDFs", "Analyze Spreadsheets"
   166|
   167|**Avoid**:
   168|
   169|- Vague names: "Helper", "Utils", "Tools"
   170|- Overly generic: "Documents", "Data", "Files"
   171|- Inconsistent patterns within your skill collection
   172|
   173|Consistent naming makes it easier to:
   174|
   175|- Reference Skills in documentation and conversations
   176|- Understand what a Skill does at a glance
   177|- Organize and search through multiple Skills
   178|- Maintain a professional, cohesive skill library
   179|
   180|### Writing effective descriptions
   181|
   182|The `description` field enables Skill discovery and should include both what the Skill does and when to use it.
   183|
   184|<Warning>
   185|  **Always write in third person**. The description is injected into the system prompt, and inconsistent point-of-view can cause discovery problems.
   186|
   187|- **Good:** "Processes Excel files and generates reports"
   188|- **Avoid:** "I can help you process Excel files"
   189|- **Avoid:** "You can use this to process Excel files" </Warning>
   190|
   191|**Be specific and include key terms**. Include both what the Skill does and specific triggers/contexts for when to use it.
   192|
   193|Each Skill has exactly one description field. The description is critical for skill selection: Claude uses it to choose the right Skill from potentially 100+ available Skills. Your description must provide enough detail for Claude to know when to select this Skill, while the rest of SKILL.md provides the implementation details.
   194|
   195|Effective examples:
   196|
   197|**PDF Processing skill:**
   198|
   199|```yaml theme={null}
   200|description: Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
   201|```
   202|
   203|**Excel Analysis skill:**
   204|
   205|```yaml theme={null}
   206|description: Analyze Excel spreadsheets, create pivot tables, generate charts. Use when analyzing Excel files, spreadsheets, tabular data, or .xlsx files.
   207|```
   208|
   209|**Git Commit Helper skill:**
   210|
   211|```yaml theme={null}
   212|description: Generate descriptive commit messages by analyzing git diffs. Use when the user asks for help writing commit messages or reviewing staged changes.
   213|```
   214|
   215|Avoid vague descriptions like these:
   216|
   217|```yaml theme={null}
   218|description: Helps with documents
   219|```
   220|
   221|```yaml theme={null}
   222|description: Processes data
   223|```
   224|
   225|```yaml theme={null}
   226|description: Does stuff with files
   227|```
   228|
   229|### Progressive disclosure patterns
   230|
   231|SKILL.md serves as an overview that points Claude to detailed materials as needed, like a table of contents in an onboarding guide. For an explanation of how progressive disclosure works, see [How Skills work](/en/docs/agents-and-tools/agent-skills/overview#how-skills-work) in the overview.
   232|
   233|**Practical guidance:**
   234|
   235|- Keep SKILL.md body under 500 lines for optimal performance
   236|- Split content into separate files when approaching this limit
   237|- Use the patterns below to organize instructions, code, and resources effectively
   238|
   239|#### Visual overview: From simple to complex
   240|
   241|A basic Skill starts with just a SKILL.md file containing metadata and instructions:
   242|
   243|<img src="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=87782ff239b297d9a9e8e1b72ed72db9" alt="Simple SKILL.md file showing YAML frontmatter and markdown body" data-og-width="2048" width="2048" data-og-height="1153" height="1153" data-path="images/agent-skills-simple-file.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=280&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=c61cc33b6f5855809907f7fda94cd80e 280w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=560&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=90d2c0c1c76b36e8d485f49e0810dbfd 560w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=840&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=ad17d231ac7b0bea7e5b4d58fb4aeabb 840w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=1100&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=f5d0a7a3c668435bb0aee9a3a8f8c329 1100w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=1650&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=0e927c1af9de5799cfe557d12249f6e6 1650w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-simple-file.png?w=2500&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=46bbb1a51dd4c8202a470ac8c80a893d 2500w" />
   244|
   245|As your Skill grows, you can bundle additional content that Claude loads only when needed:
   246|
   247|<img src="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=a5e0aa41e3d53985a7e3e43668a33ea3" alt="Bundling additional reference files like reference.md and forms.md." data-og-width="2048" width="2048" data-og-height="1327" height="1327" data-path="images/agent-skills-bundling-content.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=280&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=f8a0e73783e99b4a643d79eac86b70a2 280w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=560&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=dc510a2a9d3f14359416b706f067904a 560w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=840&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=82cd6286c966303f7dd914c28170e385 840w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=1100&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=56f3be36c77e4fe4b523df209a6824c6 1100w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=1650&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=d22b5161b2075656417d56f41a74f3dd 1650w, https://mintcdn.com/anthropic-claude-docs/4Bny2bjzuGBK7o00/images/agent-skills-bundling-content.png?w=2500&fit=max&auto=format&n=4Bny2bjzuGBK7o00&q=85&s=3dd4bdd6850ffcc96c6c45fcb0acd6eb 2500w" />
   248|
   249|The complete Skill directory structure might look like this:
   250|
   251|```
   252|pdf/
   253|├── SKILL.md              # Main instructions (loaded when triggered)
   254|├── FORMS.md              # Form-filling guide (loaded as needed)
   255|├── reference.md          # API reference (loaded as needed)
   256|├── examples.md           # Usage examples (loaded as needed)
   257|└── scripts/
   258|    ├── analyze_form.py   # Utility script (executed, not loaded)
   259|    ├── fill_form.py      # Form filling script
   260|    └── validate.py       # Validation script
   261|```
   262|
   263|#### Pattern 1: High-level guide with references
   264|
   265|````markdown theme={null}
   266|---
   267|name: PDF Processing
   268|description: Extracts text and tables from PDF files, fills forms, and merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
   269|---
   270|
   271|# PDF Processing
   272|
   273|## Quick start
   274|
   275|Extract text with pdfplumber:
   276|
   277|```python
   278|import pdfplumber
   279|with pdfplumber.open("file.pdf") as pdf:
   280|    text = pdf.pages[0].extract_text()
   281|```
   282|
   283|## Advanced features
   284|
   285|**Form filling**: See [FORMS.md](FORMS.md) for complete guide **API reference**: See [REFERENCE.md](REFERENCE.md) for all methods **Examples**: See [EXAMPLES.md](EXAMPLES.md) for common patterns
   286|````
   287|
   288|Claude loads FORMS.md, REFERENCE.md, or EXAMPLES.md only when needed.
   289|
   290|#### Pattern 2: Domain-specific organization
   291|
   292|For Skills with multiple domains, organize content by domain to avoid loading irrelevant context. When a user asks about sales metrics, Claude only needs to read sales-related schemas, not finance or marketing data. This keeps token usage low and context focused.
   293|
   294|```
   295|bigquery-skill/
   296|├── SKILL.md (overview and navigation)
   297|└── reference/
   298|    ├── finance.md (revenue, billing metrics)
   299|    ├── sales.md (opportunities, pipeline)
   300|    ├── product.md (API usage, features)
   301|    └── marketing.md (campaigns, attribution)
   302|```
   303|
   304|````markdown SKILL.md theme={null}
   305|# BigQuery Data Analysis
   306|
   307|## Available datasets
   308|
   309|**Finance**: Revenue, ARR, billing → See [reference/finance.md](reference/finance.md) **Sales**: Opportunities, pipeline, accounts → See [reference/sales.md](reference/sales.md) **Product**: API usage, features, adoption → See [reference/product.md](reference/product.md) **Marketing**: Campaigns, attribution, email → See [reference/marketing.md](reference/marketing.md)
   310|
   311|## Quick search
   312|
   313|Find specific metrics using grep:
   314|
   315|```bash
   316|grep -i "revenue" reference/finance.md
   317|grep -i "pipeline" reference/sales.md
   318|grep -i "api usage" reference/product.md
   319|```
   320|````
   321|
   322|#### Pattern 3: Conditional details
   323|
   324|Show basic content, link to advanced content:
   325|
   326|```markdown theme={null}
   327|# DOCX Processing
   328|
   329|## Creating documents
   330|
   331|Use docx-js for new documents. See [DOCX-JS.md](DOCX-JS.md).
   332|
   333|## Editing documents
   334|
   335|For simple edits, modify the XML directly.
   336|
   337|**For tracked changes**: See [REDLINING.md](REDLINING.md) **For OOXML details**: See [OOXML.md](OOXML.md)
   338|```
   339|
   340|Claude reads REDLINING.md or OOXML.md only when the user needs those features.
   341|
   342|### Avoid deeply nested references
   343|
   344|Claude may partially read files when they're referenced from other referenced files. When encountering nested references, Claude might use commands like `head -100` to preview content rather than reading entire files, resulting in incomplete information.
   345|
   346|**Keep references one level deep from SKILL.md**. All reference files should link directly from SKILL.md to ensure Claude reads complete files when needed.
   347|
   348|**Bad example: Too deep**:
   349|
   350|```markdown theme={null}
   351|# SKILL.md
   352|
   353|See [advanced.md](advanced.md)...
   354|
   355|# advanced.md
   356|
   357|See [details.md](details.md)...
   358|
   359|# details.md
   360|
   361|Here's the actual information...
   362|```
   363|
   364|**Good example: One level deep**:
   365|
   366|```markdown theme={null}
   367|# SKILL.md
   368|
   369|**Basic usage**: [instructions in SKILL.md] **Advanced features**: See [advanced.md](advanced.md) **API reference**: See [reference.md](reference.md) **Examples**: See [examples.md](examples.md)
   370|```
   371|
   372|### Structure longer reference files with table of contents
   373|
   374|For reference files longer than 100 lines, include a table of contents at the top. This ensures Claude can see the full scope of available information even when previewing with partial reads.
   375|
   376|**Example**:
   377|
   378|```markdown theme={null}
   379|# API Reference
   380|
   381|## Contents
   382|
   383|- Authentication and setup
   384|- Core methods (create, read, update, delete)
   385|- Advanced features (batch operations, webhooks)
   386|- Error handling patterns
   387|- Code examples
   388|
   389|## Authentication and setup
   390|
   391|...
   392|
   393|## Core methods
   394|
   395|...
   396|```
   397|
   398|Claude can then read the complete file or jump to specific sections as needed.
   399|
   400|For details on how this filesystem-based architecture enables progressive disclosure, see the [Runtime environment](#runtime-environment) section in the Advanced section below.
   401|
   402|## Workflows and feedback loops
   403|
   404|### Use workflows for complex tasks
   405|
   406|Break complex operations into clear, sequential steps. For particularly complex workflows, provide a checklist that Claude can copy into its response and check off as it progresses.
   407|
   408|**Example 1: Research synthesis workflow** (for Skills without code):
   409|
   410|````markdown theme={null}
   411|## Research synthesis workflow
   412|
   413|Copy this checklist and track your progress:
   414|
   415|```
   416|Research Progress:
   417|- [ ] Step 1: Read all source documents
   418|- [ ] Step 2: Identify key themes
   419|- [ ] Step 3: Cross-reference claims
   420|- [ ] Step 4: Create structured summary
   421|- [ ] Step 5: Verify citations
   422|```
   423|
   424|**Step 1: Read all source documents**
   425|
   426|Review each document in the `sources/` directory. Note the main arguments and supporting evidence.
   427|
   428|**Step 2: Identify key themes**
   429|
   430|Look for patterns across sources. What themes appear repeatedly? Where do sources agree or disagree?
   431|
   432|**Step 3: Cross-reference claims**
   433|
   434|For each major claim, verify it appears in the source material. Note which source supports each point.
   435|
   436|**Step 4: Create structured summary**
   437|
   438|Organize findings by theme. Include:
   439|
   440|- Main claim
   441|- Supporting evidence from sources
   442|- Conflicting viewpoints (if any)
   443|
   444|**Step 5: Verify citations**
   445|
   446|Check that every claim references the correct source document. If citations are incomplete, return to Step 3.
   447|````
   448|
   449|This example shows how workflows apply to analysis tasks that don't require code. The checklist pattern works for any complex, multi-step process.
   450|
   451|**Example 2: PDF form filling workflow** (for Skills with code):
   452|
   453|````markdown theme={null}
   454|## PDF form filling workflow
   455|
   456|Copy this checklist and check off items as you complete them:
   457|
   458|```
   459|Task Progress:
   460|- [ ] Step 1: Analyze the form (run analyze_form.py)
   461|- [ ] Step 2: Create field mapping (edit fields.json)
   462|- [ ] Step 3: Validate mapping (run validate_fields.py)
   463|- [ ] Step 4: Fill the form (run fill_form.py)
   464|- [ ] Step 5: Verify output (run verify_output.py)
   465|```
   466|
   467|**Step 1: Analyze the form**
   468|
   469|Run: `python scripts/analyze_form.py input.pdf`
   470|
   471|This extracts form fields and their locations, saving to `fields.json`.
   472|
   473|**Step 2: Create field mapping**
   474|
   475|Edit `fields.json` to add values for each field.
   476|
   477|**Step 3: Validate mapping**
   478|
   479|Run: `python scripts/validate_fields.py fields.json`
   480|
   481|Fix any validation errors before continuing.
   482|
   483|**Step 4: Fill the form**
   484|
   485|Run: `python scripts/fill_form.py input.pdf fields.json output.pdf`
   486|
   487|**Step 5: Verify output**
   488|
   489|Run: `python scripts/verify_output.py output.pdf`
   490|
   491|If verification fails, return to Step 2.
   492|````
   493|
   494|Clear steps prevent Claude from skipping critical validation. The checklist helps both Claude and you track progress through multi-step workflows.
   495|
   496|### Implement feedback loops
   497|
   498|**Common pattern**: Run validator → fix errors → repeat
   499|
   500|This pattern greatly improves output quality.
   501|