---
title: Pydanticの活用
category: pydantic
tags: pydantic, BaseModel, Field, validation, EmailStr, BaseSettings, settings, config
---

## 組み込みバリデータを積極的に使う

`Field()` と型アノテーションで宣言的にバリデーションする。

```python
from pydantic import BaseModel, EmailStr, Field, AnyUrl

class UserCreate(BaseModel):
    username: str = Field(min_length=1, max_length=128, pattern="^[A-Za-z0-9-_]+$")
    email: EmailStr
    age: int = Field(ge=18)
    website: AnyUrl | None = None
```

## カスタムベースモデルで一貫性を確保

プロジェクト全体で共有するベースモデルを作り、datetime形式等を統一する。

```python
from pydantic import BaseModel, ConfigDict
from datetime import datetime

def datetime_to_gmt_str(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S%z")

class CustomModel(BaseModel):
    model_config = ConfigDict(
        json_encoders={datetime: datetime_to_gmt_str},
        populate_by_name=True,
    )
```

## BaseSettingsはドメイン別に分割する

単一の巨大な `BaseSettings` は避ける。ドメインごとに独立したクラスを作る。

```python
# src/auth/config.py
from pydantic_settings import BaseSettings

class AuthConfig(BaseSettings):
    JWT_ALG: str
    JWT_SECRET: str
    JWT_EXP: int = 5  # minutes

auth_settings = AuthConfig()

# src/config.py（グローバル設定）
class GlobalConfig(BaseSettings):
    DATABASE_URL: str
    ENVIRONMENT: str = "local"

settings = GlobalConfig()
```
