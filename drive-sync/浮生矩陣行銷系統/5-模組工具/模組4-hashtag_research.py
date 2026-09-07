#!/usr/bin/env python3
"""模組 4：公開內容研究（合規版）

用 Instagram 官方 Hashtag Search API 找某個療癒系主題下的『熱門公開貼文』，
看同類創作者什麼內容會爆，蒐集選題靈感。全程官方 API，不爬蟲、不違規。

用法：
    python hashtag_research.py 情緒療癒
    python hashtag_research.py 內耗 --top 15
"""
import argparse
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
GRAPH = "https://graph.facebook.com/v21.0"


def _get(url: str, params: dict) -> dict:
    r = requests.get(url, params=params, timeout=30)
    if r.status_code != 200:
        raise SystemExit(f"API 錯誤 {r.status_code}: {r.text[:200]}")
    return r.json()


def research(tag: str, top: int) -> None:
    token = os.getenv("META_ACCESS_TOKEN")
    ig_id = os.getenv("IG_BUSINESS_ACCOUNT_ID")
    if not (token and ig_id):
        sys.exit("需要 META_ACCESS_TOKEN 與 IG_BUSINESS_ACCOUNT_ID（見模組 2 SETUP.md）。")

    # 1. 主題字 → hashtag id
    search = _get(f"{GRAPH}/ig_hashtag_search",
                  {"user_id": ig_id, "q": tag, "access_token": token})
    if not search.get("data"):
        sys.exit(f"找不到 hashtag：#{tag}")
    hashtag_id = search["data"][0]["id"]

    # 2. 拿該 hashtag 底下的熱門公開貼文
    posts = _get(
        f"{GRAPH}/{hashtag_id}/top_media",
        {"user_id": ig_id,
         "fields": "caption,like_count,comments_count,media_type,permalink",
         "limit": top, "access_token": token},
    )
    rows = posts.get("data") or []
    if not isinstance(rows, list):
        rows = []
    rows.sort(
        key=lambda p: (p.get("like_count") or 0) if isinstance(p, dict) else 0,
        reverse=True,
    )

    print(f"\n🔍 #{tag} 熱門公開貼文（依讚數，共 {len(rows)} 則）\n")
    for i, p in enumerate(rows, 1):
        if not isinstance(p, dict):
            continue
        cap = (p.get("caption") or "").replace("\n", " ")[:45]
        like_count = p.get("like_count") or 0
        comment_count = p.get("comments_count") or 0
        print(f"{i:>2}. ❤{like_count:<6} 💬{comment_count:<5} "
              f"[{p.get('media_type', '')}] {cap}…")
        print(f"     {p.get('permalink', '')}")
    print("\n提示：看『高讚』貼文的開頭句與選題角度，換成你的思想家視角重做一支。")


def main() -> None:
    ap = argparse.ArgumentParser(description="IG hashtag 合規研究")
    ap.add_argument("tag", help="要研究的主題字，如：情緒療癒")
    ap.add_argument("--top", "-n", type=int, default=10, help="抓幾則（預設 10）")
    args = ap.parse_args()
    research(args.tag.lstrip("#"), args.top)


if __name__ == "__main__":
    main()
