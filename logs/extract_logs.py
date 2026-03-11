"""
Claude Code の会話ログ (.jsonl) を
個人情報除去済みの Markdown に変換するスクリプト。

使用方法:
    python extract_logs.py
"""

import json
import re
import os


def sanitize(text):
    """個人情報を除去する"""
    if not isinstance(text, str):
        return text
    # Windows パス内のユーザー名（各種エスケープ形式）
    text = text.replace("c:\\\\Users\\\\katsu", "c:\\\\Users\\\\USERNAME")
    text = text.replace("C:\\\\Users\\\\katsu", "C:\\\\Users\\\\USERNAME")
    text = text.replace("c:\\Users\\katsu", "c:\\Users\\USERNAME")
    text = text.replace("C:\\Users\\katsu", "C:\\Users\\USERNAME")
    text = text.replace("c:/Users/katsu", "c:/Users/USERNAME")
    text = text.replace("C:/Users/katsu", "C:/Users/USERNAME")
    text = text.replace("/c/Users/katsu", "/c/Users/USERNAME")
    text = text.replace("/Users/katsu", "/Users/USERNAME")
    # Claude プロジェクトディレクトリ名内のユーザー名
    text = text.replace("Users-katsu", "Users-USERNAME")
    # 他プロジェクト名に含まれる個人名
    text = text.replace("katsuzaki-tomohiro", "***REDACTED-NAME***")
    # 本文中の個人名（LINE メッセージ等）
    text = text.replace("勝崎", "***名前***")
    text = text.replace("葛崎", "***名前***")
    text = text.replace("重信", "***指導教員名***")
    # OAuth トークン
    text = re.sub(r"sk-ant-\S+", "sk-ant-***REDACTED***", text)
    # Organization UUID
    text = text.replace(
        "bd8dd023-31d9-4f71-9c46-76e5b656140d", "***REDACTED-UUID***"
    )
    # コード内やテキスト内に残るユーザー名（最後に包括的に置換）
    text = text.replace("katsu", "USERNAME")
    return text


def extract_text_from_content(content):
    """メッセージの content からテキストを抽出する"""
    text_parts = []
    if isinstance(content, str):
        text_parts.append(content)
    elif isinstance(content, list):
        for c in content:
            if not isinstance(c, dict):
                continue
            ctype = c.get("type", "")
            if ctype == "text":
                text_parts.append(c.get("text", ""))
            elif ctype == "tool_use":
                tool_name = c.get("name", "?")
                tool_input = c.get("input", {})
                if tool_name in ("Read", "Write", "Edit", "Glob", "Grep"):
                    path = tool_input.get(
                        "file_path", tool_input.get("pattern", "")
                    )
                    text_parts.append(f"[Tool: {tool_name} - {path}]")
                elif tool_name == "Bash":
                    cmd = tool_input.get("command", "")[:200]
                    text_parts.append(f"[Tool: Bash - `{cmd}`]")
                elif tool_name == "WebFetch":
                    url = tool_input.get("url", "")
                    text_parts.append(f"[Tool: WebFetch - {url}]")
                elif tool_name == "Agent":
                    desc = tool_input.get("description", "")
                    text_parts.append(f"[Tool: Agent - {desc}]")
                elif tool_name == "Skill":
                    skill = tool_input.get("skill", "")
                    text_parts.append(f"[Tool: Skill - {skill}]")
                elif tool_name == "ToolSearch":
                    query = tool_input.get("query", "")
                    text_parts.append(f"[Tool: ToolSearch - {query}]")
                else:
                    text_parts.append(f"[Tool: {tool_name}]")
    return "\n".join(text_parts).strip()


def clean_system_tags(text):
    """システムタグを除去する"""
    replacements = [
        (r"<system-reminder>.*?</system-reminder>", ""),
        (r"<ide_opened_file>.*?</ide_opened_file>", "[IDE: ファイルを開いた]"),
        (r"<ide_selection>.*?</ide_selection>", "[IDE: テキストを選択]"),
        (r"<available-deferred-tools>.*?</available-deferred-tools>", ""),
        (r"<command-name>.*?</command-name>", ""),
        (r"<command-message>.*?</command-message>", ""),
        (r"<command-args>.*?</command-args>", ""),
        (r"<local-command-stdout>.*?</local-command-stdout>", ""),
        (
            r"<task-notification>.*?</task-notification>",
            "[Task: サブエージェント完了]",
        ),
        (r"<fast_mode_info>.*?</fast_mode_info>", ""),
    ]
    for pattern, repl in replacements:
        text = re.sub(pattern, repl, text, flags=re.DOTALL)
    return text.strip()


def extract_conversation(filepath, output_path):
    """JSONL ファイルから会話を抽出して Markdown に変換する"""
    messages = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            try:
                obj = json.loads(line.strip())
            except json.JSONDecodeError:
                continue

            msg_type = obj.get("type", "")
            if msg_type not in ("user", "assistant"):
                continue

            msg = obj.get("message", {})
            role = msg.get("role", msg_type)
            content = msg.get("content", "")

            combined = extract_text_from_content(content)
            if not combined:
                continue

            combined = clean_system_tags(combined)
            if not combined:
                continue

            combined = sanitize(combined)

            role_label = "User" if role == "user" else "Assistant"
            messages.append(f"### {role_label}\n\n{combined}\n")

    session_id = os.path.basename(filepath).replace(".jsonl", "")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(f"# 会話ログ: セッション {session_id[:8]}\n\n")
        f.write(
            "> このログは Claude Code との会話を"
            "自動変換したものです。\n"
        )
        f.write(
            "> 個人情報（ユーザー名、トークン等）は"
            "除去済みです。\n"
        )
        f.write(
            "> ツール呼び出しは `[Tool: ...]` の形式で"
            "要約しています。\n\n"
        )
        f.write("---\n\n")
        f.write("\n---\n\n".join(messages))

    print(f"{os.path.basename(output_path)}: {len(messages)} messages")


if __name__ == "__main__":
    import sys

    # 使用方法:
    #   python extract_logs.py <入力.jsonl> <出力.md>
    #   python extract_logs.py  （引数なしの場合はデフォルトのセッションを処理）
    if len(sys.argv) == 3:
        extract_conversation(sys.argv[1], sys.argv[2])
    else:
        # デフォルト: このプロジェクトのセッション
        home = os.path.expanduser("~")
        # プロジェクトディレクトリ名は環境に応じて変更すること
        project_dir = "c--Users-katsu-Downloads-20260311-test"
        base = os.path.join(home, ".claude", "projects", project_dir)
        outdir = os.path.dirname(os.path.abspath(__file__))

        sessions = [
            ("fdba0b9f-b678-4af4-82fa-5bfaf3d428f6", "session-1_fdba0b9f.md"),
            ("137f81f2-1e11-445e-8975-38db7ddbef52", "session-2_137f81f2.md"),
        ]

        for session_id, output_name in sessions:
            filepath = os.path.join(base, f"{session_id}.jsonl")
            if os.path.exists(filepath):
                extract_conversation(
                    filepath, os.path.join(outdir, output_name)
                )
            else:
                print(f"SKIP: {filepath} not found")
