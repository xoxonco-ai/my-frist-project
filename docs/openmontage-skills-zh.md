# OpenMontage 技能中文對照表

[OpenMontage](https://github.com/calesthio/OpenMontage)（開源 agentic 影片製作系統）的
`skills/` 目錄共 **156 個技能檔**，分四層。本表為中文對照，方便快速辨識。

> 這份對照的是 **OpenMontage 的技能**，不是本 repo 的 `skills/`。
> 為本地中文化參考，非 OpenMontage 上游內容。

---

## 目錄總覽

| 目錄 | 中文名 | 檔數 | 作用 |
|---|---|---|---|
| `pipelines/` | **生產管線層** | 103 | 12 條完整製片流程，各配一組分工導演 |
| `creative/` | **創意手法層** | 36 | 怎麼把片子拍得好看 |
| `meta/` | **流程統籌層** | 11 | 誰來決策、誰來把關、何時停下問你 |
| `core/` | **核心技術層** | 6 | 底層引擎與工具的正確用法 |

---

## 一、生產管線層（12 條）

| 目錄名 | 中文名 | 一句話 |
|---|---|---|
| `explainer` | **動畫解說片** | 研究＋旁白＋視覺＋配樂的知識片 |
| `animation` | **動態圖形片** | 純動畫、文字動態、抽象概念 |
| `documentary-montage` | **紀實蒙太奇** | 免費真實素材語意檢索剪輯 |
| `cinematic` | **電影感預告片** | 品牌片、teaser、氛圍剪輯 |
| `character-animation` | **角色動畫片** | SVG 骨架＋GSAP 卡通演出 |
| `clip-factory` | **短影音切片工廠** | 一支長片切成一批排名短片 |
| `talking-head` | **講者口播片** | 人臉為主的說話影片 |
| `screen-demo` | **螢幕操作導覽** | 產品 demo、教學 |
| `podcast-repurpose` | **Podcast 轉影片** | 聲音節目做成影片 |
| `localization-dub` | **在地化配音** | 翻譯、字幕、配音 |
| `avatar-spokesperson` | **虛擬主播片** | AI 人像代言 |
| `hybrid` | **實拍混搭片** | 你的實拍＋AI 補視覺 |

### 分工導演對照

| 檔名 | 中文名 | 職責 |
|---|---|---|
| `executive-producer` | **總製片** | 統籌全局、控預算、決定送回重做 |
| `research-director` | **調研導演** | 開拍前的網路調研與事實查核 |
| `idea-director` | **創意發想導演** | 從需求長出概念 |
| `proposal-director` | **提案導演** | 把概念寫成可核可的提案 |
| `script-director` | **編劇導演** | 寫劇本與旁白稿 |
| `scene-director` | **分鏡導演** | 拆場、排鏡頭 |
| `asset-director` | **素材導演** | 生圖、生影片、找素材、配樂 |
| `edit-director` | **剪輯導演** | 排時間軸、節奏、轉場 |
| `compose-director` | **合成導演** | 最終渲染輸出 |
| `publish-director` | **發佈導演** | 各平台規格與打包 |
| `character-design-director` | **角色設計導演** | 僅角色動畫片 |
| `rig-plan-director` | **骨架規劃導演** | 僅角色動畫片 |

### 各管線實際配置

導演組並非每條都相同，依製作需要增減：

| 管線 | 導演數 | 配置 |
|---|---|---|
| 角色動畫片 | 11 | 總製片＋調研＋提案＋**角色設計**＋**骨架規劃**＋編劇＋分鏡＋素材＋剪輯＋合成＋發佈 |
| 動畫解說片 | 10 | 全套十人組（含調研、提案） |
| 動態圖形片 | 10 | 全套十人組 |
| 電影感預告片 | 10 | 全套十人組 |
| 講者口播片 | 8 | 無調研、無提案 |
| 螢幕操作導覽 | 8 | 無調研、無提案 |
| 短影音切片工廠 | 8 | 無調研、無提案 |
| Podcast 轉影片 | 8 | 無調研、無提案 |
| 在地化配音 | 8 | 無調研、無提案 |
| 虛擬主播片 | 8 | 無調研、無提案 |
| 實拍混搭片 | 8 | 無調研、無提案 |
| 紀實蒙太奇 | 6 | 總製片＋創意發想＋分鏡＋素材＋剪輯＋合成 |

---

## 二、創意手法層（36）

### 敘事結構

| 檔名 | 中文名 |
|---|---|
| `storytelling` | **說故事結構** |
| `short-form` | **短影音敘事** |
| `long-form` | **長影片敘事** |
| `cinematic` | **電影語言** |
| `broll-planning` | **空鏡規劃** |

### 視覺製作

| 檔名 | 中文名 |
|---|---|
| `image-gen-usage` | **生圖用法** |
| `image-provider-usage` | **生圖供應商選用** |
| `video-gen-prompting` | **生影片提示詞** |
| `3d-world-generation` | **3D 世界生成** |
| `animated-drawing` | **手繪動畫** |
| `animation-pipeline` | **動畫製作流程** |
| `ink-theater` | **水墨劇場** |
| `typography` | **字體動態排印** |
| `data-visualization` | **資料視覺化** |
| `diagram-gen-usage` | **圖表生成** |
| `manim-usage` | **Manim 數學動畫** |

### 剪輯後製

| 檔名 | 中文名 |
|---|---|
| `video-editing` | **剪輯手法** |
| `video-stitching` | **影片接合** |
| `scene-detect-usage` | **場景切分偵測** |
| `video-understand-usage` | **影片內容理解** |
| `stock-sourcing-usage` | **素材庫檢索** |
| `screen-recording` | **螢幕錄製** |

### 聲音

| 檔名 | 中文名 |
|---|---|
| `sound-design` | **聲音設計** |
| `music-gen-usage` | **AI 配樂生成** |
| `talking-head-gen-usage` | **口播影片生成** |
| `lip-sync-usage` | **對嘴同步** |

### 畫質修補

| 檔名 | 中文名 |
|---|---|
| `enhancement-strategy` | **畫質強化策略** |
| `upscale-usage` | **解析度放大** |
| `face-restore-usage` | **人臉修復** |
| `bg-remove-usage` | **去背** |

### 各家模型專屬提示詞（`prompting/`，6 支）

| 檔名 | 中文名 |
|---|---|
| `veo-prompting` | **Veo 提示詞** |
| `sora-prompting` | **Sora 提示詞** |
| `seedance-prompting` | **Seedance 提示詞** |
| `grok-prompting` | **Grok 提示詞** |
| `hunyuan-prompting` | **混元提示詞** |
| `ltx-prompting` | **LTX 提示詞** |

---

## 三、流程統籌層（11）

| 檔名 | 中文名 | 作用 |
|---|---|---|
| `creative-intake` | **創意需求接單** | 把模糊需求問成明確簡報 |
| `taste-direction` | **美感方向把關** | 定調性與視覺品味 |
| `video-reference-analyst` | **參考影片拆解師** | 你貼一支片，它拆成可執行計畫 |
| `voice-performance-director` | **配音表演導演** | 語氣、停頓、情緒指導 |
| `animation-runtime-selector` | **動畫引擎選擇器** | 決定走 Remotion 還是 HyperFrames |
| `bespoke-composition` | **客製合成設計** | 現成場景不夠用時自己寫 |
| `checkpoint-protocol` | **檢查點協定** | 何時停下來等你核可 |
| `reviewer` | **品質審查員** | 渲染後自我複查 |
| `capability-extension` | **能力擴充** | 加新工具 |
| `skill-creator` | **技能產生器** | 寫新的技能檔 |
| `onboarding` | **新手上路** | agent 第一次進專案先讀這份 |

---

## 四、核心技術層（6）

| 檔名 | 中文名 | 作用 |
|---|---|---|
| `remotion` | **Remotion 渲染引擎** | React 路線，預設 |
| `hyperframes` | **HyperFrames 渲染引擎** | HTML/CSS/GSAP 路線 |
| `ffmpeg` | **FFmpeg 編碼後製** | 編碼、混音、字幕燒錄 |
| `color-grading` | **調色** | 統一不同來源素材的色調 |
| `subtitle-sync` | **字幕對時** | 逐字級時間軸 |
| `whisperx` | **WhisperX 語音轉文字** | 轉錄與對齊 |

---

## 建議入門順序

做療癒／覺醒系內容的話，優先讀這五份：

1. **紀實蒙太奇**（`pipelines/documentary-montage`）— 用免費素材做真實影片，不是套圖
2. **說故事結構**（`creative/storytelling`）— 所有片子的地基
3. **水墨劇場**（`creative/ink-theater`）— 東方美學調性
4. **短影音敘事**（`creative/short-form`）— 社群發佈節奏
5. **聲音設計**（`creative/sound-design`）— 療癒系最吃這塊
