# 浮生羅盤 · 發文卡品牌包（官方黑金・v5）

浮生羅盤對外 IG 發文卡的渲染工具與規格。**統一黑金風格**，用「每房間對應底圖」（ROOM_BG）做區隔——
不再分黑金／溫柔兩套主題。把每天發文包的文字，疊到品牌黑金底圖上出圖。

> 📌 **下次要出圖看這裡 → [USAGE.md](USAGE.md)**（含確切指令與流程）
> 🎨 視覺規格全文 → [`浮生矩陣-黑金/brand.md`](浮生矩陣-黑金/brand.md)

## 出什麼

| 類型 | 尺寸 | 張數 | 範本腳本 |
|------|------|------|----------|
| IG 輪播卡 | 1080×1350（4:5） | 7 張（封面+5內文+練習卡） | [`render_carousel.py`](render_carousel.py) |
| IG 限動互動 | 1080×1920（9:16） | 2 張（投票+問答） | [`render_story.py`](render_story.py) |

## 品牌規格（官方黑金）

- 字色：`GOLD=#E4C77E`（主燙金）/ `GOLD_HI=#F5E4AC`（強調關鍵詞）
- 字體：`'WenQuanYi Zen Hei','PingFang TC',sans-serif`（系統**黑體**，非明體；網路字型會被 proxy 擋）
- 暗角：**中央** radial-gradient，字全部置中
- 底圖：`bg/bg1.png~bg9.png`（官方 9 張黑金背景，tagline 已烘進底圖）
- 房間→底圖對應（ROOM_BG）見 [`room_theme_map.csv`](room_theme_map.csv)

## 內容來源

| 出什麼 | 讀哪個檔 |
|--------|----------|
| 輪播 7 張 | 各天發文包 `2_1230_IG輪播貼文` 的【輪播 7 張說明】 |
| 限動 2 張 | 各天發文包 `4_1700_IG限動互動`（限動1=投票/問答、限動2） |

發文包位置（Drive）：`01_浮生羅盤_90天信任品牌IP/03_發文包_週產出/浮生羅盤_發文包_WX/DXX_.../`

## 快速出圖

```bash
# 1. 複製範本，改 DAYS 字典（每天內容）
# 2. 底圖放進 bg/（官方 9 張黑金底圖，大檔不進 git）
python3 render_carousel.py     # 輪播 → out/
python3 render_story.py        # 限動 → out_story/
# 3. PNG 通常 1-2MB，用 Pillow 轉 JPEG(88) 縮小 → 一天一包 zip → 交付使用者拖進 Drive
```

Chrome headless 路徑：`/opt/pw-browsers/chromium-1194/chrome-linux/chrome`（本環境 Playwright 預裝；勿跑 `playwright install`）。

## 出圖前必檢

- 輪播**第 7 張 CTA 關鍵字**要和 [模組 5 `keyword_map.csv`](../modules/5-auto-reply/keyword_map.csv) 一致，留言的人才收得到自動私訊。
- 內容守 **anti-hype 硬邊界**：不恐嚇／不神化／不顯化／不療效宣稱。

## 備註

- `浮生矩陣-溫柔/` 是舊的雙主題方案，官方已改統一黑金＋每房間底圖，**溫柔版保留備查、非現行**。
- 底圖大檔不進 git；換環境時重新放 `bg/`。
