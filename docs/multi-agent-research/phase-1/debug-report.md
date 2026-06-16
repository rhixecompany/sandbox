# Phase 1 - Debug Report

Objective:
Validate the failure mode for the requested Hermes debugging command and
identify the supported CLI form.

Reproduction:
```bash
hermes /systematic-debugging
```

Observed output:
```text
hermes: error: argument command: invalid choice: '/systematic-debugging'
```

Investigation:

Workflow note:
- The `systematic-debugging` skill was loaded first to force root-cause
  investigation before any fix attempts.

```bash
hermes --help
```

Relevant output:
```text
{chat,model,fallback,secrets,migrate,gateway,proxy,lsp,setup,postinstall,
whatsapp,whatsapp-cloud,slack,send,login,logout,auth,status,cron,webhook,
portal,kanban,hooks,doctor,security,dump,debug,backup,checkpoints,import,
config,pairing,skills,bundles,plugins,curator,memory,tools,computer-use,mcp,
sessions,insights,claw,version,update,uninstall,acp,profile,completion,
dashboard,desktop,gui,logs,prompt-size}
```

```bash
hermes skills --help
```

Relevant output:
```text
usage: hermes skills [-h]
                     {browse,search,install,inspect,list,check,update,audit,
                      uninstall,reset,opt-out,opt-in,repair-official,publish,
                      snapshot,tap,config}
```

Conclusion:
- Slash-prefixed subcommands are not valid in this Hermes CLI.
- The correct skill-management path is `hermes skills <subcommand>`.
- The debug workflow is now captured with the failure, CLI evidence, and the
  supported resolution path.
