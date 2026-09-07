#!/bin/bash

# Install OpenMontage (https://github.com/calesthio/OpenMontage) and apply the
# fixes a sandboxed Claude Code container needs before its renderer will run.
#
# Idempotent — safe to re-run. Each step is skipped if already satisfied.
#
#   ./setup-openmontage.sh              # install into ~/OpenMontage
#   OM_DIR=/path/to/dir ./setup-openmontage.sh
#
# Sandbox fixes applied (steps 4-6). Upstream `make setup` alone is not enough
# in a container behind the agent egress proxy:
#   - Chrome does not trust the proxy CA, so webfont fetches fail with
#     ERR_CERT_AUTHORITY_INVALID and Remotion aborts with a NetworkError.
#   - remotion.media is not in the egress allowlist, so Remotion cannot
#     auto-download its Chrome Headless Shell (403).
#
# Known limitation: huggingface.co is also blocked, so Piper voice models
# cannot be downloaded. Free offline narration is unavailable in that case —
# use a cloud TTS provider (needs an API key in .env), or get huggingface.co
# added to the egress allowlist.

set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

OM_DIR="${OM_DIR:-$HOME/OpenMontage}"
OM_REPO="https://github.com/calesthio/OpenMontage.git"
CA_BUNDLE="/root/.ccr/ca-bundle.crt"
NSSDB="$HOME/.pki/nssdb"

echo "🎬 OpenMontage Setup"
echo "===================="
echo ""
echo "Target: $OM_DIR"
echo ""

step() { echo -e "${BLUE}==> $1${NC}"; }
ok()   { echo -e "    ${GREEN}✓${NC} $1"; }
skip() { echo -e "    ${YELLOW}—${NC} $1"; }
warn() { echo -e "    ${YELLOW}!${NC} $1"; }
die()  { echo -e "${RED}✗ $1${NC}" >&2; exit 1; }

# ---- 1. Clone ----------------------------------------------------------------
step "Cloning OpenMontage"
if [ -d "$OM_DIR/.git" ]; then
  skip "already present at $OM_DIR"
else
  git clone --depth 1 "$OM_REPO" "$OM_DIR" || die "clone failed"
  ok "cloned"
fi
cd "$OM_DIR"

# ---- 2. FFmpeg ---------------------------------------------------------------
step "Checking FFmpeg"
if command -v ffmpeg >/dev/null 2>&1 && command -v ffprobe >/dev/null 2>&1; then
  skip "$(ffmpeg -version | head -1 | cut -d' ' -f1-3)"
else
  if command -v apt-get >/dev/null 2>&1; then
    apt-get update -qq && apt-get install -y -qq ffmpeg || die "ffmpeg install failed"
    ok "installed via apt"
  else
    die "ffmpeg not found and apt-get unavailable — install it manually"
  fi
fi

# ---- 3. Upstream setup -------------------------------------------------------
# venv + pip deps + Remotion npm install + Piper + HyperFrames npx cache + .env
step "Running upstream 'make setup'"
make setup || die "make setup failed"
ok "done"

# ---- 4. Trust the agent proxy CA in Chrome's NSS store -----------------------
# Chrome on Linux reads user-added trust anchors from the NSS db, not from
# /usr/local/share/ca-certificates. Without this, every https asset the
# composition loads (Google Fonts, remote images) fails to fetch.
step "Trusting agent proxy CA in Chrome's NSS store"
if [ ! -f "$CA_BUNDLE" ]; then
  skip "no proxy CA at $CA_BUNDLE — not behind the agent proxy"
elif ! command -v certutil >/dev/null 2>&1 && ! command -v apt-get >/dev/null 2>&1; then
  warn "certutil unavailable (install libnss3-tools) — renders may fail on webfonts"
else
  command -v certutil >/dev/null 2>&1 || apt-get install -y -qq libnss3-tools
  mkdir -p "$NSSDB"
  # Only create the db when it is genuinely absent. `certutil -N` against an
  # existing store does not fail fast — it spins re-deriving the key db and
  # never returns.
  [ -f "$NSSDB/cert9.db" ] || certutil -d "sql:$NSSDB" -N --empty-password
  if certutil -L -d "sql:$NSSDB" 2>/dev/null | grep -q '^ccr-proxy-0'; then
    skip "already imported"
  else
    tmp="$(mktemp -d)"
    trap 'rm -rf "$tmp"' EXIT
    ( cd "$tmp" && csplit -z -f ca- -b '%03d.pem' "$CA_BUNDLE" \
        '/-----BEGIN CERTIFICATE-----/' '{*}' >/dev/null )
    n=0
    for f in "$tmp"/ca-*.pem; do
      certutil -d "sql:$NSSDB" -A -t "C,," -n "ccr-proxy-$n" -i "$f" && n=$((n + 1))
    done
    ok "imported $n certificates"
  fi
fi

# ---- 5. Headless Chrome for HyperFrames --------------------------------------
step "Ensuring headless Chrome for HyperFrames"
npx --yes hyperframes browser ensure >/dev/null 2>&1 \
  && ok "ready" \
  || warn "could not fetch headless shell — HyperFrames renders will fail"

# ---- 6. Point Remotion at a Chrome already on disk ---------------------------
# Remotion has no env var for this: only the --browser-executable CLI flag or
# a config file. All three call sites (video_compose.py,
# remotion_caption_burn.py, render_demo.py) run `npx remotion render` with
# remotion-composer as cwd, so one config file covers them all.
step "Configuring Remotion browser executable"
CONFIG="$OM_DIR/remotion-composer/remotion.config.ts"
if [ -f "$CONFIG" ]; then
  skip "remotion.config.ts already exists"
else
  cat > "$CONFIG" <<'EOF'
// Local environment override (not part of upstream OpenMontage).
//
// This sandbox blocks remotion.media, so Remotion cannot auto-download its
// Chrome Headless Shell. Point it at a Chromium that is already on disk.
// Order: OPENMONTAGE_CHROME env var -> hyperframes' headless shell ->
// Playwright's bundled Chromium. If none exist, fall through to Remotion's
// default behaviour.
import {Config} from '@remotion/cli/config';
import {existsSync, readdirSync} from 'node:fs';
import {join} from 'node:path';

const hyperframesShell = (): string | null => {
  const base = '/root/.cache/hyperframes/chrome/chrome-headless-shell';
  if (!existsSync(base)) return null;
  for (const dir of readdirSync(base)) {
    const bin = join(base, dir, 'chrome-headless-shell-linux64', 'chrome-headless-shell');
    if (existsSync(bin)) return bin;
  }
  return null;
};

const candidates = [
  process.env.OPENMONTAGE_CHROME,
  hyperframesShell(),
  '/opt/pw-browsers/chromium_headless_shell-1194/chrome-linux/headless_shell',
  '/opt/pw-browsers/chromium/chrome-linux/chrome',
].filter((p): p is string => Boolean(p) && existsSync(p as string));

if (candidates.length > 0) {
  Config.setBrowserExecutable(candidates[0]);
}
EOF
  ok "wrote remotion-composer/remotion.config.ts"
fi

# Keep the local-only config out of `git status` in the OpenMontage clone.
if ! grep -qF 'remotion-composer/remotion.config.ts' .git/info/exclude 2>/dev/null; then
  printf '\n# local sandbox fix — not for upstream\nremotion-composer/remotion.config.ts\n' \
    >> .git/info/exclude
fi

# ---- Done --------------------------------------------------------------------
echo ""
echo -e "${GREEN}✓ OpenMontage is installed.${NC}"
echo ""
echo "  cd $OM_DIR"
echo "  source .venv/bin/activate    # required: piper_tts is discovered via PATH"
echo ""
echo "  make demo      # render three zero-key sample videos"
echo "  make test      # run the test suite"
echo ""
echo "  Add API keys to $OM_DIR/.env to unlock cloud image/video/TTS providers."
