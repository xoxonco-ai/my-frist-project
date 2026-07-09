#!/usr/bin/env bash
# Install Pixelle-Video (https://github.com/ATH-MaaS/Pixelle-Video)
# AI fully-automated short video engine: topic in, finished video out.
#
# Usage:
#   ./tools/setup/install-pixelle-video.sh [target-dir]
#
# Default target dir: $HOME/Pixelle-Video
# Requirements installed/checked by this script: git, uv, ffmpeg, Python >= 3.11

set -euo pipefail

REPO_URL="https://github.com/ATH-MaaS/Pixelle-Video.git"
TARGET_DIR="${1:-$HOME/Pixelle-Video}"

echo "==> Installing Pixelle-Video to: $TARGET_DIR"

# --- git ---
command -v git >/dev/null 2>&1 || { echo "ERROR: git is required"; exit 1; }

# --- uv (Python package manager) ---
if ! command -v uv >/dev/null 2>&1; then
  echo "==> Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi
echo "==> uv $(uv --version | awk '{print $2}')"

# --- ffmpeg ---
if ! command -v ffmpeg >/dev/null 2>&1; then
  echo "==> Installing ffmpeg..."
  if command -v apt-get >/dev/null 2>&1; then
    (apt-get update && apt-get install -y ffmpeg) \
      || (sudo apt-get update && sudo apt-get install -y ffmpeg)
  elif command -v brew >/dev/null 2>&1; then
    brew install ffmpeg
  else
    echo "ERROR: install ffmpeg manually (https://ffmpeg.org/download.html)"; exit 1
  fi
fi
echo "==> $(ffmpeg -version | head -1)"

# --- clone ---
if [ -d "$TARGET_DIR/.git" ]; then
  echo "==> Repo already cloned; pulling latest..."
  git -C "$TARGET_DIR" pull --ff-only
else
  git clone --depth 1 "$REPO_URL" "$TARGET_DIR"
fi

cd "$TARGET_DIR"

# --- python deps ---
echo "==> Installing Python dependencies (uv sync)..."
uv sync

# --- default config ---
if [ ! -f config.yaml ] && [ -f config.example.yaml ]; then
  cp config.example.yaml config.yaml
  echo "==> Created config.yaml from config.example.yaml"
fi

echo ""
echo "✅ Pixelle-Video installed."
echo ""
echo "Start the web UI with:"
echo "  cd $TARGET_DIR && uv run streamlit run web/app.py"
echo "Then open http://localhost:8501 and configure your LLM / image / TTS providers."
