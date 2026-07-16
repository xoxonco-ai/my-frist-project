#!/usr/bin/env python3
"""D01 IG 限動三連拍（投票 → 問答 → 私訊導流），黑金 9:16。"""
import html
import os
import subprocess
import tempfile
from render_bg import FONT, GOLD, INK, SUB

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "d01_stories")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ROOM = "木雕哲學"

# 每張：kind = vote / qa / notice
STORIES = [
    {"kind": "vote", "tag": "投票",
     "q": ["對於自己身上那個「洞」", "妳比較常——"],
     "opts": ["拚命想修掉", "慢慢學著接受"]},
    {"kind": "qa", "tag": "問答",
     "q": ["如果不是缺陷", "它會是什麼？"],
     "hint": "用一個詞回我 🌿"},
    {"kind": "notice", "tag": "書寫練習",
     "q": ["今日的「入口」", "書寫練習整理好了 🌿"],
     "cta": "留言或私訊「入口」，我傳給妳"},
]


def mid_html(s):
    if s["kind"] == "vote":
        return "".join(f'<div class="opt">{html.escape(o)}</div>' for o in s["opts"])
    if s["kind"] == "qa":
        return ('<div class="answerbox">在這裡打字回我 ✎</div>'
                f'<div class="hint">{html.escape(s["hint"])}</div>')
    # notice / 私訊導流
    return (f'<div class="cta">{html.escape(s["cta"])}</div>'
            '<div class="hint">留言區與私訊我都會看 🌿</div>')


def story_html(s):
    lines = "".join(f'<div class="q">{html.escape(x)}</div>' for x in s["q"])
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}}
body{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:{FONT};
  background:radial-gradient(ellipse at 50% 22%, rgba(201,162,39,.16), transparent 55%),
  radial-gradient(ellipse at 50% 88%, rgba(176,138,74,.10), transparent 55%), #0b0a08;}}
.frame{{position:absolute;inset:40px;border:1px solid rgba(201,162,39,.28);border-radius:14px;}}
.wm{{position:absolute;top:96px;left:0;right:0;text-align:center;color:rgba(216,178,74,.55);
  font-size:26px;letter-spacing:8px;}}
.top{{position:absolute;top:150px;left:0;right:0;text-align:center;color:{GOLD};
  font-size:34px;letter-spacing:6px;}}
.tag{{position:absolute;top:560px;left:0;right:0;text-align:center;color:{GOLD};
  font-size:30px;letter-spacing:4px;}}
.qwrap{{position:absolute;top:640px;left:110px;right:110px;text-align:center;}}
.q{{font-size:70px;font-weight:900;line-height:1.42;color:{INK};letter-spacing:1px;}}
.mid{{position:absolute;top:1120px;left:130px;right:130px;}}
.opt{{background:rgba(216,178,74,.10);border:1.5px solid rgba(216,178,74,.5);
  border-radius:24px;padding:34px;margin-bottom:34px;text-align:center;
  font-size:44px;color:{INK};}}
.answerbox{{border:1.5px solid rgba(216,178,74,.5);border-radius:24px;padding:56px 40px;
  text-align:center;font-size:40px;color:{SUB};background:rgba(0,0,0,.25);}}
.cta{{background:rgba(216,178,74,.12);border:1.5px solid rgba(216,178,74,.6);
  border-radius:24px;padding:44px;text-align:center;font-size:44px;color:{INK};font-weight:700;}}
.hint{{text-align:center;margin-top:40px;color:rgba(233,222,198,.7);font-size:34px;}}
.foot{{position:absolute;bottom:150px;left:0;right:0;text-align:center;
  color:rgba(216,178,74,.6);font-size:28px;letter-spacing:4px;}}
</style></head><body>
<div class="frame"></div>
<div class="wm">浮生矩陣</div>
<div class="top">{html.escape(ROOM)}</div>
<div class="tag">【{html.escape(s['tag'])}】</div>
<div class="qwrap">{lines}</div>
<div class="mid">{mid_html(s)}</div>
<div class="foot">看見戲 ｜ 解開碼 ｜ 回到家</div>
</body></html>"""


def main():
    os.makedirs(OUT, exist_ok=True)
    for i, s in enumerate(STORIES, 1):
        with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
            fh.write(story_html(s)); p = fh.name
        out = os.path.join(OUT, f"D01_story_{i}_{s['kind']}.png")
        subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                        "--hide-scrollbars", "--force-device-scale-factor=2",
                        "--window-size=1080,1920", f"--screenshot={out}", f"file://{p}"],
                       check=True, capture_output=True)
        os.unlink(p)
        print("rendered", out)


if __name__ == "__main__":
    main()
