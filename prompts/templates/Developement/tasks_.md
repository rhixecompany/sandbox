# Tasks:

Extracted from `Developement.prompt.md`.

```
## Tasks:
1 - Setup the project by installing all dependencies using pnpm, setting up the database, and configuring any necessary environment variables at `.env.local`, importing it at `src/lib/env.ts` use `src/lib/env.ts` to Optimize `appConfig.ts` (ensure all environment variables are properly set and configured for development and production environments update all usage of this file across the project).
2 - Create, Optimize and Validate if exists copy file to end with .backup and Create, Optimize and Validate an enhanced version of `src/database/seed/**/*.ts`  to be faster (ensure all data from `users.json`, `comics.json`, `comicsdata1.json`, `comicsdata2.json`, `chapters.json`, `chaptersdata1.json`, `chaptersdata2.json` are validated using zod schemas and  then inserted into the database an onConflictDoUpdate of the inserted data with all its  chapters images, comics images, genres, inserted into the database an onConflictDoUpdate of the inserted data make sure no image is being downloaded twice by only downloading the image file if the file does not exists in the file system, using  `src/services/imageService.ts`,   save the comic images at `/comics/${comic.slug}` set `/placeholder-comic.jpg` as the default fallback image, if a user image isnt available, save the comic images at `/comics/${comic.slug}/chapters/${chapter.chapterId}` ,set `/shadcn.jpg` as the default fallback image  if a user image isnt available, use nextjs@latest best practices and dry practices, ensure it has a comprehensive logging with clear, concise descriptions,  and update all usage of this files across the project).
3 - Run pnpm  db:seed and get a list of all errors and warnings then batch fix all its errors and warnings.
4 - Create, Optimize and Validate all comprehensive configurations listed below if exists copy file to end with .backup and Create, Optimize and Validate an enhanced version of the following files use nextjs@latest best practices and dry practices. Ensure all configura
```

---
*Full content in original prompt.*
