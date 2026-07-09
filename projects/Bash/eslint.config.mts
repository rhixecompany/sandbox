import eslintReact from "@eslint-react/eslint-plugin";
import js from "@eslint/js";
import nextPlugin from "@next/eslint-plugin-next";
import tsEslintParser from "@typescript-eslint/parser";
import prettier from "eslint-config-prettier";
import betterTailwind from "eslint-plugin-better-tailwindcss";
import drizzle from "eslint-plugin-drizzle";
import importX from "eslint-plugin-import-x";
import jest from "eslint-plugin-jest";
import jsdoc from "eslint-plugin-jsdoc";
import jsxA11y from "eslint-plugin-jsx-a11y";
import nodePlugin from "eslint-plugin-n";
import noSecrets from "eslint-plugin-no-secrets";
import perfectionist from "eslint-plugin-perfectionist";
import reactRefresh from "eslint-plugin-react-refresh";
import regexp from "eslint-plugin-regexp";
import security from "eslint-plugin-security";
import sonarjs from "eslint-plugin-sonarjs";
import testingLibrary from "eslint-plugin-testing-library";
import unicorn from "eslint-plugin-unicorn";
import zod from "eslint-plugin-zod";
import { defineConfig, globalIgnores } from "eslint/config";
import globals from "globals";
import tsEslint from "typescript-eslint";

