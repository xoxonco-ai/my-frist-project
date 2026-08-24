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
Use when user asks about 禅宗 doctrine or wants 慧能大师 Huineng's teaching backed by CBETA 经证 — 坛经, 金刚经, 维摩诘, 见性成佛, 顿悟, 无念无相无住, 定慧一体, 南宗禅, 机锋公案, 菩提本无树, 风动幡动, 本来无一物, 烦恼即菩提, 弘忍, 明心见性. Differs from /huineng-perspective (creator self-doubt, no citations) by being 教义 / 原典: every doctrinal claim carries a CBETA citation. Trigger is 求法 intent — "我还不够好、创作卡住了" goes to /huineng-perspective; "坛经怎么说顿悟、想听六祖讲法、这句偈什么意思" goes here.
```

### `huineng-perspective` 的新 description

```
以慧能（六祖）的禪宗操作系統鬆動創作卡關與自我懷疑，給療癒與覺醒系自媒體創作者使用。當使用者說「我還不夠好」「我還沒準備好」「要再修煉幾年才敢出來」「作品不夠完美」「靈感枯竭」「等我完全療癒才能幫人」「一直靠讚數和外部認可才覺得有價值」時啟用，用頓悟、本來無一物、無念為宗、定慧一體拆掉那個匱乏前提。與 /master-huineng 分工：要經義、原文、公案、CBETA 經證請用 /master-huineng；要拆自己的卡點留在這裡。觸發詞：我還不夠好、還沒準備好、完美主義癱瘓、靈感枯竭、內容不夠療癒、依賴讚數、慧能視角、六祖視角。
```

改完之後，兩者唯一還共用的字面是「慧能」「六祖」——加上「視角」二字即可分流。

---

## 2. 中觀二連

`master-nagarjuna` 與 `master-kumarajiva` 的描述幾乎逐字重疊：中观、空、般若、八不、中道、缘起性空、大智度论、十二门论。

龍樹是**作者**，羅什是**譯者兼判教者**，但現在的觸發詞看不出這個差別。

- **`master-nagarjuna` 保留**：中论、回诤论、二谛、世俗谛、第一义谛、八不中道、戏论、毕竟空、离四句、破自性、龙树
- **`master-kumarajiva` 改主打**：法华经、金刚经、维摩诘、一佛乘、会三归一、火宅喻、方便品、不二法门、三论宗、译经、五种不翻、鸠摩罗什、罗什
- **兩邊都刪掉**單獨的「空」「中道」「般若」；`大智度论` 判給龍樹（論主），`十二门论`／`百论` 判給羅什（三論宗立宗依據）

---

## 3. 上座部三連

`master-ajahn-chah`／`master-mahasi-sayadaw`／`master-buddhaghosa` 共用：南传、上座部、四念处、毗婆舍那、戒定慧。其中「十六观智」「七清净」被 mahasi 與 buddhaghosa 同時宣告，「妄念太多」被 ajahn-chah 與 mahasi 同時宣告。

- **共用詞收進 `compare-masters`**，三個本尊都不再宣告泛稱
- `master-ajahn-chah` 只留：森林禅、巴蓬寺、杜多行、阿姜查、心的训练
- `master-mahasi-sayadaw` 只留：标记法、腹部起伏、缅甸内观、刹那定、行舍智、马哈希
- `master-buddhaghosa` 只留：清净道论、Visuddhimagga、四十业处、十遍 kasiṇa、阿毗达摩注释、大寺派、觉音
- 「十六观智」「七清净」歸 buddhaghosa（論典出處），mahasi 改用「密集禅修」「一小时一坐」等實修語彙
- 「妄念太多」是通用抱怨，兩邊都刪，交給 `compare-masters`

---

## 4. 藏傳三連

`master-tsongkhapa`／`master-atisha`／`master-milarepa` 共用：藏传、道次第、暇满、菩提心、缘起性空。

- `master-atisha` 守：三士道、菩提道灯论、七因果、自他相换、金洲大师、噶当、仲敦巴
- `master-tsongkhapa` 守：广论、应成中观、辨了不了义、格鲁、黄教、甘丹、三主要道
- `master-milarepa` 本來就分得開（拙火、道歌、那洛六法、玛尔巴、噶举），維持原狀
- 「藏传」「暇满」「菩提心」三個泛稱從三者移除，交給 `compare-masters` 與 `master-curriculum`

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
