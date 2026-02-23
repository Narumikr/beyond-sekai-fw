---
title: 空白ルール
category: style
tags: PEP8, whitespace, operators, commas, slices, trailing-whitespace
---

## 不要な空白を避ける場所

```python
# ❌ 括弧の内側
spam( ham[ 1 ], { eggs: 2 } )

# ✅ 正しい
spam(ham[1], {eggs: 2})

# ❌ スライスのコロン前後（パラメータがない場合）
ham[1: 9], ham[1 :9]

# ✅ スライスは対称的に
ham[1:9], ham[1:9:3], ham[:9:3]

# ❌ 関数呼び出しの括弧前
spam (1)

# ✅ 正しい
spam(1)

# ❌ インデックスのブラケット前
dict ['key']

# ✅ 正しい
dict['key']

# ❌ 行末の空白
x = 1
```

## 演算子の空白

```python
# ✅ 代入・比較・論理演算子はスペースで囲む
x = 1
y = x + 1
if x == y:
    pass

# ✅ デフォルト引数・キーワード引数はスペースなし（アノテーションなし）
def func(x=1, y=2): ...
func(x=1, y=2)

# ✅ アノテーション付きデフォルト引数はスペースあり（重要な例外）
def func(x: int = 1, y: str = "default"): ...
#                 ^               ^  アノテーションがある場合は = の両側にスペースが必要

# ✅ 優先度が高い演算子はスペースなしで表現してもよい
x = x*2 - 1
c = (a+b) * (a-b)
hypot2 = x*x + y*y

# ❌ ただしスペースを混在させない
x = x *2-1   # 混在はNG
```

## カンマ・コロン・セミコロン

```python
# ❌ カンマの前にスペース
spam(ham[1] , {eggs: 2})

# ✅ カンマの後にスペース
spam(ham[1], {eggs: 2})

# ❌ 複数文をセミコロンで区切る
x = 1; y = 2

# ✅ 1行に1文
x = 1
y = 2
```
