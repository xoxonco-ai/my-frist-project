# Addy Osmani Agent Skills 工程技能索引

來源：[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)（MIT，作者 Addy Osmani，上游 commit `2686b62`）。

25 個軟體工程流程技能已安裝到 `skills/`，資料夾名稱與上游相同（等於 frontmatter 的 `name`）。內容與上游一致，只在 frontmatter 補上 `license` 與 `metadata`（作者、來源、上游資料夾、上游 commit）以保留出處。

上游多個技能以 `../../references/*.md` 引用共用檢查清單，因此這些檔案一併原樣放在 repo 根目錄的 `references/`，相對路徑可直接解析。

## 開發生命週期

```
DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP
```

| 階段 | Skill | 用途 |
|---|---|---|
| 入口 | `using-agent-skills` | 決定當下該用哪個技能 / 工作流程 |
| 定義 | `interview-me` | 一次問一題，釐清真正需求 |
| 定義 | `idea-refine` | 把粗略想法發散、收斂成可執行概念 |
| 定義 | `spec-driven-development` | 先寫規格再寫程式 |
| 定義 | `constraint-driven-development` | 把品質底線寫成合約，防止被悄悄降低 |
| 規劃 | `planning-and-task-breakdown` | 把規格拆成有序、可驗證的小任務 |
| 規劃 | `context-engineering` | 設定 / 修復代理的上下文 |
| 實作 | `incremental-implementation` | 一次一個薄切片，逐步交付 |
| 實作 | `test-driven-development` | 紅→綠→重構 |
| 實作 | `source-driven-development` | 以官方文件為依據做實作決策 |
| 實作 | `api-and-interface-design` | 穩定的 API 與模組邊界設計 |
| 實作 | `frontend-ui-engineering` | 可及性、響應式的正式前端 UI |
| 驗證 | `debugging-and-error-recovery` | 系統化找根因 |
| 驗證 | `browser-testing-with-devtools` | 透過 Chrome DevTools MCP 在真實瀏覽器測試 |
| 審查 | `code-review-and-quality` | 合併前多軸向程式碼審查 |
| 審查 | `doubt-driven-development` | 以全新上下文對重要決策做對抗式審查 |
| 審查 | `code-simplification` | 不改行為的前提下簡化程式碼 |
| 審查 | `security-and-hardening` | 安全強化與弱點稽核 |
| 審查 | `performance-optimization` | 前後端、查詢、資料庫效能優化 |
| 上線 | `shipping-and-launch` | 上線前檢查與發佈 |
| 上線 | `ci-cd-and-automation` | 建立 / 修改 CI/CD 管線 |
| 上線 | `observability-and-instrumentation` | 日誌、指標、追蹤 |
| 維運 | `git-workflow-and-versioning` | 分支、提交、版本流程 |
| 維運 | `documentation-and-adrs` | 架構決策紀錄（ADR）與文件 |
| 維運 | `deprecation-and-migration` | 棄用舊系統與遷移使用者 |

## 斜線指令與子代理

上游的 9 個斜線指令放在 `.claude/commands/`，4 個子代理（persona）放在 `.claude/agents/`。內容與上游 `2686b62` 一致，只把指令裡的外掛命名空間 `agent-skills:<skill>` 改成本 repo 的技能名稱 `` `<skill>` ``（本 repo 的技能沒有 `agent-skills:` 前綴）。

| 指令 | 做什麼 | 會用到 |
|---|---|---|
| `/spec` | 先寫規格再寫程式 | `spec-driven-development` |
| `/plan` | 拆成小而可驗證的任務 | `planning-and-task-breakdown` |
| `/build` | 一次一個切片：實作、測試、驗證、提交；`/build auto` 核准計畫後一次跑完 | `incremental-implementation` + `test-driven-development` |
| `/test` | TDD；修 bug 用 Prove-It 模式 | `test-driven-development` |
| `/constraints` | 訂定並強制專案品質底線（`CONSTRAINTS.md`） | `constraint-driven-development` |
| `/review` | 五軸向程式碼審查 | `code-review-and-quality` |
| `/webperf` | 網頁效能稽核 | 子代理 `web-performance-auditor` |
| `/code-simplify` | 不改行為的簡化 | `code-simplification` |
| `/ship` | 平行派出三個子代理審查後給出 go / no-go | `shipping-and-launch` + 子代理 `code-reviewer`、`security-auditor`、`test-engineer` |

> 若某個指令名稱與 Claude Code 內建指令相同（例如 `/review`、`/plan`），而輸入後跑的是內建功能，請改用對應的技能名稱，例如 `/code-review-and-quality`、`/planning-and-task-breakdown`。

## 共用參考檔（`references/`）

`accessibility-checklist.md`、`definition-of-done.md`、`observability-checklist.md`、`orchestration-patterns.md`、`performance-checklist.md`、`security-checklist.md`、`testing-patterns.md`

## 更新方式

上游更新時重新複製即可（覆蓋同名資料夾，保留 frontmatter 的 `metadata` 出處欄位）：

```bash
npx skills add addyosmani/agent-skills
```

或從上游 repo 複製 `skills/<name>/` 與 `references/*.md` 覆蓋；指令與子代理則複製上游 `.claude/commands/*.md` 到 `.claude/commands/`、`agents/*.md` 到 `.claude/agents/`，再把 `agent-skills:` 前綴拿掉。
