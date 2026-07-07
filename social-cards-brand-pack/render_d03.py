#!/usr/bin/env python3
"""D03 完整 7 張輪播圖 — 反對派也要有位置（房間：登出指南 → 黑金）。
依「最新」W1 發文包：D03 = 反對派也要有位置（原金錢移至 D06），CTA「登出」。
"""
from render_preview import THEMES, card_html, render

THEME = "blackgold"           # 登出指南 → 黑金
WM = "醒"                     # 頂部水印（清醒主題）

CARDS = [
    # 1 封面 / 語錄圖
    {"kicker": "語錄圖", "wm": WM, "page": "01 / 07",
     "title": [("反對派", False), ("也要有位置", True)], "body": []},
    # 2 靈性陷阱三種模式
    {"kicker": "靈性陷阱", "wm": WM, "page": "02 / 07",
     "title": [("三種常見的模式", True)],
     "body": ["用「覺察」合理化迴避。", "用「放下」拒絕感受。", "用「相信宇宙」逃避決策。"]},
    # 3 這不是批評靈性實踐
    {"kicker": "先說清楚", "wm": WM, "page": "03 / 07",
     "title": [("這不是在批評", False), ("靈性實踐", True)],
     "body": ["那些工具本身是有效的。", "", "問題是——當它們被當成盾牌，",
              "就不再是療癒，是防衛。"]},
    # 4 真正的放下
    {"kicker": "核心句", "wm": WM, "page": "04 / 07",
     "title": [("真正的放下", False), ("是先感受，再放開", True)],
     "body": ["不是還沒感受，", "就告訴自己「我放下了」。"]},
    # 5 反對派的定義
    {"kicker": "反對派是誰", "wm": WM, "page": "05 / 07",
     "title": [("還沒準備好的", False), ("那個妳", True)],
     "body": ["那個懷疑的聲音、", "那個覺得「我還做不到」的自己——", "也要被允許存在。",
              "", "那不是不夠靈性，是很誠實。"]},
    # 6 CTA
    {"kicker": "留言解鎖", "wm": WM, "page": "06 / 07",
     "title": [("留言", False), ("「登出」", True)],
     "body": ["我寄妳清醒練習，", "一起分辨：", "這是釋懷，還是逃避？"]},
    # 7 今日練習
    {"kicker": "今日練習", "wm": WM, "page": "07 / 07",
     "title": [("一個清醒練習", False)],
     "body": ["找一句妳最近常用的靈性語言，", "然後問自己：", "",
              "「我說這句話，是真的感受到，", "　還是在阻止自己繼續感受？」"]},
]


def main():
    t = THEMES[THEME]
    for i, card in enumerate(CARDS, 1):
        name = f"D03_{THEME}_{i:02d}"
        render(name, card_html(card, t))
        print("rendered", name)


if __name__ == "__main__":
    main()
