# Brand Pack · 浮生矩陣-溫柔（療癒・留白・陪伴）

> social-cards-engine 品牌插件。用於**偏陪伴/接納/回家**的房間。
> 觸發：房間為 `木雕哲學`／`回家`，或你說「溫柔版」。
> 渲染實作：`../render_preview.py`（theme=`soft`）。

## 🎨 視覺識別（奶油底・鼠尾草綠・黑體）
```css
--bg:#faf7f2;      /* 奶油米白底（留白、不刺眼）*/
--card:#ffffff;    /* 卡片白 */
--ink:#3a352f;     /* 暖褐主字（不用純黑，柔一階）*/
--acc:#5c7d5c;     /* 鼠尾草綠 accent（品牌主色）*/
--accbg:#eef3ee;   /* 淺綠框（highlight / 練習）*/
--sub:#6b6459;     /* 灰褐內文 */
--line:#e8e2d9;    /* 米色分隔線 */
```
- **字體**：`PingFang TC`／`Noto Sans TC`，字重不過粗，行距 ≥ 1.9。
- **簽名母題**：白卡 + 柔陰影 + 大量留白 + 頁尾 wordmark「浮生矩陣 🌿」+ `0X/07`。
- **尺寸**：4:5（1080×1350），2× 高清。

## 🌿 敘事 DNA（共用）
- 第二人稱「**妳**」，溫柔不說教；`痛點對號 → 翻轉 → 一個小練習`。
- **anti-hype 硬邊界**（碰到即 carousel-joker FAIL）：不恐嚇／不神化／不絕對預測／不成功學／不顯化神話／不醫療療效宣稱。
- 溫柔版天生貼合療癒語感——重點句用 `--accbg` 淺綠柔性 highlight，不用衝突色。

## 🎯 封面 + CTA（sends / saves 優先，對齊 social-post R35/R39）
- 封面一句大字（≤14 字），綠色只點**一個關鍵詞**。
- 第 7 張：今日練習 + 留言關鍵字 CTA；關鍵字須與**模組 5 `keyword_map.csv`** 一致。

## ✅ 過閘
carousel-joker（含 anti-hype 品牌安全）→ huashu-design（留白/置中/不跑版）。
