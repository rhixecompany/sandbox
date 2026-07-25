---
name: glab-troubleshooting
description: "glab Troubleshooting Guide"
version: 1.0.0
author: Alexa
---
     1|# glab Troubleshooting Guide
     2|
     3|Comprehensive troubleshooting guide for common glab CLI issues and errors.
     4|
     5|## Installation Issues
     6|
     7|### Command Not Found
     8|
     9|**Error:**
    10|
    11|```
    12|command not found: glab
    13|```
    14|
    15|or
    16|
    17|```
    18|glab: command not found
    19|```
    20|
    21|**Causes:**
    22|
    23|- glab is not installed
    24|- glab is not in PATH
    25|
    26|**Solutions:**
    27|
    28|1. Verify installation:
    29|
    30|   ```bash
    31|   which glab
    32|   ```
    33|
    34|2. Install glab if missing (see main README for installation instructions)
    35|
    36|3. If installed but not in PATH, add to PATH:
    37|
    38|   ```bash
    39|   # Find where glab is installed
    40|   find / -name glab 2>/dev/null
    41|
    42|   # Add to PATH in ~/.bashrc or ~/.zshrc
    43|   export PATH="$PATH:/path/to/glab"
    44|   ```
    45|
    46|4. For Go installation, ensure `$GOPATH/bin` is in PATH:
    47|
    48|   ```bash
    49|   export PATH="$PATH:$(go env GOPATH)/bin"
    50|   ```
    51|
    52|### Version Conflicts
    53|
    54|**Error:**
    55|
    56|```
    57|glab: incompatible version
    58|```
    59|
    60|**Solution:** Update to the latest version:
    61|
    62|```bash
    63|# macOS
    64|brew upgrade glab
    65|
    66|# Linux (depends on package manager)
    67|sudo apt update && sudo apt upgrade glab
    68|```
    69|
    70|## Authentication Issues
    71|
    72|### 401 Unauthorized
    73|
    74|**Error:**
    75|
    76|```
    77|failed to get current user: GET https://gitlab.com/api/v4/user: 401 {message: 401 Unauthorized}
    78|```
    79|
    80|**Causes:**
    81|
    82|- Not authenticated
    83|- Token expired
    84|- Invalid token
    85|- Wrong GitLab instance
    86|
    87|**Solutions:**
    88|
    89|1. Authenticate:
    90|
    91|   ```bash
    92|   glab auth login
    93|   ```
    94|
    95|2. Check authentication status:
    96|
    97|   ```bash
    98|   glab auth status
    99|   ```
   100|
   101|3. Re-authenticate with new token:
   102|
   103|   ```bash
   104|   glab auth login --hostname gitlab.com --token YOUR_TOKEN
   105|   ```
   106|
   107|4. Verify token has correct scopes (api, read_user, write_repository)
   108|
   109|5. For self-hosted GitLab, ensure correct hostname:
   110|
   111|   ```bash
   112|   glab auth login --hostname gitlab.example.org
   113|   ```
   114|
   115|### Token Permissions
   116|
   117|**Error:**
   118|
   119|```
   120|403 Forbidden
   121|```
   122|
   123|or
   124|
   125|```
   126|insufficient permissions
   127|```
   128|
   129|**Causes:**
   130|
   131|- Token lacks required scopes
   132|- User doesn't have project permissions
   133|
   134|**Solutions:**
   135|
   136|1. Create new token with required scopes:
   137|   - api
   138|   - read_api
   139|   - read_user
   140|   - write_repository
   141|   - read_repository
   142|
   143|2. Verify project access in GitLab web UI
   144|
   145|3. Check if project is private and token has access
   146|
   147|### Multiple Accounts
   148|
   149|**Issue:** Working with multiple GitLab instances
   150|
   151|**Solution:** glab supports multiple authenticated accounts:
   152|
   153|```bash
   154|# Authenticate with gitlab.com
   155|glab auth login --hostname gitlab.com
   156|
   157|# Authenticate with self-hosted instance
   158|glab auth login --hostname gitlab.example.org
   159|
   160|# Check all authenticated accounts
   161|glab auth status
   162|
   163|# Use specific host for command
   164|glab mr list -R gitlab.example.org/namespace/project
   165|```
   166|
   167|## Repository Context Issues
   168|
   169|### Not a Git Repository
   170|
   171|**Error:**
   172|
   173|```
   174|fatal: not a git repository (or any of the parent directories): .git
   175|```
   176|
   177|**Causes:**
   178|
   179|- Running glab outside a Git repository
   180|- Git repository not initialized
   181|
   182|**Solutions:**
   183|
   184|1. Navigate to a Git repository:
   185|
   186|   ```bash
   187|   cd /path/to/your/repo
   188|   ```
   189|
   190|2. Or specify repository explicitly:
   191|
   192|   ```bash
   193|   glab mr list -R owner/repo
   194|   ```
   195|
   196|3. Initialize Git repository if needed:
   197|
   198|   ```bash
   199|   git init
   200|   git remote add origin git@gitlab.com:owner/repo.git
   201|   ```
   202|
   203|### Wrong Repository Detected
   204|
   205|**Issue:** glab operating on wrong repository
   206|
   207|**Solution:**
   208|
   209|1. Check current repository remote:
   210|
   211|   ```bash
   212|   git remote -v
   213|   ```
   214|
   215|2. Specify correct repository:
   216|
   217|   ```bash
   218|   glab mr list -R owner/correct-repo
   219|   ```
   220|
   221|3. Update Git remote if wrong:
   222|
   223|   ```bash
   224|   git remote set-url origin git@gitlab.com:owner/correct-repo.git
   225|   ```
   226|
   227|### 404 Project Not Found
   228|
   229|**Error:**
   230|
   231|```
   232|404 Project Not Found
   233|```
   234|
   235|**Causes:**
   236|
   237|- Repository doesn't exist
   238|- Wrong namespace/project name
   239|- No access permissions
   240|- Wrong GitLab instance
   241|
   242|**Solutions:**
   243|
   244|1. Verify repository name:
   245|
   246|   ```bash
   247|   # Check in GitLab web UI
   248|   # Correct format: namespace/project
   249|   ```
   250|
   251|2. Check you have access to the project
   252|
   253|3. Verify GitLab instance:
   254|
   255|   ```bash
   256|   glab auth status
   257|   ```
   258|
   259|4. For self-hosted, set correct host:
   260|
   261|   ```bash
   262|   GITLAB_HOST=gitlab.example.org glab repo view
   263|   ```
   264|
   265|## Merge Request Issues
   266|
   267|### Source Branch Already Has MR
   268|
   269|**Error:**
   270|
   271|```
   272|failed to create merge request: source branch already has a merge request
   273|```
   274|
   275|**Cause:**
   276|
   277|- A merge request already exists for this branch
   278|
   279|**Solutions:**
   280|
   281|1. List existing MRs to find it:
   282|
   283|   ```bash
   284|   glab mr list
   285|   glab mr list --source-branch=$(git branch --show-current)
   286|   ```
   287|
   288|2. View the existing MR:
   289|
   290|   ```bash
   291|   glab mr view <mr-number>
   292|   ```
   293|
   294|3. Update existing MR instead of creating new one:
   295|
   296|   ```bash
   297|   glab mr update <mr-number> --title "New title"
   298|   ```
   299|
   300|### Cannot Merge: Conflicts Exist
   301|
   302|**Error:**
   303|
   304|```
   305|Cannot merge: merge conflicts exist
   306|```
   307|
   308|**Solutions:**
   309|
   310|1. Checkout MR locally:
   311|
   312|   ```bash
   313|   glab mr checkout <mr-number>
   314|   ```
   315|
   316|2. Fetch latest target branch:
   317|
   318|   ```bash
   319|   git fetch origin main
   320|   ```
   321|
   322|3. Merge or rebase:
   323|
   324|   ```bash
   325|   git merge origin/main
   326|   # or
   327|   git rebase origin/main
   328|   ```
   329|
   330|4. Resolve conflicts and push:
   331|
   332|   ```bash
   333|   git add .
   334|   git commit
   335|   git push
   336|   ```
   337|
   338|### Pipeline Must Succeed
   339|
   340|**Error:**
   341|
   342|```
   343|cannot merge: pipeline must succeed
   344|```
   345|
   346|**Cause:**
   347|
   348|- Project requires successful pipeline before merge
   349|- Pipeline is failing or pending
   350|
   351|**Solutions:**
   352|
   353|1. Check pipeline status:
   354|
   355|   ```bash
   356|   glab ci status
   357|   ```
   358|
   359|2. View pipeline details:
   360|
   361|   ```bash
   362|   glab pipeline ci view
   363|   ```
   364|
   365|3. Fix pipeline failures and retry:
   366|
   367|   ```bash
   368|   glab ci retry
   369|   ```
   370|
   371|4. If project settings allow, force merge (not recommended):
   372|
   373|   ```bash
   374|   # Only if you have maintainer permissions
   375|   glab mr merge <mr-number> --when-pipeline-succeeds
   376|   ```
   377|
   378|### Cannot Push to Source Branch
   379|
   380|**Error:**
   381|
   382|```
   383|You cannot push commits to this source branch
   384|```
   385|
   386|**Cause:**
   387|
   388|- MR is from a fork
   389|- No write access to source repository
   390|
   391|**Solution:** Ask MR author to make changes, or:
   392|
   393|1. Checkout MR:
   394|
   395|   ```bash
   396|   glab mr checkout <mr-number>
   397|   ```
   398|
   399|2. Make changes on their fork (requires special permissions)
   400|
   401|## Pipeline/CI Issues
   402|
   403|### Pipeline Not Found
   404|
   405|**Error:**
   406|
   407|```
   408|pipeline not found
   409|```
   410|
   411|**Causes:**
   412|
   413|- No pipeline exists for current branch
   414|- Pipeline hasn't started yet
   415|
   416|**Solutions:**
   417|
   418|1. Trigger a pipeline:
   419|
   420|   ```bash
   421|   glab ci run
   422|   ```
   423|
   424|2. Check if .gitlab-ci.yml exists:
   425|
   426|   ```bash
   427|   ls -la .gitlab-ci.yml
   428|   ```
   429|
   430|3. Verify CI/CD is enabled in project settings
   431|
   432|### CI Lint Errors
   433|
   434|**Error:**
   435|
   436|```
   437|.gitlab-ci.yml is invalid
   438|```
   439|
   440|**Solutions:**
   441|
   442|1. Lint locally:
   443|
   444|   ```bash
   445|   glab ci lint
   446|   ```
   447|
   448|2. Common issues:
   449|   - YAML syntax errors (tabs vs spaces)
   450|   - Invalid job names
   451|   - Missing required fields
   452|   - Incorrect indentation
   453|
   454|3. Use GitLab CI/CD config validation in web UI
   455|
   456|4. Check GitLab CI/CD documentation for syntax
   457|
   458|### Cannot Download Artifacts
   459|
   460|**Error:**
   461|
   462|```
   463|failed to download artifacts
   464|```
   465|
   466|**Causes:**
   467|
   468|- Artifacts expired
   469|- Job didn't produce artifacts
   470|- Permission issues
   471|
   472|**Solutions:**
   473|
   474|1. Check if job has artifacts:
   475|
   476|   ```bash
   477|   glab ci view <pipeline-id>
   478|   ```
   479|
   480|2. Verify artifacts haven't expired (check project settings)
   481|
   482|3. Run job again if needed:
   483|
   484|   ```bash
   485|   glab ci retry
   486|   ```
   487|
   488|## Network and Connection Issues
   489|
   490|### Connection Timeout
   491|
   492|**Error:**
   493|
   494|```
   495|dial tcp: i/o timeout
   496|```
   497|
   498|**Causes:**
   499|
   500|- Network connectivity issues
   501|