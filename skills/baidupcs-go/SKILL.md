---
name: baidupcs-go
description: When the user wants to work with Baidu Netdisk (百度网盘) from the command line using the BaiduPCS-Go CLI. Use when the user says "Baidu Netdisk," "百度网盘," "BaiduPCS," "download from Baidu pan," "upload to Baidu cloud," "save a pan.baidu.com share link," or asks to transfer, share, or manage files on Baidu's cloud storage. For general marketing tool integrations, see the tools registry instead.
metadata:
  version: 1.0.0
---

# BaiduPCS-Go: Baidu Netdisk CLI

You are an expert operator of BaiduPCS-Go, a command-line client for Baidu Netdisk (百度网盘) that mimics Linux shell file commands. The full source is vendored in this repository at `BaiduPCS-Go/`, and the detailed integration guide is at `tools/integrations/baidupcs-go.md`.

## Initial Assessment

Before running commands, confirm:

1. **Binary availability** - Is `BaiduPCS-Go` on PATH? If not, download a [release binary](https://github.com/qjfoidnh/BaiduPCS-Go/releases) or build from the vendored source: `cd BaiduPCS-Go && go build -o BaiduPCS-Go .` (requires Go 1.23+).
2. **Login state** - Run `BaiduPCS-Go who`. If not logged in, the user must supply their `BDUSS` cookie (and `STOKEN` for transfer/share operations) from a logged-in pan.baidu.com browser session.
3. **What operation** - download, upload, save a share link (transfer), create a share, offline download, or file management.

## Authentication

```bash
BaiduPCS-Go login -bduss=<BDUSS>
BaiduPCS-Go login -cookies="BDUSS=...; STOKEN=...;"
```

**Security rules:**

- Never echo, log, or commit BDUSS/STOKEN values — they grant full account access.
- Credentials persist in `pcs_config.json` (find it with `BaiduPCS-Go env`); treat it as a secret file.
- Ask the user to paste credentials directly; do not fetch them from files without permission.

## Core Workflows

### Download files

```bash
BaiduPCS-Go ls /path/on/netdisk
BaiduPCS-Go download /path/on/netdisk/file.zip --saveto ./downloads -p 4
```

- `-p <n>` parallel connections per file, `-l <n>` concurrent files, `--ow` overwrite, `--mtime` keep modification times.
- Downloads resume automatically if interrupted.
- Keep parallel counts modest (≤ 12) — higher values trigger server-side throttling.

### Upload files

```bash
BaiduPCS-Go upload ./local-file.zip /destination/dir --policy rsync
```

- `--policy skip|overwrite|rsync|fail` controls same-name handling; `--norapid` skips the rapid-upload hash check.
- Max single file: 128 GB. Upload resume is not supported in v4.x — for huge files over unstable links, warn the user.

### Save a shared link to the user's netdisk (transfer)

```bash
BaiduPCS-Go transfer "https://pan.baidu.com/s/xxxx?pwd=abcd"
BaiduPCS-Go transfer "https://pan.baidu.com/s/xxxx" abcd   # code as second arg
```

Add `--download` to download immediately after saving. Requires `STOKEN` in the login cookies.

### Create / manage shares

```bash
BaiduPCS-Go share set -p abcd --period 7 /path/to/share
BaiduPCS-Go share list
BaiduPCS-Go share cancel <share_id>
```

### Offline download (Baidu fetches server-side)

```bash
BaiduPCS-Go offlinedl add -path=/downloads "<http|ftp|magnet|ed2k url>"
BaiduPCS-Go offlinedl list
```

### File management

```bash
BaiduPCS-Go mkdir /new-dir
BaiduPCS-Go cp /src /dst
BaiduPCS-Go mv /old-name /new-name
BaiduPCS-Go rm /path            # recoverable from recycle bin for 10 days
BaiduPCS-Go recycle list
BaiduPCS-Go recycle restore <fs_id>
```

**Confirm with the user before** `rm`, `recycle delete`, `share cancel`, or anything that removes data. `recycle delete -all` is permanent.

## Performance Tuning

```bash
BaiduPCS-Go config set -max_parallel 8        # download connections
BaiduPCS-Go config set -max_download_load 2   # concurrent downloading files
BaiduPCS-Go config set -savedir ./downloads   # default download location
BaiduPCS-Go config set -proxy socks5://host:port
```

Non-VIP accounts are speed-limited server-side; no client setting bypasses official limits. For users outside China with upload problems, `config set -proxy_hostnames pan.baidu.com` routes only Baidu traffic through a China-reachable proxy.

## Troubleshooting

- **"param error" or sudden API failures** - Baidu changes endpoints without notice; check for a newer release (`BaiduPCS-Go update`) or upstream issues.
- **Transfer fails** - verify the login included `STOKEN`, the link is valid, and the extraction code is correct.
- **Slow downloads** - reduce parallel counts first (over-parallelizing triggers throttling), then check VIP status.
- **Chinese output** - the CLI's messages are primarily Chinese; translate key output for the user when relevant.
