---
title: ミドルウェア
category: middleware
tags: middleware, HTTPS, TrustedHost, GZip, CORS, ASGI, security
---

## 組み込みミドルウェア

```python
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.gzip import GZipMiddleware

# 1. HTTPSへ強制リダイレクト（本番環境で使用）
app.add_middleware(HTTPSRedirectMiddleware)

# 2. ホストヘッダー攻撃対策（許可するホストを明示）
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["example.com", "*.example.com"]
)

# 3. GZip圧縮（minimum_size バイト以上のレスポンスを自動圧縮）
app.add_middleware(GZipMiddleware, minimum_size=1000, compresslevel=5)
```

## CORSミドルウェア

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://example.com"],  # 本番は具体的なオリジンを指定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## ミドルウェアの適用順

ミドルウェアは **追加した逆順** で適用される（後入れ先出し）。
セキュリティ系（HTTPS、TrustedHost）を最後に追加すると最初に評価される。

```python
app.add_middleware(GZipMiddleware)        # 3番目に評価
app.add_middleware(CORSMiddleware, ...)   # 2番目に評価
app.add_middleware(HTTPSRedirectMiddleware)  # 最初に評価（リクエスト入口）
```
