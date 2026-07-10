# 模組 2 設定指南｜官方 API 金鑰怎麼申請

拿你自己商業帳號的數據，全部走官方管道，合法穩定。缺哪個平台就跳過哪個，不影響其他。

---

## Instagram + Facebook（Meta Graph API）

1. 到 [developers.facebook.com](https://developers.facebook.com) 建立一個 App（類型選「商業」）。
2. IG 帳號需為**商業帳號 / 創作者帳號**，並綁定一個 Facebook 粉專。
3. 加入 **Instagram Graph API** 產品，取得 `META_ACCESS_TOKEN`（長期 token）。
4. 需要的權限：`instagram_basic`、`instagram_manage_insights`、`pages_read_engagement`、`pages_show_list`。
5. 取得 ID：
   - `IG_BUSINESS_ACCOUNT_ID`：Graph API Explorer 查 `me/accounts` → 粉專 → `instagram_business_account`。
   - `FB_PAGE_ID`：粉專「關於」頁最下方，或 `me/accounts`。

填入 `.env`：
```
META_ACCESS_TOKEN=EAAG...
IG_BUSINESS_ACCOUNT_ID=1784...
FB_PAGE_ID=1029...
```

---

## Threads（官方 API）

1. 一樣在 Meta App 中加入 **Threads API**。
2. 走 OAuth 拿 `THREADS_ACCESS_TOKEN`，權限 `threads_basic`、`threads_manage_insights`。
3. `THREADS_USER_ID`：呼叫 `GET https://graph.threads.net/v1.0/me?access_token=...`。

文件：<https://developers.facebook.com/docs/threads>

---

## 抖音（抖音開放平台）

1. 到 [抖音開放平台](https://developer.open-douyin.com) 註冊開發者、建立應用。
2. 取得 `DOUYIN_CLIENT_KEY` / `DOUYIN_CLIENT_SECRET`。
3. 走「用戶授權」OAuth 流程拿 `DOUYIN_ACCESS_TOKEN`（需要 `data.external.item` 等 scope 才能讀影片數據）。
4. 個人號權限有限；完整數據建議用「企業號 / 巨量算數」。

---

## 小紅書

小紅書—沒有面向創作者的公開資料 API。官方數據請至：
- **菲公英平台**（品牌合作與數據）
- **專業號後台 → 數據中心**

本工具不會爬小紅書（違規且會限流）。這塊維持人工看後台最安全。

---

## 跳起來

```bash
cd modules/2-analytics-dashboard
python dashboard.py
```

只要填了任一平台的金鑰，就會顯示那個平台的數據；其他自動略過。
