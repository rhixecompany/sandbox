# Audit: prompt-library-de-dup-and-backup-archive
- Subgoal: prompt-library-de-dup-and-backup-archive
- PROMPTS count: 1550
- BACKUP count: 676
- Filename-match duplicates: 373 (exact=29, divergent=21 in first-50 sample)
- Action rules: EXACT_DUP→delete backup; DIVERGENT→overwrite prompts with backup, delete backup; ONLY_PROMPTS→keep; ONLY_BACKUP→migrate then delete backup.
