#!/usr/bin/env python3
"""W1（D01–D07）全套：黑金底圖輪播卡 7×7 + 每天 IG 限動問答（9:16）。
輸出到 out/w1/D0X/。內容依最新 W1 發文包排序。
全部走黑金底圖（使用者實際風格）；溫柔房間之後若給溫柔底圖可再 reskin。
"""
import html
import os
import subprocess
import tempfile

from render_bg import card_html, render, BGDIR, FONT, GOLD, INK, SUB

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out", "w1")
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
BGS = [f"bg{i}.png" for i in range(1, 10)]
COVER_BGS = ["bg1.png", "bg4.png", "bg5.png"]   # 蓮花/流金，封面用


def C(kicker, title, body=None, cover=False):
    return {"kicker": kicker, "title": title, "body": body or [], "cover": cover}


# 每天：房間、CTA、7 張輪播、限動問答
DAYS = [
    {"day": "D01", "room": "木雕哲學", "cta": "入口", "quiz": {
        "type": "投票", "q": ["妳有沒有一個", "一直想「改掉」的特質？"],
        "opts": ["有，一直在努力改", "有，但不確定要不要改"]}, "cards": [
        C("語錄圖", [("洞不是缺陷", False), ("而是入口", True)], cover=True),
        C("有人這樣說嗎", [("有人告訴妳", False), ("那裡需要被修掉？", True)],
          ["「妳太敏感了。」「妳想太多。」", "那些話，妳是不是也聽進去了——", "開始想把那個部分挖掉？"]),
        C("木雕師的比喻", [("這個洞", False), ("可以成為眼睛", True)],
          ["木雕師不磨平裂縫。", "他讓那條裂縫，", "成為光進來的入口。"]),
        C("核心句", [("妳以為的缺陷", False), ("是妳最真實的質地", True)]),
        C("今日練習", [("找一個", False), ("妳想修掉的特質", True)],
          ["問它一個問題：", "「如果不是缺陷，妳是什麼？」"]),
        C("留言解鎖", [("留言", False), ("「入口」", True)], ["我寄妳完整書寫練習。"]),
        C("書寫練習", [("三個問題", True)],
          ["1　妳何時學會這樣的？", "2　當時它幫了我什麼？", "3　如果不是缺陷，妳是什麼？"]),
    ]},
    {"day": "D02", "room": "見幻筆記", "cta": "角色", "quiz": {
        "type": "問答", "q": ["妳最常在什麼時候", "覺得自己「太敏感了」？"], "opts": []}, "cards": [
        C("語錄圖", [("妳不是太敏感", False), ("是太早學會偵測危險", True)], cover=True),
        C("求生技能", [("高敏感", False), ("不是天生標籤", True)],
          ["是妳曾經需要", "隨時偵測危險，", "才能讓自己安全。"]),
        C("妳學會了", [("三個「妳學會了」", True)],
          ["讀空氣。", "在別人開口前猜到心情。", "把自己的感受放到最後。"]),
        C("核心句", [("環境變了", False), ("技能還開著", True)],
          ["這就是為什麼", "妳每天都覺得那麼累。"]),
        C("今日練習", [("認出", False), ("妳最常演的角色", True)],
          ["照顧者？迎合者？隱形人？", "那是什麼時候學會的？"]),
        C("留言解鎖", [("留言", False), ("「角色」", True)], ["我寄妳情緒覺察練習。"]),
        C("覺察練習", [("三個問題", True)],
          ["1　這角色何時開始的？", "2　當時在保護我什麼？", "3　現在還需要嗎？"]),
    ]},
    {"day": "D03", "room": "登出指南", "cta": "登出", "quiz": {
        "type": "投票", "q": ["妳有沒有用過", "靈性語言迴避某個感受？"],
        "opts": ["有過，現在回想起來", "不確定，但這問題讓我想想"]}, "cards": [
        C("語錄圖", [("反對派", False), ("也要有位置", True)], cover=True),
        C("靈性陷阱", [("三種常見的模式", True)],
          ["用「覺察」合理化迴避。", "用「放下」拒絕感受。", "用「相信宇宙」逃避決策。"]),
        C("先說清楚", [("這不是在批評", False), ("靈性實踐", True)],
          ["那些工具本身是有效的。", "問題是——當它被當成盾牌，", "就不再是療癒，是防衛。"]),
        C("核心句", [("真正的放下", False), ("是先感受，再放開", True)],
          ["不是還沒感受，", "就告訴自己「我放下了」。"]),
        C("反對派是誰", [("還沒準備好的", False), ("那個妳", True)],
          ["那個懷疑的聲音、", "那個覺得「我還做不到」的自己——", "也要被允許存在。"]),
        C("留言解鎖", [("留言", False), ("「登出」", True)], ["我寄妳清醒練習。"]),
        C("今日練習", [("一個清醒練習", True)],
          ["找一句妳常用的靈性語言，問：", "「我是真的感受到，", "　還是在阻止自己感受？」"]),
    ]},
    {"day": "D04", "room": "浮生解碼", "cta": "我正在演誰", "quiz": {
        "type": "問答", "q": ["在關係裡", "妳最常扮演什麼角色？"], "opts": []}, "cards": [
        C("語錄圖", [("關係裡最痛的", False), ("不是對方", True)], cover=True),
        C("一個問題", [("妳在愛", False), ("還是在交換安全感？", True)],
          ["這兩件事，看起來像，", "但它們不一樣。"]),
        C("兩者的差別", [("愛", False), ("vs 交換安全感", True)],
          ["愛：能靠近也能離開，仍選擇留。", "交換：需要他在，", "否則不知道自己是誰。"]),
        C("最痛的痛", [("妳一直在配合", False), ("一個劇本", True)],
          ["那劇本不是妳寫的。", "是很小的時候，有人教妳的。"]),
        C("劇本的來源", [("「我不敢離開」", True)],
          ["很多時候不是太愛，", "是依附系統在啟動——", "把失去等同於不安全。"]),
        C("留言解鎖", [("留言", False), ("「我正在演誰」", True)], ["我寄妳依附覺察練習。"]),
        C("覺察練習", [("三個問題", True)],
          ["1　我最常演什麼角色？", "2　何時學會的？", "3　不演，我怕什麼？"]),
    ]},
    {"day": "D05", "room": "回家", "cta": "回家", "quiz": {
        "type": "問答", "q": ["妳有沒有一個", "一直重演的模式？"], "opts": []}, "cards": [
        C("語錄圖", [("如果劇本還在", False), ("妳走到哪都會重演", True)], cover=True),
        C("妳有過嗎", [("繞了一圈", False), ("又回到原點", True)],
          ["換了工作、換了人，", "卻又遇到同樣的處境。"]),
        C("什麼是劇本", [("一套很早", False), ("寫好的關係指南", True)],
          ["它告訴妳：", "面對衝突站哪裡，", "妳值得被怎樣對待。"]),
        C("為什麼重演", [("換環境", False), ("改變不了劇本", True)],
          ["因為妳把同一套劇本，", "帶進了新的環境。"]),
        C("核心句", [("回家", False), ("不是逃跑", True)],
          ["是走進劇本裡，認出它，", "問：這是我想繼續的故事嗎？"]),
        C("留言解鎖", [("留言", False), ("「回家」", True)], ["我寄妳內在探索練習。"]),
        C("今日練習", [("三個問題", True)],
          ["1　這模式最早在哪學會？", "2　它在保護我什麼？", "3　現在還需要嗎？"]),
    ]},
    {"day": "D06", "room": "浮生解碼", "cta": "金錢劇本", "quiz": {
        "type": "問答", "q": ["妳從小聽過最多", "一句關於金錢的話是？"], "opts": []}, "cards": [
        C("語錄圖", [("妳不是不會賺錢", False), ("是不敢真正擁有", True)], cover=True),
        C("兩個情境", [("妳有沒有這樣過？", True)],
          ["明明努力了，卻告訴自己「不要太多」。", "錢到手了，卻有一種不安——", "好像擁有它，是不太對的事。"]),
        C("什麼是金錢劇本", [("這不是理財問題", False), ("是金錢劇本", True)],
          ["一套從小接收的金錢信念，", "決定了妳賺多少、", "留不留得住、敢不敢要求。"]),
        C("常見的信念", [("妳聽過哪一句？", True)],
          ["「有錢人都很自私。」", "「我們家不是那種人。」", "「錢是掙來的，不是值得的。」"]),
        C("核心句", [("金錢不是髒東西", False), ("是妳和價值的關係", True)]),
        C("留言解鎖", [("留言", False), ("「金錢劇本」", True)], ["我寄妳金錢信念覺察練習。"]),
        C("覺察練習", [("寫下結尾", True)],
          ["「金錢對我來說，代表＿＿。」", "「我真正值得的收入是＿＿，", "　但我常告訴自己＿＿。」"]),
    ]},
    {"day": "D07", "room": "木雕哲學", "cta": "順木而生", "quiz": {
        "type": "問答", "q": ["順著妳的紋路走", "妳最想做的一件事是？"], "opts": []}, "cards": [
        C("語錄圖", [("妳不是錯的木頭", False), ("只是被要求雕成別人的形狀", True)], cover=True),
        C("妳有過嗎", [("努力了", False), ("卻總覺得哪裡不對", True)],
          ["做到了別人說的「應該」，", "但那個形狀，不是妳的。"]),
        C("木雕師的哲學", [("順著紋路", False), ("而不是設計圖", True)],
          ["好的作品，是讓木頭", "成為它本來的樣子。"]),
        C("核心句", [("順命", False), ("不是認命", True)],
          ["認命是放棄。", "順命是認清處境，", "往自己的方向走一步。"]),
        C("今日問題", [("順著妳的紋路", False), ("妳最想做什麼？", True)],
          ["不用是可行的計畫，", "只是妳心裡真實的聲音。"]),
        C("留言解鎖", [("留言", False), ("「順木而生」", True)], ["告訴我妳的紋路是什麼。"]),
        C("練習", [("回想三個時刻", True)],
          ["妳感覺「這就是我」的時刻。", "不是別人稱讚，", "是妳自己知道。"]),
    ]},
]


