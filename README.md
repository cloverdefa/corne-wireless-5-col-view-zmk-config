# Corne Wireless 5-Column View ZMK Config

這是給 **Corne Wireless、Nice!Nano v2** 使用的 ZMK 設定。鍵盤採用 5 列實體配置（`foostan_corne_5col_layout`），目前專注於 Windows，包含導航與符號層、滑鼠控制、藍牙管理、tmux 快捷鍵與多個啟動程式的巨集。

![Corne 鍵位圖](assets/corne.svg)

## 鍵位層

| 層 | 用途 |
| --- | --- |
| `Base` | QWERTY 預設層；拇指鍵配置 Alt/Esc、Symbols、Shift/Space、Ctrl/Enter、Nav/Backspace、Tab。 |
| `Nav` | 數字列、游標與頁面導航（Home/End/PgUp/PgDn）、音量與媒體控制，以及 Windows 快捷鍵（截圖、輸入法切換、視窗最大化/最小化、Windows Terminal、Zen 瀏覽器）。 |
| `Symbols` | 常用符號、括號、引號、`|`、`\`、`Del`，以及 tmux 快捷鍵。 |
| `Functions` | F1–F12、PowerToys Run、視窗移動、虛擬桌面、Windows Terminal (PowerShell)、設定等系統快捷鍵；同時啟用 `Nav` 與 `Symbols` 時由 conditional layer 自動啟用。 |
| `Mouse` | 指標移動、滾輪與滑鼠左/右/中鍵。 |
| `System` | ZMK Studio 解鎖、藍牙清除/選槽（0–4）、重設與進入 bootloader。 |

### 層切換方式

- `Base` 是唯一的基礎層。
- `Symbols`：按住左拇指的 `&mo Symbols`。
- `Nav`：按住右拇指的 `&lh Nav BSPC`（點按為 Backspace，按住為 `Nav`）。
- `Functions`：同時按住 `Symbols` 與 `Nav` 的拇指鍵（tri-layer）。
- `Mouse` / `System`：在 `Functions` 層使用 `&to Mouse`、`&to System` 進入，並以各層內的 `&to Base` 返回 `Base`。

詳細位置與綁定請看 `config/corne.keymap`，鍵位圖則列出各層配置。

### 拇指鍵 hold-tap

| 行為 | 綁定 | 點按 / 按住 | 設定 |
| --- | --- | --- | --- |
| `tm`（thumb_mods） | `&tm LALT ESC`、`&tm LSHFT SPACE` | 點按 Esc / Space，按住 Alt / Shift | `tap-preferred`，150 ms，`require-prior-idle-ms` 120 |
| `em`（enter_mod） | `&em LCTRL RET` | 點按 Enter，按住 Ctrl | `balanced`，200 ms |
| `lh`（layer_hold） | `&lh Nav BSPC` | 點按 Backspace，按住進入 `Nav` | `tap-preferred`，150 ms |

## 巨集與組合鍵

keymap 定義了以下巨集：

- **啟動程式**：
  - `zen`：透過 `Win + Alt + Space`（PowerToys Run）輸入 `zen` 啟動 Zen 瀏覽器
  - `twin`：`Ctrl + Win + T` 後輸入 `D` + `Enter`，啟動 Windows Terminal (Debian)
  - `twinp`：`Ctrl + Win + T` 後輸入 `P` + `Enter`，啟動 Windows Terminal（PowerShell）
  - `ptr`：`Win + Alt + Space`，開啟 PowerToys 命令選擇區
- **tmux**：`tmx` 先送出 prefix `Ctrl + A`，再送出參數按鍵（`W` 視窗列表、`|` 切欄、`-` 切列、`C` 建立新視窗）。
- **視窗管理**：`Alt + J` / `Alt + K` 移動視窗，`Alt + F4` 關閉視窗。
- **虛擬桌面**：`Win + Ctrl + D` 新增、`Win + Ctrl + F4` 關閉、`Win + Ctrl + ←/→` 切換。

部分巨集依賴主機端快捷鍵和應用程式設定（例如 PowerToys Run 的啟動快捷鍵、Windows Terminal 的快捷鍵與設定檔順序）。

### Combos

| Combo | 位置 | 輸出 | 判定時間 | 前置閒置 |
| --- | --- | --- | --- | --- |
| `combo_esc` | `Q` + `W`（位置 0、1） | `Esc` | 50 ms | 150 ms |
| `combo_control` | `Z` + `X`（位置 20、21） | `Ctrl` | 80 ms | 150 ms |

兩個組合鍵都只在 `Base` 層生效，不會在 `Symbols` 等其他層誤觸發。

## 硬體與韌體建置

`build.yaml` 定義兩個 Nice!Nano v2 建置目標（board 為 `nice_nano//zmk`）：

