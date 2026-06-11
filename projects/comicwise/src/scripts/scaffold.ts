#!/usr/bin/env tsx
/**
 * ═══════════════════════════════════════════════════════════════════════════
 * Advanced Scaffold Generator (ENHANCED)
 * ═══════════════════════════════════════════════════════════════════════════
 *
 * Scaffolds new files following project conventions:
 * - React Components with TypeScript
 * - Server Components (Next.js)
 * - Server Actions
 * - Data Access Layer (DAL) modules
 * - Zod validation schemas
 * - Next.js Pages with metadata
 *
 * All templates include:
 * - JSDoc documentation
 * - TypeScript types
 * - "use client" / "use server" directives (as appropriate)
 * - Project-standard structure and imports
 *
 * Usage:
 *   pnpm scaffold component ComicCard              # Creates Client Component
 *   pnpm scaffold action updateComic               # Creates Server Action
 *   pnpm scaffold dal Comic                        # Creates Data Access Layer
 *   pnpm scaffold page ComicDetail                 # Creates Server Page
 *   pnpm scaffold schema Comic                     # Creates Zod Schema
 *
 * Flags:
 *   --force                  Overwrite existing files
 *   --dry-run                Show what would be created without creating
 *   --yes                    Skip confirmation prompts
 */

import { existsSync } from "node:fs";
import { mkdir, writeFile } from "node:fs/promises";
import { join } from "node:path";

import { confirmAction } from "./shared/confirmAction";

// ═══════════════════════════════════════════════════════════════════════════
// UTILITY FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Convert PascalCase to kebab-case
 */
function toKebabCase(str: string): string {
  return str.replaceAll(/([a-z0-9])([A-Z])/g, "$1-$2").toLowerCase();
}

/**
 * Convert kebab-case to PascalCase
 */
function toPascalCase(str: string): string {
  return str
    .split("-")
    .map((word) => word.charAt(0).toUpperCase() + word.slice(1).toLowerCase())
    .join("");
}

// ═══════════════════════════════════════════════════════════════════════════
// TEMPLATE DEFINITIONS
// ═══════════════════════════════════════════════════════════════════════════