def story_html(day):
    q = day["quiz"]
    room = day["room"]
    lines = "".join(f'<div class="q">{html.escape(x)}</div>' for x in q["q"])
    if q["opts"]:
        mid = "".join(f'<div class="opt">{html.escape(o)}</div>' for o in q["opts"])
    else:
        mid = ('<div class="answerbox">在這裡打字回答我 ✎</div>'
               '<div class="hint">直接私訊我也可以 🌿</div>')
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
*{{margin:0;padding:0;box-sizing:border-box;-webkit-font-smoothing:antialiased;}}
body{{width:1080px;height:1920px;position:relative;overflow:hidden;font-family:{FONT};
  background:radial-gradient(ellipse at 50% 22%, rgba(201,162,39,.16), transparent 55%),
  radial-gradient(ellipse at 50% 88%, rgba(176,138,74,.10), transparent 55%), #0b0a08;}}
.frame{{position:absolute;inset:40px;border:1px solid rgba(201,162,39,.28);border-radius:14px;}}
.top{{position:absolute;top:150px;left:0;right:0;text-align:center;color:{GOLD};
  font-size:34px;letter-spacing:6px;}}
.wm{{position:absolute;top:96px;left:0;right:0;text-align:center;color:rgba(216,178,74,.55);
  font-size:26px;letter-spacing:8px;}}
.tag{{position:absolute;top:560px;left:0;right:0;text-align:center;color:{GOLD};
  font-size:30px;letter-spacing:4px;}}
.qwrap{{position:absolute;top:640px;left:110px;right:110px;text-align:center;}}
.q{{font-size:72px;font-weight:900;line-height:1.4;color:{INK};letter-spacing:1px;}}
.mid{{position:absolute;top:1080px;left:130px;right:130px;}}
.opt{{background:rgba(216,178,74,.10);border:1.5px solid rgba(216,178,74,.5);
  border-radius:24px;padding:34px;margin-bottom:34px;text-align:center;
  font-size:44px;color:{INK};}}
.answerbox{{border:1.5px solid rgba(216,178,74,.5);border-radius:24px;padding:60px 40px;
  text-align:center;font-size:42px;color:{SUB};background:rgba(0,0,0,.25);}}
.hint{{text-align:center;margin-top:40px;color:rgba(233,222,198,.7);font-size:34px;}}
.foot{{position:absolute;bottom:150px;left:0;right:0;text-align:center;
  color:rgba(216,178,74,.6);font-size:28px;letter-spacing:4px;}}
</style></head><body>
<div class="frame"></div>
<div class="wm">浮生矩陣</div>
<div class="top">{html.escape(room)}</div>
<div class="tag">【{html.escape(q['type'])}】</div>
<div class="qwrap">{lines}</div>
<div class="mid">{mid}</div>
<div class="foot">看見戲 ｜ 解開碼 ｜ 回到家</div>
</body></html>"""


def render_story(path_png, htmlstr):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write(htmlstr)
        p = fh.name
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--hide-scrollbars", "--force-device-scale-factor=2",
                    "--window-size=1080,1920", f"--screenshot={path_png}", f"file://{p}"],
                   check=True, capture_output=True)
    os.unlink(p)


def main():
    for di, day in enumerate(DAYS):
        ddir = os.path.join(OUT, day["day"])
        os.makedirs(ddir, exist_ok=True)
        for i, c in enumerate(day["cards"], 1):
            bg = COVER_BGS[di % 3] if c["cover"] else BGS[(di * 7 + i) % 9]
            cc = {"bg": bg, "kicker": c["kicker"], "page": f"{i:02d} / 07",
                  "title": c["title"], "body": c["body"], "cover": c["cover"]}
            # render() 寫到 out/<name>.png；改寫成寫進日夾
            import render_bg
            html_str = card_html(cc)
            outfile = os.path.join(ddir, f"{i:02d}_carousel.png")
            _screenshot(outfile, html_str, "1080,1350")
        # IG 限動問答
        render_story(os.path.join(ddir, "08_story_問答.png"), story_html(day))
        print("done", day["day"])


def _screenshot(outfile, htmlstr, size):
    with tempfile.NamedTemporaryFile("w", suffix=".html", delete=False, encoding="utf-8") as fh:
        fh.write(htmlstr)
        p = fh.name
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--hide-scrollbars", "--force-device-scale-factor=2",
                    f"--window-size={size}", f"--screenshot={outfile}", f"file://{p}"],
                   check=True, capture_output=True)
    os.unlink(p)


if __name__ == "__main__":
    main()
