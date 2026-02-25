---
title: 非同期ルートの使い分け
category: async
tags: async, await, run_in_threadpool, sync, CPU, Celery, blocking
---

## 非同期ルートの使い分け

| シナリオ | 実装方法 |
|---------|---------|
| 非ブロッキングI/O（DB、外部HTTP等） | `async def` + `await` |
| ブロッキングI/O（同期ライブラリ） | `def`（FastAPIが自動でスレッドプール実行） |
| `async def` 内で同期ライブラリを使う | `run_in_threadpool()` |
| CPU集約処理（画像変換・機械学習等） | Celery / multiprocessing にオフロード |

```python
from fastapi.concurrency import run_in_threadpool

# ✅ async def 内で同期ライブラリを安全に呼ぶ
@router.get("/")
async def call_sync_library():
    result = await run_in_threadpool(sync_client.make_request, data=my_data)
    return result

# ✅ ブロッキングI/Oは def ルートで（自動的にスレッドプール実行）
@router.get("/sync")
def blocking_endpoint():
    result = sync_db_client.query("SELECT ...")
    return result
```

> **注意**: `async def` ルート内でブロッキング処理を直接呼ぶとイベントループ全体がブロックされ、
> 全リクエストが詰まる。`run_in_threadpool()` で必ずスレッドプールに委譲すること。
