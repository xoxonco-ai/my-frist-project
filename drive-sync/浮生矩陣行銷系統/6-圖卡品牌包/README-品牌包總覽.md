# 浮生矩陣 social-cards 品牌包（雚主題）

給 [social-cards-engine](https://github.com/DennisWei9898/social-cards-engine) 用的品牌插件。
**兩個主題，依房間分流**：黑金（洞察/覺醒）＋ 溫柔（陪伴/療癒）。都已修掉原本的模糊殘影。

> 📌 **下次要出圖看這裡 → USAGE.md**（兩條路：網頁 / 你 Mac，含確切指令）

## 兩個 pack

| pack | 風格 | 用在哪些房間 |
|------|------|--------------|
| `浮生矩陣-黑金/` | 近黑底・燙金・明體，貴氣有力量 | 見幻筆記・浮生解碼・登出指南 |
| `浮生矩陣-溫柔/` | 奶油底・鼠尾草綠・黑體，留白療癒 | 木雕哲學・回家 |

房間→主題對照見 `room_theme_map.csv`（提案，可改）。

## 直接出圖

```bash
python render_preview.py     # 兩主題各出 D01 樣卡到 out/
```
`render_preview.py` 已內建兩主題色票、字體（黑金=明體 Noto Serif TC / 溫柔=黑體）、
房間路由，以及乾淨版型（**無模糊殘影層**）。

## 裝進 social-cards-engine

```bash
cp -r 浮生矩陣-黑金 浮生矩陣-溫柔 <social-cards-engine>/brands/
```
之後在 Claude Code 說：
> 用 social-cards 做圖卡，房間是「浮生解碼」（→自動走黑金），讀 D03 的輪播檔，做 7 張，第 7 張 CTA 關鍵字「金錢劇本」。

## 設計重點
- **色票**取自真實素材（黑金＝你實際圖卡；溫柔＝療癒替代版），非憑愗覺。
- **封面/CTA** 對齊 social-post 的 sends>saves>likes；關鍵字回扣**模組 5** 自動私訊。
- **anti-hype 硬邊界**寫進兩包，碰到恐嚇/神化/顯化由 carousel-joker 擋下。

## 渲染腳本(完整程式碼在 GitHub repo 與備份 zip)
render_bg.py(黑金底圖版・正式)/ render_preview.py(雙主題預覽)/ render_d03.py(單日範例)/
render_w1~w3.py(週卡)/ render_examples.py
