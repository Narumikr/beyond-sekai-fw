---
title: Zen of Python（設計思想）
category: philosophy
tags: PEP20, zen, design, philosophy, guiding-principles
---

## Zen of Python（PEP 20）

Pythonの設計哲学。`import this` で確認できる19か条の指針。

```
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
```

## 重要な指針と実践

| 指針 | 意味 | 実践例 |
|------|------|--------|
| Explicit is better than implicit | 隠れた挙動より明示的な記述 | マジックメソッドの多用を避け、明示的なメソッド呼び出しを優先 |
| Simple is better than complex | シンプルな解決策を優先 | 1つの関数は1つの責務 |
| Flat is better than nested | 深いネストを避ける | 早期リターンでネストを減らす |
| Errors should never pass silently | エラーを隠蔽しない | 裸の `except:` を使わず、ログまたは再送出する |
| Readability counts | 可読性は最重要 | コードは書く回数より読まれる回数の方が多い |

## 実践例

```python
# ❌ Implicit（暗黙的）
def get_user(id):
    return db.query(id)  # Noneが返る可能性を隠蔽

# ✅ Explicit（明示的）
def get_user(id: int) -> User | None:
    return db.query(User, id)

# ❌ Nested（深いネスト）
def process(data):
    if data:
        if data.valid:
            if data.items:
                return data.items[0]

# ✅ Flat（早期リターン）
def process(data):
    if not data:
        return None
    if not data.valid:
        return None
    if not data.items:
        return None
    return data.items[0]

# ❌ Silent error（エラー隠蔽）
try:
    result = risky_operation()
except:
    pass  # 何も起きなかったように見せる

# ✅ Explicit error handling
try:
    result = risky_operation()
except ValueError as e:
    logger.error("Invalid value: %s", e)
    raise
```
