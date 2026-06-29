# Usage

> Extracted from `create-tldr-page.prompt.md`.

## Usage

### Syntax

```bash
/create-tldr-page #fetch <URL> <command> [text data] [context file]
```

### Error Handling

#### Missing Command

**User**

```bash
/create-tldr-page https://some-command.io/docs/manual.html
```

**Agent**

```text
I'll fetch the URL and analyze the documentation.
From the data extracted, I assume the command is `some-command`. Is this correct? (yes/no)
```

#### Missing URL

**User**

```bash
/create-tldr-page some-command
```

**Agent**

```text
A URL to authoritative documentation is required for tldr pages. Here are some acceptable URL
patterns:

1. https://gnu.org/software/manual/html_node/some-command.html
2. https://some.org/serve/some.man.html#some-command
3. https://some-command.io/docs/cli/latest/manual
4. https://some-command.io/docs/quickstart

Please provide the documentation URL for `some-command`.
```
