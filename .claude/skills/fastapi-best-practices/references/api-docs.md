---
title: APIドキュメント
category: documentation
tags: OpenAPI, Swagger, docs, response_model, status_code, tags, production
---

## 本番環境ではSwagger UIを非表示にする

本番環境での意図しない情報公開を防ぐ。

```python
SHOW_DOCS_ENVIRONMENT = ("local", "staging")

app_configs = {"title": "My API"}
if settings.ENVIRONMENT not in SHOW_DOCS_ENVIRONMENT:
    app_configs["openapi_url"] = None  # Swagger UIとOpenAPIスキーマを無効化

app = FastAPI(**app_configs)
```

## エンドポイントを適切にドキュメント化する

`response_model`、`status_code`、`responses` を明示することでOpenAPIスキーマが正確になる。

```python
from fastapi import status

@router.post(
    "/posts",
    response_model=PostResponse,
    status_code=status.HTTP_201_CREATED,
    description="新しい投稿を作成する",
    tags=["posts"],
    responses={
        status.HTTP_201_CREATED: {"model": PostCreatedResponse},
        status.HTTP_400_BAD_REQUEST: {"model": ErrorResponse},
        status.HTTP_422_UNPROCESSABLE_ENTITY: {"model": ValidationErrorResponse},
    },
)
async def create_post(body: PostCreate) -> PostResponse:
    ...
```
