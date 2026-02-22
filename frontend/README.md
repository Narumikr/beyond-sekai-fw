# フロントエンド

フロントエンドは以下の技術スタックや構成になっています。

必要に応じて自分の好みに合わせてください。

## クイックスタート

```bash
# 依存関係のインストール
pnpm install

# 開発サーバー起動
pnpm dev
```

ブラウザで http://localhost:3000 を開く。
`Accept-Language` ヘッダーに応じて `/ja` または `/en` へ自動リダイレクトされる。

## 技術スタック

| カテゴリ           | 技術                 | バージョン |
| ------------------ | -------------------- | ---------- |
| Framework          | Next.js (App Router) | 16.x       |
| UI Library         | React                | 19.x       |
| 言語               | TypeScript           | 5.x        |
| Styling            | Tailwind CSS         | 4.x        |
| Linter / Formatter | Biome                | 2.x        |
| Package Manager    | pnpm                 | -          |

## ディレクトリ構成

```
frontend/
├── app/                    # Next.js App Router
│   ├── [lang]/             # i18n 動的ルートセグメント
│   │   └── page.tsx        # トップページ（ja/en 対応）
│   ├── globals.css         # グローバルスタイル
│   ├── layout.tsx          # ルートレイアウト
│   └── page.tsx            # デフォルトロケールへのリダイレクト
├── dictionaries/           # i18n 翻訳ファイル
│   ├── en.json             # 英語
│   └── ja.json             # 日本語
├── public/                 # 静的アセット
├── biome.json              # Biome 設定
├── get-dictionary.ts       # 翻訳辞書ローダー
├── i18n-config.ts          # ロケール設定
├── middleware.ts            # ロケール検出・リダイレクト
├── next.config.ts          # Next.js 設定
├── postcss.config.mjs      # PostCSS 設定
└── tsconfig.json           # TypeScript 設定
```

## 開発コマンド

```bash
pnpm dev          # 開発サーバー起動
pnpm build        # プロダクションビルド
pnpm start        # プロダクションサーバー起動
pnpm lint         # Biome lint チェック
pnpm lint:fix     # Biome lint 自動修正
pnpm format       # Biome フォーマット自動修正
pnpm check        # Biome lint + format を一括修正
pnpm typecheck    # TypeScript 型チェック
```

## i18n

対応ロケールは `i18n-config.ts` で管理する。

| ロケール | 言語                 |
| -------- | -------------------- |
| `ja`     | 日本語（デフォルト） |
| `en`     | 英語                 |

`/` へのアクセスは middleware によってブラウザの `Accept-Language` ヘッダーを元に自動的に `/ja` または `/en` へリダイレクトされる。
