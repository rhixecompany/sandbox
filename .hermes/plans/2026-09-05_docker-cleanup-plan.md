# Docker / AI Agent Cleanup Plan — subgoal 9

> Trigger: line 9 of `goal-using-superpowers-brainstormin.txt`
> Authorization: destructive ops approved (SOUL.md rule 11 risk noted)

## Scope
- Delete all unused docker images, builds, containers, volumes, models, MCP toolkit artifacts
- Target: workspace-local containers only (not production services)

## Commands (with risk notes)
```
# Confirm nothing running first
`docker ps -a`

# Prune (DESTRUCTIVE — irreversible deletion of all unused images/containers/volumes)
`docker system prune -a -f --volumes`

# Verify
`docker system df`
```

## Risk Note
This deletes ALL unused Docker resources. Confirmed authorized by user (`Full execution including git push/docker cleanup — authorized`).

## Verification
- [ ] Pre-state captured (`docker system df`)
- [ ] Command executed
- [ ] Post-state verified (`docker system df` shows reduced usage)
