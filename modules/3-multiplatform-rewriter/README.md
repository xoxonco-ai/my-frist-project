# 模組 3｜一稿多平台改寫工具

一篇療癒/覺醒內容 → 自動改寫成 **IG / Threads / Facebook / 小紅書 / 抖音** 各自的語感。
用 Anthropic 官方 API 產生，**你手動貼出** —— 不碰自動發文，帳號 100% 安全。

## 安裝

```bash
# 在專案根目錄
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env      # 填入 ANTHROPIC_API_KEY
```

## 使用

```bash
cd modules/3-multiplatform-rewriter

# 方式一：直接給內容
python rewrite.py "放下不是努力放下，放下是停止抓住。當你不再用力，事情反而鬆開了。"

# 方式二：從檔案讀
python rewrite.py --file draft.txt

# 只要特定平台
python rewrite.py --file draft.txt --platforms ig,threads,xhs
```

## 平台代號

| 代號 | 平台 | 輸出風格 |
|------|------|----------|
| `ig` | Instagram | 鉤子開頭 + 收藏型金句 + 精準 hashtag |
| `threads` | Threads | 一句戳心 + 開放問題催回覆 |
| `fb` | Facebook | 第一人稱故事 + 催長留言 |
| `xhs` | 小紅書 | 大字報標題 + 搜尋關鍵字 + 分點催收藏 |
| `douyin` | 抖音 | 口播腳本（分秒分段 + 字幕重點） |

## 安全設計

- 內建紅線：不做醫療療效宣稱；小紅書/抖音版本不導流站外。
- 只產出文字草稿，發布由你決定 —— 演算法看到的是「真人經營」，最安全。
