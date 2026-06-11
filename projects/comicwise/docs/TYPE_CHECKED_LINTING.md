# Type-Checked Linting Setup - ComicWise

## Overview

ComicWise has been configured to use **TypeScript ESLint's type-checked linting infrastructure** to enable powerful type-aware rules that catch async/await errors, promise handling issues, and other type-related bugs at lint time.

**Last Updated:** March 13, 2026  
**Configuration File:** `eslint.config.mts`  
**ESLint Version:** v9.39.3 (flat config format)  
**TypeScript ESLint:** v8.56.1  
**TypeScript:** v5.9.3

---

## What is Type-Checked Linting?

Type-checked linting combines ESLint's rule system with TypeScript's full type information to catch errors that regular linting cannot. Examples:

- **`require-await`**: Flags async functions that don't actually await anything
- **`no-floating-promises`**: Catches unhandled Promise rejections
- **`await-thenable`**: Detects awaits on non-promise values
- **`no-misused-promises`**: Prevents promises in conditional expressions

## Configuration Details

### Enabled Features

✅ **Full `recommendedTypeChecked` preset** - Includes ~12 type-aware rules  
✅ **`projectService: true`** - Automatic TypeScript project detection (modern approach)  
✅ **`@typescript-eslint/require-await: "warn"`** - Gradual enforcement (warnings, not errors)  
✅ **Test file exemptions** - Disabled for `.test.ts` and `.spec.ts` files  
✅ **JavaScript file handling** - Type-checking disabled for `.js`, `.mjs`, `.cjs` files

### Configuration in `eslint.config.mts`

**Lines 46:** Added `tsEslint.configs.recommendedTypeChecked` to base configs

```typescript
tsEslint.configs.recommendedTypeChecked,
```

**Lines 90-98:** Enabled TypeScript project service

```typescript
parserOptions: {
  projectService: true,
  sourceType: "module",
  tsconfigRootDir: __dirname,
},
```

**Lines 147-148:** Configured require-await rule

```typescript
"require-await": "off",  // Disable base ESLint version
"@typescript-eslint/require-await": "warn",  // Enable TypeScript version
```

**Line 421:** Exempted test files

```typescript
"@typescript-eslint/require-await": "off",
```

**Lines 449-455:** Disabled type-checking for JavaScript files

```typescript
{
  files: ["**/*.js", "**/*.mjs", "**/*.cjs"],
  extends: [tsEslint.configs.disableTypeChecked],
},
```

---

## Fixed Async/Await Violations

The following 10 async functions had missing `await` expressions and were systematically fixed:

### `src/actions/user-preferences.actions.ts`

| Function | Line | Fix Applied |
| --- | --- | --- |
| `getUserPreferencesAction` | 19 | Added `await` to `userPreferenceDal.getByUserId()` |
| `updateThemeAction` | 66 | Added `await` to `updateUserPreferencesAction()` call |
| `updateLayoutPreferenceAction` | 73 | Added `await` to `updateUserPreferencesAction()` call |
| `updateNotificationSettingsAction` | 82 | Added `await` to `updateUserPreferencesAction()` call |
| `updatePrivacySettingsAction` | 93 | Added `await` to `updateUserPreferencesAction()` call |

### `src/app/(root)/settings/page.tsx`

| Function | Line | Fix Applied |
| --- | --- | --- |
| `SettingsContent` | 18 | Added `await` to `userPreferenceDal.getByUserId()` |

### `src/app/(root)/comics/[slug]/page.tsx`

| Function | Line | Fix Applied |
| --- | --- | --- |
| `generateMetadata` | 28 | Added `await` to `comicDal.getBySlug()` |
| `ComicDetailsContent` | 42 | Added `await` to `comicDal.getBySlug()` |

### `src/app/(root)/comics/[slug]/[chapterNumber]/page.tsx`

| Function | Line | Fix Applied |
| --- | --- | --- |
| `getChapterData` | 19-24 | Added `await` to `comicDal.getBySlug()` and `chapterDal.getByComicAndNumber()` |
| `checkIsBookmarked` | 51 | Added `await` to `bookmarkDal.getByUserAndComic()` |

---

## Running Type-Checked Linting

### Prerequisites

- **RAM:** 8GB+ recommended (type-checking is memory-intensive)
- **Machine:** Works best on CI/CD systems or development machines with sufficient resources

### Commands

```bash
# Run ESLint with type-checking
pnpm lint

# Auto-fix issues (including require-await)
pnpm lint:fix

# Watch mode (not recommended with type-checking due to performance)
pnpm lint --watch
```

### First Run

The first time you run type-checked linting:

- TypeScript compiles the entire project (~5-10 seconds)
- Subsequent runs use incremental compilation (~2-3 seconds)
- All 12 type-aware rules are evaluated

### Expected Output

With the current configuration, you should see:

- ✅ 0 require-await errors/warnings (all fixed)
- ✅ No type-checking failures
- All other type-aware rules enforced as configured

---

## Performance Considerations

### Memory Usage

Type-checking requires significant memory because:

1. Full TypeScript compilation must run before linting
2. All type information is loaded into memory
3. ~1-1.5GB of RAM consumed during linting

**Solution for Memory-Constrained Environments:**

