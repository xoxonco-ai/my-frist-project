# 模組 5｜關鍵字 → 自動私訊系統

補上你漏斗最後一環：**有人留言/私訊關鍵字 → 自動私訊書寫練習連結 + 自動收名單。**
走 Instagram 官方 Messaging API（Private Replies），合規、不封號。

```
留言「入口」 ──▶ webhook 收到 ──▶ 自動私訊練習連結 ──▶ 名單存進 leads.csv
```

## 運作方式

| 情境 | 觸發 | 系統動作 |
|------|------|----------|
| 貼文底下留言關鍵字 | Meta `comments` webhook | 用 Private Reply 私訊該用戶 |
| 直接私訊關鍵字 | Meta `messages` webhook | DM 回覆練習連結 |

兩種都會把來訪者記進 `leads.csv`（source, user_id, keyword）。

## 檔案

| 檔案 | 作用 |
|------|------|
| `app.py` | Flask webhook 伺服器（驗簽 + 關鍵字比對 + 送私訊 + 記名單） |
| `keyword_map.csv` | 關鍵字 → 練習連結對照表（已種入 D01–D23 已知關鍵字） |
| `extract_keywords.py` | 從你的 90 天排程表 CSV 一次抽出所有 CTA 關鍵字 |
| `leads.csv` | 自動產生的名單（已被 .gitignore 忽略） |

## 三步上線

```bash
# 1. 裝依賴 + 填金鑰（見 SETUP.md）
pip install -r requirements.txt
cp .env.example .env

# 2. 把 90 天關鍵字一次補齊
python extract_keywords.py 浮生矩陣_90天發文排程表_完整版.csv > keyword_map.new.csv
#   → 填好每列的 worksheet_url，改名蓋回 keyword_map.csv

# 3. 啟動 + 對外（Meta webhook 需要 https 公開網址）
python app.py
#   另開一個視窗： ngrok http 5000  → 把 https 網址填進 Meta 後台
```

詳細的 Meta 權限與 webhook 設定見 **SETUP.md**。

## 為什麼這是合規做法
Private Replies 是 Meta 官方給商業帳號的功能（ManyChat 這類工具也是走這條）。
不是模擬點擊、不是爫蟲、不是機器人洗留言 —— 只在「用戶主動找你」時回應，最安全。
