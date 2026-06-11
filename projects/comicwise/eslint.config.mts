import js from "@eslint/js";
import tsEslintParser from "@typescript-eslint/parser";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";
import prettier from "eslint-config-prettier";
import betterTailwind from "eslint-plugin-better-tailwindcss";
// @ts-expect-error - no bundled types for eslint-plugin-drizzle
import drizzle from "eslint-plugin-drizzle";
import importX from "eslint-plugin-import-x";
import jest from "eslint-plugin-jest";
import nodePlugin from "eslint-plugin-n";
import perfectionist from "eslint-plugin-perfectionist";
import playwright from "eslint-plugin-playwright";
import reactRefresh from "eslint-plugin-react-refresh";
import security from "eslint-plugin-security";
import sonarjs from "eslint-plugin-sonarjs";
import testingLibrary from "eslint-plugin-testing-library";
import unicorn from "eslint-plugin-unicorn";
import zod from "eslint-plugin-zod";

import { defineConfig, globalIgnores } from "eslint/config";
import globals from "globals";
import tsEslint from "typescript-eslint";

/**
 * ESLint Configuration for ComicWise
 *
 * Architecture:
 * 1. Base configurations (JS, TypeScript, Next.js, Prettier)
 * 2. Global ignores and language options
 * 3. Global plugins and rules
 * 4. File-specific overrides (React, tests, config files, etc.)
 *
 * All configuration values are static (no process.env access)
 * Environment-specific settings are in appConfig.ts via getEnv()
 *
 * Stack: Next.js 16.1.6, React 19, TypeScript, Drizzle ORM
 */

