# 浮生矩陣 social-cards 品牌包

給 [social-cards-engine](https://github.com/DennisWei9898/social-cards-engine) 用的品牌插件。
接上它，圖卡就從「通用模板」變成你的療癒風格。

## 怎麼裝（2 步）

```bash
# 1. 把品牌包複製進 social-cards-engine
cp -r 浮生矩陣 <social-cards-engine>/brands/浮生矩陣

# 2. 從最接近的內建 pack 複製一份渲染模板，改配色即可
cp <social-cards-engine>/brands/meme/render_template.py \
   <social-cards-engine>/brands/浮生矩陣/render_template.py
#   → 把裡面的色票換成 brand.md 的 CSS 變數（奶油底/鼠尾草綠/暖褐字）
```

之後在 Claude Code 說：
> 用 social-cards 幫我做圖卡，品牌用**浮生矩陣**，讀 D01 的 `2_1230_IG輪播貼文.md`，依【輪播說明】做 7 張，第 7 張 CTA 關鍵字用「入口」。

## 內容

- **`浮生矩陣/brand.md`** — 完整品牌規格：真實色票、字體、留白母題、房間標籤、
  anti-hype 硬邊界、封面/CTA 規則（已對齊 social-post 的 sends>saves>likes 與模組 5 自動私訊）。

## 還沒做的（要的話跟我說）
- `render_template.py`：實際渲染的 Python（4:5 HTML→PNG）。我可以照 brand.md 的色票幫你寫一版，
  但需要對齊 social-cards-engine 的模板介面——你說一聲我就做。
