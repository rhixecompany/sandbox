---
name: shadcn-cli
description: "shadcn CLI Reference"
version: 1.0.0
author: Alexa
---
     1|# shadcn CLI Reference
     2|
     3|Configuration is read from `components.json`.
     4|
     5|> **IMPORTANT:** Always run commands using the project's package runner: `npx shadcn@latest`, `pnpm dlx shadcn@latest`, or `bunx --bun shadcn@latest`. Check `packageManager` from project context to choose the right one. Examples below use `npx shadcn@latest` but substitute the correct runner for the project.
     6|
     7|> **IMPORTANT:** Only use the flags documented below. Do not invent or guess flags — if a flag isn't listed here, it doesn't exist. The CLI auto-detects the package manager from the project's lockfile; there is no `--package-manager` flag.
     8|
     9|## Contents
    10|
    11|- Commands: init, add (dry-run, smart merge), search, view, docs, info, build
    12|- Templates: next, vite, start, react-router, astro
    13|- Presets: named, code, URL formats and fields
    14|- Switching presets
    15|
    16|---
    17|
    18|## Commands
    19|
    20|### `init` — Initialize or create a project
    21|
    22|```bash
    23|npx shadcn@latest init [components...] [options]
    24|```
    25|
    26|Initializes shadcn/ui in an existing project or creates a new project (when `--name` is provided). Optionally installs components in the same step.
    27|
    28|| Flag | Short | Description | Default |
    29|| --- | --- | --- | --- |
    30|| `--template <template>` | `-t` | Template (next, start, vite, next-monorepo, react-router) | — |
    31|| `--preset [name]` | `-p` | Preset configuration (named, code, or URL) | — |
    32|| `--yes` | `-y` | Skip confirmation prompt | `true` |
    33|| `--defaults` | `-d` | Use defaults (`--template=next --preset=base-nova`) | `false` |
    34|| `--force` | `-f` | Force overwrite existing configuration | `false` |
    35|| `--cwd <cwd>` | `-c` | Working directory | current |
    36|| `--name <name>` | `-n` | Name for new project | — |
    37|| `--silent` | `-s` | Mute output | `false` |
    38|| `--rtl` |  | Enable RTL support | — |
    39|| `--reinstall` |  | Re-install existing UI components | `false` |
    40|| `--monorepo` |  | Scaffold a monorepo project | — |
    41|| `--no-monorepo` |  | Skip the monorepo prompt | — |
    42|
    43|`npx shadcn@latest create` is an alias for `npx shadcn@latest init`.
    44|
    45|### `add` — Add components
    46|
    47|> **IMPORTANT:** To compare local components against upstream or to preview changes, ALWAYS use `npx shadcn@latest add <component> --dry-run`, `--diff`, or `--view`. NEVER fetch raw files from GitHub or other sources manually. The CLI handles registry resolution, file paths, and CSS diffing automatically.
    48|
    49|```bash
    50|npx shadcn@latest add [components...] [options]
    51|```
    52|
    53|Accepts component names, registry-prefixed names (`@magicui/shimmer-button`), URLs, or local paths.
    54|
    55|| Flag | Short | Description | Default |
    56|| --- | --- | --- | --- |
    57|| `--yes` | `-y` | Skip confirmation prompt | `false` |
    58|| `--overwrite` | `-o` | Overwrite existing files | `false` |
    59|| `--cwd <cwd>` | `-c` | Working directory | current |
    60|| `--all` | `-a` | Add all available components | `false` |
    61|| `--path <path>` | `-p` | Target path for the component | — |
    62|| `--silent` | `-s` | Mute output | `false` |
    63|| `--dry-run` |  | Preview all changes without writing files | `false` |
    64|| `--diff [path]` |  | Show diffs. Without a path, shows the first 5 files. With a path, shows that file only (implies `--dry-run`) | — |
    65|| `--view [path]` |  | Show file contents. Without a path, shows the first 5 files. With a path, shows that file only (implies `--dry-run`) | — |
    66|
    67|#### Dry-Run Mode
    68|
    69|Use `--dry-run` to preview what `add` would do without writing any files. `--diff` and `--view` both imply `--dry-run`.
    70|
    71|```bash
    72|# Preview all changes.
    73|npx shadcn@latest add button --dry-run
    74|
    75|# Show diffs for all files (top 5).
    76|npx shadcn@latest add button --diff
    77|
    78|# Show the diff for a specific file.
    79|npx shadcn@latest add button --diff button.tsx
    80|
    81|# Show contents for all files (top 5).
    82|npx shadcn@latest add button --view
    83|
    84|# Show the full content of a specific file.
    85|npx shadcn@latest add button --view button.tsx
    86|
    87|# Works with URLs too.
    88|npx shadcn@latest add https://api.npoint.io/abc123 --dry-run
    89|
    90|# CSS diffs.
    91|npx shadcn@latest add button --diff globals.css
    92|```
    93|
    94|**When to use dry-run:**
    95|
    96|- When the user asks "what files will this add?" or "what will this change?" — use `--dry-run`.
    97|- Before overwriting existing components — use `--diff` to preview the changes first.
    98|- When the user wants to inspect component source code without installing — use `--view`.
    99|- When checking what CSS changes would be made to `globals.css` — use `--diff globals.css`.
   100|- When the user asks to review or audit third-party registry code before installing — use `--view` to inspect the source.
   101|
   102|> **`npx shadcn@latest add --dry-run` vs `npx shadcn@latest view`:** Prefer `npx shadcn@latest add --dry-run/--diff/--view` over `npx shadcn@latest view` when the user wants to preview changes to their project. `npx shadcn@latest view` only shows raw registry metadata. `npx shadcn@latest add --dry-run` shows exactly what would happen in the user's project: resolved file paths, diffs against existing files, and CSS updates. Use `npx shadcn@latest view` only when the user wants to browse registry info without a project context.
   103|
   104|#### Smart Merge from Upstream
   105|
   106|See [Updating Components in SKILL.md](./SKILL.md#updating-components) for the full workflow.
   107|
   108|### `search` — Search registries
   109|
   110|```bash
   111|npx shadcn@latest search <registries...> [options]
   112|```
   113|
   114|Fuzzy search across registries. Also aliased as `npx shadcn@latest list`. Without `-q`, lists all items.
   115|
   116|| Flag                | Short | Description            | Default |
   117|| ------------------- | ----- | ---------------------- | ------- |
   118|| `--query <query>`   | `-q`  | Search query           | —       |
   119|| `--limit <number>`  | `-l`  | Max items per registry | `100`   |
   120|| `--offset <number>` | `-o`  | Items to skip          | `0`     |
   121|| `--cwd <cwd>`       | `-c`  | Working directory      | current |
   122|
   123|### `view` — View item details
   124|
   125|```bash
   126|npx shadcn@latest view <items...> [options]
   127|```
   128|
   129|Displays item info including file contents. Example: `npx shadcn@latest view @shadcn/button`.
   130|
   131|### `docs` — Get component documentation URLs
   132|
   133|```bash
   134|npx shadcn@latest docs <components...> [options]
   135|```
   136|
   137|Outputs resolved URLs for component documentation, examples, and API references. Accepts one or more component names. Fetch the URLs to get the actual content.
   138|
   139|Example output for `npx shadcn@latest docs input button`:
   140|
   141|```
   142|base  radix
   143|
   144|input
   145|  docs      https://ui.shadcn.com/docs/components/radix/input
   146|  examples  https://raw.githubusercontent.com/.../examples/input-example.tsx
   147|
   148|button
   149|  docs      https://ui.shadcn.com/docs/components/radix/button
   150|  examples  https://raw.githubusercontent.com/.../examples/button-example.tsx
   151|```
   152|
   153|Some components include an `api` link to the underlying library (e.g. `cmdk` for the command component).
   154|
   155|### `diff` — Check for updates
   156|
   157|Do not use this command. Use `npx shadcn@latest add --diff` instead.
   158|
   159|### `info` — Project information
   160|
   161|```bash
   162|npx shadcn@latest info [options]
   163|```
   164|
   165|Displays project info and `components.json` configuration. Run this first to discover the project's framework, aliases, Tailwind version, and resolved paths.
   166|
   167|| Flag          | Short | Description       | Default |
   168|| ------------- | ----- | ----------------- | ------- |
   169|| `--cwd <cwd>` | `-c`  | Working directory | current |
   170|
   171|**Project Info fields:**
   172|
   173|| Field | Type | Meaning |
   174|| --- | --- | --- |
   175|| `framework` | `string` | Detected framework (`next`, `vite`, `react-router`, `start`, etc.) |
   176|| `frameworkVersion` | `string` | Framework version (e.g. `15.2.4`) |
   177|| `isSrcDir` | `boolean` | Whether the project uses a `src/` directory |
   178|| `isRSC` | `boolean` | Whether React Server Components are enabled |
   179|| `isTsx` | `boolean` | Whether the project uses TypeScript |
   180|| `tailwindVersion` | `string` | `"v3"` or `"v4"` |
   181|| `tailwindConfigFile` | `string` | Path to the Tailwind config file |
   182|| `tailwindCssFile` | `string` | Path to the global CSS file |
   183|| `aliasPrefix` | `string` | Import alias prefix (e.g. `@`, `~`, `@/`) |
   184|| `packageManager` | `string` | Detected package manager (`npm`, `pnpm`, `yarn`, `bun`) |
   185|
   186|**Components.json fields:**
   187|
   188|| Field | Type | Meaning |
   189|| --- | --- | --- |
   190|| `base` | `string` | Primitive library (`radix` or `base`) — determines component APIs and available props |
   191|| `style` | `string` | Visual style (e.g. `nova`, `vega`) |
   192|| `rsc` | `boolean` | RSC flag from config |
   193|| `tsx` | `boolean` | TypeScript flag |
   194|| `tailwind.config` | `string` | Tailwind config path |
   195|| `tailwind.css` | `string` | Global CSS path — this is where custom CSS variables go |
   196|| `iconLibrary` | `string` | Icon library — determines icon import package (e.g. `lucide-react`, `@tabler/icons-react`) |
   197|| `aliases.components` | `string` | Component import alias (e.g. `@/components`) |
   198|| `aliases.utils` | `string` | Utils import alias (e.g. `@/lib/utils`) |
   199|| `aliases.ui` | `string` | UI component alias (e.g. `@/components/ui`) |
   200|| `aliases.lib` | `string` | Lib alias (e.g. `@/lib`) |
   201|| `aliases.hooks` | `string` | Hooks alias (e.g. `@/hooks`) |
   202|| `resolvedPaths` | `object` | Absolute file-system paths for each alias |
   203|| `registries` | `object` | Configured custom registries |
   204|
   205|**Links fields:**
   206|
   207|The `info` output includes a **Links** section with templated URLs for component docs, source, and examples. For resolved URLs, use `npx shadcn@latest docs <component>` instead.
   208|
   209|### `build` — Build a custom registry
   210|
   211|```bash
   212|npx shadcn@latest build [registry] [options]
   213|```
   214|
   215|Builds `registry.json` into individual JSON files for distribution. Default input: `./registry.json`, default output: `./public/r`.
   216|
   217|| Flag              | Short | Description       | Default      |
   218|| ----------------- | ----- | ----------------- | ------------ |
   219|| `--output <path>` | `-o`  | Output directory  | `./public/r` |
   220|| `--cwd <cwd>`     | `-c`  | Working directory | current      |
   221|
   222|---
   223|
   224|## Templates
   225|
   226|| Value          | Framework      | Monorepo support |
   227|| -------------- | -------------- | ---------------- |
   228|| `next`         | Next.js        | Yes              |
   229|| `vite`         | Vite           | Yes              |
   230|| `start`        | TanStack Start | Yes              |
   231|| `react-router` | React Router   | Yes              |
   232|| `astro`        | Astro          | Yes              |
   233|| `laravel`      | Laravel        | No               |
   234|
   235|All templates support monorepo scaffolding via the `--monorepo` flag. When passed, the CLI uses a monorepo-specific template directory (e.g. `next-monorepo`, `vite-monorepo`). When neither `--monorepo` nor `--no-monorepo` is passed, the CLI prompts interactively. Laravel does not support monorepo scaffolding.
   236|
   237|---
   238|
   239|## Presets
   240|
   241|Three ways to specify a preset via `--preset`:
   242|
   243|1. **Named:** `--preset base-nova` or `--preset radix-nova`
   244|2. **Code:** `--preset a2r6bw` (base62 string, starts with lowercase `a`)
   245|3. **URL:** `--preset "https://ui.shadcn.com/init?base=radix&style=nova&..."`
   246|
   247|> **IMPORTANT:** Never try to decode, fetch, or resolve preset codes manually. Preset codes are opaque — pass them directly to `npx shadcn@latest init --preset <code>` and let the CLI handle resolution.
   248|
   249|## Switching Presets
   250|
   251|Ask the user first: **reinstall**, **merge**, or **skip** existing components?
   252|
   253|- **Re-install** → `npx shadcn@latest init --preset <code> --force --reinstall`. Overwrites all component files with the new preset styles. Use when the user hasn't customized components.
   254|- **Merge** → `npx shadcn@latest init --preset <code> --force --no-reinstall`, then run `npx shadcn@latest info` to get the list of installed components and use the [smart merge workflow](./SKILL.md#updating-components) to update them one by one, preserving local changes. Use when the user has customized components.
   255|- **Skip** → `npx shadcn@latest init --preset <code> --force --no-reinstall`. Only updates config and CSS variables, leaves existing components as-is.
   256|
   257|Always run preset commands inside the user's project directory. The CLI automatically preserves the current base (`base` vs `radix`) from `components.json`. If you must use a scratch/temp directory (e.g. for `--dry-run` comparisons), pass `--base <current-base>` explicitly — preset codes do not encode the base.
   258|