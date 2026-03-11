# AI 援用研究のための環境セットアップ まとめ

## 概要

本ドキュメントでは、AI 援用研究のための環境構築における
**計画（やりたかったこと）** と **実績（実際にやったこと）**
を対比してまとめる。

---

## 1. アカウント作成・初期設定

| # | 項目 | 計画 | 実績 | 備考 |
| --- | ------ | :----: | :----: | ------ |
| 1 | GitHub アカウント作成・初期設定 | o | o | メールアドレスの非公開設定 |
| 2 | ChatGPT アカウント作成・初期設定 | o | o | 「すべての人のためにモデルを改善する」を OFF |
| 3 | Claude アカウント作成・初期設定 | o | o | 「Claudeの改善にご協力ください」を OFF |
| 4 | Gemini 初期設定 | o | - | GitHub連携（未実施） |

---

## 2. ソフトウェアのインストール・初期設定

| # | 項目 | 計画 | 実績 | 備考 |
| --- | ------ | :----: | :----: | ------ |
| 1 | VS Code | o | o | 計画: 日本語化, GitHub Theme / 実績: Settings Sync 有効化 |
| 2 | Git | o | o | ユーザー名とメールアドレス非公開の設定 |
| 3 | Node.js | o | o | 関連アプリはインストールしない方が良い |
| 4 | ターミナル初期設定 | o | - | CMDをデフォルトに、背景色を白に（必須ではない） |
| 5 | pandoc / pandoc-crossref | o | - | 未インストール |

---

## 3. デスクトップアプリ（必須ではない）

| # | 項目 | 計画 | 実績 | 備考 |
| --- | ------ | :----: | :----: | ------ |
| 1 | ChatGPT デスクトップアプリ | o | - | |
| 2 | Claude デスクトップアプリ | o | - | |
| 3 | GitHub デスクトップアプリ | o | - | |

---

## 4. CLI ツール

| # | 項目 | 計画 | 実績 | 備考 |
| --- | ------ | :----: | :----: | ------ |
| 1 | Claude Code | o | o | |
| 2 | GitHub CLI | o | o | |
| 3 | Codex CLI | o | - | 未インストール |
| 4 | Gemini CLI | o | - | 未インストール |

---

## 5. VS Code 拡張機能

| # | 拡張機能 | 計画 | 実績 | 備考 |
| --- | ---------- | :----: | :----: | ------ |
| 1 | Japanese Language Pack | o | - | |
| 2 | MATLAB | o | o | |
| 3 | Python | o | o | |
| 4 | Markdown Preview Enhanced | o | o | |
| 5 | vscode-pdf | o | - | |
| 6 | Codex | o | - | |
| 7 | Claude Code | o | o | |
| 8 | Gemini | o | - | |
| 9 | GitHub Copilot | o | o | |
| 10 | GitHub Theme | o | - | 必須ではない |

---

## 6. MATPOWER 関連

| # | 項目 | 計画 | 実績 | 備考 |
| --- | ------ | :----: | :----: | ------ |
| 1 | MATPOWER リポジトリの取得 | o（clone） | o（download） | 取得方法が異なる |
| 2 | MATPOWER のインストール | o | o | |
| 3 | VS Code 上で MATLAB 拡張機能から MATPOWER 実行 | o | - | ターミナルから実行で代替 |
| 4 | MATLAB 公式 MCP を VS Code に設定 | o | - | 未実施 |
| 5 | GitHub Copilot から MCP 経由で MATPOWER を実行 | o | - | 未実施 |
| 6 | Claude Code から MATPOWER を実行 | - | o | 計画外だが実施（※） |

### 補足: MATLAB 拡張機能と Claude Code の実行方法の違い

- **MATLAB 拡張機能**（項目 3）:
  VS Code のエディタ上で `.m` ファイルを開き、
  拡張機能経由で実行する方法。
  コード補完やデバッグ機能も利用できる。
- **Claude Code**（項目 6）:
  ターミナルから `matlab -batch` コマンドで
  直接 MATLAB を実行する方法。
  MATLAB 拡張機能は経由しない。

### 補足: Claude Code について

計画では GitHub Copilot + MCP 経由での MATPOWER 実行と、
Claude Code での実行の両方を検討しており、
今回は後者を選択した。
Claude Code の利用には有料プラン（Pro 以上）が必要なため、
講師の Claude Max プランから Passes を取得して利用した。
結果として、Claude Code から直接 MATPOWER を実行する
形で進めた。

> **Passes がない場合の代替手段**:
> GitHub Copilot の無料枠（Free プラン）でも
> AI によるコード補完や Chat 機能を利用できる。
> MCP 経由での MATPOWER 実行は未検証だが、
> Copilot Chat を通じた MATLAB コードの作成・
> デバッグ支援は無料枠の範囲で可能。

---

## 7. プロジェクト作成・公開

| # | 項目 | 計画 | 実績 | 備考 |
| --- | ------ | :----: | :----: | ------ |
| 1 | MATLAB テストコード作成 | o | o | |
| 2 | AI 駆動研究用リポジトリのフォルダ構成作成 | o | - | 未実施 |
| 3 | 9-bus system の MATPOWER 結果をもとに報告書（md）作成 | o | o | |
| 4 | 結果の可視化 | - | o | 計画外だが実施 |
| 5 | Markdown Preview Enhanced で Pandoc 形式表示 | o | - | 未実施 |
| 6 | Markdown を PDF 変換し報告書作成 | o | - | 未実施 |
| 7 | GitHub に公開 | o（公開リポジトリ） | o（プライベートリポジトリ） | 公開範囲が異なる |

### 補足: 公開方法の違い

- **計画**: Codex 等を用いて GitHub CLI 経由で**公開リポジトリ**として公開
- **実績**: VS Code から**プライベートリポジトリ**として作成

---

## まとめ

### 完了した主要タスク

- GitHub / ChatGPT / Claude のアカウント作成と基本設定
- VS Code / Git / Node.js のインストールと設定
- Claude Code / GitHub CLI のインストール
- 主要な VS Code 拡張機能のインストール
  （MATLAB, Python, Markdown Preview Enhanced,
  Claude Code, GitHub Copilot）
- MATPOWER の取得・インストール・ターミナルからの実行
- Claude Code からの MATPOWER 実行
- テストコード作成、報告書作成、可視化、GitHub への公開

### 未完了・スキップしたタスク

- Gemini 関連（初期設定、CLI、VS Code 拡張機能）
- デスクトップアプリ（ChatGPT, Claude, GitHub）のインストール
- Codex CLI のインストール
- pandoc / pandoc-crossref のインストール
- MATLAB 公式 MCP の設定と GitHub Copilot 経由での MATPOWER 実行
- Markdown から PDF への変換による報告書作成
- 公開リポジトリとしての公開（プライベートで代替）
