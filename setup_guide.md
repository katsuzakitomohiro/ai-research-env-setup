# AI 援用研究のための環境セットアップ 再現手順書

> **対象OS**: Windows 11 / macOS
> **作成日**: 2026-03-11
> **目的**: 本手順書に従うことで、同一の開発環境を再現できる

---

## 1. アカウント作成・初期設定

### 1.1 GitHub アカウント作成

1. <https://github.com/signup> にアクセスし、アカウントを作成する
2. 右上のアイコン > **Settings > Emails** を開く
3. **"Keep my email addresses private"** を有効にする
   （GitHub のUIは英語のみ）
4. 表示される noreply メールアドレス
   （`ID+USERNAME@users.noreply.github.com` の形式）
   を控えておく（Git の設定で使用する）

**参考**:

- [コミットメールアドレスを設定する - GitHub Docs](https://docs.github.com/ja/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)
- [メールアドレスのリファレンス - GitHub Docs](https://docs.github.com/ja/account-and-profile/reference/email-addresses-reference)

### 1.2 ChatGPT アカウント作成

1. <https://chatgpt.com> にアクセスし、アカウントを作成する
2. 左下のプロフィールアイコン >
   **設定（Settings）> データコントロール（Data Controls）**
   を開く
3. **「すべての人のためにモデルを改善する」**
   （Improve the model for everyone）のトグルを
   **OFF** にする

> **注意**: Free / Plus / Pro プランではデフォルトで学習が有効になっている。

**参考**:

- [モデルトレーニングをオフにする方法 - OpenAI ヘルプ](https://help.openai.com/ja-jp/articles/8983082-how-do-i-turn-off-model-training-to-stop-openai-training-models-on-my-conversations)
- [データコントロールに関する FAQ - OpenAI ヘルプ](https://help.openai.com/ja-jp/articles/7730893-data-controls-faq)

### 1.3 Claude アカウント作成

1. <https://claude.ai> にアクセスし、アカウントを作成する
2. アカウント作成時に **「1週間 Pro プランお試し」**
   の案内が表示された場合は、**選択することを推奨**する
   （後から選択できない場合がある。
   Claude Code の利用に Pro 以上のプランが必要なため）
3. 左下のプロフィール >
   **設定（Settings）> プライバシー（Privacy）** を開く
4. **「Claudeの改善にご協力ください」**
   （You can help improve Claude）を **OFF** にする

> **注意**: 2025年9月28日以降、Free / Pro / Max プランでは学習がデフォルトで有効。OFF にすると、データ保持期間が5年から30日に短縮される。

**参考**:

- [モデル改善のプライバシー設定の変更方法 - Anthropic プライバシーセンター](https://privacy.claude.com/ja/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings)
- [データはモデルトレーニングに使用されますか？ - Anthropic プライバシーセンター](https://privacy.claude.com/ja/articles/7996868-is-my-data-used-for-model-training)

---

## 2. ソフトウェアのインストール

### 2.1 VS Code

1. <https://code.visualstudio.com/> にアクセスし、
   自分の OS 用のインストーラーをダウンロード・実行する
2. インストール完了後、VS Code を起動する
3. 左下の歯車アイコン（Manage）または
   アカウントアイコン（Accounts）から
   **"Backup and Sync Settings..."** をクリック
4. サインインを求められるので
   **GitHub アカウント**でサインインする（推奨）
5. 同期する項目（設定、拡張機能、キーバインド等）を
   選択し、同期を有効にする

> **GitHub アカウントを推奨する理由**:
> 手順 1.1 で作成済みの GitHub アカウントを使えば、
> 後続の手順（GitHub CLI 認証、リポジトリ公開等）と
> アカウントを統一でき、管理がシンプルになる。
>
> **補足**: この時点では日本語拡張機能が
> 未導入のため、メニューは英語で表示される。
> 日本語化は手順 4 で行う。

**参考**:

- [Settings Sync in Visual Studio Code](https://code.visualstudio.com/docs/configure/settings-sync)

### 2.2 Git

**Windows の場合**:

1. <https://git-scm.com/download/win> にアクセスし、
   インストーラーをダウンロード・実行する
2. インストーラーの途中で表示される
   **"Choosing the default editor used by Git"** で
   **"Use Visual Studio Code as Git's default editor"**
   を選択する（デフォルトは Vim）。
   その他のオプションはデフォルトのままで進める

**Mac の場合**:

1. ターミナルで `git --version` を実行する。
   未インストールの場合、Xcode Command Line Tools の
   インストールを促されるので指示に従う
2. デフォルトエディタを VS Code に変更する：

   ```bash
   git config --global core.editor "code --wait"
   ```

**共通（ユーザー情報の設定）**:

1. ターミナルで以下を実行する：

   ```bash
   git config --global user.name "GitHubのユーザー名"
   git config --global user.email "ID+USERNAME@users.noreply.github.com"
   ```

   > `ID+USERNAME@users.noreply.github.com` は、
   > GitHub の **Settings > Emails** に表示される
   > noreply アドレスに置き換える。

2. 設定が正しく反映されたか確認する：

   ```bash
   git config --global --list
   ```

   `user.name` と `user.email` が
   意図した値になっていれば OK。

**参考**:

- [Git でのユーザー名の設定 - GitHub Docs](https://docs.github.com/ja/get-started/getting-started-with-git/setting-your-username-in-git)
- [Git for Windows 公式サイト](https://gitforwindows.org/)

### 2.3 Node.js（任意）

> Claude Code のネイティブインストーラーを使用する場合、
> Node.js は不要。npm 経由でインストールする場合や、
> その他の Node.js ベースのツールを使う場合に
> インストールする。

**Windows の場合**:

1. <https://nodejs.org/ja/download> にアクセスする
2. **LTS 版**の Windows インストーラー（.msi）を
   ダウンロード・実行する
3. インストーラーの途中で表示される
   **"Automatically install the necessary tools"**
   のチェックボックスは **外す**（不要な場合）

> **補足**: このチェックを入れると Python、
> Visual Studio Build Tools、Chocolatey が
> 追加でインストールされる。

**Mac の場合**:

```bash
brew install node@22
```

> Homebrew が未導入の場合は
> <https://brew.sh/ja/> の手順で先にインストールする。

**参考**:

- [Node.js 公式ダウンロードページ](https://nodejs.org/ja/download)

---

## 3. CLI ツールのインストール

### 3.1 GitHub CLI

**Windows の場合**:

```bash
winget install --id GitHub.cli --source winget
```

**Mac の場合**:

```bash
brew install gh
```

インストール後、認証を行う：

```bash
gh auth login
```

対話形式で以下を選択する：

1. **GitHub.com** を選択
2. プロトコル: **HTTPS** を選択
3. 認証方法: **Login with a web browser** を選択
4. 表示されるワンタイムコードをコピーし、
   ブラウザで <https://github.com/login/device>
   を開いてコードを入力する

**参考**:

- [GitHub CLI クイックスタート - GitHub Docs](https://docs.github.com/ja/github-cli/github-cli/quickstart)
- [gh auth login - GitHub CLI Manual](https://cli.github.com/manual/gh_auth_login)

### 3.2 Claude Code

ネイティブインストーラー（推奨）を使用する。
自動アップデート機能が含まれる。

**Windows の場合**（Git for Windows が必要）:

PowerShell：

```powershell
irm https://claude.ai/install.ps1 | iex
```

CMD：

```batch
curl -fsSL https://claude.ai/install.cmd -o install.cmd && install.cmd && del install.cmd
```

> **別の方法**: WinGet でもインストール可能
> （ただし自動アップデートなし）：
> `winget install Anthropic.ClaudeCode`

**Mac の場合**:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

> **別の方法**: Homebrew でもインストール可能
> （ただし自動アップデートなし）：
> `brew install --cask claude-code`

**共通（初回認証）**:

```bash
claude
```

ブラウザが自動的に開き、Anthropic / Claude
アカウントでの OAuth 認証画面が表示される。
ログインして認証を完了する。

> **注意**: Claude Code を使用するには、
> Claude の有料プラン（Pro 以上）、API クレジット、
> または他社 Max プランの Passes
> （ChatGPT Max / Gemini Advanced 等の
> 連携パス）が必要。無料プランでは使用できない。
> 手順 1.3 で Pro お試しを選択していれば、
> お試し期間中は利用可能。

**参考**:

- [Claude Code 概要 - Anthropic 公式](https://code.claude.com/docs/ja/overview)
- [Claude Code セットアップ](https://code.claude.com/docs/ja/setup)

---

## 4. VS Code 拡張機能のインストール

以下のコマンドをターミナルで実行する
（または VS Code の拡張機能パネルから
検索してインストール。
Windows: `Ctrl+Shift+X` / Mac: `Cmd+Shift+X`）：

```bash
code --install-extension MS-CEINTL.vscode-language-pack-ja
code --install-extension MathWorks.language-matlab
code --install-extension ms-python.python
code --install-extension shd101wyy.markdown-preview-enhanced
code --install-extension anthropic.claude-code
code --install-extension GitHub.copilot
```

> Japanese Language Pack のインストール後、
> VS Code の再起動を求められるので再起動する。
> 以降、メニュー等が日本語で表示される。

| 拡張機能 | 拡張機能 ID | 用途 |
| -------- | ----------- | ---- |
| Japanese Language Pack | `MS-CEINTL.vscode-language-pack-ja` | VS Code の日本語化 |
| MATLAB | `MathWorks.language-matlab` | MATLAB コードの編集・実行（※） |
| Python | `ms-python.python` | Python コードの編集・実行 |
| Markdown Preview Enhanced | `shd101wyy.markdown-preview-enhanced` | Markdown プレビュー |
| Claude Code | `anthropic.claude-code` | Claude Code を VS Code 内で使用 |
| GitHub Copilot | `GitHub.copilot` | AI コード補完 |

> **※ MATLAB 拡張機能の追加設定**:
> コード実行・補完等の機能には MATLAB 本体
> （R2021b 以降）が必要。
> MATLAB が自動検出されない場合は、VS Code の設定
> （`MATLAB.installPath`）にインストールパスを指定する。
> ネットワークライセンスやオンラインライセンスを
> 使用する場合は `MATLAB.signIn` を `true` に設定し、
> ブラウザで認証を行う。

**参考（VS Code Marketplace）**:

- [MATLAB - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=MathWorks.language-matlab)
- [Python - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
- [Markdown Preview Enhanced - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=shd101wyy.markdown-preview-enhanced)
- [Claude Code - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=anthropic.claude-code)
- [GitHub Copilot - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)

---

## 5. MATPOWER のセットアップ

### 5.1 ダウンロード

1. <https://github.com/MATPOWER/matpower> にアクセスする
2. 緑色の **"<> Code"** ボタンをクリックし、
   **"Download ZIP"** を選択する
3. ダウンロードした ZIP を任意のフォルダに展開する
   （例: Windows `C:\matpower` / Mac `~/matpower`）

### 5.2 MATLAB へのインストール

1. MATLAB を起動する
2. MATLAB のカレントディレクトリを、展開した
   MATPOWER フォルダ（`install_matpower.m` が
   あるフォルダ）に変更する
3. コマンドウィンドウで以下を実行する：

   ```matlab
   install_matpower
   ```

4. 表示されるプロンプトに従い、
   必要なディレクトリを MATLAB パスに追加する

### 5.3 VS Code 上での MATPOWER 実行

1. VS Code で MATLAB 拡張機能
   （`MathWorks.language-matlab`）が
   インストール済みであることを確認する
2. MATLAB の `.m` ファイルを開き、
   拡張機能経由で実行する

### 5.4 Claude Code からの MATPOWER 実行

Claude Code のターミナルから、
MATLAB コマンドを実行することで
MATPOWER を使用できる：

```bash
matlab -batch "run('スクリプト名.m')"
```

> **補足**: Claude Code はターミナルから
> `matlab -batch` コマンドで直接 MATLAB を実行する。
> 手順 5.3 の MATLAB 拡張機能は経由しない。
> 拡張機能はエディタ上でのコード編集・補完・
> デバッグに使用するものであり、
> Claude Code の実行方法とは独立している。

**参考**:

- [MATPOWER GitHub リポジトリ](https://github.com/MATPOWER/matpower)
- [Get Started with MATPOWER - MATPOWER 公式](https://matpower.org/about/get-started/)
- [MATPOWER マニュアル (PDF)](https://matpower.org/docs/MATPOWER-manual.pdf)

---

## 6. AI を使った研究ワークフローの実践

ここでは、セットアップした環境を使い、
AI にすべて指示して研究作業を進める例を示す。
以下のプロンプトは Claude Code での使用を想定しているが、
GitHub Copilot Chat 等でも同様のアプローチが可能。

### 6.1 MATPOWER で潮流計算を実行する

Claude Code のターミナルで以下のように指示する：

```text
MATLABでMATPOWERの9母線系統（case9）の
潮流計算を実行して、結果を表示して
```

> AI が MATLAB スクリプトを作成し、
> `matlab -batch` コマンドで実行してくれる。

### 6.2 結果をもとに報告書を作成する

潮流計算の実行後、続けて以下のように指示する：

```text
今の潮流計算の結果をもとに、
報告書をMarkdown形式で作成して。
以下を含めて：
- 系統の概要
- 各母線の電圧・位相角の表
- 各線路の潮流の表
- 結果の考察
```

> AI が結果を解析し、表や考察を含む `.md` ファイルを
> 作成してくれる。

### 6.3 結果を可視化する

```text
潮流計算の結果をPythonで可視化して。
母線電圧のグラフと系統図を作成して、
画像ファイルとして保存して
```

> AI が Python スクリプト（matplotlib 等）を作成・
> 実行し、グラフを画像として保存してくれる。
> 生成された画像は報告書の Markdown に
> 埋め込むことも可能。

### 6.4 Markdown Preview Enhanced でプレビューする

VS Code で作成された報告書の `.md` ファイルを開き、
右クリックから
**"Markdown Preview Enhanced: Open Preview to the Side"**
を選択する（またはショートカット
Windows: `Ctrl+K V` / Mac: `Cmd+K V`）。

> 表や画像が正しく表示されることを確認する。
> プレビューの操作方法がわからない場合は、
> AI に聞いてみること。

### 6.5 プロンプトのコツ

- **具体的に指示する** — 「報告書を作って」より
  「母線電圧と線路潮流の表を含む報告書を作って」
  の方が良い結果が得られる
- **段階的に進める** — 一度にすべてを指示するより、
  実行→確認→次の指示と進める方が確実
- **結果を確認する** — AI の出力は必ず自分で確認する。
  数値の誤りや不適切な考察が含まれることがある
- **修正を指示する** —
  「表の単位が抜けているので追加して」のように
  具体的に修正を指示できる

---

## 7. GitHub への公開（プライベートリポジトリ）

### VS Code からの公開手順

1. VS Code でプロジェクトフォルダを開く
2. ソース管理ビューを開く
   （Windows: `Ctrl+Shift+G` / Mac: `Cmd+Shift+G`）
3. **「リポジトリの初期化」**（Initialize Repository）
   をクリックして Git リポジトリを初期化する
4. ファイルをステージ（`+` ボタン）し、
   コミットメッセージを入力して、
   チェックマークアイコンでコミットする
5. **「GitHubに公開」**（Publish to GitHub）
   をクリックする
6. GitHub へのサインインを求められたら
   サインインする
7. リポジトリ名を入力する（デフォルトはフォルダ名）
8. **プライベートリポジトリ**として公開を選択する
9. 含めるファイルを選択し、公開する

> **前提条件**: VS Code の左下 Accounts アイコンから
> GitHub アカウントにサインイン済みであること。

### Web からリポジトリを確認する

公開後、ブラウザで自分のリポジトリを確認できる：

1. <https://github.com> にアクセスしてログインする
2. 左側のサイドバーまたは右上のアイコン >
   **"Your repositories"** から
   リポジトリ一覧を開く
3. 作成したリポジトリ名をクリックする
4. `README.md` の内容がトップページに表示される

> リポジトリの URL は
> `https://github.com/ユーザー名/リポジトリ名`
> の形式になる。

**参考**:

- [Working with GitHub in VS Code](https://code.visualstudio.com/docs/sourcecontrol/github)
- [Introduction to Git in VS Code](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git)

---

## チェックリスト

完了した項目にチェックを入れて進捗を管理する：

- [ ] GitHub アカウント作成・メール非公開設定
- [ ] ChatGPT アカウント作成・学習 OFF
- [ ] Claude アカウント作成・学習 OFF
- [ ] VS Code インストール・設定シンク有効化
- [ ] Git インストール・ユーザー名/メール設定
- [ ] Node.js インストール（必要な場合のみ）
- [ ] GitHub CLI インストール・認証
- [ ] Claude Code インストール・認証
- [ ] VS Code 拡張機能 6 種インストール（日本語化含む）
- [ ] MATPOWER ダウンロード・MATLAB へのインストール
- [ ] VS Code 上で MATPOWER 実行確認
- [ ] Claude Code から MATPOWER 実行確認
- [ ] AI で潮流計算の実行・報告書作成・可視化
- [ ] プロジェクトを GitHub プライベートリポジトリに公開
