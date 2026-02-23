# justfile

# デフォルトレシピ: コマンド一覧を表示
default:
	@just --list

# --- 変数定義 ---

backend_dir := "backend"
frontend_dir := "frontend"
backend_port := "8000"
frontend_port := "3000"
uv := "uv"
pnpm := "pnpm"

# --- 開発サーバー起動 ---

# バックエンド開発サーバー起動（FastAPI）
api:
	cd {{backend_dir}} && {{uv}} run fastapi dev main.py --port {{backend_port}}

# フロントエンド開発サーバー起動（Next.js）
ui:
	cd {{frontend_dir}} && {{pnpm}} dev

# --- コード品質チェック ---

# フロントエンド lint チェック
lint-ui:
	cd {{frontend_dir}} && {{pnpm}} lint

# フロントエンド型チェック
typecheck-ui:
	cd {{frontend_dir}} && {{pnpm}} typecheck

# フロントエンド品質チェック（lint + 型チェック）
check-ui: lint-ui typecheck-ui

# 全サービス lint チェック
lint-all: lint-ui

# 全サービス型チェック
typecheck-all: typecheck-ui

# 全サービス品質チェック
check-all: check-ui

# --- ビルド ---

# フロントエンドビルド
build-ui:
	cd {{frontend_dir}} && {{pnpm}} build

# 全サービスビルド
build-all: build-ui

# --- 依存関係管理 ---

# フロントエンド依存関係インストール
install-ui:
	cd {{frontend_dir}} && {{pnpm}} install

# 全サービス依存関係インストール
install-all: install-ui

# --- クリーンアップ ---

# フロントエンドビルド成果物削除
clean-ui:
	cd {{frontend_dir}} && rm -rf .next node_modules/ .cache/

# 全サービスクリーンアップ
clean-all: clean-ui