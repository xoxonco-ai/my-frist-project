# 療癒／覺醒系 內容成長工具箱

一套給療癒與覺醒系自媒體創作者的內容成長工具，涵蓋 **Instagram / Facebook / Threads / 小紅書 / 抖音**。

> ⚠️ **設計原則：安全第一，永不封號。**
> 本專案**不做**大規模爬蟲、不做自動灌發文 —— 這兩件事是各平台最容易直接封號的行為。
> 我們走「官方 API + 合規研究 + 人工發布」的路線，穩定拿到你要的東西：**看懂演算法、追蹤數據、放大流量**。

---

## 四個模組

| # | 模組 | 你會得到 | 需要什麼 |
|---|------|----------|----------|
| **1** | [流量演算法攻略](docs/01-流量演算法攻略.md) | 五平台推薦邏輯 + 療癒系專屬發文公式 | 現在就能讀，免安裝 |
| **2** | [自己帳號數據儀表板](modules/2-analytics-dashboard/) | 官方 API 串接，一頁看完全平台表現 | 你的商業帳號 + API 金鑰 |
| **3** | [一稿多平台改寫工具](modules/3-multiplatform-rewriter/) | 一篇文自動改成各平台語感 | Anthropic API 金鑰 |
| **4** | [公開內容研究](modules/4-content-research/) | 合規蒐集靈感 + 競品分析 | 依平台而定 |
| **5** | [關鍵字自動私訊](modules/5-auto-reply/) | 留言關鍵字→自動私訊練習+收名單 | IG 商業帳號 + Meta 權限 |

搭配文件：[流量演算強化規格](docs/02-流量演算強化規格.md) — 貼進你的 `social-post` / `social-cards` skill，讓每篇發文自動做流量預檢。

---

## 快速開始

```bash
# 1. 讀攻略（不用安裝任何東西）
open docs/01-流量演算法攻略.md

# 2. 想跑程式的話，先裝依賴
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 3. 複製環境變數範本，填入你的金鑰
cp .env.example .env
```

## 為什麼不做全平台爬蟲？

| 平台 | 反爬強度 | 你真正需要的替代方案 |
|------|----------|----------------------|
| IG / FB / Threads | 高 | Meta Graph API / Threads API（官方、免費、拿得到自己數據） |
| 小紅書 | 極高（請求簽名 + 裝置指紋） | 蒲公英平台 / 專業號後台 |
| 抖音 | 極高（風控） | 抖音開放平台 / 巨量算數 |

爬蟲拿到的資料脆弱又違規；官方管道拿到的資料**穩定、完整、還不會害你帳號歸零**。這才是能長久經營的路。

---

## 專案結構

```
.
├── README.md
├── requirements.txt
├── .env.example
├── docs/
│   └── 01-流量演算法攻略.md
└── modules/
    ├── 2-analytics-dashboard/     # 模組 2：官方 API 數據
    ├── 3-multiplatform-rewriter/  # 模組 3：一稿多平台
    └── 4-content-research/        # 模組 4：合規研究
```
