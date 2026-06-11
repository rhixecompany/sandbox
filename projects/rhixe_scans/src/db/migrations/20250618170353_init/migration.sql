-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL,
    "name" TEXT,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "emailVerified" TIMESTAMP(3),
    "image" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Account" (
    "userId" TEXT NOT NULL,
    "type" TEXT NOT NULL,
    "provider" TEXT NOT NULL,
    "providerAccountId" TEXT NOT NULL,
    "refresh_token" TEXT,
    "access_token" TEXT,
    "expires_at" INTEGER,
    "token_type" TEXT,
    "scope" TEXT,
    "id_token" TEXT,
    "session_state" TEXT,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "Account_pkey" PRIMARY KEY ("provider","providerAccountId")
);

-- CreateTable
CREATE TABLE "Session" (
    "sessionToken" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "expires" TIMESTAMP(3) NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL
);

-- CreateTable
CREATE TABLE "VerificationToken" (
    "identifier" TEXT NOT NULL,
    "token" TEXT NOT NULL,
    "expires" TIMESTAMP(3) NOT NULL,

    CONSTRAINT "VerificationToken_pkey" PRIMARY KEY ("identifier","token")
);

-- CreateTable
CREATE TABLE "Authenticator" (
    "credentialID" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "providerAccountId" TEXT NOT NULL,
    "credentialPublicKey" TEXT NOT NULL,
    "counter" INTEGER NOT NULL,
    "credentialDeviceType" TEXT NOT NULL,
    "credentialBackedUp" BOOLEAN NOT NULL,
    "transports" TEXT,

    CONSTRAINT "Authenticator_pkey" PRIMARY KEY ("userId","credentialID")
);

-- CreateTable
CREATE TABLE "Comic" (
    "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    "title" TEXT NOT NULL,
    "slug" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "status" TEXT NOT NULL,
    "rating" DECIMAL(10,1) NOT NULL DEFAULT 0,
    "createdAt" TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    "updated_at" TIMESTAMP(6) NOT NULL,
    "link" TEXT NOT NULL,
    "serialization" TEXT,
    "numchapters" INTEGER NOT NULL DEFAULT 0,
    "numimages" INTEGER NOT NULL DEFAULT 0,
    "has_chapters" BOOLEAN NOT NULL DEFAULT false,
    "has_images" BOOLEAN NOT NULL DEFAULT false,
    "category" JSON NOT NULL,
    "author" JSON,
    "artist" JSON,
    "images" JSON[] DEFAULT ARRAY[]::JSON[],
    "genres" JSON[] DEFAULT ARRAY[]::JSON[],

    CONSTRAINT "Comic_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Chapter" (
    "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    "name" TEXT NOT NULL,
    "title" TEXT,
    "slug" TEXT NOT NULL,
    "createdAt" TIMESTAMP(6) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL,
    "updated_at" TIMESTAMP(6) NOT NULL,
    "link" TEXT NOT NULL,
    "numimages" INTEGER NOT NULL DEFAULT 0,
    "has_images" BOOLEAN NOT NULL DEFAULT false,
    "images" JSON[] DEFAULT ARRAY[]::JSON[],
    "comic" JSON NOT NULL,

    CONSTRAINT "Chapter_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Bookmark" (
    "id" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "sessionBookmarkId" TEXT NOT NULL,
    "items" JSON[] DEFAULT ARRAY[]::JSON[],

    CONSTRAINT "Bookmark_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Genre" (
    "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    "name" TEXT,

    CONSTRAINT "Genre_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Category" (
    "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    "name" TEXT NOT NULL,

    CONSTRAINT "Category_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Author" (
    "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    "name" TEXT NOT NULL,

    CONSTRAINT "Author_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Artist" (
    "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    "name" TEXT NOT NULL,

    CONSTRAINT "Artist_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "ComicImage" (
    "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    "link" TEXT NOT NULL,
    "image" TEXT,
    "status" TEXT,
    "checksum" TEXT,
    "comic" TEXT NOT NULL,

    CONSTRAINT "ComicImage_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "ChapterImage" (
    "id" UUID NOT NULL DEFAULT gen_random_uuid(),
    "link" TEXT NOT NULL,
    "image" TEXT,
    "status" TEXT,
    "checksum" TEXT,
    "comic" TEXT NOT NULL,
    "chapter" TEXT,

    CONSTRAINT "ChapterImage_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- CreateIndex
CREATE UNIQUE INDEX "Session_sessionToken_key" ON "Session"("sessionToken");

-- CreateIndex
CREATE UNIQUE INDEX "Authenticator_credentialID_key" ON "Authenticator"("credentialID");

-- CreateIndex
CREATE UNIQUE INDEX "comic_title_idx" ON "Comic"("title");

-- CreateIndex
CREATE UNIQUE INDEX "comic_slug_idx" ON "Comic"("slug");

-- CreateIndex
CREATE UNIQUE INDEX "chapter_slug_idx" ON "Chapter"("slug");

-- CreateIndex
CREATE UNIQUE INDEX "zgenre_name_idx" ON "Genre"("name");

-- CreateIndex
CREATE UNIQUE INDEX "zcategory_name_idx" ON "Category"("name");

-- CreateIndex
CREATE UNIQUE INDEX "zauthor_name_idx" ON "Author"("name");

-- CreateIndex
CREATE UNIQUE INDEX "zartist_name_idx" ON "Artist"("name");

-- AddForeignKey
ALTER TABLE "Account" ADD CONSTRAINT "Account_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Session" ADD CONSTRAINT "Session_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Authenticator" ADD CONSTRAINT "Authenticator_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Bookmark" ADD CONSTRAINT "Bookmark_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE CASCADE ON UPDATE CASCADE;
