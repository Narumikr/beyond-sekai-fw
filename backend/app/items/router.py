from fastapi import APIRouter, Depends, HTTPException

from app.items.dependencies import Pagination
from app.items.schemas import ItemCreate, ItemResponse

router = APIRouter(prefix="/items", tags=["items"])

# in-memoryストア（サンプル用。実際はDBセッションをDependsで注入する）
_store: dict[int, dict] = {
    1: {"id": 1, "name": "サンプルアイテム", "description": "初期データ"},
}
_next_id = 2


@router.get("", response_model=list[ItemResponse])
async def list_items(pagination: Pagination = Depends()) -> list[ItemResponse]:
    items = list(_store.values())
    page = items[pagination.skip : pagination.skip + pagination.limit]
    return [ItemResponse(**item) for item in page]


@router.post("", response_model=ItemResponse, status_code=201)
async def create_item(body: ItemCreate) -> ItemResponse:
    global _next_id
    item = {"id": _next_id, **body.model_dump()}
    _store[_next_id] = item
    _next_id += 1
    return ItemResponse(**item)


@router.get("/{item_id}", response_model=ItemResponse)
async def get_item(item_id: int) -> ItemResponse:
    item = _store.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(**item)
