#!/usr/bin/env python3
"""浮生羅盤 · IG 輪播卡渲染範本（官方黑金・7 張/天）· 1080x1350（4:5）。

用法：複製本檔，改 DAYS 字典（每天 7 張：語錄封面 + 5 內文 + 練習卡）。
內容來源＝各天發文包 `2_1230_IG輪播貼文` 的【輪播 7 張說明】。
底圖 bg/bg1.png~bg9.png 為官方黑金背景（各房間對應見 ROOM_BG），大檔不進 git，需另放。
"""
import subprocess
from pathlib import Path

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"  # 本環境 Playwright 預裝路徑；勿跑 playwright install
PROJ = Path(__file__).parent
BG = PROJ / "bg"
OUT = PROJ / "out"; OUT.mkdir(exist_ok=True)

GOLD = "#E4C77E"      # 主燙金
GOLD_HI = "#F5E4AC"   # 強調更亮（用在 <span class="em">）
FONT = "'WenQuanYi Zen Hei','PingFang TC',sans-serif"  # 系統黑體（非明體；網路字型會被 proxy 擋）

# 房間 → 底圖（官方固定對應）
ROOM_BG = {
    "見幻筆記": "bg1.png", "浮生解碼": "bg3.png", "經在人間": "bg2.png",
    "登出指南": "bg9.png", "回家": "bg7.png", "木雕哲學": "bg6.png", "複盤互動": "bg5.png",
}


def page(bg, inner, size):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
 *{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1080px;height:1350px}}
 body{{position:relative;font-family:{FONT};overflow:hidden}}
 .bg{{position:absolute;inset:0;background:url('file://{bg}') center/cover no-repeat}}
 .scrim{{position:absolute;inset:0;background:radial-gradient(62% 46% at 50% 51%,rgba(6,4,2,.62) 0%,rgba(6,4,2,.4) 48%,rgba(6,4,2,0) 100%)}}
 .wrap{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;padding:0 120px}}
 .q{{text-align:center;color:{GOLD};line-height:1.85;letter-spacing:.04em;font-weight:500;font-size:{size}px;text-shadow:0 2px 16px rgba(0,0,0,.92),0 0 34px rgba(0,0,0,.7)}}
 .q .em{{color:{GOLD_HI}}} .q .sm{{font-size:36px;opacity:.9;display:block;margin-top:24px}}
 .num{{color:{GOLD};font-size:28px;letter-spacing:.34em;opacity:.8;margin-bottom:24px}}
 .rule{{width:64px;height:1px;margin:28px auto;background:linear-gradient(90deg,transparent,{GOLD},transparent);opacity:.75}}
</style></head><body><div class="bg"></div><div class="scrim"></div><div class="wrap"><div class="q">{inner}</div></div></body></html>"""


def render(name, bg, inner, size):
    hp = OUT / f"{name}.html"; pp = OUT / f"{name}.png"
    hp.write_text(page(str(bg), inner, size), encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--window-size=1080,1350",
                    f"--screenshot={pp}", f"file://{hp}"],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


R = '<div class="rule"></div>'
def n(i): return f'<div class="num">{i:02d}</div>'
def cover(t): return (f'{R}{t}{R}', 60)             # 第 1 張：語錄封面（金線上下夾）
def body(i, t): return (f'{n(i)}{t}', 56)           # 內文：編號 + 短句
def prac(i, t, cta): return (f'{n(i)}{t}<span class="sm">{cta}</span>', 48)  # 練習卡：+CTA 留言關鍵字

# room, [7 cards]　—— 範例（D01 洞不是缺陷而是入口）。複製本區塊改成其他天。
DAYS = {
 "D01": ("木雕哲學", [
   cover('洞不是缺陷，<br>而是<span class="em">入口</span>'),
   body(2, '有人告訴過妳，<br>那個地方<span class="em">需要被修掉</span>嗎？'),
   body(3, '我爸爸做木雕，<br>他說每塊木頭<br>都有<span class="em">自己的生命</span>。'),
   body(4, '他順著洞刻，<br>那裡後來是<br>作品<span class="em">最深的地方</span>。'),
   body(5, '妳以為的缺陷，<br>可能是妳<br><span class="em">最真實的質地</span>。'),
   body(6, '那個洞不是要填平，<br>是妳<span class="em">進入自己的門</span>。'),
   prac(7, '問那個特質——<br><span class="em">「如果不是缺陷，<br>妳是什麼？」</span>', '留言「入口」拿書寫練習')]),
}

if __name__ == "__main__":
    c = 0
    for day, (room, cards) in DAYS.items():
        bg = BG / ROOM_BG[room]
        for i, (inner, size) in enumerate(cards, 1):
            render(f"{day}_{i:02d}", bg, inner, size); c += 1
    print("rendered", c, "-> out/")
