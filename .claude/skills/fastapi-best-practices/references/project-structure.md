---
title: プロジェクト構造
category: architecture
tags: project-structure, domain, import, module
---

## プロジェクト構造

ドメイン単位で分割し、各モジュールの責務を明確に保つ。

```
src/
├── auth/
│   ├── router.py       # APIエンドポイント
│   ├── schemas.py      # Pydanticモデル
│   ├── models.py       # DBモデル（SQLAlchemy等）
│   ├── service.py      # ビジネスロジック
│   ├── dependencies.py # ルート依存性
│   ├── config.py       # 環境変数（BaseSettings）
│   ├── constants.py    # 定数・エラーコード
│   ├── exceptions.py   # ドメイン固有の例外
│   └── utils.py        # ヘルパー関数
├── posts/
│   └── ...
└── config.py           # グローバル設定
```

## インポート規約

ドメイン間は明示的なモジュール名でインポートする。

```python
# ✅ 良い例
from src.auth import constants as auth_constants
from src.notifications import service as notification_service

# ❌ 悪い例（名前衝突・依存が不明確になる）
from src.auth.constants import *
```
