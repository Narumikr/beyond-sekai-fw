---
name: fastapi-best-practices
description: FastAPIのベストプラクティスを適用してコード設計・実装・レビューを支援する。ユーザーが「FastAPIのコードを書いて」「APIを設計して」「コードをレビューして」「バックエンドを実装して」と依頼した時、またはFastAPIのルーティング・スキーマ・依存性注入・非同期処理・DBマイグレーションに関わるコードの作成・レビュー・リファクタリングを行う時に使用する。
---

# FastAPI ベストプラクティス

FastAPIを用いた本番システム開発における実践的なベストプラクティスのリファレンス。
設計・実装・レビューのすべてのフェーズで参照すること。

## 適用タイミング

- 新しいエンドポイント・ルーターを作成する時
- 依存性注入・スキーマ・DBモデルを設計する時
- FastAPIコードをレビュー・リファクタリングする時
- パフォーマンス・セキュリティ・テストの問題を解決する時

## カテゴリ別リファレンス

### アーキテクチャ

| リファレンス | 説明 |
|------------|------|
| `references/project-structure` | ドメイン単位のディレクトリ構成・インポート規約 |

### 非同期処理

| リファレンス | 説明 |
|------------|------|
| `references/async-routes` | `async def` / `def` / `run_in_threadpool()` の使い分け |
| `references/lifespan` | 起動・終了処理（DBプール初期化・MLモデルロード等） |

### Pydantic・設定

| リファレンス | 説明 |
|------------|------|
| `references/pydantic` | バリデータ・カスタムベースモデル・BaseSettingsの分割 |

### 依存性注入

| リファレンス | 説明 |
|------------|------|
| `references/dependencies` | 検証ロジックへの活用・連鎖・キャッシュ |
| `references/dependencies-advanced` | Callableクラスによるパラメータ付き依存性 |

### データベース

| リファレンス | 説明 |
|------------|------|
| `references/database` | 命名規約・インデックス名・SQLファースト・Alembic |

### レスポンス・ミドルウェア

| リファレンス | 説明 |
|------------|------|
| `references/custom-response` | FileResponse / StreamingResponse / RedirectResponse 等 |
| `references/middleware` | HTTPS強制・TrustedHost・GZip・CORS |

### ドキュメント・テスト・本番

| リファレンス | 説明 |
|------------|------|
| `references/api-docs` | OpenAPIドキュメント設定・本番での非表示 |
| `references/testing` | AsyncClient・dependency_overrides によるモック |
| `references/proxy-config` | root_path・フォワードヘッダー設定 |
| `references/linting` | ruff によるリント・フォーマット |

---

## よくある間違い

| 間違い | 正しい実装 |
|-------|----------|
| `async def`内でブロッキング処理を直接呼ぶ | `run_in_threadpool()` を使う |
| `def`ルート内でCPU集約処理 | Celeryにオフロード |
| 単一の巨大な `BaseSettings` | ドメインごとに分割 |
| Pythonループで集計（N+1） | SQLの `func.count()` 等で集計 |
| 本番環境でSwagger UIを公開 | `openapi_url = None` で非表示 |
| モジュール間でワイルドカードインポート | 明示的なモジュール名でインポート |
| `@app.on_event("startup")` を使う | `lifespan` コンテキストマネージャに移行 |
| テストで実際の外部サービスに接続する | `app.dependency_overrides` でモック化 |
| プロキシ背後で `root_path` 未設定 | `FastAPI(root_path="/api/v1")` を設定 |
| 大容量ファイルを `bytes` でそのまま返す | `StreamingResponse` / `FileResponse` を使う |
| マイグレーションファイルに曖昧な名前 | `YYYY-MM-DD_slug.py` 形式 |
