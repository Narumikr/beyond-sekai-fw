---
title: Pythonicなパターン
category: patterns
tags: comprehension, generator, f-string, type-hints, dataclass, pathlib, walrus, unpacking
---

## 内包表記

```python
# ✅ リスト内包表記（ループより簡潔）
squares = [x**2 for x in range(10)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# ✅ 辞書内包表記
word_lengths = {word: len(word) for word in words}

# ✅ 集合内包表記
unique_initials = {name[0] for name in names}

# ✅ ジェネレータ式（メモリ効率）
total = sum(x**2 for x in range(1000000))

# ❌ 複雑な内包表記は可読性を損なう（通常のループで書く）
result = [f(x) for x in data if g(x) for y in x if h(y)]  # NG
```

## f文字列（Python 3.6+）

```python
name = "Alice"
age = 30

# ✅ f文字列（推奨）
message = f"Hello, {name}! You are {age} years old."

# ✅ 書式指定
price = 1234.5678
formatted = f"Price: {price:.2f}"  # "Price: 1234.57"

# ✅ デバッグ用（= を使う、Python 3.8+）
print(f"{name=}, {age=}")  # "name='Alice', age=30"

# ❌ 古い形式（非推奨）
message = "Hello, %s! You are %d years old." % (name, age)
message = "Hello, {}! You are {} years old.".format(name, age)
```

## 型ヒント（Python 3.10+記法）

```python
# ✅ 基本的な型ヒント
def greet(name: str) -> str:
    return f"Hello, {name}"

# ✅ Union型（Python 3.10+ は | を使用）
def find_user(user_id: int) -> User | None:
    ...

# ✅ コレクションの型
def process(items: list[int]) -> dict[str, int]:
    ...

# ✅ 省略可能な引数
def create(name: str, age: int | None = None) -> User:
    ...
```

## アンパック・代入

```python
# ✅ タプルアンパック
x, y = 1, 2
first, *rest = [1, 2, 3, 4]

# ✅ スワップ（一時変数不要）
a, b = b, a

# ✅ enumerate（インデックスと値を同時に取得）
for i, item in enumerate(items):
    print(f"{i}: {item}")

# ✅ zip（複数のリストを同時にイテレート）
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# ✅ セイウチ演算子（Python 3.8+）
while chunk := file.read(8192):
    process(chunk)
```

## dataclass

```python
from dataclasses import dataclass, field

# ✅ データクラスで __init__ を省略
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0
    tags: list[str] = field(default_factory=list)

p = Point(1.0, 2.0)
```

## pathlib（ファイルパス操作）

```python
from pathlib import Path

# ✅ pathlib（os.path より可読性が高い）
config_path = Path("config") / "settings.json"
content = config_path.read_text(encoding="utf-8")

# よく使うメソッド
path = Path("/some/file.txt")
path.exists()          # 存在確認
path.suffix            # ".txt"
path.stem              # "file"
path.parent            # "/some"
path.name              # "file.txt"
list(path.parent.glob("*.txt"))  # glob検索

# ❌ os.path（非推奨）
import os
config_path = os.path.join("config", "settings.json")
```
