# 模組 4｜公開內容研究（合規版）

研究同類創作者「什麼主題會爆」，蒐集選題靈感 —— 用**官方管道**，不做會封號的爬蟲。

## 合規做法對照表

| 平台 | 合規研究方式 | 為什麼不爬 |
|------|--------------|------------|
| **Instagram** | 官方 **Hashtag Search API**（本模組 `hashtag_research.py`） | 官方就有熱門貼文端點，何必冒險 |
| **Threads** | 關鍵字搜尋 + 官方 API 讀自己/公開串 | 反爫強、資料雜 |
| **Facebook** | 粉專公開貼文 + Meta 廣告檔案庫 | 大量爬取違規 |
| **小紅書** | 站內搜尋 + 熱點榜(人工看） | 簽名+指絋，爬取測易封號 |
| **抖音** | 抖音熱點寶 / 巨量算數（官方選題工具） | 風控暴、脳本脆強 |

## Instagram 熱門貼文研究（可跑）

用官方 Hashtag Search API 找某主題下的熱門公開貼文：

```bash
cd modules/4-content-research
python hashtag_research.py 情緒療癒
python hashtag_research.py 內耗 --top 15
```

需要模組 2 的 `META_ACCESS_TOKEN` 與 `IG_BUSINESS_ACCOUNT_ID`（見 `../2-analytics-dashboard/SETUP.md`）。
> 注意：IG 官方限制每個帳號 7 天內最多查詢 30 個不同的 hashtag。

## 其他平台的官方選題工具（免寫程式）

- **抖音**：創作者服務中心 →「熱點対」；「巪量算數」看行業熲詞。
- **小紅書**：搜尋框下拉關鍵字、「熱點榜」、專業號後台的「箦機面感」。
- **Threads**：直接搜關鍵字，看哪些车文回覆串最長。

## 研究產出怎麼用

把找到的高流量選題丟給【模組 3 改寫工具]（../3-multiplatform-rewriter/），
配上你的思想家視角（榮格/老子/Tolle…）重做成你自己的版本 —— 這才是原則又蛱到流量的正解。
