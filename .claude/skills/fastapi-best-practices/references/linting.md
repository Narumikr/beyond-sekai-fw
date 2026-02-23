---
title: リント・フォーマット
category: tooling
tags: ruff, lint, format, flake8, black, isort, CI
---

## ruff を使用する

flake8・black・isort の代替として高速なオールインワンツール。

```bash
# リント（自動修正付き）
ruff check --fix src/

# フォーマット
ruff format src/
```

## pyproject.toml 設定例

```toml
[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E", "F", "I", "N", "UP", "ANN"]
ignore = ["ANN101", "ANN102"]

[tool.ruff.lint.isort]
known-first-party = ["src"]
```

## CI での使用

```yaml
# .github/workflows/lint.yml
- name: Lint
  run: |
    ruff check src/
    ruff format --check src/
```
