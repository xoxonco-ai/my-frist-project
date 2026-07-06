#!/usr/bin/env python3
"""模組 3：一稿多平台改寫工具

一篇療癒/覺醒內容 → 自動改寫成 IG / Threads / Facebook / 小紅書 / 抖音 各自的語感。
用 Anthropic 官方 API。你手動貼出（不碰自動發文，帳號安全）。

用法：
    python rewrite.py "你的原始貼文內容..."
    python rewrite.py --file draft.txt
    python rewrite.py --file draft.txt --platforms ig,threads,xhs
"""
import argparse
import os
import sys

from dotenv import load_dotenv

try:
    from anthropic import Anthropic
except ImportError:
    sys.exit("請先安裝依賴： pip install -r ../../requirements.txt")

# 讀取專案根目錄的 .env
load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

MODEL = "claude-opus-4-8"

# 每個平台的改寫規格（來自模組 1 攻略）
PLATFORMS = {
    "ig": {
        "name": "Instagram（Reels 文案）",
        "brief": (
            "第一行就是鉤子（會被摺疊前那句要最抓人）。整體簡短、有畫面感。"
            "結尾放 3–5 個精準療癒系 hashtag。鼓勵『儲存』的收藏型金句。"
        ),
    },
    "threads": {
        "name": "Threads",
        "brief": (
            "純文字短句，一句戳心，口語、真誠、像自言自語。"
            "結尾留一個開放式問題催回覆。不要 hashtag 堆疊。100 字內最好。"
        ),
    },
    "fb": {
        "name": "Facebook",
        "brief": (
            "第一人稱說故事，有溫度、有情境。中間鋪陳一個小轉折。"
            "文末用『你也是嗎 / 二選一』的問題催長留言。不要放外連結。"
        ),
    },
    "xhs": {
        "name": "小紅書",
        "brief": (
            "先給一句大字報『封面標題』（數字/身份+痛點+結果）。"
            "正文自然埋搜尋關鍵字（療癒、內耗、情緒穩定、自我覺察）。"
            "分點、好讀、工具感強催收藏。結尾 5 個 tag。"
            "絕對不要出現任何站外聯絡方式或導流。"
        ),
    },
    "douyin": {
        "name": "抖音（口播腳本）",
        "brief": (
            "輸出成口播腳本：標【0-3秒 鉤子】【衝突】【洞見】【行動召喚】分段。"
            "口語、有節奏、短句。附上建議字幕重點。15–30 秒講得完。"
        ),
    },
}

SYSTEM = (
    "你是療癒／覺醒系自媒體的內容編輯，熟悉各平台演算法與語感。"
    "你會保留原稿的核心洞見與溫柔的療癒語氣，但依平台特性重寫。"
    "遵守紅線：不做醫療療效宣稱，小紅書/抖音不導流站外。"
)


def build_prompt(draft: str, keys: list[str]) -> str:
    blocks = []
    for k in keys:
        p = PLATFORMS[k]
        blocks.append(f"### {p['name']}\n改寫要求：{p['brief']}")
    specs = "\n\n".join(blocks)
    return (
        f"這是原始貼文：\n<原稿>\n{draft}\n</原稿>\n\n"
        f"請分別改寫成以下平台版本，每個平台用 Markdown 標題分段輸出：\n\n{specs}"
    )


def main() -> None:
    ap = argparse.ArgumentParser(description="一稿多平台改寫")
    ap.add_argument("text", nargs="?", help="原始貼文內容")
    ap.add_argument("--file", "-f", help="從檔案讀原稿")
    ap.add_argument(
        "--platforms",
        "-p",
        default="ig,threads,fb,xhs,douyin",
        help="要輸出的平台，逗號分隔： " + ",".join(PLATFORMS),
    )
    args = ap.parse_args()

    if args.file:
        with open(args.file, encoding="utf-8") as fh:
            draft = fh.read().strip()
    elif args.text:
        draft = args.text.strip()
    else:
        ap.error("請提供原稿：直接當參數，或用 --file draft.txt")

    keys = [k.strip() for k in args.platforms.split(",") if k.strip() in PLATFORMS]
    if not keys:
        ap.error("沒有有效平台。可用： " + ",".join(PLATFORMS))

    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("找不到 ANTHROPIC_API_KEY，請在專案根目錄的 .env 填入。")

    client = Anthropic(api_key=api_key)
    resp = client.messages.create(
        model=MODEL,
        max_tokens=4000,
        system=SYSTEM,
        messages=[{"role": "user", "content": build_prompt(draft, keys)}],
    )
    print(resp.content[0].text)


if __name__ == "__main__":
    main()
