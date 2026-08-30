import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "Neural KG — Agentic Resource Discovery & Open Knowledge Format",
  description: "Next-generation data query platform powered by Google BigQuery, ARD, OKF, and Gemini LLMs.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className="min-h-screen bg-[#0a0e17] text-slate-100 antialiased selection:bg-blue-600 selection:text-white">
        {children}
      </body>
    </html>
  );
}