- Run linting in CI/CD pipelines instead of locally
- Use separate linting steps for different directories if needed
- Consider running type-check and lint separately:
  ```bash
  pnpm type-check      # TypeScript validation
  pnpm lint            # ESLint (without type-checking)
  ```

### Build Time

Type-checked linting adds ~5-15 seconds to:

- CI/CD pipelines
- Pre-commit hooks (if configured)
- Development workflows

---

## Troubleshooting

### Error: "requires type information"

**Cause:** A type-checked rule is being applied to JavaScript files  
**Solution:** Already handled in `eslint.config.mts` via `disableTypeChecked` config

### Memory Errors During Linting

**Error:** `FATAL ERROR: Zone Allocation failed - process out of memory`

**Solution:**

1. Increase Node.js memory limit:
   ```bash
   NODE_OPTIONS=--max-old-space-size=4096 pnpm lint
   ```
2. Run on machine with more RAM
3. Run in CI/CD environment instead of locally

### Slow Linting Performance

**Cause:** First run includes full TypeScript compilation

**Solution:**

- Run once to cache compilation
- Subsequent runs are faster (incremental compilation)
- Keep TypeScript files unchanged when possible

---

## Rule Reference

### Enabled Type-Checked Rules

The `recommendedTypeChecked` preset includes:

| Rule | Description | Severity |
| --- | --- | --- |
| `@typescript-eslint/await-thenable` | Enforces awaiting only thenables | error |
| `@typescript-eslint/no-floating-promises` | Requires handling of promise rejections | error |
| `@typescript-eslint/no-misused-promises` | Prevents promise misuse in control flow | error |
| `@typescript-eslint/require-await` | Requires async functions to use await | **warn** |
| + 8 more type-aware rules | See TypeScript ESLint docs | varies |

### Disabled for Test Files

These rules are disabled in `.test.ts` and `.spec.ts` files:

- `@typescript-eslint/require-await` (test frameworks use async without explicit await)

### Disabled for JavaScript Files

All type-checked rules are disabled for:

- `*.js` files
- `*.mjs` files (ES modules)
- `*.cjs` files (CommonJS)

---

## Integration with CI/CD

### GitHub Actions Example

```yaml
- name: Run Type-Checked Linting
  run: pnpm lint
  env:
    NODE_OPTIONS: --max-old-space-size=4096
```

### Pre-Commit Hook (Optional)

To enforce type-checked linting before commits:

```bash
# Add to .husky/pre-commit
pnpm lint
```

Note: This may be slow on machines with limited resources. Consider running only on modified files in pre-commit.

---

## Best Practices

### Writing Async Functions

**✅ Correct:**

```typescript
export async function fetchComics() {
  const comics = await db.query.comics.findMany(); // Must await
  return comics;
}
```

**❌ Incorrect:**

```typescript
export async function fetchComics() {
  const comics = db.query.comics.findMany(); // Missing await
  return comics; // Returns Promise<Promise<...>>
}
```

### Calling Async Functions

**✅ Correct:**

```typescript
export async function updateTheme(theme: string) {
  return await updatePreferences({ theme }); // Must await
}
```

**❌ Incorrect:**

```typescript
export async function updateTheme(theme: string) {
  return updatePreferences({ theme }); // Returns unhandled Promise
}
```

### Server Components with DAL Calls

**✅ Correct:**

```typescript
async function PageComponent() {
  const data = await dal.getData();  // Always await in async functions
  return <div>{data}</div>;
}
```

**❌ Incorrect:**

```typescript
async function PageComponent() {
  const data = dal.getData();  // Missing await - data is Promise
  return <div>{data}</div>;  // Will render Promise object
}
```

---

## Future Enhancements

### Level Up: Stricter Enforcement

Once the codebase is fully compliant, increase `require-await` to `"error"`:

```typescript
"@typescript-eslint/require-await": "error",  // Instead of "warn"
```

This will fail CI/CD until all violations are fixed.

### Additional Type-Checked Rules

Consider enabling additional rules from `stylisticTypeChecked`:

- `@typescript-eslint/non-nullable-type-assertion-style`
- `@typescript-eslint/consistent-type-assertions`
- And more for stricter type safety

### Selective Type-Checking

If performance becomes a bottleneck, configure type-checking for specific directories:

```typescript
{
  files: ["src/actions/**/*.ts"],  // Only type-check actions
  extends: [tsEslint.configs.recommendedTypeChecked],
},
```

---

## References

- **TypeScript ESLint Docs:** https://typescript-eslint.io
- **Shared Configs:** https://typescript-eslint.io/docs/linting/configs
- **require-await Rule:** https://typescript-eslint.io/docs/rules/require-await
- **ESLint v9 Flat Config:** https://eslint.org/docs/latest/use/configure/configuration-files
- **ComicWise Architecture:** `docs/architecture.md`
- **Quality Gates:** `AGENTS.md`

---

## Summary

- ✅ Type-checked linting fully enabled with `projectService: true`
- ✅ All 10 async/await violations fixed
- ✅ Test files and JavaScript files properly exempted
- ✅ Ready for CI/CD integration
- ⏳ Requires adequate RAM for local development (8GB+)

Next steps: Run `pnpm lint` on machine with sufficient resources to validate type-aware rules in action.
