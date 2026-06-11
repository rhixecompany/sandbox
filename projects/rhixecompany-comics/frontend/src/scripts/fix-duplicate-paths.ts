#!/usr/bin/env tsx
/**
 * Fix Duplicate Path Script
 * Corrects paths like /uploads/comics/comics/slug → /uploads/comics/slug
 *
 * Usage:
 *   pnpm fix:duplicate-paths       # Preview changes
 *   pnpm fix:duplicate-paths --fix  # Apply fixes
 */

import chalk from "chalk";
import { Command } from "commander";
import { eq, like } from "drizzle-orm";
import { db } from "../database/db";
import { chapterImage, comic, comicImage } from "../database/schema";

const program = new Command()
  .name("fix-duplicate-paths")
  .description("Fix duplicate /uploads/comics/comics/ paths in database")
  .option("--fix", "Apply fixes (default is preview)")
  .option("--dry-run", "Preview changes without modifying (same as not using --fix)")
  .parse(process.argv);

const opts = program.opts();
const shouldFix = opts.fix && !opts.dryRun;

async function fixDuplicatePaths() {
  console.log(chalk.cyan("═══════════════════════════════════════════════════════════"));
  console.log(chalk.cyan("  Fix Duplicate Paths"));
  console.log(chalk.cyan(shouldFix ? "  (APPLYING FIXES)" : "  (PREVIEW MODE)"));
  console.log(chalk.cyan("═══════════════════════════════════════════════════════════\n"));

  let totalFixed = 0;

  // Fix comic.coverImage paths
  console.log(chalk.blue("  Checking comic.coverImage..."));
  const badComicPattern = "/uploads/comics/comics/";

  try {
    const badComics = await db
      .select({ id: comic.id, title: comic.title, coverImage: comic.coverImage })
      .from(comic)
      .where(like(comic.coverImage, `%${badComicPattern}%`));

    if (badComics.length === 0) {
      console.log(chalk.green("    ✓ No duplicate paths in comic.coverImage"));
    } else {
      console.log(chalk.yellow(`    Found ${badComics.length} comics with duplicate paths`));
      for (const c of badComics) {
        const fixed = c.coverImage.replace("/uploads/comics/comics/", "/uploads/comics/");
        console.log(`    ${c.title}: ${c.coverImage} → ${fixed}`);
        if (shouldFix) {
          await db
            .update(comic)
            .set({ coverImage: fixed })
            .where(like(comic.coverImage, `%${badComicPattern}%`));
        }
        totalFixed++;
      }
    }
  } catch (error) {
    console.error(chalk.red(`    Error: ${error}`));
  }

  // Fix comicImage.imageUrl paths
  console.log(chalk.blue("\n  Checking comicImage.imageUrl..."));

  try {
    const badComicImages = await db
      .select({ id: comicImage.id, imageUrl: comicImage.imageUrl })
      .from(comicImage)
      .where(like(comicImage.imageUrl, `%${badComicPattern}%`));

    if (badComicImages.length === 0) {
      console.log(chalk.green("    ✓ No duplicate paths in comicImage.imageUrl"));
    } else {
      console.log(chalk.yellow(`    Found ${badComicImages.length} comicImages with duplicate paths`));
      for (const ci of badComicImages) {
        const fixed = ci.imageUrl.replace("/uploads/comics/comics/", "/uploads/comics/");
        console.log(`    ID ${ci.id}: ${ci.imageUrl} → ${fixed}`);
        if (shouldFix) {
          await db.update(comicImage).set({ imageUrl: fixed }).where(eq(comicImage.id, ci.id));
        }
        totalFixed++;
      }
    }
  } catch (error) {
    console.error(chalk.red(`    Error: ${error}`));
  }

  // Fix chapterImage.imageUrl paths (just in case)
  console.log(chalk.blue("\n  Checking chapterImage.imageUrl..."));

  try {
    const badChapterImages = await db
      .select({ id: chapterImage.id, imageUrl: chapterImage.imageUrl })
      .from(chapterImage)
      .where(like(chapterImage.imageUrl, `%${badComicPattern}%`));

    if (badChapterImages.length === 0) {
      console.log(chalk.green("    ✓ No duplicate paths in chapterImage.imageUrl"));
    } else {
      console.log(chalk.yellow(`    Found ${badChapterImages.length} chapterImages with duplicate paths`));
      for (const ci of badChapterImages) {
        const fixed = ci.imageUrl.replace("/uploads/comics/comics/", "/uploads/comics/");
        console.log(`    ID ${ci.id}: ${ci.imageUrl} → ${fixed}`);
        if (shouldFix) {
          await db.update(chapterImage).set({ imageUrl: fixed }).where(eq(chapterImage.id, ci.id));
        }
        totalFixed++;
      }
    }
  } catch (error) {
    console.error(chalk.red(`    Error: ${error}`));
  }

  console.log(chalk.cyan("\n═══════════════════════════════════════════════════════════"));

  if (shouldFix) {
    console.log(chalk.green(`  ✓ Fixed ${totalFixed} paths`));
  } else {
    console.log(chalk.yellow(`  Would fix ${totalFixed} paths`));
    console.log(chalk.gray("  Run with --fix to apply changes"));
  }

  console.log(chalk.cyan("═══════════════════════════════════════════════════════════\n"));
  process.exit(0);
}

fixDuplicatePaths().catch((error) => {
  console.error(chalk.red("Fatal error:"), error);
  process.exit(1);
});
