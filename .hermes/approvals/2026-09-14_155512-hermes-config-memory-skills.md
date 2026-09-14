# Destructive-change approval

- **Requestor:** Alexa
- **Scope:** Reconcile Hermes config through its CLI; merge root/workspace SOUL/USER/MEMORY files into canonical targets; delete only the explicitly named source files after exact-content verification.
- **Authorization:** The user request explicitly directs the merge and deletion operations.
- **Rollback:** Restore deleted source files from the merged target sections using Git for workspace files and the target content/hash evidence for Hermes-home files; revert skill changes with `skill_manage`/Git as appropriate. Backups and malformed snapshots remain untouched.
- **Preconditions:** Inventory paths and hashes; parse config; verify target content before deletion.
- **Postconditions:** `hermes config check` exits 0; all source-content inclusion checks pass; exact source paths are absent only after verification; nested profile files remain unchanged.

## Approval

+1 — explicit user authorization in the task request.