export default defineConfig([
  js.configs.recommended,
  tsEslint.configs.recommended,
  tsEslint.configs.strict,
  tsEslint.configs.stylistic,

  nextPlugin.configs.recommended,
  nextPlugin.configs["core-web-vitals"],

  globalIgnores(["out/**", "build/**", "dist/**", "node_modules/**"]),
  {
    files: ["**/*.{js,jsx,ts,tsx,cjs,mts,cts}"],
    languageOptions: {
      ecmaVersion: 2024,
      globals: {
        ...globals.browser,
        ...globals.node,
        ...globals.es2024,
        ...globals.jest,
        afterAll: "readonly",
        afterEach: "readonly",
        beforeAll: "readonly",
        beforeEach: "readonly",
        describe: "readonly",
        expect: "readonly",
        it: "readonly",
        test: "readonly",
        vi: "readonly",
      },
      parser: tsEslintParser,
      parserOptions: {
        ecmaFeatures: {
          jsx: true,
        },
        ecmaVersion: 2024,
        projectService: {
          allowDefaultProject: [
            ".prettierrc.ts",
            "postcss.config.mjs",
            ".lintstagedrc.ts",
          ],
        },
        sourceType: "module",
      },
      sourceType: "module",
    },
    linterOptions: {
      noInlineConfig: false,
      reportUnusedDisableDirectives: false,
    },
    plugins: {
      "@typescript-eslint": tsEslint.plugin,
      "better-tailwindcss": betterTailwind as unknown as typeof importX,
      drizzle,
      "import-x": importX,
      jest,
      js,
      jsdoc,
      "jsx-a11y": jsxA11y,
      n: nodePlugin,
      "no-secrets": noSecrets,
      perfectionist,

      // playwright,
      "@eslint-react": eslintReact,
      "react-refresh": reactRefresh,
      regexp,
      security: security as unknown as typeof importX,
      sonarjs,
      "testing-library": testingLibrary,
      unicorn,
      // vitest,
      zod,
    },
    rules: {
      "@next/next/no-img-element": "warn", // Sometimes intentional
      "@typescript-eslint/explicit-function-return-type": "off", // Too strict
      "@typescript-eslint/explicit-module-boundary-types": "off", // Too strict
      "@typescript-eslint/no-explicit-any": "off", // Sometimes needed
      "@typescript-eslint/no-floating-promises": "warn", // Too strict
      "@typescript-eslint/no-misused-promises": "off", // React forms need async handlers
      "@typescript-eslint/no-unsafe-assignment": "off", // Sometimes needed
      "@typescript-eslint/no-unsafe-call": "off", // Sometimes needed
      "@typescript-eslint/no-unsafe-member-access": "off", // Sometimes needed
      // =====================================================
      // TYPESCRIPT-ESLINT - TypeScript Best Practices
      // =====================================================
      "@typescript-eslint/no-unused-vars": "off", // Sometimes intentional
      "@typescript-eslint/prefer-nullish-coalescing": "warn", // Sometimes || is intentional
      "@typescript-eslint/prefer-optional-chain": "warn", // Sometimes intentional

      "@typescript-eslint/require-await": "warn", // Too strict
      // =====================================================
      // BETTER TAILWINDCSS - Tailwind CSS Best Practices
      // =====================================================
      "better-tailwindcss/enforce-consistent-class-order": "error",
      "better-tailwindcss/enforce-shorthand-classes": "warn", // Too strict
      "better-tailwindcss/no-conflicting-classes": "warn", // Too strict
      "better-tailwindcss/no-deprecated-classes": "warn",
      "better-tailwindcss/no-duplicate-classes": "warn",

      "better-tailwindcss/no-unknown-classes": [
        "warn",
        {
          ignore: [
            // Tailwind v4 animation classes
            "animate-in",
            "animate-out",
            "fade-in-",
            "fade-out-",
            "zoom-in-",
            "zoom-out-",
            "slide-in",
            "slide-out",
            // Tailwind v4 data-attribute patterns
            "data-\\[state=",
            "data-\\[side=",
            // Sonner toast component class
            "toaster",
            // Project design-system classes (whitelist)
            "card",
            "card-header",
            "card-body",
            "card-footer",
            "datatable",
            "simple-form",
            "form-errors",
            "row-item",
            "field",
          ],
        },
      ], // Tailwind v4 animation classes
      curly: ["error", "all"],
      // =====================================================
      // DRIZZLE ORM - Database Best Practices
      // =====================================================
      "drizzle/enforce-delete-with-where": "off", // False positives on non-DB files
      "drizzle/enforce-update-with-where": "warn", // Sometimes intentional

      eqeqeq: "warn", // Sometimes == is intentional
      "import-x/default": "warn", // Too strict
      "import-x/named": "warn", // Too strict
      "import-x/namespace": "warn", // Too strict
      "import-x/no-duplicates": "warn", // Allow duplicates
      "import-x/no-unresolved": "warn", // Let TypeScript handle this
      // =====================================================
      // IMPORT-X - Import Organization
      // =====================================================
      "import-x/order": "off", // Conflicts with perfectionist/sort-imports

      // =====================================================
      // JSDOC - JSDoc comment quality
      // =====================================================
      "jsdoc/check-param-names": "warn",
      "jsdoc/check-tag-names": ["warn", { definedTags: ["export"] }],

      "jsdoc/check-types": "warn",
      "jsdoc/no-undefined-types": "off", // Too strict with TS generics
      "jsdoc/require-jsdoc": "off", // Don't require JSDoc on every function
      "jsdoc/require-param": "off", // TypeScript types make this redundant
      "jsdoc/require-param-description": "off", // Descriptions are optional
      "jsdoc/require-param-type": "off", // TypeScript types make this redundant
      "jsdoc/require-returns": "off", // TypeScript return types make this redundant
      "jsdoc/require-returns-description": "off", // Descriptions are optional

      "jsdoc/tag-lines": "off",
      // =====================================================
      // NODE.JS - Node.js Best Practices
      // =====================================================
      "n/no-process-env": "warn", // Config files need this
      "n/no-unpublished-import": "warn", // Too strict
      "n/no-unsupported-features/es-builtins": "warn", // Too strict
      // =====================================================
      // GENERAL JavaScript - Base ESLint Rules
      // =====================================================
      "no-console": "warn", // Console.log is intentional
      "no-debugger": "error",
      "no-dupe-else-if": "error",

      "no-duplicate-case": "error",
      "no-empty": "warn",
      "no-extra-semi": "warn", // Handled by Prettier
      "no-param-reassign": "warn", // Sometimes needed
      // =====================================================
      // NO-SECRETS - Prevent accidental secret commits
      // Threshold raised to reduce false positives on long tokens/URLs
      // =====================================================
      "no-secrets/no-secrets": ["warn", { tolerance: 4.2 }],
      "no-unreachable": "error",

      "no-unsafe-negation": "error",
      "no-unsafe-optional-chaining": "error",

      // Disable strict rules that cause errors
      "no-useless-assignment": "warn", // Too strict
      "no-var": "error",
      // =====================================================
      // PERFECTIONIST - Auto-sorting
      // =====================================================
      "perfectionist/sort-imports": "warn", // Too strict
      "perfectionist/sort-intersection-types": "warn", // Too strict
      "perfectionist/sort-objects": "warn", // Too strict
      "perfectionist/sort-union-types": "warn", // Too strict

      "prefer-const": "error",
      "preserve-caught-error": "warn", // Not all errors need cause
      "@eslint-react/exhaustive-deps": "warn",
      "@eslint-react/purity": "warn", // React compiler warnings
      "@eslint-react/rules-of-hooks": "error",
      // =====================================================
      // REACT REFRESH - Hot Reloading Compatibility
      // =====================================================
      "react-refresh/only-export-components": "off", // Too strict for this project
      // =====================================================
      // REGEXP - Regular expression correctness and safety
      // Complements security/detect-unsafe-regex
      // =====================================================
      "regexp/no-contradiction-with-assertion": "error",
      "regexp/no-control-character": "warn",
      "regexp/no-dupe-characters-character-class": "error",
      "regexp/no-empty-alternative": "warn",
      "regexp/no-empty-capturing-group": "warn",

      "regexp/no-empty-character-class": "error",
      "regexp/no-empty-group": "warn",
      "regexp/no-invalid-regexp": "error",
      "regexp/no-lazy-ends": "warn",
      "regexp/no-obscure-range": "warn",
      "regexp/no-optional-assertion": "error",
      "regexp/no-potentially-useless-backreference": "warn",
      "regexp/no-super-linear-backtracking": "error",
      "regexp/no-super-linear-move": "warn",
      "regexp/no-useless-assertions": "warn",
      "regexp/no-useless-character-class": "warn",
      "regexp/no-useless-escape": "warn",
      "regexp/no-useless-flag": "warn",
      "regexp/no-useless-non-capturing-group": "warn",
      "regexp/no-useless-quantifier": "warn",
      "regexp/no-zero-quantifier": "error",
      "regexp/prefer-character-class": "warn",
      "regexp/prefer-plus-quantifier": "warn",
      "regexp/prefer-question-quantifier": "warn",
      "regexp/prefer-star-quantifier": "warn",
      "regexp/prefer-w": "warn",
      "regexp/simplify-set-operations": "warn",
      "regexp/sort-alternatives": "off", // Too strict — order may be intentional
      "regexp/use-ignore-case": "warn",
      "require-await": "warn", // Too strict
      "security/detect-eval-with-expression": "error",
      "security/detect-non-literal-fs-filename": "error",
      "security/detect-non-literal-regexp": "warn", // Test files use dynamic regex
      "security/detect-non-literal-require": "error",
      "security/detect-possible-timing-attacks": "warn", // Too strict
      // =====================================================
      // SECURITY - Node.js Security
      // =====================================================
      "security/detect-unsafe-regex": "error",
      "sonarjs/cognitive-complexity": "off", // Sometimes intentional
      // =====================================================
      // SONARJS - Code Quality & Bugs
      // Using recommended config from plugin
      // =====================================================
      "sonarjs/no-all-duplicated-branches": "warn", // Too strict
      "sonarjs/no-collapsible-if": "warn", // Too strict
      "sonarjs/no-duplicate-string": "off", // Sometimes intentional
      "sonarjs/no-redundant-jump": "warn", // Too strict
      "sonarjs/no-small-switch": "warn", // Sometimes intentional
      // =====================================================
      // UNICORN - Modern JavaScript/TypeScript Best Practices
      // =====================================================
      "unicorn/filename-case": [
        "error",
        {
          cases: {
            camelCase: true,
            kebabCase: true,
            pascalCase: true,
          },
          ignore: [
            "^\\.env",
            "^\\.gitignore",
            "^tsconfig",
            "^next",
            "^jest",
            "^vitest",
            "^playwright",
            "^README",
            "^AGENTS",
            "^CHANGELOG",
            "^CONTRIBUTING",
            "^LICENSE",
            "^SKILL",
            "^node_mcp_server",
            "\\.md$",
          ],
        },
      ],
      "unicorn/no-abusive-eslint-disable": "error",
      "unicorn/no-array-for-each": "warn", // forEach is readable
      "unicorn/no-null": "warn", // Project uses null intentionally
      "unicorn/prefer-at": "warn", // Too strict
      "unicorn/prefer-includes": "error",
      "unicorn/prefer-number-properties": "warn", // Too strict
      "unicorn/prefer-object-from-entries": "warn", // Too strict
      "unicorn/prefer-optional-catch-binding": "warn", // Too strict
      "unicorn/prefer-string-replace-all": "warn", // Too strict
      "unicorn/prefer-string-slice": "error",
      "unicorn/throw-new-error": "error",
      "zod/no-any-schema": "error",
      "zod/no-empty-custom-schema": "error",
      "zod/no-optional-and-default-together": "error",
      "zod/no-unknown-schema": "error",
      "zod/prefer-meta": "error",
      "zod/prefer-string-schema-with-trim": "warn", // Too strict
      // =====================================================
      // ZOD - Schema Validation Best Practices
      // =====================================================
      "zod/require-error-message": "error",
      "zod/require-schema-suffix": "off", // Too strict
    },
    settings: {
      "better-tailwindcss": {
        attributes: ["class", "className"],
        callees: [
          "cc",
          "clb",
          "clsx",
          "cn",
          "cnb",
          "ctl",
          "cva",
          "cx",
          "dcnb",
          "objstr",
          "tv",
          "twJoin",
          "twMerge",
        ],
        // entryPoint: "./src/app/globals.css",
        // Tailwind v4 animation patterns
        knownAnimations: [
          "animate-in",
          "animate-out",
          "fade-in",
          "fade-out",
          "zoom-in",
          "zoom-out",
          "slide-in",
          "slide-out",
        ],
        // Add known project-specific utility classes so the plugin doesn't flag them
        knownClasses: [
          "card",
          "card-header",
          "card-body",
          "card-footer",
          "datatable",
          "simple-form",
          "form-errors",
          "row-item",
          "field",
        ],
        tags: ["myTag"],
        tailwindConfig: "",
        variables: ["className", "classNames", "classes", "style", "styles"],
      },
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
    },
  },
  prettier,
]);
