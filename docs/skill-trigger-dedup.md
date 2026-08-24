# Skill 觸發詞去重方案

盤點日期：2026-08-24　·　範圍：帳號同步的 50 個 skill

盤點結果：**沒有任何兩個 skill 同名**。使用者感受到的「重複」全部發生在 `description` 的觸發詞層——同一句話同時符合好幾個 skill 的觸發條件，於是每次叫出來的都不一樣。

下面每一節都可以直接複製貼上取代現有的 `description` 欄位。

---

## 1. 慧能（最高優先）

`master-huineng` 與 `huineng-perspective` 是同一位人物的兩個 skill，共用了 **10 個以上**觸發詞：慧能、六祖、頓悟、見性、自性、本來面目、無念、無相、無住、禪宗、菩提本無樹、不立文字、直指人心、見性成佛。

### 不要合併

兩者做的是不同的事：

| | `master-huineng` | `huineng-perspective` |
|---|---|---|
| 性質 | 祖師講法，帶 CBETA 經證鐵律 | 創作者認知框架 |
| 附屬檔 | `sources/` `references/` `tests/` `meta.json` | 無，單檔 |
| 語言 | 簡體 | 繁體 |
| 硬性規則 | 每個教義斷言必附 `【《》，T48n2008】` | 7 個心智模型各帶局限性 |
| 使用時機 | 想弄懂經義、讀原文、聽祖師開示 | 卡在「我還不夠好」「還沒準備好」 |

合併會毀掉其中一邊。正確做法是把**觸發軸線從詞彙改成意圖**，沿用 repo 既有的 `compare-masters` / `master-debate` / `master-curriculum` 三者互指的寫法。

### `master-huineng` 的新 description

```
Use when user asks about 禅宗 doctrine or wants 慧能大师 Huineng's teaching backed by CBETA 经证 — 坛经, 应无所住而生其心, 见性成佛, 顿悟, 无念无相无住, 定慧一体, 南宗禅, 机锋公案, 菩提本无树, 风动幡动, 本来无一物, 烦恼即菩提, 弘忍, 明心见性, 六祖. Differs from /huineng-perspective (creator self-doubt, no citations) by being 教义 / 原典: every doctrinal claim carries a CBETA citation; and from /master-kumarajiva by claiming only 坛经 — the 金刚经 / 维摩诘经 texts themselves belong there. Trigger is 求法 intent — "我还不够好、创作卡住了" goes to /huineng-perspective; "金刚经罗什怎么译的、维摩诘经讲什么" goes to /master-kumarajiva; "坛经怎么说顿悟、想听六祖讲法、这句偈什么意思" goes here.
```

### `huineng-perspective` 的新 description

```
以慧能（六祖）的禪宗操作系統鬆動創作卡關與自我懷疑，給療癒與覺醒系自媒體創作者使用。當使用者說「我還不夠好」「我還沒準備好」「要再修煉幾年才敢出來」「作品不夠完美」「靈感枯竭」「等我完全療癒才能幫人」「一直靠讚數和外部認可才覺得有價值」時啟用，用頓悟、本來無一物、無念為宗、定慧一體拆掉那個匱乏前提。與 /master-huineng 分工：要經義、原文、公案、CBETA 經證請用 /master-huineng；要拆自己的卡點留在這裡。觸發詞：我還不夠好、還沒準備好、完美主義癱瘓、靈感枯竭、內容不夠療癒、依賴讚數、慧能視角、六祖視角。
```

改完之後，兩者唯一還共用的字面是「慧能」「六祖」——加上「視角」二字即可分流。

---

## 2. 中觀二連

`master-nagarjuna` 與 `master-kumarajiva` 的描述幾乎逐字重疊：中观、空、般若、八不、中道、缘起性空、大智度论、十二门论。

分工軸線：龍樹是**論主**（造論的人），羅什是**譯者兼判教者**（把這批論帶進漢地、並判釋法華一乘的人）。

> **勘誤**：本文件初版曾把 `五种不翻` 列給羅什，這是錯的——五種不翻是**玄奘**的譯經原則，`master-xuanzang` 已正確宣告。羅什的譯經標誌是「意譯」與《高僧傳》裡「嚼飯與人」那句。

### `master-nagarjuna` 的新 description

```
Use when user asks about Madhyamaka source-text argument or wants teaching in 龙树菩萨 Nāgārjuna's voice — 中论, 回诤论, 宝鬘论, 大智度论, 二谛, 世俗谛, 第一义谛, 八不中道, 戏论, 毕竟空, 不可得, 如幻, 离四句, 破自性, 涅槃与世间不二, 难行道易行道, 龙树. Differs from /master-kumarajiva (译经与判教) by being 论主 / 造论: the arguments as Nāgārjuna built them. Trigger is 破自性 intent — "法华经为什么说会三归一" goes to /master-kumarajiva; "八不中道怎么破自性、二谛怎么分" goes here. Bare 空 / 中道 / 般若 alone goes to /compare-masters.
```

### `master-kumarajiva` 的新 description

