---
name: glab-commands-detailed
description: "glab Commands - Detailed Reference"
version: 1.0.0
author: Alexa
---
     1|# glab Commands - Detailed Reference
     2|
     3|This is a comprehensive reference for all glab commands. This file is loaded when detailed command information is needed.
     4|
     5|## Merge Requests (MR)
     6|
     7|### Listing Merge Requests
     8|
     9|```bash
    10|# List MRs assigned to you
    11|glab mr list --assignee=@me
    12|
    13|# List MRs where you're a reviewer
    14|glab mr list --reviewer=@me
    15|
    16|# List all open MRs
    17|glab mr list
    18|
    19|# Filter by state
    20|glab mr list --state=merged
    21|glab mr list --state=closed
    22|glab mr list --state=all
    23|```
    24|
    25|### Creating Merge Requests
    26|
    27|```bash
    28|# Create MR from current branch (interactive)
    29|glab mr create
    30|
    31|# Create MR with title and description
    32|glab mr create --title "Fix bug" --description "Fixes issue #123"
    33|
    34|# Create MR for specific issue
    35|glab mr create 123
    36|
    37|# Create draft MR
    38|glab mr create --draft
    39|
    40|# Create MR and assign reviewers
    41|glab mr create --reviewer=username1,username2
    42|
    43|# Create MR with labels
    44|glab mr create --label="bug,priority:high"
    45|
    46|# Create MR with assignee
    47|glab mr create --assignee=username
    48|
    49|# Create MR to a specific target branch
    50|glab mr create --target-branch=develop
    51|
    52|# Create MR and remove source branch after merge
    53|glab mr create --remove-source-branch
    54|```
    55|
    56|### Viewing and Interacting with MRs
    57|
    58|```bash
    59|# View MR details (opens in browser by default)
    60|glab mr view 123
    61|
    62|# View MR in terminal
    63|glab mr view 123 --web=false
    64|
    65|# View MR with comments
    66|glab mr view 123 --comments
    67|
    68|# Checkout MR branch locally
    69|glab mr checkout 243
    70|
    71|# Approve MR
    72|glab mr approve 123
    73|
    74|# Unapprove MR
    75|glab mr unapprove 123
    76|
    77|# Merge MR
    78|glab mr merge 123
    79|
    80|# Merge and delete source branch
    81|glab mr merge 123 --remove-source-branch
    82|
    83|# Close MR without merging
    84|glab mr close 123
    85|
    86|# Reopen closed MR
    87|glab mr reopen 123
    88|
    89|# Add note/comment to MR
    90|glab mr note 123 -m "Looks good to me"
    91|
    92|# Update MR title
    93|glab mr update 123 --title "New title"
    94|
    95|# Update MR description
    96|glab mr update 123 --description "New description"
    97|
    98|# Mark MR as draft
    99|glab mr update 123 --draft
   100|
   101|# Mark MR as ready (remove draft status)
   102|glab mr update 123 --ready
   103|
   104|# Subscribe to MR notifications
   105|glab mr subscribe 123
   106|
   107|# Unsubscribe from MR notifications
   108|glab mr unsubscribe 123
   109|```
   110|
   111|## Issues
   112|
   113|### Listing Issues
   114|
   115|```bash
   116|# List all issues
   117|glab issue list
   118|
   119|# List issues assigned to you
   120|glab issue list --assignee=@me
   121|
   122|# List issues with specific label
   123|glab issue list --label=bug
   124|
   125|# List issues with multiple labels
   126|glab issue list --label="bug,priority:high"
   127|
   128|# List closed issues
   129|glab issue list --state=closed
   130|
   131|# List all issues (open and closed)
   132|glab issue list --state=all
   133|
   134|# Search issues
   135|glab issue list --search="login error"
   136|
   137|# List issues assigned to specific user
   138|glab issue list --assignee=username
   139|```
   140|
   141|### Creating and Managing Issues
   142|
   143|```bash
   144|# Create issue interactively
   145|glab issue create
   146|
   147|# Create issue with title and description
   148|glab issue create --title "Bug in login" --description "Users cannot log in"
   149|
   150|# Create issue with labels
   151|glab issue create --title "Feature request" --label="enhancement,feature"
   152|
   153|# Create issue with assignee
   154|glab issue create --title "Fix bug" --assignee=username
   155|
   156|# Create confidential issue
   157|glab issue create --title "Security issue" --confidential
   158|
   159|# View issue details
   160|glab issue view 456
   161|
   162|# View issue in browser
   163|glab issue view 456 --web
   164|
   165|# Close issue
   166|glab issue close 456
   167|
   168|# Close with a comment
   169|glab issue close 456 -m "Fixed in MR !123"
   170|
   171|# Reopen issue
   172|glab issue reopen 456
   173|
   174|# Update issue title
   175|glab issue update 456 --title "New title"
   176|
   177|# Update issue description
   178|glab issue update 456 --description "New description"
   179|
   180|# Add labels to issue
   181|glab issue update 456 --label="bug,confirmed"
   182|
   183|# Assign issue
   184|glab issue update 456 --assignee=username
   185|
   186|# Subscribe to issue
   187|glab issue subscribe 456
   188|
   189|# Unsubscribe from issue
   190|glab issue unsubscribe 456
   191|```
   192|
   193|## CI/CD Pipelines
   194|
   195|### Viewing Pipelines
   196|
   197|```bash
   198|# Watch pipeline in progress (interactive)
   199|glab pipeline ci view
   200|
   201|# List recent pipelines
   202|glab ci list
   203|
   204|# List pipelines with specific status
   205|glab ci list --status=failed
   206|glab ci list --status=success
   207|glab ci list --status=running
   208|
   209|# View specific pipeline status
   210|glab ci status
   211|
   212|# View pipeline for specific branch
   213|glab ci status --branch=main
   214|
   215|# Get pipeline trace/logs
   216|glab ci trace
   217|
   218|# Get trace for specific job
   219|glab ci trace <job-id>
   220|
   221|# View pipeline details
   222|glab ci view <pipeline-id>
   223|
   224|# Delete a pipeline
   225|glab ci delete <pipeline-id>
   226|```
   227|
   228|### Triggering and Managing Pipelines
   229|
   230|```bash
   231|# Run/trigger pipeline
   232|glab ci run
   233|
   234|# Run pipeline for specific branch
   235|glab ci run --branch=develop
   236|
   237|# Run pipeline with variables
   238|glab ci run --variables-file /tmp/variables.json
   239|
   240|# Run pipeline with inline variables
   241|glab ci run -V KEY1=value1 -V KEY2=value2
   242|
   243|# Retry failed pipeline
   244|glab ci retry
   245|
   246|# Retry specific pipeline
   247|glab ci retry <pipeline-id>
   248|
   249|# Cancel running pipeline
   250|glab ci cancel
   251|
   252|# Cancel specific pipeline
   253|glab ci cancel <pipeline-id>
   254|```
   255|
   256|### CI Configuration
   257|
   258|```bash
   259|# Lint .gitlab-ci.yml file in current directory
   260|glab ci lint
   261|
   262|# Lint specific file
   263|glab ci lint --path=.gitlab-ci.yml
   264|
   265|# View CI configuration
   266|glab ci config
   267|
   268|# Get CI job artifacts
   269|glab ci artifact <job-id>
   270|
   271|# Download artifacts to specific path
   272|glab ci artifact <job-id> -p path/to/download
   273|```
   274|
   275|## Repository Operations
   276|
   277|### Cloning Repositories
   278|
   279|```bash
   280|# Clone repository
   281|glab repo clone namespace/project
   282|
   283|# Clone to specific directory
   284|glab repo clone namespace/project target-dir
   285|
   286|# Clone from self-hosted GitLab
   287|GITLAB_HOST=gitlab.example.org glab repo clone groupname/project
   288|
   289|# Clone repository by group (interactive)
   290|glab repo clone -g groupname
   291|
   292|# Clone with specific protocol
   293|glab repo clone namespace/project --protocol=ssh
   294|glab repo clone namespace/project --protocol=https
   295|```
   296|
   297|### Repository Information and Management
   298|
   299|```bash
   300|# View repository details
   301|glab repo view
   302|
   303|# View specific repository
   304|glab repo view owner/repo
   305|
   306|# View in browser
   307|glab repo view --web
   308|
   309|# Fork repository
   310|glab repo fork
   311|
   312|# Fork to specific namespace
   313|glab repo fork --clone --namespace=mygroup
   314|
   315|# Archive repository
   316|glab repo archive owner/project
   317|
   318|# Unarchive repository
   319|glab repo unarchive owner/project
   320|
   321|# Delete repository
   322|glab repo delete owner/project
   323|
   324|# Create repository
   325|glab repo create project-name
   326|
   327|# Create private repository
   328|glab repo create project-name --private
   329|
   330|# Create repository with description
   331|glab repo create project-name --description "My project"
   332|
   333|# Mirror repository
   334|glab repo mirror source-repo target-repo
   335|```
   336|
   337|## API Access
   338|
   339|### Making API Calls
   340|
   341|```bash
   342|# GET request
   343|glab api projects/:id/merge_requests
   344|
   345|# GET with specific project ID
   346|glab api projects/12345/merge_requests
   347|
   348|# POST request with data
   349|glab api --method POST projects/:id/issues --field title="Bug report"
   350|
   351|# POST with multiple fields
   352|glab api --method POST projects/:id/issues \
   353|  --field title="Bug" \
   354|  --field description="Description here" \
   355|  --field labels="bug,priority:high"
   356|
   357|# PUT request
   358|glab api --method PUT projects/:id/merge_requests/1 --field title="New Title"
   359|
   360|# DELETE request
   361|glab api --method DELETE projects/:id/issues/123
   362|
   363|# Paginated API request (auto-fetches all pages)
   364|glab api --paginate projects/:id/issues
   365|
   366|# Pagination with query parameters (specify per_page in URL)
   367|glab api "projects/:id/issues?per_page=100"
   368|
   369|# Combine pagination flag with query parameters
   370|glab api --paginate "projects/:id/merge_requests?per_page=50&state=opened"
   371|
   372|# Manual pagination (specific page)
   373|glab api "projects/:id/issues?page=2&per_page=100"
   374|
   375|# Include response headers
   376|glab api --include projects/:id
   377|
   378|# Silent mode (no progress)
   379|glab api --silent projects/:id/merge_requests
   380|```
   381|
   382|## Labels
   383|
   384|```bash
   385|# List all labels
   386|glab label list
   387|
   388|# Create label
   389|glab label create "bug" --color="#FF0000"
   390|
   391|# Create label with description
   392|glab label create "feature" --color="#00FF00" --description "New features"
   393|
   394|# Delete label
   395|glab label delete "old-label"
   396|```
   397|
   398|## Releases
   399|
   400|```bash
   401|# List releases
   402|glab release list
   403|
   404|# Create release
   405|glab release create v1.0.0
   406|
   407|# Create release with notes
   408|glab release create v1.0.0 --notes "Release notes here"
   409|
   410|# Create release from file
   411|glab release create v1.0.0 --notes-file CHANGELOG.md
   412|
   413|# Create release with assets
   414|glab release create v1.0.0 --asset-links='[{"name":"Asset","url":"https://..."}]'
   415|
   416|# View specific release
   417|glab release view v1.0.0
   418|
   419|# Download release assets
   420|glab release download v1.0.0
   421|
   422|# Delete release
   423|glab release delete v1.0.0
   424|```
   425|
   426|## Snippets
   427|
   428|```bash
   429|# List snippets
   430|glab snippet list
   431|
   432|# List all snippets (including private)
   433|glab snippet list --all
   434|
   435|# Create snippet
   436|glab snippet create --title "Config" --filename config.yml
   437|
   438|# Create snippet from file
   439|glab snippet create --title "Script" myfile.sh
   440|
   441|# Create private snippet
   442|glab snippet create --title "Secret" --private secret.txt
   443|
   444|# View snippet
   445|glab snippet view <snippet-id>
   446|
   447|# Delete snippet
   448|glab snippet delete <snippet-id>
   449|```
   450|
   451|## User Operations
   452|
   453|```bash
   454|# View current user information
   455|glab user view
   456|
   457|# View specific user
   458|glab user view username
   459|
   460|# List user's events
   461|glab user events
   462|
   463|# List specific user's events
   464|glab user events username
   465|```
   466|
   467|## Variables (CI/CD)
   468|
   469|```bash
   470|# List variables
   471|glab variable list
   472|
   473|# Get specific variable
   474|glab variable get VAR_NAME
   475|
   476|# Set/create variable
   477|glab variable set VAR_NAME value
   478|
   479|# Set protected variable
   480|glab variable set VAR_NAME value --protected
   481|
   482|# Set masked variable
   483|glab variable set VAR_NAME value --masked
   484|
   485|# Update variable
   486|glab variable update VAR_NAME new-value
   487|
   488|# Delete variable
   489|glab variable delete VAR_NAME
   490|
   491|# Export variables
   492|glab variable export > variables.json
   493|
   494|# Import variables
   495|glab variable import < variables.json
   496|```
   497|
   498|## Additional Commands
   499|
   500|### Aliases
   501|