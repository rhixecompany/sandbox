import { getGenresAction } from "@/actions/admin/genre.actions";
import { AdminGenresWrapper } from "@/components/admin/admin-genres-wrapper";

export const metadata = {
  title: "Admin - Genres",
};

export default async function AdminGenresPage() {
  const result = await getGenresAction();
  const genres = result.ok ? result.data : [];
  return <AdminGenresWrapper genres={genres} />;
}
