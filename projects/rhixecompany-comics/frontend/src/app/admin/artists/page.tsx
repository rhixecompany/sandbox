import { getArtistsAction } from "@/actions/admin/artist.actions";
import { AdminArtistsWrapper } from "@/components/admin/admin-artists-wrapper";

export const metadata = {
  title: "Admin - Artists",
};

export default async function AdminArtistsPage() {
  const result = await getArtistsAction();
  const artists = result.ok ? result.data : [];
  return <AdminArtistsWrapper artists={artists} />;
}
