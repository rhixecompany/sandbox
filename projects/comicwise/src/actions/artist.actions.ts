"use server";
import { revalidatePath, revalidateTag } from "next/cache.js";
import { z } from "zod";

import { auth } from "@/auth";
import { artistDal } from "@/dal/artist-dal";
import type { ActionResult } from "@/types/actions-types";

const ArtistSchema = z.object({
  name: z.string().min(1, "Name required").max(255),
  bio: z.string().optional(),
  imageUrl: z.string().url().optional().or(z.literal("")),
});

type ArtistType = Awaited<ReturnType<typeof artistDal.getById>>;

export async function createArtistAction(input: unknown): Promise<ActionResult<NonNullable<ArtistType>>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") return { ok: false, error: "Forbidden" };
  const parsed = ArtistSchema.safeParse(input);
  if (!parsed.success) {
    const error = parsed.error.issues[0];
    return { ok: false, error: error?.message ?? "Invalid" };
  }
  try {
    const { name, bio, imageUrl } = parsed.data;
    const artist = await artistDal.create({
      name,
      image: imageUrl || null,
      isActive: true,
      bio: bio || null,
      searchVector: null,
      createdAt: new Date(),
    });
    revalidatePath("/admin/artists");
    revalidateTag("search-results", "max");
    return { ok: true, data: artist };
  } catch (e) {
    console.error("[createArtistAction]", e);
    return { ok: false, error: "Failed to create artist" };
  }
}

export async function updateArtistAction(id: number, input: unknown): Promise<ActionResult<NonNullable<ArtistType>>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") return { ok: false, error: "Forbidden" };
  const parsed = ArtistSchema.partial().safeParse(input);
  if (!parsed.success) {
    const error = parsed.error.issues[0];
    return { ok: false, error: error?.message ?? "Invalid" };
  }
  try {
    const artist = await artistDal.update(id, parsed.data);
    if (!artist) return { ok: false, error: "Artist not found" };
    revalidatePath("/admin/artists");
    revalidateTag("search-results", "max");
    return { ok: true, data: artist };
  } catch (e) {
    console.error("[updateArtistAction]", e);
    return { ok: false, error: "Failed to update artist" };
  }
}

export async function deleteArtistAction(id: number): Promise<ActionResult<void>> {
  const session = await auth();
  const u = session?.user as { role?: unknown };
  if (typeof u?.role !== "string" || u.role !== "admin") return { ok: false, error: "Forbidden" };
  try {
    await artistDal.delete(id);
    revalidatePath("/admin/artists");
    revalidateTag("search-results", "max");
    return { ok: true, data: undefined };
  } catch (e) {
    console.error("[deleteArtistAction]", e);
    return { ok: false, error: "Failed to delete artist" };
  }
}
