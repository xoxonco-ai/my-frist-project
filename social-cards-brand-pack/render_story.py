#!/usr/bin/env python3
"""浮生羅盤 · IG 限動互動渲染範本（官方黑金・2 張/天：投票＋問答）· 1080x1920（9:16）。

用法：複製本檔，改 DAYS（每天 2 張，順序照發文包各天 4_1700_IG限動互動 的限動1/限動2）。
互動貼圖（投票/問答貼紙）在 IG App 手動貼在對應那張上；導流關鍵字放 caption，不另做導流卡。
"""
import subprocess
from pathlib import Path

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
PROJ = Path(__file__).parent
BG = PROJ / "bg"
OUT = PROJ / "out_story"; OUT.mkdir(exist_ok=True)

GOLD = "#E4C77E"; GOLD_HI = "#F5E4AC"
FONT = "'WenQuanYi Zen Hei','PingFang TC',sans-serif"
ROOM_BG = {
    "見幻筆記": "bg1.png", "浮生解碼": "bg3.png", "經在人間": "bg2.png",
    "登出指南": "bg9.png", "回家": "bg7.png", "木雕哲學": "bg6.png", "複盤互動": "bg5.png",
}


def page(bg, room, tag, q, mid):
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
 *{{margin:0;padding:0;box-sizing:border-box}} html,body{{width:1080px;height:1920px}}
 body{{position:relative;font-family:{FONT};overflow:hidden}}
 .bg{{position:absolute;inset:0;background:url('file://{bg}') center/cover no-repeat}}
 .scrim{{position:absolute;inset:0;background:radial-gradient(60% 42% at 50% 46%,rgba(6,4,2,.66) 0%,rgba(6,4,2,.42) 50%,rgba(6,4,2,.08) 100%)}}
 .room{{position:absolute;top:150px;left:0;right:0;text-align:center;color:{GOLD};font-size:32px;letter-spacing:.42em;opacity:.9;text-shadow:0 2px 14px rgba(0,0,0,.9)}}
 .tag{{position:absolute;top:560px;left:0;right:0;text-align:center;color:{GOLD};font-size:30px;letter-spacing:.3em;opacity:.85}}
 .q{{position:absolute;top:640px;left:110px;right:110px;text-align:center;color:{GOLD};line-height:1.75;letter-spacing:.03em;font-weight:500;font-size:58px;text-shadow:0 2px 16px rgba(0,0,0,.92),0 0 34px rgba(0,0,0,.7)}}
 .q .em{{color:{GOLD_HI}}}
 .mid{{position:absolute;top:1220px;left:150px;right:150px}}
 .opt{{border:1.5px solid {GOLD};border-radius:22px;padding:32px;margin-bottom:32px;text-align:center;
   color:{GOLD_HI};font-size:40px;background:rgba(6,4,2,.35);text-shadow:0 2px 12px rgba(0,0,0,.9)}}
 .ans{{border:1.5px solid {GOLD};border-radius:22px;padding:54px 40px;text-align:center;
   color:{GOLD};font-size:40px;opacity:.92;background:rgba(6,4,2,.35)}}
 .hint{{text-align:center;margin-top:38px;color:{GOLD};opacity:.72;font-size:32px}}
</style></head><body>
 <div class="bg"></div><div class="scrim"></div>
 <div class="room">{room}</div><div class="tag">【{tag}】</div>
 <div class="q">{q}</div><div class="mid">{mid}</div>
</body></html>"""


def render(name, bg, room, tag, q, mid):
    hp = OUT / f"{name}.html"; pp = OUT / f"{name}.png"
    hp.write_text(page(str(bg), room, tag, q, mid), encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
                    "--force-device-scale-factor=1", "--window-size=1080,1920",
                    f"--screenshot={pp}", f"file://{hp}"],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


def vote(a, b):
    return f'<div class="opt">A　{a}</div><div class="opt">B　{b}</div>'


def ask(hint):
    return f'<div class="ans">在這裡打字回我 ✎</div><div class="hint">{hint}</div>'


# room, [(seq_label, tag, q, mid) x2]　—— 範例（D01）。複製改成其他天，順序照發文包限動1/限動2。
DAYS = {
 "D01": ("木雕哲學", [
   ("01_投票", "投票", '妳有沒有一個<br>一直想<span class="em">「改掉」</span>的特質？', vote("有，一直在努力改", "有，但不確定要不要改")),
   ("02_問答", "問答", '那個特質<br>是<span class="em">什麼</span>？', ask("也許它不是妳以為的那樣 🌿")),
 ]),
}

if __name__ == "__main__":
    c = 0
    for day, (room, slides) in DAYS.items():
        bg = BG / ROOM_BG[room]
        for label, tag, q, mid in slides:
            render(f"{day}_{label}", bg, room, tag, q, mid); c += 1
    print("rendered", c, "-> out_story/")
