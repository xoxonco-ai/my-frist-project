# Remotion Agent Skills 影片技能索引

來源：[remotion-dev/skills](https://github.com/remotion-dev/skills)（作者 Remotion，版本 4.0.532，上游 commit `0b5db9d`）。

12 個 Remotion 技能已安裝到 `skills/`，資料夾名稱與上游相同（等於 frontmatter 的 `name`）。內容與上游一致，只在 frontmatter 補上 `license` 與 `metadata`（作者、版本、來源、上游資料夾、上游 commit），並把上游的頂層 `version` 欄位移入 `metadata.version`，以符合 Agent Skills 規格。

> **授權**：Remotion 採用 [Remotion License](https://remotion.dev/license)，個人與小型團隊可免費使用，一定規模以上的公司需購買授權。實際用 Remotion 產出影片前請先確認。

| Skill | 用途 |
|---|---|
| `remotion-best-practices` | 路由入口，涵蓋其他所有技能；不確定用哪個時先用它 |
| `remotion-create` | 建立新的 Remotion 專案或 composition |
| `remotion-markup` | Remotion React 標記：版面、動畫、字體、媒體、特效、時間軸 |
| `remotion-studio` | 啟動 Studio 預覽影片 |
| `remotion-render` | 輸出影片或靜態圖 |
| `remotion-captions` | 字幕轉錄、顯示與動畫 |
| `remotion-maps` | 地圖動畫 |
| `remotion-multimedia` | 用 Mediabunny 處理影音 |
| `remotion-interactivity` | 讓 Studio 能互動編輯的標記寫法 |
| `remotion-saas` | 用 Remotion 打造影片產生 App |
| `remotion-docs` | 查詢最新 Remotion 官方文件 |
| `remotion-upgrade` | 升級 Remotion 與相關套件 |

範例提示：`/remotion-create 幫唱片行做一支宣傳影片`
