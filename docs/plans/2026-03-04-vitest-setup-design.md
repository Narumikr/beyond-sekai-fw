# Vitest テスト環境セットアップ 設計書

## 概要

frontendにVitestを導入し、テスト実装のサンプルを配置する。
ユニットテストとコンポーネントテストの2パターンを最小構成で示す。

## 採用アプローチ

アプローチB（ユニット + コンポーネントテスト）を採用。

- `vitest` + `@testing-library/react` + `jsdom` を使用
- テストファイルはソースファイルと同じディレクトリに配置（コロケーション）
- サンプルとして「関数テスト」と「コンポーネントテスト」の2パターンを提供

## 追加パッケージ

```
vitest
@vitejs/plugin-react
@testing-library/react
@testing-library/user-event
jsdom
```

## 設定ファイル

### `frontend/vitest.config.ts`

- environment: `jsdom`（コンポーネントテスト用）
- `@vitejs/plugin-react` でJSXを処理
- `@/*` のパスエイリアスを解決（tsconfig.jsonに合わせる）
- テスト対象: `**/*.test.{ts,tsx}`（node_modules, .next を除外）

### `frontend/package.json`

以下のスクリプトを追加:

```json
"test": "vitest run",
"test:watch": "vitest"
```

### `justfile`

以下のコマンドを追加:

```
# フロントエンドテスト実行
test-ui:
  cd {{frontend_dir}} && {{pnpm}} test

# 全サービステスト実行
test-all: test-ui
```

## テストファイル

### 1. ユニットテストサンプル — `frontend/proxy.test.ts`

`getLocale()` 関数の言語検出ロジックをテスト。

テストケース:
- 日本語 Accept-Language → `"ja"`
- 英語 Accept-Language → `"en"`
- 未対応言語 → デフォルト `"ja"`
- q値を持つ複数言語 → 優先度順に解決

### 2. 非同期関数テストサンプル — `frontend/get-dictionary.test.ts`

`getDictionary()` 関数の辞書ロードをテスト。

テストケース:
- `getDictionary("ja")` → 日本語辞書オブジェクトを返す
- `getDictionary("en")` → 英語辞書オブジェクトを返す

### 3. コンポーネントテストサンプル

**新規コンポーネント**: `frontend/app/components/atoms/Button/Button.tsx`

AtomicDesign に従い atoms 層にシンプルなButtonコンポーネントを作成。
Next.js Server Components（`page.tsx`, `layout.tsx`）はサーバーAPI（`headers()`等）のモックが複雑になるため、
新規クライアントコンポーネントをテスト対象とする。

**テストファイル**: `frontend/app/components/atoms/Button/Button.test.tsx`

テストケース:
- テキストが正しくレンダリングされるか
- クリックイベントが発火するか
- `disabled` 状態のときクリックイベントが発火しないか

## ファイル構成（変更後）

```
frontend/
├── app/
│   └── components/
│       └── atoms/
│           └── Button/
│               ├── Button.tsx       # 新規: テスト対象コンポーネント
│               └── Button.test.tsx  # 新規: コンポーネントテストサンプル
├── proxy.ts
├── proxy.test.ts                    # 新規: ユニットテストサンプル
├── get-dictionary.ts
├── get-dictionary.test.ts           # 新規: 非同期関数テストサンプル
├── vitest.config.ts                 # 新規: Vitest設定
└── package.json                     # 変更: testスクリプト追加
```
