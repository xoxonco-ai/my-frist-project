#!/usr/bin/env python3
"""從你的 90 天排程表 CSV 抽出所有 CTA 關鍵字，產生 keyword_map 骨架。

你的排程表有「CTA」欄，內容像「留言『入口』拿書寫練習」。
這支程式把引號裡的關鍵字全撈出來，省得你 90 天一個個手打。

用法：
    python extract_keywords.py 浮生矩陣_90天發文排程表_完整版.csv > keyword_map.new.csv
之後把 worksheet_url 一欄填上你的練習連結即可。
"""
import csv
import re
import sys

# 抓中文引號「」或直角引號內的關鍵字
KW_RE = re.compile(r"[「『]([^」』]{1,12})[」』]")


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit("用法：python extract_keywords.py <排程表.csv>")

    seen = {}  # keyword -> first note
    with open(sys.argv[1], encoding="utf-8-sig") as fh:
        for row in csv.DictReader(fh):
            cta = row.get("CTA") or row.get("cta") or ""
            title = row.get("標題") or row.get("Day") or ""
            for kw in KW_RE.findall(cta):
                kw = kw.strip()
                # 過濾明顯不是關鍵字的（拿書寫練習之類）
                if kw and kw not in seen and "練習" not in kw:
                    seen[kw] = title

    w = csv.writer(sys.stdout)
    w.writerow(["keyword", "worksheet_url", "note"])
    for kw, note in seen.items():
        w.writerow([kw, "https://你的網域/練習/" + kw, note])
    print(f"# 共抽出 {len(seen)} 個關鍵字，請填 worksheet_url", file=sys.stderr)


if __name__ == "__main__":
    main()
