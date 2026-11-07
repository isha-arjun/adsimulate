import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = { title: "AdSimulate — Campaign Decision Intelligence", description: "Understand the creative. Simulate the economics. Make better advertising decisions." };
export default function RootLayout({children}:{children:React.ReactNode}) { return <html lang="en"><body>{children}</body></html>; }