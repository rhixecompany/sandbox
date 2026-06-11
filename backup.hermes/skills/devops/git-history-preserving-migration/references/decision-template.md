# Decision template

Project: <project-name>
Source: <absolute-path>
Target: <absolute-path>
Action: create (clone|copy) | overwrite_with_clone | overwrite_with_copy | skip
Rationale: <text>

Planned commands (Windows PowerShell):
- Backup: Compress-Archive -Path '<target>\*' -DestinationPath '<backup-zip-path>'
- If clone (preserve history): git clone '<source>' '<target>'
- If copy (user prefers PowerShell): Copy-Item -Path '<source>' -Destination '<target>' -Recurse -Force
- If initialize new git repo: git -C '<target>' init && git -C '<target>' add . && git -C '<target>' commit -m 'Initial import (migration)'

Verification:
- backup: <backup-zip-path>
- target_exists: yes/no
- git_history_preserved: yes/no
- git_log_top: <first 5 lines of `git -C '<target>' log --oneline -n 5`>

Rollback steps:
- Unzip backup: Expand-Archive -Path '<backup-zip-path>' -DestinationPath '<target>' -Force
