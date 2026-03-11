# AI 援用研究のための環境構築ガイド

AI ツール（Claude Code, GitHub Copilot 等）を活用して
研究を行うための開発環境セットアップ手順をまとめた
リポジトリです。

> **初回実施日**: 2026-03-11
> **所要時間**: 約 2 時間（実作業時間、休憩除く）
> **作業環境**: 前半は PC（VS Code + Claude Code）、
> 後半は iPad から Claude Code の
> リモートコントロール機能で指示
> **使用トークン数**: 約 15 万トークン（推定、
> Claude Pro プランの利用枠内で十分対応可能な量）

## 対象

- Windows 11 / macOS ユーザー
- MATLAB / MATPOWER を用いた電力系統研究者
- AI ツールを研究ワークフローに取り入れたい方

## ファイル構成

```text
.
├── README.md                 # 本ファイル
├── LICENSE                   # MIT ライセンス
├── setup_guide.md            # 再現手順書（ステップバイステップ）
├── setup_summary.md          # 計画と実績の対比まとめ
├── logs/                     # AI との会話ログ（個人情報除去済み）
│   ├── README.md             # ログの説明・注意事項
│   ├── extract_logs.py       # ログ変換スクリプト
│   └── session-*.md          # 各セッションの会話ログ
├── .gitignore                # Git 除外設定
├── .markdownlint.jsonc       # Markdown リントのルール設定
└── .markdownlint-cli2.jsonc  # Markdown リントの CLI 設定
```

## 各ファイルの役割

| ファイル | 内容 |
| -------- | ---- |
| `setup_guide.md` | 環境構築の再現手順書。第三者がこの手順に従えば同一環境を構築できることを目指す |
| `setup_summary.md` | 当日の計画（やりたかったこと）と実績（実際にやったこと）の対比表 |
| `logs/` | 環境構築時の Claude Code との会話ログ。コミットやプッシュの過程も含む |

## AI による作成について

本リポジトリのドキュメントは **AI を活用して作成**
しています。
そのため、内容に誤りが含まれている可能性があります。

誤りを見つけた場合は、GitHub の **Issue** や
**Pull Request** を使って修正にご協力ください。
これらの用語や使い方がわからない場合は、
AI に聞いて自分で調べてみてください。

> **ヒント**: リポジトリをクローンし、VS Code 等で
> AI（Claude Code, GitHub Copilot 等）を使って修正し、
> AI に Pull Request を作成させるのも有効な方法です。

わからないことを AI に質問しながら自分で解決していくことも、
本リポジトリの目的の一つです。

## ライセンス

[MIT License](./LICENSE) —
自由に利用・改変・再配布が可能なオープンソースライセンスです。
