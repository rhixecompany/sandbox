Memory edits & backup policy

1. Read policy: C:\\Users\\Alexa\\AppData\\Local\\hermes\\.hermes_policies
2. If [backup].enabled = false -> overwrite files in-place (no .bak)
3. If deletion requested, move to trash first (C:\\Users\\Alexa\\AppData\\Local\\hermes\\trash) unless user explicitly requests permanent deletion — then delete immediately and log action in ~/.hermes/.hermes_history
4. After editing USER.md and MEMORY.md run: python scripts/validate_memories.py and attach output to the action report
5. When editing memory files, ensure canonical keys: Name:, OS:, Editor/IDE:, Shell preference:, Active model:
