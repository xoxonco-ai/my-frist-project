#!/usr/bin/env bash
# Install LiveTalking (https://github.com/lipku/LiveTalking) into ./LiveTalking
#
# Usage:
#   ./scripts/install-livetalking.sh          # CPU install (no GPU)
#   GPU=1 ./scripts/install-livetalking.sh    # CUDA 12.8 install (requires NVIDIA GPU)
#
# Requirements: Python 3.10+, git, ffmpeg (apt-get install -y ffmpeg)

set -euo pipefail

REPO_URL="https://github.com/lipku/LiveTalking.git"
TARGET_DIR="${TARGET_DIR:-LiveTalking}"

echo "==> Checking prerequisites"
command -v git >/dev/null || { echo "git is required"; exit 1; }
command -v python3 >/dev/null || { echo "python3 is required"; exit 1; }
command -v ffmpeg >/dev/null || echo "WARNING: ffmpeg not found — install it with: apt-get install -y ffmpeg"

if [ ! -d "$TARGET_DIR" ]; then
  echo "==> Cloning LiveTalking"
  git clone --depth 1 "$REPO_URL" "$TARGET_DIR"
else
  echo "==> $TARGET_DIR already exists, skipping clone"
fi

cd "$TARGET_DIR"

echo "==> Creating virtual environment"
python3 -m venv venv
./venv/bin/pip install --upgrade pip -q

echo "==> Installing PyTorch"
if [ "${GPU:-0}" = "1" ]; then
  # CUDA 12.8 build, per the official README. For other CUDA versions see
  # https://pytorch.org/get-started/previous-versions
  ./venv/bin/pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu128
else
  # CPU build. If download.pytorch.org is unreachable, fall back to PyPI wheels.
  ./venv/bin/pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
    || ./venv/bin/pip install torch torchvision torchaudio
fi

echo "==> Installing LiveTalking requirements"
./venv/bin/pip install -r requirements.txt

echo
echo "==> Install complete."
echo
echo "Next steps (models must be downloaded manually):"
echo "  1. Download models from Google Drive:"
echo "     https://drive.google.com/drive/folders/1FOC_MD6wdogyyX_7V1d4NDIO7P9NlSAJ?usp=sharing"
echo "     (or Quark Cloud: https://pan.quark.cn/s/83a750323ef0)"
echo "  2. Copy wav2lip256.pth to $TARGET_DIR/models/wav2lip.pth"
echo "  3. Extract wav2lip256_avatar1.tar.gz into $TARGET_DIR/data/avatars/"
echo "  4. Start the server:"
echo "     cd $TARGET_DIR && ./venv/bin/python app.py --transport webrtc --model wav2lip --avatar_id wav2lip256_avatar1"
echo "  5. Open http://<server-ip>:8010/index.html in a browser"
