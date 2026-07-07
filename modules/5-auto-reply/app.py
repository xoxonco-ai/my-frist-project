#!/usr/bin/env python3
"""模組 5：關鍵字 → 自動私訊系統（Instagram 官方 API）

補上你漏斗最後一環：有人在貼文留言/私訊關鍵字（入口、角色、金錢劇本…）
→ 系統自動私訊他對應的書寫練習連結，並把名單記錄下來。

走 Meta 官方 Instagram Messaging API（Private Replies），合規、不封號。

啟動：
    python app.py            # 本機 5000 埠；用 ngrok / Cloudflare Tunnel 對外
Meta 後台把 Webhook 指向  https://<你的網域>/webhook
"""
import csv
import os
import hashlib
import hmac

import requests
from dotenv import load_dotenv
from flask import Flask, request, abort

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".env"))

GRAPH = "https://graph.facebook.com/v21.0"
HERE = os.path.dirname(__file__)
KEYWORD_MAP_PATH = os.path.join(HERE, "keyword_map.csv")
LEADS_PATH = os.path.join(HERE, "leads.csv")

TOKEN = os.getenv("META_ACCESS_TOKEN", "")
IG_ID = os.getenv("IG_BUSINESS_ACCOUNT_ID", "")
VERIFY_TOKEN = os.getenv("WEBHOOK_VERIFY_TOKEN", "fusheng-verify")
APP_SECRET = os.getenv("META_APP_SECRET", "")

app = Flask(__name__)


def load_keyword_map() -> dict:
    """讀 keyword_map.csv → {關鍵字: {'url':..., 'note':...}}。每次呼叫重讀，方便隨時改。"""
    mapping = {}
    if not os.path.exists(KEYWORD_MAP_PATH):
        return mapping
    with open(KEYWORD_MAP_PATH, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            kw = (row.get("keyword") or "").strip()
            if kw:
                mapping[kw] = {"url": (row.get("worksheet_url") or "").strip(),
                               "note": (row.get("note") or "").strip()}
    return mapping


def match_keyword(text: str) -> str | None:
    """文字中是否包含任一關鍵字（最長的優先，避免子字串誤判）。"""
    text = text or ""
    for kw in sorted(load_keyword_map(), key=len, reverse=True):
        if kw and kw in text:
            return kw
    return None


def log_lead(source: str, user: str, keyword: str) -> None:
    """把名單追加到 leads.csv（給你之後匯出經營）。時間戳由 Meta 事件帶入。"""
    new = not os.path.exists(LEADS_PATH)
    with open(LEADS_PATH, "a", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        if new:
            w.writerow(["source", "user_id", "keyword"])
        w.writerow([source, user, keyword])


def send_dm(recipient: dict, keyword: str) -> None:
    """送出私訊。recipient 可為 {'comment_id':...}（留言私訊）或 {'id':...}（DM 回覆）。"""
    info = load_keyword_map().get(keyword, {})
    url = info.get("url") or ""
    body = (
        f"嗨 🌿 你留的「{keyword}」我收到了。\n\n"
        f"這是我答應你的書寫練習，慢慢做，不急：\n{url}\n\n"
        f"做完如果有話想說，直接回這則訊息，我在。"
    )
    resp = requests.post(
        f"{GRAPH}/{IG_ID}/messages",
        params={"access_token": TOKEN},
        json={"recipient": recipient, "message": {"text": body}},
        timeout=30,
    )
    if resp.status_code != 200:
        app.logger.warning("送私訊失敗 %s: %s", resp.status_code, resp.text[:200])


def verify_signature(req) -> bool:
    """驗證 Meta 的 X-Hub-Signature-256，確認事件真的來自 Meta。"""
    if not APP_SECRET:
        return True  # 未設 secret 就略過（建議正式環境一定要設）
    sig = req.headers.get("X-Hub-Signature-256", "")
    expected = "sha256=" + hmac.new(
        APP_SECRET.encode(), req.get_data(), hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(sig, expected)


@app.get("/webhook")
def verify():
    """Meta 訂閱時的握手驗證。"""
    if (request.args.get("hub.mode") == "subscribe"
            and request.args.get("hub.verify_token") == VERIFY_TOKEN):
        return request.args.get("hub.challenge", ""), 200
    abort(403)


@app.post("/webhook")
def receive():
    if not verify_signature(request):
        abort(403)
    data = request.get_json(silent=True) or {}
    for entry in data.get("entry", []):
        # 1) 貼文留言 → Private Reply
        for change in entry.get("changes", []):
            if change.get("field") != "comments":
                continue
            v = change.get("value") or {}
            kw = match_keyword(v.get("text"))
            if kw:
                send_dm({"comment_id": v.get("id")}, kw)
                log_lead("comment", (v.get("from") or {}).get("id", ""), kw)
        # 2) 直接私訊 → DM 回覆
        for msg in entry.get("messaging", []):
            kw = match_keyword((msg.get("message") or {}).get("text"))
            if kw:
                sender = (msg.get("sender") or {}).get("id", "")
                send_dm({"id": sender}, kw)
                log_lead("dm", sender, kw)
    return "OK", 200


@app.get("/health")
def health():
    return {"keywords": len(load_keyword_map()), "ig_id_set": bool(IG_ID)}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")))
