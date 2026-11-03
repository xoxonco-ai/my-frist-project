# OpenMontage 使用指南（中文）

[OpenMontage](https://github.com/calesthio/OpenMontage) 是開源的 agentic 影片製作系統。
本文是中文操作指南：怎麼裝、怎麼開口、每個指令做什麼。

> 本地中文化參考，非 OpenMontage 上游內容。
> 技能檔的中文對照另見 [`openmontage-skills-zh.md`](openmontage-skills-zh.md)。

---

## 先理解一件事

OpenMontage **沒有程式編排器**。它不是你跑一個 `main.py` 然後等影片跑出來。

它是一整套寫給 AI coding assistant 讀的說明書 —— **你的 AI 助理本身就是製片統籌**。
你把 repo 開在 Claude Code / Cursor / Codex 裡，用白話交代要什麼，助理去讀管線定義、
讀該階段的導演技能檔、呼叫工具、自我檢查、在關鍵決策點停下來問你。

所以「使用 OpenMontage」= 在 AI 助理裡開這個 repo，然後講人話。

---

## 安裝

### 先決條件

| 需求 | 說明 |
|---|---|
| Python 3.10+ | |
| FFmpeg | `brew install ffmpeg` / `sudo apt install ffmpeg` |
| Node.js 18+ | Remotion 與 HyperFrames 都靠它 |
| AI coding assistant | Claude Code、Cursor、Copilot、Windsurf、Codex 皆可 |

### 三行裝完

```bash
git clone https://github.com/calesthio/OpenMontage.git
cd OpenMontage
make setup
```

`make setup` 會做五件事：建 `.venv`、裝 Python 相依、`npm install` Remotion、
裝免費離線語音 Piper TTS、預熱 HyperFrames 的 npx 快取，最後從 `.env.example` 生出 `.env`。

### 沒有 make 的話

```bash
python3 -m venv .venv && source .venv/bin/activate \
  && python -m pip install -r requirements.txt \
  && cd remotion-composer && npm install && cd .. \
  && python -m pip install piper-tts \
  && cp .env.example .env
```

Windows PowerShell 把 `source .venv/bin/activate` 換成 `.\.venv\Scripts\Activate.ps1`；
若 `npm install` 報 `ERR_INVALID_ARG_TYPE`，改用 `npx --yes npm install`。

### API 金鑰（全部可選）

`.env` 裡每一把鑰匙都是選配，**加越多工具越多，一把都不加也能做出片**。
常見的幾把：

| 金鑰 | 解鎖什麼 |
|---|---|
| `FAL_KEY` | FLUX 圖片 + Veo / Kling / MiniMax 影片 |
| `ATLASCLOUD_API_KEY` | Seedream / Nano Banana / GPT Image + Kling / Seedance / Hailuo |
| `PEXELS_API_KEY`、`PIXABAY_API_KEY`、`UNSPLASH_ACCESS_KEY` | 免費素材庫（開發者金鑰免費申請） |
| `ELEVENLABS_API_KEY` | 高階配音、AI 音樂、音效 |
| `GOOGLE_API_KEY` | Imagen 圖片、Google TTS（700+ 嗓音） |
| `SUNO_API_KEY` | 整首歌、演奏曲 |

有 NVIDIA GPU 的話 `make install-gpu`，再在 `.env` 加 `VIDEO_GEN_LOCAL_ENABLED=true`，
可本機免費生影片。

---

## 零金鑰能做到什麼

`make setup` 完就立刻可用的免費能力：

| 能力 | 用什麼 |
|---|---|
| 旁白配音 | Piper TTS（離線、免費） |
| 開放素材 | Archive.org、NASA、Wikimedia Commons |
| 合成（React） | Remotion —— 圖片場景、文字卡、數據卡、圖表、逐字字幕 |
| 合成（HTML/GSAP） | HyperFrames —— 動態字體、產品短片、SVG 角色動畫 |
| 後製 | FFmpeg —— 編碼、字幕燒錄、混音、調色 |
| 字幕 | 內建，含逐字時間軸 |

重點：**它不只是「讓靜圖動起來」**。走 `documentary-montage` 這條管線，
它會從免費素材庫與開放檔案庫抓真實動態影片、做語意排序、剪成時間軸、
輸出一支真正的實拍剪輯片 —— 完全不需要付費影片模型。

---

## 怎麼用

開好 repo 之後，直接講要什麼：

```
做一支 60 秒的動畫解說，講神經網路怎麼學習
```

```
做一支 75 秒的城市雨天紀錄片蒙太奇。只用實拍素材，不要旁白，
輓歌式的調性，要配樂。
```

助理接著會自己跑完：線上研究 → 提案 → 腳本 → 分鏡 → 素材 → 剪輯 → 合成，
中間在幾個關卡停下來等你點頭。

---

## Rule Zero：所有製作都走管線

這是 OpenMontage 的硬規則。助理收到任何影片需求時，必須：

1. **選管線** —— 從 `pipeline_defs/` 裡挑一條，不確定就問你
2. **讀 manifest** —— `pipeline_defs/<管線>.yaml`，知道有哪些階段、工具、品質關卡
3. **跑 preflight** —— 掃描註冊表，把實際可用的能力攤給你看
4. **逐階段執行** —— 每個階段動手前，先讀 `skills/pipelines/<管線>/<階段>-director.md`
5. **呼叫工具前先讀 Layer 3 技能** —— `.agents/skills/` 裡有各家供應商的提示詞訣竅

明文禁止的事：寫臨時 Python 腳本直接呼叫工具、跳過管線直打 API、
沒讀導演技能就生素材、繞過 preflight / 檢查點 / 審查。

> 智慧在技能檔裡，不在即興寫的程式碼裡。

---

## 七階段流程

每條管線都走同一組骨架：

```
research → proposal → script → scene_plan → assets → edit → compose
```

每個階段配一個**導演技能檔**（一份 markdown），教助理這個階段該怎麼做。

其中 `research` 是一等公民：動筆寫腳本前，助理會先去搜 YouTube、Reddit、
Hacker News、新聞與學術來源，蒐集數據點、觀眾疑問、趨勢角度與視覺參考，
整理成有引用的研究簡報。

---

## 12 條管線

| 管線 | 做什麼 | 穩定度 |
|---|---|---|
| `animated-explainer` | 從題目到全自動生成的解說片 | production |
| `animation` | 動態圖像、動態字體、動畫序列 | production |
| `cinematic` | 預告片、前導片、情緒向剪輯 | production |
| `screen-demo` | 軟體螢幕錄製與操作導覽 | production |
| `hybrid` | 既有素材 + AI 生成輔助視覺 | production |
| `avatar-spokesperson` | 虛擬主播、對嘴影片 | production |
| `documentary-montage` | 從 CLIP 索引的免費素材庫剪出主題蒙太奇 | beta |
| `talking-head` | 以人物談話為主的影片 | beta |
| `clip-factory` | 一支長片切成一批排序過的短影音 | beta |
| `podcast-repurpose` | Podcast 精華轉影片 | beta |
| `character-animation` | 本地綁定的卡通角色、可重用角色演出 | beta |
| `localization-dub` | 字幕、配音、多語版本 | beta |
| `framework-smoke` | 測試用的兩階段冒煙測試 | test |

> beta 管線未經完整審核，能跑但有粗糙處；助理選到時應主動告知。

各管線的分工導演數量不一致，從 6 到 11 不等 —— `character-animation` 有 11 個
（多了角色設計與綁定規劃），`animation`／`cinematic`／`explainer` 各 10 個，
七條管線 8 個，`documentary-montage` 只有 6 個（它是檢索驅動，不跑腳本與提案）。

---

## 常用指令

```bash
make setup              # 完整安裝（預設目標，直接 make 也是跑這個）
make demo               # 零金鑰示範片：純 Remotion 的圖表、文字、數據動畫
make demo-list          # 列出有哪些示範可以跑
make preflight          # 印出供應商選單：現在到底有哪些工具可用
make hyperframes-doctor # 完整診斷 HyperFrames 執行環境
make hyperframes-warm   # 刷新 npx 快取到最新版 hyperframes
make test               # 跑 pytest
make install-gpu        # 加裝 GPU 本地影片生成
```

### 能力探查（preflight 的三個層次）

助理在動工前應該跑第一個，**不要**把第三個貼進對話（它是 MB 級的 JSON）：

```bash
# 1. 人類可讀的彙總 —— 預設用這個
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.provider_menu_summary(), indent=2))"

# 2. 完整選單 —— 每個能力底下可用／不可用的供應商
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.provider_menu(), indent=2))"

# 3. 原始封包 —— 每個工具的完整契約，只在除錯時用
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.support_envelope(), indent=2))"
```

彙總會回四個欄位：`composition_runtimes`（ffmpeg／remotion／hyperframes 是否就緒）、
`capabilities[]`（每類能力「N 個已設定／共 M 個」）、`setup_offers[]`（一分鐘就能補上的環境變數）、
`runtime_warnings[]`（像「hyperframes: npm 套件無法解析」這種會靜默壞掉的訊號）。

### Backlot：即時監看面板

```bash
python -m backlot open                  # 片庫 —— 磁碟上每個專案
python -m backlot open <project-id>     # 某支製作的即時看板
python scripts/backlot_simulate_run.py  # 還沒有專案？看一場模擬跑給你看
```

跑完之後按 **▶ REPLAY RUN**，整場製作會依時間戳重播，可以從頭拖到尾。
看板是觀察者，不是阻擋者 —— 開不起來不影響製作繼續跑。

---

## 專案目錄

每次製作都在 `projects/` 底下開一個工作區（已 gitignore，產物都可重生）：

```
projects/<project-name>/
├── artifacts/          # 各階段的 JSON 產出（research_brief、script、scene_plan…）
├── assets/
│   ├── images/         # 生成的圖片
│   ├── video/          # 生成的影片片段
│   ├── audio/          # 旁白片段 + 最終混音
│   ├── music/          # 背景音樂
│   └── subtitles.srt   # 字幕
└── renders/
    └── final.mp4       # 最終成品
```

命名用 kebab-case，從片名推導（例如 `hidden-math-of-nature`）。
所有工具都必須明確寫入 `projects/<project-id>/` 底下 —— 寫到 repo 根目錄、
當前目錄或暫存目錄的檔案，看板看不到，也違反工作區契約。

想放自己的無版權音樂，丟進 `music_library/`（同樣 gitignore），
素材階段會先翻這個資料夾，再考慮呼叫 API 生音樂。

---

## 人類審核關卡

什麼時候會停下來問你，由 manifest 的 `human_approval_default` 決定，**這個值是綁定的**，
助理不能自行改判。`lib/checkpoint.py` 會強制執行：被設關卡的階段，
沒有 `human_approved=True` 就寫不進 `completed`。

典型的關卡：`proposal`、`script`、`scene_plan`、`assets`（逐場看生成的素材，
就是 Backlot 看板上的膠捲條），以及有發布階段的管線的 `publish`。
多數管線在 `edit` 與 `compose` 自動放行，但不是全部 —— `documentary-montage` 的 `edit` 也設關卡。

**同意是逐關的。** 一開始說「你繼續」不涵蓋後面的關卡；
要一次授權整場，必須記成 `decision_log` 裡 `category: "approval_policy"` 的條目才算數。

---

## 兩套合成引擎

| | Remotion | HyperFrames |
|---|---|---|
| 技術 | React | HTML / CSS / GSAP |
| 預設用於 | 數據驅動的解說片、沿用既有 React 場景堆疊 | 動態圖像為主、天生適合 HTML + GSAP 的需求 |
| 擅長 | 彈簧動畫圖片場景、文字卡、數據卡、圖表、TikTok 式逐字字幕、TalkingHead | 動態字體、產品短片、發表影片、網站轉影片、SVG 角色綁定動畫 |

在提案階段就會二選一並鎖定為 `render_runtime`。
`character-animation` 管線的 SVG/GSAP 綁定輸出走 HyperFrames。
完整決策矩陣見 repo 內 `skills/core/hyperframes.md`。

助理有一條硬規則：**兩套執行環境都要攤出來給你選**，不能擅自替你決定。

---

## 延伸閱讀（repo 內）

| 檔案 | 內容 |
|---|---|
| `AGENT_GUIDE.md` | 給 AI 助理的行為契約 —— Rule Zero、決策溝通、關卡協定 |
| `PROJECT_CONTEXT.md` | 專案脈絡 |
| `PROMPT_GALLERY.md` | 提示詞範例集 |
| `docs/PROVIDERS.md` | 所有供應商整理 |
| `skills/INDEX.md` | 技能檔索引 |
| `backlot/README.md` | 監看面板運作原理 |
| `README_zh-CN.md` | 官方簡體中文 README |

技能檔分佈：`skills/` 有 156 個導演與技法檔（四層：pipelines／creative／meta／core），
另外 `.agents/skills/` 有 577 個 Layer 3 供應商知識檔 —— 那是教助理把每個工具
用得像專家的部分。
