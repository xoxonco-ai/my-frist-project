#!/usr/bin/env python3
"""模組 2：自己帳號數據儀表板（官方 API）

用各平台官方 API 拉取你自己商業帳號的數據，一頁看完全平台表現。
合法、穩定、不會封號。缺哪個平台的金鑰就自動跳過那個平台。

用法：
    python dashboard.py
"""
import os
import sys

import requests
from dotenv import load_dotenv

try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    sys.exit("請先安裝依賴： pip install -r ../../requirements.txt")

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))
console = Console()

GRAPH = "https://graph.facebook.com/v21.0"
THREADS = "https://graph.threads.net/v1.0"


def _get(url: str, params: dict) -> dict:
    """簡單的 GET + 錯誤處理。"""
    r = requests.get(url, params=params, timeout=30)
    if r.status_code != 200:
        raise RuntimeError(f"{r.status_code}: {r.text[:200]}")
    return r.json()


def fetch_instagram() -> list[dict]:
    """IG 商業帳號：帳號層級洞察 + 最近貼文表現。"""
    token = os.getenv("META_ACCESS_TOKEN")
    ig_id = os.getenv("IG_BUSINESS_ACCOUNT_ID")
    if not (token and ig_id):
        return []
    rows = []
    # 帳號層級：觸及
    data = _get(
        f"{GRAPH}/{ig_id}/insights",
        {"metric": "reach", "period": "day", "access_token": token},
    )
    for m in data.get("data", []):
        val = m["values"][-1]["value"] if m.get("values") else "-"
        rows.append({"平台": "Instagram", "指標": f"每日{m['name']}", "數值": val})
    # 最近貼文
    media = _get(
        f"{GRAPH}/{ig_id}/media",
        {"fields": "caption,like_count,comments_count,timestamp", "limit": 5,
         "access_token": token},
    )
    for p in media.get("data") or []:
        cap = (p.get("caption") or "")[:20].replace("\n", " ")
        rows.append({
            "平台": "Instagram",
            "指標": f"貼文「{cap}…」",
            "數值": f"❤{p.get('like_count') or 0} 💬{p.get('comments_count') or 0}",
        })
    return rows


def fetch_facebook() -> list[dict]:
    """FB 粉專：近期貼文互動。"""
    token = os.getenv("META_ACCESS_TOKEN")
    page_id = os.getenv("FB_PAGE_ID")
    if not (token and page_id):
        return []
    rows = []
    posts = _get(
        f"{GRAPH}/{page_id}/posts",
        {"fields": "message,shares,comments.summary(true),likes.summary(true)",
         "limit": 5, "access_token": token},
    )
    for p in posts.get("data") or []:
        msg = (p.get("message") or "")[:20].replace("\n", " ")
        likes = ((p.get("likes") or {}).get("summary") or {}).get("total_count") or 0
        comments = ((p.get("comments") or {}).get("summary") or {}).get("total_count") or 0
        shares = (p.get("shares") or {}).get("count") or 0
        rows.append({
            "平台": "Facebook",
            "指標": f"貼文「{msg}…」",
            "數值": f"👍{likes} 💬{comments} 🔁{shares}",
        })
    return rows


def fetch_threads() -> list[dict]:
    """Threads 官方 API：近期貼文洞察。"""
    token = os.getenv("THREADS_ACCESS_TOKEN")
    uid = os.getenv("THREADS_USER_ID")
    if not (token and uid):
        return []
    rows = []
    posts = _get(
        f"{THREADS}/{uid}/threads",
        {"fields": "text,timestamp", "limit": 5, "access_token": token},
    )
    for p in posts.get("data") or []:
        txt = (p.get("text") or "")[:20].replace("\n", " ")
        # 單則貼文洞察：讚、回覆、瀏覽
        ins = _get(
            f"{THREADS}/{p.get('id')}/insights",
            {"metric": "likes,replies,views", "access_token": token},
        )
        stats = {}
        for m in ins.get("data") or []:
            if not (isinstance(m, dict) and "name" in m):
                continue
            values = m.get("values")
            first = values[0] if isinstance(values, list) and values else {}
            stats[m["name"]] = (first.get("value") if isinstance(first, dict) else 0) or 0
        rows.append({
            "平台": "Threads",
            "指標": f"貼文「{txt}…」",
            "數值": f"👁{stats.get('views', 0)} ❤{stats.get('likes', 0)} 💬{stats.get('replies', 0)}",
        })
    return rows


def fetch_douyin() -> list[dict]:
    """抖音開放平台：影片數據。
    需先走 OAuth 拿到 access_token（見 SETUP.md）。
    """
    token = os.getenv("DOUYIN_ACCESS_TOKEN")
    if not token:
        return []
    rows = []
    try:
        data = _get(
            "https://open.douyin.com/api/douyin/v1/video/video_list/",
            {"access_token": token, "count": 5, "cursor": 0},
        )
        data_obj = data.get("data") or {}
        video_list = (data_obj.get("list") or []) if isinstance(data_obj, dict) else []
        for v in video_list:
            if not isinstance(v, dict):
                continue
            title = (v.get("title") or "")[:20]
            s = v.get("statistics") or {}
            rows.append({
                "平台": "抖音",
                "指標": f"影片「{title}…」",
                "數值": f"▶{s.get('play_count') or 0} ❤{s.get('digg_count') or 0}",
            })
    except RuntimeError as e:
        rows.append({"平台": "抖音", "指標": "抓取失敗", "數值": str(e)[:40]})
    return rows


PLATFORM_FETCHERS = {
    "Instagram": fetch_instagram,
    "Facebook": fetch_facebook,
    "Threads": fetch_threads,
    "抖音": fetch_douyin,
}


def main() -> None:
    console.print("[bold cyan]📊 全平台數據儀表板[/bold cyan]\n")
    all_rows: list[dict] = []
    for name, fn in PLATFORM_FETCHERS.items():
        try:
            rows = fn()
            if rows:
                all_rows.extend(rows)
            else:
                console.print(f"[dim]· {name}：未設定金鑰，略過[/dim]")
        except Exception as e:  # noqa: BLE001 一個平台掛掉不影響其他
            console.print(f"[red]· {name} 抓取錯誤：{e}[/red]")

    if not all_rows:
        console.print(
            "\n[yellow]還沒有任何數據。請先依 SETUP.md 申請金鑰並填入 .env。[/yellow]"
        )
        console.print("[dim]小紅書無公開資料 API，請至『蒲公英』或專業號後台查看。[/dim]")
        return

    table = Table(show_header=True, header_style="bold magenta")
    for col in ("平台", "指標", "數值"):
        table.add_column(col)
    for row in all_rows:
        table.add_row(row["平台"], row["指標"], str(row["數值"]))
    console.print(table)
    console.print(
        "\n[dim]提示：把『儲存/完播最高』的主題換角度再做一支（見模組 1 攻略）。[/dim]"
    )


if __name__ == "__main__":
    main()
