# Phase 6: New DAL Files (9 new files)

> Extracted from `plan-comicWiseImplementation.prompt.md`.

## Phase 6: New DAL Files (9 new files)

### 6.1 — `src/dal/artist-dal.ts`

```ts
import { db } from "@/database/db";
import { artist } from "@/database/schema";
import { eq, ilike } from "drizzle-orm";
import { BaseDal, DalOptions } from "./base-dal";

type ArtistType = typeof artist.$inferSelect;

export class ArtistDal extends BaseDal<ArtistType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(artist)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0);
  }
  async getById(id: number): Promise<ArtistType | null> {
    const result = await db
      .select()
      .from(artist)
      .where(eq(artist.id, id))
      .limit(1);
    return result[0] ?? null;
  }
  async search(query: string) {
    return db
      .select()
      .from(artist)
      .where(ilike(artist.name, `%${query}%`));
  }
  async create(data: Omit<ArtistType, "id">) {
    const [result] = await db.insert(artist).values(data).returning();
    return result;
  }
  async update(id: number, data: Partial<Omit<ArtistType, "id">>) {
    const [result] = await db
      .update(artist)
      .set(data)
      .where(eq(artist.id, id))
      .returning();
    return result ?? null;
  }
  async delete(id: number) {
    await db.delete(artist).where(eq(artist.id, id));
  }
}
export const artistDal = new ArtistDal();
```

### 6.2 — `src/dal/author-dal.ts`

```ts
import { db } from "@/database/db";
import { author } from "@/database/schema";
import { eq, ilike } from "drizzle-orm";
import { BaseDal, DalOptions } from "./base-dal";

type AuthorType = typeof author.$inferSelect;

export class AuthorDal extends BaseDal<AuthorType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(author)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0);
  }
  async getById(id: number): Promise<AuthorType | null> {
    const result = await db
      .select()
      .from(author)
      .where(eq(author.id, id))
      .limit(1);
    return result[0] ?? null;
  }
  async search(query: string) {
    return db
      .select()
      .from(author)
      .where(ilike(author.name, `%${query}%`));
  }
  async create(data: Omit<AuthorType, "id">) {
    const [result] = await db.insert(author).values(data).returning();
    return result;
  }
  async update(id: number, data: Partial<Omit<AuthorType, "id">>) {
    const [result] = await db
      .update(author)
      .set(data)
      .where(eq(author.id, id))
      .returning();
    return result ?? null;
  }
  async delete(id: number) {
    await db.delete(author).where(eq(author.id, id));
  }
}
export const authorDal = new AuthorDal();
```

### 6.3 — `src/dal/genre-dal.ts`

```ts
import { db } from "@/database/db";
import { genre, comicToGenre } from "@/database/schema";
import { eq, ilike } from "drizzle-orm";
import { BaseDal, DalOptions } from "./base-dal";

type GenreType = typeof genre.$inferSelect;

export class GenreDal extends BaseDal<GenreType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(genre)
      .limit(options?.limit ?? 50)
      .offset(options?.offset ?? 0);
  }
  async getById(id: number): Promise<GenreType | null> {
    const result = await db
      .select()
      .from(genre)
      .where(eq(genre.id, id))
      .limit(1);
    return result[0] ?? null;
  }
  async getBySlug(slug: string): Promise<GenreType | null> {
    const result = await db
      .select()
      .from(genre)
      .where(eq(genre.slug, slug))
      .limit(1);
    return result[0] ?? null;
  }
  async search(query: string) {
    return db
      .select()
      .from(genre)
      .where(ilike(genre.name, `%${query}%`));
  }
  async create(data: Omit<GenreType, "id">) {
    const [result] = await db.insert(genre).values(data).returning();
    return result;
  }
  async update(id: number, data: Partial<Omit<GenreType, "id">>) {
    const [result] = await db
      .update(genre)
      .set(data)
      .where(eq(genre.id, id))
      .returning();
    return result ?? null;
  }
  async delete(id: number) {
    await db.delete(genre).where(eq(genre.id, id));
  }
  async getComicsForGenre(genreId: number) {
    return db.query.comicToGenre.findMany({
      where: eq(comicToGenre.genreId, genreId),
      with: { comic: true }
    });
  }
}
export const genreDal = new GenreDal();
```

