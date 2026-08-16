---
name: clonedeps-README
description: "clonedeps"
version: 1.0.0
author: Alexa
---
     1|# clonedeps
     2|
     3|`clonedeps` is a bundled OpenCode workflow skill for cloning a small set of important dependency source repositories into a local ignored workspace so agents can read library internals.
     4|
     5|It is orchestrator-owned. The orchestrator delegates source discovery and URL/ref resolution to `@librarian`, asks for approval, then performs the git and filesystem operations directly.
     6|
     7|There is intentionally no helper script. Dependency discovery, ref validation, and cloning are repo-specific enough that the orchestrator/librarian workflow is safer than a brittle cross-ecosystem script.
     8|
     9|Cloned repositories live under `.slim/clonedeps/repos/<safe-repo-name>/`, one folder per source repository, and are ignored by git. `.slim/clonedeps.json` is intentionally trackable project metadata. After cloning, the orchestrator should add or update a concise `## Cloned Dependency Source` section in root `AGENTS.md` that lists each read-only cloned repo path directly with a one-sentence purpose.
    10|
    11|If `.slim/clonedeps.json` already exists, read it first and reuse those clones before asking `@librarian` for new recommendations.
    12|