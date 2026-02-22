import { redirect } from "next/navigation";
import { i18n } from "@/i18n-config";

// ミドルウェアがリダイレクトを処理するが、万が一のフォールバック
export default function RootPage() {
  redirect(`/${i18n.defaultLocale}`);
}
