---
title: コメント・Docstring
category: documentation
tags: PEP8, comments, docstrings, inline-comments, block-comments
---

## コメントの原則

- **コードと矛盾するコメントはコメントなしより悪い**
- コメントは「なぜ（why）」を説明する。「何を（what）」はコードが語る
- コードが変わったらコメントも更新する

## ブロックコメント

```python
# これはブロックコメントです。
# コードと同じインデントレベルで記述します。
# 各行は '# ' で始めます（空行は '#' のみ）。

def process_data(data):
    # ステップ1: データを正規化
    normalized = normalize(data)

    # ステップ2: フィルタリング（負の値を除外）
    filtered = [x for x in normalized if x >= 0]
    return filtered
```

## インラインコメント

```python
# ✅ 最低2スペース離してから '# '
x = x + 1  # カウンタをインクリメント

# ❌ 自明なことを書かない（コードの翻訳はNG）
x = x + 1  # xに1を加える
```

## Docstring（PEP 257準拠）

```python
# ✅ 一行Docstring（閉じる '"""' は同じ行）
def add(a: int, b: int) -> int:
    """2つの整数を足して返す。"""
    return a + b


# ✅ 複数行Docstring
def complex_function(param1: str, param2: int) -> dict:
    """関数の概要を1行で記述する。

    必要に応じて詳細な説明を続ける。
    空行を1行挟んでから詳細を書く。

    Args:
        param1: 説明文
        param2: 説明文

    Returns:
        返り値の説明

    Raises:
        ValueError: 不正な値が渡された場合
    """
    ...


# ✅ クラスのDocstring
class MyClass:
    """クラスの概要を記述する。

    クラスの詳細な説明、使用方法など。

    Attributes:
        attr1: 属性の説明
        attr2: 属性の説明
    """

    def __init__(self, attr1: str, attr2: int):
        self.attr1 = attr1
        self.attr2 = attr2
```

## よくある間違い

```python
# ❌ 開始の '"""' と同じ行にテキストを続けて複数行
"""これは
複数行です"""

# ✅ 複数行のdocstringは最初の行に概要、その後詳細
"""これは概要。

詳細な説明。
"""
```
