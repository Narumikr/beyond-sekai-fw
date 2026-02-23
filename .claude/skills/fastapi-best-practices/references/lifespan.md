---
title: Lifespan（起動・終了処理）
category: lifecycle
tags: lifespan, startup, shutdown, on_event, contextmanager, db_pool, ML, resource
---

## Lifespan コンテキストマネージャ

`@app.on_event("startup"/"shutdown")` は非推奨。`lifespan` パラメータを使う。
yield前が起動処理、yield後が終了処理になる。

```python
from contextlib import asynccontextmanager
from fastapi import FastAPI

# アプリ全体で共有するリソース（モジュールスコープの辞書等）
ml_models = {}
db_pool = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- 起動時処理（yield前）---
    # DBコネクションプール・MLモデル・外部サービス接続等を初期化
    ml_models["predictor"] = await load_ml_model()
    db_pool = await create_db_pool(settings.DATABASE_URL)

    yield  # ← アプリがリクエストを受け付ける期間

    # --- 終了時処理（yield後）---
    # 確保したリソースを確実に解放する
    ml_models.clear()
    await db_pool.close()

app = FastAPI(lifespan=lifespan)
```

## 主な用途

| 用途 | 例 |
|-----|---|
| DBコネクションプール | `asyncpg.create_pool()` |
| MLモデルのロード | `torch.load()`, `transformers` |
| 外部サービス接続 | Redis, S3クライアント初期化 |
| バックグラウンドタスク | スケジューラの開始・停止 |

> **注意**: Lifespan イベントはメインアプリのみに適用される。`mount()` したサブアプリには適用されない。
