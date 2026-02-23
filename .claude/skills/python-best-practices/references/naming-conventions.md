---
title: 命名規則
category: style
tags: PEP8, naming, snake_case, CamelCase, constants, private, dunder
---

## 命名規則一覧（PEP 8）

| 対象 | 形式 | 例 |
|------|------|-----|
| 関数・メソッド | `snake_case` | `get_user()`, `calculate_total()` |
| 変数 | `snake_case` | `user_name`, `item_count` |
| クラス | `CapWords` | `UserProfile`, `HTTPClient` |
| 定数 | `UPPER_SNAKE_CASE` | `MAX_RETRY`, `DEFAULT_TIMEOUT` |
| モジュール | `snake_case` | `user_service.py`, `auth_utils.py` |
| パッケージ | 小文字・アンダースコアなし推奨 | `mypackage/` |
| 型変数 | `CapWords` (短い) | `T`, `KT`, `VT` |

## プライベート・特殊な命名

```python
class MyClass:
    # パブリック（外部から使用可）
    public_attr = "value"

    # 規約的にプライベート（アンダースコア1つ）
    _internal_attr = "value"

    # 名前マングリング（アンダースコア2つ）→ _MyClass__private
    __mangled_attr = "value"

    # マジックメソッド（ダンダー）
    def __init__(self): ...
    def __repr__(self): ...
```

## 避けるべき名前

```python
# ❌ 数字と誤読しやすい1文字変数名
l = 1     # 'l' (小文字エル) → 1と混同
O = 0     # 'O' (大文字オー) → 0と混同
I = 1     # 'I' (大文字アイ) → 1と混同

# ✅ 意味のある名前を使う
length = 1
origin = 0
index = 1
```

## 関数・変数の命名パターン

```python
# 動詞 + 目的語（関数）
def get_user_by_id(user_id: int) -> User: ...
def calculate_monthly_revenue(year: int, month: int) -> Decimal: ...
def validate_email_format(email: str) -> bool: ...

# 名詞（変数・属性）
user_count = 0
active_users: list[User] = []
is_authenticated = False  # bool は is_, has_, can_ プレフィックスが読みやすい
```
