---
schema: 1
summary: >
  Per-root inventory of a prompt library.
  Fill one section per root; dedupe by body MD5, not filename.
roots:
  canonical:
    path: ""
    pattern: "**/*.{prompt.md,agent.md,instructions.md,md}"
    counts: {}
    hashes: {}
  legacy:
    - path: ""
      pattern: "*.prompt.md"
      counts: {}
      hashes: {}
duplicates:
  exact_body_groups: []
  filename_collisions: []
  cross_root_duplicates: []
notes: ""