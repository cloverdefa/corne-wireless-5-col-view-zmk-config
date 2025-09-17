# Repository Guidelines

本文件為本倉庫（Corne 無線 5 列視圖 ZMK 設定）的貢獻者指南。請保持變更最小且聚焦，並以可重現的方式驗證。

## 專案結構與模組
- `config/corne.keymap`：主要層（WinDef/MacDef/WinNav/MacNav/Code/Func/SYS）、combos 與巨集定義。
- `config/corne.conf`：藍牙/省電/去彈跳與（可選）ZMK Studio 設定。
- `config/west.yml`：ZMK 專案 manifest（目前固定 `zmk` v0.3）。
- `build.yaml`：CI 建置矩陣（left/right + nice!view；Studio snippet 預設註解，可視需求啟用）。
- `README.md`：使用說明與層概覽。

## 建置、測試與開發
前置：安裝 Zephyr SDK/West，並以此倉庫作為 config。

```bash
west init -l config && west update
# 左半
west build -s zmk/app -d build/left -b nice_nano_v2 -- \
  -DSHIELD="corne_left nice_view_adapter nice_view" \
  -DZMK_CONFIG=$PWD/config
west flash -d build/left
# 右半
west build -s zmk/app -d build/right -b nice_nano_v2 -- \
  -DSHIELD="corne_right nice_view_adapter nice_view" \
  -DZMK_CONFIG=$PWD/config
west flash -d build/right
```
說明：以上指令會建置左右半並啟用 nice!view，使用本倉庫的 `config/`。若需啟用 ZMK Studio，請於兩側指令尾端加入 `-DSNIPPET=studio-rpc-usb-uart`。

## 程式風格與命名
- Devicetree/DTS：4 空白縮排；保持 10 鍵列對齊，易讀優先。
- 層節點：`<Name>_layer`（例：`WinDef_layer`），並提供 `label` 與 `display-name`。
- 巨集/行為標籤：snake_case（例：`ter_win`, `max_mac`）。
- `.conf`：一行一個 `CONFIG_*`，必要註解緊隨其後。

## 測試指南
- 建置兩側皆需成功，燒錄後驗證：
  - 層切換：`Code`/`Func`/`SYS`（`&mo`, `&to`）。
  - 巨集：`ter_win`、`ter_mac`、`max_mac`、`rec_mac`。
  - 藍牙：`&bt BT_SEL n`、`&bt BT_CLR`；喚醒/睡眠（`CONFIG_ZMK_IDLE_SLEEP_TIMEOUT`）。
  - 顯示：nice!view 正常刷新。

## Commit 與 PR 規範
- 建議採用 Conventional Commits：`feat:`, `fix:`, `refactor:`, `build:`, `ci:` 等；可用範圍：`keymap`, `conf`, `ci`。
- Commit 內容專注單一更動，避免泛用訊息（如「GIT COMMIT MESSAGE」）。
- PR 需包含：
  - 變更摘要與動機、相關 Issue 連結。
  - 重要片段（前/後）或鍵位圖截圖。
  - 本地驗證步驟與結果（左右半皆可建置/燒錄）。

## 安全與設定提示（可選）
- 勿提交個人配對資料；變更 `west.yml` 版本需說明理由。
- `CONFIG_ZMK_STUDIO_LOCKING` 調整請審慎評估以免影響 Studio 使用。
