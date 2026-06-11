# ComicWise — API Reference

## Overview

ComicWise uses **Next.js Server Actions** for all mutations. There are no traditional REST API endpoints. All actions return `ActionResult<T>` discriminated unions.

## Authentication

### `auth.signIn(provider, credentials)`
- **File:** `src/actions/auth.actions.ts`
- **Purpose:** Authenticate user
- **Providers:** Credentials, GitHub, Keycloak
- **Returns:** `ActionResult<Session>`

### `auth.signUp(data)`
- **File:** `src/actions/auth.actions.ts`
- **Purpose:** Register new user
- **Input:** `{ email, username, password, name }`
- **Validation:** Zod schema with password strength check
- **Returns:** `ActionResult<User>`

### `auth.signOut()`
- **File:** `src/actions/auth.actions.ts`
- **Purpose:** End current session

## Comics

### `comic.list(filters)`
- **File:** `src/actions/comic.actions.ts`
- **Purpose:** List comics with pagination & filtering
- **Filters:** genre, status, rating, search query, sort order
- **Returns:** `ActionResult<{ comics: Comic[], total: number }>`

### `comic.getById(id)`
- **File:** `src/actions/comic.actions.ts`
- **Purpose:** Get comic details with chapters
- **Returns:** `ActionResult<ComicDetails>`

### `comic.create(data)`
- **File:** `src/actions/comic.actions.ts`
- **Purpose:** Create new comic (admin only)
- **Returns:** `ActionResult<Comic>`

### `comic.update(id, data)`
- **File:** `src/actions/comic.actions.ts`
- **Purpose:** Update comic details (admin)

### `comic.delete(id)`
- **File:** `src/actions/comic.actions.ts`
- **Purpose:** Soft-delete comic (admin)

## Chapters

### `chapter.list(comicId)`
- **File:** `src/actions/chapter.actions.ts`
- **Purpose:** Get chapters for a comic
- **Returns:** `ActionResult<Chapter[]>`

### `chapter.getById(id)`
- **File:** `src/actions/chapter.actions.ts`
- **Purpose:** Get chapter with images
- **Returns:** `ActionResult<ChapterWithImages>`

### `chapter.markAsRead(chapterId)`
- **File:** `src/actions/chapter.actions.ts`
- **Purpose:** Mark chapter as read

## Bookmarks

### `bookmark.add(comicId)`
- **File:** `src/actions/bookmark.actions.ts`
- **Purpose:** Add comic to bookmarks

### `bookmark.remove(comicId)`
- **File:** `src/actions/bookmark.actions.ts`
- **Purpose:** Remove bookmark

### `bookmark.list()`
- **File:** `src/actions/bookmark.actions.ts`
- **Purpose:** List user's bookmarks

## Ratings

### `rating.rate(comicId, score)`
- **File:** `src/actions/rating.actions.ts`
- **Purpose:** Rate a comic (1-5)
- **Returns:** `ActionResult<{ averageRating: number }>`

### `rating.getForComic(comicId)`
- **File:** `src/actions/rating.actions.ts`
- **Purpose:** Get rating statistics

## Comments

### `comment.create(chapterId, content)`
- **File:** `src/actions/comment.actions.ts`
- **Purpose:** Post a comment on a chapter

### `comment.list(chapterId)`
- **File:** `src/actions/comment.actions.ts`
- **Purpose:** Get comments for a chapter

## User Profile

### `user.getProfile()`
- **File:** `src/actions/user.actions.ts`
- **Purpose:** Get current user's profile

### `user.updateProfile(data)`
- **File:** `src/actions/user.actions.ts`
- **Purpose:** Update profile info

### `user.getReadingHistory()`
- **File:** `src/actions/user.actions.ts`
- **Purpose:** Get reading history

## Reading Goals

### `readingGoal.set(goal)`
- **File:** `src/actions/readingGoal.actions.ts`
- **Purpose:** Set reading goals

### `readingGoal.getProgress()`
- **File:** `src/actions/readingGoal.actions.ts`
- **Purpose:** Get goal progress

## Notifications

### `notification.list()`
- **File:** `src/actions/notification.actions.ts`
- **Purpose:** List user notifications

### `notification.markAsRead(id)`
- **File:** `src/actions/notification.actions.ts`
- **Purpose:** Mark notification read

## ActionResult Pattern

```typescript
// All Server Actions return this discriminated union
type ActionResult<T> = 
  | { ok: true; data: T }
  | { ok: false; error: string };

// Usage in client component
const result = await someAction(input);
if (!result.ok) {
  toast.error(result.error);
  return;
}
setData(result.data);
```
