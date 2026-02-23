---
title: プロキシ背後での動作（root_path）
category: deployment
tags: proxy, root_path, Nginx, Traefik, OpenAPI, forwarded, ASGI
---

## root_path の設定

Nginx / Traefik等のリバースプロキシ背後で動かす場合は `root_path` を設定する。
未設定だとSwagger UIのサーバーURLが壊れてAPI呼び出しが失敗する。

```python
# 方法1: FastAPI インスタンスで設定（推奨）
app = FastAPI(root_path="/api/v1")

# 方法2: 起動コマンドで指定
# fastapi run main.py --root-path /api/v1 --forwarded-allow-ips="*"
```

## フォワードヘッダーの信頼設定

```bash
# プロキシからのヘッダーを信頼する（本番では特定IPのみ許可を推奨）
fastapi run main.py --forwarded-allow-ips="10.0.0.1"

# 開発・内部ネットワークの場合（全IP許可）
fastapi run main.py --forwarded-allow-ips="*"
```

## 複数環境対応（OpenAPI サーバー設定）

```python
app = FastAPI(
    root_path="/api/v1",
    servers=[
        {"url": "https://api.example.com", "description": "Production"},
        {"url": "https://staging.example.com/api/v1", "description": "Staging"},
    ],
)
```

## デバッグ確認

```python
@app.get("/debug/root-path")
def check_root_path(request: Request):
    return {"root_path": request.scope.get("root_path")}
```
