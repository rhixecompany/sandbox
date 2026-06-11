'use server';

import { auth } from '@/lib/auth';

import db from '@/lib/prisma';
import { BookmarkItem } from '@/types';
import { Prisma } from '@prisma/client';
import { revalidatePath } from 'next/cache';
import { cookies } from 'next/headers';
import { convertToPlainObject, formatError } from '../utils';
import { bookmarkItemSchema, insertBookmarkSchema } from '../validators';

export async function addItemToBookmark(data: BookmarkItem) {
  try {
    // Check for bookmark cookie
    const sessionBookmarkId = (await cookies()).get('sessionBookmarkId')?.value;
    if (!sessionBookmarkId) throw new Error('Bookmark session not found');

    // Get session and user ID
    const session = await auth();
    const userId = session?.user?.id ? (session.user.id as string) : undefined;

    // Get bookmark
    const bookmark = await getMyBookmark();

    // Parse and validate item
    const item = bookmarkItemSchema.parse(data);

    // Find comic in database
    const comic = await db.comic.findFirst({
      where: { id: item.id },
    });
    if (!comic) throw new Error('Comic not found');

    if (!bookmark) {
      // Create new bookmark object
      const newBookmark = insertBookmarkSchema.parse({
        userId: userId,
        items: [item],
        sessionBookmarkId: sessionBookmarkId,
      });

      // Add to database
      await db.bookmark.create({
        data: newBookmark,
      });

      // Revalidate comic page
      revalidatePath(`/series/${comic.slug}`);

      return {
        success: true,
        message: `${comic.title} added to bookmark`,
      };
    } else {
      // Check if item is already in bookmark
      const existItem = (bookmark.items as BookmarkItem[]).find(
        (x) => x.id === item.id
      );

      if (existItem) {
        // Increase the quantity
        (bookmark.items as BookmarkItem[]).find((x) => x.id === item.id)!.qty =
          existItem.qty + 1;
      } else {
        // If item does not exist in bookmark

        // Add item to the bookmark.items
        bookmark.items.push(item);
      }

      // Save to database
      await db.bookmark.update({
        where: { id: bookmark.id },
        data: {
          items: bookmark.items as Prisma.BookmarkUpdateitemsInput[],
        },
      });

      revalidatePath(`/series/${comic.slug}`);

      return {
        success: true,
        message: `${comic.title} ${
          existItem ? 'updated in' : 'added to'
        } bookmark`,
      };
    }
  } catch (error) {
    return {
      success: false,
      message: formatError(error),
    };
  }
}

export async function getMyBookmark() {
  // Check for bookmark cookie
  const sessionBookmarkId = (await cookies()).get('sessionBookmarkId')?.value;
  if (!sessionBookmarkId) throw new Error('Bookmark session not found');

  // Get session and user ID
  const session = await auth();
  const userId = session?.user?.id ? (session.user.id as string) : undefined;

  // Get user bookmark from database
  const bookmark = await db.bookmark.findFirst({
    where: userId
      ? { userId: userId }
      : { sessionBookmarkId: sessionBookmarkId },
  });

  if (!bookmark) return undefined;

  // Convert decimals and return
  return convertToPlainObject({
    ...bookmark,
    items: bookmark.items as BookmarkItem[],
  });
}

export async function removeItemFromBookmark(id: string) {
  try {
    // Check for bookmark cookie
    const sessionBookmarkId = (await cookies()).get('sessionBookmarkId')?.value;
    if (!sessionBookmarkId) throw new Error('Bookmark session not found');

    // Get Comic
    const comic = await db.comic.findFirst({
      where: { id: id },
    });
    if (!comic) throw new Error('Comic not found');

    // Get user bookmark
    const bookmark = await getMyBookmark();
    if (!bookmark) throw new Error('Bookmark not found');

    // Check for item
    const exist = (bookmark.items as BookmarkItem[]).find((x) => x.id === id);
    if (!exist) throw new Error('Item not found');

    // Check if only one in qty
    if (exist.qty === 1) {
      // Remove from bookmark
      bookmark.items = (bookmark.items as BookmarkItem[]).filter(
        (x) => x.id !== exist.id
      );
    } else {
      // Decrease qty
      (bookmark.items as BookmarkItem[]).find((x) => x.id === id)!.qty =
        exist.qty - 1;
    }

    // Update bookmark in database
    await db.bookmark.update({
      where: { id: bookmark.id },
      data: {
        items: bookmark.items as Prisma.BookmarkUpdateitemsInput[],
      },
    });

    revalidatePath(`/series/${comic.slug}`);

    return {
      success: true,
      message: `${comic.title} was removed from bookmark`,
    };
  } catch (error) {
    return { success: false, message: formatError(error) };
  }
}
