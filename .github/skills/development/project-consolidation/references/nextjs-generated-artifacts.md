# Next.js Generated Artifacts in Consolidated Repos

Use this note when a consolidated repo includes a Next.js frontend and the build emits files the scaffold did not originally contain.

## Expected build-generated files

- `next-env.d.ts` — normal Next.js type shim; create/commit if the build generates it and the repo expects typed App Router usage.
- `tsconfig.json` — Next.js may rewrite parts of this file during `next build` / `next dev` to align TypeScript settings.
- `*.tsbuildinfo` — build cache artifact; ignore in `.gitignore` unless a project explicitly tracks it.

## Verification rules

1. Run the framework build after scaffold changes.
2. Re-read the generated files from disk, don't assume the build output is unchanged.
3. Update docs and file-structure references so the generated files are documented.
4. If the build rewrites TypeScript config, keep the effective config unless there is a strong project reason to restore the older form.

## Common pitfall

Don't treat every generated file as noise. Some generated files are part of the valid runtime scaffold and should be documented, not removed.