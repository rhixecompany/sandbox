---
name: glab-quick-reference
description: "glab Quick Reference Guide"
version: 1.0.0
author: Alexa
---
     1|# glab Quick Reference Guide
     2|
     3|A condensed reference for the most commonly used GitLab CLI commands.
     4|
     5|## Authentication
     6|
     7|```bash
     8|glab auth login                    # Interactive login
     9|glab auth status                   # Check auth status
    10|echo "token" | glab auth login --stdin  # Login with token
    11|```
    12|
    13|## Merge Requests
    14|
    15|```bash
    16|# Listing
    17|glab mr list                       # All open MRs
    18|glab mr list --assignee=@me        # MRs assigned to me
    19|glab mr list --reviewer=@me        # MRs for me to review
    20|
    21|# Creating
    22|glab mr create                     # Interactive creation
    23|glab mr create --title "Fix" --description "Desc"
    24|glab mr create --draft             # Create draft MR
    25|glab mr create --reviewer=alice,bob
    26|
    27|# Viewing & Managing
    28|glab mr view 123                   # View MR #123
    29|glab mr checkout 123               # Checkout MR branch
    30|glab mr approve 123                # Approve MR
    31|glab mr merge 123                  # Merge MR
    32|glab mr note 123 -m "Comment"      # Add comment
    33|```
    34|
    35|## Issues
    36|
    37|```bash
    38|# Listing
    39|glab issue list                    # All issues
    40|glab issue list --assignee=@me     # Assigned to me
    41|glab issue list --label=bug        # With label
    42|
    43|# Creating & Managing
    44|glab issue create                  # Interactive
    45|glab issue create --title "Bug" --label=bug
    46|glab issue view 456                # View issue
    47|glab issue close 456               # Close issue
    48|```
    49|
    50|## CI/CD
    51|
    52|```bash
    53|# Pipelines
    54|glab pipeline ci view              # Watch pipeline
    55|glab ci list                       # List pipelines
    56|glab ci status                     # Pipeline status
    57|glab ci trace                      # View logs
    58|
    59|# Running & Managing
    60|glab ci run                        # Trigger pipeline
    61|glab ci lint                       # Lint .gitlab-ci.yml
    62|glab ci retry                      # Retry pipeline
    63|glab ci cancel                     # Cancel pipeline
    64|```
    65|
    66|## Repository
    67|
    68|```bash
    69|glab repo clone org/project        # Clone repository
    70|glab repo view                     # View repo details
    71|glab repo fork                     # Fork repository
    72|```
    73|
    74|## API
    75|
    76|```bash
    77|glab api projects/:id/merge_requests           # GET request
    78|glab api --method POST projects/:id/issues \
    79|  --field title="Bug"              # POST with data
    80|```
    81|
    82|## Common Flags
    83|
    84|```bash
    85|--help, -h                         # Show help
    86|--repo, -R owner/repo              # Specify repository
    87|--web, -w                          # Open in browser
    88|--output, -o json                  # JSON output
    89|--verbose                          # Verbose output
    90|```
    91|
    92|## Environment Variables
    93|
    94|```bash
    95|GITLAB_TOKEN=xxx                   # API token
    96|GITLAB_HOST=gitlab.example.org     # Self-hosted GitLab
    97|```
    98|
    99|## Configuration
   100|
   101|```bash
   102|glab config get                    # View configuration
   103|glab config set key value          # Set config value
   104|```
   105|
   106|## Complete Command List
   107|
   108|- `glab alias` - Create command shortcuts
   109|- `glab api` - Make API calls
   110|- `glab auth` - Authentication management
   111|- `glab changelog` - Generate changelogs
   112|- `glab check-update` - Check for updates
   113|- `glab ci` - CI/CD operations
   114|- `glab cluster` - Kubernetes cluster management
   115|- `glab completion` - Shell completion
   116|- `glab config` - Configuration management
   117|- `glab deploy-key` - Deploy key management
   118|- `glab duo` - GitLab Duo AI features
   119|- `glab incident` - Incident management
   120|- `glab issue` - Issue tracking
   121|- `glab iteration` - Iteration management
   122|- `glab job` - CI job operations
   123|- `glab label` - Label management
   124|- `glab mr` - Merge request operations
   125|- `glab opentofu` - OpenTofu integration
   126|- `glab release` - Release management
   127|- `glab repo` - Repository operations
   128|- `glab schedule` - Pipeline schedule management
   129|- `glab securefile` - Secure file management
   130|- `glab snippet` - Snippet operations
   131|- `glab ssh-key` - SSH key management
   132|- `glab stack` - Stack management
   133|- `glab token` - Access token management
   134|- `glab user` - User operations
   135|- `glab variable` - CI/CD variable management
   136|- `glab version` - Show version
   137|
   138|## Tips
   139|
   140|1. Use `glab <command> --help` for detailed help
   141|2. Commands auto-detect repository context from git remote
   142|3. Use `-R owner/repo` when outside a repository
   143|4. Most commands have `--web` flag to open in browser
   144|5. Use `--output=json` for scripting
   145|6. Enable completion: `glab completion --shell fish`
   146|