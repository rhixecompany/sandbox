# Output Formatting Rules

> Extracted from `create-tldr-page.prompt.md`.

## Output Formatting Rules

You MUST follow these placeholder conventions:

- **Options with arguments**: When an option takes an argument, wrap BOTH the option AND its argument separately
  - Example: `minipro {{[-p|--device]}} {{chip_name}}`
  - Example: `git commit {{[-m|--message]}} {{message_text}}`
  - **DO NOT** combine them as: `minipro -p {{chip_name}}` (incorrect)

- **Options without arguments**: Wrap standalone options (flags) that don't take arguments
  - Example: `minipro {{[-E|--erase]}}`
  - Example: `git add {{[-A|--all]}}`

- **Single short options**: Do NOT wrap single short options when used alone without long form
  - Example: `ls -l` (not wrapped)
  - Example: `minipro -L` (not wrapped)
  - However, if both short and long forms exist, wrap them: `{{[-l|--list]}}`

- **Subcommands**: Generally do NOT wrap subcommands unless they are user-provided variables
  - Example: `git init` (not wrapped)
  - Example: `tldr {{command}}` (wrapped when variable)

- **Arguments and operands**: Always wrap user-provided values
  - Example: `{{device_name}}`, `{{chip_name}}`, `{{repository_url}}`
  - Example: `{{path/to/file}}` for file paths
  - Example: `{{https://example.com}}` for URLs

- **Command structure**: Options should appear BEFORE their arguments in the placeholder syntax
  - Correct: `command {{[-o|--option]}} {{value}}`
  - Incorrect: `command -o {{value}}`
