from dataclasses import dataclass

from fastapi import Query


@dataclass
class Pagination:
    """ページネーションパラメータを依存性として注入する"""

    skip: int = Query(default=0, ge=0)
    limit: int = Query(default=10, ge=1, le=100)
