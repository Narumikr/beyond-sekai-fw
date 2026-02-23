---
title: データベース（SQLAlchemy + Alembic）
category: database
tags: SQLAlchemy, Alembic, migration, naming, index, N+1, SQL, ORM
---

## 命名規約

| 対象 | 規約 | 例 |
|-----|------|---|
| テーブル名 | `lower_snake_case`、単数形 | `post`, `user`, `post_like` |
| 関連テーブル | ドメインプレフィックス | `payment_account`, `payment_bill` |
| 日時カラム | `_at` サフィックス | `created_at`, `updated_at` |
| 日付カラム | `_date` サフィックス | `birth_date` |

## インデックス名を明示的に設定する

マイグレーション間で一貫したインデックス名を保つためにMetaDataに規約を設定する。

```python
POSTGRES_INDEXES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",
    "uq": "%(table_name)s_%(column_0_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}

metadata = MetaData(naming_convention=POSTGRES_INDEXES_NAMING_CONVENTION)
```

## SQLファーストアプローチ（N+1問題の回避）

複雑な集計・JOINはSQLで行い、Pythonループで追加クエリを発行しない。

```python
# ✅ SQLで一度に集計する
posts = await db.execute(
    select(Post, func.count(PostLike.id).label("like_count"))
    .outerjoin(PostLike)
    .group_by(Post.id)
)

# ❌ N+1問題（投稿数だけクエリが増える）
posts = await db.execute(select(Post))
for post in posts:
    post.like_count = await db.scalar(
        select(func.count(PostLike.id)).where(PostLike.post_id == post.id)
    )
```

## Alembicマイグレーション

- マイグレーションは静的で復元可能（downgrade実装必須）に保つ
- 説明的なファイル名で変更内容が一目でわかるようにする

```ini
# alembic.ini
# NOTE: alembic.ini は ConfigParser を使うため % を %% に二重にすること
file_template = %%(year)d-%%(month).2d-%%(day).2d_%%(slug)s
# 生成例: 2024-08-24_post_content_idx.py
```
