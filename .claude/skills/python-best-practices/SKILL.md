---
name: python-best-practices
description: Pythonのベストプラクティスを適用してコード設計・実装・レビューを支援する。ユーザーが「Pythonのコードを書いて」「コードをレビューして」「リファクタリングして」と依頼した時、またはPythonの命名規則・コードスタイル・型ヒント・例外処理・Pythonicなパターンに関わるコードの作成・レビュー・リファクタリングを行う時に使用する。
---

# Python ベストプラクティス

PEP 8（コードスタイル）・PEP 20（設計思想）に基づくPython実践リファレンス。
設計・実装・レビューのすべてのフェーズで参照すること。

## 適用タイミング

- 新しいモジュール・クラス・関数を作成する時
- 命名規則・コードスタイルを決定する時
- Pythonコードをレビュー・リファクタリングする時
- 例外処理・型ヒント・Pythonicなパターンを実装する時

## カテゴリ別リファレンス

### 設計思想

| リファレンス | 説明 |
|------------|------|
| `references/zen-of-python` | PEP 20 — Pythonの設計哲学19か条 |

### コードスタイル（PEP 8）

| リファレンス | 説明 |
|------------|------|
| `references/naming-conventions` | 関数・クラス・定数・プライベートの命名規則 |
| `references/code-layout` | インデント・行長・空行・インポート順 |
| `references/whitespace` | 演算子・カンマ・スライスの空白ルール |
| `references/comments-docstrings` | コメント・docstringの書き方 |

### 実装パターン

| リファレンス | 説明 |
|------------|------|
| `references/programming-recommendations` | None比較・型チェック・例外処理・戻り値の一貫性 |
| `references/pythonic-patterns` | 内包表記・コンテキストマネージャ・f文字列・型ヒント |

---

## よくある間違い

| 間違い | 正しい実装 |
|-------|------------|
| `if x == None:` | `if x is None:` |
| `if type(x) is int:` | `if isinstance(x, int):` |
| `except:` で全例外をキャッチ | 具体的な例外クラスを指定 |
| `from module import *` | 明示的なインポート |
| `foo[:3] == 'bar'` | `foo.startswith('bar')` |
| インライン変数名 `l`, `O`, `I` | 誤読しない名前を使う |
| タブでインデント | 4スペースでインデント |
| 型ヒントなしの関数定義 | `def func(x: int) -> str:` で型を明示 |
