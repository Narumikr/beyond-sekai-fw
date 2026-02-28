from contextlib import asynccontextmanager
from typing import TypedDict

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import app_settings, cors_settings
from app.items import (
    router as items_router,  # TODO: サンプル実装なので、プロジェクト開始時に削除
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    # 起動時: DB接続・外部サービス初期化などをここで行う
    print(f"Starting {app_settings.app_name}...")
    yield
    # 終了時: リソース解放などをここで行う
    print("Shutting down...")

app = FastAPI(
    title=app_settings.app_name,
    debug=app_settings.debug,
    lifespan=lifespan,
    openapi_url="/openapi.json" if app_settings.openapi_enabled else None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_settings.allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# TODO: サンプル実装なので、プロジェクト開始時に削除
app.include_router(items_router.router)


class HealthResponse(TypedDict):
    status: str


@app.get("/health", tags=["health"])
async def health_check() -> HealthResponse:
    return {"status": "Hello, SEKAI"}
