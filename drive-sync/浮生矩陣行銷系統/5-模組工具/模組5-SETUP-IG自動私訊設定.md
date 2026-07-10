# 模組 5 設定指南｜IG 自動私訊

## 一、需要的 Meta 權限

在你模組 2 已建立的 Meta App 上，加開：

- `instagram_manage_messages`（送私訊 / Private Replies 必備）
- 已有的 `instagram_basic`、`pages_manage_metadata`

> IG 帳號需為**商業帳號**並綁定 FB 粉專；且在 IG App →「設定 → 訊息 → 允許存取訊息」開啟。

## 二、.env 要裝的欄位

```
META_ACCESS_TOKEN=            # 沿用模組 2 的長期 token
IG_BUSINESS_ACCOUNT_ID=       # 沿用模組 2
META_APP_SECRET=              # App 後台 → 設定 → 基本資料 → 應用程式密鑰
WEBHOOK_VERIFY_TOKEN=fusheng-verify   # 自訂一組字串，Meta 後台要填一樣的
```

## 三、設定 Webhook

1. Meta App 後台 → **Webhooks** → 選 **Instagram**。
2. Callback URL 填：`https://<你的公開網址>/webhook`
   - 本機測試：另開視窗跑 `ngrok http 5000`，用它給的 https 網址。
   - 正式：部署到任何雲（Render / Railway / Fly.io 都行）。
3. Verify Token 填你 `.env` 裡的 `WEBHOOK_VERIFY_TOKEN`。
4. 訂閱欄位（Subscribe）勾選：**`comments`** 和 **`messages`**。

## 四、測試

```bash
python app.py
# 瀏覽器開 http://localhost:5000/health → 應顯示 keywords 數量
```

用另一個 IG 帳號去你貼文留言「入口」，幾秒內該帳號應收到自動私訊。

## 注意事項

- **回覆視窗**：Private Reply 限留言後 7 天內；一般 DM 回覆限用戶私訊後 24 小時內。系統是即時觸發，正常都在窗內。
- **一天上限**：Meta 對訊息量有頻率限制；正常經營不會踩到，但別拿來群發廣告。
- **內容邊界**：私訊只送「用戶自己要求的練習連結」，不主動推銷，最安全也最不會被檢舉。
