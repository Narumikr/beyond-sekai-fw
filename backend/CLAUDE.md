# バックエンドガイドライン

<!-- 本プロジェクトは Webアプリ開発のためのスタートアップリポジトリテンプレートのため概要の記載はしませんが、新しくプロジェクトを開始したらコメントアウトを消して自分のプロジェクトの概要に書き換えてください。 -->

## ディレクトリ構成

```
backend/
├── app/
│   ├── {domain}/           # ドメイン単位のフォルダ（例: items, users）
│   │   ├── router.py       # APIエンドポイント
│   │   ├── schemas.py      # Pydanticモデル（Request / Response を分離）
│   │   ├── dependencies.py # ドメイン固有の Depends
│   │   ├── service.py      # ビジネスロジック（必要に応じて）
│   │   ├── models.py       # DBモデル（SQLAlchemy等、必要に応じて）
│   │   └── exceptions.py   # ドメイン固有の例外（必要に応じて）
│   ├── main.py             # FastAPI インスタンス / lifespan / ミドルウェア
│   └── config.py           # BaseSettings（ドメインごとに分割）
├── pyproject.toml
└── CLAUDE.md
```

## Skills

FastAPIのコードスタイルとベストプラクティスに関するガイドラインは `.claude/skills` にSkills が定義されているため参照してください。

| スキル名                   | 概要                                     | 使用するタイミング                                       |
| -------------------------- | ---------------------------------------- | -------------------------------------------------------- |
| `fastapi-best-practices`   | FastAPI 実装・設計のベストプラクティス   | ルーター・スキーマ・DI・非同期処理・テストの実装時       |
| `python-best-practices`    | Python コードスタイル・型ヒント・命名規則 | 全般的な Python コードの作成・レビュー時                 |
| `api-design`               | RESTful API 設計レビュー                 | エンドポイント設計・ステータスコード・エラーハンドリング |

## 開発ガイドライン

- **ドメイン単位**でフォルダを分割する（`routers/` `schemas/` のような種類別フォルダは NG）
- `@app.on_event("startup")` は使わず、`lifespan` コンテキストマネージャを使う
- Pydantic スキーマはリクエスト用とレスポンス用を分けて定義する
- 設定は `BaseSettings` を使い、ドメインごとにクラスを分割する
- ルート間の共通処理は `Depends` で依存性として注入する
- 本番環境では `openapi_url=None` を設定し Swagger UI を非公開にする
- `async def` 内でブロッキング I/O を直接呼ばない（`run_in_threadpool()` を使う）
