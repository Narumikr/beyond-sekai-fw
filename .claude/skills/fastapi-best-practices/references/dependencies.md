---
title: 依存性注入（Dependencies）
category: dependencies
tags: Depends, dependency, injection, validation, chain, cache, reuse
---

## 検証ロジックに依存性を活用する

`Depends()` はバリデーション層として機能し、ルート関数をシンプルに保つ。

```python
from fastapi import Depends, HTTPException
from pydantic import UUID4

# ✅ 依存性でバリデーション + オブジェクト取得を行う
async def valid_post_id(post_id: UUID4) -> dict:
    post = await service.get_by_id(post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.get("/posts/{post_id}")
async def get_post(post: dict = Depends(valid_post_id)):
    return post  # ルート関数はビジネスロジックのみ
```

## 依存性の連鎖でロジックを再利用する

依存性は他の依存性を使用でき、重複ロジックを排除できる。

```python
async def valid_owned_post(
    post: dict = Depends(valid_post_id),      # 投稿の存在確認を再利用
    token_data: dict = Depends(parse_jwt_data), # 認証を再利用
) -> dict:
    if post["creator_id"] != token_data["user_id"]:
        raise HTTPException(status_code=403, detail="Not the owner")
    return post

@router.put("/posts/{post_id}")
async def update_post(post: dict = Depends(valid_owned_post)):
    ...
```

## 依存性のキャッシュ

同じ依存関数はリクエストスコープ内で1回だけ実行される。
複数箇所で同じ依存性を参照してもDBクエリ等は重複しない。

```python
# parse_jwt_data が valid_post_id と valid_owned_post の両方で使われていても、
# 1リクエスト中に1回だけ実行される
```

## async 依存性を優先する

```python
# ✅ async 依存性（推奨）
async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return await auth_service.decode_token(token)

# ❌ sync 依存性（不必要なスレッドプールのオーバーヘッドが発生）
def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    return auth_service.decode_token(token)
```

> sync 依存性はスレッドプールで実行されるため、小さな処理でも不必要なオーバーヘッドが発生する。
> 特別な理由がない限り `async def` を使うこと。