### 6.4 — `src/dal/notification-dal.ts`

```ts
import { db } from "@/database/db";
import { notification } from "@/database/schema";
import { and, eq, desc } from "drizzle-orm";
import { BaseDal, DalOptions } from "./base-dal";

type NotificationType = typeof notification.$inferSelect;

export class NotificationDal extends BaseDal<NotificationType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(notification)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0)
      .orderBy(desc(notification.createdAt));
  }
  async getById(id: number): Promise<NotificationType | null> {
    const result = await db
      .select()
      .from(notification)
      .where(eq(notification.id, id))
      .limit(1);
    return result[0] ?? null;
  }
  async getByUser(
    userId: string,
    options?: DalOptions & { unreadOnly?: boolean }
  ) {
    const conditions = [eq(notification.userId, userId)];
    if (options?.unreadOnly)
      conditions.push(eq(notification.read, false));
    return db
      .select()
      .from(notification)
      .where(and(...conditions))
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0)
      .orderBy(desc(notification.createdAt));
  }
  async markRead(id: number) {
    const [result] = await db
      .update(notification)
      .set({ read: true })
      .where(eq(notification.id, id))
      .returning();
    return result ?? null;
  }
  async markAllRead(userId: string) {
    await db
      .update(notification)
      .set({ read: true })
      .where(
        and(
          eq(notification.userId, userId),
          eq(notification.read, false)
        )
      );
  }
  async create(data: Omit<NotificationType, "id" | "createdAt">) {
    const [result] = await db
      .insert(notification)
      .values(data)
      .returning();
    return result;
  }
  async delete(id: number) {
    await db.delete(notification).where(eq(notification.id, id));
  }
}
export const notificationDal = new NotificationDal();
```

### 6.5 — `src/dal/user-dal.ts`

```ts
import { db } from "@/database/db";
import { user } from "@/database/schema";
import { eq, ilike, desc } from "drizzle-orm";
import { BaseDal, DalOptions } from "./base-dal";

type UserType = typeof user.$inferSelect;

export class UserDal extends BaseDal<UserType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(user)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0)
      .orderBy(desc(user.createdAt));
  }
  async getById(id: string): Promise<UserType | null> {
    const result = await db
      .select()
      .from(user)
      .where(eq(user.id, id))
      .limit(1);
    return result[0] ?? null;
  }
  async getByEmail(email: string): Promise<UserType | null> {
    const result = await db
      .select()
      .from(user)
      .where(eq(user.email, email))
      .limit(1);
    return result[0] ?? null;
  }
  async search(query: string) {
    return db
      .select()
      .from(user)
      .where(ilike(user.name, `%${query}%`));
  }
  async update(id: string, data: Partial<Omit<UserType, "id">>) {
    const [result] = await db
      .update(user)
      .set(data)
      .where(eq(user.id, id))
      .returning();
    return result ?? null;
  }
  async updateRole(id: string, role: "user" | "admin" | "moderator") {
    const [result] = await db
      .update(user)
      .set({ role })
      .where(eq(user.id, id))
      .returning();
    return result ?? null;
  }
  async delete(id: string) {
    await db.delete(user).where(eq(user.id, id));
  }
}
export const userDal = new UserDal();
```

### 6.6 — `src/dal/chapter-image-dal.ts`

```ts
import { db } from "@/database/db";
import { chapterImage } from "@/database/schema";
import { eq, asc } from "drizzle-orm";
import { BaseDal, DalOptions } from "./base-dal";

type ChapterImageType = typeof chapterImage.$inferSelect;

export class ChapterImageDal extends BaseDal<ChapterImageType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(chapterImage)
      .limit(options?.limit ?? 50)
      .offset(options?.offset ?? 0);
  }
  async getById(id: number): Promise<ChapterImageType | null> {
    const result = await db
      .select()
      .from(chapterImage)
      .where(eq(chapterImage.id, id))
      .limit(1);
    return result[0] ?? null;
  }
  async getByChapter(chapterId: number) {
    return db
      .select()
      .from(chapterImage)
      .where(eq(chapterImage.chapterId, chapterId))
      .orderBy(asc(chapterImage.pageNumber));
  }
  async create(data: Omit<ChapterImageType, "id">) {
    const [result] = await db
      .insert(chapterImage)
      .values(data)
      .returning();
    return result;
  }
  async bulkCreate(images: Omit<ChapterImageType, "id">[]) {
    return db.insert(chapterImage).values(images).returning();
  }
  async delete(id: number) {
    await db.delete(chapterImage).where(eq(chapterImage.id, id));
  }
}
export const chapterImageDal = new ChapterImageDal();
```