const eslintConfig = defineConfig([
  // ===========================
  // Base configurations
  // ===========================
  js.configs.recommended,
  tsEslint.configs.recommended,
  tsEslint.configs.recommendedTypeChecked,
  nextVitals,
  nextTs,

  // ===========================
  // Global ignores
  // ===========================
  globalIgnores([
    ".next/**",
    "out/**",
    "build/**",
    "dist/**",
    "node_modules/**",
    "next-env.d.ts",
    ".references/**",
    "src/backuptests/**/*.ts",
    "logs/**",
    "coverage/**",
    "test-results/**",
    "playwright-report/**",
    ".vercel/**",
    "skills/**",
    ".github/skills/**",
    ".vscode/backup/**",
  ]),

  // ===========================
  // Global settings for all files
  // ===========================
  {
    languageOptions: {
      ecmaVersion: 2022,
      sourceType: "module",
      globals: {
        ...globals.browser,
        ...globals.node,
        ...globals.es2021,
        ...globals.jest,
        describe: "readonly",
        it: "readonly",
        test: "readonly",
        expect: "readonly",
        beforeAll: "readonly",
        beforeEach: "readonly",
        afterAll: "readonly",
        afterEach: "readonly",
        vi: "readonly",
      },
      parserOptions: {
        ecmaVersion: 2022,
        sourceType: "module",
        ecmaFeatures: {
          jsx: true,
        },
        projectService: {
          allowDefaultProject: [".prettierrc.ts", "postcss.config.mjs"],
        },
      },
      parser: tsEslintParser,
    },
    linterOptions: {
      noInlineConfig: false,
      reportUnusedDisableDirectives: true,
    },
    settings: {
      "import-x/resolver": [
        {
          typescript: {
            alwaysTryTypes: true,
            project: "./tsconfig.json",
          },
        },
        "node",
      ],
      react: {
        version: "detect",
      },
      "better-tailwindcss": {
        entryPoint: "src/styles/globals.css",
        tailwindConfig: "",
        attributes: ["class", "className"],
        callees: ["cc", "clb", "clsx", "cn", "cnb", "ctl", "cva", "cx", "dcnb", "objstr", "tv", "twJoin", "twMerge"],
        variables: ["className", "classNames", "classes", "style", "styles"],
        tags: ["myTag"],
      },
    },
    files: ["**/*.{js,jsx,ts,tsx,cjs,mts,cts}"],
    plugins: {
      "import-x": importX,
      "@typescript-eslint": tsEslint.plugin,
      unicorn,
      security: security as unknown as typeof importX,
      sonarjs,
      perfectionist,
      n: nodePlugin,
      "react-refresh": reactRefresh,
      // eslint-disable-next-line @typescript-eslint/no-unsafe-assignment
      drizzle,
      "better-tailwindcss": betterTailwind,
      zod,
      jest,
      "testing-library": testingLibrary,
      playwright,
      js,
    },
    rules: {
      // ----- TypeScript-ESLint -----
      "require-await": "off",
      "@typescript-eslint/require-await": "off",
      "@typescript-eslint/no-floating-promises": ["warn", { ignoreVoid: true }],
      "@typescript-eslint/no-unused-vars": [
        "warn",
        {
          argsIgnorePattern: "^_",
          varsIgnorePattern: "^_",
        },
      ],
      "@typescript-eslint/no-explicit-any": "error",
      "@typescript-eslint/ban-ts-comment": ["error", { "ts-expect-error": false }],
      "@typescript-eslint/consistent-type-imports": [
        "warn",
        {
          prefer: "type-imports",
          fixStyle: "inline-type-imports",
        },
      ],
      "@typescript-eslint/no-import-type-side-effects": "error",

      // ----- Import-X -----
      "import-x/order": "off",
      "import-x/no-unresolved": "off",
      "import-x/no-duplicates": "warn",
      "import-x/no-named-as-default": "warn",
      "import-x/no-named-as-default-member": "warn",

      // ----- Node/Import Resolution -----
      "n/no-missing-import": "off",

      // ----- Perfectionist (disabled - causes too many false positives) -----
      "perfectionist/sort-objects": "off",
      "perfectionist/sort-imports": "off",

      // ----- Testing Library -----
      "testing-library/no-await-sync-queries": "off",
      "react-hooks/rules-of-hooks": "error",
      "react-hooks/exhaustive-deps": "warn",

      // ----- JSX Accessibility -----
      "jsx-a11y/alt-text": "warn",
      "jsx-a11y/anchor-has-content": "warn",
      "jsx-a11y/anchor-is-valid": "warn",
      "jsx-a11y/aria-props": "warn",
      "jsx-a11y/aria-role": "warn",
      "jsx-a11y/click-events-have-key-events": "warn",
      "jsx-a11y/heading-has-content": "warn",
      "jsx-a11y/html-has-lang": "warn",
      "jsx-a11y/img-redundant-alt": "warn",
      "jsx-a11y/interactive-supports-focus": "warn",
      "jsx-a11y/label-has-associated-control": "warn",
      "jsx-a11y/no-autofocus": "warn",
      "jsx-a11y/no-redundant-roles": "warn",
      "jsx-a11y/no-static-element-interactions": "warn",
      "jsx-a11y/role-has-required-aria-props": "warn",
      "jsx-a11y/tabindex-no-positive": "warn",

      // ----- Unicorn -----
      "unicorn/filename-case": [
        "warn",
        {
          case: "kebabCase",
          ignore: [
            // Next.js special files
            "^layout\\.tsx?$",
            "^page\\.tsx?$",
            "^error\\.tsx?$",
            "^loading\\.tsx?$",
            "^not-found\\.tsx?$",
            "^template\\.tsx?$",
            "^default\\.tsx?$",
            "^route\\.ts$",
            // React components (PascalCase allowed)
            "^[A-Z][a-zA-Z0-9]*\\.tsx$",
            // Test files
            ".*\\.test\\.tsx?$",
            ".*\\.spec\\.tsx?$",
            // Config files
            "^[A-Z][A-Z0-9_]*\\.md$",
            // Special directories
            "^__[a-zA-Z0-9_]+__$",
            // Root config files
            "^appConfig\\.ts$",
          ],
        },
      ],
      "unicorn/prefer-node-protocol": "warn",
      "unicorn/no-abusive-eslint-disable": "off",
      "unicorn/no-array-for-each": "warn",
      "unicorn/prefer-array-find": "warn",
      "unicorn/prefer-array-flat-map": "warn",
      "unicorn/prefer-string-replace-all": "warn",

      // ----- Security -----
      "security/detect-eval-with-expression": "warn",
      "security/detect-non-literal-fs-filename": "warn",
      "security/detect-non-literal-regexp": "warn",
      "security/detect-object-injection": "warn",
      "security/detect-possible-timing-attacks": "warn",
      "security/detect-unsafe-regex": "warn",

      // ----- SonarJS -----
      "sonarjs/cognitive-complexity": "off",
      "sonarjs/no-duplicate-string": ["warn", { threshold: 8 }],
      "sonarjs/no-identical-functions": "warn",
      "sonarjs/no-collapsible-if": "warn",
      "sonarjs/prefer-immediate-return": "warn",

      // ----- Perfectionist -----
      "perfectionist/sort-named-imports": [
        "warn",
        {
          type: "alphabetical",
          order: "asc",
        },
      ],
      "perfectionist/sort-named-exports": [
        "warn",
        {
          type: "alphabetical",
          order: "asc",
        },
      ],
      "perfectionist/sort-object-types": [
        "warn",
        {
          type: "alphabetical",
          order: "asc",
        },
      ],
      "perfectionist/sort-interfaces": [
        "warn",
        {
          type: "alphabetical",
          order: "asc",
        },
      ],
      "perfectionist/sort-jsx-props": [
        "warn",
        {
          type: "alphabetical",
          order: "asc",
          ignoreCase: true,
        },
      ],
      "perfectionist/sort-union-types": [
        "warn",
        {
          type: "alphabetical",
          order: "asc",
        },
      ],

      // ----- Node.js (n) -----
      "n/no-deprecated-api": "warn",
      "n/no-unsupported-features/es-syntax": "error",
      "n/prefer-promises/fs": "warn",
      "n/prefer-promises/dns": "warn",

      // ----- General code quality -----
      "no-console": ["warn", { allow: ["warn", "error"] }],
      "no-debugger": "error",
      "prefer-const": "error",
      "prefer-arrow-callback": "warn",
      eqeqeq: "error",
      "@typescript-eslint/no-empty-object-type": "warn",
      "react-refresh/only-export-components": [
        "warn",
        {
          allowConstantExport: true,
          allowExportNames: [
            "metadata",
            "generateMetadata",
            "viewport",
            "generateViewport",
            "generateStaticParams",
            "revalidate",
            "fetchCache",
            "runtime",
            "preferredRegion",
            "maxDuration",
          ],
        },
      ],
      "better-tailwindcss/enforce-consistent-class-order": "warn",
      "better-tailwindcss/no-conflicting-classes": "warn",
      "better-tailwindcss/no-duplicate-classes": "warn",
      "better-tailwindcss/no-unnecessary-whitespace": "warn",
      "drizzle/enforce-delete-with-where": [
        "warn",
        {
          drizzleObjectName: ["db", "tx"],
        },
      ],
      "drizzle/enforce-update-with-where": [
        "warn",
        {
          drizzleObjectName: ["db", "tx"],
        },
      ],

      // ----- Jest (also works for vitest) -----
      "jest/no-disabled-tests": "warn",
      "jest/no-focused-tests": "error",
      "jest/no-identical-title": "warn",
      "jest/valid-expect": "warn",
      "jest/expect-expect": "warn",

      // ----- Testing Library -----
      "testing-library/await-async-queries": "warn",
      "testing-library/await-async-utils": "warn",
      "testing-library/no-debugging-utils": "off",
      "testing-library/no-dom-import": "warn",
      "testing-library/prefer-screen-queries": "warn",
      ...playwright.configs["flat/recommended"].rules,
      "playwright/no-standalone-expect": "off",
      "playwright/no-wait-for-timeout": "warn",
      "playwright/prefer-web-first-assertions": "warn",
      "playwright/expect-expect": "warn",
      "playwright/no-focused-test": "error",
      "playwright/no-skipped-test": "warn",
      "playwright/valid-expect": "warn",
      "playwright/no-networkidle": "warn",
      "playwright/no-conditional-in-test": "warn",
      "playwright/no-conditional-expect": "warn",
      "playwright/no-wait-for-navigation": "warn",
      "playwright/no-useless-await": "warn",

      // ----- Next.js -----
      "@next/next/no-img-element": "warn",
      "@next/next/no-html-link-for-pages": "error",
      "@next/next/no-sync-scripts": "error",
      "@next/next/no-duplicate-head": "error",
      "@next/next/google-font-display": "warn",
    },
  },

  // ===========================
  // React Server Components (RSC) - Strict rules
  // ===========================
  // {
  //   files: ["src/app/**/*.tsx", "src/components/**/*.tsx"],
  //   rules: {
  //     "no-console": ["warn", { allow: ["warn", "error"] }],
  //   },
  // },

  // ===========================
  // Test files - Relaxed rules
  // ===========================
  {
    files: [
      "src/**/*.test.ts",
      "src/**/*.test.tsx",
      "src/**/*.spec.ts",
      "src/**/*.spec.tsx",
      "src/tests/**/*.ts",
      "src/tests/**/*.tsx",
    ],
    rules: {
      "@typescript-eslint/no-explicit-any": "off",
      "@typescript-eslint/require-await": "off",
      "security/detect-object-injection": "off",
      "security/detect-unsafe-regex": "off",
      "no-console": "off",
      "playwright/no-standalone-expect": "off",
      "@typescript-eslint/no-unsafe-assignment": "off",
      "@typescript-eslint/no-unsafe-call": "off",
      "@typescript-eslint/no-unsafe-member-access": "off",
      "@typescript-eslint/no-unsafe-return": "off",
      "@typescript-eslint/no-misused-promises": "off",
      "@typescript-eslint/unbound-method": "off",
      "@typescript-eslint/consistent-type-imports": "off",
      "@typescript-eslint/no-floating-promises": "off",
      "playwright/no-conditional-in-test": "off",
      "playwright/no-conditional-expect": "off",
      "playwright/no-networkidle": "off",
      "playwright/no-wait-for-navigation": "off",
      "sonarjs/no-duplicate-string": "off",
      "testing-library/prefer-screen-queries": "off",
      "playwright/expect-expect": "off",
      "playwright/no-skipped-test": "off",
      "playwright/no-wait-for-timeout": "off",
      "playwright/prefer-locator": "off",
    },
  },

  // ===========================
  // Database & ORM - Drizzle specific
  // ===========================
  // {
  //   files: ["src/database/**/*.ts", "src/dal/**/*.ts"],
  //   rules: {
  //     "drizzle/enforce-delete-with-where": "error",
  //     "drizzle/enforce-update-with-where": "error",
  //     "sonarjs/cognitive-complexity": "warn",
  //   },
  // },

  // ===========================
  // Scripts - Relaxed rules (CLI tools)
  // ===========================
  {
    files: ["src/scripts/**/*.ts"],
    rules: {
      "no-console": "off",
      "security/detect-object-injection": "off",
      "security/detect-non-literal-fs-filename": "off",
      "security/detect-non-literal-regexp": "off",
      "security/detect-unsafe-regex": "off",
      "sonarjs/cognitive-complexity": "off",
      "sonarjs/no-collapsible-if": "off",
      "testing-library/no-await-sync-queries": "off",
      "testing-library/no-debugging-utils": "off",
      "@typescript-eslint/no-explicit-any": "off",
      "@typescript-eslint/no-unsafe-assignment": "off",
      "@typescript-eslint/no-unsafe-call": "off",
      "@typescript-eslint/no-unsafe-member-access": "off",
      "@typescript-eslint/no-unsafe-return": "off",
      "@typescript-eslint/restrict-template-expressions": "off",
      "@typescript-eslint/no-unused-vars": "off",
      "@typescript-eslint/await-thenable": "off",
      "@typescript-eslint/no-floating-promises": "off",
      "@typescript-eslint/consistent-type-imports": "off",
      eqeqeq: "off",
      "unicorn/filename-case": "off",
      "unicorn/no-array-for-each": "off",
      "unicorn/no-abusive-eslint-disable": "off",
      "perfectionist/sort-named-imports": "off",
      "perfectionist/sort-object-types": "off",
      "perfectionist/sort-union-types": "off",
    },
  },

  // ===========================
  // Lib & Hooks - Relaxed console rules
  // ===========================
  {
    files: ["src/lib/**/*.ts", "src/lib/**/*.tsx", "src/hooks/**/*.ts", "src/hooks/**/*.tsx"],
    rules: {
      "no-console": "off",
    },
  },

  // ===========================
  // Server Actions - Relaxed rules (Drizzle queries are sync)
  // ===========================
  // {
  //   files: ["src/actions/**/*.ts"],
  //   rules: {
  //     "testing-library/no-await-sync-queries": "warn",
  //   },
  // },

  // ===========================
  // Stores - Relaxed rules
  // ===========================
  {
    files: ["src/stores/**/*.ts"],
    rules: {
      "security/detect-object-injection": "off",
    },
  },

  // ===========================
  // UI Components - Relaxed fast-refresh rules
  // ===========================
  {
    files: ["src/components/ui/**/*.tsx"],
    rules: {
      "react-refresh/only-export-components": "off",
      "jsx-a11y/anchor-is-valid": "off",
      "jsx-a11y/anchor-has-content": "off",
      "jsx-a11y/click-events-have-key-events": "off",
      "security/detect-object-injection": "off",
      "jsx-a11y/no-autofocus": "off",
      "@typescript-eslint/no-unused-vars": "off",
    },
  },

  // ===========================
  // Reading Components - Relaxed rules
  // ===========================
  {
    files: ["src/components/reading/**/*.tsx"],
    rules: {
      "security/detect-object-injection": "off",
      "jsx-a11y/no-static-element-interactions": "off",
      "@typescript-eslint/no-floating-promises": "off",
      "jsx-a11y/label-has-associated-control": "off",
    },
  },

  // ===========================
  // Search Components - Relaxed rules
  // ===========================
  {
    files: ["src/components/search/**/*.tsx"],
    rules: {
      "security/detect-object-injection": "off",
    },
  },

  // ===========================
  // Settings Components - Relaxed rules
  // ===========================
  {
    files: ["src/components/settings/**/*.tsx"],
    rules: {
      "jsx-a11y/label-has-associated-control": "off",
    },
  },

  // ===========================
  // Optimized Components - Relaxed rules
  // ===========================
  {
    files: ["src/components/optimized/**/*.tsx"],
    rules: {
      "no-console": "off",
      "security/detect-object-injection": "off",
    },
  },

  // ===========================
  // Profile Components - Relaxed rules
  // ===========================
  {
    files: ["src/components/profile/**/*.tsx"],
    rules: {
      "jsx-a11y/label-has-associated-control": "off",
    },
  },

  // ===========================
  // Bookmarks Components - Relaxed rules
  // ===========================
  {
    files: ["src/components/bookmarks/**/*.tsx"],
    rules: {
      "security/detect-object-injection": "off",
    },
  },

  // ===========================
  // Comics Components - Relaxed rules
  // ===========================
  {
    files: ["src/components/comics/**/*.tsx"],
    rules: {
      "security/detect-object-injection": "off",
    },
  },

  // ===========================
  // Reading Components - Relaxed rules
  // ===========================
  // {
  //   files: ["src/components/reading/**/*.tsx"],
  //   rules: {
  //     "security/detect-object-injection": "warn",
  //     "jsx-a11y/no-static-element-interactions": "warn",
  //     "@typescript-eslint/no-floating-promises": "warn",
  //   },
  // },

  // ===========================
  // Optimized Components - Relaxed rules
  // ===========================
  // {
  //   files: ["src/components/optimized/**/*.tsx"],
  //   rules: {
  //     "no-console": "warn",
  //     "security/detect-object-injection": "warn",
  //   },
  // },

  // ===========================
  // Layout Components - Relaxed anchor rules
  // ===========================
  // {
  //   files: ["src/components/layout/**/*.tsx"],
  //   rules: {
  //     "jsx-a11y/anchor-is-valid": "warn",
  //   },
  // },

  // ===========================
  // Configuration files
  // ===========================
  // {
  //   files: ["*.config.ts", "*.config.mts", "*.config.js", "appConfig.ts"],
  //   rules: {
  //     "no-console": "warn",
  //     "unicorn/filename-case": "warn",
  //   },
  // },

  // ===========================
  // Plain JS config files (.mjs) — disable type-checked rules
  // These files are not included in tsconfig and cannot use typed linting
  // ===========================
  {
    files: ["**/*.mjs"],
    ...tsEslint.configs.disableTypeChecked,
  },

  // ===========================
  // Generated/Third-party Type Files
  // ===========================
  {
    files: ["src/types/eslint-plugin-drizzle-generated.d.ts"],
    rules: {
      "@typescript-eslint/no-explicit-any": "off",
    },
  },

  // ===========================
  // Prettier (MUST BE LAST)
  // ===========================
  prettier,
]);

export default eslintConfig;
