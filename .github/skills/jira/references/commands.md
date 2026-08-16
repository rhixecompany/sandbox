---
name: jira-commands
description: "Commands Reference"
version: 1.0.0
author: Alexa
---
     1|# Commands Reference
     2|
     3|Complete reference for the `jira` CLI.
     4|
     5|---
     6|
     7|## Viewing Issues
     8|
     9|```bash
    10|# View single issue
    11|jira issue view ISSUE-KEY
    12|
    13|# View with more comments
    14|jira issue view ISSUE-KEY --comments 5
    15|
    16|# Get raw JSON
    17|jira issue view ISSUE-KEY --raw
    18|```
    19|
    20|---
    21|
    22|## Listing Issues
    23|
    24|```bash
    25|# List all issues in project
    26|jira issue list
    27|
    28|# List my issues
    29|jira issue list -a$(jira me)
    30|
    31|# Filter by status (use quotes for multi-word statuses)
    32|jira issue list -s"In Progress"
    33|jira issue list -s"To Do"
    34|jira issue list -sDone
    35|
    36|# Filter by type
    37|jira issue list -tBug
    38|jira issue list -tStory
    39|jira issue list -tTask
    40|jira issue list -tEpic
    41|
    42|# Filter by priority
    43|jira issue list -yHigh
    44|jira issue list -yCritical
    45|
    46|# Filter by label
    47|jira issue list -lurgent -lbug
    48|
    49|# Combine filters
    50|jira issue list -a$(jira me) -s"In Progress" -yHigh
    51|
    52|# Search with text
    53|jira issue list "login error"
    54|
    55|# Recently accessed
    56|jira issue list --history
    57|
    58|# Issues I'm watching
    59|jira issue list -w
    60|
    61|# Created/updated filters
    62|jira issue list --created today
    63|jira issue list --created week
    64|jira issue list --updated -2d
    65|
    66|# Plain output for scripting
    67|jira issue list --plain --no-headers
    68|
    69|# Specific columns
    70|jira issue list --plain --columns key,summary,status,assignee
    71|
    72|# Raw JQL query
    73|jira issue list -q"status = 'In Progress' AND assignee = currentUser()"
    74|
    75|# Paginate results
    76|jira issue list --paginate 20
    77|jira issue list --paginate 10:50 # start:limit
    78|```
    79|
    80|---
    81|
    82|## Creating Issues
    83|
    84|```bash
    85|# Interactive creation
    86|jira issue create
    87|
    88|# Non-interactive with all fields
    89|jira issue create \
    90|    -tBug \
    91|    -s"Login button not working" \
    92|    -b"Users cannot click the login button on Safari" \
    93|    -yHigh \
    94|    -lbug -lurgent
    95|
    96|# Create and assign to self
    97|jira issue create -tTask -s"Summary" -a$(jira me)
    98|
    99|# Create subtask (requires parent)
   100|jira issue create -tSub-task -P"PROJ-123" -s"Subtask summary"
   101|
   102|# Create with custom fields
   103|jira issue create -tStory -s"Summary" --custom story-points=3
   104|
   105|# Skip prompts for optional fields
   106|jira issue create -tTask -s"Quick task" --no-input
   107|
   108|# Open in browser after creation
   109|jira issue create -tBug -s"Bug title" --web
   110|
   111|# Read description from file
   112|jira issue create -tStory -s"Summary" --template /path/to/template.md
   113|
   114|# Read description from stdin
   115|echo "Description here" | jira issue create -tTask -s"Summary"
   116|```
   117|
   118|**Multi-line content:** The CLI chokes on multi-line strings. Write to `/tmp` first:
   119|
   120|```bash
   121|cat > /tmp/jira_body.md <<'EOF'
   122|## Description
   123|User needs ability to export data...
   124|
   125|## Acceptance Criteria
   126|- Export works for CSV
   127|- Export works for JSON
   128|EOF
   129|
   130|jira issue create --no-input \
   131|  -tStory \
   132|  -pPROJ \
   133|  -s"Add export functionality" \
   134|  -b"$(cat /tmp/jira_body.md)"
   135|```
   136|
   137|---
   138|
   139|## Transitioning Issues
   140|
   141|```bash
   142|# Move to a state
   143|jira issue move ISSUE-KEY "In Progress"
   144|jira issue move ISSUE-KEY "Done"
   145|jira issue move ISSUE-KEY "To Do"
   146|
   147|# Move with comment
   148|jira issue move ISSUE-KEY "Done" --comment "Completed the implementation"
   149|
   150|# Move and set resolution
   151|jira issue move ISSUE-KEY "Done" -R"Fixed"
   152|
   153|# Move and reassign
   154|jira issue move ISSUE-KEY "In Review" -a"reviewer@example.com"
   155|
   156|# Open in browser after transition
   157|jira issue move ISSUE-KEY "Done" --web
   158|```
   159|
   160|---
   161|
   162|## Assigning Issues
   163|
   164|```bash
   165|# Assign to specific user
   166|jira issue assign ISSUE-KEY "user@example.com"
   167|jira issue assign ISSUE-KEY "John Doe"
   168|
   169|# Assign to self
   170|jira issue assign ISSUE-KEY $(jira me)
   171|
   172|# Assign to default assignee
   173|jira issue assign ISSUE-KEY default
   174|
   175|# Unassign
   176|jira issue assign ISSUE-KEY x
   177|```
   178|
   179|---
   180|
   181|## Comments
   182|
   183|```bash
   184|# Add comment
   185|jira issue comment add ISSUE-KEY -b"This is my comment"
   186|
   187|# Add comment from file
   188|jira issue comment add ISSUE-KEY --template /path/to/comment.md
   189|```
   190|
   191|---
   192|
   193|## Sprints
   194|
   195|```bash
   196|# List sprints
   197|jira sprint list
   198|
   199|# Active sprint only
   200|jira sprint list --state active
   201|
   202|# Add issue to sprint
   203|jira sprint add SPRINT-ID ISSUE-KEY
   204|
   205|# Close sprint
   206|jira sprint close SPRINT-ID
   207|```
   208|
   209|---
   210|
   211|## Linking Issues
   212|
   213|| Relationship | Meaning                    |
   214|| ------------ | -------------------------- |
   215|| `Blocks`     | First ticket blocks second |
   216|| `Relates`    | General relationship       |
   217|| `Duplicate`  | Same work                  |
   218|| `Epic-Story` | Story belongs to Epic      |
   219|
   220|```bash
   221|# Basic link
   222|jira issue link PROJ-123 PROJ-456 "Relates"
   223|
   224|# Blocker (blocker comes first)
   225|jira issue link PROJ-100 PROJ-200 "Blocks"
   226|# Meaning: PROJ-100 blocks PROJ-200
   227|
   228|# Link to epic
   229|jira issue link PROJ-EPIC PROJ-STORY "Epic-Story"
   230|```
   231|
   232|---
   233|
   234|## Other Commands
   235|
   236|```bash
   237|# Open issue in browser
   238|jira open ISSUE-KEY
   239|
   240|# Show current user
   241|jira me
   242|
   243|# Server info
   244|jira serverinfo
   245|
   246|# List projects
   247|jira project list
   248|
   249|# List boards
   250|jira board list
   251|```
   252|