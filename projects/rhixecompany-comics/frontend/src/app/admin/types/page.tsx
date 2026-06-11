import { getTypesAction } from "@/actions/admin/type.actions";
import { AdminTypesWrapper } from "@/components/admin/admin-types-wrapper";

export const metadata = {
  title: "Admin - Comic Types",
};

export default async function AdminTypesPage() {
  const result = await getTypesAction();
  const types = result.ok ? result.data : [];
  return <AdminTypesWrapper types={types} />;
}
