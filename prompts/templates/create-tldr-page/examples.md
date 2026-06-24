# Examples

> Extracted from `create-tldr-page.prompt.md`.

## Examples

### Reference Examples

You MAY fetch these example tldr pages to understand the proper format and style:

- [git](https://raw.githubusercontent.com/jhauga/tldr/refs/heads/main/pages/common/git.md)
- [distrobox-create](https://raw.githubusercontent.com/jhauga/tldr/refs/heads/main/pages/linux/distrobox-create.md)
- [nmcli](https://raw.githubusercontent.com/jhauga/tldr/refs/heads/main/pages/linux/nmcli.md)

### Expected Output Using Example

**User**

```bash
/create-tldr-page #fetch https://git-scm.com/docs/git git
```

**Agent**

```markdown
# git

> Distributed version control system. Some subcommands such as `commit`, `add`, `branch`, `switch`, `push`, etc. have their own usage documentation. More information: <https://git-scm.com/docs/git>.

- Create an empty Git repository:

`git init`

- Clone a remote Git repository from the internet:

`git clone {{https://example.com/repo.git}}`

- View the status of the local repository:

`git status`

- Stage all changes for a commit:

`git add {{[-A|--all]}}`

- Commit changes to version history:

`git commit {{[-m|--message]}} {{message_text}}`

- Push local commits to a remote repository:

`git push`

- Pull any changes made to a remote:

`git pull`

- Reset everything the way it was in the latest commit:

`git reset --hard; git clean {{[-f|--force]}}`
````
