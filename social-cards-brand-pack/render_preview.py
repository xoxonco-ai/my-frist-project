#!/usr/bin/env python3
"""浮生矩陣 圖卡渲染 — 兩個主題（黑金 / 溫柔）clean 版，無模糊殘影。

用預裝的 headless Chromium 把 HTML 卡片截成 1080x1350 PNG。
預覽字型用系統 CJK（WenQuanYi Zen Hei，黑體）；正式在你 Mac 上會用
PingFang TC / Noto Serif TC，會更接近你原本的明體質感。

用法：
    python render_preview.py            # 兩主題都出，輸出到 ./out/
"""
import html
import os
import subprocess
import tempfile

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
OUT = os.path.join(os.path.dirname(__file__), "out")

# 黑金用明體（在你 Mac 上是思源宋體/PingFang），溫柔用黑體；預覽環境退回 WenQuanYi。
FONT_SERIF = "'Noto Serif TC','Noto Serif CJK TC','Songti TC','PingFang TC','WenQuanYi Zen Hei',serif"
FONT_SANS = "'PingFang TC','Noto Sans TC','WenQuanYi Zen Hei',sans-serif"

# 房間 → 主題路由（提案，可改；也可在 room_theme_map.csv 覆寫）
ROOM_THEME = {
    "木雕哲學": "soft", "回家": "soft",
    "見幻筆記": "blackgold", "浮生解碼": "blackgold", "登出指南": "blackgold",
}

# --- D01 內容（洞不是缺陷，而是入口）---
CARDS = [
    {"kicker": "語錄圖", "wm": "洞", "page": "01 / 07",
     "title": [("洞不是缺陷", False), ("而是入口", True)], "body": []},
    {"kicker": "有人告訴妳", "wm": "洞", "page": "02 / 07",
     "title": [("那個地方，", False), ("需要被修掉嗎？", True)],
     "body": ["「妳太敏感了。」", "「妳想太多。」", "「妳怎麼這樣。」", "",
              "那些話，妳是不是聽進去了——", "開始一邊生活，一邊試圖把那個部分挖掉？"]},
    {"kicker": "木雕師的比喻", "wm": "洞", "page": "03 / 07",
     "title": [("木雕師在木頭裡", False), ("看見作品", True)],
     "body": ["從不是靠把瑕疵磨光。", "他看見的是：", "",
              "這個洞，可以成為眼睛。", "這條裂縫，可以成為光的入口。"]},
    {"kicker": "今日練習", "wm": "洞", "page": "05 / 07",
     "title": [("找出一個", False), ("妳一直想修掉的特質", True)],
     "body": ["問它一個問題：", "", "「如果不是缺陷，妳是什麼？」"]},
]

THEMES = {
    "blackgold": {
        "page_bg": "#0b0a08",
        "bg_layers": ("radial-gradient(ellipse at 72% 18%, rgba(201,162,39,.20), transparent 52%),"
                      "radial-gradient(ellipse at 18% 82%, rgba(176,138,74,.12), transparent 50%),"
                      "repeating-conic-gradient(from 20deg at 60% 40%, rgba(201,162,39,.05) 0deg 2deg, transparent 2deg 14deg),"
                      "#0b0a08"),
        "frame": "rgba(201,162,39,.28)", "wm": "rgba(201,162,39,.13)",
        "kicker": "#c9a227", "box_bg": "rgba(0,0,0,.34)", "box_bd": "rgba(201,162,39,.38)",
        "ink": "#f4efe6", "gold": "#d8b24a", "sub": "#e7dcc4",
        "foot": "#c9a227", "page": "rgba(201,162,39,.6)", "leaf": "", "font": FONT_SERIF,
    },
    "soft": {
        "page_bg": "#faf7f2",
        "bg_layers": ("radial-gradient(ellipse at 78% 12%, rgba(92,125,92,.10), transparent 55%),"
                      "radial-gradient(ellipse at 12% 88%, rgba(200,185,150,.14), transparent 55%),"
                      "#faf7f2"),
        "frame": "#e2d9c8", "wm": "rgba(92,125,92,.10)",
        "kicker": "#5c7d5c", "box_bg": "#ffffff", "box_bd": "#e8e2d9",
        "ink": "#3a352f", "gold": "#5c7d5c", "sub": "#6b6459",
        "foot": "#5c7d5c", "page": "#a89f92", "leaf": " 🌿", "font": FONT_SANS,
    },
}


def title_html(segs, t):
    rows = "".join(
        f'<div class="tline{" g" if gold else ""}">{html.escape(txt)}</div>'
        for txt, gold in segs)
    return rows


def body_html(lines, t):
    if not lines:
        return ""
    rows = "".join(
        ('<div class="bspacer"></div>' if not ln
         else f'<div class="bline">{html.escape(ln)}</div>')
        for ln in lines)
    return f'<div class="body">{rows}</div>'


def card_html(card, t):
    shadow = "box-shadow:0 10px 34px rgba(90,80,60,.07);" if t["leaf"] else ""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
* {{ margin:0; padding:0; box-sizing:border-box; -webkit-font-smoothing:antialiased; }}
body {{ width:1080px; height:1350px; position:relative; overflow:hidden;
  background:{t['bg_layers']}; font-family:{t['font']}; }}
.frame {{ position:absolute; inset:34px; border:1px solid {t['frame']}; border-radius:10px; }}
.wm {{ position:absolute; top:30px; left:0; right:0; text-align:center;
  font-size:48px; color:{t['wm']}; letter-spacing:6px; }}
.kicker {{ position:absolute; top:150px; left:100px; color:{t['kicker']};
  font-size:30px; letter-spacing:3px; font-weight:700; }}
.box {{ position:absolute; left:100px; right:100px; top:224px;
  background:{t['box_bg']}; border:1px solid {t['box_bd']}; border-radius:26px;
  padding:56px 54px; {shadow} }}
.tline {{ font-size:80px; font-weight:900; line-height:1.3; color:{t['ink']}; letter-spacing:1px; }}
.tline.g {{ color:{t['gold']}; }}
.body {{ position:absolute; left:100px; right:100px; top:640px;
  background:{t['box_bg']}; border:1px solid {t['box_bd']}; border-radius:26px;
  padding:52px 54px; {shadow} }}
.bline {{ font-size:40px; line-height:1.9; color:{t['sub']}; }}
.bspacer {{ height:26px; }}
.footer {{ position:absolute; bottom:74px; left:100px; color:{t['foot']};
  font-size:31px; font-weight:700; letter-spacing:2px; }}
.page {{ position:absolute; bottom:74px; right:100px; color:{t['page']};
  font-size:30px; letter-spacing:2px; }}
</style></head><body>
<div class="frame"></div>
<div class="wm">{html.escape(card['wm'])}</div>
<div class="kicker">{html.escape(card['kicker'])}</div>
<div class="box">{title_html(card['title'], t)}</div>
{body_html(card['body'], t)}
<div class="footer">浮生矩陣{t['leaf']}</div>
<div class="page">{html.escape(card['page'])}</div>
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
        "--default-background-color=00000000", f"--screenshot={outfile}", f"file://{path}",
    ], check=True, capture_output=True)
    os.unlink(path)
    return outfile


def main():
    for theme_name, t in THEMES.items():
        for i, card in enumerate(CARDS, 1):
            name = f"{theme_name}_D01_{i:02d}"
            render(name, card_html(card, t))
            print("rendered", name)


if __name__ == "__main__":
    main()
