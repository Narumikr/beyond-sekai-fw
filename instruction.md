# AI-Driven Development Instructions / AI駆動開発手順

## Getting Started / はじめに

This document provides instructions for using AI assistants (Claude, GitHub Copilot, Kiro, Codex) effectively in this project.

このドキュメントは、このプロジェクトでAIアシスタント（Claude、GitHub Copilot、Kiro、Codex）を効果的に使用するための手順を提供します。

## Setup / セットアップ

### Prerequisites / 前提条件

1. Read the project README.md
2. Review CLAUDE.md for development guidelines
3. Understand the skills outlined in SKILL.md
4. Familiarize yourself with the project structure

1. プロジェクトのREADME.mdを読む
2. 開発ガイドラインについてCLAUDE.mdをレビューする
3. SKILL.mdで概説されているスキルを理解する
4. プロジェクト構造に慣れる

### Environment / 環境

Ensure your development environment is properly configured:

開発環境が適切に設定されていることを確認してください：

- Install required dependencies
- Set up linters and formatters
- Configure IDE/editor with appropriate extensions
- 必要な依存関係をインストールする
- リンターとフォーマッターをセットアップする
- 適切な拡張機能でIDE/エディタを設定する

## Development Workflow / 開発ワークフロー

### 1. Understanding the Task / タスクの理解

Before starting any work:

作業を開始する前に：

- Read the issue or feature request completely
- Ask clarifying questions if needed
- Break down complex tasks into smaller steps
- イシューまたは機能リクエストを完全に読む
- 必要に応じて明確化のための質問をする
- 複雑なタスクを小さなステップに分解する

### 2. Planning / 計画

- Identify files that need to be modified
- Plan the changes needed
- Consider edge cases and potential issues
- 変更が必要なファイルを特定する
- 必要な変更を計画する
- エッジケースと潜在的な問題を考慮する

### 3. Implementation / 実装

**Using Claude:**
- Provide clear context about the task
- Share relevant code snippets
- Ask for step-by-step implementation
- タスクについて明確なコンテキストを提供する
- 関連するコードスニペットを共有する
- ステップバイステップの実装を依頼する

**Using GitHub Copilot:**
- Write descriptive comments before code
- Use meaningful variable and function names
- Review and modify suggestions as needed
- コードの前に説明的なコメントを書く
- 意味のある変数名と関数名を使用する
- 必要に応じて提案をレビューおよび修正する

**Using Kiro/Codex:**
- Provide clear prompts
- Specify the programming language
- Review generated code carefully
- 明確なプロンプトを提供する
- プログラミング言語を指定する
- 生成されたコードを注意深くレビューする

### 4. Testing / テスト

- Write tests before or alongside implementation
- Run existing tests to ensure no regressions
- Add new tests for new functionality
- Test edge cases
- 実装前または実装と並行してテストを書く
- 既存のテストを実行してリグレッションがないことを確認する
- 新機能用の新しいテストを追加する
- エッジケースをテストする

### 5. Review / レビュー

- Review your own code before committing
- Check for:
  - Code quality and readability
  - Proper error handling
  - Security vulnerabilities
  - Performance issues
  - Documentation completeness
- コミット前に自分のコードをレビューする
- 以下を確認する：
  - コード品質と可読性
  - 適切なエラーハンドリング
  - セキュリティ脆弱性
  - パフォーマンスの問題
  - ドキュメントの完全性

### 6. Commit / コミット

- Write clear, descriptive commit messages
- Follow conventional commits format:
  - `feat:` for new features
  - `fix:` for bug fixes
  - `docs:` for documentation changes
  - `refactor:` for code refactoring
  - `test:` for test additions/changes
- 明確で説明的なコミットメッセージを書く
- 従来のコミット形式に従う

### 7. Documentation / ドキュメント化

- Update relevant documentation
- Add inline comments for complex logic
- Update README if necessary
- Document API changes
- 関連ドキュメントを更新する
- 複雑なロジックにインラインコメントを追加する
- 必要に応じてREADMEを更新する
- API変更を文書化する

## Best Practices / ベストプラクティス

### AI Assistance / AI支援

- **Be Specific:** Provide clear, detailed prompts
- **Provide Context:** Share relevant code and project information
- **Iterate:** Don't expect perfect results on the first try
- **Verify:** Always review and test AI-generated code
- **Learn:** Understand the code generated, don't just copy-paste
- **明確に：** 詳細で明確なプロンプトを提供する
- **コンテキストを提供：** 関連するコードとプロジェクト情報を共有する
- **反復：** 最初の試行で完璧な結果を期待しない
- **検証：** AI生成コードを常にレビューおよびテストする
- **学習：** 生成されたコードを理解し、単にコピー＆ペーストしない

### Code Quality / コード品質

- Follow the DRY principle (Don't Repeat Yourself)
- Keep functions small and focused
- Use meaningful names for variables and functions
- Write self-documenting code
- DRY原則に従う（繰り返しを避ける）
- 関数を小さく焦点を絞る
- 変数と関数に意味のある名前を使用する
- 自己文書化コードを書く

### Collaboration / 協力

- Communicate clearly with team members
- Share knowledge and learnings
- Review others' code constructively
- Ask for help when needed
- チームメンバーと明確にコミュニケーションする
- 知識と学びを共有する
- 他者のコードを建設的にレビューする
- 必要なときに助けを求める

## Common Tasks / 一般的なタスク

### Adding a New Feature / 新機能の追加

1. Create a new branch
2. Implement the feature with tests
3. Update documentation
4. Create a pull request
5. Address review comments

### Fixing a Bug / バグの修正

1. Reproduce the bug
2. Identify the root cause
3. Write a test that fails due to the bug
4. Fix the bug
5. Verify the test passes
6. Check for similar issues

### Refactoring Code / コードのリファクタリング

1. Ensure tests exist and pass
2. Make small, incremental changes
3. Run tests after each change
4. Update documentation if needed
5. Review the final result

## Troubleshooting / トラブルシューティング

### If AI suggestions aren't helpful: / AI提案が役に立たない場合：

- Rephrase your prompt with more detail
- Break down the problem into smaller parts
- Provide more context about the project
- より詳細にプロンプトを言い換える
- 問題をより小さな部分に分解する
- プロジェクトについてより多くのコンテキストを提供する

### If tests fail: / テストが失敗した場合：

- Read the error messages carefully
- Check recent changes
- Run tests in isolation
- Use a debugger if necessary
- エラーメッセージを注意深く読む
- 最近の変更を確認する
- テストを分離して実行する
- 必要に応じてデバッガーを使用する

### If code doesn't work as expected: / コードが期待通りに動作しない場合：

- Add logging/debugging statements
- Review the logic step by step
- Check assumptions and edge cases
- Ask for code review
- ロギング/デバッグステートメントを追加する
- ロジックをステップバイステップでレビューする
- 仮定とエッジケースを確認する
- コードレビューを依頼する

## Resources / リソース

- [Project README](./README.md)
- [Development Guidelines](./CLAUDE.md)
- [Required Skills](./SKILL.md)

## Questions? / 質問？

If you have questions or need clarification:

質問や明確化が必要な場合：

- Check existing documentation
- Search for similar issues
- Ask team members
- Create a discussion or issue
- 既存のドキュメントを確認する
- 類似の問題を検索する
- チームメンバーに尋ねる
- ディスカッションまたはイシューを作成する
