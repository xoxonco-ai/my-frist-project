# Pixelle-Video 安裝指南 / Installation Guide

[Pixelle-Video](https://github.com/ATH-MaaS/Pixelle-Video) 是一個 AI 全自動短影片引擎：輸入一個主題，自動完成腳本生成、AI 配圖、語音合成、背景音樂與影片合成。

Pixelle-Video is an AI fully-automated short video engine: give it a topic and it generates the script, AI illustrations, voiceover, background music, and the final video.

## 系統需求 / Requirements

- Python >= 3.11
- [uv](https://docs.astral.sh/uv/)（Python 套件管理器 / package manager）
- [ffmpeg](https://ffmpeg.org/)（影片處理 / video processing）
- git

## 快速安裝 / Quick Install

使用本倉庫提供的安裝腳本 / use the install script in this repo:

```bash
./tools/setup/install-pixelle-video.sh            # 安裝到 ~/Pixelle-Video
./tools/setup/install-pixelle-video.sh /path/dir  # 或自訂安裝目錄
```

腳本會自動：檢查並安裝 `uv` 與 `ffmpeg`、clone 倉庫、執行 `uv sync` 安裝相依套件、並從 `config.example.yaml` 建立預設 `config.yaml`。

## 手動安裝 / Manual Install

```bash
git clone https://github.com/ATH-MaaS/Pixelle-Video.git
cd Pixelle-Video
uv sync
cp config.example.yaml config.yaml
```

## 啟動 / Run

```bash
cd Pixelle-Video
uv run streamlit run web/app.py
```

開啟瀏覽器前往 http://localhost:8501 ，然後在網頁介面中設定：

1. **LLM**：OpenAI、通義千問（Qwen）、DeepSeek、Ollama 等的 API 金鑰
2. **圖像/影片生成**：ComfyUI、RunningHub，或 DashScope / OpenAI / Kling 等直連 API
3. **語音合成（TTS）**：Edge-TTS（免費預設）、Index-TTS 等

## 其他部署方式 / Alternatives

- **Docker**：倉庫內含 `Dockerfile` 與 `docker-compose.yml`，可用 `docker compose up` 啟動
- **Windows 一鍵包**：官方提供免安裝整合包，解壓後執行 `start.bat`
