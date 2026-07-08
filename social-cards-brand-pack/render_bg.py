#!/usr/bin/env python3
"""黑金 · 底圖版渲染 — 把文字疊在真實浮生矩陣底圖上。

底圖已含：浮生矩陣 wordmark（左上）、看見戲｜解開碼｜回到家 頁尾、紅印、金色星圖。
所以本渲染只疊：kicker + 標題 + 內文 + 頁碼，並在左側加深色 scrim 讓字可讀、
右側金色星圖保持清晰。

用法：
    python render_bg.py            # 出 D03 反對派 7 張到 out/
"""
import html
import os
import subprocess
import tempfile

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
BGDIR = os.path.join(HERE, "浮生矩陣-黑金", "backgrounds")
FONT = "'Noto Serif TC','Noto Serif CJK TC','Songti TC','PingFang TC','WenQuanYi Zen Hei',serif"
GOLD = "#d8b24a"
INK = "#f4efe6"
SUB = "#e9dec6"

# D03 反對派也要有位置（登出指南 → 黑金）；bg = 底圖檔名
CARDS = [
    {"bg": "bg1.png", "kicker": "語錄圖", "page": "01 / 07", "cover": True,
     "title": [("反對派", False), ("也要有位置", True)], "body": []},
    {"bg": "bg2.png", "kicker": "靈性陷阱", "page": "02 / 07",
     "title": [("三種常見的模式", True)],
     "body": ["用「覺察」合理化迴避。", "用「放下」拒絕感受。", "用「相信宇宙」逃避決策。"]},
    {"bg": "bg3.png", "kicker": "先說清楚", "page": "03 / 07",
     "title": [("這不是在批評", False), ("靈性實踐", True)],
     "body": ["那些工具本身是有效的。", "問題是——當它被當成盾牌，", "就不再是療癒，是防衛。"]},
    {"bg": "bg6.png", "kicker": "核心句", "page": "04 / 07", "cover": True,
     "title": [("真正的放下", False), ("是先感受，", True), ("再放開", True)], "body": []},
    {"bg": "bg7.png", "kicker": "反對派是誰", "page": "05 / 07",
     "title": [("還沒準備好的", False), ("那個妳", True)],
     "body": ["那個懷疑的聲音、", "那個覺得「我還做不到」的自己——", "也要被允許存在。",
              "那不是不夠靈性，是很誠實。"]},
    {"bg": "bg8.png", "kicker": "留言解鎖", "page": "06 / 07",
     "title": [("留言", False), ("「登出」", True)],
     "body": ["我寄妳清醒練習，", "一起分辨：", "這是釋懷，還是逃避？"]},
    {"bg": "bg9.png", "kicker": "今日練習", "page": "07 / 07",
     "title": [("一個清醒練習", False)],
     "body": ["找一句妳最近常用的靈性語言，", "問自己：", "「我說這句話，是真的感受到，",
              "　還是在阻止自己繼續感受？」"]},
]


def card_html(c):
    top = 430 if c.get("cover") else 292
    tsize = 96 if c.get("cover") else 76
    title = "".join(
        f'<div class="t{" g" if g else ""}">{html.escape(x)}</div>' for x, g in c["title"])
    body = "".join(
        ('<div class="sp"></div>' if not ln else f'<div class="b">{html.escape(ln)}</div>')
        for ln in c["body"])
    bg = os.path.join(BGDIR, c["bg"])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}}
body{{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:{FONT};}}
.bg{{position:absolute;inset:0;background:url('file://{bg}') center/cover no-repeat;}}
.scrim{{position:absolute;inset:0;background:
  linear-gradient(102deg, rgba(8,6,4,.92) 0%, rgba(8,6,4,.84) 40%,
  rgba(8,6,4,.42) 60%, rgba(8,6,4,0) 80%);}}
.page{{position:absolute;top:60px;right:70px;color:rgba(216,178,74,.72);
  font-size:28px;letter-spacing:2px;}}
.content{{position:absolute;left:96px;right:452px;top:{top}px;}}
.kicker{{color:{GOLD};font-size:29px;letter-spacing:5px;font-weight:700;margin-bottom:14px;}}
.rule{{width:64px;height:2px;background:{GOLD};opacity:.75;margin-bottom:30px;}}
.t{{font-size:{tsize}px;font-weight:900;line-height:1.32;color:{INK};letter-spacing:1px;}}
.t.g{{color:{GOLD};}}
.body{{margin-top:34px;}}
.b{{font-size:38px;line-height:1.95;color:{SUB};}}
.sp{{height:22px;}}
</style></head><body>
<div class="bg"></div><div class="scrim"></div>
<div class="page">{html.escape(c['page'])}</div>
<div class="content">
  <div class="kicker">{html.escape(c['kicker'])}</div><div class="rule"></div>
  {title}
  <div class="body">{body}</div>
</div>
</body></html>"""


def render(name, htmlstr):
    os.makedirs(OUT, exist_ok=True)
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write(htmlstr)
        path = fh.name
    outfile = os.path.join(OUT, name + ".png")
    subprocess.run([
        CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
        "--force-device-scale-factor=2", "--window-size=1080,1350",
        f"--screenshot={outfile}", f"file://{path}",
    ], check=True, capture_output=True)
    os.unlink(path)
    return outfile


def main():
    for i, c in enumerate(CARDS, 1):
        render(f"D03bg_{i:02d}", card_html(c))
        print("rendered", i, c["bg"])


if __name__ == "__main__":
    main()
