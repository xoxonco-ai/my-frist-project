# LiveTalking 使用指南

安裝方式見 [livetalking-install.md](./livetalking-install.md)。本文說明安裝後如何使用。

## 使用流程總覽

```
下載模型（一次性） → 啟動伺服器 → 瀏覽器或 API 互動
```

## 第一步：放置模型檔（只需一次）

從以下任一來源下載模型：

- Google Drive：<https://drive.google.com/drive/folders/1FOC_MD6wdogyyX_7V1d4NDIO7P9NlSAJ?usp=sharing>
- 夸克網盤：<https://pan.quark.cn/s/83a750323ef0>

下載後放到指定位置：

| 檔案 | 放置位置 |
|------|----------|
| `wav2lip256.pth` | `LiveTalking/models/wav2lip.pth`（**必須改名**為 `wav2lip.pth`） |
| `wav2lip256_avatar1.tar.gz` | 解壓後整個資料夾放到 `LiveTalking/data/avatars/wav2lip256_avatar1/` |

## 第二步：啟動伺服器

```bash
cd LiveTalking
./venv/bin/python app.py --transport webrtc --model wav2lip --avatar_id wav2lip256_avatar1
```

常用啟動參數：

| 參數 | 預設值 | 說明 |
|------|--------|------|
| `--transport` | `webrtc` | 輸出方式：`webrtc` / `rtmp` / 虛擬攝影機 |
| `--tts` | `edgetts` | TTS 引擎（edgetts 免費，無需 API key） |
| `--max_session` | `5` | 最大並行連線數 |
| `--listenport` | `8010` | 伺服器連接埠 |
| `--push_url` | — | RTMP 推流位址（搭配 `--transport rtmp`） |

> 防火牆需開放 TCP:8010 與 UDP 連接埠（WebRTC 需要）。

## 第三步：開始互動

### 瀏覽器（最簡單）

開啟 `http://<伺服器IP>:8010/index.html`，點 **Start Connection**，數字人視訊出現後在文字框輸入內容送出，數字人就會開口說話。

| 頁面 | 用途 |
|------|------|
| `/index.html` | 主頁面：連線、文字/語音驅動、錄影 |
| `/avatar.html` | 上傳影片自動製作自己的數字人頭像 |
| `/admin.html` | 管理主控台：監控連線、調整全域設定 |

### API（程式整合）

建立 WebRTC 連線（`POST /offer`）後會取得 `sessionid`，之後用 `/human` 驅動說話：

```bash
# echo 模式：數字人直接唸出這段文字
curl -X POST http://localhost:8010/human \
  -H "Content-Type: application/json" \
  -d '{"sessionid": "<session-id>", "text": "你好，歡迎光臨", "type": "echo"}'

# chat 模式：先由 LLM 回答，再說出來（需先在 config.yaml 設定 LLM API key）
curl -X POST http://localhost:8010/human \
  -H "Content-Type: application/json" \
  -d '{"sessionid": "<session-id>", "text": "介紹一下你自己", "type": "chat", "interrupt": true}'
```

- `interrupt: true` 會打斷數字人當前的播報
- `POST /humanaudio` 可直接上傳音訊檔驅動嘴型
- 完整 API 文件：`LiveTalking/docs/api.md`；頭像 API：`LiveTalking/docs/avatar_api.md`

## 進階設定

- **接 LLM 對話**：編輯 `LiveTalking/config.yaml`，填入 OpenAI 相容的 API key 與模型名稱，`chat` 模式即可使用
- **換 TTS 聲音**：`/human` 請求的 `tts` 參數可指定 `voice`、`emotion` 等
- **直播推流**：`--transport rtmp --push_url rtmp://...` 推到直播平台
- **虛擬攝影機**：見 `LiveTalking/docs/virtualcam_guide.md`，可把數字人輸出到視訊會議軟體

## 常見問題

| 症狀 | 原因 |
|------|------|
| 啟動時 `FileNotFoundError: ./models/wav2lip.pth` | 模型檔沒放對位置，或忘記改名為 `wav2lip.pth` |
| 網頁連線後看不到視訊 | UDP 連接埠被防火牆擋住 |
| 嘴型延遲嚴重、卡頓 | 用 CPU 推論——即時互動需要 NVIDIA GPU |

官方文件：<https://doc.livetalking.ai>
