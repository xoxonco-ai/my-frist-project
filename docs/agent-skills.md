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

## 共用參考檔（`references/`）

`accessibility-checklist.md`、`definition-of-done.md`、`observability-checklist.md`、`orchestration-patterns.md`、`performance-checklist.md`、`security-checklist.md`、`testing-patterns.md`

## 更新方式

上游更新時重新複製即可（覆蓋同名資料夾，保留 frontmatter 的 `metadata` 出處欄位）：

```bash
npx skills add addyosmani/agent-skills
```

或從上游 repo 複製 `skills/<name>/` 與 `references/*.md` 覆蓋。
