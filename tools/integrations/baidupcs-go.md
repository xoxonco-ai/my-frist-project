# BaiduPCS-Go

Command-line client for Baidu Netdisk (百度网盘), modeled after Linux shell file commands. Vendored in this repo at `BaiduPCS-Go/` (upstream: [qjfoidnh/BaiduPCS-Go](https://github.com/qjfoidnh/BaiduPCS-Go)).

## Capabilities

| Integration | Available | Notes |
|-------------|-----------|-------|
| API | - | No public REST API; the CLI wraps Baidu PCS endpoints internally |
| MCP | - | Not available |
| CLI | ✓ | Single static Go binary, all platforms (Windows/macOS/Linux/ARM) |
| SDK | - | Go packages importable from `github.com/qjfoidnh/BaiduPCS-Go/baidupcs` (unofficial) |

## Install / Build

Prebuilt binaries: [GitHub releases](https://github.com/qjfoidnh/BaiduPCS-Go/releases). Or build from the vendored source (Go 1.23+):

```bash
cd BaiduPCS-Go
go build -o BaiduPCS-Go .
```

Run with no arguments to enter an interactive shell with tab completion; or pass a command for one-shot use.

## Authentication

- **Type**: Baidu account session cookies (no OAuth, no API key)
- **Primary credential**: `BDUSS` cookie (plus optional `STOKEN` for transfer/share operations)
- **Login methods**:

```bash
BaiduPCS-Go login                          # interactive: paste full cookies or BDUSS
BaiduPCS-Go login -bduss=<BDUSS>           # direct BDUSS
BaiduPCS-Go login -cookies="BDUSS=...; STOKEN=...; ..."  # full cookie string
```

Get cookies from a logged-in browser session at pan.baidu.com (DevTools > Application > Cookies). Multiple accounts are supported (`su`, `loglist`, `logout`). Credentials are stored locally in `pcs_config.json` (location shown by `BaiduPCS-Go env`) — treat that file as a secret.

## Common Agent Operations

### Account and quota

```bash
BaiduPCS-Go who              # current account
BaiduPCS-Go quota            # storage used / total
BaiduPCS-Go loglist          # list logged-in accounts
BaiduPCS-Go su <uid>         # switch account
```

### Browse the netdisk

```bash
BaiduPCS-Go ls /apps          # list a directory (-l, --time, --size, --name, --asc/--desc)
BaiduPCS-Go tree --depth 2 /  # directory tree
BaiduPCS-Go cd /videos        # change working directory
BaiduPCS-Go pwd               # print working directory
BaiduPCS-Go meta <path>       # file/dir metadata (fs_id, md5, size)
BaiduPCS-Go search -r "report" /docs   # recursive filename search
```

### Download

```bash
BaiduPCS-Go download <netdisk-path> --saveto ./downloads
# alias: d. Key flags:
#   -p <n>       parallel connections per file
#   -l <n>       files downloaded concurrently
#   --ow         overwrite existing files
#   --retry <n>  retry count
#   --mtime      preserve file modification time
```

Supports wildcards, directories, and resume of interrupted downloads.

### Upload

```bash
BaiduPCS-Go upload <local-file-or-dir> <netdisk-dir>
# alias: u. Key flags:
#   -p <n>            parallel chunks
#   --policy skip|overwrite|rsync|fail   same-name handling
#   --norapid         skip rapid-upload (秒传) hash check
```

Max single file size 128 GB. Upload resume is no longer supported (API change in v4.x); downloads still resume.

### Save someone else's share link (transfer)

```bash
BaiduPCS-Go transfer "https://pan.baidu.com/s/xxxx" <extraction-code>
# or a link with the code appended: https://pan.baidu.com/s/xxxx?pwd=abcd
#   --download   download after saving
#   --collect    flatten into a single folder
```

### Share your files

```bash
BaiduPCS-Go share set -p abcd --period 7 <path>   # create share (password, expiry days)
BaiduPCS-Go share list                            # list active shares
BaiduPCS-Go share cancel <share_id>               # cancel a share
```

### Offline download (server-side fetch)

```bash
BaiduPCS-Go offlinedl add -path=/downloads "<http/ftp/magnet/ed2k-url>"
BaiduPCS-Go offlinedl list
BaiduPCS-Go offlinedl cancel <task_id>
```

### File management

```bash
BaiduPCS-Go mkdir /new-dir
BaiduPCS-Go rm <path>                 # goes to recycle bin (10-day retention)
BaiduPCS-Go cp <src> <dst>
BaiduPCS-Go mv <src> <dst>            # also renames
BaiduPCS-Go recycle list
BaiduPCS-Go recycle restore <fs_id>
BaiduPCS-Go recycle delete -all       # empty recycle bin (permanent)
```

### Configuration

```bash
BaiduPCS-Go config                    # show all settings
BaiduPCS-Go config set -max_parallel 8 -max_download_load 2
BaiduPCS-Go config set -savedir ./downloads
BaiduPCS-Go config set -proxy socks5://127.0.0.1:1080
BaiduPCS-Go config set -proxy_hostnames pan.baidu.com   # route only Baidu hosts via proxy
```

## Notes & Caveats

- Non-VIP accounts are speed-limited by Baidu server-side; the tool does not bypass official limits.
- Documentation and CLI output are primarily Chinese.
- Session cookies (BDUSS) grant full account access — never commit `pcs_config.json` or paste cookies into logs.
- Unofficial client: Baidu API changes can break features between releases (see upstream changelog).
