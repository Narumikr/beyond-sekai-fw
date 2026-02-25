---
title: コードレイアウト
category: style
tags: PEP8, indentation, line-length, blank-lines, imports, whitespace
---

## インデント

```python
# ✅ 4スペース（タブは使わない）
def long_function_name(
        var_one, var_two,
        var_three, var_four):
    print(var_one)

# 継続行はオープン区切り文字に揃える
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

# または4スペース追加インデントで区別
def long_function_name(
        var_one, var_two):
    print(var_one)
```

## 行の長さ

| 対象 | 最大文字数 |
|------|-----------|
| コード行 | **79文字** |
| docstring / コメント | **72文字** |

```python
# ✅ バックスラッシュより括弧で継続（推奨）
result = (some_variable
          + another_variable
          - third_variable)

# ✅ 文字列の暗黙的な連結
message = (
    "This is a very long string that "
    "spans multiple lines."
)
```

## 空行

```python
class MyClass:
    """クラスの説明。"""

    class_var = 1   # クラス変数

    def method_one(self):
        pass

    def method_two(self):  # メソッド間は1行空ける
        pass


class AnotherClass:  # トップレベルの定義間は2行空ける
    pass


def standalone_function():  # トップレベル関数も2行空ける
    pass
```

## インポート

```python
# ✅ 正しい順序（グループ間は空行）
import os
import sys                          # 1. 標準ライブラリ

import requests                     # 2. サードパーティ
from fastapi import FastAPI

from myapp.models import User       # 3. ローカルアプリケーション
from myapp.utils import format_date

# ✅ 1行に1インポート
import os
import sys

# ❌ 複数を1行でインポート
import os, sys

# ✅ 絶対インポートを優先
from mypackage import module

# ✅ 相対インポートが必要な場合は明示的に
from . import sibling
from ..parent import something

# ❌ ワイルドカードインポートは禁止
from module import *
```
