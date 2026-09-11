import js from "@eslint/js";
import globals from "globals";
import tseslint from "typescript-eslint";

export default [
	{
		// Submodules are separate repos with their own configs/deps (see
		// projects/*/AGENTS.md). Root lint covers meta-repo code only.
		ignores: [
			"projects/**",
			"**/node_modules/**",
			".next/**",
			"out/**",
			"dist/**",
			"build/**",
			"coverage/**",
			".eslintcache",
		],
	},
	js.configs.recommended,
	...tseslint.configs.recommended,
	{
		languageOptions: {
			ecmaVersion: "latest",
			sourceType: "module",
			globals: {
				...globals.node,
				...globals.es2021,
				...globals.browser,
			},
		},
		rules: {
			"@typescript-eslint/no-unused-vars": ["warn", { argsIgnorePattern: "^_" }],
			"@typescript-eslint/no-explicit-any": "warn",
			"no-console": "off",
		},
	},
];