const templates = {
  /**
   * Client Component Template
   */
  component: (name: string) => {
    const pascalName = toPascalCase(name);
    const kebabName = toKebabCase(name);
    return `/**
 * ${pascalName} Component
 *
 * @component
 * A reusable React component that renders [description].
 *
 * @example
 * <${pascalName} />
 */

"use client";

import type { FC } from "react";

export interface ${pascalName}Props {
  /** Additional CSS classes */
  className?: string;
}

/**
 * Renders the ${pascalName} component
 */
export const ${pascalName}: FC<${pascalName}Props> = ({ className = "" }) => {
  return (
    <div className={className}>
      {/* ${pascalName} content */}
    </div>
  );
};

export default ${pascalName};
`;
  },

  /**
   * Server Action Template
   */
  action: (name: string) => {
    const camelName = name.charAt(0).toLowerCase() + name.slice(1);
    const kebabName = toKebabCase(name);
    return `/**
 * ${camelName} Server Action
 *
 * Handles [description] on the server side.
 */

"use server";

import { ActionResult } from "@/types/actions";

/**
 * ${camelName} Action
 *
 * @param data - Input data for the action
 * @returns Action result with success/error status
 */
export async function ${camelName}(
  data: unknown
): Promise<ActionResult<unknown>> {
  try {
    // Validate input
    // const validData = schema.parse(data);

    // TODO: Implement server logic

    return {
      ok: true,
      data: null,
    };
  } catch (error) {
    console.error("[${camelName}] Error:", error);

    return {
      ok: false,
      error: error instanceof Error ? error.message : "An error occurred",
    };
  }
}
`;
  },

  /**
   * Data Access Layer (DAL) Template
   */
  dal: (name: string) => {
    const pascalName = toPascalCase(name);
    const lowerName = name.toLowerCase();
    return `/**
 * ${pascalName} Data Access Layer
 *
 * Handles database operations for ${lowerName} entities.
 */

import { db } from "@/database/db";
import { ${lowerName}s } from "@/database/schema";
import { eq } from "drizzle-orm";

export type ${pascalName} = typeof ${lowerName}s.$inferSelect;
export type New${pascalName} = typeof ${lowerName}s.$inferInsert;

/**
 * Fetch all ${lowerName} records
 */
export async function getAll${pascalName}s() {
  try {
    return await db.select().from(${lowerName}s);
  } catch (error) {
    console.error("[getAll${pascalName}s] Error:", error);
    throw error;
  }
}

/**
 * Fetch a single ${lowerName} by ID
 */
export async function get${pascalName}ById(id: string) {
  try {
    const [record] = await db
      .select()
      .from(${lowerName}s)
      .where(eq(${lowerName}s.id, id));
    return record ?? null;
  } catch (error) {
    console.error("[get${pascalName}ById] Error:", error);
    throw error;
  }
}

/**
 * Create a new ${lowerName}
 */
export async function create${pascalName}(data: New${pascalName}) {
  try {
    const [record] = await db
      .insert(${lowerName}s)
      .values(data)
      .returning();
    return record;
  } catch (error) {
    console.error("[create${pascalName}] Error:", error);
    throw error;
  }
}

/**
 * Update an existing ${lowerName}
 */
export async function update${pascalName}(
  id: string,
  data: Partial<New${pascalName}>
) {
  try {
    const [record] = await db
      .update(${lowerName}s)
      .set(data)
      .where(eq(${lowerName}s.id, id))
      .returning();
    return record ?? null;
  } catch (error) {
    console.error("[update${pascalName}] Error:", error);
    throw error;
  }
}

/**
 * Delete a ${lowerName}
 */
export async function delete${pascalName}(id: string) {
  try {
    await db.delete(${lowerName}s).where(eq(${lowerName}s.id, id));
  } catch (error) {
    console.error("[delete${pascalName}] Error:", error);
    throw error;
  }
}
`;
  },

  /**
   * Next.js Server Page Template
   */
  page: (name: string) => {
    const pascalName = toPascalCase(name);
    return `/**
 * ${pascalName} Page
 *
 * Server component for the ${pascalName} page.
 */

import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "${pascalName}",
  description: "${pascalName} page description",
};

/**
 * ${pascalName} Page
 *
 * @returns JSX for the ${pascalName} page
 */
export default function ${pascalName}Page() {
  return (
    <main className="container mx-auto py-8">
      <h1 className="text-3xl font-bold mb-4">${pascalName}</h1>
      {/* Page content */}
    </main>
  );
}
`;
  },

  /**
   * Zod Validation Schema Template
   */
  schema: (name: string) => {
    const pascalName = toPascalCase(name);
    const lowerName = name.toLowerCase();
    return `/**
 * ${pascalName} Validation Schema
 *
 * Zod schemas for validating ${lowerName} data.
 */

import { z } from "zod";

/**
 * Base ${pascalName} schema with common fields
 */
export const base${pascalName}Schema = z.object({
  // TODO: Define fields
  // id: z.string().uuid(),
  // createdAt: z.date(),
});

/**
 * Schema for creating a new ${pascalName}
 */
export const create${pascalName}Schema = base${pascalName}Schema.omit({
  // id: true,
  // createdAt: true,
});

/**
 * Schema for updating a ${pascalName}
 */
export const update${pascalName}Schema = create${pascalName}Schema.partial();

/**
 * Schema for ${pascalName} responses
 */
export const ${pascalName}ResponseSchema = base${pascalName}Schema;

export type ${pascalName} = z.infer<typeof base${pascalName}Schema>;
export type Create${pascalName} = z.infer<typeof create${pascalName}Schema>;
export type Update${pascalName} = z.infer<typeof update${pascalName}Schema>;
`;
  },
};

// ═══════════════════════════════════════════════════════════════════════════
// CONFIGURATION & TYPES
// ═══════════════════════════════════════════════════════════════════════════

interface ScaffoldOptions {
  dryRun: boolean;
  force: boolean;
  json: boolean;
  yes: boolean;
}

interface ScaffoldConfig {
  fullPath: string;
  kebabName: string;
  name: string;
  pascalName: string;
  targetPath: string;
  type: string;
}

// ═══════════════════════════════════════════════════════════════════════════
// HELPER FUNCTIONS
// ═══════════════════════════════════════════════════════════════════════════

/**
 * Parse command-line arguments
 */
function parseArgs(): ScaffoldOptions {
  const args = process.argv.slice(2);
  return {
    dryRun: args.includes("--dry-run"),
    force: args.includes("--force"),
    json: args.includes("--json"),
    yes: args.includes("--yes"),
  };
}

/**
 * Validate scaffold type
 */
function isValidType(type: string): type is keyof typeof templates {
  return type in templates;
}

/**
 * Determine target path based on type
 */
function getTargetPath(type: string, name: string): string {
  const kebabName = toKebabCase(name);
  const pascalName = toPascalCase(name);

  switch (type) {
    case "component":
      return join("src", "components", kebabName, `${kebabName}.tsx`);

    case "dal":
      return join("src", "dal", `${kebabName}-dal.ts`);

    case "action":
      return join("src", "actions", `${kebabName}.actions.ts`);

    case "page":
      return join("src", "app", "(root)", kebabName, "page.tsx");

    case "schema":
      return join("src", "schemas", `${kebabName}.schema.ts`);

    default:
      return join("src", `${kebabName}.ts`);
  }
}

