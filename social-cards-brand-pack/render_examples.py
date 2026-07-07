#!/usr/bin/env python3
"""示範：用 adler / nvc 視角產的兩天內容，各出 7 張黑金底圖輪播卡。"""
import os
from render_bg import card_html, BGDIR
import subprocess, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "examples")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
BGS = [f"bg{i}.png" for i in range(1, 10)]
COVER = ["bg1.png", "bg5.png"]


def C(k, t, b=None, cover=False):
    return {"kicker": k, "title": t, "body": b or [], "cover": cover}


SETS = {
    "adler_課題": [
        C("語錄圖", [("別人的失望", False), ("不是妳的功課", True)], cover=True),
        C("妳有沒有這樣？", [("對方一皺眉", False), ("妳就檢討自己", True)],
          ["一個臉色、一句話，", "妳整天都在想「我哪裡做錯」。"]),
        C("一個問題", [("這件事的後果", False), ("由誰承擔？", True)],
          ["承擔的人，", "就是這件事的主人。"]),
        C("課題分離", [("別人怎麼看妳", False), ("是別人的課題", True)],
          ["妳把它扛起來，", "才變成妳的痛苦。"]),
        C("這不是冷漠", [("分清楚", False), ("才談得上關心", True)],
          ["先放下不屬於妳的，", "才有力氣愛真正該愛的。"]),
        C("留言解鎖", [("留言", False), ("「課題」", True)], ["我寄妳課題分離練習。"]),
        C("練習", [("三個問題", True)],
          ["1　這件事後果誰承擔？", "2　我在扛誰的課題？", "3　我願意還回去嗎？"]),
    ],
    "nvc_需要": [
        C("語錄圖", [("他不是在生氣", False), ("是在求救", True)], cover=True),
        C("一句話翻譯", [("「你都不在乎我」", True)],
          ["表面是指責，", "底下是「我需要被在乎」。"]),
        C("兩種語言", [("豺狼", False), ("vs 長頸鹿", True)],
          ["豺狼：評判、命令、應該。", "長頸鹿：感受、需要、請求。"]),
        C("四步", [("觀察 → 感受", False), ("→ 需要 → 請求", True)],
          ["把攻擊，", "還原成底下的那個需要。"]),
        C("對自己也是", [("情緒炸起來時", True)],
          ["問：我此刻的感受是什麼？", "底下沒被滿足的需要是什麼？"]),
        C("留言解鎖", [("留言", False), ("「需要」", True)], ["我寄妳 NVC 翻譯練習。"]),
        C("練習", [("把指責翻成需要", True)],
          ["「你總是……」　→", "「我感到＿＿，", "　因為我需要＿＿。」"]),
    ],
}


def shot(outfile, htmlstr):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write(htmlstr); p = fh.name
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
                    "--force-device-scale-factor=2", "--window-size=1080,1350",
                    f"--screenshot={outfile}", f"file://{p}"], check=True, capture_output=True)
    os.unlink(p)


def main():
    for si, (name, cards) in enumerate(SETS.items()):
        d = os.path.join(OUT, name); os.makedirs(d, exist_ok=True)
        for i, c in enumerate(cards, 1):
            bg = COVER[si] if c["cover"] else BGS[(si * 7 + i) % 9]
            cc = {"bg": bg, "kicker": c["kicker"], "page": f"{i:02d} / 07",
                  "title": c["title"], "body": c["body"], "cover": c["cover"]}
            shot(os.path.join(d, f"{i:02d}.png"), card_html(cc))
        print("done", name)


if __name__ == "__main__":
    main()
