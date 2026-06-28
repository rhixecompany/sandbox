---
name: skill-creator-schemas
description: "JSON Schemas"
version: 1.0.0
author: Alexa
---
     1|# JSON Schemas
     2|
     3|This document defines the JSON schemas used by skill-creator.
     4|
     5|---
     6|
     7|## evals.json
     8|
     9|Defines the evals for a skill. Located at `evals/evals.json` within the skill directory.
    10|
    11|```json
    12|{
    13|  "evals": [
    14|    {
    15|      "id": 1,
    16|      "prompt": "User's example prompt",
    17|      "expected_output": "Description of expected result",
    18|      "files": ["evals/files/sample1.pdf"],
    19|      "expectations": [
    20|        "The output includes X",
    21|        "The skill used script Y"
    22|      ]
    23|    }
    24|  ],
    25|  "skill_name": "example-skill"
    26|}
    27|```
    28|
    29|**Fields:**
    30|
    31|- `skill_name`: Name matching the skill's frontmatter
    32|- `evals[].id`: Unique integer identifier
    33|- `evals[].prompt`: The task to execute
    34|- `evals[].expected_output`: Human-readable description of success
    35|- `evals[].files`: Optional list of input file paths (relative to skill root)
    36|- `evals[].expectations`: List of verifiable statements
    37|
    38|---
    39|
    40|## history.json
    41|
    42|Tracks version progression in Improve mode. Located at workspace root.
    43|
    44|```json
    45|{
    46|  "current_best": "v2",
    47|  "iterations": [
    48|    {
    49|      "version": "v0",
    50|      "parent": null,
    51|      "expectation_pass_rate": 0.65,
    52|      "grading_result": "baseline",
    53|      "is_current_best": false
    54|    },
    55|    {
    56|      "version": "v1",
    57|      "parent": "v0",
    58|      "expectation_pass_rate": 0.75,
    59|      "grading_result": "won",
    60|      "is_current_best": false
    61|    },
    62|    {
    63|      "version": "v2",
    64|      "parent": "v1",
    65|      "expectation_pass_rate": 0.85,
    66|      "grading_result": "won",
    67|      "is_current_best": true
    68|    }
    69|  ],
    70|  "skill_name": "pdf",
    71|  "started_at": "2026-01-15T10:30:00Z"
    72|}
    73|```
    74|
    75|**Fields:**
    76|
    77|- `started_at`: ISO timestamp of when improvement started
    78|- `skill_name`: Name of the skill being improved
    79|- `current_best`: Version identifier of the best performer
    80|- `iterations[].version`: Version identifier (v0, v1, ...)
    81|- `iterations[].parent`: Parent version this was derived from
    82|- `iterations[].expectation_pass_rate`: Pass rate from grading
    83|- `iterations[].grading_result`: "baseline", "won", "lost", or "tie"
    84|- `iterations[].is_current_best`: Whether this is the current best version
    85|
    86|---
    87|
    88|## grading.json
    89|
    90|Output from the grader agent. Located at `<run-dir>/grading.json`.
    91|
    92|```json
    93|{
    94|  "claims": [
    95|    {
    96|      "claim": "The form has 12 fillable fields",
    97|      "type": "factual",
    98|      "verified": true,
    99|      "evidence": "Counted 12 fields in field_info.json"
   100|    }
   101|  ],
   102|  "eval_feedback": {
   103|    "suggestions": [
   104|      {
   105|        "assertion": "The output includes the name 'John Smith'",
   106|        "reason": "A hallucinated document that mentions the name would also pass"
   107|      }
   108|    ],
   109|    "overall": "Assertions check presence but not correctness."
   110|  },
   111|  "execution_metrics": {
   112|    "tool_calls": {
   113|      "Read": 5,
   114|      "Write": 2,
   115|      "Bash": 8
   116|    },
   117|    "total_tool_calls": 15,
   118|    "total_steps": 6,
   119|    "errors_encountered": 0,
   120|    "output_chars": 12450,
   121|    "transcript_chars": 3200
   122|  },
   123|  "expectations": [
   124|    {
   125|      "text": "The output includes the name 'John Smith'",
   126|      "passed": true,
   127|      "evidence": "Found in transcript Step 3: 'Extracted names: John Smith, Sarah Johnson'"
   128|    },
   129|    {
   130|      "text": "The spreadsheet has a SUM formula in cell B10",
   131|      "passed": false,
   132|      "evidence": "No spreadsheet was created. The output was a text file."
   133|    }
   134|  ],
   135|  "summary": {
   136|    "passed": 2,
   137|    "failed": 1,
   138|    "total": 3,
   139|    "pass_rate": 0.67
   140|  },
   141|  "timing": {
   142|    "executor_duration_seconds": 165.0,
   143|    "grader_duration_seconds": 26.0,
   144|    "total_duration_seconds": 191.0
   145|  },
   146|  "user_notes_summary": {
   147|    "uncertainties": ["Used 2023 data, may be stale"],
   148|    "needs_review": [],
   149|    "workarounds": [
   150|      "Fell back to text overlay for non-fillable fields"
   151|    ]
   152|  }
   153|}
   154|```
   155|
   156|**Fields:**
   157|
   158|- `expectations[]`: Graded expectations with evidence
   159|- `summary`: Aggregate pass/fail counts
   160|- `execution_metrics`: Tool usage and output size (from executor's metrics.json)
   161|- `timing`: Wall clock timing (from timing.json)
   162|- `claims`: Extracted and verified claims from the output
   163|- `user_notes_summary`: Issues flagged by the executor
   164|- `eval_feedback`: (optional) Improvement suggestions for the evals, only present when the grader identifies issues worth raising
   165|
   166|---
   167|
   168|## metrics.json
   169|
   170|Output from the executor agent. Located at `<run-dir>/outputs/metrics.json`.
   171|
   172|```json
   173|{
   174|  "errors_encountered": 0,
   175|  "files_created": ["filled_form.pdf", "field_values.json"],
   176|  "output_chars": 12450,
   177|  "tool_calls": {
   178|    "Read": 5,
   179|    "Write": 2,
   180|    "Bash": 8,
   181|    "Edit": 1,
   182|    "Glob": 2,
   183|    "Grep": 0
   184|  },
   185|  "total_steps": 6,
   186|  "total_tool_calls": 18,
   187|  "transcript_chars": 3200
   188|}
   189|```
   190|
   191|**Fields:**
   192|
   193|- `tool_calls`: Count per tool type
   194|- `total_tool_calls`: Sum of all tool calls
   195|- `total_steps`: Number of major execution steps
   196|- `files_created`: List of output files created
   197|- `errors_encountered`: Number of errors during execution
   198|- `output_chars`: Total character count of output files
   199|- `transcript_chars`: Character count of transcript
   200|
   201|---
   202|
   203|## timing.json
   204|
   205|Wall clock timing for a run. Located at `<run-dir>/timing.json`.
   206|
   207|**How to capture:** When a subagent task completes, the task notification includes `total_tokens` and `duration_ms`. Save these immediately — they are not persisted anywhere else and cannot be recovered after the fact.
   208|
   209|```json
   210|{
   211|  "duration_ms": 23332,
   212|  "executor_duration_seconds": 165.0,
   213|  "executor_end": "2026-01-15T10:32:45Z",
   214|  "executor_start": "2026-01-15T10:30:00Z",
   215|  "grader_duration_seconds": 26.0,
   216|  "grader_end": "2026-01-15T10:33:12Z",
   217|  "grader_start": "2026-01-15T10:32:46Z",
   218|  "total_duration_seconds": 23.3,
   219|  "total_tokens": 84852
   220|}
   221|```
   222|
   223|---
   224|
   225|## benchmark.json
   226|
   227|Output from Benchmark mode. Located at `benchmarks/<timestamp>/benchmark.json`.
   228|
   229|```json
   230|{
   231|  "metadata": {
   232|    "skill_name": "pdf",
   233|    "skill_path": "/path/to/pdf",
   234|    "executor_model": "claude-sonnet-4-20250514",
   235|    "analyzer_model": "most-capable-model",
   236|    "timestamp": "2026-01-15T10:30:00Z",
   237|    "evals_run": [1, 2, 3],
   238|    "runs_per_configuration": 3
   239|  },
   240|
   241|  "notes": [
   242|    "Assertion 'Output is a PDF file' passes 100% in both configurations - may not differentiate skill value",
   243|    "Eval 3 shows high variance (50% ± 40%) - may be flaky or model-dependent",
   244|    "Without-skill runs consistently fail on table extraction expectations",
   245|    "Skill adds 13s average execution time but improves pass rate by 50%"
   246|  ],
   247|  "run_summary": {
   248|    "with_skill": {
   249|      "pass_rate": {
   250|        "mean": 0.85,
   251|        "stddev": 0.05,
   252|        "min": 0.8,
   253|        "max": 0.9
   254|      },
   255|      "time_seconds": {
   256|        "mean": 45.0,
   257|        "stddev": 12.0,
   258|        "min": 32.0,
   259|        "max": 58.0
   260|      },
   261|      "tokens": {
   262|        "mean": 3800,
   263|        "stddev": 400,
   264|        "min": 3200,
   265|        "max": 4100
   266|      }
   267|    },
   268|    "without_skill": {
   269|      "pass_rate": {
   270|        "mean": 0.35,
   271|        "stddev": 0.08,
   272|        "min": 0.28,
   273|        "max": 0.45
   274|      },
   275|      "time_seconds": {
   276|        "mean": 32.0,
   277|        "stddev": 8.0,
   278|        "min": 24.0,
   279|        "max": 42.0
   280|      },
   281|      "tokens": {
   282|        "mean": 2100,
   283|        "stddev": 300,
   284|        "min": 1800,
   285|        "max": 2500
   286|      }
   287|    },
   288|    "delta": {
   289|      "pass_rate": "+0.50",
   290|      "time_seconds": "+13.0",
   291|      "tokens": "+1700"
   292|    }
   293|  },
   294|
   295|  "runs": [
   296|    {
   297|      "eval_id": 1,
   298|      "eval_name": "Ocean",
   299|      "configuration": "with_skill",
   300|      "run_number": 1,
   301|      "result": {
   302|        "pass_rate": 0.85,
   303|        "passed": 6,
   304|        "failed": 1,
   305|        "total": 7,
   306|        "time_seconds": 42.5,
   307|        "tokens": 3800,
   308|        "tool_calls": 18,
   309|        "errors": 0
   310|      },
   311|      "expectations": [
   312|        { "text": "...", "passed": true, "evidence": "..." }
   313|      ],
   314|      "notes": [
   315|        "Used 2023 data, may be stale",
   316|        "Fell back to text overlay for non-fillable fields"
   317|      ]
   318|    }
   319|  ]
   320|}
   321|```
   322|
   323|**Fields:**
   324|
   325|- `metadata`: Information about the benchmark run
   326|  - `skill_name`: Name of the skill
   327|  - `timestamp`: When the benchmark was run
   328|  - `evals_run`: List of eval names or IDs
   329|  - `runs_per_configuration`: Number of runs per config (e.g. 3)
   330|- `runs[]`: Individual run results
   331|  - `eval_id`: Numeric eval identifier
   332|  - `eval_name`: Human-readable eval name (used as section header in the viewer)
   333|  - `configuration`: Must be `"with_skill"` or `"without_skill"` (the viewer uses this exact string for grouping and color coding)
   334|  - `run_number`: Integer run number (1, 2, 3...)
   335|  - `result`: Nested object with `pass_rate`, `passed`, `total`, `time_seconds`, `tokens`, `errors`
   336|- `run_summary`: Statistical aggregates per configuration
   337|  - `with_skill` / `without_skill`: Each contains `pass_rate`, `time_seconds`, `tokens` objects with `mean` and `stddev` fields
   338|  - `delta`: Difference strings like `"+0.50"`, `"+13.0"`, `"+1700"`
   339|- `notes`: Freeform observations from the analyzer
   340|
   341|**Important:** The viewer reads these field names exactly. Using `config` instead of `configuration`, or putting `pass_rate` at the top level of a run instead of nested under `result`, will cause the viewer to show empty/zero values. Always reference this schema when generating benchmark.json manually.
   342|
   343|---
   344|
   345|## comparison.json
   346|
   347|Output from blind comparator. Located at `<grading-dir>/comparison-N.json`.
   348|
   349|```json
   350|{
   351|  "expectation_results": {
   352|    "A": {
   353|      "passed": 4,
   354|      "total": 5,
   355|      "pass_rate": 0.8,
   356|      "details": [{ "text": "Output includes name", "passed": true }]
   357|    },
   358|    "B": {
   359|      "passed": 3,
   360|      "total": 5,
   361|      "pass_rate": 0.6,
   362|      "details": [{ "text": "Output includes name", "passed": true }]
   363|    }
   364|  },
   365|  "output_quality": {
   366|    "A": {
   367|      "score": 9,
   368|      "strengths": [
   369|        "Complete solution",
   370|        "Well-formatted",
   371|        "All fields present"
   372|      ],
   373|      "weaknesses": ["Minor style inconsistency in header"]
   374|    },
   375|    "B": {
   376|      "score": 5,
   377|      "strengths": ["Readable output", "Correct basic structure"],
   378|      "weaknesses": [
   379|        "Missing date field",
   380|        "Formatting inconsistencies",
   381|        "Partial data extraction"
   382|      ]
   383|    }
   384|  },
   385|  "reasoning": "Output A provides a complete solution with proper formatting and all required fields. Output B is missing the date field and has formatting inconsistencies.",
   386|  "rubric": {
   387|    "A": {
   388|      "content": {
   389|        "correctness": 5,
   390|        "completeness": 5,
   391|        "accuracy": 4
   392|      },
   393|      "structure": {
   394|        "organization": 4,
   395|        "formatting": 5,
   396|        "usability": 4
   397|      },
   398|      "content_score": 4.7,
   399|      "structure_score": 4.3,
   400|      "overall_score": 9.0
   401|    },
   402|    "B": {
   403|      "content": {
   404|        "correctness": 3,
   405|        "completeness": 2,
   406|        "accuracy": 3
   407|      },
   408|      "structure": {
   409|        "organization": 3,
   410|        "formatting": 2,
   411|        "usability": 3
   412|      },
   413|      "content_score": 2.7,
   414|      "structure_score": 2.7,
   415|      "overall_score": 5.4
   416|    }
   417|  },
   418|  "winner": "A"
   419|}
   420|```
   421|
   422|---
   423|
   424|## analysis.json
   425|
   426|Output from post-hoc analyzer. Located at `<grading-dir>/analysis.json`.
   427|
   428|```json
   429|{
   430|  "comparison_summary": {
   431|    "winner": "A",
   432|    "winner_skill": "path/to/winner/skill",
   433|    "loser_skill": "path/to/loser/skill",
   434|    "comparator_reasoning": "Brief summary of why comparator chose winner"
   435|  },
   436|  "improvement_suggestions": [
   437|    {
   438|      "priority": "high",
   439|      "category": "instructions",
   440|      "suggestion": "Replace 'process the document appropriately' with explicit steps",
   441|      "expected_impact": "Would eliminate ambiguity that caused inconsistent behavior"
   442|    }
   443|  ],
   444|  "instruction_following": {
   445|    "winner": {
   446|      "score": 9,
   447|      "issues": ["Minor: skipped optional logging step"]
   448|    },
   449|    "loser": {
   450|      "score": 6,
   451|      "issues": [
   452|        "Did not use the skill's formatting template",
   453|        "Invented own approach instead of following step 3"
   454|      ]
   455|    }
   456|  },
   457|  "loser_weaknesses": [
   458|    "Vague instruction 'process the document appropriately' led to inconsistent behavior",
   459|    "No script for validation, agent had to improvise"
   460|  ],
   461|  "transcript_insights": {
   462|    "winner_execution_pattern": "Read skill -> Followed 5-step process -> Used validation script",
   463|    "loser_execution_pattern": "Read skill -> Unclear on approach -> Tried 3 different methods"
   464|  },
   465|  "winner_strengths": [
   466|    "Clear step-by-step instructions for handling multi-page documents",
   467|    "Included validation script that caught formatting errors"
   468|  ]
   469|}
   470|```
   471|