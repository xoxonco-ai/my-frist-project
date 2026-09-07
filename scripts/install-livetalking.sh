#!/usr/bin/env bash
# Install LiveTalking (https://github.com/lipku/LiveTalking) into ./LiveTalking
#
# Usage:
#   ./scripts/install-livetalking.sh          # CPU install (no GPU)
#   GPU=1 ./scripts/install-livetalking.sh    # CUDA install (requires NVIDIA GPU)
#   GPU=1 CUDA_VERSION=cu124 ./scripts/install-livetalking.sh  # other CUDA version
#
# Requirements: Python 3.10+, git, ffmpeg (apt-get install -y ffmpeg)

set -euo pipefail

REPO_URL="https://github.com/lipku/LiveTalking.git"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
TARGET_DIR="${TARGET_DIR:-$REPO_ROOT/LiveTalking}"

echo "==> Checking prerequisites"
command -v git >/dev/null || { echo "git is required"; exit 1; }
command -v python3 >/dev/null || { echo "python3 is required"; exit 1; }
python3 -c 'import sys; exit(0 if sys.version_info >= (3, 10) else 1)' || {
  echo "ERROR: Python 3.10 or higher is required."
  python3 --version
  exit 1
}
command -v ffmpeg >/dev/null || echo "WARNING: ffmpeg not found — install it with: apt-get install -y ffmpeg"

if [ ! -d "$TARGET_DIR" ]; then
  echo "==> Cloning LiveTalking"
  git clone --depth 1 "$REPO_URL" "$TARGET_DIR"
elif [ ! -d "$TARGET_DIR/.git" ]; then
  echo "ERROR: $TARGET_DIR exists but is not a git repository. Please remove or rename it and try again."
  exit 1
else
  echo "==> $TARGET_DIR already exists and is a git repository, skipping clone"
fi

cd "$TARGET_DIR"

echo "==> Creating virtual environment"
python3 -m venv venv || {
  echo "ERROR: Failed to create virtual environment."
  echo "On Debian/Ubuntu systems, you may need to install python3-venv:"
  echo "  sudo apt-get install -y python3-venv"
  exit 1
}
./venv/bin/pip install --upgrade pip -q

echo "==> Installing PyTorch"
if [ "${GPU:-0}" = "1" ]; then
  # Defaults to the CUDA 12.8 build, per the official README. Override via
  # CUDA_VERSION (e.g. CUDA_VERSION=cu124); see
  # https://pytorch.org/get-started/previous-versions
  CUDA_VERSION="${CUDA_VERSION:-cu128}"
  ./venv/bin/pip install torch torchvision torchaudio --index-url "https://download.pytorch.org/whl/${CUDA_VERSION}"
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
