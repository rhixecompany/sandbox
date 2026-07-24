# Server Actions Reference

> Extracted from `features.prompt.md`.

## Server Actions Reference

### Profile Actions (`src/actions/profile.actions.ts`)

| Action                 | Schema                 | Status |
| ---------------------- | ---------------------- | ------ |
| `updateProfileAction`  | `ProfileUpdateSchema`  | ✅     |
| `changePasswordAction` | `ChangePasswordSchema` | ✅     |
| `updateSettingsAction` | `SettingsSchema`       | ✅     |
| `deleteAccountAction`  | N/A                    | ✅     |

### Bookmark Actions (`src/actions/bookmark.actions.ts`)

| Action                       | Schema                 | Status |
| ---------------------------- | ---------------------- | ------ |
| `addToBookmarksAction`       | `CreateBookmarkSchema` | ✅     |
| `removeFromBookmarksAction`  | N/A                    | ✅     |
| `updateBookmarkStatusAction` | `UpdateBookmarkSchema` | ✅     |
| `getUserBookmarksAction`     | N/A                    | ✅     |

### Comic Actions (`src/actions/comic.actions.ts`)

| Action                   | Schema              | Status |
| ------------------------ | ------------------- | ------ |
| `getComicBySlugAction`   | N/A                 | ✅     |
| `getComicsListAction`    | `ComicFilterSchema` | ✅     |
| `getRelatedComicsAction` | N/A                 | ✅     |

### Chapter Actions (`src/actions/chapter.actions.ts`)

| Action                      | Schema                  | Status |
| --------------------------- | ----------------------- | ------ |
| `getChapterAction`          | N/A                     | ✅     |
| `getChapterListAction`      | N/A                     | ✅     |
| `markChapterAsReadAction`   | N/A                     | ✅     |
| `saveReadingProgressAction` | `ReadingProgressSchema` | ✅     |

---
