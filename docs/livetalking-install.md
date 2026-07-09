# LiveTalking 安裝指南

[LiveTalking](https://github.com/lipku/LiveTalking) 是一個即時互動串流數字人引擎，支援 wav2lip、musetalk、ernerf 等模型，可透過 WebRTC / RTMP / 虛擬攝影機輸出。

## 快速安裝

在儲存庫根目錄執行：

```bash
# CPU 環境（無 GPU）
./scripts/install-livetalking.sh

# GPU 環境（CUDA 12.8）
GPU=1 ./scripts/install-livetalking.sh
```

腳本會：

1. 將 LiveTalking 原始碼 clone 到 `./LiveTalking/`
2. 建立 Python 虛擬環境（`LiveTalking/venv/`）
3. 安裝 PyTorch（依 `GPU` 環境變數選擇 CPU 或 CUDA 版本）
4. 安裝 `requirements.txt` 中的所有相依套件

## 系統需求

| 項目 | 需求 |
|------|------|
| 作業系統 | Linux / Windows / macOS |
| Python | 3.10 以上 |
| ffmpeg | 必要（`apt-get install -y ffmpeg`） |
| GPU | 建議使用 NVIDIA GPU（即時推論需要）；CPU 可安裝但推論速度不足以即時互動 |

## 手動下載模型（必要步驟）

模型檔案無法自動下載，需手動取得：

| 來源 | 連結 |
|------|------|
| Google Drive | <https://drive.google.com/drive/folders/1FOC_MD6wdogyyX_7V1d4NDIO7P9NlSAJ?usp=sharing> |
| 夸克網盤 | <https://pan.quark.cn/s/83a750323ef0> |

1. 將 `wav2lip256.pth` 複製到 `LiveTalking/models/` 並重新命名為 `wav2lip.pth`
2. 解壓 `wav2lip256_avatar1.tar.gz`，將整個資料夾放到 `LiveTalking/data/avatars/`

## 啟動伺服器

```bash
cd LiveTalking
./venv/bin/python app.py --transport webrtc --model wav2lip --avatar_id wav2lip256_avatar1
```

> 伺服器需開放 TCP:8010 與 UDP 連接埠。

啟動後用瀏覽器開啟 `http://<伺服器IP>:8010/index.html`，點「Start Connection」即可播放數字人視訊並輸入文字互動。

## 其他頁面

| 頁面 | 網址 | 說明 |
|------|------|------|
| 首頁 | `/index.html` | WebRTC 連線 + 文字/語音驅動 + 錄影控制 |
| 頭像製作 | `/avatar.html` | 上傳影片自動產生數字人頭像 |
| 管理主控台 | `/admin.html` | 即時工作階段監控與全域設定 |

## 官方文件

- 完整文件：<https://doc.livetalking.ai>
- 安裝 FAQ：<https://doc.livetalking.ai/en/docs/faq/>
