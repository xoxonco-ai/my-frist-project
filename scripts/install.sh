#!/usr/bin/env bash
# =============================================================================
# LiveTalking 一鍵安裝腳本 (install.sh)
# -----------------------------------------------------------------------------
# 用途：在「有 NVIDIA GPU 的 Linux 機器」上，從零把 LiveTalking 環境裝好。
# 官方建議環境：Ubuntu 24.04 / Python 3.12 / PyTorch 2.9.1 / CUDA 12.8
# GPU 需求：wav2lip256 建議 RTX 3060 以上；musetalk 建議 RTX 3080Ti 以上。
#
# 用法：
#   chmod +x install.sh
#   ./install.sh                # 用 venv 安裝 (預設)
#   USE_CONDA=1 ./install.sh     # 改用 conda 安裝
#   CUDA_TAG=cu121 ./install.sh  # 手動指定 CUDA 版本 (cu118/cu121/cu124/cu128)
# =============================================================================
set -euo pipefail

REPO_URL="https://github.com/lipku/LiveTalking.git"
PROJECT_DIR="${PROJECT_DIR:-$HOME/LiveTalking}"
PY_VER="${PY_VER:-3.12}"
TORCH_VER="2.9.1"
TV_VER="0.24.1"
TA_VER="2.9.1"

log()  { printf '\033[1;32m[INSTALL]\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m[WARN]\033[0m %s\n' "$*"; }
err()  { printf '\033[1;31m[ERROR]\033[0m %s\n' "$*" >&2; }

# -----------------------------------------------------------------------------
# 0. 檢查 GPU
# -----------------------------------------------------------------------------
if command -v nvidia-smi >/dev/null 2>&1; then
    log "偵測到 GPU："
    nvidia-smi --query-gpu=name,driver_version,memory.total --format=csv,noheader || true
else
    warn "找不到 nvidia-smi —— 這台機器可能沒有 NVIDIA GPU。"
    warn "LiveTalking 的即時推論需要 GPU，純 CPU 無法即時運作。"
    warn "若只是先把環境裝起來，可按 Enter 繼續；要中止請 Ctrl+C。"
    read -r _ || true
fi

# -----------------------------------------------------------------------------
# 1. 自動判斷 CUDA 版本 → 選 PyTorch wheel 的 index-url
# -----------------------------------------------------------------------------
if [ -z "${CUDA_TAG:-}" ]; then
    if command -v nvidia-smi >/dev/null 2>&1; then
        CUDA_RAW="$(nvidia-smi | grep -oE 'CUDA Version: [0-9]+\.[0-9]+' | grep -oE '[0-9]+\.[0-9]+' | head -1 || true)"
    fi
    case "${CUDA_RAW:-}" in
        12.8*|12.9*|13.*) CUDA_TAG="cu128" ;;
        12.4*|12.5*|12.6*|12.7*) CUDA_TAG="cu124" ;;
        12.1*|12.2*|12.3*) CUDA_TAG="cu121" ;;
        11.*)             CUDA_TAG="cu118" ;;
        *)                CUDA_TAG="cu128" ;;   # 預設跟官方一致
    esac
fi
log "使用 CUDA 標籤：${CUDA_TAG} (可用環境變數 CUDA_TAG 覆寫)"
TORCH_INDEX="https://download.pytorch.org/whl/${CUDA_TAG}"

# -----------------------------------------------------------------------------
# 2. 取得原始碼
# -----------------------------------------------------------------------------
if [ -d "$PROJECT_DIR/.git" ]; then
    log "專案已存在，執行 git pull：$PROJECT_DIR"
    git -C "$PROJECT_DIR" pull --ff-only || warn "git pull 失敗，沿用現有程式碼。"
else
    log "clone LiveTalking 到 $PROJECT_DIR"
    git clone "$REPO_URL" "$PROJECT_DIR"
fi
cd "$PROJECT_DIR"

# -----------------------------------------------------------------------------
# 3. 建立 Python 環境並安裝依賴
# -----------------------------------------------------------------------------
if [ "${USE_CONDA:-0}" = "1" ]; then
    command -v conda >/dev/null 2>&1 || { err "找不到 conda，請先安裝 Miniconda/Anaconda。"; exit 1; }
    # shellcheck disable=SC1091
    source "$(conda info --base)/etc/profile.d/conda.sh"
    if ! conda env list | grep -q '^livetalking '; then
        log "建立 conda 環境 livetalking (python=$PY_VER)"
        conda create -y -n livetalking "python=$PY_VER"
    fi
    conda activate livetalking
    PIP="pip"
else
    log "建立 venv (venv/)"
    python3 -m venv venv
    # shellcheck disable=SC1091
    source venv/bin/activate
    PIP="pip"
fi

log "升級 pip"
$PIP install --upgrade pip

log "安裝 PyTorch ${TORCH_VER} (${CUDA_TAG})"
$PIP install "torch==${TORCH_VER}" "torchvision==${TV_VER}" "torchaudio==${TA_VER}" --index-url "$TORCH_INDEX"

log "安裝 requirements.txt"
$PIP install -r requirements.txt

# -----------------------------------------------------------------------------
# 4. 建立模型與 avatar 目錄
# -----------------------------------------------------------------------------
mkdir -p models data/avatars
log "已建立 models/ 與 data/avatars/ 目錄"

# -----------------------------------------------------------------------------
# 5. 驗證安裝
# -----------------------------------------------------------------------------
log "驗證 import 與 CUDA："
python - <<'PY'
import torch
print("  torch      :", torch.__version__)
print("  cuda avail :", torch.cuda.is_available())
if torch.cuda.is_available():
    print("  gpu        :", torch.cuda.get_device_name(0))
import transformers, diffusers, aiortc, librosa  # noqa
print("  deps ok    : transformers / diffusers / aiortc / librosa 均可 import")
PY

# -----------------------------------------------------------------------------
# 6. 後續步驟說明
# -----------------------------------------------------------------------------
cat <<EOF

=============================================================================
✅ 依賴安裝完成。接下來手動做兩件事：

【下載模型權重】(二選一網盤)
  夸克網盤     : https://pan.quark.cn/s/83a750323ef0
  Google Drive : https://drive.google.com/drive/folders/1FOC_MD6wdogyyX_7V1d4NDIO7P9NlSAJ

【放置檔案 (wav2lip 範例)】
  1) wav2lip256.pth  ->  $PROJECT_DIR/models/wav2lip.pth   (記得改名!)
     mv /你的下載路徑/wav2lip256.pth models/wav2lip.pth
  2) 解壓 wav2lip256_avatar1.tar.gz 整個資料夾放到 data/avatars/
     tar -xzf /你的下載路徑/wav2lip256_avatar1.tar.gz -C data/avatars/

【啟動服務】
  # venv:   source venv/bin/activate
  # conda:  conda activate livetalking
  python app.py --transport webrtc --model wav2lip --avatar_id wav2lip256_avatar1

【開啟】瀏覽器開 http://伺服器IP:8010/index.html  (需開放 TCP:8010 與 UDP 埠)

官方文件：https://doc.livetalking.ai
=============================================================================
EOF
