import Footer from "@/components/layout/footer";
import Navbar from "@/components/layout/navbar";

import type { ReactNode } from "react";

export default async function RootLayout({ children }: { children: ReactNode }) {
  return (
    <div className="flex flex-1 flex-col">
      <Navbar />
      <div className="@container/main flex flex-1 flex-col gap-2">{children}</div>
      <Footer />
    </div>
  );
}
