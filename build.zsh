#!/usr/bin/env zsh
# 以 Docker 在本地建置 ZMK 韌體，行為對應 GitHub Actions（讀取 build.yaml）
set -euo pipefail

cd "${0:A:h}"

# 映像 tag 請與 config/west.yml 釘住的 ZMK 版本對應
IMAGE="${ZMK_IMAGE:-zmkfirmware/zmk-build-arm:stable}"
OUT_DIR="firmware"
PRISTINE="${PRISTINE:-0}"   # PRISTINE=1 ./build.zsh 強制全新建置

mkdir -p "$OUT_DIR"

docker run --rm -i \
  --user "$(id -u):$(id -g)" \
  -e HOME=/tmp \
  -e PRISTINE="$PRISTINE" \
  -e GIT_CONFIG_COUNT=1 \
  -e GIT_CONFIG_KEY_0=safe.directory \
  -e GIT_CONFIG_VALUE_0='*' \
  -v "$PWD":/workspace -w /workspace \
  "$IMAGE" bash -s <<'INNER'
set -euo pipefail

[[ -d .west ]] || west init -l config
west update
west zephyr-export

python3 - <<'PY'
import os, shlex, shutil, subprocess, yaml

with open("build.yaml") as f:
    entries = yaml.safe_load(f)["include"]

for e in entries:
    board  = e["board"]
    shield = e.get("shield", "")
    name   = e.get("artifact-name") or f"{shield.replace(' ', '_')}-{board.replace('/', '_')}"
    bdir   = f"build/{name}"

    cmd = ["west", "build", "-s", "zmk/app", "-d", bdir, "-b", board]
    if os.environ.get("PRISTINE") == "1":
        cmd.append("-p")
    if e.get("snippet"):
        cmd += ["-S", e["snippet"]]
    cmd += ["--", "-DZMK_CONFIG=/workspace/config"]
    if shield:
        cmd.append(f"-DSHIELD={shield}")
    cmd += shlex.split(e.get("cmake-args", ""))

    print(f"\n==> 建置 {name}", flush=True)
    subprocess.run(cmd, check=True)
    shutil.copy(f"{bdir}/zephyr/zmk.uf2", f"firmware/{name}.uf2")
    print(f"    -> firmware/{name}.uf2")
PY
INNER

echo "\n完成，韌體位於 $OUT_DIR/"
ls -l "$OUT_DIR"
