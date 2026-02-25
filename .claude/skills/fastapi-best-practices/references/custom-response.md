---
title: カスタムレスポンス
category: response
tags: response_class, StreamingResponse, FileResponse, RedirectResponse, HTMLResponse, JSONResponse, media_type
---

## レスポンスクラスの種類

| クラス | 用途 |
|-------|-----|
| `JSONResponse` | JSON（デフォルト） |
| `HTMLResponse` | HTMLページ返却 |
| `PlainTextResponse` | プレーンテキスト |
| `RedirectResponse` | リダイレクト（301/302/307/308） |
| `StreamingResponse` | 動画・大容量ファイルのストリーミング |
| `FileResponse` | ファイルダウンロード |
| `Response` | XML等の任意フォーマット |

## コード例

```python
from fastapi.responses import (
    StreamingResponse, FileResponse, RedirectResponse, Response
)

# ストリーミング（大容量ファイルをメモリに載せない）
@router.get("/video")
def stream_video():
    def iterfile():
        with open("large-video.mp4", "rb") as f:
            yield from f
    return StreamingResponse(iterfile(), media_type="video/mp4")

# ファイルダウンロード
@router.get("/download")
async def download_file():
    return FileResponse("report.pdf", filename="report.pdf")

# リダイレクト
@router.get("/old-path")
async def redirect():
    return RedirectResponse("/new-path", status_code=301)

# XML等の任意フォーマット
@router.get("/data.xml")
def get_xml():
    return Response(content="<data/>", media_type="application/xml")
```

## デフォルトレスポンスクラスの変更

アプリ全体のデフォルトを変更したい場合は `default_response_class` を使う。

```python
from fastapi.responses import ORJSONResponse

# orjson を使って高速なJSONシリアライズ
app = FastAPI(default_response_class=ORJSONResponse)
```
