import { NextResponse } from "next/server";
import type { NextRequest } from "next/server";
import { i18n } from "@/i18n-config";

function getLocale(request: NextRequest): string {
  const acceptLanguage = request.headers.get("accept-language") ?? "";
  for (const locale of i18n.locales) {
    if (acceptLanguage.toLowerCase().includes(locale)) {
      return locale;
    }
  }
  return i18n.defaultLocale;
}

export function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  const pathnameHasLocale = i18n.locales.some(
    (locale) =>
      pathname.startsWith(`/${locale}/`) || pathname === `/${locale}`
  );

  if (pathnameHasLocale) {
    const locale = pathname.split("/")[1];
    const response = NextResponse.next();
    response.headers.set("x-locale", locale);
    return response;
  }

  // ロケールプレフィックスがない場合はリダイレクト
  const locale = getLocale(request);
  const newPath = `/${locale}${pathname === "/" ? "" : pathname}`;
  const response = NextResponse.redirect(new URL(newPath, request.url));
  response.headers.set("x-locale", locale);
  return response;
}

/**
 * ミドルウェアを適用するパスを制限するための設定。
 * * 下記のパス以外のすべてのリクエストに対してミドルウェアを実行します：
 * - /api/... (APIルート)
 * - /_next/static/... (ビルド済みのJS, CSSなどの静的ファイル)
 * - /_next/image/... (Next.jsの画像最適化用パス)
 * - favicon.ico (サイトアイコン)
 * * これにより、静的アセットやAPI呼び出しに対してロケールのリダイレクト処理が
 * 誤って適用されるのを防ぎ、パフォーマンスを向上させています。
 * * @see https://nextjs.org/docs/app/building-your-application/routing/middleware#matcher
 */
export const config = {
  matcher: ["/((?!api|_next/static|_next/image|favicon.ico).*)"],
};
