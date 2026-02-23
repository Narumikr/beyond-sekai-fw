---
title: テスト
category: testing
tags: pytest, AsyncClient, httpx, asyncio, dependency_overrides, mock, fixture
---

## 非同期テストクライアントを最初から使う

`TestClient` ではなく `httpx.AsyncClient` + `ASGITransport` を使う。

```python
import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.fixture
async def client():
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test"
    ) as client:
        yield client

@pytest.mark.asyncio
async def test_create_post(client: AsyncClient):
    resp = await client.post("/posts", json={"title": "test"})
    assert resp.status_code == 201
    assert resp.json()["title"] == "test"
```

## テスト時の依存性オーバーライド

`app.dependency_overrides` で外部サービス・認証をモックに差し替える。
テスト後は必ずリセットする。

```python
from fastapi.testclient import TestClient
from app.main import app
from app.auth.dependencies import get_current_user

# テスト用モック
async def mock_current_user():
    return {"user_id": "test-user-id", "role": "admin"}

def test_protected_endpoint():
    app.dependency_overrides[get_current_user] = mock_current_user
    client = TestClient(app)

    response = client.get("/admin/dashboard")
    assert response.status_code == 200

    app.dependency_overrides = {}  # 必ずリセット（他のテストに影響しないよう）
```

> **ユースケース**: JWT検証・外部API・有料サービス・重い処理を持つ依存性をテスト時に差し替える
