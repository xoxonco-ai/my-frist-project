# drive-sync — Google Drive 同步內容

此資料夾為 **Google Drive → 本機（單向下載）** 的同步結果，方便在 repo 內離線檢視 Drive 上的行銷文件。此處內容**不覆寫**任何既有程式碼，僅作為 Drive 內容的本機鏡像；要正式納入專案時再手動挑選合併。

- **同步方向**：Drive → 本機（下載）
- **同步日期**：2026-07-10
- **來源帳號**：xoxonco@gmail.com

## 內容對應

| 本機資料夾 | Drive 來源資料夾 |
|-----------|-----------------|
| `浮生矩陣行銷系統/` | Google Drive「浮生矩陣行銷系統」（1-7 號子資料夾） |

### 已同步（浮生矩陣行銷系統，23 個檔案）

- `1-攻略與規格/` — 流量演算法攻略、強化規格
- `2-工作流與使用手冊/` — skill 總覽與內容工作流、使用方法與觸發指令大全
- `3-全部Skills合併總檔/` — 說明檔（合併檔存放位置指引）
- `4-Skills原始檔/` — 說明檔（原始檔存放位置指引）
- `5-模組工具/` — 模組 2~5 的 Python 工具（dashboard / rewrite / hashtag_research / extract_keywords）與 README/SETUP、keyword_map.csv
- `6-圖卡品牌包/` — 品牌包總覽、出圖使用指南、溫柔/黑金 brand、room_theme_map.csv
- `7-工具整合指南/` — 說明檔（工具整合指南存放位置指引）

## 未同步（刻意略過）

依「只下載專案相關文件/skills」的設定，以下項目**未**下載：

- `wav2lip` 模型檔（`.tar` / `.gz` / `.pth`，合計約 950MB）等大型二進位檔
- 課程資料夾（如「2026 覺醒營」等）與其他與本專案無關的內容
- `.git`、`node_modules`、`.DS_Store` 等版控/相依/系統檔

## 備註

- Drive 上的「4-Skills原始檔 / 3-全部Skills合併總檔」多與本 repo `skills/`、`modules/`、`social-cards-brand-pack/` 內容重疊，Drive 端僅放「存放位置說明」，故此處同步的是說明檔而非重複的 skills 原始碼。
- 本次同步工具僅支援單向複製，無法做含刪除比對的雙向同步。