```
Use when user asks about 鸠摩罗什 Kumārajīva's translations and 三论宗 judgement of the teachings, or wants teaching in his voice — 法华经, 金刚经, 维摩诘经, 阿弥陀经, 一佛乘, 会三归一, 火宅喻, 方便品, 不二法门, 实相, 三论宗, 百论, 十二门论, 长安译场, 意译, 嚼饭与人, 鸠摩罗什, 罗什. Differs from /master-nagarjuna (论主 / 造论) by being 译者与判教者: how these texts entered Chinese and how the three vehicles resolve into one. Trigger is 经典与译传 intent — "八不中道怎么破自性" goes to /master-nagarjuna; "法华经为什么说会三归一、维摩诘的不二法门" goes here. Bare 空 / 中道 / 般若 alone goes to /compare-masters.
```

改完後兩者不再共用任何字面。`大智度论` 判給龍樹（論主），`百论`／`十二门论` 判給羅什（三論宗立宗依據）。

---

## 3. 上座部三連

`master-ajahn-chah`／`master-mahasi-sayadaw`／`master-buddhaghosa` 共用：南传、上座部、四念处、毗婆舍那、戒定慧。其中「十六观智」「七清净」被 mahasi 與 buddhaghosa 同時宣告，「妄念太多」被 ajahn-chah 與 mahasi 同時宣告。

分工軸線：覺音是**論典出處**（定義在哪、次第怎麼排），馬哈希是**可執行的技術指令**（現在標什麼），阿姜查是**森林口傳譬喻**（日常怎麼過）。

### `master-ajahn-chah` 的新 description

```
Use when user asks about 泰国森林禅林派 practice or wants teaching in 阿姜查 Ajahn Chah's voice — 森林禅, 巴蓬寺, 杜多行 dhutaṅga, 头陀支, 心的训练, 与法同住, 日常劳作即修行, 宁静的森林水池, 阿姜查, Ajahn Chah, 阿姜苏美多. Differs from /master-mahasi-sayadaw (标记法的技术指令) and /master-buddhaghosa (清净道论的论典体系) by being 譬喻式的森林口传: everyday images, not a numbered method. Trigger is 森林传承 intent — "标记法怎么标、腹部起伏" goes to /master-mahasi-sayadaw; "七清净出自哪里" goes to /master-buddhaghosa; "森林里怎么过日子、心怎么训练" goes here. Bare 南传 / 上座部 / 四念处 / 毗婆舍那 / 妄念太多 alone goes to /compare-masters.
```

### `master-mahasi-sayadaw` 的新 description

```
Use when user asks how to actually run 缅甸内观, or wants teaching in 马哈希尊者 Mahāsi Sayādaw's voice — 标记法, Noting Method, 腹部起伏, 密集禅修, 经行, 刹那定, 行舍智, 清净智论, Mahasi Sasana Yeiktha, 马哈希, Mahasi, Sayadaw. Differs from /master-buddhaghosa (论典体系与出处) and /master-ajahn-chah (森林口传譬喻) by being 可执行的技术指令: what to note, when, how fast. Trigger is 实修操作 intent — "七清净、十六观智出自哪里" goes to /master-buddhaghosa; "森林里怎么过日子" goes to /master-ajahn-chah; "坐下来第一步标什么、腹部起伏怎么观" goes here. Bare 南传 / 上座部 / 四念处 / 毗婆舍那 / 妄念太多 alone goes to /compare-masters.
```

### `master-buddhaghosa` 的新 description

```
Use when user asks where a Theravāda stage is defined or how the map fits together, or wants teaching in 觉音尊者 Buddhaghosa's voice — 清净道论, Visuddhimagga, 四十种业处 kammaṭṭhāna, 十遍 kasiṇa, 七清净, 十六观智, 阿毗达摩注释, 尼柯耶注释, 大寺派 Mahāvihāra, 缘起十二支, 觉音, Buddhaghosa. Differs from /master-mahasi-sayadaw (可执行的标记技术) and /master-ajahn-chah (森林口传譬喻) by being 论典 / 体系: definitions and sequence, with sources. Trigger is 出处与次第 intent — "坐下来第一步标什么" goes to /master-mahasi-sayadaw; "七清净有哪七个、十六观智的次序、某业处出自哪一品" goes here. Bare 南传 / 上座部 / 戒定慧 alone goes to /compare-masters.
```

「妄念太多」是通用抱怨，三者都刪，交給 `compare-masters`。

---

## 4. 藏傳三連

`master-tsongkhapa`／`master-atisha`／`master-milarepa` 共用：藏传、道次第、暇满、菩提心、缘起性空。

分工軸線：阿底峽是**道次第之根**（《菩提道燈論》這部根本論），宗喀巴是**廣釋與抉擇**（《廣論》與應成正見），米拉日巴是**實證與證道歌**（身心上發生什麼事）。

### `master-atisha` 的新 description