/**
 * Display help message
 */
function showHelp(): void {
  console.log(`
${"\x1b[1m\x1b[36m"}═══════════════════════════════════════════════════════════════${"\x1b[0m"}
${"\x1b[1m\x1b[36m"}  Advanced Scaffold Generator${"\x1b[0m"}
${"\x1b[1m\x1b[36m"}═══════════════════════════════════════════════════════════════${"\x1b[0m"}

${"\x1b[1m"}Usage:${"\x1b[0m"}
  pnpm scaffold <type> <name> [options]

${"\x1b[1m"}Types:${"\x1b[0m"}
  component       Create a client React component
  action          Create a server action (use server)
  dal             Create a Data Access Layer module
  page            Create a Next.js server page
  schema          Create a Zod validation schema

${"\x1b[1m"}Examples:${"\x1b[0m"}
  pnpm scaffold component ComicCard
  pnpm scaffold action updateComic
  pnpm scaffold dal Comic
  pnpm scaffold page ComicDetail
  pnpm scaffold schema Comic

${"\x1b[1m"}Options:${"\x1b[0m"}
  --force         Overwrite existing files
  --dry-run       Show what would be created
  --yes           Skip confirmation prompts
  --json          Output structured JSON

${"\x1b[1m"}Examples with Options:${"\x1b[0m"}
  pnpm scaffold component ComicCard --dry-run
  pnpm scaffold dal Comic --force --yes
  pnpm scaffold page ComicDetail --json
`);
}

// ═══════════════════════════════════════════════════════════════════════════
// MAIN FUNCTION
// ═══════════════════════════════════════════════════════════════════════════

async function main() {
  const options = parseArgs();
  const type = process.argv[2]?.toLowerCase() || "";
  const name = process.argv[3] || "";

  // Validate arguments
  if (!type || !name) {
    showHelp();
    process.exit(1);
  }

  if (!isValidType(type)) {
    console.error(`\x1b[31m✗ Unknown scaffold type: ${type}\x1b[0m`);
    showHelp();
    process.exit(1);
  }

  // Prepare configuration
  const kebabName = toKebabCase(name);
  const pascalName = toPascalCase(name);
  const targetPath = getTargetPath(type, name);
  const fullPath = join(process.cwd(), targetPath);

  const config: ScaffoldConfig = {
    type,
    name,
    targetPath,
    fullPath,
    kebabName,
    pascalName,
  };

  // Check if file exists
  if (existsSync(fullPath) && !options.force && !options.dryRun) {
    if (!options.json) {
      console.error(`\x1b[31m✗ File already exists: ${targetPath}\x1b[0m`);
      console.error(`  Use --force to overwrite`);
    }
    process.exit(1);
  }

  // Show dry-run preview
  if (options.dryRun && !options.json) {
    console.log(`\x1b[33m⚠ DRY-RUN MODE\x1b[0m`);
    console.log(`\nWould create: ${targetPath}\n`);
    console.log("Template preview:");
    console.log("─".repeat(60));
    console.log(templates[type](pascalName).substring(0, 300));
    console.log("...");
    console.log("─".repeat(60));
  }

  // Request confirmation
  if (!options.dryRun && !options.yes && !options.json) {
    const confirmed = await confirmAction({
      title: `Create ${type.toUpperCase()}`,
      message: `This will create a new ${type} file.`,
      affectedType: "file",
      yesFlag: options.yes,
      cautionLevel: "low",
      details: [targetPath],
    });

    if (!confirmed) {
      if (!options.json) {
        console.log("Cancelled.");
      }
      process.exit(0);
    }
  }

  // Create the file
  if (!options.dryRun) {
    try {
      await mkdir(join(fullPath, ".."), { recursive: true });
      const content = templates[type](pascalName);
      await writeFile(fullPath, content, "utf-8");
    } catch (error) {
      const errorMsg = error instanceof Error ? error.message : "Unknown error";
      if (options.json) {
        console.log(JSON.stringify({ success: false, error: errorMsg }));
      } else {
        console.error(`\x1b[31m✗ Error creating file: ${errorMsg}\x1b[0m`);
      }
      process.exit(1);
    }
  }

  // Output result
  if (options.json) {
    console.log(
      JSON.stringify({
        success: true,
        type,
        name: pascalName,
        file: targetPath,
        dryRun: options.dryRun,
      })
    );
  } else {
    const action = options.dryRun ? "Would create" : "Created";
    console.log(`\x1b[32m✓ ${action} ${type}: ${targetPath}\x1b[0m`);
  }
}

main();