- `corne-left`：`corne_left` + `nice_view_adapter` + `nice_view`，並啟用 ZMK Studio（`studio-rpc-usb-uart` snippet 與 `-DCONFIG_ZMK_STUDIO=y`）
- `corne-right`：`corne_right` + `nice_view_adapter` + `nice_view`

兩個目標都包含 nice!view。ZMK Studio 僅在左半部的建置啟用；`System` 層提供 `&studio_unlock` 用來解鎖，`corne.conf` 中的 Studio 設定則預設為註解。

此 repo 提供給 ZMK 建置流程使用的 `build.yaml`，但 repo 本身未包含 GitHub Actions workflow。若已接上能讀取此建置矩陣的 CI，請在該 CI workflow run 下載 `corne-left`、`corne-right` artifacts；否則可依下方方式本機建置。

### 本機建置

需要安裝 ZMK 所需的 west、Zephyr/SDK 工具鏈。manifest 位於 `config/west.yml`，目前追蹤 ZMK `main` 分支（透過 `import: app/west.yml` 匯入 ZMK 的相依專案）。

在 repo 根目錄初始化並更新 west workspace：

```sh
west init -l config
west update
```

建置左半部（含 ZMK Studio）：

```sh
west build -s zmk/app -d build/left -b nice_nano//zmk -S studio-rpc-usb-uart -- \
  -DSHIELD="corne_left nice_view_adapter nice_view" \
  -DZMK_CONFIG="$PWD/config" \
  -DCONFIG_ZMK_STUDIO=y
```

建置右半部：

```sh
west build -s zmk/app -d build/right -b nice_nano//zmk -- \
  -DSHIELD="corne_right nice_view_adapter nice_view" \
  -DZMK_CONFIG="$PWD/config"
```

建置產物的位置依 west/Zephyr 版本與建置設定而異；請從各 build 目錄中取出對應的 `.uf2`，並燒錄至相應半部。

## 設定檔

- `config/corne.keymap`：實體配置選擇、6 個層、巨集、combos、hold-tap 行為及 conditional layers。
- `config/corne.conf`：藍牙連線參數、睡眠、按鍵 debounce、鍵盤名稱與 pointing 支援（詳見下表）。
- `config/west.yml`：west manifest，追蹤 ZMK `main`。
- `build.yaml`：左右半部及 nice!view 的建置矩陣。
- `main.py`：呼叫 `keymap` CLI 解析 keymap 並繪製 SVG。
- `assets/corne.svg`：產生的鍵位圖。

### `corne.conf` 重點

| 項目 | 設定 |
| --- | --- |
| 藍牙連線間隔 | `CONFIG_BT_PERIPHERAL_PREF_MIN_INT=12`、`CONFIG_BT_PERIPHERAL_PREF_MAX_INT=24`（平衡延遲與功耗） |
| 背景掃描 | `CONFIG_BT_BACKGROUND_SCAN_INTERVAL=512`、`CONFIG_BT_BACKGROUND_SCAN_WINDOW=36`（降低耗電） |
| 睡眠 | 啟用 `CONFIG_ZMK_SLEEP`，閒置 900000 ms（15 分鐘）後進入睡眠 |
| Debounce | 按下 3 ms、放開 5 ms |
| 鍵盤名稱 | `Corne-5` |
| Pointing | 啟用 `CONFIG_ZMK_POINTING`（供 `Mouse` 層使用） |
| 預設關閉（註解） | 高功率發射（`CONFIG_BT_CTLR_TX_PWR_PLUS_8`）、USB logging、`CONFIG_ZMK_STUDIO` 等開發選項，需要時再開啟 |

## 更新鍵位圖

安裝提供 `keymap` CLI 的 `keymap-drawer` 後，在 repo 根目錄執行：

```sh
python main.py
```

腳本會解析 `config/corne.keymap` 並更新鍵位圖 SVG，中間 YAML 檔案會在成功後刪除。

## 授權

本專案採用 MIT License，詳見 [LICENSE.md](LICENSE.md)。