```
Use when user asks about 噶当派 foundations or wants teaching in 阿底峡尊者 Atiśa's voice — 菩提道灯论 Bodhipathapradīpa, 三士道, 七因果, 自他相换, 依止善知识, 业果, 金洲大师 Serlingpa, 噶当六论, 仲敦巴 Dromtönpa, 热振寺, 藏地后弘期, 阿底峡, 觉沃杰, Jowo Je. Differs from /master-tsongkhapa (广论与应成中观的广释) by being 道次第之根: the root text the later lamrim expands, plus the bodhicitta trainings. Trigger is 根本论 intent — "广论怎么讲止观、应成怎么破" goes to /master-tsongkhapa; "三士道分哪三士、七因果怎么修" goes here. Bare 藏传 / 道次第 / 暇满 / 菩提心 alone goes to /compare-masters.
```

### `master-tsongkhapa` 的新 description

```
Use when user asks about 格鲁派 doctrine or wants teaching in 宗喀巴大师 Tsongkhapa's voice — 菩提道次第广论 lam rim chen mo, 密宗道次第广论, 三主要道, 应成中观 Prāsaṅgika, 辨了不了义, 入中论善显密意疏, 月称, 因明, 甘丹寺, 格鲁, 黄教, 宗喀巴, 杰仁波切, Je Rinpoche. Differs from /master-atisha (菩提道灯论这个根) by being 广释与抉择: the expanded treatise and the Prāsaṅgika settling of view. Trigger is 抉择正见 intent — "三士道分哪三士、七因果" goes to /master-atisha; "广论怎么讲止观、应成与自续差在哪、了义不了义怎么分" goes here. Bare 藏传 / 道次第 / 暇满 / 缘起性空 alone goes to /compare-masters.
```

### `master-milarepa` 的新 description

```
Use when user asks about 噶举派 yogic practice or wants teaching in 米拉日巴尊者 Milarepa's voice — 大手印 phyag chen, 拙火 tummo, 那洛六法, 中有成就法, 道歌 mgur, 十万歌集, 玛尔巴 Marpa, 上师瑜伽, 山洞苦行, 闭关, 气脉明点, 觉受 nyams, 本觉 rig pa, 噶举, 白教, 米拉日巴, 密勒日巴, Milarepa. Differs from /master-atisha and /master-tsongkhapa (both 教理次第) by being 实证与证道歌: what the practice does to body and mind, sung rather than argued. Trigger is 苦行实修 intent — "三士道、广论次第" goes to those two; "拙火怎么起、闭关怎么熬、道歌里说什么" goes here. Bare 藏传 / 暇满 / 菩提心 alone goes to /compare-masters.
```

「藏传」「暇满」「菩提心」「道次第」四個泛稱從三者全部移除，交給 `compare-masters` 與 `master-curriculum`。

---

## 5. 單字觸發詞全面禁令

這是誤觸最大的來源。以下單字目前被多個 skill 同時宣告：

| 單字 | 目前宣告者 |
|---|---|
| 放下 | `master-ajahn-chah`、`watts-perspective`、`zhuangzi-perspective` |
| 當下 | `tolle-perspective`、`watts-perspective` |
| 自性 | `master-huineng`、`huineng-perspective` |
| 無為 | `laozi-perspective`、`zhuangzi-perspective` |
| 覺醒 | `campbell-perspective`、`tolle-perspective` |
| 原型 | `jung-perspective`、`hillman-perspective`、`campbell-perspective` |
| 比較 | `krishnamurti-perspective`、`compare-masters` |

**規則：任何 skill 的 description 都不得宣告通用單字。**一律改成帶語境的整句，例如：

- ✗ `放下` → ✓ `放不下一段關係`、`一直想控制結果`
- ✗ `當下` → ✓ `一直活在對未來的焦慮裡`
- ✗ `原型` → ✓ `夢裡反覆出現同一個形象`（jung）、`症狀想告訴我什麼`（hillman）、`我的人生階段對應哪一段旅程`（campbell）

---

## 6. 做頁面／做設計有七個在搶

`canvas-design`、`theme-factory`、`brand-guidelines`、`web-artifacts-builder`（帳號同步）＋ `design`、`artifact-design`、`dataviz`（Claude Code 內建）全部落在同一個語意區。

內建那三個會自動接手，不需要處理。帳號端建議二選一：

- 要輸出 **PNG／PDF 靜態稿** → 留 `canvas-design`
- 要輸出 **HTML／Artifact 網頁** → 留 `web-artifacts-builder`，`theme-factory` 併入它的配色章節

---

## 7. `huashu-nuwa` 曾是空殼

原本的 `SKILL.md` 只有 8 行純 frontmatter，沒有任何內容——會被「造skill」「女娲」觸發然後給不出指示。已補上完整內容（`skills/huashu-nuwa/SKILL.md`），並在 description 末尾加上與 `skill-creator` 的分工：

> 只做人物视角 skill（`*-perspective` / `master-*`）；通用 skill 的创建、评测与描述调优交给 `skill-creator`。

---

## 套用方式

這些 skill 存在 claude.ai 帳號的 skill 區（`~/.claude/skills/synced/` 只是同步下來的本機副本，直接改會被下次同步覆蓋）。

要讓修改生效，在 claude.ai 的 skill 編輯介面逐一貼上新的 description，或在原始編寫的專案裡改完重新同步。
