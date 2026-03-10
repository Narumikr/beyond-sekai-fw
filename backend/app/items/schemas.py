from pydantic import BaseModel, ConfigDict, Field


# リクエスト用（idなし・作成時のみ使う項目を定義）
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: str | None = Field(default=None, max_length=500)


# レスポンス用（サーバー付与項目を含む）
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str | None

    model_config = ConfigDict(from_attributes=True)
