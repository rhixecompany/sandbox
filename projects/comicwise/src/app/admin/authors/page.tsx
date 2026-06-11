import { getAuthorsAction } from "@/actions/admin/author.actions";
import { AdminAuthorsWrapper } from "@/components/admin/admin-authors-wrapper";

export const metadata = {
  title: "Admin - Authors",
};

export default async function AdminAuthorsPage() {
  const result = await getAuthorsAction();
  const authors = result.ok ? result.data : [];
  return <AdminAuthorsWrapper authors={authors} />;
}
