/**
 * Chapter Server Actions
 * Handle chapter CRUD operations
 */

"use server";

import { revalidatePath } from "next/cache.js";
import { z } from "zod";

import { auth } from "@/auth";
import { auditLogDal } from "@/dal/audit-log-dal";
import { chapterDal } from "@/dal/chapter-dal";

import type { ActionResult } from "@/types/actions-types";

const createChapterSchema = z.object({
  slug: z.string().min(1, "Slug is required"),
  title: z.string().min(1, "Title is required"),
  chapterNumber: z.number().positive("Chapter number must be positive"),
  comicId: z.number().positive("Comic ID is required"),
  releaseDate: z.string().datetime().optional(),
  url: z.string().url().optional(),
  content: z.string().optional(),
});

const updateChapterSchema = z.object({
  id: z.number().positive("ID is required"),
  slug: z.string().min(1).optional(),
  title: z.string().min(1).optional(),
  chapterNumber: z.number().positive().optional(),
  releaseDate: z.union([z.string().datetime(), z.date()]).optional(),
  url: z.string().url().optional(),
  content: z.string().optional(),
});

export async function createChapterAction(input: unknown): Promise<ActionResult<{ chapterId: number }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = createChapterSchema.safeParse(input);
  if (!parsed.success) {
    const error = parsed.error.issues[0];
    return { ok: false, error: error?.message ?? "Invalid input" };
  }

  const { slug, title, chapterNumber, comicId, releaseDate, url, content } = parsed.data;

  try {
    const chapter = await chapterDal.create({
      slug,
      title,
      chapterNumber,
      comicId,
      releaseDate: releaseDate ? new Date(releaseDate) : new Date(),
      url,
      content,
    });

    await auditLogDal.create({
      userId: session.user.id,
      action: "create",
      resource: "chapter",
      resourceId: String(chapter.id),
      details: { title: chapter.title },
    });

    revalidatePath(`/admin/chapters`);
    revalidatePath(`/comics/${slug}`);

    return { ok: true, data: { chapterId: chapter.id } };
  } catch {
    return { ok: false, error: "Failed to create chapter" };
  }
}

export async function updateChapterAction(input: unknown): Promise<ActionResult<{ success: boolean }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  const parsed = updateChapterSchema.safeParse(input);
  if (!parsed.success) {
    const error = parsed.error.issues[0];
    return { ok: false, error: error?.message ?? "Invalid input" };
  }

  const { id, releaseDate, ...rest } = parsed.data;

  // Build update data with converted date
  const updateData: Record<string, unknown> = { ...rest };
  if (releaseDate) {
    updateData.releaseDate = typeof releaseDate === "string" ? new Date(releaseDate) : releaseDate;
  }

  try {
    await chapterDal.update(id, updateData);

    await auditLogDal.create({
      userId: session.user.id,
      action: "update",
      resource: "chapter",
      resourceId: String(id),
      details: updateData,
    });

    revalidatePath(`/admin/chapters`);

    return { ok: true, data: { success: true } };
  } catch {
    return { ok: false, error: "Failed to update chapter" };
  }
}

export async function deleteChapterAction(id: number): Promise<ActionResult<{ success: boolean }>> {
  const session = await auth();
  if (!session?.user?.id) {
    return { ok: false, error: "Not authenticated" };
  }

  try {
    const chapter = await chapterDal.getById(id);
    if (!chapter) {
      return { ok: false, error: "Chapter not found" };
    }

    await chapterDal.delete(id);

    await auditLogDal.create({
      userId: session.user.id,
      action: "delete",
      resource: "chapter",
      resourceId: String(id),
      details: { title: chapter.title },
    });

    revalidatePath(`/admin/chapters`);

    return { ok: true, data: { success: true } };
  } catch {
    return { ok: false, error: "Failed to delete chapter" };
  }
}

export async function getChapterAction(id: number): Promise<ActionResult<unknown>> {
  try {
    const chapter = await chapterDal.getById(id);
    if (!chapter) {
      return { ok: false, error: "Chapter not found" };
    }
    return { ok: true, data: chapter };
  } catch {
    return { ok: false, error: "Failed to get chapter" };
  }
}
