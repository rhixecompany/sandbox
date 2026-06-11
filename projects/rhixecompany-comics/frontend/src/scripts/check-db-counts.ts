import { db } from "@/database/db";
import { artist, author, chapter, chapterImage, comic, comicImage, genre, user } from "@/database/schema";
import { sql } from "drizzle-orm";

async function main() {
  const [
    comicCount,
    chapterCount,
    comicImageCount,
    chapterImageCount,
    userCount,
    authorCount,
    artistCount,
    genreCount,
  ] = await Promise.all([
    db.select({ count: sql<number>`count(*)` }).from(comic),
    db.select({ count: sql<number>`count(*)` }).from(chapter),
    db.select({ count: sql<number>`count(*)` }).from(comicImage),
    db.select({ count: sql<number>`count(*)` }).from(chapterImage),
    db.select({ count: sql<number>`count(*)` }).from(user),
    db.select({ count: sql<number>`count(*)` }).from(author),
    db.select({ count: sql<number>`count(*)` }).from(artist),
    db.select({ count: sql<number>`count(*)` }).from(genre),
  ]);

  console.log("\n📊 Database Counts:");
  console.log("================");
  console.log(`  comics:         ${comicCount[0].count}`);
  console.log(`  chapters:       ${chapterCount[0].count}`);
  console.log(`  comic-images:   ${comicImageCount[0].count}`);
  console.log(`  chapter-images: ${chapterImageCount[0].count}`);
  console.log(`  users:          ${userCount[0].count}`);
  console.log(`  authors:        ${authorCount[0].count}`);
  console.log(`  artists:        ${artistCount[0].count}`);
  console.log(`  genres:         ${genreCount[0].count}`);
  console.log("");

  const total =
    comicCount[0].count +
    chapterCount[0].count +
    comicImageCount[0].count +
    chapterImageCount[0].count +
    userCount[0].count +
    authorCount[0].count +
    artistCount[0].count +
    genreCount[0].count;

  console.log(`  TOTAL:          ${total}`);
}

main().catch(console.error);
