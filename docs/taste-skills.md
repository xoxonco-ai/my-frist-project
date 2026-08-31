# Taste Skill 設計技能索引

來源：[Leonxlnx/taste-skill](https://github.com/Leonxlnx/taste-skill)（MIT，作者 Leonxlnx，上游 commit `72e2995`）。

13 個前端設計 / 設計圖生成技能已安裝到 `skills/`，資料夾名稱使用各技能 frontmatter 的 `name`（符合本 repo「name 必須等於資料夾名」的規則），內容與上游一致，只在 frontmatter 補上 `license` 與 `metadata`（作者、來源、上游資料夾、上游 commit）以保留出處。

## 實作型技能（輸出程式碼）

| Skill（本 repo 資料夾） | 中文名 | 上游資料夾 | 說明 |
|---|---|---|---|
| `design-taste-frontend` | 質感前端設計 v2 | taste-skill | 預設主力技能 v2（實驗版）。讀 brief 推斷設計語言，調 VARIANCE / MOTION / DENSITY 三個旋鈕，反樣板化的 landing page、作品集、改版。 |
| `design-taste-frontend-v1` | 質感前端設計 v1（舊版） | taste-skill-v1 | 原始 v1，需要完全相容舊行為時才用。 |
| `gpt-taste` | 質感前端設計 GPT／Codex 版 | gpt-tasteskill | 給 GPT / Codex 的嚴格版：更高版面變異、更強 GSAP 指示、更兇的 anti-slop。 |
| `image-to-code` | 設計圖轉程式碼 | image-to-code-skill | 先產設計參考圖 → 深度分析 → 再實作前端對齊。 |
| `redesign-existing-projects` | 舊網站改版稽核 | redesign-skill | 既有專案：先稽核 UI，再修版面、間距、層級、樣式。 |
| `high-end-visual-design` | 高級感視覺設計 | soft-skill | 高級感、留白、柔對比、premium 字體、彈簧動態。 |
| `full-output-enforcement` | 完整輸出強制（防偷懶） | output-skill | 防止模型偷工：完整輸出，禁止 placeholder 註解。 |
| `minimalist-ui` | 極簡編輯風介面 | minimalist-skill | 編輯感產品 UI（Notion / Linear 風），克制配色、結構清爽。 |
| `industrial-brutalist-ui` | 工業粗獷風介面 | brutalist-skill | 工業粗獷：瑞士字體、極端對比、實驗性版面。 |
| `stitch-design-taste` | Google Stitch 設計規範 | stitch-skill | Google Stitch 相容規則，含 `DESIGN.md` 輸出格式。 |

## 生成圖片型技能（只出圖，不出程式碼）

| Skill（本 repo 資料夾） | 中文名 | 上游資料夾 | 說明 |
|---|---|---|---|
| `imagegen-frontend-web` | 網頁設計稿生成（只出圖） | imagegen-frontend-web | 網站設計稿：hero、landing、多區塊，每個 section 一張橫圖。 |
| `imagegen-frontend-mobile` | App 畫面設計稿生成（只出圖） | imagegen-frontend-mobile | 手機 App 畫面與流程，iOS / Android / 跨平台。 |
| `brandkit` | 品牌識別設計稿（只出圖） | brandkit | 品牌識別板：logo 概念、識別系統、色票、字體、mockup。 |

## 更新方式

上游更新時重跑安裝流程即可（覆蓋同名資料夾，保留 frontmatter 的 `metadata` 出處欄位）：

```bash
npx skills add https://github.com/Leonxlnx/taste-skill
```

或直接從上游 repo 複製對應的 `SKILL.md` 覆蓋。
