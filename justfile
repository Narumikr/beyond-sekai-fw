# justfile

# デフォルトレシピ: コマンド一覧を表示
default:
	@just --list

# --- 変数定義 ---

backend_dir := "backend"
frontend_dir := "frontend"
script_dir := "scripts"
backend_port := "8000"
frontend_port := "3000"
uv := "uv"
pnpm := "pnpm"

# --- 開発サーバー起動 ---

# バックエンド開発サーバー起動（FastAPI）
api:
	cd {{backend_dir}} && {{uv}} run fastapi dev app/main.py --port {{backend_port}}

# フロントエンド開発サーバー起動（Next.js）
ui:
	cd {{frontend_dir}} && {{pnpm}} dev

# --- コード品質チェック ---

# バックエンド lint チェック
lint-api:
	cd {{backend_dir}} && {{uv}} run ruff check .

# バックエンド フォーマット
format-api:
	cd {{backend_dir}} && {{uv}} run ruff format .

# バックエンド 型チェック
typecheck-api:
	cd {{backend_dir}} && {{uv}} run pyright

# バックエンド テスト
test-api:
	cd {{backend_dir}} && {{uv}} run pytest

# バックエンド 品質チェック（lint + 型チェック）
check-api: lint-api typecheck-api

# フロントエンド lint チェック
lint-ui:
	cd {{frontend_dir}} && {{pnpm}} lint

# フロントエンド型チェック
typecheck-ui:
	cd {{frontend_dir}} && {{pnpm}} typecheck

# フロントエンド品質チェック（lint + 型チェック）
check-ui: lint-ui typecheck-ui

# フロントエンドテスト実行
test-ui:
	cd {{frontend_dir}} && {{pnpm}} test

# 全サービステスト実行
test-all: test-api test-ui

# 全サービス lint チェック
lint-all: lint-api lint-ui

# 全サービス型チェック
typecheck-all: typecheck-api typecheck-ui

# 全サービス品質チェック
check-all: check-api check-ui

# --- ビルド ---

# フロントエンドビルド
build-ui:
	cd {{frontend_dir}} && {{pnpm}} build

# 全サービスビルド
build-all: build-ui

# --- 依存関係管理 ---

# バックエンド依存関係インストール
install-api:
	cd {{backend_dir}} && {{uv}} sync

# フロントエンド依存関係インストール
install-ui:
	cd {{frontend_dir}} && {{pnpm}} install

# 全サービス依存関係インストール
install-all: install-api install-ui

# --- クリーンアップ ---

# フロントエンドビルド成果物削除
clean-ui:
	cd {{frontend_dir}} && rm -rf .next node_modules/ .cache/

# 全サービスクリーンアップ
clean-all: clean-ui

# --- スキーマ生成 ---

# OpenAPI スキーマを shared/api/openapi.json に出力
gen-openapi:
	cd {{backend_dir}} && {{uv}} run python ../{{script_dir}}/backend/export_openapi.py

# OpenAPI スキーマを生成してブラウザでプレビュー
preview-openapi:
	bash {{script_dir}}/backend/preview_openapi.sh