### 6.7 — `src/dal/comic-image-dal.ts`

```ts
import { db } from "@/database/db";
import { comicImage } from "@/database/schema";
import { eq } from "drizzle-orm";
import { BaseDal, DalOptions } from "./base-dal";

type ComicImageType = typeof comicImage.$inferSelect;

export class ComicImageDal extends BaseDal<ComicImageType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(comicImage)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0);
  }
  async getById(id: number): Promise<ComicImageType | null> {
    const result = await db
      .select()
      .from(comicImage)
      .where(eq(comicImage.id, id))
      .limit(1);
    return result[0] ?? null;
  }
  async getByComic(comicId: number) {
    return db
      .select()
      .from(comicImage)
      .where(eq(comicImage.comicId, comicId));
  }
  async create(data: Omit<ComicImageType, "id">) {
    const [result] = await db
      .insert(comicImage)
      .values(data)
      .returning();
    return result;
  }
  async delete(id: number) {
    await db.delete(comicImage).where(eq(comicImage.id, id));
  }
}
export const comicImageDal = new ComicImageDal();
```

### 6.8 — `src/dal/type-dal.ts`

```ts
import { db } from "@/database/db";
import { type as comicType } from "@/database/schema";
import { eq, ilike } from "drizzle-orm";
import { BaseDal, DalOptions } from "./base-dal";

type ComicTypeType = typeof comicType.$inferSelect;

export class TypeDal extends BaseDal<ComicTypeType> {
  async list(options?: DalOptions) {
    return db
      .select()
      .from(comicType)
      .limit(options?.limit ?? 20)
      .offset(options?.offset ?? 0);
  }
  async getById(id: number): Promise<ComicTypeType | null> {
    const result = await db
      .select()
      .from(comicType)
      .where(eq(comicType.id, id))
      .limit(1);
    return result[0] ?? null;
  }
  async search(query: string) {
    return db
      .select()
      .from(comicType)
      .where(ilike(comicType.name, `%${query}%`));
  }
  async create(data: Omit<ComicTypeType, "id">) {
    const [result] = await db
      .insert(comicType)
      .values(data)
      .returning();
    return result;
  }
  async update(id: number, data: Partial<Omit<ComicTypeType, "id">>) {
    const [result] = await db
      .update(comicType)
      .set(data)
      .where(eq(comicType.id, id))
      .returning();
    return result ?? null;
  }
  async delete(id: number) {
    await db.delete(comicType).where(eq(comicType.id, id));
  }
}
export const typeDal = new TypeDal();
```

### 6.9 — `src/dal/index.ts` (barrel)

```ts
export { bookmarkDal, BookmarkDal } from "./bookmark-dal";
export { chapterDal, ChapterDal } from "./chapter-dal";
export {
  chapterImageDal,
  ChapterImageDal
} from "./chapter-image-dal";
export { comicDal, ComicDal } from "./comic-dal";
export { comicImageDal, ComicImageDal } from "./comic-image-dal";
export { commentDal, CommentDal } from "./comment-dal";
export {
  commentRatingDal,
  CommentRatingDal
} from "./comment-rating-dal";
export { genreDal, GenreDal } from "./genre-dal";
export { notificationDal, NotificationDal } from "./notification-dal";
export { ratingDal, RatingDal } from "./rating-dal";
export {
  readingProgressDal,
  ReadingProgressDal
} from "./reading-progress-dal";
export { artistDal, ArtistDal } from "./artist-dal";
export { authorDal, AuthorDal } from "./author-dal";
export { typeDal, TypeDal } from "./type-dal";
export { userDal, UserDal } from "./user-dal";
export {
  userPreferencesDal,
  UserPreferencesDal
} from "./user-preferences-dal";
export { BaseDal } from "./base-dal";
export type { DalOptions } from "./base-dal";
```

---
