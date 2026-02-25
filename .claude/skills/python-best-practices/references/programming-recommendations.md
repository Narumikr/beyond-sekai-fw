---
title: プログラミング推奨事項
category: best-practices
tags: PEP8, None, isinstance, exceptions, return, truthiness, comparison
---

## None・真偽値の比較

```python
# ✅ None との比較は is / is not を使う
if x is None:
    pass
if x is not None:
    pass

# ❌ == で比較しない
if x == None:   # NG
if x != None:   # NG

# ✅ bool との比較は不要（直接評価）
if is_valid:
    pass
if not is_valid:
    pass

# ❌ True/False と == で比較しない
if is_valid == True:    # NG
if is_valid is True:    # NGではないが冗長
```

## 型チェック

```python
# ✅ isinstance を使う（継承も考慮される）
if isinstance(obj, int):
    pass

# ✅ 複数の型を同時にチェック
if isinstance(obj, (int, float)):
    pass

# ❌ type() との直接比較は避ける
if type(obj) is int:     # 継承を考慮しない
if type(obj) == int:     # 同上
```

## 例外処理

```python
# ✅ 具体的な例外クラスを指定
try:
    value = int(user_input)
except ValueError:
    print("Invalid input")

# ✅ 複数の例外をまとめてキャッチ
try:
    connect()
except (ConnectionError, TimeoutError) as e:
    logger.error("Connection failed: %s", e)

# ❌ 裸の except は禁止（KeyboardInterrupt も捕捉してしまう）
try:
    do_something()
except:
    pass  # NG

# ✅ Exception を基底クラスとして使うことは許容
try:
    do_something()
except Exception as e:
    logger.error("Unexpected error: %s", e)
    raise
```

## 文字列操作

```python
# ✅ startswith / endswith を使う
if foo.startswith("bar"):
    pass
if filename.endswith(".py"):
    pass

# ❌ スライスで代替しない
if foo[:3] == "bar":   # NG
```

## 関数の戻り値

```python
# ✅ 戻り値は一貫させる（Noneも明示）
def find_user(user_id: int) -> User | None:
    if user_id > 0:
        return get_user_from_db(user_id)
    return None  # 明示的に None を返す

# ❌ 一部だけ return して他は None を暗黙的に返す
def find_user(user_id: int):
    if user_id > 0:
        return get_user_from_db(user_id)
    # ここで None が暗黙的に返される（NG）
```

## シーケンスの真偽値評価

```python
# ✅ 空のシーケンスは False として評価される（len() 不要）
if not items:          # リスト・タプル・文字列が空かチェック
    print("empty")
if items:              # 要素があるかチェック
    process(items)

# ❌ len() を使った冗長な比較
if len(items) == 0:    # NG
if len(items) > 0:     # NG
```

## コンテキストマネージャ

```python
# ✅ ファイル操作は with を使う（自動クローズ）
with open("file.txt", "r") as f:
    content = f.read()

# ❌ 手動でクローズ
f = open("file.txt", "r")
content = f.read()
f.close()  # 例外が起きるとクローズされない
```
