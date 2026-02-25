---
title: 高度な依存性注入（Callableクラス）
category: dependencies
tags: Depends, callable, class, __init__, __call__, parameterized, role, permission
---

## パラメータ付き依存性（Callableクラス）

同じロジックを異なるパラメータで再利用したい場合は、`__init__` + `__call__` を持つクラスを使う。

```python
from typing import Annotated
from fastapi import Depends, HTTPException

class RoleChecker:
    def __init__(self, required_role: str):
        self.required_role = required_role  # __init__ でパラメータを受け取る

    def __call__(self, user: dict = Depends(get_current_user)) -> dict:
        # __call__ で依存性ロジックを実装
        if user["role"] != self.required_role:
            raise HTTPException(status_code=403, detail="権限不足")
        return user

# クラスではなく、インスタンスを Depends に渡す
admin_only = RoleChecker("admin")
editor_only = RoleChecker("editor")

@router.delete("/posts/{post_id}", dependencies=[Depends(admin_only)])
async def delete_post(post_id: UUID4): ...

@router.patch("/posts/{post_id}", dependencies=[Depends(editor_only)])
async def update_post(post_id: UUID4): ...
```

## ポイント

- `__init__()`: 依存性をカスタマイズするパラメータを定義
- `__call__()`: リクエストごとに実行される依存性ロジック
- インスタンスを `Depends()` に渡す（クラスではない）
- ロール検証・レート制限・機能フラグなどに応用できる
